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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c42a75f0-bb65-3f07-87ec-7218df14cc17 | -13.93137 | -47.47315 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b000f653-03b3-3553-8e2f-333a65b578d9 | -13.93981 | -47.46124 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c52de49d-13a9-3982-be1d-2608d8a6cd4f | -13.93901 | -47.46507 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb724c83-8d00-3267-82b4-b1c442f7ee03 | -13.4832 | -46.70713 | 2025-11-20 03:44:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c851b8f-b74e-38dd-a892-076ef3cb5b39 | -13.48796 | -46.71191 | 2025-11-20 03:44:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ecb3bf75-68c7-3829-a594-e22db94e7b85 | -13.48722 | -46.71562 | 2025-11-20 03:44:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71dbfcd8-579b-3a13-996b-083f71da1c2c | -10.48802 | -49.36512 | 2025-11-20 03:44:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b654446f-59d8-306e-bba5-64627e1fe23f | -12.94798 | -47.71529 | 2025-11-20 03:44:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 090148f4-719a-3fb2-a17c-b4ad39f72823 | -13.93076 | -47.47004 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b07779b-6b58-346f-abe3-8d792176d258 | -14.54132 | -48.63015 | 2025-11-20 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f20d0d64-768b-319a-a08f-00e84395a835 | -17.17706 | -43.2994 | 2025-11-20 03:44:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ec35751-c15f-321c-b98a-ba1dc99b74cf | -10.3586 | -48.90817 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 8b234702-f71d-3306-8d9f-7eecf11f38a1 | -11.41406 | -48.44592 | 2025-11-20 03:44:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95be9d77-0f0e-3d13-85f4-fd7cba4ec978 | -11.26665 | -48.50256 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a712f59-4b62-3eef-8b2d-87fc5888f7b9 | -13.93832 | -47.46203 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e657429f-b87d-3dc5-b597-60378d0759a8 | -15.56052 | -43.54645 | 2025-11-20 03:44:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba0c6dfe-6d9b-34f1-b1d4-433e05a88001 | -13.51356 | -47.91511 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 570f8693-6801-3c4b-8364-77888e4f67e3 | -17.68003 | -42.4401 | 2025-11-20 03:44:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e72f1a4d-171a-3c03-ba34-e11f2e9d131c | -15.54479 | -50.66479 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 338c365a-96a2-3bd4-adc1-2e0ef6c1fff8 | -13.92902 | -47.47875 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea0b5fa4-24da-3251-9a16-812b9508f47d | -13.94058 | -47.4575 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffaea5c5-8d0d-3ec6-bc70-f568986b1831 | -13.93046 | -47.47753 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3abe78df-47a3-3d73-950c-136f7e35d4f8 | -12.88119 | -50.1589 | 2025-11-20 03:44:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1ab92f2-e463-38a5-a661-31fb3c695e31 | -15.78726 | -43.35493 | 2025-11-20 03:44:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0f41a27-6647-329e-8ade-090cb281d659 | -10.66781 | -49.71222 | 2025-11-20 03:44:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6e430ef-bb9e-3684-a583-8d08aba648a2 | -10.36527 | -48.90931 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cf594572-0c6f-305e-8e8c-0a26aa62bdda | -15.88727 | -43.45135 | 2025-11-20 03:44:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02d12e1a-8cc6-36e1-bc3a-db55f368214e | -22.42739 | -47.63311 | 2025-11-20 03:46:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e7392932-6028-32fe-94bf-1fe9cff79395 | -20.29186 | -50.98209 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| c72f0394-e36e-3826-9ae1-ef65d1193cb9 | -22.16224 | -41.5765 | 2025-11-20 03:46:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 759f968a-6e89-33c7-8356-ad6c83f6c1e6 | -17.50581 | -44.92086 | 2025-11-20 03:46:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c6db2fe-c4cb-3b46-8f5e-17e868171351 | -20.29314 | -50.97665 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| eaa4b739-30b6-3247-82a4-c7424db83171 | -20.88534 | -52.34838 | 2025-11-20 03:46:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 53412b48-e7fb-3df0-bc71-f59ed7178782 | -19.08284 | -41.75702 | 2025-11-20 03:46:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 0c715270-12d3-3204-ab48-ae0406210870 | -17.86247 | -45.2332 | 2025-11-20 03:46:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbcf0379-d47d-3b9b-9415-dad10dab029f | -19.79343 | -46.07885 | 2025-11-20 03:46:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef506ebc-a458-3722-9a02-541829bf58ce | -20.88904 | -52.34674 | 2025-11-20 03:46:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78e48d8d-db7a-3ada-af57-6d47e712843f | -18.80222 | -40.76998 | 2025-11-20 03:46:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 853060df-e0ec-386a-9ffc-07acf90f50ff | -20.29689 | -50.96062 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| e02baa4a-09ce-33d3-ae9d-35603f823fe6 | -21.42447 | -41.17186 | 2025-11-20 03:46:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 262deed1-b6ba-3740-916d-a5f1e505b48c | -22.83307 | -46.32174 | 2025-11-20 03:46:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f920ccb8-3439-3b21-8be9-0c6260efc3bc | -17.90498 | -46.7156 | 2025-11-20 03:46:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a567ea7e-f39b-3284-b03c-917dc7e36cfa | -20.30315 | -50.96204 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| a39fbca8-5669-3490-92cd-8a3f46978b7f | -19.79543 | -46.07589 | 2025-11-20 03:46:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd3773ab-7831-3d05-a661-d88d4e966b80 | -21.04408 | -48.55355 | 2025-11-20 03:46:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7f8a0b32-12e6-3444-89bb-45effddade87 | -21.14799 | -48.52767 | 2025-11-20 03:46:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7ccfab74-3336-32aa-92a4-d2b3abd1c90b | -22.97743 | -48.66969 | 2025-11-20 03:46:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 462b0106-ea32-3454-b347-a681cac92f9f | -18.91612 | -47.17461 | 2025-11-20 03:46:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d55fcf8e-1a2c-33cd-824a-0a5fa0f4762e | -20.56224 | -49.57044 | 2025-11-20 03:46:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8a6c0c4-a3a4-3277-9d22-9c1b76baf5e8 | -19.83652 | -46.92736 | 2025-11-20 03:46:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1503cfb5-a72b-38ed-9b1a-12e5f0712e1e | -17.89992 | -46.71449 | 2025-11-20 03:46:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da5e1af7-7461-36f6-9279-bf12c825792d | -20.30065 | -50.97273 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 118f6c42-e6ec-3d2a-8280-d5a2c87173a4 | -17.50401 | -44.9283 | 2025-11-20 03:46:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db0cd31a-34b8-3797-82cc-043d734c0073 | -21.26041 | -42.21798 | 2025-11-20 03:46:00 | NOAA-21 | BARÃO DE MONTE ALTO | MINAS GERAIS | Brasil | 3105509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b23ee513-764d-379a-b9b8-fec0760320d8 | -21.04329 | -48.55717 | 2025-11-20 03:46:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 292b8b37-cb4e-334a-abbe-c31b8727da41 | -23.0266 | -45.8658 | 2025-11-20 03:46:00 | NOAA-21 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9ebe4e08-8bda-3a50-a010-6b53288726aa | -22.16268 | -41.576 | 2025-11-20 03:46:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46f868f3-1b88-3136-b142-95ce5e44c491 | -21.2463 | -49.17168 | 2025-11-20 03:46:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d3d1d6a7-1296-36f7-94a9-cac03347c7b2 | -22.97668 | -48.67311 | 2025-11-20 03:46:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dff4a3e-adc4-33ef-9404-84836ef1abc9 | -19.77004 | -48.01057 | 2025-11-20 03:46:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33bb9878-0ead-32d6-b0e2-783ee904c5a7 | -21.26289 | -43.37075 | 2025-11-20 03:46:00 | NOAA-21 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cebc986e-1a00-3c31-9ec3-c6958c7f57a0 | -22.42635 | -47.63162 | 2025-11-20 03:46:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f3eaf490-b669-3165-9d9c-e27a4ec8452f | -20.29568 | -50.96581 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| bbfa83fd-15ad-34ff-9172-90656fb04db7 | -20.8874 | -52.35336 | 2025-11-20 03:46:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 241c8209-d303-36ad-bd4e-ba79448c586a | -20.99037 | -42.89747 | 2025-11-20 03:46:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 11707568-fb88-3a32-96a3-93505d79f99c | -19.85168 | -46.03962 | 2025-11-20 03:46:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e93d8455-bf9d-30f0-9815-35655f6d0d57 | -20.24128 | -50.67675 | 2025-11-20 03:46:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8247d7e-793b-3e86-80ed-6d5a2dd12956 | -19.07918 | -41.75628 | 2025-11-20 03:46:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5599e38e-6e0d-36eb-8a3f-11375ad7f61f | -20.67773 | -50.12416 | 2025-11-20 03:46:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7c727add-bda6-3b05-96f9-e7169eafdc69 | -20.29443 | -50.97113 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| 2c8afc09-7fad-3642-9b39-be30143573d2 | -19.47557 | -48.92154 | 2025-11-20 03:46:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59c375fb-ee0e-3034-b8e6-2e93dd43385a | -17.90178 | -46.71551 | 2025-11-20 03:46:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b7bf0c-a68d-34e6-9f11-43725b096046 | -17.50484 | -44.92574 | 2025-11-20 03:46:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be56f079-ea6e-3918-ac42-0e8546b04d19 | -20.30191 | -50.96732 | 2025-11-20 03:46:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 75bdeab9-2c8a-3371-94c9-5d495d99648a | -19.83646 | -46.93032 | 2025-11-20 03:46:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504855c0-9ac6-3f5d-9307-cafab3c47797 | -20.56196 | -49.56927 | 2025-11-20 03:46:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed43665-7c97-3d4e-a48e-cd0ce723d7c5 | -17.50494 | -44.92341 | 2025-11-20 03:46:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e89e82-6228-3a0e-b539-0539d6270d3e | -3.01434 | -44.46177 | 2025-11-20 04:10:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c8581c3-336f-3ebc-bd47-15d30bdd9cdf | -3.68242 | -50.1684 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae5d4d83-319d-3edf-8341-fc4bef08042c | -4.66556 | -43.22811 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81b40578-5b95-3be9-a356-3a3fea505a97 | -4.60338 | -45.46779 | 2025-11-20 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59dd0e84-75d5-3833-9945-3fb3d81f5b92 | -3.6744 | -50.15781 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc0bf790-4fbb-3a55-bc1e-74f7497103de | -4.14115 | -43.68279 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56590d07-fb33-3818-a4d4-a2564a662daf | -2.93359 | -45.05159 | 2025-11-20 04:10:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 07710cad-bd88-3d00-856b-d52f3096af45 | -2.95935 | -41.55378 | 2025-11-20 04:10:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70da073-3ef4-38f9-ace8-61a4312360c6 | -5.87142 | -39.15614 | 2025-11-20 04:10:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4fece483-22df-3f05-b51a-6ca09a5ec202 | -3.23389 | -44.84793 | 2025-11-20 04:10:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23ce8803-233e-34c9-aa66-96f37bf4fb51 | -3.23166 | -44.8619 | 2025-11-20 04:10:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bcf8367-9201-313c-a634-617527553046 | -2.2641 | -46.53132 | 2025-11-20 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5224cfca-4e15-3c6f-a107-d54d1f6cc335 | -6.85612 | -35.1744 | 2025-11-20 04:10:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9082a64d-e304-3a22-8649-4d7c6882e65a | -3.6787 | -50.15729 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36258a6c-91b0-31a2-8f2e-75ad6e5481ed | -7.02843 | -35.19406 | 2025-11-20 04:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 25317089-2518-37a2-b10a-5d2d6adc8468 | -7.02791 | -35.18732 | 2025-11-20 04:10:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7447336c-a9da-3f44-a144-c3770e7f9c74 | -5.61428 | -37.47099 | 2025-11-20 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8784af1-1178-398a-afec-ad6cf686dcb9 | -6.26374 | -39.23361 | 2025-11-20 04:10:00 | NPP-375D | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a95f0f0b-0628-3eb5-858c-14334a474d04 | -3.68463 | -50.49266 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aca3e59c-cd72-37c7-b8b3-c54191e0d959 | -4.66677 | -43.22057 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8039bd0-fdca-3445-9b61-584b968b3f53 | -3.67803 | -50.16899 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 633d523d-2a3f-32dd-8ac3-cfd2be3f3a19 | -4.67368 | -43.22168 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a4ce774-2f7e-307d-aa6d-31ef37347747 | -5.81633 | -35.55453 | 2025-11-20 04:10:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README5.md)
