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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1149c436-103c-3e39-901c-46192f393006 | -22.78169 | -47.12345 | 2025-09-12 04:29:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b29269f4-ebfa-3d4f-9969-f03e3a876de2 | -23.35308 | -47.15085 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44499e39-e408-3674-9962-ef82292e4896 | -20.57346 | -44.36272 | 2025-09-12 04:29:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b24e70fa-59c5-3aad-b273-a7022ede4bc4 | -23.14299 | -48.25628 | 2025-09-12 04:29:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 857325ce-5581-3c91-be14-fd0c9979486b | -21.00022 | -46.05783 | 2025-09-12 04:29:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69b41cc3-b47e-3433-959a-0aa545255475 | -22.63032 | -53.09346 | 2025-09-12 04:29:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3ef2d7c5-e476-30df-a3c9-2b7881a6fe1b | -19.99159 | -47.63472 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba0433e-cd84-3390-9641-4bb2c909ff97 | -22.62678 | -53.09274 | 2025-09-12 04:29:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c6eae245-53a3-3bc2-b342-74fb2b9310d0 | -22.22472 | -49.60538 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88417b53-9463-360a-b150-d002f19520c8 | -19.99387 | -47.6429 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8da67994-9f1c-3b36-b2dd-bd4b6ca5e97a | -22.18652 | -49.59204 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a12dbe39-133b-3e58-92e1-87179bd9e54a | -23.10746 | -47.49786 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6f25a33e-5022-31fb-b6a3-5737433addda | -23.42555 | -47.02267 | 2025-09-12 04:29:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 593b42ea-7806-316f-9fbd-9f1fc734e879 | -21.33874 | -45.0344 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68beb5fc-a4fa-334a-8063-7ea61aa96400 | -22.6591 | -53.11726 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45a7bbb4-b63a-39c6-a792-8f265d5e3d12 | -21.18859 | -47.52498 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a36b80ef-e451-325e-a31b-c2a2f1abb0ff | -19.99883 | -46.9177 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a6ac49-d61c-3554-8b05-0ba35f80bc2f | -20.48399 | -49.73178 | 2025-09-12 04:29:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0892e9f5-d753-3438-8846-39ab5db06f9f | -23.27431 | -46.54699 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ff0aa6a-f68e-3104-80d0-c4c11d1c0ae3 | -21.48779 | -45.94053 | 2025-09-12 04:29:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7925a43e-dd5b-3553-a06e-9dfcc17d84fa | -21.953 | -47.55116 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4c27533-5a21-3acd-8d37-f21645f53a31 | -21.964 | -47.54877 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfba5bcb-c734-3e98-a52b-53dd30714afc | -20.55665 | -46.35862 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45ba11ba-07bf-3167-86ad-43aad701417a | -22.94892 | -47.47121 | 2025-09-12 04:29:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7697e493-c216-3ee9-a9d8-1859186dbb4c | -21.34013 | -45.02386 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4123e668-1ee5-361c-b644-6a7ca3362d18 | -22.13883 | -47.83644 | 2025-09-12 04:29:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7146dd60-60ff-332a-8c94-a9fa982f981e | -22.85148 | -47.34385 | 2025-09-12 04:29:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3a1efe3e-181d-3c2e-b8a0-9984ae9eb22f | -23.39322 | -46.71208 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc9eabf6-0561-3561-a671-756788e9d859 | -22.66541 | -53.12304 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e237c87-9641-3aa1-972b-7fcd1a235234 | -22.63462 | -53.08988 | 2025-09-12 04:29:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 417ca592-a3aa-342c-892e-527ab594855a | -22.19157 | -49.7347 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e3a07c53-3a61-3a85-9bcc-66d330f2bc15 | -22.52172 | -45.09802 | 2025-09-12 04:29:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8339507c-fb17-3590-83a6-d9f5fa4db220 | -21.32264 | -45.00545 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7fd99791-e845-3684-9990-3afa3553cd66 | -23.16262 | -47.48938 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 07a69308-c774-38e9-94b3-4bdc36f9a9b9 | -22.40182 | -46.74766 | 2025-09-12 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| df658c35-656f-3538-b83a-c591667d7299 | -23.13325 | -47.49347 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 10e5573c-36ed-33c2-9e53-4655acfa0167 | -22.65632 | -53.11223 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 04544357-16da-3a64-acfa-0a4275652f9f | -21.96221 | -47.56115 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f20e1493-23a8-36da-a5d9-d24bfeb584af | -21.32063 | -45.02088 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 30d74435-11da-3929-b418-eb13693a8c57 | -21.64857 | -50.11964 | 2025-09-12 04:29:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 40c0ce40-f5ed-37ad-b2c0-c742a0a67152 | -20.69948 | -46.07633 | 2025-09-12 04:29:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca56576-129c-3344-b953-16e814f46ae3 | -21.95359 | -47.54702 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df175acb-940d-3b59-9e0b-a758230c1a6e | -23.14035 | -49.65364 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ffd79971-2f5b-33ef-8a94-a18839423bb5 | -23.11156 | -47.4942 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 248f6a93-f15e-3301-b9f8-0d2628c62951 | -23.09452 | -49.86179 | 2025-09-12 04:29:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1c1c995c-f12e-3e92-8919-45c75df7159b | -22.68636 | -45.52343 | 2025-09-12 04:29:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ffa0aba6-704c-3d49-b18a-671026cacd51 | -22.66895 | -53.12378 | 2025-09-12 04:29:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4b959a8-6e8d-33b1-b31c-f63ec52ac04b | -21.62336 | -46.80027 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| efcfc628-ae5f-3dd0-9e6c-1a04362f35a8 | -21.19205 | -47.52553 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 11c26fdd-6cd4-34e4-b319-8d7ac041a646 | -22.35417 | -47.54807 | 2025-09-12 04:29:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d87d59a-c84a-320f-9e67-116ac9bcd29c | -23.60408 | -47.18876 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6419f352-fe73-3814-adeb-940c61e0929f | -21.94141 | -47.55763 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c463dc23-6a1e-37d7-9c2a-3b163ce015cd | -23.14329 | -47.47326 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fbaa09cb-a0a4-36a6-a929-d13d6939f2b7 | -20.01545 | -47.6386 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ca7a240-3d13-3f83-bba1-5707c884cac1 | -23.54315 | -47.60269 | 2025-09-12 04:29:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 99090fc4-290a-39eb-a36a-1d5a18059f1d | -19.99783 | -47.63969 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05cd2d82-932f-3605-8309-7e628c15def3 | -20.5853 | -48.57674 | 2025-09-12 04:29:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16073d4f-7c1f-3d65-893f-d9f7c6eeea0b | -19.98818 | -47.63413 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a212b7e3-feab-3246-9ff5-bf4ddbff1bf4 | -21.33764 | -43.50918 | 2025-09-12 04:29:00 | NOAA-20 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| cdfaa85e-50a0-3c35-ad95-16cc573fc9ac | -22.26211 | -49.56218 | 2025-09-12 04:29:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56f11ddf-ae1c-35e2-adc6-ad3ca00a79b9 | -24.11895 | -48.7032 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 93fada93-f23f-34f3-a6b4-6e935f15ec8f | -23.11567 | -47.49057 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6a958aa5-756c-3da7-ab5f-6ac3c8ed7b82 | -23.12211 | -47.49593 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f137bba-3aab-3ff3-8332-8cbef76b2ef9 | -23.52133 | -46.97625 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0f60b41-1d04-31cd-9215-3082218c54ee | -22.18494 | -49.73351 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 290.9 |
| 4c76ff1d-f9f4-3846-826c-2c13f8eff893 | -22.79302 | -47.80439 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 626d101d-dab2-311a-8239-4fd0822935af | -20.37044 | -49.97677 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a89e8f68-02b5-325f-8661-ea6816993e8a | -20.00066 | -47.64416 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd7c1e1a-e7a7-3015-aabf-90dfbde9944b | -22.18594 | -49.59576 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b6639ae-1a08-3d55-b119-0ddc28879617 | -23.12329 | -47.48749 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f3561d6-2f7e-3618-9614-db83e9d2a711 | -23.19188 | -49.64712 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 390ae2d8-7bb2-3ab3-90c1-2adf8919d064 | -20.01486 | -47.64256 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d9299d0b-90c0-35ae-89d5-2bf29b51c656 | -21.96281 | -47.55704 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8021af19-4f9f-3a5a-9dff-ea58aa536eed | -20.57177 | -43.78155 | 2025-09-12 04:29:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69d058b5-10c7-3910-9f05-17c81d3cb395 | -21.36983 | -45.16576 | 2025-09-12 04:29:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 50d96039-87b3-307c-bb56-f2481e14d704 | -21.48717 | -45.94516 | 2025-09-12 04:29:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 67004e21-3e6b-3aa4-9fe8-4b6cac8ff621 | -22.4533 | -46.14961 | 2025-09-12 04:29:00 | NOAA-20 | BOM REPOUSO | MINAS GERAIS | Brasil | 3107901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d1d537bd-f7b6-3e9c-bcca-63a3d12aab46 | -19.97292 | -47.59557 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e6707ce-738d-3ade-9a0c-be1d1e2c75c9 | -23.53985 | -46.17192 | 2025-09-12 04:29:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5fd47a9f-6716-382e-8de7-36c79f0d5b5c | -24.80179 | -50.23133 | 2025-09-12 04:29:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 580530cc-1240-3b70-9230-e8bd17ed9114 | -23.19463 | -49.65149 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 727d29b6-6527-323c-8c4c-0d499476fb82 | -21.91752 | -47.91695 | 2025-09-12 04:29:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8827dd43-4b42-3eca-a705-963a82317e0c | -22.3976 | -46.75152 | 2025-09-12 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 57c03ff3-2586-39ce-ab51-c574dc929e38 | -22.61077 | -46.41657 | 2025-09-12 04:29:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ba802a6e-8320-3938-a413-2fd062b3eec6 | -20.00933 | -46.91927 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f4f3c6c-4e5a-339e-9369-c1567dac60eb | -19.98252 | -47.62522 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b36c89b7-7b5a-3820-80be-d3d3e68d2f59 | -22.61014 | -46.42128 | 2025-09-12 04:29:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f4216409-33f9-3248-afcf-8e0fdf8309a4 | -20.35615 | -48.40764 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d2407fd-ee9e-3aa9-88ba-100c7dae0ac1 | -21.84647 | -46.50954 | 2025-09-12 04:29:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 409855c4-773a-327b-ae10-6a3daeed942c | -20.56946 | -44.36204 | 2025-09-12 04:29:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d604ad64-1e9d-3944-a6e0-ee1eef0ab76e | -22.78898 | -47.80779 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92fb67b8-798e-32b9-b375-8546121a54b1 | -19.6678 | -57.00269 | 2025-09-12 04:29:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 594142c9-12da-33b3-85de-5b6b391aa6bf | -24.16848 | -51.03464 | 2025-09-12 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a323901d-6f54-3e9c-b9e3-b8128582da86 | -23.11801 | -47.49954 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| ae825825-108d-3f3a-9104-e030c8b8a1d5 | -23.2214 | -49.43097 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1f3cddcc-03a3-33e0-a639-ad3affdd2024 | -22.40121 | -46.75208 | 2025-09-12 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 91a879b6-8f30-3f4b-914d-239aba365ef5 | -23.35187 | -47.18662 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3040821d-f9eb-362b-bfa8-b65b9b12d460 | -23.30747 | -51.12577 | 2025-09-12 04:29:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 668f8c93-4ca2-3372-b3bb-48c0fce16cef | -22.68391 | -45.5251 | 2025-09-12 04:29:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7a176140-1283-3888-b761-425c0e9cc295 | -22.66618 | -53.11872 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README94.md)
