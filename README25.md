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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d61e99c8-9548-32b5-bcf7-69b56e3e08b0 | -9.25188 | -56.30003 | 2025-10-11 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2754abd8-b2fd-35c1-8120-3824dbc0ae49 | -11.91539 | -44.18197 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d8a365bc-5687-3340-9d57-b245c99269d5 | -9.25998 | -44.38123 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d5739d9-9cac-35d4-94ca-e31e460783aa | -13.21101 | -42.34493 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| fe968c39-0ea2-3bcc-bcc4-56ef85c072f6 | -13.08293 | -54.84426 | 2025-10-11 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea5ec7b-6ff4-3d70-b1a4-debfdb1ac334 | -14.73682 | -47.44712 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c101c02-41d7-36e7-aa2c-a64ceddcf19a | -13.28813 | -47.13094 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7769091-f4ed-3caa-9dbf-db35d117e463 | -11.7774 | -45.03903 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2ab91ba-2758-3032-bcf5-97a9ba380799 | -15.64459 | -44.47912 | 2025-10-11 04:34:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 979f4f31-e36a-3136-a57c-af4dc95f6907 | -10.54726 | -47.3102 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5d646ca1-6463-3f6c-a52d-20505ce3eb25 | -13.80172 | -45.76117 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68280cb5-eb18-3b12-9382-fb963537a0ba | -14.94589 | -46.75266 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34c951d8-c64c-3015-bbbe-d14c74d5b6ab | -13.44881 | -43.68803 | 2025-10-11 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c331ed92-1210-3ccb-bfe7-43919fb6129d | -15.40925 | -47.30086 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5472aad8-3474-367a-8e1d-86b133c85bda | -12.99456 | -48.39974 | 2025-10-11 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e509b9b5-72b5-3883-b711-c4feede6fd9b | -11.62407 | -55.01033 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f589754d-650b-3a6b-a3d8-5c9ae8e9a72e | -13.30017 | -47.12136 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 30d2da8a-0801-3b9a-a31d-9e974b628f95 | -14.28205 | -45.89996 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3d8528f-3bde-389c-ba37-ebecbb2861f1 | -11.63816 | -55.0048 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d9c059-d785-35fb-9e32-260f56213072 | -11.76375 | -43.32082 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2291d389-23f1-3cc3-9b2a-0107e7bc82e3 | -14.01298 | -47.05458 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb3b1c6-c9b5-3691-abf3-ab439d33caf7 | -11.82778 | -51.26589 | 2025-10-11 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ef21cd0-d5d7-3ba6-ad8d-b6f17e8aaddc | -14.93465 | -46.75456 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7351f298-6be0-36d0-912c-81324d764924 | -13.79613 | -45.38966 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f245ef-e464-3518-8071-bfc1b007b0cc | -13.21624 | -42.34072 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| c3dccf83-7973-3358-968c-d3f33bd77417 | -12.74985 | -48.64209 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90280f31-ff76-37d0-a7c5-613e6f1c8a3d | -14.43945 | -50.34649 | 2025-10-11 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e079db8c-8908-372d-8304-da5ca9301dc0 | -9.26956 | -44.36834 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abbc5d00-afe8-31fc-b08d-b118a445128a | -11.82715 | -51.26971 | 2025-10-11 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f0f3104-d002-3c5f-a8bc-76a42e439ade | -14.43888 | -50.35006 | 2025-10-11 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7738241-e2ed-3e87-bd06-33602835bc53 | -16.20374 | -44.4524 | 2025-10-11 04:34:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc88213f-e58d-33bf-b98f-6c2e8b938c96 | -15.49452 | -47.98728 | 2025-10-11 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d52643a-64fb-318c-85f8-c1f604e71650 | -13.41797 | -47.24426 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fae9ed75-c497-37d8-84c7-6e910b6f9845 | -15.38998 | -47.28547 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c11b1e2d-f83b-34b8-b4c7-2f0f3b692ec0 | -13.29893 | -48.49937 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe3a6000-e1bc-3b19-94a2-6f91d7c54d7c | -11.74253 | -46.40009 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ac21a7f-9b91-3031-bea9-980098ef704e | -9.44953 | -45.45764 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1422fcfc-0df1-3b1b-8e12-0095678f173d | -13.08088 | -47.78801 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 611620a5-c050-3893-b1a7-9080675f577a | -15.91128 | -43.28106 | 2025-10-11 04:34:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e372bf60-d3ad-3d6e-87f2-611b7d0a6fac | -9.39946 | -45.77533 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e95bf7cb-016c-3507-baae-f4d30384d25a | -11.44958 | -43.4805 | 2025-10-11 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27032bc6-b987-3e00-914d-653f722bfc9e | -10.0733 | -45.91664 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62bf90a7-e2c0-31f5-b1d5-9c1cac7a481c | -13.21085 | -42.34737 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| f51d7bd0-738d-3830-88c9-9157b9bb8549 | -10.20351 | -44.60153 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d42886-c276-3653-8b1f-5302bcc65a21 | -11.19027 | -50.52037 | 2025-10-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae41ca5-56cd-3426-b3b9-b642c3b00c6b | -13.29048 | -47.99005 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae86599-de91-3972-82d0-1e7f99981917 | -15.29706 | -46.14015 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad87e9b7-ba4d-336d-b121-3609e797b356 | -10.62077 | -54.95313 | 2025-10-11 04:34:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33a4c4f1-9d27-3824-abf7-fa753526bce2 | -9.81361 | -45.52057 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f139c721-2a49-3cd5-ae07-0ff8e5680678 | -13.3165 | -47.1226 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebb1e97f-936d-36f6-9323-48dd5dc3fe62 | -14.98917 | -45.56378 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228e8a2f-56c9-3a2e-8f70-78ba6a9ddea1 | -13.45946 | -48.09173 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4701921d-14e6-31a9-b669-4d01bca919a4 | -13.25542 | -48.0261 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5c45bd5-d4e1-369a-bb6c-564b190b1e26 | -11.76484 | -43.31293 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a280009-976e-31f3-a800-0c1044da8555 | -14.94355 | -46.74345 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa9f1dcc-e017-398c-8e24-5cf8ca0d9a10 | -15.75964 | -48.96521 | 2025-10-11 04:34:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc91f28-69cf-335b-a475-f63b8ebf59c7 | -10.07744 | -45.91309 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d58e0d6-e9f1-3c4d-a32a-5b1d0d6023e6 | -11.62758 | -55.01513 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 204c6d89-5569-3933-984b-4ebc4ae7e77c | -11.86116 | -44.91126 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36288bd0-8df6-3d40-a8d4-9228a50211e1 | -14.92394 | -46.77849 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 963cdc9e-e673-3521-baac-2ad5dc485029 | -13.21688 | -42.3359 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| a911f062-bb07-3a93-ace1-53bc3d859fa9 | -13.21165 | -42.34007 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 799616f2-8a6f-3d8d-861e-ec42163af035 | -13.519 | -48.16757 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4296ca7-54fb-3d47-8081-d586486051af | -12.23947 | -51.13531 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca1c51a-fec7-3e58-a795-816d72a477cc | -13.28392 | -47.99706 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d858344-6357-3a9a-8fe2-716cb58cc76b | -8.68193 | -48.35646 | 2025-10-11 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a97710b-5cd7-3e6d-a604-e11806ddb3fa | -13.22184 | -42.33416 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| e6ff1256-9cf2-3e14-a71b-7a0fcb5cd1a3 | -12.24568 | -51.14022 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b454453a-8703-31bd-9df3-ac4922eb81d7 | -13.38753 | -47.73372 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b17ab0-7449-396e-a668-0ff7717cbbc6 | -12.69062 | -51.19489 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec2c44d0-781d-33d6-9e2b-d3e708d24476 | -13.32695 | -47.12365 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a30297f1-8aa0-3041-965f-49b8c5229179 | -10.16016 | -44.55277 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c20cf46-2bb6-340b-9ab4-521ebe46f8e0 | -13.26768 | -48.01328 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef046ae2-819c-37a4-95b2-cc8cc85f0ea2 | -14.95721 | -46.75016 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98218771-7bcf-3f78-b539-41a114223fb2 | -12.72869 | -45.843 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80a3a9df-61a7-363c-a423-51defe8a6ccb | -13.30279 | -48.49639 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea8c3e5-b65f-366d-bd12-3957bec760ed | -13.25987 | -48.01946 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1a4c51-5b85-341c-8d13-3325b9f20c5c | -14.71022 | -47.43544 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4b2cf51-e1e7-3b7a-b6b4-50782ad47d3e | -12.95367 | -46.48001 | 2025-10-11 04:34:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 338907c1-ea0a-3a1a-97d4-48ced49a96f2 | -14.2777 | -45.90406 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7073f00-c0f9-36cb-9d8d-4719c52cdbd3 | -12.90292 | -47.05423 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 73e8b5b8-f44d-3dae-8c5e-76755abf1068 | -15.06808 | -46.60485 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56b6a0c4-2517-3f71-97c2-80d19a523ca4 | -10.15636 | -44.55223 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9044b6db-2cbe-3f72-95b7-c9b5953ff684 | -11.87466 | -45.49276 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6d8f073-2ad4-367f-9f4a-a95785648a66 | -12.64439 | -48.31113 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e13e1029-775c-340c-8f08-a64f3c5e192d | -10.07623 | -45.92122 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e06170-a0f5-3103-ae67-88cb36c08ec9 | -13.38637 | -47.27139 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23bcc3eb-3814-371b-8507-9b5c2e719d02 | -12.4527 | -45.0748 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9a2fb43-7343-3bb0-90bc-4b8d0b0e0da7 | -12.49937 | -55.74173 | 2025-10-11 04:34:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c1f1a0-5b96-3237-aaf5-c693ab49cad0 | -13.25488 | -48.02967 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a1c49f6-76eb-33ca-901b-6de6efa98f0e | -11.76476 | -46.3713 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f04bfeff-f04f-3b16-a537-f73d5405b569 | -10.19408 | -44.61164 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1177a6d9-9254-31f4-a34f-dcfe46c2933c | -14.96257 | -41.69247 | 2025-10-11 04:34:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| feb467f6-2863-303f-8fac-acf0f1433c80 | -11.63323 | -55.00797 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59d1a109-ddd2-3b03-8c74-f7c5ee3ec3c7 | -13.30665 | -47.11741 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71b39949-6ff5-319c-9cb4-338ccfadafcb | -15.68724 | -46.64032 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 077c39ff-c56d-32b3-b95d-8a8826092edd | -13.26041 | -48.0159 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc947f09-ba62-329e-89b6-02e06ff7ca67 | -13.84126 | -45.79251 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a28f39f-a308-3a3b-9b63-ef643bb61eeb | -8.93157 | -47.20554 | 2025-10-11 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1858a3e1-4184-3d05-b52d-e879fac24184 | -13.4051 | -47.75521 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
