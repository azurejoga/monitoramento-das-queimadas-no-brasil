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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 941142bb-f405-3c97-9486-3fb2682c1fac | -18.65568 | -52.59665 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ca4db86f-ccb8-3ee3-b78c-f2a10739307b | -18.65871 | -52.59969 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e0725831-d623-341f-a4ed-e23c4fb0e444 | -20.41197 | -46.41047 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 591e4e2e-fc92-3990-90d4-1a3eaa0e268e | -22.45388 | -49.01371 | 2025-09-01 04:36:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61589def-b344-3590-b199-ddf86c14acba | -23.10994 | -46.61185 | 2025-09-01 04:36:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e28383d-8e9c-349b-bfe1-7e610de000dc | -22.34619 | -48.3804 | 2025-09-01 04:36:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4ec42ac9-3472-32a6-b159-75ba88932800 | -19.34559 | -44.00128 | 2025-09-01 04:36:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55dcb707-989a-38a9-930f-4bc33f80af56 | -20.6319 | -55.31234 | 2025-09-01 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6834343-6e49-3b31-9b46-8aac605f9375 | -19.83998 | -44.99387 | 2025-09-01 04:36:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d070c08-7811-3462-8d68-b5b4ec5990b0 | -19.48017 | -46.58444 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f8da86-6bce-3420-9ef8-5e43354c0776 | -18.65909 | -52.59729 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 90d14dfe-43fa-3d2e-8d92-6726f77821f8 | -22.36086 | -52.13605 | 2025-09-01 04:36:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 336dd733-49c1-31d7-a581-573f2cc92e80 | -20.40034 | -46.40806 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33e6f493-eecb-3686-ab76-67b7febcfdf1 | -23.38712 | -47.04989 | 2025-09-01 04:36:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ac303f7-42f6-38ff-a1af-5e7110c20227 | -21.3558 | -49.05135 | 2025-09-01 04:36:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 49adf399-47c0-390f-986a-b0222d74bd0e | -19.12141 | -46.45163 | 2025-09-01 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8eff908-74d8-3d03-8d10-63d62fded68e | -23.18948 | -50.67086 | 2025-09-01 04:36:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5100c4ff-956d-3366-b010-ac96b1a88b5d | -20.13408 | -44.97506 | 2025-09-01 04:36:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebb7b663-c020-3cdd-a8f6-27f1eae127e3 | -20.40809 | -46.40971 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79ffdf1a-a0bc-3cb7-a1a9-90b944586427 | -19.49101 | -46.59096 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77af93ac-9e90-3fb3-837d-2534d839a9d5 | -22.98776 | -46.22038 | 2025-09-01 04:36:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec71f825-a99c-34ee-8f29-621563b9b018 | -19.50682 | -45.31574 | 2025-09-01 04:36:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e1c8cf-c13b-33f4-820e-b94f9dffcbce | -20.80984 | -45.62546 | 2025-09-01 04:36:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 161957b4-422f-39b8-928f-03706802f4e3 | -23.18971 | -45.74925 | 2025-09-01 04:36:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e816b8ee-7728-3822-b5cc-7f7655d34fb8 | -19.97216 | -50.22223 | 2025-09-01 04:36:00 | NOAA-20 | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db365a5a-44ed-30a1-92a9-430faa8d3d57 | -23.80537 | -48.14709 | 2025-09-01 04:36:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8272b02f-f272-33a7-8c6f-258bc81db092 | -20.98015 | -48.85974 | 2025-09-01 04:36:00 | NOAA-20 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 051dfc8a-bd36-3390-bbec-b6f5f5b0dcde | -20.63475 | -55.31796 | 2025-09-01 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0e2d86-3491-35e2-bfc0-d242248b82c9 | -18.65936 | -52.59586 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3809d94c-07d9-3798-9f41-bbba2ce35ab5 | -21.11442 | -47.80171 | 2025-09-01 04:36:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db660b36-08ad-391c-9caa-ca3425e75079 | -18.91488 | -47.19878 | 2025-09-01 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9b95e0d-e119-356f-bae3-0af91615c1a6 | -21.35521 | -49.05542 | 2025-09-01 04:36:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4bf7b37-691e-3f52-b844-c1446d53f323 | -23.8456 | -50.7028 | 2025-09-01 04:36:00 | NOAA-20 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26f53fae-06a4-3c3e-b153-b6e149ccc439 | -19.69334 | -49.33168 | 2025-09-01 04:36:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62278ceb-d9d0-3be4-8f10-8c01124e1b3b | -22.25012 | -54.88805 | 2025-09-01 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e1ce44ff-23ab-3b6e-9755-9e045110fadd | -21.08265 | -48.22561 | 2025-09-01 04:36:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c900ea34-2517-389c-965f-6352a10f970d | -21.08982 | -48.22674 | 2025-09-01 04:36:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc06d188-8ef3-3c5f-9e82-cb30807d097f | -22.37624 | -52.44403 | 2025-09-01 04:36:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 471f1eb7-12a3-3b9a-af19-f89a62f72ea3 | -29.06533 | -51.67052 | 2025-09-01 04:38:00 | NOAA-20 | COTIPORÃ | RIO GRANDE DO SUL | Brasil | 4305959 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7366fbd-1a59-3467-b66b-ddda95a7c22c | -26.32288 | -52.70364 | 2025-09-01 04:38:00 | NOAA-20 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5509ea1-b40d-3f61-8001-cdc8c425e371 | -23.74161 | -54.94304 | 2025-09-01 04:38:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d34b8940-5de5-3331-93b5-0a8eabbf8d9f | -23.73458 | -54.94149 | 2025-09-01 04:38:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9dd844cc-9dc3-32d2-95a3-bbddfb5de86e | -29.63801 | -50.92916 | 2025-09-01 04:38:00 | NOAA-20 | ARARICÁ | RIO GRANDE DO SUL | Brasil | 4300877 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 67fe693e-a5bb-3133-889c-f0b16391450d | -23.78905 | -54.59205 | 2025-09-01 04:38:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6e304ae1-f7fe-39c5-b915-3cdda8140dfa | -29.06474 | -51.67464 | 2025-09-01 04:38:00 | NOAA-20 | BENTO GONÇALVES | RIO GRANDE DO SUL | Brasil | 4302105 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 427c7947-6010-375c-a5f0-752680f47ec8 | -26.3262 | -52.70428 | 2025-09-01 04:38:00 | NOAA-20 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4122aa54-a91d-37d3-a72c-0b6b9fd828ff | -23.73534 | -54.93717 | 2025-09-01 04:38:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53cb44b4-8259-37ca-9954-0c7519602960 | -9.135 | -65.5453 | 2025-09-01 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 23b5568c-aa31-3fb0-9a54-8e15deeb3493 | -6.8281 | -52.8143 | 2025-09-01 04:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f0ebe530-0adb-3924-8710-a449b04ea478 | -7.076 | -44.3376 | 2025-09-01 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4d3c1d05-b085-352f-87a8-c9fc8b42a49c | -7.0757 | -44.3606 | 2025-09-01 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bdaef670-72f5-3b0c-afaa-6b1bbc358670 | -8.7684 | -61.4261 | 2025-09-01 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 547b9383-1ed7-33ec-85ce-bc813cc4c957 | -7.0946 | -44.3589 | 2025-09-01 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7fadc8fa-7f56-38b3-b299-933813d0ca2e | -7.0948 | -44.3358 | 2025-09-01 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 1f439329-491e-3770-a19b-29640303c64b | -7.0948 | -44.3358 | 2025-09-01 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 828af185-54c5-3b1a-a371-c48b6f4dc664 | -7.0757 | -44.3606 | 2025-09-01 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a8e0ea99-8513-3f74-b17a-c6b9f95c32d4 | -7.0946 | -44.3589 | 2025-09-01 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e36accb8-8311-317a-b605-7e1756c272b7 | -7.076 | -44.3376 | 2025-09-01 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c7177bb8-5999-381f-a636-5d6584442f90 | -6.8281 | -52.8143 | 2025-09-01 04:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c9b937b0-cdaa-36ae-913d-210f567985ef | -11.026 | -47.0538 | 2025-09-01 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| cb1155f4-9571-32b5-990a-c33939ba00fb | -11.045 | -47.0514 | 2025-09-01 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 67d03e8c-2425-35e1-aebc-4947383f5664 | -6.8281 | -52.8143 | 2025-09-01 05:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 882dfd2a-f9b9-3628-bc0d-da6d95c387b4 | -7.6783 | -61.0908 | 2025-09-01 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 361506f3-d713-37a7-8334-c2394de79652 | -7.0948 | -44.3358 | 2025-09-01 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 92f49806-7055-314e-ab24-208a095555a4 | -7.076 | -44.3376 | 2025-09-01 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5ceb4b5d-d111-3cfc-9fa7-9a8eb2f35ff1 | -7.0946 | -44.3589 | 2025-09-01 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 519730a0-fb3f-3629-8584-708a7d6b53b1 | -11.0447 | -47.0738 | 2025-09-01 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 190124b2-a0bb-32e4-88e3-f7044a939693 | -7.0757 | -44.3606 | 2025-09-01 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f58dae6c-7c3a-3bf0-bfac-7d98f47f3e7a | -11.0454 | -47.029 | 2025-09-01 05:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fbe20555-42b5-34c1-bb09-06372789bb54 | -12.5722 | -48.2059 | 2025-09-01 05:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 984b4b28-aee7-3e53-9d05-e8172566fcc2 | -11.0454 | -47.029 | 2025-09-01 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a7a122ca-b0a8-318f-b930-2ba8f8da5bea | -6.8281 | -52.8143 | 2025-09-01 05:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e23329b1-4c01-383f-ab35-35fad3ae30e9 | -15.7294 | -48.9669 | 2025-09-01 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ed8008b3-9964-331b-b108-78a708b0e6aa | -7.0948 | -44.3358 | 2025-09-01 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f10ebcec-6c78-3d11-8138-6f344060f72a | -12.5722 | -48.2059 | 2025-09-01 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9deac176-7c49-3fb7-a983-9e6687264bc6 | -11.045 | -47.0514 | 2025-09-01 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b9f396f2-69b8-3d55-b776-8c960e37f97e | -7.076 | -44.3376 | 2025-09-01 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6ffb4178-14c8-319e-abd9-fe90eeca53af | -7.0757 | -44.3606 | 2025-09-01 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 44b2af8b-3997-3ddf-9e7f-4e26a2c2fbb6 | -7.6784 | -61.0717 | 2025-09-01 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a86f783f-b8ff-3cda-8837-5df03f2f3980 | -15.5867 | -48.321 | 2025-09-01 05:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 06ee5e58-b697-3744-bc1a-0315855fbaf0 | -15.7289 | -48.9892 | 2025-09-01 05:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5ce7dce8-6ee1-3c8b-bee1-2cdce2bd1f85 | -11.0377 | -45.1487 | 2025-09-01 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.6 |
| 552f9986-44c1-3fc2-918d-649ef8428ff2 | -10.6131 | -44.3051 | 2025-09-01 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a819f115-c828-3d82-b03c-4ec6a961b08f | -7.0948 | -44.3358 | 2025-09-01 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3b07d035-ca7f-3e56-ae34-312070bdff65 | -21.3468 | -49.0553 | 2025-09-01 05:20:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| ad010dcd-3fe0-302b-99f3-24ae723d2122 | -11.8185 | -46.4087 | 2025-09-01 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 956cf0f1-1475-3524-a852-c0809aeefce5 | -19.482 | -46.5768 | 2025-09-01 05:20:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 746cc47f-e70e-3ffa-8118-51c69f8cdca9 | -15.7294 | -48.9669 | 2025-09-01 05:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 6f179467-381b-3bff-b93d-4eb0d8aab248 | -14.7422 | -46.7701 | 2025-09-01 05:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f1f4c23c-03d2-3caa-a8fd-42a9229a0ef4 | -7.0946 | -44.3589 | 2025-09-01 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 464368a8-57b2-3068-a35e-da2ff90d20e2 | -11.0373 | -45.1717 | 2025-09-01 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 66757cae-bf44-39a6-aa92-fd3371e4e862 | -12.5722 | -48.2059 | 2025-09-01 05:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ee9803cd-e981-341a-ab37-a3407294d091 | -10.594 | -44.3077 | 2025-09-01 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ec88a3e0-99dc-307c-be88-8171205c76c7 | -11.0572 | -45.123 | 2025-09-01 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c94b25da-dd4b-3b57-9af1-154dff9dcf65 | -10.6128 | -44.3284 | 2025-09-01 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 791601f3-d701-34c6-8404-21d8ae7cc4b2 | -11.0568 | -45.146 | 2025-09-01 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 2b3625f7-3ce6-35d7-859b-e4b937a2da97 | -7.076 | -44.3376 | 2025-09-01 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 08909f49-13cb-332a-a23b-d0951fdb5761 | -13.1644 | -45.2897 | 2025-09-01 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a2b049f0-711b-3769-a8d8-ed48d5e8b283 | -15.7289 | -48.9892 | 2025-09-01 05:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 92fb1842-0c21-3b12-b407-a76a53501730 | -10.5937 | -44.331 | 2025-09-01 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |


[Clique aqui para ver as próximas entradas](README75.md)
