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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1932b38a-cd5d-3554-a95e-4d522a386f81 | -14.047 | -44.5545 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43cf0d80-a2a8-3b85-9ed9-fcc227f2c9fb | -11.8856 | -46.74775 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 632364a7-589f-3c1d-902e-847c663bf419 | -11.02819 | -47.03505 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4101ea93-83d9-39d3-b0e5-6ccec5a8d911 | -11.37855 | -43.6363 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da20b245-5a01-36b8-86ae-540086d9d70b | -12.78412 | -48.08971 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba86ae99-9c7a-3ce5-ab31-9190efc27827 | -14.04329 | -44.54844 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07b94a1f-71a0-3613-a861-9d38f11226f2 | -8.90914 | -40.44199 | 2025-09-01 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 570bdda0-7d2f-36dc-8921-eb51b4d9f143 | -11.08873 | -44.61402 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2517649d-ee5d-3cc8-b60f-f56914631cae | -9.28062 | -47.10857 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 768ca560-4130-3294-aa1e-7351426b10fe | -8.8454 | -47.49435 | 2025-09-01 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39590e33-46b9-3b5c-a2a1-b531724fd431 | -10.04527 | -48.10252 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ef3ccc1-a7c5-3f83-bac8-db736c877b1b | -11.02581 | -47.04732 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bd2a003-486c-3ef5-af29-c331126edcbf | -13.4931 | -46.93398 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7658fc6a-c0cb-3943-aa05-7b8ab3ff13b4 | -11.32378 | -43.4694 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89a46596-1ab2-30df-ad38-3c52aa852e91 | -13.48765 | -46.93206 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91d14ce7-5192-3d1c-9e6b-7e9bdac2d6fb | -13.34506 | -47.04896 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec45e1e4-d209-3ef1-8b68-fdf560ced446 | -11.37942 | -43.63145 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a375ba1-079b-31ff-b432-373c6374b854 | -12.56996 | -48.20519 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 03739088-cd13-3fd7-81ff-9eddd91d50f7 | -13.33638 | -46.97582 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9eb7667-0378-360c-a939-966456e96640 | -13.51394 | -46.82978 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 068b4ff8-ea2a-3420-a8b7-022eb0102723 | -10.60009 | -44.33196 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 89be6549-6a51-31e0-a4ca-f6d7f337bd49 | -11.79498 | -46.42705 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d04d584-6e1d-3161-b408-0820fb08c3b0 | -13.33562 | -46.97968 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 113a334e-85be-3924-a775-5dd5194aa9ae | -12.56536 | -44.79251 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5115135-1d5a-3bf4-bfaa-ec4a8782197f | -11.02413 | -47.05599 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca69dc9e-e3e3-3807-86af-a3342af854dd | -13.5781 | -46.93644 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2e38728-f630-3de2-b002-2a91b2ef2cbf | -12.57042 | -48.20815 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b9e2eaec-b838-3a74-90de-a3b7065a3761 | -9.23548 | -47.0856 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58e24463-aa4d-3664-bc91-79461b9c8653 | -11.04764 | -45.14139 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 7b146922-7ea2-3cfb-b3da-04a532144ce3 | -8.1968 | -46.77991 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1711d11e-a79f-376a-950d-763197cca009 | -11.90015 | -46.68149 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94b61718-70a4-3691-8d18-34d66b631fb3 | -11.82075 | -46.41127 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5422879f-4f9d-3ba2-82bc-f77e979661f5 | -8.84353 | -47.50403 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ec6ac18-4e78-3548-82b4-eb7362acc502 | -11.85054 | -46.78884 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6426e7bc-bad6-35dd-8ec7-187c6e0de136 | -11.03121 | -46.98865 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1b47cf1-c043-32bc-8849-d4e94a7cfe50 | -11.87834 | -46.70488 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2de73d04-226c-3e92-9beb-cf2251aad351 | -11.80447 | -46.43689 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6592043c-d3f5-3094-bce1-152b398fe0cb | -11.04016 | -45.15303 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 08351150-ba1d-36b3-815e-1b0998faa9a6 | -8.20125 | -46.77327 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a6a65cfd-ff57-319f-8032-5dc4ff434b37 | -11.88732 | -46.74862 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 417a3e1c-59f2-3815-8385-433b80bdc892 | -8.89014 | -45.11891 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9db082ea-1502-34a1-9222-a93a811d5da5 | -12.61668 | -48.19722 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b30ec971-5258-39d0-a101-bddda3117af2 | -11.91188 | -46.44118 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dbd25f0-3eff-34d0-82f2-4b9eeed41fa9 | -7.94233 | -46.44736 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b2998fc-bcde-3586-8a37-e62309d5247b | -12.60072 | -48.2138 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 056acf15-6d14-38fd-b398-dfc34d14a3fe | -11.37307 | -43.64039 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0982921d-f2f7-32e9-b65c-94166a42e2f0 | -13.5156 | -46.9923 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4b756cd-8ebe-31fe-bc48-bcbcf9409126 | -12.58446 | -48.20108 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c87eb05d-746d-3fce-afa8-dfb08730221d | -12.57508 | -44.79435 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69936b0e-8d41-3bcc-8eac-273fbd39b621 | -11.05219 | -46.91114 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0958708-90ad-3d65-8718-78712011028c | -14.00798 | -44.50523 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d94871a7-8aee-3fc1-b874-59cd79c586f1 | -14.02747 | -44.47823 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e51553ee-5d89-3c1d-b5d2-68cc3874d95e | -13.47473 | -42.47651 | 2025-09-01 03:45:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 082d6c8f-c6a0-3c73-b128-a17aa6728575 | -9.6391 | -46.61099 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 725b478f-98cd-3435-9a15-ae04438934c8 | -11.04525 | -46.9778 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd200d1f-8140-3480-a3a1-0f30f307ec23 | -13.69941 | -46.89974 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d906c1e4-4499-3bc1-aaf3-83f833e103be | -11.89732 | -46.68886 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c54d9ad7-16a4-3ef2-8857-0691af6e1a59 | -14.04607 | -44.55952 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89100bd4-5050-31b2-8c93-db773e7a7be9 | -14.00752 | -46.31936 | 2025-09-01 03:45:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df63421-b0e4-3be9-8eff-3b9bb077128f | -13.68726 | -50.765 | 2025-09-01 03:45:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95599329-6fe6-392d-ae62-6adcf21e8b6d | -14.15853 | -43.67241 | 2025-09-01 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d87da3f3-32d2-3845-90f9-8bcbe0a0e915 | -11.03566 | -47.05845 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bee3d3e2-958b-3453-a014-205874b22123 | -7.95514 | -46.45187 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2489dc4-21bf-3d60-a4c7-79dd436d50f2 | -12.80535 | -48.07684 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a952d30c-150f-3c38-89cd-cfae4392bcd7 | -8.88955 | -45.12215 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0f80b85-3214-3185-b2a1-99bf1fb3f7c0 | -14.04701 | -44.56836 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 21a3633d-8bba-3f96-b2d8-25434733226f | -9.64648 | -46.63283 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb14183d-8727-3175-9698-c406a176b588 | -12.83924 | -48.07549 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ef8f3bc-d68c-3cf4-b724-603aecf40f9b | -13.36503 | -46.94524 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72f5c55f-2c7e-3541-bb2e-7642f0df74d0 | -13.48186 | -46.989 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0df09b0d-7450-3641-a351-de2659f55f2d | -7.63416 | -42.65143 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96ebb729-98ea-36a3-b90a-b08d88079d24 | -11.80884 | -46.41416 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bfcc5c06-3b78-3fd7-b35c-8283ad661b52 | -8.89882 | -45.10139 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8797898b-2a35-330f-b759-58632aff8095 | -10.88817 | -45.80919 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce36be8f-400b-3e17-9e5e-e92aee6a6417 | -8.88009 | -47.21122 | 2025-09-01 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54aec794-3211-36cb-823c-83abb833b49d | -13.37544 | -46.95047 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92b860b1-3529-3163-bc4c-f41d4c62282a | -11.96005 | -45.84735 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dfac87e9-94b4-3005-a3da-b79386a3f06b | -13.48142 | -46.93458 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 636fa546-f7e0-3601-962a-8643c5e54a1a | -12.55409 | -48.22165 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6c6c87d-8bef-3ee1-bc3c-bfbdd5433ff4 | -12.09333 | -44.72267 | 2025-09-01 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c5699db-210a-3ffc-a431-298c8ebf5653 | -9.64034 | -46.60165 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 291340bb-432f-3569-b7fd-61bfda4d2ad5 | -11.05141 | -46.91517 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 204120ff-75bd-3053-8564-d71073796230 | -10.77351 | -48.83906 | 2025-09-01 03:45:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 279f10f1-2640-35fa-befe-669e01387b5d | -8.15962 | -42.3042 | 2025-09-01 03:45:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 69ca23ff-8438-311c-b3f0-066cb20cd47c | -9.67194 | -47.04177 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe2e7e3-ea02-36c0-adc4-5ef1297cbda6 | -13.4871 | -46.93551 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07b66bd9-663a-3ba6-b1e2-8bb8ecea7b59 | -10.88545 | -45.80851 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e763ce3-9207-3e5a-b39c-0193043440fa | -13.47764 | -46.9842 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd104e47-137d-300f-9683-e9db77f5a936 | -7.88214 | -46.99647 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acd739d0-49ae-3487-b1b0-2cd7c374756b | -8.29569 | -46.32259 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b03b15b-32bd-3616-84bf-bd543b1ae225 | -12.85281 | -48.06987 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e796fd82-7d48-3214-a7e5-97046950edbc | -12.583 | -48.20285 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90712132-274e-38a6-8eb0-358e47ed533c | -10.12668 | -45.76591 | 2025-09-01 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c2f9f47-429d-3385-9fe0-a34028a05f35 | -9.6407 | -47.80307 | 2025-09-01 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a916af28-dfe6-3b34-8d89-c01bbf9b678d | -8.70363 | -47.87378 | 2025-09-01 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 461b0fff-8d1e-3cd0-86ed-88020da85303 | -13.47583 | -46.93398 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a29170c-6ef2-3a4c-8bb8-3d9a98d62557 | -11.96037 | -45.85007 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6b62c1d-826a-3ea8-9785-8c0aad78ee1b | -13.9902 | -44.54842 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824c8685-b58f-3d8d-b1ad-848b5d10a2ab | -11.37135 | -43.57077 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f50f333c-66dc-3995-909d-7d1d3bf02f70 | -12.82719 | -48.07363 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README21.md)
