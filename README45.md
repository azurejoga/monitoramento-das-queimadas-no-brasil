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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a3eae14-2d43-3379-82dc-47d5c9730691 | -11.05425 | -49.56303 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 639be811-a459-3942-ba8a-41bbb100ac48 | -11.38648 | -46.66411 | 2026-10-10 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a4f85a0a-fefe-3a3b-92d0-96d64d87d0c3 | -10.89947 | -44.8037 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bec8447c-c456-3f50-bbae-d313b9d6bed5 | -13.8974 | -43.91626 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34413cca-d01f-3257-876c-86831addf7ce | -9.09037 | -54.70571 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9add39-50ca-365c-a19a-5b752c3d482a | -15.90326 | -38.95537 | 2026-10-10 04:10:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 362f7235-cf93-3b85-b5dc-d1453c7560f7 | -16.64747 | -40.53984 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fe794ade-d157-31c7-a792-2a8a5aa88c6e | -11.96076 | -43.48429 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66ced01-6cd4-3fa3-92e8-239cf29968b2 | -11.82856 | -43.58927 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16f0020b-6b93-34d8-8d5d-b8ac123f73d0 | -15.65429 | -48.13056 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e75b3dd-d2bb-3e4c-99da-860e90dbd950 | -13.12643 | -48.58372 | 2026-10-10 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c76f61-2d29-3cf8-a6fb-b9852978e4b8 | -11.59335 | -43.69886 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 529f915e-1adc-34f5-938c-b1de9a5c81c3 | -13.76592 | -48.12214 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8702887a-ceba-3564-8e14-00faf750761c | -11.85507 | -46.78675 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7586223b-9c7c-35fb-95e8-60bc0105c0b9 | -12.96115 | -42.50005 | 2026-10-10 04:10:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6150e1c-e48f-3bfa-a480-e19ae605a71a | -11.46388 | -43.37825 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 129b4134-7779-3d34-8197-7942dfe745e9 | -8.49827 | -54.60664 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdc643a4-f5f8-37d7-96d1-a82905a59007 | -16.98147 | -45.94754 | 2026-10-10 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7beef749-4089-3de7-8586-0a0feb05c05b | -10.24826 | -49.66012 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b664771d-074c-34f5-843b-c598122874b7 | -14.24038 | -47.30137 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c183e3c0-4692-3fab-b7af-8193c5592d09 | -11.03072 | -45.43374 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af1c9028-9709-3167-b199-13ace95552c2 | -11.0981 | -47.63313 | 2026-10-10 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4018fc35-af40-341b-9e37-75dbaa2ecd82 | -11.99593 | -43.45803 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 302d39ef-205e-3b77-a672-0f2348e793e3 | -9.28832 | -50.31382 | 2026-10-10 04:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c99ff43-90de-3b6c-8476-678e8df4e854 | -11.76109 | -46.78919 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4e7c35c2-7467-3af5-a5f3-e43578c79866 | -11.0851 | -44.11076 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e06a5de3-d193-3e95-8df4-0235fa6fe771 | -17.45699 | -45.07749 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d29b0b9-e464-3a03-8e19-1436f8bb68d8 | -13.35872 | -43.92131 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d1960370-d5f2-372b-9340-b2ad0266f5ba | -13.3576 | -43.9284 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c00085cc-971c-331f-bb2b-e33c1820e129 | -10.90082 | -44.8383 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac8cc932-d9d3-3a26-b069-2da3054b72ce | -14.45905 | -43.93642 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 98f97f40-aa3a-3c9a-926b-bee2be8ad42f | -10.24401 | -49.68405 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9d9fe5e-fcc9-3935-aa95-f751dc4de003 | -14.45301 | -43.93178 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f49ef5b-4626-3094-ae61-0216039365b3 | -11.9993 | -43.43686 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e368502-3b9e-3dff-af12-0c187775533b | -11.59683 | -43.61259 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6e9b2d-2f24-33af-8b7b-32d72d56dc6d | -14.46017 | -43.92933 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7317ef1-1f48-3ad1-baa9-15716fbd0c2f | -13.74218 | -48.51241 | 2026-10-10 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be315425-5808-37de-9f03-adfd6b115f53 | -13.67777 | -49.10719 | 2026-10-10 04:10:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95d2cd79-2253-36b3-b73d-3087b679ecb7 | -13.35823 | -43.90305 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4539bfc4-ca42-3984-bc9b-f61bf17134ee | -13.35436 | -43.90605 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02a80963-3042-3da2-97bc-7d2928ed42ad | -9.51413 | -54.66962 | 2026-10-10 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6e2c096-8585-363f-b715-b542ed5b0062 | -11.98613 | -43.45232 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09e1e926-da8d-37b9-99bd-31a8c92da992 | -11.02046 | -49.11076 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17b23943-4905-3295-8d27-93608f4560ec | -11.60595 | -43.7482 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4995bd55-7ea4-312d-b47c-639609ae2007 | -13.91516 | -47.849 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adc87988-3bc6-35e0-a619-f59674a926be | -11.59606 | -43.72466 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d53b3cca-8c20-3b2d-8f28-d094df556144 | -15.381 | -41.94303 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b0d4224b-68a0-3be5-8bfa-d4d717dfa6b1 | -11.0941 | -43.99031 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84494292-df1b-33bd-95e6-e9578e9a5ce5 | -12.0102 | -43.4964 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6a79e0d-d601-34c1-98df-7533c10bb658 | -11.83901 | -43.60906 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d52a38d4-3cc6-3fcb-89a1-76e03cb748ae | -16.45 | -42.77295 | 2026-10-10 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 899bb9e2-f1e0-3643-a39c-6a7767f3fe79 | -12.2281 | -44.69205 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d2ab7580-4d1c-3682-9c67-1cc89d879535 | -18.09637 | -42.26596 | 2026-10-10 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3da58695-8b91-3156-af57-398e555603b8 | -16.60569 | -46.76067 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbdf98e9-f783-3bf8-a684-6b131f462f20 | -15.25773 | -47.925 | 2026-10-10 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac33cd78-e6f9-3aa1-a19c-132c8f2e5335 | -11.56787 | -43.70931 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 674b6f07-d091-39ba-a657-3d1bb5cc4a17 | -11.02261 | -44.0564 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 739fe236-c1ec-36f6-af87-d9113a2680db | -11.60319 | -43.74411 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 983234d6-98f7-397f-afec-740421a69a3c | -14.97273 | -41.69161 | 2026-10-10 04:10:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1e0c2b73-5290-3b9b-90e5-c13598abd434 | -15.02368 | -46.26162 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9d3a26b-9e6a-36ce-b299-babff87f3b85 | -11.08845 | -44.11131 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dde85ba3-8d80-30bf-971c-84ff3b959bbd | -14.05032 | -47.00658 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78d001c5-e368-3427-87ea-33ce89ad224b | -9.99094 | -47.99993 | 2026-10-10 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0375a65d-805f-373e-82f6-3ba1a2695cd9 | -11.78955 | -46.72329 | 2026-10-10 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c7b6467-cbb0-3a73-8204-f30b06b607ba | -10.61291 | -43.27151 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 878d8477-4e56-3bfa-b4cb-e2001ab6ccee | -10.49302 | -47.33006 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8269cf8d-e9c5-3c6e-972f-87efb11fc734 | -13.1794 | -48.12619 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7684a4f-232c-3973-898e-47ca2d50adb8 | -11.75957 | -46.77544 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7bab96aa-82e7-332c-9801-c09616e8278e | -14.57757 | -43.83281 | 2026-10-10 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5cb9dd8-8200-3582-8585-3cd202a17ddf | -13.37034 | -43.91232 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 060b9df9-79e6-3a31-b1d1-820ed9f93af0 | -13.69015 | -49.13367 | 2026-10-10 04:10:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3945530b-60e2-303c-9951-b273375b3955 | -13.80731 | -42.65773 | 2026-10-10 04:10:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3bf7676d-e5d6-35ee-8d62-82eee1677374 | -13.63632 | -44.42186 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 687c6874-243f-3343-8046-0838a013712a | -15.36887 | -41.92643 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 7541ac38-ee31-300f-9870-12626b1f2654 | -11.02856 | -45.4251 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6a9954d-fe3c-3032-8250-959820c36195 | -10.52494 | -49.45625 | 2026-10-10 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96402f87-21a3-3f46-8c85-e038dc228dcc | -14.73214 | -48.21021 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 033d7b13-f76d-3d1e-8518-8404925b4a76 | -12.2223 | -44.64193 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8cf35ebb-7113-3253-9ee4-f6e7fdc29551 | -11.03139 | -45.42974 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d7aa6a3-cc9d-38f7-8b4b-e7ae203f1cdf | -11.96682 | -43.48887 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1aa5ea2-1ff2-3c99-8cf4-0ebc9aec724b | -14.45245 | -43.93532 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2182e757-d401-3d17-be00-6b108a3c4e93 | -11.77474 | -46.80908 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ea09a8c-eb51-3f4e-a745-5de5a5fd3253 | -11.73074 | -46.74247 | 2026-10-10 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f0ac4a8-3e7a-3c4e-83ba-88352febe0ee | -9.8915 | -47.63167 | 2026-10-10 04:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a38b3c4c-e6aa-3054-a814-28613365a3a4 | -15.66185 | -48.13207 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f5d0953-cdc4-3b29-885d-c0d84881c958 | -14.45631 | -43.93232 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d06a00a-5e7e-3e04-a0a2-c092cee4c5aa | -15.85065 | -42.03398 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f697c84c-1c3f-3b92-b6bb-a0c781e01a54 | -12.33702 | -47.32036 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4cc1b50-74ae-3349-9d52-91b9805d95c4 | -10.54206 | -47.3022 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf03e07a-a34b-300d-a576-90f1910dee50 | -12.77769 | -44.88576 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b0c54e4-7adc-3114-928b-eb611d63e2fb | -12.93088 | -47.44202 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96b4ac85-2256-3bdc-89f5-91cd694ffc3e | -13.92282 | -47.85039 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25657450-aa86-3aeb-8677-2b89aee5e3be | -11.02228 | -45.41961 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 80f74b9b-6cb3-37ec-bb99-300a7eed314d | -11.96957 | -43.49289 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c584d5f-ff42-3779-94ac-8f35071df682 | -11.17599 | -45.32314 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b716a4e-f777-3266-97dc-c95908ad2f04 | -11.86153 | -48.02811 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5506b7df-e311-3841-9346-acc7ed06fd7f | -11.99695 | -47.38974 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fba6f393-0f64-3c5f-a5f2-d676aab13d03 | -12.05929 | -43.42152 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36577af4-f4a6-3879-964d-91977fae4af4 | -11.74676 | -43.63387 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74cdd656-31ca-35c5-83a4-8ba7dee96699 | -11.08337 | -44.12159 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README46.md)
