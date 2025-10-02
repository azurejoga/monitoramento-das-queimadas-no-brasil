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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f3e48d8-ecc1-347b-b354-b9685ac02fa0 | -15.28033 | -49.30431 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6adbfea9-e99b-3449-b3ea-7d8c44c2c4e2 | -12.90147 | -47.17117 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78b8c7c7-ab95-323e-8b40-8a099cad2782 | -15.28407 | -56.779 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83fe7a55-d1cc-3f59-9522-f4ade695588c | -10.84011 | -45.3801 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1b62ec1-77b9-3a76-937a-c4c316073c71 | -12.67684 | -46.86255 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9909e99b-99e3-3016-8b60-0d4b83662f65 | -13.39705 | -47.77966 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 99d65423-6069-348b-ad95-83cc1fedc15a | -12.89856 | -46.91548 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ded8f0db-3dc8-306b-a6a1-fb8d021da830 | -13.32173 | -47.20753 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8c2f324-8ca8-37e7-9450-e3b76de7735f | -14.68245 | -49.61555 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d391c49c-0f05-3bfe-85f7-6022fd64c9c4 | -12.45754 | -54.31845 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02d30627-94d2-38fa-861e-a60c6b6983f5 | -11.17181 | -47.26711 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a197d46c-18db-3e16-aa0a-eb3962f4c34b | -14.36648 | -45.96727 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a006978-e745-3b66-b3eb-e1da3f2761e6 | -13.46394 | -47.23208 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2d5379a-94a3-3f84-9f74-d035891476e0 | -9.94737 | -43.69965 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abdaf25f-cacf-35ac-9dc8-3ed9cef11d27 | -13.94783 | -48.09431 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c6b15e9-b46c-38a7-88ec-90cf74f6d93b | -12.65654 | -46.87447 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 133468fe-62c2-3c71-8d5d-ea61cf24fbed | -9.92507 | -43.74354 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| eb4185ec-4ed5-3a1e-a08b-50b76e0e23e1 | -11.59829 | -47.22526 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9a19687-4827-334b-90a2-0b0956d07b89 | -16.09421 | -51.05121 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a10b2969-fe2c-3056-b38a-1669b415a635 | -13.45689 | -47.25097 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18b8780a-8721-3aa4-bcc2-a15b19f4e523 | -14.88687 | -48.12822 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99024f1f-f577-3898-bfa3-fa559ba3ccbc | -11.7794 | -46.83847 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 189a57f3-69d3-3f85-a597-1f1144163c6a | -12.11395 | -43.43287 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 297acb92-3fe9-30a4-b741-3965374f6249 | -12.703 | -48.57539 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82fdd919-1806-3b45-a8e8-2e33af7959ee | -11.16902 | -47.28806 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a7ac05b-8dde-33bc-bfd5-7f806cc033dc | -13.23377 | -48.51271 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3711791e-72c2-3e5f-8875-d73b54811329 | -15.03379 | -48.06451 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a3b1cb0-972d-36d7-8691-869410cd67e2 | -9.94602 | -43.71027 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997518c9-6286-3827-aa7e-fbbc81936c0a | -14.41346 | -46.12016 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d8902ac-b21d-3cd4-a093-b30508f3b090 | -15.27846 | -56.77018 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbd1aa13-2b01-3633-82f3-711c2212c8bf | -14.32188 | -45.8772 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31074578-8dc2-3846-9838-b0968d18e70f | -10.2272 | -50.32189 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4ddb1339-2c78-30d9-a2b9-c4fe6cc78bbe | -13.16111 | -47.83783 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87219707-70fd-3079-8c72-43b0e3a45b76 | -13.30264 | -47.847 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f06256d-c5a1-3991-a1de-08ad3cdcbef8 | -13.37255 | -47.28558 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c34e3e64-2963-31ce-8c10-d764b330a4e3 | -11.44021 | -44.96397 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71363a85-c9fe-316d-921b-dcd0a3ccfb7b | -10.84429 | -48.00513 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e18b0f39-7cb6-3a2e-afee-9ccc1c603915 | -12.81884 | -47.02641 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 914bc0bf-fa4d-3d57-90f7-337f33bfc73f | -14.49041 | -48.42353 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76fa6925-7986-30e0-b921-9a81199ccebf | -13.85972 | -51.24381 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eca62b7d-6637-348d-a48d-a6dc559b34eb | -11.26681 | -47.81157 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc348471-470d-31aa-bb45-c63a1dab3517 | -13.15818 | -47.82647 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12a4cb1c-3dd0-37b4-aab6-a9cc9278f956 | -9.92482 | -43.74018 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 06e168cf-57ba-3851-906c-bfab02f212c9 | -13.42589 | -47.79689 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 961992d6-53f4-3f61-b75a-ed03fbf483a5 | -13.45632 | -47.25539 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a62d15e-eff2-3e4b-8fce-9eba68c2c5d1 | -11.82036 | -45.0056 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9ce4901-34ef-3952-b7d4-82d568387b03 | -14.92302 | -47.22898 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3b62adc-352f-30d7-aa73-c0a95ec4de4a | -13.78933 | -47.99842 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f95459d2-f888-3e75-bd7d-86d734a539b5 | -11.42927 | -47.28434 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ce0efa-5fb9-3c76-91b1-6ee0b7901ea0 | -11.52878 | -43.54696 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 085be252-e6d0-30c0-ae90-11eb98fdb73e | -13.80372 | -47.53772 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0007e3e-6810-3632-ac06-54a01f5ad342 | -11.10469 | -51.07671 | 2025-10-02 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbfef24c-6904-3b55-b8f2-032eddeb9ad3 | -12.42954 | -50.16367 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77eb5d85-8bf9-3a1d-9ade-108dbaa7be9e | -14.97999 | -46.9176 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 824abbf1-3eff-31ab-bec9-9624879c2c88 | -13.9516 | -48.1333 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ca00771e-4667-30a6-818c-bdf8d270fbd1 | -14.88204 | -48.33081 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ba47369-66ad-3c02-bc94-bd03cf352d54 | -13.16916 | -47.81027 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 492b687f-35cd-33a5-83a1-54250750afc2 | -10.4304 | -47.47295 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63ccd8b0-258f-3fad-9245-71bcc33bdeca | -14.22181 | -46.10337 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db1f7c84-c1ad-3a5e-be10-8fac4b63059a | -15.50292 | -45.90835 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d417de3-2ecc-3c1a-bf68-b1fe97df97e9 | -14.88675 | -48.31166 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da2b03e8-a052-3437-9a7e-95fe2b6d169a | -13.5328 | -47.27895 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f09c251b-b12c-33f2-bec1-501e8b0b19f2 | -11.17069 | -47.27549 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 136cd78a-abd8-37f8-9e05-a9a0bddb6ab4 | -13.15878 | -47.82189 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b44a688-8f0e-367a-973e-06fcc9d2acb6 | -12.68417 | -48.56037 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3cf2434b-1094-3f40-ad9c-6d06f95aad18 | -15.14287 | -48.01947 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d35f520e-3038-38dc-a749-e6b73c951c4b | -11.58048 | -47.02966 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e974ec2-791d-3776-8daa-567a70d214dc | -15.94624 | -43.30786 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99de9067-2836-31b1-84eb-c5200f654c69 | -13.07194 | -47.01642 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75e87a5a-9e16-3b02-b0f4-4eaed7ba35d3 | -13.07132 | -47.02123 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ced4927-40e9-32a0-b99d-35084b517ea5 | -15.24373 | -46.9831 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc69d03-3572-383d-9891-17b4b13c30a4 | -9.93056 | -43.74421 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| fd1a38b4-ad45-339a-8d6f-737d813a49b6 | -11.61797 | -45.04034 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b899850-4559-3afc-b0c6-d251c6fe70b4 | -13.76697 | -48.00088 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a83d0b6e-2217-3938-9d6e-3daa9f9526ea | -14.68321 | -49.61001 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10f34925-6e92-359e-9f21-6d28eaed64d6 | -11.49627 | -43.50726 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2215f433-6b59-3fe2-b392-7397399ac607 | -10.53788 | -54.86855 | 2025-10-02 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b39c2c00-c052-302c-97a0-566b306291e1 | -14.43718 | -46.34761 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0794fb67-1c96-37ea-9c5c-b5fbcaf68f55 | -9.93547 | -43.70541 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566231a0-7723-323c-bb0c-53d8baecd29a | -10.86998 | -47.81543 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| def72e8a-f463-3c23-ad2c-c0bba82ecc28 | -15.14835 | -52.80138 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d6c16f-ff25-33b4-803f-2aad9d71a4c1 | -10.82798 | -46.61874 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c3677d8-b3b2-3f8b-afe1-c463dae2fa7b | -11.46681 | -45.00053 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60338444-2ff3-3984-9043-6ee2ca1f8ea0 | -9.44911 | -50.90449 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55c83537-c069-3539-89d0-bae57c690176 | -14.87702 | -48.13573 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8703ae0e-ceae-35fa-b274-3a366b4d7cba | -10.10881 | -45.67251 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc77dff1-3941-3ff1-b572-fe9c308613a0 | -10.21291 | -48.19653 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37ed104e-e16b-398e-a461-6a7d97cf39fb | -13.21657 | -48.51472 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f874b339-d24a-3b04-8fad-e5b93a672dbd | -12.10873 | -43.42764 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bca4fa0-add4-3ae2-96e2-8142787f7011 | -15.25948 | -49.3056 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 597862cf-960d-331b-b6dc-ee56e352eda8 | -14.87324 | -48.13066 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 862e33ed-8427-3b2c-8e12-cbc9edfae343 | -12.47435 | -47.27025 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3ece7bae-5823-351a-80bf-75b402985302 | -15.2585 | -49.31288 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f9a8967-f949-306f-a237-1b71c11f0210 | -10.65002 | -48.50564 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f39f4c8-c85d-3d66-a7f8-ec015d20970e | -11.86234 | -48.08634 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c1e46d5-bc24-3dcb-ad9f-571c857778cb | -15.23736 | -48.73059 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c24a1bce-62cb-32e2-b117-70b2b10cce98 | -11.82246 | -45.03053 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c81c2d53-f4cb-3fe2-bda8-7af48f87c1ea | -13.32101 | -47.21284 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6878e504-6d4a-385d-851d-61053f77ec0c | -14.4798 | -48.43842 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 993e2a8e-1ac3-3d8b-9d27-8d09f9c385fb | -11.34743 | -44.97469 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README131.md)
