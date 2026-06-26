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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccc67a47-5c15-36b3-895a-0da9f77fb8be | -13.25638 | -54.42391 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d375876b-65ad-31b0-a784-6456228c7532 | -12.62521 | -57.89759 | 2026-06-26 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c5eb9ba1-23eb-3c8b-ae8f-7572e0c8ec05 | -9.19297 | -45.32086 | 2026-06-26 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 921cad1f-4e38-38d8-b016-07ba67f49972 | -13.73833 | -54.05202 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72649dc3-f43b-3aa8-9ad0-9efc2a469589 | -13.25643 | -54.43601 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8f9feb54-1fe3-367c-9693-ad316bc938c0 | -18.69917 | -42.37214 | 2026-06-26 04:34:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ef331f2-f498-3573-a08a-99c945a64107 | -17.97062 | -44.56645 | 2026-06-26 04:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10f1c102-9673-3413-9f23-6ddca0ea092c | -17.69778 | -43.70949 | 2026-06-26 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4dcde12-738f-36e3-aeef-762c478d7119 | -17.44935 | -47.15877 | 2026-06-26 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66588fc1-237e-38cc-8c09-67ef6dc0a262 | -17.61489 | -46.68893 | 2026-06-26 04:34:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60e9564d-4978-34f2-9a10-a448fec11ccc | -17.44546 | -47.16183 | 2026-06-26 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe99b981-c9cb-3cd4-8c93-3d75f664f2d2 | -17.44602 | -47.15821 | 2026-06-26 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bce21846-f1fd-314f-b16c-a709c817b534 | -17.96703 | -44.56588 | 2026-06-26 04:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ef67ad5-7b04-3ab6-a117-95cd659625dc | -17.96764 | -44.56158 | 2026-06-26 04:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8b3978b-2208-33c0-8c2d-e23d9f1b0ca8 | -28.14911 | -48.81933 | 2026-06-26 04:36:00 | NPP-375D | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be64f402-fde0-3556-918e-a8023f9bf2dd | -28.15249 | -48.82001 | 2026-06-26 04:36:00 | NPP-375D | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17b55949-57ee-38ab-841d-c9d06365848d | -5.7758 | -45.0599 | 2026-06-26 04:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 15c8d2b1-9f2d-3996-8f7f-a22ebd57f4a8 | -5.3303 | -44.69046 | 2026-06-26 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc5e6cfb-2f04-38ee-b652-13de4d4b8a90 | -4.14201 | -43.65837 | 2026-06-26 04:49:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b74a18d-5b65-30e4-9e75-b58e04ae1e65 | -5.94333 | -43.47182 | 2026-06-26 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8c09d05-5047-3333-ac3f-b057e23c07a9 | -5.7894 | -45.05834 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| e04dd0e9-edb2-3bd4-a3f2-6082d96e836a | -5.78512 | -45.05769 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 2246bcb5-0bc6-39ef-9feb-725100f9b397 | -5.78571 | -45.05365 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4367fab9-cf41-3b10-8470-c4ab6ca4fe47 | -5.93854 | -43.47116 | 2026-06-26 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c48a65-52e7-3bf8-8720-225d15586ddc | -5.77601 | -45.06035 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 321fa417-d62f-3b7e-93a4-186b25d66fc8 | -5.78999 | -45.05426 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0a151ea2-073c-3a05-b412-7c2bc7b5af93 | -5.7863 | -45.04958 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b68f3856-b7f7-31fc-b743-a41d84757fb9 | -4.34812 | -47.76237 | 2026-06-26 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f093e0d8-626d-38ac-8eb0-aa4ef83f2d26 | -5.77824 | -45.05464 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7c98801d-4b48-3bb4-9c65-c40c147c9a87 | -4.94312 | -48.2414 | 2026-06-26 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b458c55-01eb-3db6-8c12-f854a00b5a7b | -4.94251 | -48.24526 | 2026-06-26 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b65ddae-e515-345a-940b-50cd4fa4cd54 | -3.31053 | -42.49659 | 2026-06-26 04:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e8fd834-ab35-3aa3-972b-4dac3e7aef2c | -5.78925 | -43.89048 | 2026-06-26 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 055be656-aec5-3bc3-943d-39b37c0ee5ad | -5.78688 | -45.04552 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a56f2e44-bd5c-372e-9fe2-f0b3b8615ed5 | -5.78202 | -45.04891 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 32cf4d6a-4185-33da-97d1-9ac8c0d7c792 | -4.14249 | -43.65563 | 2026-06-26 04:49:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfa6d6b-fecf-392f-bb32-27018ff78efe | -5.77763 | -45.05865 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| edc31f0f-fde2-3634-892d-968a2d51ae95 | -4.35167 | -47.76294 | 2026-06-26 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e40ab9eb-f8be-3097-923a-86e2ca2d7624 | -5.79719 | -45.12455 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbdfe3d4-436e-344f-98ff-69b93055fdfe | -5.77658 | -45.05636 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fca2ef33-de17-3370-af65-9f456e70beb5 | -4.94601 | -48.24584 | 2026-06-26 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa104f01-54a7-381b-9f73-d3c69c533bde | -5.78085 | -45.05702 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9c3c1f99-a5ad-3247-aa1f-4fb71b0bfec2 | -4.94191 | -48.24915 | 2026-06-26 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f692094-8057-33dd-99e9-6b4105f31a41 | -5.78144 | -45.05298 | 2026-06-26 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e76349c0-f36f-3fd4-8977-c7cc84bf2536 | -5.32596 | -44.68977 | 2026-06-26 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbd6695b-356a-3964-aa4d-d0565879e7b0 | -5.32658 | -44.68553 | 2026-06-26 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8acb9449-80b4-3deb-a2e3-51b9e941cf57 | -5.94407 | -43.46666 | 2026-06-26 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d79796de-c5f5-392b-ad4a-88a541fa55f8 | -5.78995 | -43.88572 | 2026-06-26 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b814b5d-b5f9-3fbc-b4da-3fafd7861385 | -5.7758 | -45.0599 | 2026-06-26 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| df30cf48-bdce-30ca-adb7-0936c51244d8 | -5.7945 | -45.0586 | 2026-06-26 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 2d6a6ff3-ce3b-3563-bb26-1ad325273dea | -11.51006 | -56.12099 | 2026-06-26 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 523f56b2-6343-3f85-be35-5bf3ba7b0b8b | -6.98697 | -42.89114 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8f00dec2-29ed-3830-9316-6b220d76377d | -10.10083 | -49.59494 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cd1dd8f-f6c7-3f30-8f06-78dcefeafff2 | -8.13662 | -47.88081 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92fdb34f-1829-31a2-a60d-c513c1b59155 | -7.56863 | -45.88284 | 2026-06-26 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f76925e2-2bb6-3303-81df-3918a2af6ffb | -8.12726 | -47.8928 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9495ac5e-5fca-3213-ab82-da9ae5cc5a54 | -8.22645 | -48.17594 | 2026-06-26 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20796654-1240-3d3a-8536-8b8a6d1f60fd | -10.79524 | -49.58834 | 2026-06-26 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dc4c5341-a710-3645-9e1b-0c86fd942c1b | -10.27916 | -60.54164 | 2026-06-26 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f76a8f-717d-38d0-9aab-6a0fc19544c9 | -11.5483 | -48.26141 | 2026-06-26 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7484938c-9fe1-385c-a633-910f03abddee | -12.07893 | -54.60583 | 2026-06-26 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d5c1ff8-50ab-3084-a746-b6ac45b85311 | -10.09735 | -49.59442 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2c02394-f596-3bf3-8a90-2098ee5f9e6d | -12.74248 | -44.49031 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38fe581b-1de3-3d56-8d3c-4c8701e06e57 | -9.49583 | -57.31333 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dd6ad46-63a5-3212-9a86-a7c2d1253893 | -10.39929 | -56.75749 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b61a1d3-abd4-30b8-889c-0e632cafa606 | -10.54276 | -47.71333 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53efed99-6752-39ab-bb5d-fc8a0ca69564 | -10.63172 | -47.04205 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22e7cd06-28bd-35ef-861b-69e880f32c7a | -11.81215 | -52.517 | 2026-06-26 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7989217f-dc8b-3153-bc3e-9b2e9511b984 | -9.00854 | -47.99683 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27f1c5a7-5be0-30d6-86d4-4db419678eba | -6.30636 | -44.65129 | 2026-06-26 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba32c5dd-416d-3b1a-bb4a-daa760bcffe8 | -10.16363 | -56.62897 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3799ef3d-3e2b-3d4b-b0ad-4d6a9eee0a5e | -8.44042 | -51.56087 | 2026-06-26 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a908cf9-9c73-3c2e-a6f5-30f64f87030f | -10.9047 | -54.1263 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f5751a-2519-3f94-81d6-b3077055e719 | -8.32657 | -47.12175 | 2026-06-26 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75dc976d-89be-3863-9e5c-d278deb7e120 | -11.36145 | -52.9559 | 2026-06-26 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0cf59b9d-d0cd-30b7-9577-ec7975c88ba1 | -9.78613 | -56.94569 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 123fc769-b9c8-3e57-b07d-4fbb31d033c7 | -10.56373 | -47.20476 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 164640ff-7caa-36f5-a9fa-b980b9cc7069 | -9.40482 | -50.67199 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7574864-e587-3222-a214-b7d72190217b | -11.25286 | -43.32082 | 2026-06-26 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 87b19556-f706-3a38-9d33-6fe5203d32d0 | -6.97561 | -42.89864 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 667124b8-680c-3498-b8c1-6709a732a552 | -6.50276 | -42.21605 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0693a361-eecf-355a-b1ea-72e81f3278f4 | -9.19171 | -45.32095 | 2026-06-26 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 147583a5-e265-3401-bb8c-293e28d65f5d | -9.09778 | -47.52421 | 2026-06-26 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2622cfe4-bbf5-3c92-9c7f-073f64d4bb51 | -11.77303 | -46.44263 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83b55a85-f4d1-3675-9a99-22adaaa3aee8 | -9.89633 | -57.39899 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20949497-c5ad-378d-85be-3b45ad45252c | -12.87113 | -44.35091 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfb1e385-60cb-3e80-9824-086d98cfc0fc | -10.15932 | -56.6074 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2e8fa90-26bb-3f10-80f2-e61f0d514957 | -8.34473 | -50.50335 | 2026-06-26 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf947aa1-b6b5-35b3-bb38-64e7a145668f | -10.10256 | -49.58333 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6060a62-40c6-3a3c-b194-b8daf014986c | -12.86814 | -44.34035 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67f2fe94-438e-3325-9c7a-b3de6ad27e32 | -9.58929 | -56.92262 | 2026-06-26 04:51:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d770a8e-9524-3de7-894a-18d096811384 | -11.37678 | -47.81736 | 2026-06-26 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19ad4973-294f-363d-9108-661bdf6f3536 | -10.80542 | -48.5652 | 2026-06-26 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88ee54c3-d127-3140-b3c3-f1336e5f3f7e | -11.77836 | -46.43539 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98f9d6ef-4670-3dab-beb8-954f88022e34 | -8.13596 | -47.88522 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61b67cba-3037-33a7-954a-4580241145eb | -8.4569 | -46.99799 | 2026-06-26 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2644366d-eb17-31af-b6a6-c87cb968d03f | -6.97056 | -42.89786 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 842fa812-d9e8-3423-934e-23d24ca94597 | -7.8293 | -55.4039 | 2026-06-26 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1a409b2-b04d-319b-93fa-d8db93bfac3c | -11.91578 | -43.77953 | 2026-06-26 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6be7f6c-cc95-3647-b5c3-9a443be1d86a | -6.50171 | -42.22344 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
