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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc4eb20e-5eac-3db9-b1a8-816b1ffb7618 | -9.8821 | -44.8402 | 2026-10-06 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 2dbc95c8-6dd8-30a9-a2d0-04f16eda8fc1 | -9.256 | -67.6438 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 26bf382f-35b6-352e-b10a-35382d97d919 | -6.4279 | -43.4686 | 2026-10-06 18:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ee9e5ddb-6ecc-3d3c-bb95-df3e1b1e8235 | -9.1257 | -67.8322 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 88ae3297-6a42-3a2c-9aa5-4a6271ccc8c7 | -5.1017 | -42.9167 | 2026-10-06 18:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d3ed9393-b5f1-32a2-b3b1-1b0f8d720f06 | -6.4903 | -62.8554 | 2026-10-06 18:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| fa4d14e4-1ef6-329c-9c04-897b972c3e79 | -9.1068 | -67.9437 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| e23ef6f0-484a-3558-b446-1a916f352751 | -6.8955 | -43.6601 | 2026-10-06 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 43157da4-0278-34d7-9a05-47afab299f1c | -8.5554 | -66.9759 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 20a29c08-843b-3b8b-a235-13118a438599 | -3.342 | -43.3901 | 2026-10-06 18:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 246dec37-16ff-37d8-85d7-f65c4e144f4b | -9.5151 | -67.7484 | 2026-10-06 18:40:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f329497a-dc14-363f-a013-1135ade93fa2 | -6.8764 | -43.685 | 2026-10-06 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 9f22f560-f136-391e-bf24-ae631afc7bf8 | -3.3923 | -44.4695 | 2026-10-06 18:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 864a0709-6a4c-3c82-99f9-9477ca2bda2b | -5.7376 | -45.1533 | 2026-10-06 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1065.5 |
| e90e9e80-5ad1-33e7-95c1-1a1ea9e6bba0 | -9.124 | -68.313 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e14779a1-cd32-33f1-a20f-2fde9861bd0e | -11.8296 | -44.688 | 2026-10-06 18:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 79f21a85-4d4c-3978-b20d-88cbe0a0179d | -9.8824 | -44.8171 | 2026-10-06 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 398.2 |
| cf91280e-852e-3db6-92cd-dd18f3c6d49a | -11.8315 | -43.5391 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 76ca297f-65d8-3e71-93b3-96eb1242fd64 | -9.2365 | -67.9035 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 136afe38-ff76-37bc-8cbd-df92878031f2 | -9.3431 | -64.7143 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.0 |
| acca4b0c-5de5-3843-a7f9-e6f941a2c794 | -6.8952 | -43.6833 | 2026-10-06 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ddfe3b9d-dd74-3364-86e0-c9654a629047 | -7.8604 | -72.4587 | 2026-10-06 18:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1d255974-14b9-3bb0-ad86-17f60bc2a91c | -9.0892 | -67.685 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 259.9 |
| 4e3bbebb-9086-3ec0-87ab-8725a590286e | -9.6049 | -68.5979 | 2026-10-06 18:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 079904d0-7eb5-3855-abb3-3fa127a65ddb | -9.0705 | -67.741 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 0df2cd47-7c94-3f76-8e23-77150a8085fd | -9.4751 | -64.3336 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 0ff61d3b-095a-3b5c-b5ef-4956de17e6fc | -9.1077 | -67.6845 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| a7b04301-0652-3e67-867e-7dc3e9b4198c | -11.6378 | -43.6403 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 04a19c8e-33ca-3243-8a61-33b52e6625a3 | -9.7318 | -64.9818 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 43f8ed9f-9325-3ed0-9cce-2dfdb117c3c1 | -4.1574 | -44.2726 | 2026-10-06 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f1b8200e-b2ae-3057-89cb-fdcfa680df27 | -4.8081 | -42.1577 | 2026-10-06 18:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| f08939de-836d-3f7a-aae0-c06d60f3e5e5 | -5.496 | -42.8178 | 2026-10-06 18:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 76fd70a6-9df4-3281-ba0a-2b5b088568fa | -11.2267 | -45.2604 | 2026-10-06 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2f5db272-d59a-361b-9839-b6172b9c408a | 2.4585 | -50.8299 | 2026-10-06 18:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b4b1470b-3d6a-332b-a7d9-a41d8e1c7a1f | -9.2366 | -67.885 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 1258986f-1e74-347e-9afe-39ed4d9105dd | -11.6951 | -43.655 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| c8a3d0fa-f8b0-36be-a0ee-73fbeb20f2fc | -11.4507 | -43.3854 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| bebc9d86-bd8d-3898-9cd3-ac9da6433051 | -11.8311 | -43.5628 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 05d2a237-b261-367a-892a-6a7df1551d29 | -8.9257 | -66.8549 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 08aa7085-7ad4-38f1-aee3-97c4497d0f1d | -9.1072 | -67.8326 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| c8e957d7-00ab-3174-8707-634b50c7d973 | -8.9188 | -68.8527 | 2026-10-06 18:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 9ea8042c-078c-3653-9ddc-cdb4e86e4ee7 | -7.8167 | -45.3193 | 2026-10-06 18:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 322.1 |
| 4fc7edf6-8443-3b4f-97c8-a800ed879066 | -8.2495 | -70.8289 | 2026-10-06 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 114.6 |
| faf8b1b4-e14b-315d-b26d-9b7e2e07e8b5 | -8.7707 | -68.9478 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| cf6eff32-cfd4-3eda-9f39-66df61cd4719 | -5.7378 | -45.1307 | 2026-10-06 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 16cfa9e6-5357-3896-8a02-4d28fa9db53a | -7.6074 | -42.3667 | 2026-10-06 18:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 91789319-f694-327a-b32e-0b34aa9dbc1b | -9.0705 | -67.7225 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 6ffa26fd-cd40-308b-8f28-8ea0a8d77817 | -11.8216 | -47.3521 | 2026-10-06 18:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2ddca7a4-af18-38c0-9cdf-c72cbafedd7a | -7.5332 | -70.0331 | 2026-10-06 18:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 54cd8b28-ce12-375f-854a-ca91a21b4598 | -5.9838 | -40.9123 | 2026-10-06 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 204.8 |
| 719445b6-7ab2-3b90-9dde-6e24703b437a | -8.9258 | -66.8364 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 00a732a4-5002-39fe-8e19-27d9a44a5223 | -4.123 | -46.834 | 2026-10-06 18:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 435.4 |
| d2e29aa8-4d9e-34a7-a902-85a5ed48d3fc | -8.7324 | -69.4271 | 2026-10-06 18:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c98f5416-123e-3393-bfd9-622805190c8e | -6.3304 | -43.8253 | 2026-10-06 18:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c872f9e1-054b-379b-9445-489ab3548bb2 | -9.1885 | -66.0102 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 2b3ce2fa-1e0b-3139-a076-dc06d3e65b85 | -11.6374 | -43.664 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 59bec067-e3e9-3c06-a9d0-43a26496ab40 | -9.256 | -67.6438 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 4e7caa4e-34f8-38ec-92f3-008f87a311c5 | -9.0892 | -67.6665 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| f3520e05-73d7-3e66-a9a0-23df05920e77 | -6.914 | -43.6816 | 2026-10-06 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f21131ac-1ee6-316e-ab8d-f9ee24a55f06 | -3.0461 | -65.0844 | 2026-10-06 18:40:00 | GOES-19 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 8d6fdefd-2db9-3cf5-b2ad-7ffc021272f8 | -9.8844 | -64.2802 | 2026-10-06 18:40:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 7a906ca1-1c28-30e0-8cf9-4cb868036d56 | -9.1055 | -68.3135 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d8dca9c2-db4a-3657-8b17-29efae353ab5 | -3.292 | -42.2673 | 2026-10-06 18:40:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| f7248d75-9e08-30cc-9c80-60af58cf1793 | -3.3793 | -43.3884 | 2026-10-06 18:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f0ae250d-6cea-3688-9f37-2770b0b0f347 | -9.8828 | -44.794 | 2026-10-06 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e4b408eb-6c9c-3c60-aad6-b3dd109b70f8 | -8.537 | -66.9764 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.8 |
| c6b94d52-fac4-3abd-b7e0-9a773bff6c0b | -9.5468 | -64.8196 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 328.6 |
| cf61bdfb-64cd-3aa2-9c69-333ffacbc1ae | -7.0345 | -71.7545 | 2026-10-06 18:40:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 00b93951-8a70-3f87-bea8-ad4acd1ecfbb | -8.5368 | -67.0135 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| dae79ab8-d3fb-33b0-9e4b-66d1a2391545 | 3.5079 | -51.2784 | 2026-10-06 18:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 0c684e5c-85fd-3096-8f6c-164f55a7dca5 | -9.1068 | -67.9437 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 5575e309-ab37-3462-92cf-f6aa97d12e38 | -11.6946 | -43.6787 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 2b1dc0f7-865a-3451-b8c3-5dc150a691e2 | -3.3606 | -43.4125 | 2026-10-06 18:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 6f80eccd-a209-365d-b7cf-c70e2fc57725 | -3.3607 | -43.3893 | 2026-10-06 18:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 394.2 |
| 58871f61-f799-37c2-b9ce-a11a5413ffbc | 1.7304 | -55.6259 | 2026-10-06 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 45edaf76-d491-3bc9-8b3a-84027bd7c077 | -6.6217 | -37.8923 | 2026-10-06 18:40:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 9f7a7f34-2106-37c3-99fb-b1198fa681d2 | -6.4091 | -43.4702 | 2026-10-06 18:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| cb270968-2120-3337-b431-682d18fffe13 | -9.4633 | -66.7842 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| bfcfb162-1ce2-3e08-9266-95b0bd8656fa | -9.3263 | -68.7519 | 2026-10-06 18:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 106.8 |
| fdeaaa15-1d25-353f-a6c9-9e4f4ee173a6 | -9.8634 | -44.8195 | 2026-10-06 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| bf96df9d-a81f-3c55-b704-39c9aede70de | -3.3921 | -44.4923 | 2026-10-06 18:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6214943e-8bc6-3d78-ac38-495053f67f47 | -9.5469 | -64.8008 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 163.0 |
| cfaf3cda-cee6-3530-90de-3250d097d5ee | -9.1257 | -67.8322 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 8d2bd339-0906-3824-ae9f-45e9db323052 | -7.5657 | -73.0437 | 2026-10-06 18:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 3ab76f40-c48d-3f26-a8d4-f734643dbbbf | -9.7317 | -65.0006 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 913a7c2e-9692-38c1-9c9b-59a06070f1e4 | -11.7143 | -43.652 | 2026-10-06 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8ce4a5d4-c225-3d05-8507-f865ca19ab32 | -3.7811 | -41.7675 | 2026-10-06 18:40:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 649fedf5-f1c8-32f5-8add-e8d24a68e9c5 | -9.5006 | -66.7459 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 2115be8d-fe45-33ba-ba2b-d8b94e7a9a9e | -6.0266 | -42.2792 | 2026-10-06 18:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 49ccffc8-543d-3588-84d4-fd85de3d0069 | -5.4174 | -39.1062 | 2026-10-06 18:40:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 75b2804f-2ad2-33fe-b08f-1bbc8b92297c | 3.5263 | -51.2778 | 2026-10-06 18:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5a4fed39-a5f4-31ef-9ff1-96a1c6a2dd2c | -6.6312 | -43.7765 | 2026-10-06 18:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 5cef630c-3d1f-3734-a8a2-b2b5d02d6c9d | -6.4279 | -43.4686 | 2026-10-06 18:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1ceaf234-a11b-3f0f-87fc-c6d69adbaa74 | -9.1829 | -67.3861 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 6379ec1e-b893-3bbc-bbf0-cb2f9471b5d8 | -9.1076 | -67.703 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| fa598660-633f-30d9-9809-c38b57cb9240 | -9.1253 | -67.9432 | 2026-10-06 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| cb3cbdef-9854-3b0b-9b1d-a72de62a2669 | -8.5367 | -67.0505 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| fd80672a-4095-3365-940b-c4e0c813dd74 | -4.1416 | -46.8331 | 2026-10-06 18:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 417.2 |
| ef7cb8f6-a023-3b5f-b66c-4fff8db9bca2 | -9.4565 | -64.3344 | 2026-10-06 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ff9cc49f-2d89-3e1b-8bb7-bb81f6525ba6 | -9.4819 | -66.7836 | 2026-10-06 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |


[Clique aqui para ver as próximas entradas](README101.md)
