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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc0a80e-5c27-3c90-961b-5fad9db2e4e1 | -5.97894 | -47.06931 | 2026-07-01 04:55:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf5bbee6-c8ca-378a-8759-d7a7823c4f3a | -9.69555 | -47.69311 | 2026-07-01 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dd17e94-6c0c-3621-a5db-623e5b764f98 | -9.16665 | -58.06858 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac4640e6-67aa-37b1-8446-aea28acc393c | -8.50819 | -50.14999 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 569806a1-cfba-371b-abe2-c78e81227b1b | -9.33174 | -58.02144 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c40f1042-42fc-30a9-a3db-e7316dd98df2 | -10.12131 | -52.08537 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28d776e6-01db-32ac-917c-dd70fd5901d5 | -5.8117 | -43.79642 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9d3691f-9e4d-344d-99d4-e4f6160f5304 | -9.02389 | -59.53899 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 808bd72a-7737-3b9c-864a-e363713dc87e | -7.74878 | -44.19268 | 2026-07-01 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee0a2fab-265f-3395-963e-5ecb16a64639 | -9.08166 | -59.48917 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09272ccf-5983-3904-8e59-d87a917926b6 | -6.42797 | -55.79897 | 2026-07-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35622d99-b821-370f-aca3-9f490df59ebb | -9.1754 | -58.06484 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75b0a2ef-5344-37c6-bd62-cdc8c6c04abc | -7.01186 | -50.07655 | 2026-07-01 04:55:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8070ee6-b280-3c23-85a0-d617ed1b69ea | -9.88339 | -50.39938 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e901acfe-a7af-33a0-a1e1-329407967ba2 | -7.28965 | -46.25382 | 2026-07-01 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e62f2ec9-993c-351a-baa7-4fd921a2671c | -8.34558 | -46.81826 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aeccaf0f-d3bb-37fb-af6c-f5ce1571b364 | -9.17146 | -58.06416 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78aaa4ab-635d-3e18-96ed-4e49b9bec346 | -7.00354 | -42.7741 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 665dbc77-f562-3df6-8b77-4b34756535e7 | -8.13813 | -47.87833 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a9dfd43-a32e-3623-8cb7-94cc11d8155f | -8.64847 | -47.77002 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f348ee7d-3731-3b8d-9ea1-100e402962ac | -7.74397 | -44.18897 | 2026-07-01 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9dcb18b-1778-3fc9-817f-a4c4fba9b88c | -10.92374 | -43.04421 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d793412c-3f25-365d-8bb6-757f156fc215 | -10.12638 | -52.09735 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 012d285c-a04d-34db-b9a9-1564f319a013 | -11.91346 | -43.38885 | 2026-07-01 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b049941d-afd8-35c3-aebe-e4f5ecd7bd25 | -11.53999 | -47.45785 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6f9e258-1a79-3377-a3ea-b74a15709ca3 | -7.00303 | -42.77791 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8f7dcee-7dec-3f49-b068-8760fa7031df | -9.16752 | -58.06351 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd98ead-1f22-3a57-859d-f07321fa1f4a | -10.12976 | -52.09789 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd017d92-a833-39e4-9e0b-3d9d5e667476 | -8.59671 | -48.01113 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f612f09a-f070-31c1-80e3-5b3ea0167400 | -10.4373 | -49.58506 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f531edb6-a815-3fdb-b7e9-b98d4224b282 | -9.11751 | -58.25875 | 2026-07-01 04:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26061475-c1af-3bbb-9d02-d30a9b7fa469 | -10.59846 | -53.45119 | 2026-07-01 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e4fe48a-4916-3e64-9d76-7eddb3bf9ddb | -8.12131 | -47.87947 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c788a450-5bb9-3d6d-b670-c770376874d2 | -9.60203 | -56.92208 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43477373-3b52-3b0d-be9c-b7503bb9e26c | -10.12694 | -52.09372 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9871a57e-0e4a-395e-af5e-265d64d8e1c6 | -10.12301 | -52.09682 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e7b94460-6395-3911-805a-a5527a6b41ba | -5.81227 | -43.79707 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fac529f6-f66e-3236-ad91-e6d9d572896b | -8.50224 | -50.42659 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fd48ad5-d727-3ee9-ae5e-cbde47a89445 | -9.08783 | -59.48936 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8ad9566-d533-35bc-8315-5b98e2ce9c48 | -9.88464 | -50.39104 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da9db2b-1f84-363b-943e-282e0c19011f | -5.5562 | -43.96622 | 2026-07-01 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78207c6c-0dc5-3ae0-b5d7-d4ae0122a287 | -4.34783 | -47.76009 | 2026-07-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2d4a13-9141-300e-97b9-0f085860662a | -7.7526 | -48.84388 | 2026-07-01 04:55:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2251f75-3501-30dd-8393-bd993e05dfcf | -9.32868 | -58.01572 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b265c19-c9c8-39a7-bdaa-c9b9904a4b3a | -17.71863 | -46.79692 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9c8d17b-b848-3076-8d3c-6b5308931e4f | -11.90564 | -57.38792 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46d7f4bf-1b2d-3071-85e5-6bfd29151fa3 | -11.63342 | -59.00928 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44421ff2-6819-3706-8aff-9c738f9ce72e | -17.44144 | -47.16413 | 2026-07-01 04:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e3981e-6bb8-3a9e-af10-1d207cc19fe3 | -10.66796 | -54.53064 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7a12d2bc-1df8-326e-9963-877f82a16959 | -12.41582 | -58.40127 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4adf1ff7-85a8-3a30-8bc7-6cf498f7c91a | -11.73917 | -57.83714 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca68fde-6957-357f-b4ac-98fa40b7a3c0 | -17.71395 | -46.79316 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc867bca-2935-32b3-a31f-013ada92976d | -11.42606 | -56.05938 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8a755ca7-a770-36f8-a8f1-332999e5d6d9 | -15.07667 | -55.81105 | 2026-07-01 04:57:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b8db273-efbb-3499-ac3c-bdd9e75008c4 | -10.93521 | -58.60046 | 2026-07-01 04:57:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29653f76-3882-3a9c-a1b4-e34d23296247 | -12.83008 | -44.35582 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 0dee2cb3-bda7-33b9-bd8a-6d44515de3b1 | -12.41449 | -58.38612 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59284a31-1afc-3313-b151-79533d40f009 | -11.4267 | -56.05553 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8c2eb797-2d2d-3ea9-bd2a-8aded03f5231 | -12.76508 | -44.47818 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f64b785e-c7ec-3390-8753-28dce176e74d | -11.62752 | -59.01927 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c0a3e8f2-e918-3a2d-bdce-c58dcd348ba8 | -11.42261 | -56.0588 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 788e6cb6-ac07-3f21-aa4f-546363aa14a1 | -11.50476 | -54.50447 | 2026-07-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dce00ac-a04f-3712-91ff-9c1f228409b1 | -17.71362 | -46.79609 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3de89489-80c8-3650-a92c-c613bb74a07e | -11.04203 | -56.92181 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dde3f3e-dbcd-373d-8ab9-9717f6a3e969 | -10.68127 | -54.53283 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d6c96b2-9f4b-3e1f-8f45-74eb091e7398 | -13.72458 | -47.87436 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efc43d70-80c4-3efc-b725-074ca15b4c41 | -12.41283 | -58.39577 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ec54369-b0ca-379b-8061-0741fb030f4f | -12.8425 | -44.34624 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1a0b5117-4dc8-3212-86ec-5bfd4c33276a | -12.76239 | -44.49673 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| c9082e03-da96-3409-9d62-96014cbc3ff9 | -11.73934 | -57.81364 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe0491cc-402a-31be-911e-56b9a78d2793 | -13.72381 | -47.8767 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94dcb604-8d8f-3d89-befc-7551b13e3275 | -10.79446 | -53.5439 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94781a21-8398-3b7e-b017-a38f6d453965 | -10.67299 | -54.52058 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2a6177b5-ddc5-371b-ad94-402130c582f0 | -11.4239 | -56.05111 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75804557-cf40-3546-a023-0b802efd0478 | -12.76801 | -44.50053 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 871d37c6-9dd1-3640-a465-b74c95c62da6 | -10.76745 | -53.54313 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0271f161-76af-3eb8-b8c6-ef5af1e94c07 | -15.59893 | -43.60163 | 2026-07-01 04:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 381a25c1-f707-3e1a-97e7-6f15081796da | -17.91567 | -52.71326 | 2026-07-01 04:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 218b3db8-2d1e-3d35-9308-28015b9e2d21 | -12.41665 | -58.39644 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a4915703-5e86-3394-9ac3-739af814d233 | -11.56187 | -52.80438 | 2026-07-01 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe98f9f4-bc4e-383c-b89c-cac65169d616 | -12.52615 | -48.29102 | 2026-07-01 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d38bad3e-10b5-3ff2-9742-a9f5fb6438ce | -11.7876 | -56.99558 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 802c0b57-8ada-3a0c-a30d-fe4252531adb | -10.67405 | -54.53527 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ad385138-ee67-3f40-8dba-318496c79769 | -12.84295 | -44.34253 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5ff30824-deb3-3a6f-94a0-88e5ca83d323 | -12.76284 | -44.49313 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8f70edf4-b3e4-37c1-a733-3fa90594b095 | -12.21967 | -56.56172 | 2026-07-01 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3c9fb01c-d07b-345b-b0e9-39152e0c1f89 | -10.30233 | -57.12796 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ed6274e-b504-3754-81bf-2e465a6566b6 | -10.66521 | -54.52657 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11043837-c361-3c22-ba45-6298dd40ed4b | -11.88096 | -57.10941 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adea4217-d3f5-3e43-98db-ed7c032cb896 | -11.44096 | -55.90931 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e1664bf-7d7f-3ed1-8752-1e213a31024f | -11.90274 | -57.38297 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d772147-a0bb-3158-835f-a9b787eb2e7a | -13.47318 | -47.87716 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77c82d34-7121-3ef2-9c26-196e9d320ffc | -12.75825 | -44.48524 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 27188154-c3bc-385f-b9d6-5998de0bb031 | -12.77015 | -44.47935 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 022b04f1-53a6-3250-92db-74084a05616c | -12.83561 | -44.35662 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cfd789d0-5867-3c96-b941-b521c9999968 | -10.85305 | -56.66187 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 077eeffc-07c0-30d1-b921-9844150b860c | -11.4188 | -56.06652 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ab2e053-b0e9-3583-a107-1c415595623b | -13.65508 | -60.6234 | 2026-07-01 04:57:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dd90383-3919-3700-83d2-47867c430a3b | -11.83972 | -56.93926 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdf10976-da27-3904-be36-bf8f5d861573 | -11.43691 | -55.9125 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README24.md)
