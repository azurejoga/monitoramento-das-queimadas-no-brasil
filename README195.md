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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dc1276c-fef8-3a23-b912-cdc48446dead | -16.8604 | -55.86337 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7b66a1b-f486-3aed-9095-8032e930c27b | -16.85982 | -55.86731 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 64b5f938-17d0-33a5-885c-b2672f198ca9 | -16.85751 | -55.88309 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c993dba5-cb10-34fa-9cbd-0c8e93ebe117 | -17.96644 | -56.47328 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 848d24b2-67bc-321e-92e7-bf48a43e0d48 | -18.13669 | -56.38291 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ca75f865-6e61-3e2e-a750-61d4ae5c9261 | -18.13325 | -56.38236 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1731d3db-16ad-37da-a6cb-a6b9001930ba | -18.13269 | -56.38627 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 28970ff1-1cf1-3e24-a5eb-6f6c54d563bf | -18.12981 | -56.38181 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 16c8b542-cf8b-3342-a074-a8fde09e47f7 | -18.12925 | -56.38572 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2cb677e2-737f-39cf-8f74-fb9690e0ac03 | -18.12869 | -56.38963 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 115a9696-2624-3ecc-81b0-36ab5d0c9ff3 | -18.12812 | -56.39354 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 760064b9-9015-3af1-8446-030bbd6fc220 | -18.12625 | -56.3858 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 81db6ac5-ad83-3d8e-8933-718d941ceb85 | -18.12582 | -56.38517 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fa40dcfc-4cf4-3023-a68e-8baa5ab6341a | -18.12412 | -56.39691 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4e02090f-885b-3b55-8bc0-2c294c17aa93 | -18.12282 | -56.38525 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b8ba9600-4dfe-314c-86cc-7a4b86e1fdae | -18.12224 | -56.38916 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f50fe84b-bc64-3c19-8c0a-f387d4fa8f45 | -18.12166 | -56.39306 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5e05b650-3e7c-394f-954f-c162510262e5 | -18.12108 | -56.39697 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 5c1b0e11-93a2-30f6-8429-14538d4c4852 | -18.1188 | -56.38861 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d9435512-1e32-39f8-88ec-962c20bcd4c7 | -18.11823 | -56.39252 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8b70dc06-2a07-3704-9f67-dff0fee428f3 | -18.11765 | -56.39642 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c2db8b80-c6c3-3718-8cc7-100fd285447b | -18.11537 | -56.38807 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2393bab0-4041-3693-87f8-96ba06fcb2e8 | -18.11479 | -56.39197 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 14142fe3-93bb-303e-8a1f-2799fe2b79a5 | -18.11422 | -56.39587 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| aab305ef-c3d2-368f-a04e-1bfc93a7a76b | -18.11364 | -56.39978 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 55ffd480-de48-326f-ae6a-11d31b2d0381 | -18.11136 | -56.39142 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 66d09bfb-0a6d-3801-bb2d-7c3f0a33b248 | -18.11078 | -56.39533 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 53e9cbc9-8c2b-39bb-9346-88b75a5489de | -18.1102 | -56.39923 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f93ce401-d1f6-3b5c-9a91-a7f569e5c664 | -18.10735 | -56.39478 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6db8a209-f4ea-3fdb-a394-cb76930d7def | -18.10677 | -56.39868 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| dec60746-c902-3a99-8c28-25cafbb5d822 | -18.10278 | -56.37807 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f92146c7-ac5b-3570-b39d-c18511801dc5 | -18.09992 | -56.37361 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fedabb70-311e-3db5-a010-0c1f13898c9e | -18.09935 | -56.37752 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dc53e1bb-9f28-35ae-ae26-845f6a2c0998 | -18.09877 | -56.38142 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aad46254-e407-37f9-a73b-9fd9fc850565 | -18.09591 | -56.37697 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0b9a4832-3fee-3b3c-9902-ab47a4edc76f | -18.09534 | -56.38087 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ab145fda-a304-3cdf-b7ab-898050fd812e | -16.6234 | -57.1069 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 50d39e69-bc7f-3bdd-bc13-96e79597502f | -16.62229 | -57.1142 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0a3e0855-f51e-31a8-926c-3350c31c8159 | -16.61895 | -57.11366 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 124732d8-9efc-3b2d-8048-c7aa6a76dcb7 | -16.60396 | -57.14488 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 43d1f9a6-454b-3602-bb50-69cb03406ba3 | -16.60154 | -57.14485 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 80c681aa-fa4c-3d30-93f4-31a1e035f79b | -16.58293 | -57.46147 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ae2003f1-087a-3aab-ac41-56de8b6d7652 | -16.44262 | -57.33847 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f581fa9a-8e66-379a-b913-96fa551612ce | -16.43873 | -57.34153 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 095d3721-8325-35e1-be12-f33cb89e1d79 | -16.4332 | -57.33321 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c35941d4-137a-3747-a536-44cb1d78a106 | -16.42987 | -57.33266 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ec8abd50-adde-3614-8fa0-1f379031a9ef | -16.4271 | -57.3285 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 109fe78a-f108-3a46-a9e3-f4111ef88211 | -16.42655 | -57.33212 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b05fda42-30ac-3730-a019-e75786d37b0c | -16.42322 | -57.33157 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b70f9642-9c23-3b6a-ac39-f2d9056fd0dc | -16.42045 | -57.32741 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d7888d66-9faa-3a85-bced-2d9749df5856 | -16.44152 | -57.32345 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b09e84b3-9868-3261-a459-d4cfb2c3a3e2 | -16.43652 | -57.33376 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 97d19d1f-6d44-3bfa-acd1-e3d8581970e4 | -16.43043 | -57.32904 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4d870812-adbd-3dd9-9eaf-4348b099f488 | -16.42267 | -57.33519 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d5a9a863-4984-31e8-9a41-5a592c59c6e0 | -16.41713 | -57.32686 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ae673837-e23a-3a63-bb6a-137a9c4b82da | -16.394 | -57.69632 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3da49786-36c5-388d-9a21-d80bf7759e3a | -16.39344 | -57.69991 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7457c84f-4081-3af1-93e2-9a52dcd464bb | -16.39289 | -57.7035 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 70bd96c3-a0d3-34fc-a957-fffacf72f9d3 | -16.39069 | -57.69576 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 09509e9e-7550-3eef-b6a3-3018e59d77b7 | -16.39013 | -57.69936 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dec48b80-1cb6-3bce-ad22-022b34ccb80e | -16.38957 | -57.70294 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d0d9fa04-86f1-3e5a-8fd8-c1d5d66517a7 | -16.38626 | -57.70239 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a3b6b23c-29d0-31a9-b826-9a93942a1f4a | -16.38514 | -57.70956 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8a88db01-be2e-3e11-a758-05a86bbd80ba | -16.38239 | -57.70543 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f301b689-0eef-355c-b99f-377b7751be02 | -16.38183 | -57.70902 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a167a14-8621-3cc4-8cf2-3c485985b80b | -16.38127 | -57.7126 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5c48fe0e-a73f-322f-8c52-b2b05f16bce4 | -16.37852 | -57.70847 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 41a7a6f9-729d-307e-8019-2c28755e63d5 | -16.37521 | -57.70791 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 49c1bced-00fc-3ddd-a3b7-dc25e6f2c569 | -16.37245 | -57.70377 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66dab4f1-e1c2-37ee-a5bc-ae030319ddb8 | -16.37189 | -57.70737 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9592e657-0ab8-3076-a87a-e9b280552e00 | -16.16192 | -57.4191 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 096a1e5f-d9e1-3aa2-a7f6-df93b437fd91 | -16.15403 | -57.60194 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a99bb007-b7ba-3586-801b-ca5257473d19 | -16.15072 | -57.60139 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6c8f9c76-d979-3889-91ee-0a2d94ec4636 | -16.14465 | -57.59673 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b4c5d9ac-6587-3339-a79a-d49e681de218 | -16.14133 | -57.59616 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3bbefbfb-82a5-30d0-b5ef-5d777fea1ac1 | -16.13981 | -57.40801 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcb0267c-969e-35cc-a91e-c77a9bf23163 | -16.13032 | -57.55763 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0dd012a0-2e26-3669-9b52-d250074dfda5 | -16.12589 | -57.56426 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a6f46747-05f6-31e3-8602-7c214f53c39a | -16.12534 | -57.56781 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| df707acd-b80a-3c2e-88c6-582bb6308bce | -16.12258 | -57.56371 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 922d2796-dc25-3285-810d-19311736fef5 | -16.11872 | -57.56671 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dfd8419e-0d99-3f12-be32-1628de6fb3b3 | -15.8718 | -57.47461 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa974ae-9102-3903-a551-5d3b07868c37 | -15.68937 | -57.66448 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6791265b-934d-3cfe-8def-2efda33d0e29 | -15.6682 | -57.38659 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afe95a88-75be-399c-86e9-8843b93cf7ef | -15.661 | -57.38916 | 2024-10-09 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b67d39-65ff-386d-853f-94fee1ac630d | -16.56437 | -57.73563 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 10d3e890-8e0e-3a5c-a9a9-b9780e5b3aad | -16.56161 | -57.73148 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c9932b31-4578-3c86-8c36-1c862efb55d4 | -16.56106 | -57.73508 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3b5c3a99-30b3-30a1-a6bf-d951a8b2ab21 | -16.55994 | -57.74226 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 235f656c-2a8f-3c8e-a34a-3cece84de17f | -16.55938 | -57.74585 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a1253337-890e-32d9-80c3-37760ee0e026 | -16.5583 | -57.73093 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b1bf5534-5a89-3c78-90f6-6d9b9a8b3ac3 | -16.55774 | -57.73453 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 70d9abce-9e5d-3d17-a251-eeaea5dcf5a6 | -16.55663 | -57.74171 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7e93f279-4139-3ef4-a776-df09c95f629f | -16.55607 | -57.7453 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1c1f1487-dc57-3752-b2d5-78f4d995cec6 | -16.55499 | -57.73038 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f16da725-27e1-3fa1-9d1b-999541423802 | -16.55446 | -57.71188 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d4eea3fd-8f7d-3061-859a-e6bf788cd4dd | -16.55443 | -57.73398 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30703dd9-4218-338d-893f-7a910200f9ec | -16.55331 | -57.74117 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 48bf5d5b-34e1-3001-b372-fb4f752246cc | -16.55276 | -57.74475 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9ed43338-bd8a-39ba-8e51-c8d0ae2f5b83 | -16.55112 | -57.73343 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README196.md)
