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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66e66879-0d85-309a-bd8e-882a1ce5a0cd | -16.77687 | -42.7564 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 527ca8fd-4010-302e-bdc2-aa183a9a4abb | -10.89066 | -46.07703 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fa399724-3c66-3111-bc23-a0f47f647656 | -10.68781 | -44.54184 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8824933e-10ca-347c-8135-0b8c11b8d70d | -14.13562 | -44.69117 | 2025-10-19 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369a251f-ca2c-30db-9565-17acef747483 | -12.6928 | -46.95661 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e808892c-aebc-32e7-859a-1537c682a97c | -15.53137 | -43.83723 | 2025-10-19 03:45:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f313792-4074-31b8-a5a3-7516a7c1d131 | -16.14705 | -41.15922 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6afd1a2c-34c3-304f-872d-0dfbd6f4dd5c | -14.47345 | -43.34346 | 2025-10-19 03:45:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a216a84d-aec1-3597-8a59-792bfee8c08d | -11.63802 | -44.08749 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc79c4ea-4d41-3069-9389-1aaa2327195b | -12.33804 | -41.38862 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7bc91c3f-25e3-3db7-a130-7fc4190d9217 | -10.69336 | -44.53993 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca85e919-80a7-3afb-a9c6-197a52ed0cf1 | -16.74141 | -42.79191 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9ec987-46dd-3639-b0da-f8b2bd183e9b | -12.46014 | -45.43337 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 603fbe56-ce68-39eb-81b8-38ce348713dd | -10.23476 | -44.89587 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c5d0e56-5570-3166-9a87-7ce6a4f55543 | -16.78418 | -42.76181 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ab928590-fcdd-3508-b6ae-53f2c6742d3f | -12.30164 | -47.26406 | 2025-10-19 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c117bde-4453-3467-b3c3-d6ab3952a225 | -10.53978 | -44.50438 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2561d3c9-ee87-310b-b0c6-a3ff96a8e113 | -12.99024 | -47.27732 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7181364-1a49-3207-953b-848a588ab7cc | -15.78837 | -43.25654 | 2025-10-19 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb0ff5c3-a37a-3f93-a324-586c2d621413 | -14.55648 | -43.5099 | 2025-10-19 03:45:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13e2f683-20f2-3592-9daf-89dffd363edb | -16.7502 | -42.78928 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82771e91-ff79-3791-8a91-6b70d123dafe | -15.98311 | -41.21023 | 2025-10-19 03:45:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f616ad9f-d223-3944-9890-a392e0b5735f | -12.3341 | -41.38784 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76cee538-47ab-367a-9396-34015682df93 | -10.68096 | -44.55174 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3081f12c-82b0-36f9-bf4e-f5845ad9f25e | -12.45985 | -45.44411 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 171d8f5f-6b56-3fc6-8ba1-8899999b87c3 | -15.09212 | -40.1667 | 2025-10-19 03:45:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ae4b9101-ba32-3c50-9f95-27dead25d866 | -10.12694 | -44.53279 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18a4bd4f-00d8-3a8c-9ccb-9249b1422211 | -14.21287 | -44.39141 | 2025-10-19 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 550dedcb-5afb-36da-965e-0ddf7c905158 | -16.76086 | -42.77622 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 743b62e6-e3ed-39d1-8610-5649eac06c94 | -16.75217 | -42.8014 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad95ce4f-a3a2-3642-ac36-6a8bff31c540 | -10.2226 | -44.05849 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| abaed919-8997-3160-865a-bf69646b2b7a | -10.81283 | -43.92771 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4a2230b-7c4c-30bd-85d8-2a5903c70e47 | -15.90667 | -41.57338 | 2025-10-19 03:45:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b79dc28d-976d-3289-a2af-fc8c84e339df | -10.68042 | -44.55472 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31329383-db72-3bcb-a121-94c68587437a | -10.91572 | -43.82595 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c8e5141-1bf9-3699-b89a-a3e779c60b26 | -16.15154 | -41.1553 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cc784d1-33f7-340c-8f11-8e0aa32aaa63 | -10.53562 | -44.04308 | 2025-10-19 03:45:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ba81f11-b737-3bfa-adfe-c36ce1767332 | -12.98367 | -47.28042 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7032d8c4-0974-3967-a6c1-50941f567eb7 | -16.7892 | -42.80893 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18f45ad5-3612-3308-b75a-6b493a9a4cd2 | -10.91096 | -43.82512 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bdd8fbf-26b0-392b-9655-a31b98d98a1b | -16.26423 | -42.48176 | 2025-10-19 03:45:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b611db0-dcd2-35cb-ad13-6a7b6ea25b31 | -10.8086 | -43.92537 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8445a1d-af8b-352e-ad90-c01fcc02a876 | -10.86173 | -43.93134 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 875cc5de-f582-3049-836a-ae6a95b10af4 | -10.80628 | -44.01667 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06c65d48-522c-3df1-9c02-e5a4ce39d30e | -10.91501 | -43.82763 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d8e9eb3-a8fb-3bb5-a567-b7b12f4d48ff | -12.98942 | -47.28152 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc4b2dbc-210f-3c4e-a1d0-6757f4c65371 | -13.75013 | -43.60056 | 2025-10-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9f9eb7c-7b46-3c8c-afdb-9cf33d8bc547 | -11.781 | -47.55434 | 2025-10-19 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfd8dac8-a7b6-3843-be52-66566891fd57 | -16.73804 | -42.81052 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7531c8d-8654-3a4e-bbd2-6d66416f42da | -14.14113 | -43.1773 | 2025-10-19 03:45:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bea57f51-631a-3b77-affd-e57921c759ce | -10.53529 | -44.5006 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e29a674-2b24-38f9-8c9f-6221e39a6a3c | -12.4544 | -45.43555 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6782ff44-8e69-3bc4-ae44-534af35512a3 | -12.31893 | -41.38739 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2fb3437-7188-3b5d-8b56-a209934c72e7 | -17.08519 | -41.69596 | 2025-10-19 03:45:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e30e6594-4353-3d65-9338-3fedc1e927f2 | -12.99026 | -47.28258 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8acd6d8b-a5de-3f43-91cb-c9c173a39ea3 | -16.14576 | -41.14482 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 950a5f15-e33d-3f32-8bc3-960412591d7b | -16.14495 | -41.14946 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 28f27b69-529d-37b7-b648-58e31b594a58 | -15.78499 | -43.25128 | 2025-10-19 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 960427f2-bf83-3a8b-a7b9-2fe1e3e5940b | -15.19048 | -43.56812 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8d3c9ed3-37d9-3b47-a510-48901d00c6c6 | -11.62981 | -44.07851 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfe7bc61-766a-3042-a658-9c65954d9fec | -12.33471 | -41.39046 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b641305c-db94-3823-a17d-5c1ae4399a36 | -11.04883 | -40.21343 | 2025-10-19 03:45:00 | NOAA-21 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46154db8-f7ff-3559-ae0b-b35a656af430 | -15.24542 | -39.38679 | 2025-10-19 03:45:00 | NOAA-21 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39bf204c-25e4-3464-85cf-8fcb1c45868b | -16.7474 | -42.75891 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75b4127e-18bf-32fa-b10a-0035c32e157c | -9.96236 | -45.28467 | 2025-10-19 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53d843d0-38f7-3a02-b152-ed706704f517 | -13.92826 | -42.95727 | 2025-10-19 03:45:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc8512d8-fd33-340d-ab5c-d2235b019e94 | -11.89562 | -45.43596 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a1bdb05-c29b-32a3-a15d-2e1087b97bfc | -14.95092 | -41.64511 | 2025-10-19 03:45:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3dbee466-55eb-3537-bacb-d77604812b78 | -10.88636 | -46.09959 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43ce2116-4c28-3e1f-b948-69cdb0192552 | -10.44906 | -45.02528 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23a2b3dc-916e-34e6-9c03-67fbe1c9ac73 | -12.45955 | -45.43654 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27c26062-5756-3352-b3fc-546afc8f3e7c | -16.51995 | -43.54787 | 2025-10-19 03:45:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de8350ca-048c-3819-ba1d-864221e826ae | -15.01223 | -40.45816 | 2025-10-19 03:45:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b4836cb2-1b63-3505-95f1-12f1667c4161 | -16.14785 | -41.15469 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7b40d9fd-630f-3491-b4c1-91bf37bfee9d | -9.91032 | -45.95748 | 2025-10-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6afc4b0e-5616-3ec6-b889-3bb819627f34 | -12.15547 | -45.09745 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59ca6926-c02c-3628-9522-b8554fd0a930 | -15.79114 | -43.63973 | 2025-10-19 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d6f7c42-7b21-3b2e-b274-b92afd717a20 | -16.78086 | -42.75726 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a6c99ab9-8e24-3b1c-9c8a-28410e9f1d9b | -14.55728 | -43.50555 | 2025-10-19 03:45:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d13b55ed-720a-33c4-af0f-16d511592b50 | -14.2782 | -42.33077 | 2025-10-19 03:45:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4bfcd8a-3d7d-36ca-b6c8-a26e4ca34511 | -16.82546 | -41.80028 | 2025-10-19 03:45:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f8cf7aed-79dd-3afb-a0d1-525c3bd17111 | -15.45117 | -45.91264 | 2025-10-19 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a66949e-b969-3661-8d0e-716721c0ace1 | -10.85397 | -43.94673 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cba4069c-7ae8-37f2-a121-004338894bbe | -9.90475 | -45.95641 | 2025-10-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ea4fdd84-0f23-3f3f-aa59-b7b44879f284 | -12.98048 | -47.27199 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9cb9185-4c74-30ff-b4a1-ed5e19478d61 | -13.89846 | -45.53298 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34f1563c-d6b8-319e-816c-b5552b998136 | -15.70466 | -41.25957 | 2025-10-19 03:45:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fac76421-87f8-3448-96ff-90cf9819fdbc | -13.89498 | -43.4545 | 2025-10-19 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f974d3f4-605f-3c78-bdee-21e5484b9427 | -10.85876 | -43.94766 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02f53e29-f40f-3871-a933-76a8294d854a | -10.85215 | -43.92951 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d33530f3-8d92-3cb4-bf43-417ac16d2a9a | -16.75685 | -42.77549 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 11796ebb-d59c-374c-b942-ccc84459cbb9 | -16.75355 | -42.79376 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05040c5e-6953-3554-8eba-6159f031a65b | -12.4617 | -45.43463 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 950e4cdc-b457-3585-b8c7-ee18336acb7c | -12.57018 | -45.43538 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f0ebcf-ed87-3d42-99bd-bf75bf262b45 | -16.73869 | -42.80693 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d8b48b55-713c-336e-ae58-8ea9288d1176 | -10.84635 | -43.93414 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aed60c06-06fc-3d1d-8f0c-9655cdaa7ca0 | -11.61263 | -44.06438 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3ee559b1-3d00-34db-98ae-937b360ffb1a | -12.9804 | -47.26671 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef6acca-b2c9-3a1f-a072-d814a1fd0152 | -15.51845 | -41.67699 | 2025-10-19 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 03e140a2-9ecc-3e98-a4ef-5b6aca9685a4 | -16.7789 | -42.76815 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README14.md)
