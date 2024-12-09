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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b452b337-ef76-369f-9fd2-62f5e88b9407 | -17.09376 | -43.80456 | 2024-12-09 03:57:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a25ceee7-2758-3f62-922a-54ff744630f2 | -18.30779 | -47.19031 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f89b1af-6499-3281-9774-960516dc972e | -18.30365 | -47.19504 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c5ab29e-01b8-38df-8371-0dc25cf7bada | -7.75005 | -35.26257 | 2024-12-09 04:10:00 | AQUA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| ce2b79ec-e29f-3921-8edd-0f2a11e4878b | -6.96111 | -34.91627 | 2024-12-09 04:10:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 9ad65218-5ed9-3104-a956-f887fc7feaab | -7.74531 | -35.25666 | 2024-12-09 04:10:00 | AQUA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| f0867a71-21c0-3997-8bfb-1916133aa9f8 | -6.96432 | -34.92429 | 2024-12-09 04:10:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 4b2b0f17-e6d3-3bba-9492-4208d8961dc4 | -10.23889 | -36.28363 | 2024-12-09 04:12:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.1 |
| 209139a7-b265-38a0-943c-61c756b49a94 | -10.23405 | -36.31067 | 2024-12-09 04:12:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 82e7bbdb-8f00-363f-8ca7-1ffeb6105fc1 | -10.23515 | -36.30306 | 2024-12-09 04:12:00 | AQUA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 0b419362-a593-3d6f-b67e-874c520f0946 | -3.81758 | -52.36033 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8e05a68-e685-3ce4-bf2e-1b4222bc243a | -3.81812 | -52.35714 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 076c5ca5-3385-320f-a651-0a22d2f31cb6 | -2.46757 | -47.96251 | 2024-12-09 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db69f042-9d0a-366f-aef5-0d86af36213b | -3.3502 | -39.8976 | 2024-12-09 04:16:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9809329e-a0a8-33b7-9f45-4bc45c15533d | -2.84031 | -46.69368 | 2024-12-09 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 165667fb-914e-3f77-a8d0-5dcb426c344e | -4.07564 | -46.71313 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba4ff5b5-5445-3cfe-a039-51004d14191c | -4.06127 | -46.89067 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86ed28ff-96cf-3723-beac-ae96f5ed3693 | -2.03204 | -46.67029 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc9f4a68-20c8-38b7-98c2-5e837b837e47 | -2.62975 | -48.05744 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9285a206-8efe-344e-b163-cbc8cd48c142 | -1.69823 | -45.81286 | 2024-12-09 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678cfe12-3843-3c15-bde5-82d885d9bcbc | -3.00516 | -48.04025 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0a2c228-f531-3ea5-ad5d-1da8a8d6be4c | -2.24236 | -47.9908 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd946e2f-eb9f-38df-a9ca-edf594b9c59c | -4.08855 | -46.6545 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43289cf8-23e0-368b-af3c-f4271480f346 | -2.86211 | -46.71803 | 2024-12-09 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bde600cb-dad7-394b-a07d-85a077dc47a0 | -2.62588 | -48.05682 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c598687f-784a-3083-9311-a5264a8e0e50 | -5.4754 | -39.41181 | 2024-12-09 04:16:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 008b2498-31bb-38e1-97f3-4461bfee5b07 | -4.08435 | -46.72675 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4e04ea5-0417-3fc7-94ac-3976401ec191 | -4.09129 | -46.70676 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66eb3714-802f-3544-a7e4-4727ab97b312 | -2.62897 | -48.06227 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae60dba5-ffea-3b38-a964-ab90c81e1e54 | -1.60994 | -52.64003 | 2024-12-09 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4c9247f-0ec9-3316-8540-f47b2f2e8e50 | -1.60707 | -52.63855 | 2024-12-09 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcb50851-5a57-36fc-85e7-1ea6077e611c | -1.64983 | -45.91565 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd99151f-a8ef-3a10-8c3d-facc9b97ba9e | -4.07838 | -46.67308 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a28e2fa-97c4-3e94-a471-1883d0bbfc81 | -4.07855 | -46.71762 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f3001be-317d-3026-97ab-82462b4a3ebd | -2.6251 | -48.06163 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133c1e0b-2201-33ed-b847-647173a1f043 | -4.07501 | -46.71711 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57452cd4-d923-31d2-8212-36822e89206d | -4.05029 | -46.71312 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f217217d-ecad-375f-979b-c90c07442097 | -4.07981 | -46.70967 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8568e09-5f80-3fc4-89fb-298f3c3266bc | -4.05798 | -46.71036 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 843f9bf4-4887-375d-a506-9c4158eb9652 | -3.81328 | -52.36453 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe8f907-3aea-3222-9315-1f01232e3b14 | -2.46372 | -47.96189 | 2024-12-09 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59b7c4ae-1077-313b-8299-dc314818cd7a | -4.0819 | -46.67362 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be9f4f7-07d3-3196-8dab-7dfa534a9a26 | -4.69832 | -45.28664 | 2024-12-09 04:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d92df4f6-b6ad-342d-a250-86ca92c0f90f | -1.84322 | -47.45087 | 2024-12-09 04:16:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b675715c-c237-3baf-9db0-6a31c47a0dfc | -4.08852 | -46.72327 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bbe988e-b053-3aaa-99c8-a82b407b55fb | -4.08834 | -46.67858 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dc7c503-3629-39e0-b4f3-1a53c5c4e1d3 | -2.90124 | -40.44013 | 2024-12-09 04:16:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf8bb2db-21df-3242-801c-c4041827d0f8 | -3.005 | -48.12646 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b32af58-6c70-3025-b988-26aee9da5326 | -4.04741 | -46.7085 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 913d67e8-7414-3bec-86ee-91d4f9665a39 | -4.09165 | -46.70341 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1075d752-59d2-34ce-8c29-ac3c40258562 | -1.777 | -45.9111 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e55cbd26-678c-3578-ae63-e7a2b7f8a41e | -4.08938 | -46.69492 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b05b232-3520-3e3e-9de0-b6194c23ce1a | -4.2015 | -46.29118 | 2024-12-09 04:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bdfca2f-377e-3f41-9709-a1fbed005c88 | -2.828 | -40.40418 | 2024-12-09 04:16:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79f2bc4b-54f3-3752-b06e-8a1e291cd5b6 | -1.1936 | -46.66481 | 2024-12-09 04:16:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b76ed53d-e9b8-3fab-bba7-9dbc9503a88c | -1.78048 | -45.91166 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e676989c-1fe6-336a-bc03-5c4998c870c8 | -3.00679 | -48.04322 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cbb86f5-dfcc-310c-8f06-f7fcda3f6735 | -4.05903 | -46.887 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8c3fbf-9a58-3f67-8d1c-e6683bbf318d | -4.08562 | -46.71872 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 423b8566-2803-325e-bb33-2fede45927b1 | -3.14072 | -45.59973 | 2024-12-09 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8862bb3-935d-3c81-8cef-b8d9fc2e7235 | -4.09103 | -46.70737 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f55d9407-c130-3b64-b81b-4e2111d24895 | -4.08081 | -46.7262 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b5979c-570b-35ee-915b-860349a5da26 | -2.84389 | -46.69424 | 2024-12-09 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5285e9cd-dc91-344c-9f57-385db8e7139f | -2.46668 | -47.08678 | 2024-12-09 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 603dac1f-b7c7-37b6-b5c5-4677399ffe3e | -2.90597 | -48.01944 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca6179a8-7018-3545-b1ec-0d445a965092 | -2.93637 | -46.70294 | 2024-12-09 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd3fd0a0-ebc9-32c8-b3ae-e45daab921d5 | -2.90753 | -48.02245 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bcc1907-e78b-32dd-a4f9-45bf196f446c | -2.03565 | -46.67083 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24bff77f-ab31-3370-bbf6-56f2750d880d | -1.64408 | -45.90683 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74546369-1219-3ff6-80ec-7fa13edcc406 | -4.0887 | -46.72263 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c1461bc-5668-3586-8f7c-56ddf47d656f | -4.08334 | -46.71023 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ceb9fa-4431-3d81-9393-ccc3648319d0 | -2.62124 | -48.06101 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2cb19be9-3145-3736-85a4-d2b0a4115c77 | -4.5475 | -48.01525 | 2024-12-09 04:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c15bfe20-61c2-36e5-9d8d-b4e9570512db | -4.08915 | -46.71928 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42d54f18-47e1-3296-a4f9-c58a4b349c4f | -2.33066 | -44.60135 | 2024-12-09 04:16:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10bed327-b8e6-3c9e-933c-e29f9f39abf7 | -4.04805 | -46.70452 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8c85a63-61f4-3706-9d69-750607af512f | -3.84292 | -41.569 | 2024-12-09 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d9e8c2a-36b6-3b16-98ac-fe428a7467ba | -1.45214 | -45.81468 | 2024-12-09 04:16:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113da30c-3678-3ee0-90cf-04cb3cb099fd | -4.54825 | -48.01071 | 2024-12-09 04:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59616235-76dc-3def-aaf3-acfa217c57b9 | -5.13163 | -44.39544 | 2024-12-09 04:16:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 109616a6-f61f-3897-9c6d-7c1a29cc2ba9 | -4.08451 | -46.72609 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 524da1d2-d219-3e9c-ab1f-5477557eaa3d | -4.08543 | -46.67415 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0011cfa8-40d8-35e1-8c4c-522e40f8052e | -2.04884 | -46.63487 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3957309d-fd26-3260-ac8c-59d2ce9983d1 | -4.07274 | -46.7086 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73413b9-e0c5-38b6-9162-ae6fe1482b72 | -4.04253 | -46.67117 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5270d4ce-099a-311d-afba-73d71c32b769 | -1.64818 | -45.90352 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b24816-5d75-3f2a-9b8c-4c08eb065145 | -5.18769 | -43.9307 | 2024-12-09 04:16:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0b95cd8-b961-314c-bed5-cbca3667f0e3 | -4.05192 | -46.88577 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f99031-2060-399f-9dd5-de0e99d49ad5 | -4.05093 | -46.70913 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52399e98-7cfd-36d1-aea3-041331ac71d1 | -3.8119 | -52.363 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eef92401-acd1-3a1f-85d6-02071ae0a0ec | -4.04677 | -46.71247 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96d69a1b-11f5-3828-ab42-3c353dff314a | -4.08711 | -46.71017 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e09f8d54-2291-3ce7-8d48-b99d8b11e398 | -3.91785 | -46.72626 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87087b61-b653-36e6-b01f-3ac8f9b148d4 | -3.96625 | -46.96363 | 2024-12-09 04:16:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 503db4ad-c5fb-364b-9a96-0df156636aa9 | -4.06033 | -46.87409 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e29c2c0-5343-36c9-84b4-ec033cfed992 | -4.06215 | -46.70691 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5306f3f2-0929-3ee7-8965-267fdb74e1f2 | -3.8574 | -40.44686 | 2024-12-09 04:16:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77661fbb-6466-3b83-a584-3420e365d52c | -4.08499 | -46.72271 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfa517af-029e-31ae-b690-bf44315936c8 | -3.3509 | -39.89303 | 2024-12-09 04:16:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43b26f53-11ab-3cdd-b94f-cf4478ac8154 | -4.0584 | -46.89097 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
