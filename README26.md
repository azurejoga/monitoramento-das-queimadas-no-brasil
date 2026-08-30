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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129eccbc-69ac-3219-b84a-44631de9883b | -6.8798 | -42.87916 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e288f13b-bf5c-35f5-8f37-981b8f47529d | -6.12945 | -44.88247 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 432f3f7a-a16d-33c9-ad01-29e09ede98e3 | -4.08247 | -45.94816 | 2026-08-30 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79e73631-1dcd-357c-be99-7ddbe4be9643 | -6.42993 | -41.55999 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93dc1d77-edfe-3aa1-8ecc-8441c6264109 | -5.46107 | -48.90926 | 2026-08-30 04:12:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2453eb69-07f3-3638-a7c2-a47d8077827e | -6.44082 | -41.53563 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7e27c4d-94bf-3c8a-8259-2be052881545 | -4.37052 | -47.77204 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| aa48633e-2ce1-3f6b-9cf3-c2d344478a4d | -5.04299 | -44.69288 | 2026-08-30 04:12:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9f89dc5-8cb5-3d32-a3f8-8536fc972a55 | -6.87477 | -41.66069 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 104dfc06-37ce-3fc6-86b8-cac2fbca8b1f | -6.35042 | -44.10096 | 2026-08-30 04:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3b494ea-ddbe-35d2-9718-bc7808900b8f | -6.89471 | -41.75319 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a87a64aa-57fe-3645-b185-329ae1152015 | -2.95407 | -43.25219 | 2026-08-30 04:12:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19c1f042-df6c-3ff5-94a8-1bd7f8259581 | -6.43906 | -41.54655 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6de2f957-48db-3907-b822-7c24b0456603 | -1.32738 | -47.56412 | 2026-08-30 04:12:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| daa24df8-76c8-366d-ae2c-1c724de89d9f | -6.43684 | -41.53872 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20d19396-343c-3a53-912f-ef524fcfb63e | -5.89068 | -47.72844 | 2026-08-30 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85df5994-7c19-3a59-a358-15c231829fb6 | -2.93983 | -41.73635 | 2026-08-30 04:12:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9faf8443-1399-3198-8207-ef315c9f3231 | -6.89411 | -41.75686 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf702775-c16b-3a39-9488-4b5a31540af8 | -1.32218 | -47.56324 | 2026-08-30 04:12:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbc8d1cf-b54b-3bb8-ad9f-694ba2b9664c | -5.45574 | -48.93915 | 2026-08-30 04:12:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31a655ae-7756-30ff-8df2-4085c27a3a91 | -5.50261 | -44.01902 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df596056-3038-3e4c-89ca-0c6bce78e82d | -5.31556 | -45.2576 | 2026-08-30 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08791677-f947-3d7c-9b8c-f1020bbe0bb8 | -4.37088 | -47.77732 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6b466b99-5b71-33a1-ae25-a92e257b4e81 | -6.84852 | -42.86985 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 21e1337e-d9a0-322d-b274-0462035c6b71 | -5.99607 | -45.08496 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30e80e8a-3e42-31e3-8788-1c00f8859488 | -5.04356 | -44.6894 | 2026-08-30 04:12:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8b61580-5c07-3477-a67d-e8e6569252fe | -6.87079 | -41.66381 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bfb0be5-2b3c-3bb7-acce-8bf3c84c673f | -6.18283 | -44.58348 | 2026-08-30 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 917861b9-9147-36ad-95b6-68fc25a835c7 | -2.47992 | -46.85551 | 2026-08-30 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba76078-5fd0-333c-9e9e-251c686808c3 | -6.87914 | -42.88321 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| afea8622-ee0f-30df-b93a-0332801cca37 | -5.50311 | -44.62431 | 2026-08-30 04:12:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d90c9da9-b890-3c8f-9cab-dafe2776bcf7 | -4.27075 | -48.66125 | 2026-08-30 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 751d8684-d524-33e5-9f44-04a69d93ecde | -3.36408 | -39.82008 | 2026-08-30 04:12:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7eddbd51-e62a-33ea-83a7-adf693af8a4c | -6.86739 | -41.66328 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b5d7130-f703-3882-9313-e81b4de0ca44 | -1.58311 | -47.73978 | 2026-08-30 04:12:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27ed636d-7297-366d-b80c-b0dbcc78c327 | -2.00226 | -44.79783 | 2026-08-30 04:12:00 | NPP-375D | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa32c8d4-9b89-35f6-bed2-48ea8d662ad6 | -3.18797 | -48.02194 | 2026-08-30 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e11dcbea-6204-3ea9-a743-6f812da17ef0 | -6.86562 | -41.67427 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3c82ae73-57a7-3f95-9532-6386c92a3532 | -5.99199 | -45.08431 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dab0848-26ce-31b5-acf1-458fe1346b24 | -5.45822 | -48.90924 | 2026-08-30 04:12:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2308a2e-b44a-3ce8-8747-c39795f32e61 | -6.86341 | -41.66642 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5ce7912-6bba-3189-984c-260768b7aaea | -6.88045 | -42.87514 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f50d50c1-4a69-35f8-8e23-f0e571fd9c6d | -5.60674 | -44.11678 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd8a937c-1640-3e76-b86b-a155292e608f | -6.86504 | -41.67793 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 18978c21-fef3-329a-b39f-bda429c7bc8f | -5.99724 | -45.07784 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc96b11e-d7c7-3bbc-8292-cbc9ecec8110 | -2.03489 | -48.78444 | 2026-08-30 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0bdee9c-c62b-3ee6-9430-0caf7f9fd9b5 | -6.86798 | -41.6596 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7df8fb0a-3c68-376c-bc10-f05791115076 | -6.28834 | -37.67797 | 2026-08-30 04:12:00 | NPP-375D | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86c4f947-71e2-3018-b9cf-59d5fafc1a9d | -5.63963 | -44.97887 | 2026-08-30 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 122d5f7c-f980-3ce5-bec0-f761b122c0f5 | -5.60516 | -44.12642 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64b21a27-2678-3ad6-9af2-c16540d64b5e | -6.86961 | -41.67115 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 629496e3-9767-31f7-bcb9-38f0131df6bf | -6.34739 | -44.09555 | 2026-08-30 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3dbdfd0-ace4-35bd-b145-98d549ecd767 | -6.89072 | -41.75628 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8141bf1d-ed88-36ca-9805-2f19fd2f432f | -6.82878 | -42.87894 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb71ddce-1359-38bf-8797-457e4e94079f | -6.43228 | -41.54545 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4b6d14d-7559-33cf-9496-a79bd4e90e0f | -6.833 | -42.87549 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fbd81910-cf01-317e-8db7-e094331a420d | -7.25165 | -39.31225 | 2026-08-30 04:12:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ec6f195f-4d18-3267-9543-d531d236a25e | -6.3436 | -44.09484 | 2026-08-30 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc624636-af70-34a6-b891-b8bc7bbde1be | -6.83005 | -41.74347 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1dcbd393-8222-3e30-abcc-c4f478d1fcfa | -6.83012 | -42.87087 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3e440754-f63f-34d7-b802-8129a8b92503 | -6.92396 | -42.6748 | 2026-08-30 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 810a098d-8089-312b-9d9d-d74b4cb1e1d0 | -2.48238 | -46.85741 | 2026-08-30 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e063cbc-7458-3819-9692-8ea54d451874 | -5.1973 | -45.26942 | 2026-08-30 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79cd67e7-789e-3f92-a1e4-7e5030b6b2fd | -5.76675 | -35.74723 | 2026-08-30 04:12:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f24fbc28-6286-3e08-b812-a3f1b228fc08 | -5.50338 | -44.01431 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c77c04b6-c4b9-31f2-9cee-1290291d52c2 | -5.46354 | -48.91022 | 2026-08-30 04:12:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 957660eb-efc8-3286-8dda-fc0d31d64d27 | -6.86459 | -41.65907 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca9950b6-a3c0-38cf-996e-8ed1c2356704 | -2.88586 | -40.46003 | 2026-08-30 04:12:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59ec60aa-0c85-30b7-b30e-f3ecd521f420 | -5.77312 | -44.20342 | 2026-08-30 04:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fa66ad1-fab3-3217-a8cd-775b8f2ced1e | -6.06816 | -44.87882 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e97eb34-4bf4-38eb-9056-8996994e3dd1 | -6.8668 | -41.66695 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd6fcce7-b14b-3660-8530-4a0b9cc7baaa | -6.86105 | -41.68105 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| aa3ffc3e-83b2-3b74-acdc-37f23498d848 | -5.52673 | -44.38391 | 2026-08-30 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0d840ab-ccfa-3b73-9629-24d945d08757 | -6.77492 | -38.21079 | 2026-08-30 04:12:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 574b81f5-4a8c-333d-bd6e-11c03b6ff7b3 | -4.07803 | -45.94735 | 2026-08-30 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 958dfbfe-403e-3856-99d7-11fdffd53258 | -5.60751 | -44.11203 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07847929-3874-3330-80f0-4e7f0b7d5f18 | -3.18278 | -48.02098 | 2026-08-30 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dca8cdac-ace1-3590-a73c-cbcf39756177 | -4.97644 | -37.23677 | 2026-08-30 04:12:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 854b0d0c-3f62-3077-afa5-7fd06f334b04 | -2.10869 | -49.00149 | 2026-08-30 04:12:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d84f9593-89ce-3c1d-a15b-6e0ea6f6a6bd | -2.79916 | -49.58513 | 2026-08-30 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87410f89-f38e-3f00-944f-7ce78fd40ff0 | -5.49954 | -44.01371 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5c12f7e-f264-3633-8904-0a89d5aac8a4 | -6.86915 | -42.87736 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a4652e2a-a8ec-3e46-bf33-1da32a1accb3 | -6.34282 | -44.09954 | 2026-08-30 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 41e0e7ab-8e66-3af0-98b0-cf9d8d9bd236 | -6.8685 | -42.88139 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2575f7fc-48fa-3938-bea3-db4086aed858 | -2.95121 | -43.25353 | 2026-08-30 04:12:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16dbf77b-260f-3daf-81e8-09006f7dec1a | -6.43651 | -43.07766 | 2026-08-30 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 275b3781-e2a1-39c7-82c6-112cc2b65d00 | -6.8702 | -41.66748 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26eb626b-f807-351b-bad3-7e0e3fcf9196 | -5.60596 | -44.12155 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 736fd25e-6233-34d4-a261-29b4e1e084b6 | -6.43139 | -41.78962 | 2026-08-30 04:12:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48b67c85-b15f-33a9-9b87-1208751b577a | -5.8858 | -47.72757 | 2026-08-30 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd4deebb-cc5c-3838-8eb3-64f1eeafde38 | -5.99547 | -45.08855 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3962e482-e041-359a-a359-e511d18b7ab4 | -5.31971 | -45.25838 | 2026-08-30 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c182172-1c8d-3443-b11c-bc23fab70fe2 | -6.82945 | -42.8749 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c24f68f-4a9d-3f9b-91e3-ffe5b4d30b85 | -6.82589 | -42.87434 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e75c0a73-913d-3756-8963-6e2578197318 | -3.85492 | -40.97076 | 2026-08-30 04:12:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9838ce4c-aaa7-3c0b-82e2-32286ffd130c | -5.88813 | -47.73287 | 2026-08-30 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2cacf76-02c4-3dfa-9e3e-f4adee1edf78 | -2.11176 | -49.00288 | 2026-08-30 04:12:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 404ef4de-fdd5-3852-8e86-a989e8f39516 | -3.22224 | -49.22627 | 2026-08-30 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3260a459-6bfb-378c-ac86-2b21fff047fe | -6.87138 | -41.66014 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0709dc56-59a3-3159-81ca-6139b2086bdc | -6.43509 | -41.54964 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
