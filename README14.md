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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fa0b039-02c5-31db-8b68-0061594efd4c | -15.09815 | -48.73822 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d533f346-2684-371e-bb6a-93ce420879bc | -12.23588 | -43.14058 | 2026-08-16 03:55:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f3dbcfcc-bb2a-3f61-911b-0821aa4e448b | -15.04308 | -47.0186 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83c3eaaa-071d-39e7-ae06-25920aaa0fb5 | -14.47512 | -45.68632 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d69f592-509f-3de9-85bb-6ed22dd6e09a | -11.06907 | -47.27159 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32cec74e-4eb6-3de8-b9ac-ec3824140117 | -11.32244 | -46.22372 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c47d97-0ae0-3236-a972-3a5b533350aa | -15.09303 | -48.70826 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c86e057-c296-35de-86b8-dcc968c96f62 | -12.22884 | -43.13431 | 2026-08-16 03:55:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5e2b647-5fe5-322f-87a2-b8758c956e8b | -19.68724 | -45.40287 | 2026-08-16 03:57:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e2e2cb8-fd24-3dc8-ad40-5075028768bb | -19.68707 | -42.10774 | 2026-08-16 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 841ad3c7-2c9d-3c4a-8634-a3bcc61bccb2 | -18.30779 | -44.50222 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bac36a33-496e-3355-9779-f81b08801363 | -22.79327 | -51.40157 | 2026-08-16 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5c4e7825-a035-31b9-89b8-463fcea63bef | -18.3185 | -44.5098 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 32d809b7-5f56-36db-a392-dbae18417ab4 | -19.68298 | -42.11103 | 2026-08-16 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1f15e042-745e-3447-bee1-2f8bde0a08be | -21.43096 | -45.18291 | 2026-08-16 03:57:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7bf74226-8789-3895-a73a-cef022a33bb8 | -20.32762 | -46.7271 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fafde8ac-5c1e-3f35-a5f0-a0f7efbef46b | -22.77144 | -47.09573 | 2026-08-16 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8a79e9f-e2a4-3b06-b0c3-8ea77119c2a5 | -20.33195 | -46.72785 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f1adb7fb-e008-3f1a-9f2c-9c9a8495d843 | -20.87096 | -45.73432 | 2026-08-16 03:57:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 930bf045-3e6c-3d18-be15-0064ccbc1f00 | -18.30974 | -44.51348 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdd0d425-e1cf-341c-b47e-3172f9428eae | -18.85756 | -43.75618 | 2026-08-16 03:57:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a8b5f4d-c231-3ecb-bc72-76b089e4f04b | -17.71354 | -48.65635 | 2026-08-16 03:57:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdc0a4b8-344c-3c86-88bd-96d39a590130 | -22.86692 | -47.0984 | 2026-08-16 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8d3080d-42ae-36bf-9e2e-ce8d29f172b8 | -20.33709 | -46.7245 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| cf4410db-8d55-3de0-b110-7fc7c5280492 | -18.5933 | -43.77041 | 2026-08-16 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22722124-60e4-3b23-841a-7b5d91b8dd40 | -20.32677 | -46.73145 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf474fb9-b261-373e-8bef-708e5ae9e598 | -20.34986 | -46.70483 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 356306c5-e795-3ff7-bc16-7b3d17878f18 | -18.95329 | -47.32315 | 2026-08-16 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ef4643a-1222-3895-b14e-73c2764afac3 | -20.1538 | -44.787 | 2026-08-16 03:57:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c332b561-9eec-3bc6-9daf-3e3c93c6542a | -21.45172 | -48.6862 | 2026-08-16 03:57:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73902902-484d-361b-a793-93356b3af465 | -16.84507 | -49.43843 | 2026-08-16 03:57:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52698592-2c5c-3d07-ac3d-75489d914c47 | -22.21906 | -48.62725 | 2026-08-16 03:57:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90b6da07-9c92-3cfa-a4ae-2b78d6f53172 | -19.98887 | -44.21827 | 2026-08-16 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f06a5fc4-78d9-3785-ada6-259bf48077a4 | -21.82983 | -48.42016 | 2026-08-16 03:57:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a60e24-74a7-3c37-b0af-ae13287c340e | -22.06712 | -47.20678 | 2026-08-16 03:57:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2ccde17-66c6-3994-860f-b9192f7c7aee | -18.42144 | -48.57225 | 2026-08-16 03:57:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 467b51cf-cb8e-3f4b-94ed-c481805aadd2 | -22.21433 | -48.62647 | 2026-08-16 03:57:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5abcb5ac-9b22-355e-928d-290f8cdf7128 | -21.43483 | -45.18362 | 2026-08-16 03:57:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 80ef7476-566e-3e2c-9cc8-4d038180ba73 | -20.34477 | -46.70803 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45e554da-f8e7-37f0-b516-fe18d94bef96 | -18.30291 | -44.50672 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c920327-ce91-3ca6-b049-a2fa5095f2ef | -18.9195 | -48.21862 | 2026-08-16 03:57:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2eacfea-48b0-3383-af1c-f1e750979b60 | -19.68337 | -42.11167 | 2026-08-16 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c13bd2b2-5e7b-35ae-9710-bf99b2ca14f2 | -18.31754 | -44.51501 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5834aac8-594f-3be4-b1c1-e44178469218 | -20.34051 | -46.70691 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd7a004-a0a4-3a94-8df4-7138fccd6b7d | -22.79962 | -51.39904 | 2026-08-16 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a4fcb174-df62-3b89-b40e-f9b8075b464d | -21.4332 | -45.18685 | 2026-08-16 03:57:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 401d47e9-63c8-39b8-b7a6-f8504e244d6d | -18.62822 | -48.6005 | 2026-08-16 03:57:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35f6ac51-48a4-3e71-9079-3823173d9997 | -20.24681 | -46.74381 | 2026-08-16 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70350415-5024-303a-afb5-f447756e8cae | -19.68639 | -42.1117 | 2026-08-16 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8781fa5-8a01-38fc-92e4-85e762a6e1e2 | -22.22114 | -49.74598 | 2026-08-16 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4ab7e62-3294-35b9-88ed-b8b8c7c03d0b | -22.79416 | -51.39766 | 2026-08-16 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b08c2be9-a245-3803-bdbf-ae26c6697f95 | -22.22048 | -49.74907 | 2026-08-16 03:57:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9159f26-0ad0-3a71-8c0a-444f28e39ead | -23.04937 | -46.57476 | 2026-08-16 03:57:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 94c8f307-9333-35b9-b335-8a02d8a06b24 | -18.42643 | -48.5735 | 2026-08-16 03:57:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd2e331a-699d-36e2-96ad-4eab1019eb02 | -18.30681 | -44.50748 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ee9b3af-c1ef-3fbb-81ef-9c509cb73633 | -21.43412 | -45.18182 | 2026-08-16 03:57:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9c62339b-0d13-32f6-91a5-37771fc26e54 | -19.68404 | -42.1077 | 2026-08-16 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d7339ba-8c28-34f6-8010-923ee31f2e30 | -20.34648 | -46.6992 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60ceb5af-487d-39ed-acfe-7106b7d2a6bd | -21.53018 | -46.76355 | 2026-08-16 03:57:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 26f3cd41-f8e2-3470-9c03-a2fbca2b506f | -19.22848 | -46.79305 | 2026-08-16 03:57:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7fbbfed-06fc-323c-82a9-8952df5e9281 | -22.87112 | -47.09932 | 2026-08-16 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| add16615-4de6-3855-8818-3e4dde937f78 | -20.5079 | -50.12458 | 2026-08-16 03:57:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c56b8521-f8b4-3b3c-8741-a02397a54618 | -18.92435 | -48.21971 | 2026-08-16 03:57:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 247b8509-6ba3-3da5-82f5-2bf346ebc976 | -20.24771 | -46.7391 | 2026-08-16 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7bb31e3-073f-39ec-8627-6c83a217f93d | -20.52667 | -42.35709 | 2026-08-16 03:57:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1121cf52-6d25-313e-ade9-b0c10af0b76b | -20.33278 | -46.72358 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 89dbfc0c-29f3-32cb-a192-ee1489abbd40 | -20.3407 | -46.75205 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9fd8972-5456-35f9-b1cc-24a22cd3c6c0 | -20.05236 | -41.52376 | 2026-08-16 03:57:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 76b9c17d-06ca-3e50-8d4c-4f4d393c970c | -20.87176 | -47.01503 | 2026-08-16 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b1465e-cd80-3367-987f-a4a27207adbf | -21.531 | -46.7593 | 2026-08-16 03:57:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0971b450-dea4-3aff-a5d7-c6e040495ba5 | -18.85671 | -43.76086 | 2026-08-16 03:57:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad03f78c-5f8c-3d27-9756-ced01cc5bd98 | -17.66729 | -50.48855 | 2026-08-16 03:57:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1adf8f06-28ac-3ba0-bea7-2dc2850cfe57 | -20.33625 | -46.72881 | 2026-08-16 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 07600755-15da-373c-84ca-5b6954d82406 | -18.30389 | -44.50146 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3523b1fc-4f5b-39ff-ad63-2ca8ea2ebf88 | -17.1751 | -46.11548 | 2026-08-16 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30817e28-f43f-34af-908c-58c77bd21243 | -20.24857 | -46.7407 | 2026-08-16 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c739cc8-09c2-38b6-b71f-52892a450e80 | -18.31071 | -44.50825 | 2026-08-16 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53e95301-f2a1-346b-886f-9f21bf097bd7 | -17.61496 | -44.38387 | 2026-08-16 03:57:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83444bb1-acb6-3930-9447-945a92177376 | -18.6276 | -48.60346 | 2026-08-16 03:57:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2be19b86-984e-3b4d-82da-82d0f6d5dfbe | -22.79502 | -51.39392 | 2026-08-16 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f2f472c2-51be-32fc-b6f9-315c05ff9c1d | -18.59329 | -47.13266 | 2026-08-16 03:57:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdb7766c-563b-39c5-b4fb-16dc386511be | -16.66722 | -49.13917 | 2026-08-16 03:57:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c392bf-d99e-3817-9a6a-b482bb655a63 | -8.4275 | -62.676 | 2026-08-16 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 764f6ea7-fdd8-3d43-9547-97af58ad870c | -6.82 | -56.4551 | 2026-08-16 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9a266e66-c3fb-3b55-98c5-ce2ef0b826bb | -6.7123 | -58.9412 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 28b3732a-1fce-39b4-a13b-920b4a00aa60 | -8.9601 | -60.5165 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| acdc801c-ceb0-3128-b2b3-f23b79e722c8 | -6.1107 | -57.723 | 2026-08-16 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8ec79d81-380a-3c70-8e86-5e8f120b3aad | -6.6193 | -59.0802 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a2e4ac3a-45d7-31b3-ac00-65104ca31d0b | -8.9415 | -60.5174 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 379e1796-a293-3a62-a096-d123b6244499 | -6.2192 | -47.7419 | 2026-08-16 04:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d48f0732-df4e-37c5-a369-648766068f15 | -6.6378 | -59.0602 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ddc3fdc1-517c-3aa3-93d9-ede16d5e7a54 | -6.6377 | -59.0795 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6d1ad82c-dfe6-3a0c-8cc7-7756d37ba600 | -6.1108 | -57.7035 | 2026-08-16 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 69df7dee-55aa-3104-97d3-093575dadb1d | -8.9414 | -60.5367 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 24d7dbd4-e5f6-33be-bfd8-00389d881784 | -6.6194 | -59.0609 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 22bba25e-2472-3ad0-b7fc-00c49c3f200b | -6.8387 | -56.4344 | 2026-08-16 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 83e9aba2-e034-3f78-8944-ebcba9e3dacb | -8.9785 | -60.5349 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e120555e-a057-3fd0-880e-1016e85599c1 | -6.6938 | -58.942 | 2026-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7cf8aa7c-5909-342e-9c7a-53e5e16cbf91 | -8.9787 | -60.5156 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| d53ee194-35f9-3dd0-ae8b-1ef2329acd87 | -8.96 | -60.5358 | 2026-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |


[Clique aqui para ver as próximas entradas](README15.md)
