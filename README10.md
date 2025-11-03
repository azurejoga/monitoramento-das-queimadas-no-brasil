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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4ab47cb-c87e-35aa-9457-bd0c286d3a79 | -6.68236 | -46.67597 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fc91b8c-74cd-3d72-a15f-a2fa57ba6127 | -3.84829 | -51.32665 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1552c3cf-6d68-30e5-a8db-3344508d6c2e | -3.12249 | -51.20976 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b17af419-2b85-3806-9053-27fcd0d7bbb1 | -6.2233 | -42.68266 | 2025-11-03 04:50:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0b7ed220-8ab6-316b-b6a1-800331be4dcc | -3.14521 | -49.4724 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cef3861d-7a01-3187-a1ab-d92b0cd860e9 | -4.21361 | -44.22689 | 2025-11-03 04:50:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4212a2e9-a8b8-31e6-a1e0-fa86a7e70b4d | -3.45303 | -50.22288 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f8609af-846f-36df-8447-1731dd5e4ecb | -2.90477 | -53.95774 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5536d6a6-7505-3ecf-9878-df06f57e9baf | -2.83666 | -49.40778 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cd54356-3293-3085-9002-47cd9966538b | 0.99198 | -51.22498 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d8a310d-1d7c-37ee-a580-eaec6c7e3e3b | -3.45359 | -50.21924 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbc6206c-51a3-3846-bb80-ec15980d83c8 | -5.02991 | -43.62096 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1d8f449-7ac3-3320-80ed-e8df7f1bc045 | -4.94867 | -45.51475 | 2025-11-03 04:50:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 075934e2-f476-3fcf-a9d2-02638b2808d7 | -6.68297 | -46.67194 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf0ddf81-3354-3c50-b267-38d30fe87efc | -5.65644 | -47.52346 | 2025-11-03 04:50:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ff7df6e-34d3-3213-8def-342137ec7b49 | -2.6635 | -54.76678 | 2025-11-03 04:50:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 283f10a6-5843-3ce1-b870-0744878be32d | -4.2128 | -44.23226 | 2025-11-03 04:50:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60749d80-37e6-3079-a209-f3ad0e4b5cdc | -3.23824 | -50.79591 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9e7ead2-20f3-3839-8c83-b15204aa65f9 | -5.03415 | -43.62796 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174b4f79-17b8-3c1e-a1f3-5bc9234eb564 | -0.89537 | -52.03698 | 2025-11-03 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5fe2f74c-a79a-3b33-bc71-746c635df137 | -3.29719 | -51.91414 | 2025-11-03 04:50:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f41622a-fac2-338c-b8a4-c67d53a4510c | 0.99474 | -51.22103 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eee32d9-9cee-3ffc-afc5-9b477db55b4a | -3.38665 | -54.27748 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82e6f79c-6135-3c33-ad48-e98c171d994f | 1.62132 | -55.63995 | 2025-11-03 04:50:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a4fe4f8-da54-3944-9dee-a6a8ffc7adc7 | -4.9622 | -45.5169 | 2025-11-03 04:50:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5439958-83d1-3460-a216-da57f677e1b6 | -3.44087 | -51.47527 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 806f53f9-1018-335b-bae2-23de3c57785b | -3.15876 | -50.82697 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 487aadad-8b54-3404-b8c5-7388ea31f1f0 | -3.01907 | -51.3703 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abef6647-20c3-3636-948b-96e714ec2e0f | -6.6818 | -46.67108 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d456254b-cd16-3d66-a134-3dc333f1fc70 | -3.11863 | -51.2127 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea5888c-3a2f-3c10-b36d-2e613610ee8e | -3.40225 | -50.27462 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7959db36-41a7-37a7-93d2-fd6aa72ec71b | -4.65925 | -42.52279 | 2025-11-03 04:50:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6602475-217a-3479-ad51-d106ccc9a6cd | -2.83259 | -49.41107 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc1deaa-3274-3632-ac63-b3baeb63db04 | -2.09642 | -49.97588 | 2025-11-03 04:50:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41397026-01e1-373a-aac4-e1672b72dff5 | -3.45698 | -50.21976 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 352b37bd-81cf-35ef-813f-65e61ec8ba88 | -2.78246 | -51.79411 | 2025-11-03 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| faa9ceaf-3ec6-3308-b4c4-19eaab48aef6 | -2.83725 | -49.40394 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19c4582d-8fdc-355c-b93d-ab5ebd5cfe99 | -5.42929 | -46.36094 | 2025-11-03 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de81a72e-f76c-3626-920e-b56ea4412bc4 | -1.81906 | -52.04067 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b7a6f9-0f50-3bfd-93cc-559deb4c0c7e | -6.84719 | -46.29414 | 2025-11-03 04:50:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 050d553c-d577-3ecc-a0bf-d0de1d6bfe8a | 0.99144 | -51.22154 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c959970e-3185-3719-b6fa-857772b938e6 | -3.14032 | -50.20527 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df921811-d9ed-3b5e-9ad1-5a185820e7b5 | -2.92913 | -54.02763 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5e4ac88-c604-36a6-a8e9-34f42138590d | -1.39809 | -53.08978 | 2025-11-03 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5fee0bf7-7320-312a-a865-492b5e56068e | -3.0163 | -51.36634 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133ce152-8e51-3ded-976e-3663fcafc3c1 | -3.14462 | -49.47625 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8803b65a-b50f-3507-af63-bdaaa8235579 | -5.72216 | -42.18802 | 2025-11-03 04:50:00 | NOAA-20 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b4f7f0a-de75-3ead-bd40-3198503ac9d1 | -1.96797 | -52.10975 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e160dc85-bb7b-3f77-929b-7215f396cf4f | -2.65341 | -48.51005 | 2025-11-03 04:50:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f758173d-fea8-313f-990f-0ad5f031efd7 | -3.23589 | -58.88839 | 2025-11-03 04:50:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9d7ed83-0c1f-39fb-99ec-4497fc545ea1 | -3.22356 | -50.58816 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 586c376a-8361-3552-9d60-33f08bf294df | 1.00081 | -51.21656 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c0590b-d428-3132-b562-c32b8c9f7ea7 | -4.10371 | -54.11562 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35974435-b304-3bfa-972e-e63aeedb4c18 | -3.24212 | -50.79292 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efcc1e07-1a97-3c78-a218-cf9160b89fcb | -2.96114 | -47.00664 | 2025-11-03 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 868650cf-b689-3dba-b6fb-0bb4de25d708 | -3.86338 | -54.58104 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9070c72c-85d4-30e6-a243-31ab5b0812a2 | -3.46095 | -53.04467 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a53550bc-ff10-3575-b595-bcfc51b61902 | -5.42866 | -46.36509 | 2025-11-03 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5074a2e8-3c89-3de8-ae9e-db5bf0dd72b4 | -3.38727 | -54.27364 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b69e160b-38ed-3cf1-b018-28a8efa0b86e | -3.56045 | -54.57186 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fb4e0fe-2263-30fd-a692-08e9e98b089f | -1.93805 | -52.70855 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b8284f-9425-3d8b-9ce0-2f3a006da0c1 | -2.83378 | -49.40342 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d08cae2d-2897-3dfe-b5e6-546f469b77cf | -3.24157 | -53.27279 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c1021f6-4e21-3134-a816-1e61dbfe529d | -5.18117 | -60.30717 | 2025-11-03 04:50:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8656c7d5-6464-3452-ba23-c54aa36665c9 | -1.96743 | -52.11319 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74e11311-aeb0-37be-9aed-2946a3eeee9d | 0.99805 | -51.22051 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4657ac20-3646-39df-9ea8-8c2c2e498cb1 | -2.94095 | -51.41458 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52609f16-1513-35cf-99ba-8fa6bfc77ed6 | -1.94329 | -54.14778 | 2025-11-03 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6e0654f-38f5-3be1-8e1a-1f7389604715 | -4.70187 | -46.45419 | 2025-11-03 04:50:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f8d10e-037d-34a7-9d05-a38107443797 | -3.84498 | -51.32614 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc9805f7-1d7a-3dbe-8446-14588e22b64e | 1.00411 | -51.21605 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624c6bfa-06df-398d-bc5b-f571931b56df | -3.39013 | -54.27803 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03f1cd26-c6e7-32b2-984c-bbcea47b75dd | -5.03035 | -43.61793 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f048aa-b375-3eb2-8f7c-a0f13378a480 | 1.62078 | -55.6365 | 2025-11-03 04:50:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55a77f89-d17c-358a-b2ea-1fa55e1dc70f | 0.69404 | -51.44843 | 2025-11-03 04:50:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de439bd1-dc00-39ae-9a0e-05380b30b43e | -3.39075 | -54.27419 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f329798-23f1-3765-9fdb-5a1a74dc11e7 | -2.63477 | -47.29874 | 2025-11-03 04:50:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02890dae-ee19-30b2-b596-0f7594551881 | -3.45642 | -50.2234 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d62d2bba-b8a6-3578-9087-89ec36abf662 | -3.13873 | -51.58274 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 847dd535-e041-3272-8dc4-045e32c5a121 | -1.27313 | -53.85441 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734014fd-22c6-3b10-a94a-c6d649c625bd | -0.89315 | -52.02954 | 2025-11-03 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 05d66e26-d8f2-3207-87c4-74e5a8b2bbef | -4.70608 | -46.45489 | 2025-11-03 04:50:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4eef3e2-c842-34c0-81a7-4ca72ede8817 | -6.22278 | -42.68642 | 2025-11-03 04:50:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b8254067-d1ed-3397-8a02-683ae9c54ac8 | -0.89592 | -52.03352 | 2025-11-03 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f9aee0ea-8b64-3301-904a-31163d8cf674 | -6.68552 | -46.6757 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a6ec47-deba-3351-af62-d7402e9fffad | -3.71042 | -51.1881 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f766ca03-4ec5-3a63-8c92-52af387dca1a | -3.66438 | -51.71812 | 2025-11-03 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 718705bd-6ae6-3e64-b8eb-4f98d6b5ef27 | -1.39867 | -53.08615 | 2025-11-03 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f596bdfc-8d7e-36f2-8e7b-2c735f6314a5 | -3.24267 | -50.78939 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75416010-c9f7-381b-9ac1-344becbd4643 | -2.26926 | -47.85646 | 2025-11-03 04:50:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a885af11-8a5a-3139-8238-941e73ec98f7 | -3.66769 | -51.71864 | 2025-11-03 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4251933-a758-3b60-aecc-14c8336cf75d | -3.82623 | -52.39214 | 2025-11-03 04:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b332c16d-8e72-31f1-894d-5185b1ff4cba | -5.03079 | -43.61489 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e3b063-a6e4-3f79-b331-62960bd3c495 | -1.49788 | -53.1236 | 2025-11-03 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282cde38-4d13-37ea-a7a2-e40bd1d627e7 | -1.50786 | -55.37357 | 2025-11-03 04:50:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0611a87a-4d14-3c2b-9146-f346f6fbaf94 | -4.25794 | -44.25057 | 2025-11-03 04:50:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bb4795b-d52d-3c91-9836-e3a6909296a3 | -5.04065 | -43.61956 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 636d78ec-6769-3cd7-a72d-209e9f42de49 | -5.43213 | -46.36076 | 2025-11-03 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb73288b-add0-33c1-ab87-fce87b50b538 | -3.5579 | -52.8835 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeb71431-43fe-3112-86b3-2235901513ee | -2.69294 | -59.81567 | 2025-11-03 04:50:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README11.md)
