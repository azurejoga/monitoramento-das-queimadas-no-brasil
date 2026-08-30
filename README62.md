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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9952d9dd-5500-36d9-8a52-060506cc62e5 | -14.16257 | -52.81409 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55d62ced-f7ae-31f2-b9eb-86163fc117f0 | -15.10296 | -48.16574 | 2026-08-30 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60f479cc-8b2a-399f-aabf-9c27daf1326d | -14.28123 | -57.04148 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df28c3d0-325f-3c8b-9c8a-326f310bf1bc | -14.16747 | -52.81475 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94aacdb1-f7af-3fa3-8f0b-e755aedabd1f | -14.91314 | -52.63547 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c785a72b-8255-3738-87e0-ea5a2bad2d25 | -13.87093 | -54.12727 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92a4c4eb-fb00-35db-b97b-a1a60d110390 | -14.51782 | -59.83369 | 2026-08-30 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae945bd2-3c59-31f1-8ce8-60f31f085146 | -14.24239 | -54.65108 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bb195da3-2e80-309d-856c-0b19e7f60187 | -16.35467 | -50.98458 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56761429-263c-31cb-9ca0-09b9b72b0fc4 | -15.22805 | -57.65533 | 2026-08-30 05:21:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef782cc-93a5-3f09-b22c-a041efdd79b9 | -14.15837 | -52.80774 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3f6cb727-5d34-3772-ae56-029be9923ede | -14.41953 | -52.54702 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 57e37e6e-98d3-3b30-b6ea-4fc23b54b9fc | -14.24729 | -54.64734 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5bf1daa7-96d4-3972-9ab7-fedec84bbcf2 | -11.71536 | -54.5337 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29e421c7-442d-3ff8-85b2-f6f93e125df5 | -15.37324 | -52.66338 | 2026-08-30 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d9c37ea-bc5c-369a-87b7-be4cd252ad02 | -14.40806 | -52.55761 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5b9cbb8-f76b-3426-b5d3-5454251dab6b | -14.15347 | -52.80704 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfe983d4-cd41-39a3-826c-a6e46156f796 | -16.34381 | -50.97804 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 25ca2891-d5c6-355f-9a06-f7764518e2cc | -13.83751 | -54.10398 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a6a910e-f46c-32af-96d1-9318dc48180d | -14.24673 | -54.65163 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ad6962fa-5cbf-3392-8167-128fa8479940 | -14.23574 | -52.8476 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ec7975e-5628-33c8-be0e-17feb07e9a67 | -14.91348 | -52.6327 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9591c841-10db-3a48-9b4c-ef6c219638c1 | -11.71578 | -54.53322 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ce5273f-17f9-3a50-a0aa-52dc597b877c | -9.92375 | -67.87761 | 2026-08-30 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a858a637-c149-3322-9870-65046f616802 | -14.44619 | -58.47869 | 2026-08-30 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2aa769a-aabc-3232-8385-ce2d8bf140fc | -15.67887 | -56.28196 | 2026-08-30 05:21:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 264a2d67-5207-3dd0-8114-083bd66ec048 | -14.28132 | -53.19157 | 2026-08-30 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31d14e10-6f01-3408-9692-cca89aad55f3 | -14.03596 | -54.01485 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c63c07ee-9959-308a-b4a7-362b9f947b57 | -16.34901 | -50.98349 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56b75472-0fe8-367c-8bdb-e1622b7dc73f | -15.13643 | -50.63054 | 2026-08-30 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3ae5e645-4093-3f81-87b7-8133e37a22c1 | -14.1981 | -52.87129 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aeae405c-c29a-308d-9d45-7dc1c216fd49 | -14.44087 | -58.44144 | 2026-08-30 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ebd08d1-f354-305c-a466-ad464db0daba | -14.94043 | -56.33948 | 2026-08-30 05:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 649d440a-76ec-3cec-9413-94356fafac5b | -14.76242 | -48.73613 | 2026-08-30 05:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f649f9b-dc42-3ad0-a2b5-715e09b58afd | -14.03146 | -54.01414 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa72cf45-9e20-3c43-a536-3dad113dd340 | -14.43349 | -52.55756 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e3fbb1a-536d-39e2-bbaa-fefd79f260b1 | -13.85927 | -54.11174 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e1deb40-a231-3067-a753-11a0c143cdaa | -13.83714 | -54.03417 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 478ca2b1-6ebf-3c29-bf4b-93510a8607e0 | -15.22743 | -57.65973 | 2026-08-30 05:21:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fffcac74-2bfe-35d2-b9b3-5b9db85dbe68 | -16.34337 | -50.98229 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3bb01db9-b3c3-3424-ab8b-cd9b88ce273f | -14.20931 | -52.86057 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a629545a-0b56-3781-adc2-b3ee12fee585 | -15.12486 | -53.58191 | 2026-08-30 05:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8cd9f241-88d6-3c30-91e9-19bf96bf2d6a | -14.76759 | -48.7372 | 2026-08-30 05:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f6f9e914-912a-3c57-b27d-dbb186d64734 | -13.46296 | -57.04184 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7b7bc60-157c-3b4a-a705-3070253cc7ab | -14.51448 | -59.83314 | 2026-08-30 05:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79000fc6-38aa-3d9b-9148-2cc72cb1c3d3 | -14.42694 | -56.26334 | 2026-08-30 05:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 670a61c1-b625-377b-a712-174a909ddcff | -16.3634 | -51.01109 | 2026-08-30 05:21:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85c1181a-5850-318d-896d-4d0a73a0d073 | -13.45864 | -57.04573 | 2026-08-30 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5760e25d-dee7-32dd-aa0e-30147e108497 | -14.25163 | -54.64789 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6dcb1863-cd9a-3ae8-8ca4-36c4b3c7b360 | -22.01695 | -56.03265 | 2026-08-30 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eecf578c-b44b-30e7-8b26-e941f092579b | -20.11461 | -48.27026 | 2026-08-30 05:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c60a77c-9386-399e-a64f-08fd27de4c3d | -19.08426 | -57.40057 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8ff76331-4c86-34ec-bd3e-6144cd4c47bb | -19.47782 | -57.5689 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2eda3653-2bd5-326d-8620-5322b1166b55 | -21.01344 | -57.83626 | 2026-08-30 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b1bcbee-fded-3030-8e03-d0af75ec7758 | -22.01254 | -56.03212 | 2026-08-30 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01a978b1-23a0-3016-a06e-b023182db48a | -19.47849 | -57.56382 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 243fbe59-d08c-31e4-8ba4-cad02bf0644e | -19.08105 | -57.39487 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ad679be4-18e3-3ac5-9cdc-8bd9b54f4432 | -21.0264 | -57.82763 | 2026-08-30 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f8a96264-8841-3b5c-8322-21ddd615af8a | -19.08941 | -57.39738 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0467a3e4-7f4a-3b5a-9538-1267e4fbadbf | -19.07716 | -57.39431 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7b20909f-2f22-394d-a3dc-2b86665d98cc | -20.11498 | -48.27647 | 2026-08-30 05:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5939d274-f4d7-3020-b2dc-9de55adb9d9c | -23.81733 | -54.73269 | 2026-08-30 05:23:00 | NOAA-21 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1a7a5b6b-7c57-3e88-b9bb-48f3453f2916 | -20.11414 | -48.27681 | 2026-08-30 05:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 719ee4cd-e85a-39e2-a5b9-fbba2cdae87c | -19.08814 | -57.40114 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9b012e1d-3a26-3a33-bfe3-df0311056b02 | -20.11549 | -48.2699 | 2026-08-30 05:23:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 398f999e-4ff0-3392-ab91-14b7bed519cf | -19.47462 | -57.56324 | 2026-08-30 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2c0d6e5c-616d-328f-a928-5f5027139a96 | -11.8211 | -51.0322 | 2026-08-30 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9aaa0c44-9f48-3083-a5f6-1c5b7c75bbc7 | -11.8018 | -51.0556 | 2026-08-30 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| feddd75a-c288-30db-90e1-195b5da10a11 | -4.9603 | -55.8622 | 2026-08-30 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 5a93dd68-9a63-31aa-99dd-3c8ae67bcb71 | -11.1631 | -50.594 | 2026-08-30 05:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 69901e3b-bce9-34d0-8dca-d9b4113d31c9 | -11.7831 | -51.0365 | 2026-08-30 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a72d52f1-f68c-3bf8-a3e2-d559e7da1627 | -4.9604 | -55.8424 | 2026-08-30 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 55f1d437-cf0e-3908-a51d-51863b925384 | -11.8021 | -51.0343 | 2026-08-30 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 9e783ae0-d6d1-39d7-ab68-2da89e36441e | -5.4876 | -57.1416 | 2026-08-30 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 603fc9d1-4038-3edd-99ae-42daefb5303d | -9.8927 | -60.2752 | 2026-08-30 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 376c5fd6-e711-3882-b40f-3af877a7103b | -9.8927 | -60.2752 | 2026-08-30 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d55ca59e-262b-308d-8b3d-455f54e081ab | -11.1631 | -50.594 | 2026-08-30 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| cc2e3d76-2eba-32e0-a9bd-bc4c02470243 | -11.8021 | -51.0343 | 2026-08-30 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 4fc47689-70f3-3ef3-9d57-8db9b18bff0e | -11.7831 | -51.0365 | 2026-08-30 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| cc6cdf82-82b7-330f-bf7b-fb9e5166572b | -4.9603 | -55.8622 | 2026-08-30 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| a7a0750d-474b-3a16-b6d6-5053500342af | -11.8211 | -51.0322 | 2026-08-30 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ad015446-468d-36eb-9fca-78c2a1c491a2 | -11.8018 | -51.0556 | 2026-08-30 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7fe699c3-dffd-3a1f-8dc0-425061eb3a83 | -4.9604 | -55.8424 | 2026-08-30 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 66d45dfe-f2a5-3761-a281-2bd0081a3cb0 | -5.4876 | -57.1416 | 2026-08-30 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 243d99f7-83bb-3555-8393-213cbf28a405 | -11.8018 | -51.0556 | 2026-08-30 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6011085c-7222-3a30-b845-0c448e48786d | -4.9603 | -55.8622 | 2026-08-30 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ffa43115-e22d-33b1-9b0f-8649a738a0b3 | -11.8021 | -51.0343 | 2026-08-30 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 87d0f301-7456-3a5b-8aa5-4b144dd27830 | -4.9604 | -55.8424 | 2026-08-30 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b5bcfa42-be58-3fdb-ba14-93b6fe02e5df | -9.8927 | -60.2752 | 2026-08-30 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 94de6912-139a-3d49-859e-eabae4c90d66 | -8.61157 | -54.77411 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c169ef9-66d7-3d8f-8513-b80c1894d7a2 | -1.24786 | -55.70361 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6763a72-de2a-3e86-809c-db5090cef198 | -6.78282 | -55.68229 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf6d555d-4e50-3226-927b-90096a38eea1 | -7.00414 | -59.65146 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4a3f85-8344-3f23-a7d8-34312100e7a0 | -6.85944 | -59.47147 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d13c34e0-17fb-30d4-98da-98294db531fd | -9.89514 | -60.279 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2c1ac039-1582-3a4e-9e1f-1f32b2fc9e70 | -3.23734 | -61.24931 | 2026-08-30 05:53:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d14bd39-a362-337e-9661-3c207139821e | -8.47311 | -63.928 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87cd8a01-8d06-3ca0-9803-38a572b370b8 | -6.93965 | -58.95332 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 418f5a31-4d3d-3cc7-8e2d-a3400a34c77f | -9.71239 | -60.72451 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b65bd801-7e15-37be-926a-22201e94ce16 | -7.55512 | -61.31672 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README63.md)
