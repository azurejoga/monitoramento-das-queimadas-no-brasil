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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d37094f-25a7-3847-9c45-860ed67f9504 | -9.40199 | -48.01984 | 2026-07-07 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e705a315-0a25-36ee-bae7-fcd8b4f8bd66 | -6.94805 | -43.72669 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61be09c-3dc7-30bd-86ce-7ff1c4201a25 | -6.93838 | -43.70116 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9f36611-e05c-3f00-b2e7-6f8c4834b408 | -6.92769 | -43.70882 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 89af2337-0d01-3e32-a972-d00cb60b5787 | -12.79048 | -44.49744 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14a29c35-3695-3114-99d3-03a5572bac7e | -11.63195 | -46.37594 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c70863fc-a3ba-3e71-b806-318e4fdb7a6d | -10.69843 | -49.60988 | 2026-07-07 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23bf1b4b-3d99-3b17-9d46-1fd69815dcba | -12.6853 | -48.21627 | 2026-07-07 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc37c402-087e-3494-ac49-4bed253cee9c | -6.92928 | -43.69964 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6d5ee251-7ffb-3c98-856f-63338f985d98 | -11.6789 | -44.5479 | 2026-07-07 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 37795b20-88dc-3457-89ac-2c8f7486a489 | -10.9397 | -43.0593 | 2026-07-07 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ef55f0f7-9722-371d-98da-17a847887bf9 | -6.9138 | -43.7049 | 2026-07-07 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 74ce8219-5c40-3fdc-8b01-2cda9e11537a | -13.2783 | -54.3469 | 2026-07-07 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 72518423-dda6-3c56-ac88-c2a38be726fc | -6.9326 | -43.7032 | 2026-07-07 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 634af1f3-2d1a-3fd0-a800-803151c37a2f | -14.48753 | -47.0609 | 2026-07-07 03:51:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be855de9-c0c7-33a1-b7be-ac692e53d43b | -21.06017 | -47.26327 | 2026-07-07 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faaf0920-18f0-3a89-ae78-f65fd0f6bcf2 | -21.14248 | -40.88718 | 2026-07-07 03:51:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe9ed822-35b7-3129-8dc3-fb0ee9bca9ea | -20.52635 | -43.97231 | 2026-07-07 03:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7978f805-bd06-3d19-8124-524e23626040 | -14.4881 | -47.05795 | 2026-07-07 03:51:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef06ffd9-7ec0-3c0d-a234-34edc77667d4 | -19.74353 | -40.37675 | 2026-07-07 03:51:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 532a5e0f-1a3d-35e5-b22a-1f1d5459c4a9 | -19.85158 | -49.07182 | 2026-07-07 03:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95774c00-0f73-3914-b786-00bb29cb8222 | -20.7939 | -41.12793 | 2026-07-07 03:51:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 917388ce-e2ee-3d2a-a83f-93fbbd269cac | -15.5121 | -42.21635 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df4223db-916f-3e7f-b60f-eee4717bf228 | -20.1228 | -41.61918 | 2026-07-07 03:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9d3434f-aaed-3a96-98da-21864f71ead2 | -15.51062 | -42.20307 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe5a5258-bf9a-304b-9102-5b467c4e31cf | -19.85093 | -49.07492 | 2026-07-07 03:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33a568c6-c4a7-3074-b917-b4b9cc33e531 | -20.28442 | -42.20602 | 2026-07-07 03:51:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d9c0b6e0-76e0-3763-b4d1-8796dd5c69b5 | -15.50918 | -42.21154 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec2e32be-c262-3d8d-9eea-27178042ec10 | -20.5272 | -43.96757 | 2026-07-07 03:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 38eb80ef-776d-3865-9fb7-27268b3c9798 | -21.06116 | -47.25839 | 2026-07-07 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 185ec95b-3ddb-306e-a1dc-91fd11986e52 | -20.71553 | -47.29037 | 2026-07-07 03:51:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299de187-0633-335d-b0b8-55e2d93ad59e | -15.51282 | -42.21211 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c2951be-7233-339c-8f22-9fb762837ac8 | -20.71196 | -47.29198 | 2026-07-07 03:51:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5a1c5a5-994e-3e28-b046-4ada446ce22f | -21.06558 | -47.25956 | 2026-07-07 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de8a0dbe-2c4c-3f19-9beb-47ff86bb6b9f | -15.507 | -42.20243 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46a16a91-91e8-3c5c-b8e9-6dd6fff8693e | -15.51425 | -42.20372 | 2026-07-07 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e6c552-2712-3f57-b738-79ba0fa526d6 | -21.50811 | -48.82209 | 2026-07-07 03:53:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba7b8c53-d344-3ea5-9e41-92628af09429 | -22.28863 | -46.86359 | 2026-07-07 03:53:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 285cbc0a-e891-3980-8ea7-65edf85bef61 | -22.3808 | -49.79101 | 2026-07-07 03:53:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1198cc0f-e1c4-3e5e-84aa-c32984363a09 | -22.78818 | -49.3436 | 2026-07-07 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d010618-ecd8-3404-bd5e-4f13acc4596d | -22.02616 | -48.22205 | 2026-07-07 03:53:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdea79b8-3efa-3ba3-aebf-332654f747ad | -21.50936 | -48.81622 | 2026-07-07 03:53:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e1782b0-31bf-3f2f-8df9-8261c8ba94f9 | -22.28351 | -46.86708 | 2026-07-07 03:53:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8d28867-0844-39fa-b5f8-ff3364f1741d | -23.56402 | -47.51812 | 2026-07-07 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8f79e8f9-0deb-36f4-88c8-0deffc6e934c | -21.25513 | -49.17858 | 2026-07-07 03:53:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c75a6cb3-2afd-3198-b788-881843b2d88c | -22.38307 | -49.79261 | 2026-07-07 03:53:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49d5a059-a93c-3989-9573-20fe30351ccc | -22.37803 | -49.79123 | 2026-07-07 03:53:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cc58805a-61e6-3c61-958c-ba7e2afffad5 | -22.02507 | -48.2274 | 2026-07-07 03:53:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4af4f5b1-8b09-3177-ae46-ee1147f3d24d | -23.56496 | -47.51349 | 2026-07-07 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0c3abccf-f2ed-3023-81c8-553738734c60 | -22.78996 | -49.34085 | 2026-07-07 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fe38ad1-9294-3870-b4f9-bb09694d67f5 | -22.27925 | -46.86615 | 2026-07-07 03:53:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eb7615b-8c0a-37cc-8c33-4a6560e39ad5 | -11.6789 | -44.5479 | 2026-07-07 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 22065c02-3cdc-3bc6-9807-eab8f9ed324f | -13.2592 | -54.3489 | 2026-07-07 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 72056d24-75b2-3850-a8e4-7dede6f47d8e | -10.9397 | -43.0593 | 2026-07-07 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7c96f807-26e3-3088-8e6c-7ee54015cd8e | -13.2783 | -54.3469 | 2026-07-07 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9981240f-163a-3d32-a06a-2b363b3ad702 | -13.2595 | -54.3283 | 2026-07-07 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c64ac691-95e6-3292-a074-d42f35dea5df | -6.9138 | -43.7049 | 2026-07-07 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5af08844-489c-3dca-b210-e3f02d9d5bc0 | -6.9326 | -43.7032 | 2026-07-07 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cf089b57-f9a0-35c0-80ac-62d710986797 | -10.9397 | -43.0593 | 2026-07-07 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a40b6358-93a7-3aa0-902c-0ba699520a28 | -11.6789 | -44.5479 | 2026-07-07 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3fb68def-b2ba-3423-92c0-ba71a2c10660 | -13.2783 | -54.3469 | 2026-07-07 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 067e9e13-df79-33ea-b0a6-2b743432cf4f | -12.7944 | -44.4895 | 2026-07-07 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ab1add6b-bd9c-3c5a-a942-0d8e1339740f | -13.2595 | -54.3283 | 2026-07-07 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| aeb17566-630f-3617-b120-7a03edbcb772 | -13.2592 | -54.3489 | 2026-07-07 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 456dea7b-feac-3a24-b215-905be6674fce | -13.2786 | -54.3262 | 2026-07-07 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c8816eb0-436f-3859-b9ff-fd33e9e05f7e | -6.9138 | -43.7049 | 2026-07-07 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e7c5540a-8e7f-3b6c-a868-9306c125a0be | -6.9138 | -43.7049 | 2026-07-07 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 281bbf16-aff6-30f6-bd68-e9c80ca187cb | -13.2783 | -54.3469 | 2026-07-07 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3a46df2e-6fab-39f7-960b-beb747c608fc | -6.9326 | -43.7032 | 2026-07-07 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0cc78245-982a-3495-a5c3-bfb4fcf1d1c4 | -5.83163 | -43.48086 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b81a94d-2de4-3984-a4b2-3313e4dad2ff | -6.9285 | -43.71212 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed3939d3-930a-3266-8a8d-0525cfe1a39a | -5.5065 | -44.07696 | 2026-07-07 04:23:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb97a807-8fcb-3005-ab0d-1baf70c1b9b1 | -7.31214 | -43.25349 | 2026-07-07 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11603975-6dc0-38ca-8753-d3b79638150b | -7.31492 | -43.25749 | 2026-07-07 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814a8ae7-3903-31db-83cc-30773fd2f6f4 | -2.97786 | -49.27064 | 2026-07-07 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87208257-813d-3f94-9468-a19812f12f9b | -3.19444 | -49.0621 | 2026-07-07 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a6859d6-1afe-3d1b-b8fb-75dace804dbf | -5.81786 | -43.589 | 2026-07-07 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 454e8300-21a0-34db-867d-70a951cf1211 | -5.82063 | -43.59301 | 2026-07-07 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e246f045-c0f5-3c4d-87df-0c14c146319d | -6.93016 | -43.7017 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f90cae4a-d6c3-38b0-aabb-cdcd4bc8fff2 | -8.11939 | -47.11702 | 2026-07-07 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb7dc8dc-3230-3a61-b3c5-f0b2db3e0b91 | -5.82831 | -43.48034 | 2026-07-07 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8296cddd-7765-3f39-95d6-60a2971b54e5 | -6.43635 | -44.57437 | 2026-07-07 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 233d48dd-6006-3e7b-b397-c20b22713f1e | -8.03536 | -45.04062 | 2026-07-07 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9650689a-58f8-34a4-ad8d-7682cc72bd8c | -6.92906 | -43.70865 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 297252e9-f635-33f0-897f-9d956d121d23 | -4.38284 | -43.3541 | 2026-07-07 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db509cc1-0677-38ac-8f1a-6553489a790d | -5.22593 | -43.16063 | 2026-07-07 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3d21d8e-21c0-35ad-8ee5-b1b2f3e72899 | -6.89516 | -43.71055 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38ead523-85de-345c-a714-76377289b64f | -5.4076 | -45.19136 | 2026-07-07 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0a0f667-684b-37b3-b20a-05086b1aeff4 | -6.91134 | -43.71296 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7ce59db6-c478-314e-87b9-71533fa3d69b | -6.50494 | -42.21052 | 2026-07-07 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04d0c634-df49-3147-b59c-bbe9cb4ffba5 | -6.91632 | -43.70305 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f706fdc-f45f-34d5-9ccb-6e0365c71d48 | -6.43199 | -55.80032 | 2026-07-07 04:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ba8558-935e-3c41-8a59-54bea91f9881 | -6.43916 | -44.57846 | 2026-07-07 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a7b643-8180-36ed-9934-5d2f72c5422d | -4.28322 | -48.23447 | 2026-07-07 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49acf0c3-c3a7-3d40-aff3-67cfbca2ceff | -6.90469 | -43.7119 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5137b61-4d40-3a6b-9c93-becf87dfeb07 | -7.37634 | -44.00512 | 2026-07-07 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e5e1472-6279-31c9-b0a1-a0144ddcbcf8 | -2.88682 | -42.95346 | 2026-07-07 04:23:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 895248aa-06ef-3e8d-8f8d-7cacbf3e3537 | -6.913 | -43.70253 | 2026-07-07 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94b5f729-228c-36ff-8179-83016a73e029 | -7.00878 | -42.77651 | 2026-07-07 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3b288cb-51c0-3f0d-bdc2-28b50dab4401 | -4.82885 | -44.05678 | 2026-07-07 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README10.md)
