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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70832e9b-c658-36bb-a095-0369a0b34de9 | -2.614 | -54.33212 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58102192-4e9d-38e3-b07d-612cdee39d6e | -2.64449 | -59.76937 | 2024-11-18 05:29:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7111391-2cfa-3075-b3b9-a16d2b811708 | -3.46941 | -49.9741 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9954731-e6e2-3b14-9e0b-03d4bb72f551 | -2.19543 | -53.66846 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8358e8fe-2d3f-38e5-b8c6-af074f71915f | -3.58774 | -53.77599 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a440e2-e8f0-35ae-8fc9-a6243e5260b3 | -3.56239 | -50.24434 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dde47e5-0336-3b6c-90d8-9035d406c935 | -12.54953 | -57.82661 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4b6c1af-c746-30b7-94a2-7c67c89c7a8e | -3.56694 | -50.25243 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2addae97-9b42-3153-bce2-e66d4d58e4a2 | -2.52499 | -54.8774 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f52b2019-249f-309c-9b56-77c07a52f4bf | -2.19467 | -53.67352 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b6c21fe-91e7-38a2-b307-bf1452fed3a2 | -3.04733 | -54.40099 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00be99e9-be75-3a26-8bcf-f5f7c0d58497 | -4.08027 | -54.89607 | 2024-11-18 05:29:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff9e0960-4f40-3e3a-b5fd-001ab2e00785 | -12.57462 | -57.76676 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50780260-ee54-362b-b045-cf80adb73199 | -3.34087 | -53.30711 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57f13f20-e839-34d4-821e-9bd1c1d68a45 | -3.03182 | -54.10475 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7a1dc4f-1d7e-3b81-9354-6fdc97dd0342 | -2.61083 | -54.54057 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42aeed6b-f9d9-3d03-9653-4e48ce1f99f8 | -3.06492 | -54.40866 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71f6c107-440c-3986-ad2d-929e16ea8426 | -3.05576 | -54.40728 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ebefab6f-92d8-33ef-b086-3da548c69f20 | -14.28839 | -57.63721 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbdc4584-6e47-3bb8-9698-765d34fbf8e7 | -12.57828 | -57.77128 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a51e02cc-fd22-3fca-b341-0e61148ec49d | -3.08288 | -54.65832 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 917b1bc1-c3de-3b8c-a06e-1cd8a7dec67d | -3.76822 | -50.15953 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f75a9be-61cf-3884-98a2-d04f511e43f4 | -3.57333 | -50.25501 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 51a72f00-46b2-37c7-8f3a-8fd1c77eba36 | -2.61152 | -54.53598 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b01a7d7-d717-322a-b7fe-04c7db0854e3 | -3.7737 | -50.16496 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01a19683-e102-3b55-9ad4-0862e151efed | -3.52896 | -50.25618 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cab8d95d-2399-3fb4-8e12-bcd7d2dadc10 | -3.59255 | -53.7768 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d31f656a-c1d3-30e4-a164-db400b2def95 | -3.51405 | -50.23045 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 41a2e595-d8ab-34ab-8b95-1c9fd9faa97b | -2.52434 | -54.88157 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f27ee626-f2fa-3aa6-ac15-c25866ed5a1a | -2.58564 | -51.71803 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 243e2508-7590-3644-a7a8-022505b36e79 | -3.76376 | -52.1445 | 2024-11-18 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57514591-10c1-3e7f-b2ae-ec1d9bda6c1e | -3.52928 | -50.25793 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 128cfe19-778b-3e11-9808-7ab30915e442 | -3.31129 | -53.3706 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c400bcc9-6f90-3607-b5fe-a269658421a1 | -3.05405 | -47.99935 | 2024-11-18 05:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52fdcd7-43f5-3c47-8374-dffe09b872d5 | -3.04664 | -54.40566 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07279d97-a3b1-3981-b7c3-dd14a5706449 | -2.57936 | -51.72158 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d27b9ef-1d09-34fa-9a27-b85ec483617f | -3.33139 | -50.50105 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e787c853-8959-3277-8a4d-0ecc8a673dfa | -3.33736 | -50.50205 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 337b8d52-79e0-39ad-89dd-c726811c820a | -3.74316 | -54.65427 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a58e679-7f84-3a07-bb15-37b1bfb74e63 | -3.18639 | -53.24659 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9db1f1c-1c37-3c25-9f17-ca3dc4b27903 | -3.58247 | -53.72419 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ee08fca1-7d25-3800-b9fc-bca04e7ae4b3 | -3.068 | -53.28479 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f5777d5-77c5-3a11-88cc-cc86584eed18 | -3.69417 | -50.11611 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a099dbff-7463-3da7-8744-ec9de0c2bcb9 | -3.53345 | -54.49271 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21c103df-9a62-315c-b58a-b91da9a327aa | -2.19695 | -53.65827 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7456ef-05ee-3e3f-91fc-67f3124665a7 | -3.69292 | -50.11456 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6280345-a124-3ac6-96d7-4b54edd39062 | -2.20018 | -53.66919 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f2f168a2-8bf6-332d-b80f-9197907e39e4 | -3.338 | -50.49771 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b534fba6-3222-3240-9d77-72a156a22d39 | -3.14445 | -52.97678 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7383d3b2-a2c2-3206-986a-edf7eebddfaa | -2.36955 | -53.67545 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23564c88-f2eb-3fd3-8f8b-4000779530ee | -2.19611 | -53.66032 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b23167c8-dbfc-3e5a-abdf-c3b1601dcb26 | -3.74114 | -52.03408 | 2024-11-18 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2560dbc-ca28-322c-91ba-51eae12b2a88 | -4.1143 | -51.0485 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d064486-a412-30e3-a1e6-5bff77f459e2 | -3.30997 | -53.36935 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ddf5cf2-b846-3ed1-9bc7-da5be26da55f | -2.13318 | -52.07482 | 2024-11-18 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e3f7350-7575-329f-85d9-ac6ed9b186ec | -2.28896 | -53.63055 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b37b3d0a-2000-3752-9c67-6e9ed0152d39 | -3.54968 | -54.57336 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 096388fb-16f5-3159-96cd-9d7076bb6634 | -14.28894 | -57.63289 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7834b51a-5a66-3bab-8a71-754beb1b2fb6 | -1.80077 | -54.03455 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6d3a1f7-e1cc-3a11-85e4-b226be2923d7 | -3.45975 | -50.0103 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 949b7c9c-f69a-336f-b444-8eacc2771d4e | -3.34463 | -50.49423 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ac9d44-cc3c-36b3-a6c6-8320c750b7ce | -3.10541 | -53.74682 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34d6a818-3c48-35fc-8632-b80b57d8bfd3 | -3.08219 | -54.66282 | 2024-11-18 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a5e740b-3e42-30ca-b5b7-0fa7b135da1e | -3.74658 | -54.71767 | 2024-11-18 05:29:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71058a72-0450-33ee-88a0-f11525169748 | -14.28461 | -57.63226 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4de322df-430a-3713-9759-de55652a25b4 | -1.69766 | -54.12465 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4245e81b-99c3-3153-ae56-6a5da1edf2a3 | -2.19619 | -53.6634 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f95706b8-26c0-3074-a094-584afb1e219b | -3.5134 | -50.2349 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 52987510-6815-37c7-a6ba-e522545b8654 | -14.29273 | -57.63775 | 2024-11-18 05:29:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f951679-a201-3396-bfa3-6bd080e23527 | -4.27357 | -50.88716 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f5303fc-10f8-3fb1-9567-fb3dd715f607 | -4.26732 | -50.67768 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 995b342f-7b1f-305c-9cde-32149fe2a982 | -12.5537 | -57.82724 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e9107c3-f3d5-3e40-be37-f78b7fb99b58 | -3.06478 | -53.27263 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e63f9a8-7a37-3f6f-9e63-e9ed7e9f17de | -3.18139 | -53.24602 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd5821cf-13ff-399d-96d6-5052fd9dbc97 | -2.57882 | -51.72508 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 844f8f5a-2cf2-3ca2-83b0-f3cb3a58be22 | -3.30714 | -53.36444 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58ed4041-d268-398f-abd0-a515901722b7 | -3.47159 | -49.97337 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e751cd4d-de29-32ff-8703-67ab5d961d22 | -3.53056 | -50.24893 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5d2f2d7-2a90-37ed-b3ce-2a67f84c5e3e | -3.58408 | -50.51994 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c796daea-23b9-35e5-83dc-9cd6517acc79 | -2.20095 | -53.66407 | 2024-11-18 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45fbf08f-c8ba-354b-a45a-305a0aee2d95 | -12.55942 | -57.8163 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f05c7867-fd28-309b-bb96-dae2bf658b47 | -1.62188 | -55.14252 | 2024-11-18 05:29:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fccc254a-38ac-3257-9102-97b7df51fb4e | -3.31402 | -54.17728 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37fc4efa-8e0b-32e3-ad28-352205103d51 | -3.33864 | -50.4933 | 2024-11-18 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a7c68a89-e307-3b3e-b43b-ea375b991999 | -12.55421 | -57.82344 | 2024-11-18 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa349b50-f4ef-3fa4-960a-fb86dd856447 | -3.58505 | -53.72702 | 2024-11-18 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d4e3f13-d6b6-3bab-8c3d-1c631241d684 | -3.57945 | -50.25585 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b410959-4154-389b-9baf-337d65a51aad | -3.5615 | -50.24717 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49d94140-548c-3394-97ef-96bc79524b1d | -3.26321 | -51.61396 | 2024-11-18 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33614b7c-182a-371b-8645-d5ab64ea8207 | -3.76428 | -52.141 | 2024-11-18 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 778a4934-7560-3f18-976e-1750607e4117 | -1.80155 | -54.02962 | 2024-11-18 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 888a91e3-35e8-3c2a-b5ce-ec12f9ebe6e5 | -4.27332 | -50.67855 | 2024-11-18 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 005de963-6a08-350c-8739-6d9d077447cd | -3.58342 | -50.52435 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7315afb0-d176-3e6d-a45f-966dea5350f4 | -3.56013 | -50.25621 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b713f09-3423-30d3-813c-b7475ecd106d | -2.61994 | -54.32351 | 2024-11-18 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9808b5ef-1277-33be-adb1-34dd70b4300a | -3.34005 | -53.31261 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8ae4abf-bc64-3f7b-bf1c-de217c0910b3 | -3.68799 | -50.11523 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e54f2d32-84bc-3933-a41c-9477f01102cf | -3.62824 | -50.22121 | 2024-11-18 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e9e372-7a74-3cc0-8a20-a8169f4e9897 | -3.34582 | -53.30793 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a06cc5aa-064e-3654-9168-a22d2d983f4e | -3.38726 | -53.26864 | 2024-11-18 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README42.md)
