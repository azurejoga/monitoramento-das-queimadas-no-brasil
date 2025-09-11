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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0241496-fa51-3f79-b84a-e16c90ed129d | -15.60263 | -52.74011 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58869162-4308-39a8-9dbc-90c2f6f22f74 | -22.21899 | -43.43412 | 2025-09-11 04:25:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b1aae49-141b-3289-aad7-912bd11339df | -19.75179 | -47.18517 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faa13ea5-02f5-3ddb-923b-3394daae3dc5 | -17.50035 | -43.75619 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c82a546-1702-3525-ab26-4a279133b00c | -20.01964 | -47.7681 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc62a29f-c243-3196-b2a7-8cf28e77782c | -15.79927 | -52.24178 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75150feb-4e93-3035-8221-da1ff45ad37b | -17.57813 | -50.16173 | 2025-09-11 04:25:00 | NPP-375D | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f776c5a2-f6d6-3fc1-aaa7-2af4aa751f3f | -15.11697 | -52.40757 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5dadb55-a3b0-365c-ae35-952c7cf3dc96 | -15.09863 | -50.0631 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89de6850-7168-341b-9b13-0ba9b2f01ef5 | -20.13039 | -47.68471 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83ee5f16-ed2f-301b-887c-6447736c347c | -16.26217 | -46.78589 | 2025-09-11 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad9c6c92-3c37-3160-af8b-58451f767534 | -20.3978 | -46.27849 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f935a2f-feec-3cdd-b75d-8c2edd40b6e8 | -20.00986 | -47.63406 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a9bafb4-d292-3eec-969c-5496c5f21482 | -14.42896 | -52.94172 | 2025-09-11 04:25:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fc7d15f-725f-344e-86c1-0999db842bc2 | -19.41975 | -43.13078 | 2025-09-11 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe272e59-715e-3f1b-8cf0-56dcf4653377 | -21.29661 | -45.95722 | 2025-09-11 04:25:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8186ba8-7f28-37fe-a514-5a50a7135a15 | -16.88425 | -45.76133 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 204ec260-6582-36ea-84ac-7265312bdebb | -17.68676 | -44.19729 | 2025-09-11 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff33b03b-8a0f-336b-b7de-202d2ee7266a | -17.94016 | -44.48228 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25afd9e5-1f13-34c8-9398-14b955d45a0a | -17.37549 | -52.93192 | 2025-09-11 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7692ff1-3ec9-3d43-bbdd-5478b9585f62 | -15.56545 | -54.75413 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 723487b4-e07e-3189-8c96-c30a263b69c8 | -18.82414 | -46.87143 | 2025-09-11 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60bf74ce-2a82-3327-b1cf-f4b86775479e | -17.97043 | -44.47426 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4b2c60c-8fe5-3e40-9931-312c2091e3e1 | -20.1658 | -44.61921 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98e237a2-bfd0-30bb-a2d9-5a9d15363bca | -17.32955 | -46.68033 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1b4a69f-41ed-3002-bcf2-8b2a6aa68d3e | -17.49979 | -43.75379 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff70bf5c-1ca3-3866-a583-14bcb82aead5 | -15.1037 | -50.13575 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47e58542-6c62-30be-8d3d-3651a98895de | -20.36268 | -42.19593 | 2025-09-11 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 09d37117-41dc-36a0-8c9e-c70150520ebc | -17.68253 | -44.20123 | 2025-09-11 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80b708fc-4b6a-361a-b0d7-57ab0fb15269 | -21.22937 | -43.83659 | 2025-09-11 04:25:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 230fb779-7956-3576-a0a7-75d983978b9c | -17.8493 | -46.74742 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c5e010e-fd08-37ed-8f28-d1b8effbb12c | -16.58566 | -50.0886 | 2025-09-11 04:25:00 | NPP-375D | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe140674-7a14-3281-b34c-c5b9fc5b7ea8 | -20.90646 | -45.28949 | 2025-09-11 04:25:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 33c839a2-7ead-3198-b74b-96d4e519777e | -22.32014 | -50.86671 | 2025-09-11 04:25:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79b70090-8c07-367b-9621-316a2a4feec1 | -16.08493 | -49.71724 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18dfcc66-f385-3f7e-91ee-d650bf499aa7 | -20.39167 | -45.79844 | 2025-09-11 04:25:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7733fda6-44ca-30a7-a773-d3fd03c8c160 | -15.12883 | -52.41365 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a8663b6-f88f-3092-bbdd-faa48e4dfcd4 | -19.55171 | -46.9467 | 2025-09-11 04:25:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16f688f8-2180-3bb0-a9c5-29014432c43a | -22.79411 | -47.80889 | 2025-09-11 04:25:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 398cd6e9-476c-3094-a11e-d152577a1d25 | -16.63307 | -49.76876 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2a85c48-393f-34f5-9162-45acce51138f | -20.4874 | -54.91806 | 2025-09-11 04:25:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4300bca-b7f5-3229-9382-1698ec4220e7 | -17.25302 | -46.08605 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6aae47c9-c09e-3d48-a464-769d6cde37a7 | -15.14308 | -52.40687 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b6621e-6267-397e-8803-5969ecb40c56 | -14.51555 | -53.92808 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9a05922-594d-3c3a-9f44-76fe38069ee6 | -19.95835 | -46.88157 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dee0b13-3468-3566-ab26-d3f09c6c0b15 | -20.54243 | -47.61874 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb1fa058-9001-31fe-8797-3908200853f4 | -15.55469 | -54.74449 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d09d009-38a5-3c83-b526-d03a727d4da5 | -15.81856 | -52.22918 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6e9f5a9-40c5-3580-bf61-301426e63e4d | -17.93512 | -44.47906 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62068e54-14e8-30d7-a307-8f16d075f563 | -19.66175 | -45.65446 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f20c6ca9-3802-3576-ae7e-e7da52c992f5 | -17.82856 | -44.2658 | 2025-09-11 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26f6fc87-000b-3abf-b6ca-7d6dc2bde78a | -15.11992 | -50.12946 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c583972a-d7df-3aab-8645-9eb769125fc3 | -20.1414 | -47.7018 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c017059a-65fe-3e2e-b388-c25fe5676896 | -20.0927 | -44.4767 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 664a9f29-2fd6-3795-8b3b-f1772ae478df | -17.25034 | -46.75691 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59c45a3a-e3b3-313d-a186-70745d9a2341 | -16.17559 | -48.68509 | 2025-09-11 04:25:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e21e3fd-9d9c-3b5a-b6ec-c02d6f414d89 | -19.46145 | -40.88214 | 2025-09-11 04:25:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4fb5dbc7-ea8e-310b-bdeb-d63a8a74b2eb | -22.52219 | -49.08621 | 2025-09-11 04:25:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc421cbf-5c35-37e3-a281-98eb8c772143 | -15.98082 | -42.98367 | 2025-09-11 04:25:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 50806cf8-9da0-317a-9026-c164094fc114 | -15.14379 | -52.40308 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e70f5581-0be6-31d2-9dc7-d902420d42e5 | -21.43222 | -48.91573 | 2025-09-11 04:25:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3769e6b2-33ef-3ca0-8ca7-4574df1b3609 | -20.23881 | -43.58078 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d0830b60-8edc-3265-ab97-8c51753c5fc1 | -20.89267 | -47.01623 | 2025-09-11 04:25:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af3fb827-a2a7-34a8-a26f-3d4854b695cd | -14.30574 | -54.76086 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9ac35ac-61d6-3ee6-9d36-87f98a5c02b0 | -20.33404 | -46.61464 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1baa748e-03b2-3f88-9e3f-e9da0c41dbc9 | -21.84132 | -48.08713 | 2025-09-11 04:25:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6741343f-7d74-3561-824f-e5bd9e38dd34 | -18.56059 | -46.5634 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3ce5560-148f-3a4b-af4d-f9b234b8ebf9 | -15.82339 | -52.22597 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a76d5a5f-11f6-39b4-94c0-13ec1b5c4cdf | -19.23401 | -48.00937 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c9cf69b9-3290-3bb0-b7dc-c818d384e6de | -21.91318 | -47.91199 | 2025-09-11 04:25:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa1c652e-7c56-309b-bfb8-b07ab634efe8 | -20.57595 | -47.68921 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88858f72-68c7-372b-aec5-6a145270726e | -16.05032 | -49.98325 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15b5b742-8b65-31d0-b279-d2be26b8c3c8 | -15.14796 | -52.40389 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f52202f-796f-32f0-b603-b84dd30ca4b1 | -14.91439 | -55.87174 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 509dc5a5-207a-30b1-8fd6-10abbbfc94fd | -20.00711 | -47.62981 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 656dde74-e515-3f56-8d7d-4c909ef0350b | -15.13895 | -52.45243 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01634c2e-1c25-3b92-9b9b-4c79be12944f | -14.89321 | -55.87664 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c316316-210b-3eac-b9b6-409265e3613b | -16.63155 | -49.75629 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f713aac8-b771-372c-8a4b-2fb2d2b9e29f | -14.72741 | -55.61854 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06de13b3-61ff-3e2f-aa2c-01014b030433 | -19.90795 | -44.23848 | 2025-09-11 04:25:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47f04e84-b003-3c4f-b6b4-5cbc9197fca2 | -15.14735 | -52.45397 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b6eeec4-a19a-3118-9c1d-135a586b3277 | -21.29355 | -47.08653 | 2025-09-11 04:25:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fa6127d-4bda-317b-92b6-5b0c1d83d648 | -22.83955 | -47.46498 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e6ef4b5a-4b50-3117-bba9-44e27ac35491 | -19.723 | -43.91286 | 2025-09-11 04:25:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ac09404-6515-3e75-891c-a92aceb62809 | -16.37218 | -49.41009 | 2025-09-11 04:25:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b2131e7-b5b0-36ee-822f-3a1eb48c07c1 | -21.35358 | -44.22641 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdf6e419-33d1-3425-9672-06ea2fe27dcb | -22.69117 | -47.31476 | 2025-09-11 04:25:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94d6cc9c-d5c4-3281-8eb7-d9a98e3a1436 | -19.95898 | -46.88459 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59f6c77c-167c-37f1-80eb-273ce43aa1b3 | -15.79883 | -52.23113 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11fac11-276b-3f27-8119-dc97a368d426 | -17.84319 | -46.74265 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90f143a7-f92c-301f-929c-28784ed7f308 | -18.34561 | -44.36656 | 2025-09-11 04:25:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aea6777b-1445-3ba7-a481-3c1e6661a891 | -17.82649 | -46.73985 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e016aaf0-7d43-302a-aab5-6ae62237ddba | -15.80576 | -52.27519 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f2c5a0e-6085-39f5-be23-b122217017ae | -16.64843 | -47.73658 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db8552f6-e70d-3e7b-8f88-8dec556fdfaf | -20.05386 | -44.84064 | 2025-09-11 04:25:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b9205eb-a6a5-3e8f-8400-b8db71c84483 | -15.79479 | -52.25361 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2182e638-dc8a-38f6-920c-d80a3becfcfe | -15.08037 | -50.05981 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5e8ef73-d00e-3a1c-a07a-b4b154b4570c | -14.44206 | -52.94447 | 2025-09-11 04:25:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f6020ce-84f4-3da4-bf9b-607449413e98 | -18.56001 | -46.56712 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb57c0b5-a405-3190-b4e5-1920b5e6b7a7 | -20.53909 | -47.61814 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README77.md)
