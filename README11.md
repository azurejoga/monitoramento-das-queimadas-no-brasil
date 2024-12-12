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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 522cea5b-d037-37b3-8d12-63a0153f9734 | -6.9345 | -43.54499 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5e683336-388a-311d-96fd-a0fedac2222b | -8.55982 | -40.80071 | 2024-12-12 03:21:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ffa6856-0005-3590-9b1a-e4374e7ed040 | -6.92563 | -43.51747 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 9c0378bf-126a-37e6-966b-13b215943840 | -8.91775 | -35.2384 | 2024-12-12 03:21:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8b7c6c2e-2256-38c2-af8e-fa746e64c8b8 | -8.27026 | -35.4274 | 2024-12-12 03:21:00 | NOAA-20 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 767a5b36-d27e-3c4a-9e57-f0b23d5104fd | -8.26631 | -35.42678 | 2024-12-12 03:21:00 | NOAA-20 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 919b94dd-c5b1-31d2-a58a-43cb23a68930 | -9.69822 | -36.18468 | 2024-12-12 03:21:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 8091c1ba-85ab-35f1-8777-73ac77a37253 | -6.91886 | -43.51606 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| df6b8206-619a-3bcf-ac8d-3e03dc3f37d1 | -6.93483 | -43.53886 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 41fd56c0-b2ae-3095-99a3-22fcdcc51b2f | -9.38865 | -38.88229 | 2024-12-12 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ee04bdc1-da54-309d-9913-1a8af7459184 | -6.93564 | -43.53896 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d328694b-1755-35b6-b373-e8caf32cae65 | -10.49407 | -36.85334 | 2024-12-12 03:21:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9501ede7-a90a-31a7-86c0-dc7ac5c61d9f | -9.38966 | -38.87679 | 2024-12-12 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 80f43f96-48f9-365a-94e9-b21c5d3a99d1 | -9.78131 | -37.10844 | 2024-12-12 03:21:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f9c8cde-e829-325d-98b2-039aeb8c289a | -14.05093 | -43.30707 | 2024-12-12 03:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fad72e89-7299-3648-9440-24e808ab495c | -6.93032 | -43.52504 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 02ef3c05-e99a-3369-b6ff-5a5da81b614e | -7.88909 | -42.44949 | 2024-12-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d096cb3e-d05b-3c56-a1e0-4eebd50c65b7 | -6.92012 | -43.5422 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72fcd912-4ca7-3151-b890-51a2dc2d2f2b | -6.92126 | -43.53599 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e3aa96bc-dbc2-3490-b9ba-5ec90d8c4364 | -9.69885 | -36.18107 | 2024-12-12 03:21:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| d622bbff-9dfa-31c1-afcf-0fe743a10629 | -8.65464 | -36.91261 | 2024-12-12 03:21:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c86e5dcb-89f4-31f3-8054-77d750bf369e | -9.38653 | -38.87978 | 2024-12-12 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f9ff300d-8864-3e5a-971d-85b3d2d4fd97 | -6.93256 | -43.55125 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e300e50-69bf-3e0f-bcd2-a401aa767921 | -9.97374 | -39.17962 | 2024-12-12 03:21:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 252569e9-fd6b-31a3-b5e9-e1232897fa20 | -6.92089 | -43.54233 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 34f981cf-81e5-3202-b6e8-57a0440300f0 | -6.93004 | -43.53135 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| cc6b4345-8750-3f9f-984c-941855c8dd7f | -9.97267 | -39.17733 | 2024-12-12 03:21:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f67a05de-28f0-33d9-b02d-a5be7f28dc80 | -10.53975 | -44.6855 | 2024-12-12 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d5b8dc9-22ca-30fa-9303-b569fbebf9e5 | -9.6086 | -35.90657 | 2024-12-12 03:21:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 0329333f-36b1-3f19-a7c7-4344da8c3318 | -6.92326 | -43.52991 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 744c372f-f5e6-367b-a88b-93f276ccf08c | -6.9405 | -43.5464 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8de6edf9-0685-3969-aef9-6bcd8e036f8a | -10.59325 | -44.98738 | 2024-12-12 03:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 695553fb-9d1f-306f-aa6c-9625b9f90137 | -6.91647 | -43.52852 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 50d10c5b-aebc-3cc4-bf3a-45f21e07ace1 | -9.6948 | -36.18035 | 2024-12-12 03:21:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 63e403a3-d13c-3771-a561-c8df3847024a | -6.92207 | -43.53614 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cd4f3ecd-41ed-3d94-aff8-36dd3d077490 | -6.91562 | -43.52833 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 37590678-1825-33ac-a8cf-8392ebde99d6 | -10.50814 | -36.69728 | 2024-12-12 03:21:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ef7db0f7-a862-39a4-b869-fbd0dd2eec03 | -6.92355 | -43.52353 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 39461f1b-9f08-3757-9ecd-93eb4859407b | -6.92471 | -43.51725 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c453b413-7ca5-3ad1-aea2-393c7c678466 | -7.88281 | -42.44823 | 2024-12-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d1f8454-39b4-3d52-b039-b33beead504f | -6.91676 | -43.52214 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 0cc91564-d583-3820-930f-69d05c987d95 | -6.92683 | -43.51118 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 8631c1a0-2fd5-3540-b4a9-6893906614fa | -8.56051 | -40.79692 | 2024-12-12 03:21:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a5578ef-c52d-374b-aed8-b3b9b5d32f83 | -6.9277 | -43.54366 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b61d8f35-e54d-3044-9cbe-a65ce2952b22 | -10.51227 | -36.69809 | 2024-12-12 03:21:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d700e9d-55a4-358a-a35d-5dca6c2f0097 | -6.92887 | -43.53747 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1a98b2ee-ec70-3f28-ada1-bf123bd9608b | -6.93121 | -43.5252 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 48e0b68a-7e46-3d16-b753-4622f6774601 | -6.92241 | -43.52974 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4de69340-65a9-304c-9749-b7c79e51ee42 | -14.04669 | -43.3083 | 2024-12-12 03:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8caf88e-36cf-3acb-be8c-6dc2aed16152 | -10.53961 | -44.68531 | 2024-12-12 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 324dc885-a236-35f6-a406-8a2756d25ab3 | -6.93372 | -43.54491 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c444aaa-7327-39fb-8d2a-aad99fb6427c | -6.91766 | -43.52234 | 2024-12-12 03:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7ce0895f-367f-3cab-99d9-69d505f28e17 | -8.34705 | -35.0249 | 2024-12-12 03:21:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1abf382f-666d-36bd-88c1-95ba209d487b | -14.04498 | -43.30574 | 2024-12-12 03:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab87dcc0-3aa6-36fe-aedc-d305a8fcf525 | -11.1959 | -53.8348 | 2024-12-12 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5ac26079-96a2-3789-8746-a4c811ebca01 | -6.9158 | -43.5185 | 2024-12-12 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7e31ba24-49f7-31d0-b322-0cb71e93eef9 | -18.0663 | -52.955 | 2024-12-12 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 9d6be1e5-3eca-3586-9201-01327d95d435 | -18.0659 | -52.9766 | 2024-12-12 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 84c7ede9-ad4f-3c27-a22f-e2276c93e363 | -18.0464 | -52.9582 | 2024-12-12 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b7fda6e0-94a4-3aa3-bb1e-5a62bd6d7005 | -18.046 | -52.9798 | 2024-12-12 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0f2396be-5a8a-31d5-a25d-4cd6685bb493 | -11.2148 | -53.833 | 2024-12-12 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 128a1767-1a50-35c6-ba31-58cd32a70fca | -3.2502 | -46.8929 | 2024-12-12 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b202c0bf-0927-3db4-a4b6-912449438028 | -6.9349 | -43.4934 | 2024-12-12 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f8a684ed-d21d-333b-93f6-9a01ddf0034f | -3.2503 | -46.8709 | 2024-12-12 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| deab1f12-52a8-34a6-8fbb-e5f12321326f | -18.0668 | -52.9335 | 2024-12-12 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 289f2be6-8f46-398e-8374-befd37c7f83b | -6.9346 | -43.5168 | 2024-12-12 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d312acdc-7a3b-3614-b14f-9d440e231fda | -3.2503 | -46.8709 | 2024-12-12 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1facff3c-c251-3edc-8cb5-75fd97fefe50 | -11.2148 | -53.833 | 2024-12-12 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f164cd22-959c-3d1a-b0e3-fd04a937582b | -18.046 | -52.9798 | 2024-12-12 03:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 38a0466a-a2e2-3028-9158-4b2811fd2cce | -3.2317 | -46.8716 | 2024-12-12 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 21b84c23-ff8b-3c2a-8346-668d5bc243e2 | -18.0659 | -52.9766 | 2024-12-12 03:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 973a1f2a-9718-310e-9edf-59ecc2cb9751 | -18.0663 | -52.955 | 2024-12-12 03:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f910de28-d437-338a-87c0-aef99c1cd457 | -3.2502 | -46.8929 | 2024-12-12 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 836c6502-2f09-3a23-97c5-79fa0852d590 | -11.1959 | -53.8348 | 2024-12-12 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 25fcd8dd-2aec-3365-9a68-44c2658ce6d2 | -15.0867 | -59.6288 | 2024-12-12 03:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 92905b4b-d6e2-3cf6-956c-e6c3fd79fde3 | -1.8788 | -54.6908 | 2024-12-12 03:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 755d4bac-d577-3b4f-9bc7-e6673ff57c00 | -11.1959 | -53.8348 | 2024-12-12 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 68295882-fcb4-3ead-b07c-747ecb4bd74a | -3.2502 | -46.8929 | 2024-12-12 03:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7a65568c-1453-398b-9ece-9f98e578c655 | -9.8745 | -36.189 | 2024-12-12 03:50:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| ff0794f4-17d3-33c8-87cb-30f3270c4be5 | -3.2503 | -46.8709 | 2024-12-12 03:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 28cbf711-4ec6-36c8-9f53-2ae0b2397bf6 | -9.8552 | -36.1924 | 2024-12-12 03:50:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 160.4 |
| 838c5f18-369e-3532-b6e8-a8a2bd3ce187 | -18.0663 | -52.955 | 2024-12-12 03:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f059c708-0e68-3f82-a75a-9f00dc899a9e | -18.0659 | -52.9766 | 2024-12-12 03:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f6e40008-fd8a-378b-8170-65487f681917 | -6.9346 | -43.5168 | 2024-12-12 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 97bb054b-5b42-3e64-81f0-36fc2ec4dfa6 | -3.2317 | -46.8716 | 2024-12-12 03:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5618333f-428e-3a7c-b17d-d14d358a7e5c | -9.8547 | -36.2195 | 2024-12-12 03:50:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 99.2 |
| bb6e02c8-27f5-33dc-a4d2-2fd4e7d99d58 | -6.9158 | -43.5185 | 2024-12-12 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e0a83df1-0e41-3c44-9b48-8e33beefa62d | -6.9346 | -43.5168 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 301.8 |
| bdd09ced-ff8b-3b1c-81bf-14e3a0809609 | -18.0659 | -52.9766 | 2024-12-12 04:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d25ea9af-0a68-301e-bb9b-6b141a5372fb | -6.9344 | -43.5401 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 8a3fd8ec-2430-37e9-a6a1-97cb7f745f11 | -6.9156 | -43.5418 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e115874e-8317-358d-a07b-fcc8ba3e9b0f | -3.2317 | -46.8716 | 2024-12-12 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 783be847-cd7f-313d-9260-36e42b38528c | -6.9158 | -43.5185 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 158.7 |
| d0c1a485-05ba-31c8-b31c-f8ef6762923b | -6.9161 | -43.4952 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 28b3f979-c3f1-3791-a6af-d55cbbd94ece | -6.9349 | -43.4934 | 2024-12-12 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 4fb770af-ece3-3ebc-bb7d-384bd75c7ba2 | -3.2503 | -46.8709 | 2024-12-12 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 26ef0a21-dbd9-3b6f-8cd5-515e5ff13a38 | -3.2502 | -46.8929 | 2024-12-12 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3a13b397-6a4c-3e24-8d26-f090bed96637 | -1.8788 | -54.6908 | 2024-12-12 04:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2ea46abe-0627-3d71-8448-9394afcf136c | -18.0663 | -52.955 | 2024-12-12 04:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7c97057a-98a5-3064-9d92-5fd26be1cf0d | -6.9344 | -43.5401 | 2024-12-12 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |


[Clique aqui para ver as próximas entradas](README12.md)
