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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f82abcf-b33d-31cf-b917-11161a1b91a4 | -23.11734 | -46.39018 | 2025-10-27 04:36:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cea6a2a5-5ce7-3e77-bd20-d2af1204712f | -27.53137 | -52.89061 | 2025-10-27 04:38:00 | NOAA-21 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| babdf962-5e09-35ca-8376-25bb0317ce1f | -24.65578 | -53.34652 | 2025-10-27 04:38:00 | NOAA-21 | CAFELÂNDIA | PARANÁ | Brasil | 4103453 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19b0af31-7475-3b75-81dc-7addf5af2658 | -30.13336 | -51.96111 | 2025-10-27 04:38:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| ef9c5fb5-1f07-3614-b564-af7ece95c45c | -4.4805 | -43.4237 | 2025-10-27 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| de0464f9-4fff-3809-9e8f-41a74ee0eaa0 | -7.8223 | -46.4664 | 2025-10-27 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 04329387-3a2c-3819-ae88-077f72a58be7 | -10.8401 | -56.959 | 2025-10-27 04:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2414501f-ce7a-3d16-b6a8-7ec51c80e904 | -10.3597 | -47.1577 | 2025-10-27 04:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f681f125-d1d2-34ca-a59c-ba999e891b92 | -7.822 | -46.4887 | 2025-10-27 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 333b1f6a-ef1d-3979-a57d-876d5866222f | -7.8408 | -46.487 | 2025-10-27 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ad396b9b-e07a-3c30-822c-dac054b9d4c8 | -7.8411 | -46.4646 | 2025-10-27 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 088362d1-89b2-39bd-9ae0-8e417d40e809 | -4.4479 | -45.4599 | 2025-10-27 04:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 28b1245a-720b-3e3f-bc41-af002edbe09d | -10.3594 | -47.18 | 2025-10-27 04:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| bf30184e-60ad-3544-b9dc-d7bb269fe014 | -4.4618 | -43.4248 | 2025-10-27 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6a6d0446-b61c-3f98-b490-39b7bd66020e | -7.8413 | -46.4423 | 2025-10-27 04:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 775d8de6-84b3-38b0-b9bf-e34aa0453d48 | -7.8411 | -46.4646 | 2025-10-27 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 28eb2c3e-d3d8-38a6-8f4c-612f14cf7a0d | -10.8401 | -56.959 | 2025-10-27 04:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2fbb1bfd-f9aa-342d-8450-9e958c5e7bc8 | -7.822 | -46.4887 | 2025-10-27 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5b7be843-9273-3048-b8cc-e6e6a01a13f6 | -4.4618 | -43.4248 | 2025-10-27 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| f058dc98-5ceb-3a93-b477-ceddd2811bdc | -7.8223 | -46.4664 | 2025-10-27 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 384cb1e5-1c0d-312d-882c-54c291988b6e | -10.3594 | -47.18 | 2025-10-27 04:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| d924c1e9-1099-3e74-9147-4a8c29b7313f | -7.8413 | -46.4423 | 2025-10-27 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 9ac069de-c36c-31ce-a8ab-485c73cbacf4 | -7.8225 | -46.444 | 2025-10-27 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| d55eb9d0-500d-377f-98f9-f0eefc4c9c2d | -4.4807 | -43.4005 | 2025-10-27 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 83f1296c-76bd-334b-b101-be647dc53194 | -4.4805 | -43.4237 | 2025-10-27 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 9141a422-ba1e-33f1-8dd2-4c122c2c6a16 | -7.8408 | -46.487 | 2025-10-27 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 1199e28e-7d75-3f68-8933-fccd3594df52 | 2.78062 | -51.36095 | 2025-10-27 04:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ad6f717e-29e4-3451-b9e0-763ce1912b24 | 3.64067 | -51.82966 | 2025-10-27 04:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68f9d1e5-2166-374a-878a-61e1c94005c1 | 3.64012 | -51.82621 | 2025-10-27 04:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b122bc-015e-3a72-bb8b-857afc28fe2f | 2.51344 | -51.07476 | 2025-10-27 04:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d162b72e-6c6c-3ec2-8736-b893c5e96631 | 2.11124 | -50.91436 | 2025-10-27 04:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61b6bee5-9b19-37bc-97cd-f3e87227ef53 | 3.02527 | -51.4514 | 2025-10-27 04:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa440c9c-fb1d-3f72-820c-768e3f8f5452 | 3.46869 | -51.78934 | 2025-10-27 04:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e363425-6079-3c0b-b939-4d9f4287e037 | 2.35019 | -51.54272 | 2025-10-27 04:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0392feac-8b3e-3a78-a91b-7c175fd7848c | -3.14776 | -50.44926 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6462bb7a-8f59-379b-87fd-25502a070359 | -2.12939 | -56.84534 | 2025-10-27 04:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6191ef2-ab88-39a5-908e-c6838c3b0879 | -2.97064 | -51.03252 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbd15b6c-2022-3a86-b34b-ed8b3bcde11c | -1.3971 | -53.10089 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaa5b32d-5f59-393a-9ba4-6cd8dd4c2576 | 0.4341 | -50.82209 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e90b97c1-86ed-3c9f-b722-ab699c061449 | -4.48075 | -43.42445 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 816a0f6e-60ee-3cd2-b1a0-c02c4321677a | -3.46587 | -47.6856 | 2025-10-27 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bec4972-1098-3064-b225-82827d83fc07 | -4.36073 | -48.6679 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ac959e4-4278-3413-8254-4eb7fa928b5c | -2.90502 | -53.1288 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84e9f3e-b3e1-3c29-8403-185048f31186 | -2.89829 | -53.13131 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfbc7c69-4e7f-35fc-af3d-5f209d4e6223 | -3.82354 | -52.29689 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 879c28c7-aecb-3378-bb1a-2d15de2913fe | -3.52063 | -52.20334 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7588faa-fe74-3049-9ef4-2f9a953bebfe | -4.48178 | -43.4269 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6e674cda-9e32-3a31-811f-42147de5c0b1 | 1.1476 | -51.07071 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 754b265f-57e3-33c8-9e06-b603d9a99caa | -3.55733 | -49.495 | 2025-10-27 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc8038a9-f4ff-3526-b1ea-91b2baf643d8 | -1.57154 | -53.453 | 2025-10-27 04:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d8ea49-9705-33c3-a104-35339fe40828 | -2.08177 | -48.36744 | 2025-10-27 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4247487-2d99-3d6d-a4bc-00997915a688 | -5.5931 | -41.3243 | 2025-10-27 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bc2d09c-c05e-38d4-9c29-07d6b738a655 | -4.47599 | -45.32524 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c2e4a80-1d20-306b-a539-3710b2b51ec7 | -3.09749 | -49.44875 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 960b2641-3665-314e-8e3d-fabdb5075af2 | -3.3372 | -42.88947 | 2025-10-27 04:59:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c925838-1d55-31bc-b338-c0bcd476ced1 | -2.61379 | -51.75046 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28192b0f-bb78-3446-8151-925ac5e32df6 | -3.47199 | -49.96914 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efb15f63-56ad-327b-9c74-e6772f4b8799 | 1.60907 | -55.7353 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4786c53e-21b0-3d20-bd25-556ef2bf8f86 | -3.04448 | -53.01562 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba51feef-b8fa-3eef-aace-7084985b7f84 | 0.43753 | -50.82156 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80374249-189e-3f61-870c-0171b137d886 | -4.83286 | -45.33895 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f35c96d-2836-33f1-82ab-3802f7dc72d6 | 1.62463 | -55.7156 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac1e2eb-66b3-391d-8d44-2abd6d8a0dc6 | -4.45295 | -43.66295 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42b1c47d-7567-3e39-8594-a93895e8c858 | -4.23256 | -50.13433 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dabc1b75-46d8-325a-a8e5-90541e9b84f3 | -1.751 | -46.5423 | 2025-10-27 04:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab8f508c-1671-3fdc-926c-1c573f64f5fc | -3.07067 | -48.02257 | 2025-10-27 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c45a89-5880-3d9c-9b28-86e03084acf5 | -4.44039 | -43.42476 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e58f43f-3d0a-307a-ada1-a49c3c74ad1d | -3.14756 | -50.33017 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dee3368-e87d-3944-86f0-83f7fb672f9f | -4.80682 | -43.30146 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb4f7df2-4989-313f-9c07-905cf5a3ded1 | -3.72797 | -49.68616 | 2025-10-27 04:59:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee5b3e5b-ff0d-3f40-bc08-896e08252cad | -3.10919 | -51.21036 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98b8031a-62e0-3631-96b2-24f11ace5661 | -3.71421 | -50.17834 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8032d855-2be0-35e9-b9ca-74d2d8af70bf | -4.47378 | -43.43169 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 81e496dc-b402-387e-85b6-745d41280323 | -1.4015 | -53.09452 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c56911be-8584-3567-aa71-308c26b3d2a3 | -3.87142 | -52.19014 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5da1c75-cb8f-33c8-bea8-50e940250a3d | -4.4761 | -43.41518 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e5910e-850e-3156-ac41-3bea474289bd | -1.18659 | -53.38531 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79c9d41c-3257-3fb2-98e7-dc1836394158 | -3.08063 | -51.27269 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64af9bf3-db1e-3684-8213-699c19f084bb | -3.14002 | -50.1623 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31769c4e-0e41-38df-bec2-ada8239abb64 | -4.45689 | -45.45494 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6acdb8b5-2cde-39c6-93f8-7ebb8e4218bc | -4.48118 | -43.431 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ed27beb4-66c3-310e-9489-f719d431785f | -3.06161 | -49.37645 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 677f19bd-4c12-3f6e-befd-a853146b40f7 | -4.45163 | -49.58339 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14a25e15-4f8d-3120-9d78-08cdb98d46f6 | -3.33972 | -52.84069 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10bccd6b-dcba-35f2-84d8-9b35e4e75b06 | -5.53062 | -41.72312 | 2025-10-27 04:59:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fa107c5-f218-3148-9660-2d2668d25755 | -3.55623 | -53.01392 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3685d7e9-39e7-3b45-b572-e0867e1b1bb7 | -3.12677 | -49.10309 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 731000d1-b13a-3bf4-8653-6cae314813c0 | -2.63667 | -47.30232 | 2025-10-27 04:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6177ec4e-aa04-3d6d-9624-2a9483363ca6 | 0.80655 | -50.83673 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e9952e0-7ca2-3f2f-b3d5-93f94974bbd6 | -4.88802 | -43.22634 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03f21921-51e2-3fb4-8121-3a58a36f959e | -3.21665 | -50.79527 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1631374-486a-3dee-b76d-983fade78611 | -4.22141 | -48.35624 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f2633fb-c526-3032-a8a3-16b1b38f854b | -4.47028 | -43.41417 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaaf52fe-c366-38c8-adb0-de0fb22b1af5 | -1.35591 | -49.16583 | 2025-10-27 04:59:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e74a7c9-a7b1-3787-9de9-35ff81888706 | -2.86332 | -41.75277 | 2025-10-27 04:59:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a6e4c47-3684-30e9-b9a6-5bc2f64291aa | -4.39021 | -43.31643 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f8a8a43-d0aa-329b-a67a-89250a0ebcec | -4.51667 | -44.04686 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36589a8e-be86-31a5-9ac7-e59e699b910f | -2.77254 | -54.57088 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d7810a-cb56-37ed-ab50-b082ce61ad05 | -3.05004 | -53.02359 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aae6c03a-1c6b-31c1-9e2f-f4e6147136ff | -4.4269 | -45.97745 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README53.md)
