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
| f91c7491-e58a-3e19-91b6-a985f446e0df | -13.05132 | -53.71745 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bee4cd76-cebb-3731-866c-955890068d95 | -17.34992 | -43.85733 | 2025-05-07 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6cff6083-ede1-3b16-9099-eb918f3fb1f7 | -15.07923 | -48.94558 | 2025-05-07 04:04:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fafa512-bcf9-3d04-9d66-ca6d8540992c | -11.40994 | -48.71145 | 2025-05-07 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 171a441b-e93e-399a-9ad3-85f27db303b3 | -11.78848 | -47.35659 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 703beab3-3d68-3818-8cba-8b52ff820a3e | -13.50061 | -52.95694 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 581dbc79-45cb-343d-979c-4a87814e86f9 | -9.26319 | -47.90796 | 2025-05-07 04:04:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcc981f9-3c8b-3912-b8bc-ceea75d0fb63 | -16.04475 | -43.80228 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00e36bf3-af44-3b5e-ad9e-0c8fc37d16a3 | -17.77937 | -42.80656 | 2025-05-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ebab99c-b0c3-3070-9cd5-e858400a7539 | -13.0493 | -53.72216 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6c168f9-1198-3996-9760-ba18c40e1730 | -15.8298 | -46.57408 | 2025-05-07 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a8ae6b7-e2d0-3171-b7d4-ca190459d57f | -13.50662 | -52.95826 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 230b4e5d-eaf3-3446-a742-6fc15f1d04b1 | -10.67923 | -44.39114 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fba3cec-af2d-3cbd-b036-d5011aaf436c | -11.78416 | -47.35574 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27e5c7fe-0241-361a-a5aa-61b9f030ab6f | -14.64212 | -45.91432 | 2025-05-07 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303e6a4f-767f-3d55-82da-49a3ea96f0c2 | -13.5057 | -52.9628 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76d6934-3a9f-3115-b136-46698fc81e46 | -12.79211 | -44.90723 | 2025-05-07 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 205fa825-956b-3a31-be7c-f52c55bd2a02 | -10.72105 | -42.32289 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dd4f5588-e1ba-32de-9914-f3e2500c28dd | -17.38691 | -42.65869 | 2025-05-07 04:04:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12d225ba-90bd-38b7-968e-a92eef20114c | -12.17373 | -54.23926 | 2025-05-07 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a20c8a59-cc08-3aab-aa2e-a4a7fdd683d9 | -11.27292 | -52.47099 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1039b1b2-7570-3717-9d44-979d4b6919ba | -10.98386 | -44.44478 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbeb4b9c-39a6-3101-a1b4-278d4c90ea4c | -13.04825 | -53.72737 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d3afd36e-e0a6-34f2-92d5-1a5a8e725d2a | -15.21299 | -43.82308 | 2025-05-07 04:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb1e5111-8359-33c6-bfe2-ab2113604f10 | -11.39751 | -52.95195 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d24b6c5f-a944-389a-9c5d-a189dd6c33d1 | -11.80197 | -47.3807 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483746b7-1c71-3c66-9eec-ca9d1c0190ab | -10.71369 | -42.32541 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aceee96e-d6e3-3455-bcee-d692f712b1dd | -13.05023 | -53.72266 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bda61d2f-b653-3f10-a934-38e7f5e22ca8 | -10.98529 | -44.44223 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4043f0f8-30fc-3201-9b92-d4be3ef10b82 | -12.17673 | -54.24115 | 2025-05-07 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e90eafb-d03e-3e61-9e25-a9851b182447 | -16.04352 | -43.80979 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec21f167-a3bd-31cd-b122-cfa348276aec | -11.51719 | -48.57992 | 2025-05-07 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6dc29bb-045e-3ee3-a279-47a3b8ab1618 | -11.39329 | -52.94064 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1262a015-1773-3f64-8832-66d508436fe1 | -16.0429 | -43.81354 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34a40e1c-fe4a-3b50-886f-72ac44cc79b5 | -12.83247 | -47.40983 | 2025-05-07 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0faad7e-6e73-3f9a-aee0-c28d44b237ca | -14.68911 | -53.39494 | 2025-05-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe0a3174-62b2-3786-90e6-79c3f9cac731 | -14.6459 | -45.91502 | 2025-05-07 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fb86945-a141-34b3-822b-012bce6b96a1 | -17.678 | -42.74076 | 2025-05-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 629b8730-2dfb-382b-af71-d31725753a16 | -11.3923 | -52.94555 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d38721c3-8eac-3ed6-8ef4-ef9f9e612d11 | -13.50116 | -52.95956 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de513749-1c3b-3f19-a283-b83798a06fc7 | -11.19411 | -44.51067 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da0bfedb-9273-3e3f-ae39-4df04dac6655 | -10.71767 | -42.32233 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a0b2b02f-0818-3ab7-8d1a-358a0a63ed3f | -15.82891 | -46.57901 | 2025-05-07 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a90f027b-8b0f-39bf-a2f7-fd87a9875da4 | -11.25944 | -52.4761 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb31931-7cfa-3482-b604-849fc1eb3fcf | -10.98163 | -44.44157 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb5cb4a-7e41-3c0e-a744-ab6b3477be82 | -14.64674 | -45.91032 | 2025-05-07 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce850fa2-95a6-3c2a-a649-48e071d08d83 | -14.72576 | -42.87806 | 2025-05-07 04:04:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 62949f33-4096-3583-a5eb-143236e85fbc | -10.98752 | -44.44544 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68ff2ec3-91cb-3171-abab-c086d43b4462 | -14.68963 | -53.39359 | 2025-05-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579dfd8c-c60f-3e88-9955-df1cff613849 | -11.56002 | -47.62056 | 2025-05-07 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d638b956-2fca-3448-81f2-a2a5a34273e1 | -17.67742 | -42.74438 | 2025-05-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fda25c65-bef4-3cf4-a054-793c9c804aff | -12.17009 | -54.23971 | 2025-05-07 04:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 596aedd2-54dd-3578-a10f-291c866b3062 | -14.69059 | -53.3891 | 2025-05-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 449110cc-1d12-3bfa-80ac-765d2b097d8b | -11.2585 | -52.48095 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33848963-6d72-35ed-a273-4b5913498aac | -16.04073 | -43.80542 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 903660c6-d100-352a-836b-686597cbe9ea | -11.58886 | -47.61237 | 2025-05-07 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25fac870-812d-375c-aade-c2d9cf3180b2 | -14.10572 | -44.13064 | 2025-05-07 04:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81161a9b-6147-335c-9339-4f5c05ce21e4 | -17.78212 | -42.81076 | 2025-05-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7950dcf8-218c-3c37-b37b-4aea03a61671 | -15.79441 | -41.27856 | 2025-05-07 04:04:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6535489b-ba76-35f9-a79b-386d71e01bb4 | -13.90343 | -43.8 | 2025-05-07 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0d85319-f436-3856-bad3-03ebaf640d47 | -11.77464 | -48.70457 | 2025-05-07 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 41eba5fb-6e7f-3520-877a-6c18b87b999d | -10.71707 | -42.32597 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 26827984-b3de-39a5-b55b-e1ebdc36ffb2 | -11.25883 | -52.47813 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73c5e384-231b-3858-8c56-3b79d96f6700 | -13.50019 | -52.96419 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69bac8dc-b84c-3256-a5cc-8087e8015f51 | -11.27896 | -52.47238 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a3e3dc7-3af9-3137-8985-4557a0f32601 | -16.68159 | -43.88425 | 2025-05-07 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2175b4e1-efda-35f6-b928-ea826018f978 | -11.79764 | -47.37991 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4540c75b-52bf-3c21-853e-d69f7253a292 | -11.39129 | -52.95053 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebc006db-df0e-3250-8e4a-1da0adc6f3d5 | -11.51624 | -48.58511 | 2025-05-07 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d881e312-e07f-3f37-a7b2-c42c784fc2a4 | -17.34654 | -43.85672 | 2025-05-07 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e617dc0f-532b-3485-8ea0-04d4501933b1 | -13.04914 | -53.72784 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de5371c7-1840-3afe-b0f9-435338adc761 | -11.41391 | -48.71357 | 2025-05-07 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89100cf0-3451-3c50-8fa4-b2dece37c3cb | -11.19341 | -44.50872 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50bff302-548c-3c61-8aae-6ff1336443fc | -13.04284 | -53.72626 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aaa50916-ab71-3c35-912d-5fc04f92784a | -11.41491 | -48.70826 | 2025-05-07 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d73f275-6c1c-35e7-ab01-87d9309a4f90 | -14.7224 | -42.87749 | 2025-05-07 04:04:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 854e4566-a119-3444-b0e9-c386617d71c9 | -11.19266 | -44.5131 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2232f237-905d-3c14-bfa0-5def4a423513 | -13.05036 | -53.71696 | 2025-05-07 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c37584c-26b2-3396-9b19-37a41163593b | -17.36295 | -42.51312 | 2025-05-07 04:04:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5caac9a7-1851-345f-a2aa-491c38a91974 | -15.84676 | -48.16832 | 2025-05-07 04:04:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90bc0360-f0b0-33ec-9599-5a6c55f07d1e | -14.10223 | -44.13002 | 2025-05-07 04:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c5af817-110a-32a7-8eba-2eb6b326d1eb | -10.67078 | -44.40506 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b03c90b2-256d-3135-ac38-259c318f3c6e | -11.39951 | -52.942 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 78b15665-ad17-3988-8a41-b3163f84d4db | -10.66967 | -44.4028 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d88765d-9e2e-35fc-bfd1-9b396a4f534c | -12.82821 | -47.40901 | 2025-05-07 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 901dc5ab-3343-3869-b588-e1a82533a7a7 | -11.4147 | -48.71237 | 2025-05-07 04:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c56eac71-8cc1-318c-ba2a-bd05799d463e | -11.80274 | -47.37648 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77aa70a7-160b-308c-b529-903aa2f0dcd5 | -14.69004 | -53.39043 | 2025-05-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28e65b7-9bc8-3db4-95f6-763e4c51c695 | -10.71428 | -42.32177 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4e1abf84-8b1d-33ec-9231-2f53fb016e67 | -11.7834 | -47.35993 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa1c1e42-af96-39aa-91aa-f76b28986115 | -11.38706 | -52.9393 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 21fb7c9a-e864-3f70-80d7-3224d8e8a623 | -16.04413 | -43.80604 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a600148-d193-3161-b771-10f21face6ec | -17.77879 | -42.81019 | 2025-05-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f13f73-0184-3620-a145-62ede2e1b0ae | -14.30746 | -44.28352 | 2025-05-07 04:04:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7674bd5-67fb-3acd-8ea8-c13ec242996b | -11.39429 | -52.93571 | 2025-05-07 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f620111f-1e42-3976-b404-1826f4ecf686 | -16.64033 | -45.14025 | 2025-05-07 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f85c1f6-06b4-329d-bcf3-dc7fe315d890 | -15.22399 | -51.55531 | 2025-05-07 04:04:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4980551d-9767-3fb0-a512-98148ed0f326 | -16.65859 | -43.66449 | 2025-05-07 04:04:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca4e3128-bbac-3136-afeb-91aa49ac8a9b | -11.77368 | -48.70969 | 2025-05-07 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd2c6c38-1fd7-3f9f-9374-09666fa815bd | -9.26873 | -47.90396 | 2025-05-07 04:04:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README5.md)
