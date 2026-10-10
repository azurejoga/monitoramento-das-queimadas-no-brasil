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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 662da337-a57d-3e5b-bef3-c8952699da15 | -10.8909 | -44.8001 | 2026-10-10 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c730ed64-8ae2-3c2c-bf81-8d53fc00529c | -7.535 | -45.3006 | 2026-10-10 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 43add492-3d94-3955-8529-169fd7247e76 | -10.8905 | -44.8232 | 2026-10-10 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 83979e64-11c5-33ea-9325-80c6ec21bf74 | -3.2389 | -49.4199 | 2026-10-10 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 7190f086-3ff4-3c61-ad4e-67b12ca0fc0f | -3.2204 | -49.4205 | 2026-10-10 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7d6e0589-d97b-3f08-9cdc-7ca6a204b212 | -3.2388 | -49.4411 | 2026-10-10 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a06c3bc0-94f6-3f80-ab3a-45cda9f84dd7 | -3.2203 | -49.4417 | 2026-10-10 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| bb69ae94-7a6b-38a9-bdae-2d3a9a65d8ba | -7.0228 | -47.661 | 2026-10-10 03:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1803c9e3-264d-300d-8457-0fb85a2b35b7 | -3.5676 | -54.6946 | 2026-10-10 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 008657b3-a6ed-387c-b110-732b05b373a5 | -4.4025 | -49.7774 | 2026-10-10 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ad5e44bf-76e1-303c-a405-8f0b0c175197 | -14.4003 | -54.9657 | 2026-10-10 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9a73d4b7-8add-3e74-9275-265a028404cb | -7.5347 | -45.3233 | 2026-10-10 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 50ab737e-9ee4-3251-a36a-cdc3292e3748 | -3.6048 | -54.5936 | 2026-10-10 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 84339eae-ac32-3a01-a0b3-b1bd4c41849e | -10.9097 | -44.8206 | 2026-10-10 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d4356b95-21f9-3d89-96de-90910b7bfce7 | -7.06324 | -40.95958 | 2026-10-10 03:23:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 703343e6-6119-3df4-b8fb-daaa56c28fa6 | -7.06973 | -41.60453 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e7e32754-2b15-3403-a3c3-bb9723f27e7f | -5.29594 | -37.32991 | 2026-10-10 03:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 76a28a90-c6c2-3150-9693-aaa87a84e284 | -5.86571 | -37.28072 | 2026-10-10 03:23:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 521e3f29-fe34-360f-92d9-51df14a8e447 | -7.07139 | -41.6016 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8c522eb1-931d-33c1-9cc8-7fe695088e1d | -7.22545 | -40.35845 | 2026-10-10 03:23:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2137f017-4580-3561-8817-6c56193ea6a7 | -10.1667 | -36.31991 | 2026-10-10 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 22f09287-efe5-3936-bd23-68dae0c50d95 | -9.89449 | -36.17096 | 2026-10-10 03:23:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 7fbbddc6-4e84-38b8-ab79-35c8fa4d645b | -7.09466 | -41.75821 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 747b6d15-d5b7-3997-b6a5-1d2f57c7ceb5 | -5.29542 | -37.3329 | 2026-10-10 03:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2b17e4c4-c430-3f7f-9040-2c711184aaf5 | -7.21368 | -34.90737 | 2026-10-10 03:23:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f96d5254-6f93-33a1-b215-952982b0f5ed | -7.22634 | -40.35369 | 2026-10-10 03:23:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b487056-1f7c-30b5-b2eb-455ac34d43bc | -10.16591 | -36.32432 | 2026-10-10 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ee755a36-58a2-39eb-8172-15b325532ac5 | -5.81561 | -35.38605 | 2026-10-10 03:23:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75fb6233-97f6-312b-b055-e61166110bd8 | -7.06495 | -41.59993 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a227bf4-ea23-37d3-96c5-b6b1a29ebf7f | -7.09572 | -41.75264 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4f72bf27-64ac-35c0-b681-c38e58a404b9 | -7.07051 | -41.60635 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb3eceea-7a1f-343c-8da5-8e55972ec620 | -5.81487 | -35.39048 | 2026-10-10 03:23:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d616816-a20a-36ca-875b-cee8903787d6 | -10.16229 | -36.31913 | 2026-10-10 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| a506c3e1-96c2-3442-a6d3-27aa578461fd | -7.07063 | -41.59988 | 2026-10-10 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 35f9112d-8278-3dad-9067-47665b91f2d4 | -10.16151 | -36.32354 | 2026-10-10 03:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a3a551f7-8f06-3420-962d-4d73fa5bfdae | -11.97166 | -43.47898 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba434d4c-118b-33f5-ac83-25858fd7649f | -15.85248 | -42.03944 | 2026-10-10 03:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b13e306-20f1-33a1-8be2-9e22a11ea04a | -11.9998 | -43.44526 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dfefbfc8-3cc5-321e-9f57-ee8606a9e878 | -11.12788 | -43.2569 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3ab5ca5d-c50d-3fbf-b0a6-ff4d6179f387 | -11.9668 | -43.49005 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60af0b57-0e27-31de-b4c3-0be9c2d09e36 | -11.08572 | -44.1082 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 394e927c-4901-3f91-a71b-192e51074cab | -12.05572 | -43.4115 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a30f32c0-9eb1-3e72-917e-1ba288e82a3c | -17.10213 | -41.57034 | 2026-10-10 03:25:00 | NOAA-20 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d73ecd07-eee4-3e4e-8fc5-8733307906b2 | -13.36572 | -43.8937 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2665dfa4-3994-320b-bb77-10d71c4532c0 | -11.59872 | -43.74913 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8471488b-ec5a-3105-99fc-58f775897cfe | -11.9703 | -43.47309 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e205c802-85e5-3020-9c51-ef07058a026e | -13.25862 | -43.9983 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae609aac-803c-3cab-83f6-2cf1413b71b8 | -11.94828 | -43.478 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbac99b2-eb35-327c-b4e5-983f1611f851 | -15.37219 | -41.91772 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77b88594-a6ba-30ec-8042-13a007aa1744 | -13.37307 | -43.90394 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c9a95c7-d84a-368f-9080-1430149f6290 | -15.38653 | -41.90673 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74c5a358-5548-33e5-ba37-174d06457738 | -12.771 | -44.88406 | 2026-10-10 03:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c2681b6-40b5-3da3-aca0-8a6f7a3e3e85 | -11.56965 | -43.71698 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26bc4b22-6ec4-3138-a68d-13b90798a562 | -11.99674 | -43.45975 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50637c09-965c-3d5e-bfae-bcc1dd895e10 | -17.15009 | -41.34002 | 2026-10-10 03:25:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f60dbb5-ff15-3bcd-8600-503b0230faff | -11.07573 | -44.12055 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5fe83c35-2f5c-3493-86c5-43c39894e06d | -11.83388 | -43.58727 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b9c55f-98ad-3621-bae5-b85b45a12fba | -13.36987 | -43.90715 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8bc3861-4577-34e8-8130-eb92a9c51000 | -13.38208 | -43.71907 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ea06292-53a0-3e68-8e89-c91a0d95b3f4 | -11.02728 | -44.05208 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09c9a439-d6fb-36cf-8d79-70bbf820e837 | -11.60015 | -43.7421 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fd45cd1-6472-34ff-ae2c-37b5ff689e75 | -14.46038 | -43.95909 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9750424-70fa-34e9-bdea-82d5cf145442 | -17.10059 | -41.57768 | 2026-10-10 03:25:00 | NOAA-20 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 270011ab-e2df-3fab-8917-3a21ab9d12de | -14.4564 | -43.9458 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 873a00ec-7a7f-3fd6-bd72-47c0fa5a9fa9 | -11.02761 | -44.02853 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea1f2165-2d96-34ce-8fc5-50d815048840 | -11.46111 | -43.38338 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7b92d3b-6c79-3e40-a2e7-1df686c4294d | -13.37177 | -43.90987 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0ae43a4-6a3a-33c0-8f1b-1c633342a321 | -11.9612 | -43.48323 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1e730a4-a941-3cba-a847-18f7167ecf52 | -11.03139 | -44.06748 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14d52bb3-4a20-312b-bbeb-5aeb5ef764a2 | -13.3757 | -43.89198 | 2026-10-10 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de36baf7-2a08-315d-b98e-8bd3c0b0ce99 | -12.05445 | -43.41757 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e29d47d3-f546-3749-9c59-db77139f4f5b | -17.34874 | -42.68067 | 2026-10-10 03:25:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd0fafe2-f8d7-393d-9a40-04118a8453ea | -11.99815 | -43.45308 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 054040e5-5152-34da-a69e-14c54f16bca3 | -11.07885 | -44.12201 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7cc6dec1-ea7d-3ff0-92ca-214ce2eb560c | -11.96785 | -43.48498 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25f2a09e-dd45-332c-aaff-56f95037b299 | -11.98227 | -43.46202 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0afca971-44f7-3b7d-8f96-5c487e4621fe | -13.38239 | -43.89346 | 2026-10-10 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c21aa9f-e784-328f-aa93-a140b0fe0bde | -13.26407 | -44.00572 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59eded9b-6aad-3e64-909e-64a01c408493 | -15.84679 | -42.03788 | 2026-10-10 03:25:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c08f8c0-4848-3e7c-ac0c-220fb9778a7a | -11.99689 | -43.44566 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d21e35fe-e638-36d9-a1cb-8b69bfc9cd6d | -11.97438 | -43.46619 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d238025-7739-3674-a44a-5835443a53e8 | -14.46168 | -43.9532 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4da2f952-d0c8-3a27-9ef9-67595f2fc83a | -11.96643 | -43.47066 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04ee0f35-3e73-3047-b6ee-60f3412f3a38 | -14.44587 | -43.93097 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7bd6319-3cda-3efc-b3bc-bace9694415c | -13.25733 | -44.00418 | 2026-10-10 03:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e532ddfa-01e7-3f64-95b3-5d67c39eb416 | -11.60311 | -43.72772 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a6c33e9-b90e-329a-ab51-d62e69dd3779 | -11.07722 | -44.11357 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a685ba5f-5ff1-3aa0-bd18-28d657f50b0c | -11.08732 | -44.11663 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| afcc6200-9f1c-3be7-85ce-5f4dfdcc499d | -11.59499 | -43.73251 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1e4d6fb7-a664-3e1a-b232-343a9bc6abb1 | -11.56271 | -43.71602 | 2026-10-10 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 94189afd-4b76-3bec-8444-a625107fe1e1 | -11.95467 | -43.48098 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9802fb8-85d7-3b58-b271-593a3bda4d96 | -14.46344 | -43.95734 | 2026-10-10 03:25:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1f48963-b6f8-3c93-ad2e-e614a31514fa | -15.39302 | -41.90444 | 2026-10-10 03:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d2763183-16c5-3da6-ae8a-e627006c62f9 | -11.94941 | -43.47256 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f543174a-f416-3d7f-80e9-8e4255e0db3a | -16.82588 | -41.03667 | 2026-10-10 03:25:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f9d42edb-1bd3-3338-b34a-7166c5a03408 | -11.9791 | -43.49832 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 70589d83-9bd3-3062-adb7-25209551d22e | -11.952 | -43.47263 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a2ec0b5-3857-313a-a93b-b0d88da68a0c | -12.04073 | -43.38332 | 2026-10-10 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4399d5e-a77a-33fd-86ef-a1bf1e379447 | -11.02049 | -44.06346 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8e175631-05ce-375e-a7d8-181b7c781120 | -11.0192 | -44.03384 | 2026-10-10 03:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README26.md)
