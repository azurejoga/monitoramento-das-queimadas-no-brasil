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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d847a04a-36f0-371f-9952-835978b4edf7 | -19.59869 | -43.68313 | 2025-09-07 04:00:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52bbf887-8e28-36ea-bec0-1911c3299b27 | -14.44904 | -48.45837 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e214a9b-a312-3a9d-984b-1cc71900b667 | -15.36177 | -43.66807 | 2025-09-07 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3185e7f7-baa5-3fd7-abb7-24f01ba79bbc | -14.56179 | -43.72746 | 2025-09-07 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a3c9d1-71a6-3426-b14c-092098cc7ba4 | -15.73203 | -47.02443 | 2025-09-07 04:00:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3b5f3ae0-8d9f-3238-a7a7-f48e2bd36c51 | -14.45002 | -48.45326 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 460fdb69-05ca-34e8-9a38-476116d508e8 | -19.89813 | -41.44254 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 917ac085-bd06-3a57-b6ad-c14e2c7a7cef | -15.84176 | -52.27722 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 31a33ecf-8e11-37d3-b334-87517d7aed7c | -14.26818 | -44.97235 | 2025-09-07 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e79f7762-11c3-39f1-bb4d-f9efd6debbfc | -19.51002 | -42.57091 | 2025-09-07 04:00:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2e80caa0-ad62-3a84-b061-f8c97eae118b | -14.48624 | -48.77128 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df9d11d8-75e3-3723-866b-45daf787f212 | -14.58602 | -48.09847 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a3d7825-226c-329e-99f5-abac9da50b71 | -13.71591 | -46.88601 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd498283-f128-3ffe-aa53-191b3b458039 | -17.6723 | -43.52854 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a521663-aa94-3f72-9e2e-562b9e5c69f8 | -16.93788 | -45.76266 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd96a886-cad6-3f5f-ba89-aa38ecf14e82 | -16.30353 | -45.69271 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a35d66f5-2994-37f0-bf18-1cb199a1658d | -21.62885 | -44.01232 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d922fa55-d85f-3a1a-b93b-77ab92aa0f29 | -20.54907 | -46.44608 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2193b329-eb41-3a5d-84c3-78cc55cd73f1 | -22.69405 | -46.92222 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| afb5658b-f88f-3aff-a7f9-496dc61dfdf2 | -20.54243 | -46.43818 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da36c34d-e8f0-3609-886b-302289e00c40 | -20.40802 | -43.76812 | 2025-09-07 04:02:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 445c46a0-9bb6-307a-84f6-566db684722f | -23.0171 | -44.93802 | 2025-09-07 04:02:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8096ed4b-3f0f-3bd9-9467-b616df866e96 | -22.69386 | -46.92611 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a34c378-741f-3d49-b5df-fd0b77dbff41 | -24.14527 | -49.5169 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f70756-2454-309f-93ff-3c59a8339ee4 | -24.14181 | -49.51136 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6eea47e1-d321-3a77-981a-23a6b9bf7b75 | -20.53268 | -46.44685 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d702a0ad-a914-3299-8868-2e8daf4df9fc | -22.41801 | -47.44011 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7c039861-eef6-3af4-a766-3208a5510482 | -21.62816 | -44.01632 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 36db7f76-ec73-39b3-97e2-4552164449a5 | -21.70961 | -45.38498 | 2025-09-07 04:02:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9f09371a-93fa-3c92-aabf-6f5d480c4f25 | -22.42274 | -47.43724 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 18b573b4-bfdb-327f-93a5-56b58956094c | -21.21131 | -44.33466 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2c17ea51-16dc-347b-aaae-f17792489d66 | -20.54422 | -46.45034 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a663739e-fa11-3260-85fe-ef22ee3f1452 | -21.86425 | -46.49438 | 2025-09-07 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa9f7e7d-f5ff-3901-b5ab-4a2b3580da85 | -22.69968 | -46.91645 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 26d45d4f-de35-3087-9234-f67bfe02fe46 | -22.77601 | -51.30649 | 2025-09-07 04:02:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 402fdc44-95f3-35a7-a549-d9ebf66482df | -24.14708 | -49.50823 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3e6b607-a1f4-3ecf-acd9-e5e44fc79cd6 | -22.70284 | -46.91848 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ee06b25c-c5d0-3fc1-b12c-117d6046c4eb | -20.22094 | -44.2057 | 2025-09-07 04:02:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2475ff42-9258-3214-bef9-e14f2fc5af4d | -21.20705 | -44.33976 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5dbf59ce-399c-3f35-8359-73b23fd7b8c2 | -21.48332 | -45.56113 | 2025-09-07 04:02:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f1278f20-3aed-323b-b373-cd815561b54b | -20.40734 | -43.77214 | 2025-09-07 04:02:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0662f8d6-735e-37ad-b6f3-23c405117105 | -23.5519 | -49.9062 | 2025-09-07 04:02:00 | NPP-375D | QUATIGUÁ | PARANÁ | Brasil | 4120705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 219f1e0d-b28a-3141-a05f-4b94ab68067a | -21.29514 | -43.95507 | 2025-09-07 04:02:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| be697352-3fa4-37d2-93c5-54e925345483 | -22.33024 | -49.37901 | 2025-09-07 04:02:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 193a01c6-99ab-3b12-873d-c9c9e4b9ec5a | -23.43011 | -50.80023 | 2025-09-07 04:02:00 | NPP-375D | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| dca3623e-632e-3380-bbba-507147d474a7 | -22.33017 | -49.38083 | 2025-09-07 04:02:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6326112d-0561-32b6-9d9d-a3a75faf04bb | -20.79575 | -49.32553 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c65a8acc-abfb-32f4-b9aa-68433e27dd51 | -22.42134 | -47.44453 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 37e77a8b-5848-3978-9c98-ffc4c6748287 | -20.45821 | -42.52245 | 2025-09-07 04:02:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6235d2b1-713f-30ff-a012-09289c0901e4 | -20.33762 | -43.88715 | 2025-09-07 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e01cf575-3d58-3b45-a2ad-2f35c04ea5a6 | -21.70725 | -45.35624 | 2025-09-07 04:02:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c8b8caad-554b-3a72-aae2-7e88e5e726d1 | -22.69482 | -46.92089 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9cb3f451-ab09-30fa-b5b2-24b467bd000b | -21.20776 | -44.33563 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f64adc3b-9e3d-358e-a8b7-911b3e7ee52e | -20.35705 | -43.87837 | 2025-09-07 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b707ccc-7c0f-3c68-bb69-d770e8f730d0 | -22.41326 | -47.44302 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 36980319-9803-3adc-b225-bfeea343f104 | -20.10213 | -47.33498 | 2025-09-07 04:02:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09997a1e-3916-387b-b59e-3e7bef4b1b58 | -22.33117 | -49.37598 | 2025-09-07 04:02:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7f561eb-8f8b-33d8-937e-a47474d789ee | -21.62748 | -44.02031 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0237c683-47a2-33c5-849a-e9a1089184f3 | -24.14403 | -49.51021 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 799173a7-7466-37b8-9483-a3ab02bb3738 | -22.14525 | -49.12278 | 2025-09-07 04:02:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bf002b3-a041-3344-a6db-afa5fc76fd55 | -21.20708 | -44.33813 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 552d6def-c002-3a2e-be2a-49b1ca801823 | -22.41731 | -47.44376 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 810c9963-7bcc-3779-b727-555b80062888 | -20.53654 | -46.4479 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b646fb3-571b-3e53-9d2e-63a2cd84f9e6 | -22.4147 | -47.43561 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f5c3cee2-bde4-3d02-913e-4335d91b21d1 | -21.48616 | -45.56659 | 2025-09-07 04:02:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 0409f44b-b885-374c-882f-04d318a54eec | -21.83627 | -46.45205 | 2025-09-07 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aba91249-54c9-381a-b0ea-23a27d071b9f | -24.15097 | -49.5215 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5d055c5-1da5-39f3-89f0-bad00df9a71b | -21.2078 | -44.33401 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| af8c51ad-54ff-3eab-a061-571313afa40f | -20.54039 | -46.44907 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dac800b6-ad2a-3718-8b8c-cdf02395c0ff | -24.14617 | -49.51258 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3325572c-f07c-3d68-8fe0-44fb9fdc00ce | -22.69872 | -46.92162 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9ffc051e-10c9-33d7-8e9b-86ecf2a0d62e | -22.70404 | -53.24864 | 2025-09-07 04:02:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 24b7cf81-b377-39a0-9b40-5e3b0ccd99ee | -21.62404 | -44.0196 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 92b9e42a-6e1f-3788-a06a-45811f0a0cb8 | -22.87549 | -47.14056 | 2025-09-07 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| afa540f5-5d52-3bae-85c5-9e4fda789062 | -24.14272 | -49.507 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd8b8c39-ba05-3303-aeb2-346dddf75f66 | -20.54803 | -46.45167 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9c0f41a2-c86e-337f-8a9f-8bf8aeb2615c | -22.41397 | -47.43935 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3c7cc9f-9e1e-3507-8cba-22792c2adf0c | -21.71131 | -44.51837 | 2025-09-07 04:02:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e5ce9dd1-7af5-3e0f-ae0a-3a92b7eee6d7 | -20.33415 | -43.88652 | 2025-09-07 04:02:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 611da33e-79c8-3e9d-91b2-fb21c1df9c79 | -22.69794 | -46.92295 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 64336b7f-a2e2-3d59-aeb1-8de7bd68f642 | -22.7767 | -51.30325 | 2025-09-07 04:02:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4dc6f430-7fc6-36cb-973b-6ceeea7c1826 | -22.69776 | -46.92686 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5cf426e0-1e25-3556-bcb3-d689019f0bf7 | -20.24002 | -44.8498 | 2025-09-07 04:02:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d849b4b5-6a8a-37bb-91b6-036f6bbe250b | -20.26178 | -44.53381 | 2025-09-07 04:02:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7f89ee9c-9fc9-3781-b675-113f63ebc282 | -21.6316 | -44.01703 | 2025-09-07 04:02:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9f068edb-353f-3e88-b052-d52b5b79f2a2 | -21.487 | -45.56192 | 2025-09-07 04:02:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 426f86b6-af84-34bb-b4b9-d73d5f93338f | -22.42204 | -47.4409 | 2025-09-07 04:02:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4782e0d5-0f2e-39ae-a4bb-f672a770b903 | -20.54141 | -46.44362 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bf0e4304-c737-34ee-8249-b43923ca4535 | -22.69579 | -46.9157 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 94ca7c21-505b-3b9e-970a-d525f13283ca | -21.48248 | -45.5658 | 2025-09-07 04:02:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4e94e4bd-57d1-38c5-ad5b-e3370ea652b6 | -20.79745 | -49.32778 | 2025-09-07 04:02:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cc592083-6acb-3bad-bc0e-ed76d61487ab | -22.69504 | -46.91703 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 376f0e50-43f1-32f8-b10a-a8a551d73e1a | -20.10015 | -45.31785 | 2025-09-07 04:02:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41065ba9-5830-3cf5-a094-f7fe9f7d6ab8 | -22.42605 | -47.4418 | 2025-09-07 04:02:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0f6d1ab-6236-3e18-836a-d2055aa2dcf4 | -22.69893 | -46.91778 | 2025-09-07 04:02:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 939d3b66-0271-3644-acea-34870af6c623 | -22.1471 | -49.1219 | 2025-09-07 04:02:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de88981a-9b54-3f59-85c5-dc89acd00f42 | -24.15009 | -49.52588 | 2025-09-07 04:02:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c6838d1-93b1-34a1-8046-c8785b67d285 | -20.77334 | -44.45973 | 2025-09-07 04:02:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 92004bdf-4701-31c4-88a1-3c19188fde5a | -21.42813 | -44.16801 | 2025-09-07 04:02:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3c10b9e7-b3e2-35c8-821a-4397aed999d4 | -20.77261 | -44.46386 | 2025-09-07 04:02:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README39.md)
