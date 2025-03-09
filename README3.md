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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15bc3d22-0370-38a8-8384-d751b5a86e00 | -13.56217 | -47.92974 | 2025-03-09 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39338925-8a4f-36bd-b238-4b3e98795f36 | -12.49739 | -45.53186 | 2025-03-09 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e61ef91-1547-3b92-ac68-dea39b538169 | -12.00196 | -48.5689 | 2025-03-09 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39f69bcd-8a8a-386a-9227-0a220f4f0ea4 | -11.56796 | -47.61913 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2599e6f-aeaa-3003-bfd7-b6ce5dc91728 | -15.07711 | -48.94432 | 2025-03-09 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d0f8fd-f226-3c3a-992c-dc58958a6916 | -22.71638 | -46.11733 | 2025-03-09 04:34:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6f5926a-e45b-3632-a297-aca5c7893052 | -22.7123 | -46.11679 | 2025-03-09 04:34:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3e0638e1-2702-3bc6-bde5-a79b34434041 | -20.76417 | -46.76843 | 2025-03-09 04:34:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 38296655-9d96-347d-8dae-ade1f40c7625 | -21.1868 | -54.14448 | 2025-03-09 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9de5a0e4-75e7-3608-bd5e-286d8eebea98 | -19.83288 | -40.11163 | 2025-03-09 04:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0af63da8-1c39-3195-b84b-71d814c3c05c | -21.184 | -54.13961 | 2025-03-09 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ce62d22-2be7-3c15-9859-1409330c1ff4 | -20.76725 | -49.36619 | 2025-03-09 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56ba3c2a-1e64-3736-b348-1a8ed164482e | -15.91529 | -43.91373 | 2025-03-09 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6d0a964-4a3b-360e-a942-8a55adc798ae | -16.08246 | -48.1079 | 2025-03-09 04:34:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34a57a5f-8f0e-3e59-bf01-d5160dd3a61c | -20.31117 | -45.58281 | 2025-03-09 04:34:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1f6cff8-9f36-3b0c-add5-906016d23078 | -23.03341 | -43.49703 | 2025-03-09 04:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4cc701d-08be-39d9-b408-c1e77eb79359 | -22.11956 | -51.46698 | 2025-03-09 04:34:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d72b83e5-c61a-394a-b234-38716cec4e74 | -16.68222 | -43.88214 | 2025-03-09 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36fffd76-ad92-3f62-8bc8-34608a0a0df4 | -22.67544 | -42.85772 | 2025-03-09 04:34:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ce0101bb-4612-3986-9c7f-09f11d55249c | -20.72236 | -49.43462 | 2025-03-09 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4fc1302-e001-31e9-8ba5-6f87359d58f1 | -16.08587 | -48.10845 | 2025-03-09 04:34:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d03a41d4-1dde-3863-85d8-bc3cb87fe56e | -21.06972 | -52.33621 | 2025-03-09 04:34:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f96f120b-64d8-364a-8b83-ccd51cfba478 | -20.47617 | -53.67427 | 2025-03-09 04:34:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e445451c-4396-3940-9f87-50fe7f5b9df5 | -22.78667 | -43.75927 | 2025-03-09 04:34:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2ec2e96-5075-3095-82a5-f18b009c66be | -22.67577 | -42.85462 | 2025-03-09 04:34:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f053632-2c5f-3ac1-857b-3c6114057450 | -20.72575 | -49.43519 | 2025-03-09 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c6eb053-e701-3cd9-9133-009a67c50ca0 | -18.83211 | -48.00328 | 2025-03-09 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 107323d0-a877-394f-888e-5fc0eebd7bf3 | -19.10055 | -46.91337 | 2025-03-09 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a423db7c-780a-3b71-9752-2bbd41ea4228 | -16.69023 | -50.69922 | 2025-03-09 04:34:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0261b785-8618-3b0e-a406-a0b000b19e19 | -22.11625 | -51.46638 | 2025-03-09 04:34:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a945c100-4fd9-3af7-8e03-eac6d03d1489 | -20.5798 | -44.57452 | 2025-03-09 04:34:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c945f6c8-2024-3c7b-ab8d-886f2ebec151 | -21.20952 | -48.55581 | 2025-03-09 04:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| beb2f436-6a42-37e0-8481-9b40331109a6 | -18.82802 | -48.00684 | 2025-03-09 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4637cfc0-9aab-3f50-9e4d-cef0603e8f37 | -16.68166 | -43.88675 | 2025-03-09 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fb2aef9-c244-3a0f-b960-bf3e24dde2fe | -22.67519 | -42.85571 | 2025-03-09 04:34:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f456ecaf-e2c6-333a-ab73-88e7b06d0627 | -18.83154 | -48.00737 | 2025-03-09 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54bf0188-b2fd-3973-86da-8776cd427754 | -21.20601 | -48.55521 | 2025-03-09 04:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6fd10c39-577b-3bf5-93b8-ddcc7c749be7 | -21.15208 | -48.52938 | 2025-03-09 04:34:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 14dc2360-b273-3de2-9733-e894879c9435 | -15.08043 | -48.94487 | 2025-03-09 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94c46359-78c9-398b-b9f2-1e479d8c74d7 | -17.00395 | -47.94593 | 2025-03-09 04:34:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd734610-4171-3471-b492-7618c0db994a | -19.10424 | -46.91409 | 2025-03-09 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be1633a6-6040-3d8d-a7a5-e3d516c6ced5 | -22.71276 | -46.11303 | 2025-03-09 04:34:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7a13c5b-f18d-3fae-8358-eda72183fe62 | -19.67953 | -45.37768 | 2025-03-09 04:34:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0ff202b-8a3e-312e-bbe6-c8da79e2ef9a | -22.12014 | -51.46326 | 2025-03-09 04:34:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 68aa481b-37db-3044-8ac5-fbb48302fe52 | -19.83246 | -40.11593 | 2025-03-09 04:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c5855978-05d6-3174-91ff-d41769dc46ca | -19.10795 | -46.91475 | 2025-03-09 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 344c79ae-7fe7-3807-a2bf-27ad82d60918 | -18.80456 | -51.62975 | 2025-03-09 04:34:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0e81d5e-9afd-39fa-88e4-c4e48a8c827a | -22.60962 | -47.46326 | 2025-03-09 04:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 352745ee-d4a1-376b-97e7-ff8ea1d8601c | -16.68067 | -43.88385 | 2025-03-09 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9df0dbdf-193d-3165-bb38-6a6f90a4316c | -20.41711 | -43.55326 | 2025-03-09 04:34:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1b0c0aed-318e-3e18-a274-b2c748a6c113 | -24.16938 | -46.77924 | 2025-03-09 04:36:00 | NOAA-20 | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1db6e8cb-2cfb-3041-a8d7-53a327c2a755 | -23.33897 | -46.77242 | 2025-03-09 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3632db5-19ee-3d6c-aaf8-b435ee5570c7 | -26.40773 | -53.23859 | 2025-03-09 04:36:00 | NOAA-20 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c98d06b3-c81a-37b7-8802-e6475ba3717d | -27.27148 | -51.68443 | 2025-03-09 04:36:00 | NOAA-20 | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0579744e-1a58-358c-96d9-8228d98cb2ff | -23.73287 | -53.24741 | 2025-03-09 04:36:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8da44415-6e1e-3b62-92f7-3c5494891ad9 | -26.40836 | -53.23473 | 2025-03-09 04:36:00 | NOAA-20 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3336026-e09d-32b2-aa7e-675e2e7081f6 | -24.16782 | -46.77737 | 2025-03-09 04:36:00 | NOAA-20 | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f99030ef-e7f1-3e37-b4e7-31520c5818f1 | -23.3551 | -50.73627 | 2025-03-09 04:36:00 | NOAA-20 | NOVA AMÉRICA DA COLINA | PARANÁ | Brasil | 4116604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad2c188e-e4d7-36a4-8b1a-99dde8a2dbf7 | -28.65101 | -49.46141 | 2025-03-09 04:36:00 | NOAA-20 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12f38d00-0d1b-38e7-a5e7-45c5125ba977 | -23.98108 | -48.91912 | 2025-03-09 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30404fc1-2cbf-326f-9f21-234d60a18ba0 | -22.85047 | -54.65006 | 2025-03-09 04:36:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ff1b904-1f70-3165-b73a-a3ef4df1f97e | -23.54223 | -48.23419 | 2025-03-09 04:36:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fd95e06-ec8a-3ae1-a551-0ce815253fbb | -11.64442 | -54.38235 | 2025-03-09 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78bdd7be-9529-3977-9015-69c53f3d3651 | -9.18701 | -61.38359 | 2025-03-09 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e10f4f-11e3-3fe8-acae-fb5a2a3cd462 | -13.61243 | -59.76748 | 2025-03-09 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb5ba5ff-e4b6-37c5-8811-183ed5e42fbf | -13.61591 | -59.76801 | 2025-03-09 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b6040c6-d37e-30fd-8a52-6578e75bb021 | -22.11739 | -51.46513 | 2025-03-09 05:27:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7c47aa6d-678f-3d7d-a45a-13b2c8a73178 | -9.19306 | -61.37434 | 2025-03-09 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5fd1a2e-98e7-31ca-9986-de4f0d737744 | -9.19172 | -61.3802 | 2025-03-09 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3edb70db-213a-3109-b4cf-3a05ba980d7f | -9.19229 | -61.376 | 2025-03-09 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ed04d18-48a6-3540-ba92-8867c92e4fb2 | -7.04796 | -44.38956 | 2025-03-09 12:21:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 91e083f6-383f-3f8a-beff-afd4283f46a2 | -7.04668 | -44.39839 | 2025-03-09 12:21:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3d432ffd-b133-3cef-8f3a-05f973a2ba0b | -6.34834 | -43.08741 | 2025-03-09 12:21:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74709dd2-042b-30af-8d46-e8686036a38f | -8.78726 | -40.92455 | 2025-03-09 12:21:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f02a7935-7636-365e-9e12-7cd403e9bc73 | -8.22024 | -46.38901 | 2025-03-09 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 23960e49-dc57-3cf5-b647-b1b15892ec56 | -5.63546 | -38.26231 | 2025-03-09 12:21:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| aaf25288-d656-3d23-bd84-96eb88c8bfdc | -7.02271 | -44.42456 | 2025-03-09 12:21:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9b3a5104-0a82-3f59-85a8-f7dd708792a7 | -12.48328 | -45.51812 | 2025-03-09 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e10b0d9-78b2-3b3e-b09c-a53ecd0601ca | -14.39371 | -43.73351 | 2025-03-09 12:23:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 58ecae59-9d21-3700-96e6-2ead0ed905a6 | -13.56487 | -47.92656 | 2025-03-09 12:23:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bddb8fd6-62f7-3683-8e44-c74c507e0508 | -15.2041 | -42.6438 | 2025-03-09 12:23:00 | TERRA_M-T | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 851c1a84-ebda-327f-b8a6-200350bd7377 | -12.85768 | -42.48367 | 2025-03-09 12:23:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7391e42a-dd7a-354f-946f-e779e107589c | -12.31973 | -42.85497 | 2025-03-09 12:23:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0ef86e76-9382-3189-b833-0a7535e0f1d1 | -12.48458 | -45.50914 | 2025-03-09 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b719903-a1a3-38d4-887b-2bf9e735289d | -14.3951 | -43.7234 | 2025-03-09 12:23:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 08f3b094-eb14-3c7b-84c5-018700f732dd | -15.20563 | -42.63173 | 2025-03-09 12:23:00 | TERRA_M-T | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9cf03fae-0183-3bd8-bfc4-06cebecdf71e | -19.52306 | -47.22138 | 2025-03-09 12:25:00 | TERRA_M-T | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5011b25f-a98f-39c2-8132-3f63c7eeb470 | -17.16883 | -47.6686 | 2025-03-09 12:25:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a35cd28d-4367-3538-8777-d0f52becabe8 | -17.17782 | -47.67002 | 2025-03-09 12:25:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 095d5e82-c8ea-35e1-b92b-29b3fbd6df6b | -19.52171 | -47.23071 | 2025-03-09 12:25:00 | TERRA_M-T | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ef68443-ea16-39d1-a532-f6f443bde314 | -22.57903 | -46.9959 | 2025-03-09 12:27:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 401e298d-1e87-33c2-8180-aa2fdd80c7d7 | -21.02456 | -51.53902 | 2025-03-09 12:27:00 | TERRA_M-T | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 66243ad5-918b-3340-90e0-32571a00e66e | -26.31809 | -51.81196 | 2025-03-09 12:27:00 | TERRA_M-T | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 2dd85b56-5b31-3c03-ace1-102251b8715e | -21.22803 | -44.17317 | 2025-03-09 12:27:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| d51e1f0f-449d-34e7-bbd9-83085bdbc52a | -21.22955 | -44.16121 | 2025-03-09 12:27:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 29fc6461-142e-38f2-9d86-a82f1db9f51e | -22.71857 | -46.11605 | 2025-03-09 12:27:00 | TERRA_M-T | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b59fc49c-b47c-36e2-aa17-7a305c84f80f | -22.71721 | -46.12611 | 2025-03-09 12:27:00 | TERRA_M-T | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |


