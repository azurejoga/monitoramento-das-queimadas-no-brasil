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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de93ddd9-a90f-36f3-8b67-cb557f069f9b | -8.44351 | -47.28962 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 495464df-39c2-3c16-b792-1b0fdb0e0e22 | -9.79712 | -57.45097 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19217aa0-0dc2-3d9b-b569-31a6e9cc527a | -7.71653 | -44.74239 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e258421e-be02-35ca-bd8c-83a8b749de87 | -13.00794 | -45.21117 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d76effe2-6919-37b9-8f3d-b86b75630394 | -8.05546 | -48.62912 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a426a5e8-65bc-3812-a031-1999355b940c | -9.13526 | -60.52971 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f06aa24-718b-37d8-a615-dd15a7d7b174 | -14.33586 | -47.30256 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 576f47f0-c407-3f56-b079-c8ae0b7e5a96 | -9.44651 | -60.52518 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d40c632-a3a5-3fa2-b047-0cb4bde0eb80 | -9.23705 | -57.06655 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5871748-1635-3881-b804-534861b5f493 | -7.31437 | -44.37294 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae3268fe-b4cb-3e97-8086-29698f8c6ebb | -9.6953 | -57.8035 | 2025-09-09 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df8d7c9f-5f32-3d8f-9636-8296ed89a39f | -13.84289 | -46.23798 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1038df56-adf5-321c-a60f-404e7c2b9fe0 | -12.81839 | -52.94199 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b50c4b3-8258-3a57-a7fc-781e6cccb2f4 | -12.08061 | -42.57977 | 2025-09-09 04:34:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49f2e05d-160b-3333-9ae0-e5d4d46063bf | -7.71221 | -44.74619 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e753f344-0c8a-36f7-a54f-6b5a3bdeb2e8 | -8.03376 | -45.50502 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94d03f6a-aa13-32de-9969-5b4aa9ce20ee | -12.47754 | -53.83404 | 2025-09-09 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dcb0dd1-2a6c-387b-95f0-c264f2e34cf3 | -11.83085 | -47.55218 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43982ff3-69d2-3cd0-aacf-f1f6c1254e3e | -7.443 | -49.2723 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04764a63-6c71-385d-8a20-ec323df74461 | -8.03995 | -48.63735 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1882960-fdc1-3ea3-b276-3757de85d525 | -8.37709 | -45.00655 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4faf3350-f732-392f-a6a9-bc3505ebdd66 | -7.99017 | -46.33287 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 455e390c-f251-32dc-9815-94b8a07f6952 | -11.17037 | -48.36895 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94046ae3-dbc7-3af2-8bec-384484f1a18f | -9.43052 | -46.73101 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4e82414-b0e6-3e27-ac89-017e2e702988 | -9.24699 | -57.06645 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 092b3952-ee18-37f1-92b2-980af4f07ce3 | -11.30431 | -46.50623 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9bf6970b-4a31-37bf-9cb2-9486e9197956 | -8.03746 | -43.81219 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2216667c-9e8e-351b-943b-fd2ca11d2c71 | -12.62524 | -56.97975 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5987f1e-f2b9-354a-8dcc-a3b96828d582 | -11.31543 | -55.12224 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae8a417a-b2e7-3863-9a89-012609f592d7 | -14.32832 | -47.31918 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 424dc29e-80c8-373b-8841-76fa65a27bf8 | -11.34277 | -46.5682 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f061bd-5b59-33ca-9e39-5a78cabdb5f1 | -8.49092 | -47.33308 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dba5a37b-204a-37bc-9d04-5428f0936697 | -11.04149 | -52.06446 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26e40977-f754-3460-8ca3-0008e3dc22b1 | -14.41381 | -48.46678 | 2025-09-09 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20eaf1c5-03fe-31f1-ab0c-2fa72e16ae68 | -11.46384 | -49.26035 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bedf094d-d849-30f1-989d-f1c06135c904 | -11.4809 | -49.2595 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a725021-17ae-342b-a850-0af37827f69f | -12.29328 | -49.9977 | 2025-09-09 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cacbf82b-a48d-318e-975c-fb73d0770486 | -9.71101 | -46.82258 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cdf48991-abae-39d2-9947-005c73b7ff29 | -13.08815 | -49.90051 | 2025-09-09 04:34:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c29d1db9-905c-32bc-89fa-a1931232085c | -11.20554 | -55.00365 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8af6a957-8eb8-3a75-8a9b-180b3790be0e | -12.20166 | -53.89167 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d2f7ac04-0300-32c4-992c-55b1ec2efc10 | -13.79712 | -46.27143 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2935714-fce1-3b13-b708-bf35de1bcd71 | -12.51264 | -45.29491 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 332c6fa6-5f61-32dd-986f-261288b21339 | -12.94158 | -54.79802 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d0ce1f9-a583-371b-b31b-68d412b692c3 | -8.00305 | -45.46709 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e6a970e-aa41-378d-866c-4b8d0012210d | -9.50193 | -48.25136 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c83f12d2-978b-393b-a6e7-d507d7f56b25 | -13.04898 | -48.0327 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb52f9ee-8b29-3178-9fd1-ff3c2425a54b | -12.63086 | -56.97559 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f2dddae-5a85-3cf2-b930-06774dfc5695 | -7.74635 | -50.31653 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a934069e-bacd-3f1a-a005-5ac54bcb86c6 | -12.8538 | -47.97721 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 129b7c2e-42fa-371c-980e-3fa4606cdd5a | -9.22616 | -60.81769 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6976753-281d-3e8a-95fc-ee75a2de1e4d | -12.95112 | -54.81499 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edcfc537-2ec8-3068-aef4-5725c49b8671 | -11.2027 | -54.99498 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5535d0a3-e412-303b-9ce6-b6a099be49a1 | -13.13406 | -54.91717 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ebb8b57-3e4d-3392-9fb7-9545455f4127 | -7.80051 | -45.20565 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccab2f9a-04f5-3bbe-ba3e-ca75c4cb769d | -12.92659 | -54.76507 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a19177-4c73-3f60-93f3-f1977320ab47 | -10.17763 | -46.22708 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7865853-0f55-3104-8f04-1b767ba026d6 | -9.45043 | -60.50533 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b82dc1c-73e9-3ef9-bf7b-8fa1ede7cb46 | -9.58892 | -47.97506 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e818963a-0dc3-3253-b27e-7a1d798963c2 | -9.80282 | -53.31823 | 2025-09-09 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7929e894-407c-3055-af0a-176d73c8ccdc | -12.93819 | -54.79361 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2136e37-0ae8-3f36-a73e-c940944c87d9 | -11.22318 | -59.13016 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1593eae6-c6b7-31f0-a4cd-72c59b68b668 | -7.74574 | -50.32033 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e057283-91a3-339e-90b8-b44f882d6dbb | -8.05876 | -48.62964 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 21f1fe33-a236-3142-9258-a143b2d96425 | -11.34609 | -50.43228 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9819ce65-dc1e-3718-883a-291591a03a6a | -9.8612 | -48.84778 | 2025-09-09 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 779df164-3420-3d4c-a1c0-a84ad2d1b74c | -11.60576 | -52.20573 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab7dfe7d-f134-34d0-96b9-bb41a5091716 | -9.44994 | -60.51871 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffbeffa9-402a-3f5a-a887-dd54d7c5c8c5 | -10.97055 | -46.81167 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31cd3e97-636e-32e3-a444-7324338d4638 | -10.96886 | -45.11449 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| cdbb19ab-bc5b-3260-b650-564bfaf4f029 | -11.33696 | -46.55907 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2578e383-490c-3408-a6e8-7e9f9c82a1b7 | -9.21982 | -60.81632 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9868bb63-2a85-3e4f-90f5-e385ce1fe8c0 | -12.29596 | -50.00232 | 2025-09-09 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88975d4a-afb8-3e06-9ff1-e1a00baa9cbe | -8.37774 | -45.02601 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0f2964d4-fa97-3754-a961-d318a99ffda6 | -11.4152 | -43.5804 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f98c949-eac4-3781-80a8-4feea410c9e1 | -12.01686 | -51.07335 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73b09e3-687a-3260-b64d-80ea0635cc6a | -9.45675 | -46.44089 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e47fe3a3-0e3f-3396-9225-a3670dc08d2c | -9.16699 | -59.3778 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72680f75-f068-33b8-9669-e6da4e48454d | -8.06811 | -48.63468 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2296b66-6aba-34d3-9369-1079532aa659 | -9.45995 | -60.5 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c26ce0a-eb4a-369c-8f5b-ef430ae46a73 | -11.83669 | -46.77876 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f042997-0584-3439-8054-c4bb35d79ec1 | -11.33986 | -46.56366 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67456421-c0f8-3193-a039-49738b7a40a8 | -7.56397 | -44.65839 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7db4ee8-1b7f-33a7-8987-ffa0e2eb06cd | -11.37418 | -43.52457 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 806a810b-dd45-39b1-9831-90083b32cbc1 | -7.94828 | -44.84527 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 359894f7-03ff-372e-a583-151604f1d282 | -12.47369 | -53.83339 | 2025-09-09 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39fd4892-9f20-3eb5-823b-c77d981a90e1 | -12.63268 | -56.96554 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b35b721a-1362-3a59-858a-5f8618702f8b | -6.87571 | -47.90652 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88f32fea-82a6-3b9e-bf02-d80d9929698b | -7.79988 | -45.20981 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47cf8999-e4cd-3f84-80f6-4df20db50843 | -7.99073 | -46.32912 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f0b13c9-d0d4-3149-a51c-5a5638c2f436 | -10.57413 | -52.01112 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e755dae-1990-3e5d-8a29-12ef86679a71 | -12.96362 | -54.76811 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a2029c-2a98-3a62-8505-1c8b25ee8939 | -7.77938 | -52.12674 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2387d76f-84a1-37c0-8157-82c4618e45d4 | -12.61582 | -56.97805 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7934bcf-1c1f-30d2-86d8-d3c3a2e538de | -8.43962 | -47.29262 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f82b4b52-2af6-3a56-b864-6e69353dcc43 | -12.63862 | -56.96892 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3e0cc66-ca1d-3e28-9921-4815d888959b | -10.30005 | -43.39259 | 2025-09-09 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46f24092-53d1-392b-b7af-6b8abd0afe2f | -9.22413 | -60.82815 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02eff483-77f5-3e52-880b-ef3e1551c10f | -7.87817 | -44.81177 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9a40699-652b-376c-b37a-492d69c8c111 | -11.41884 | -43.58478 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README45.md)
