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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b87fe743-9083-3016-8bea-d98255469ec4 | -19.97265 | -42.43814 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 6a946cd5-a562-3e1e-a005-e521e0bcc86e | -19.97204 | -42.44265 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| ee78b4ba-8dfd-3094-8ea7-86c4c11fc404 | -19.89335 | -42.63683 | 2024-10-09 04:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d81dae46-ed2a-393d-94d4-b386606e8f01 | -19.83373 | -42.38671 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5684f87e-ac10-39f6-8670-133ab5869849 | -20.68204 | -42.33224 | 2024-10-09 04:17:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1169b9ec-5fe0-344b-8e39-8cf390603719 | -20.37758 | -42.21175 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b5c80174-e508-3ca1-b328-42f9504a2e6a | -20.00972 | -42.44357 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5f55cef0-2e7e-3c82-82bd-6b1c775459fe | -20.00909 | -42.44813 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 57912413-1e84-32d6-933d-509f5f41f18b | -20.00661 | -42.43863 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5515cd8b-11ab-3b04-8db2-50110b9e46a0 | -19.9992 | -42.43752 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e43890ba-b590-3598-a9e1-13ea170620c1 | -19.99467 | -42.18856 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 25871268-d8c3-3b6d-842f-e2a4ef051e5d | -19.83 | -42.38625 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3e74fa48-cd5e-3ea1-9821-8c3515851517 | -19.7689 | -42.84183 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ae65a5ef-38b1-3692-81fc-542bb7b34b41 | -20.58559 | -43.28103 | 2024-10-09 04:17:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 379d5a00-da2a-351f-b678-f87009d10aaa | -20.11777 | -43.48079 | 2024-10-09 04:17:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 81c61a37-5513-336b-984f-cf8f0a0e80ea | -20.11425 | -43.48015 | 2024-10-09 04:17:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 83bb2774-27d0-3670-9031-9b889b8e88eb | -22.23081 | -43.41372 | 2024-10-09 04:17:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 014a6c4a-f885-3499-a871-94e5535956ad | -21.53121 | -43.82837 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c7ae241-544d-3c33-8892-c307c55fa103 | -20.9648 | -43.54023 | 2024-10-09 04:17:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 47c3473e-06bc-3387-8d6d-fd5e04fe689b | -20.99148 | -43.06394 | 2024-10-09 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 76b969d6-88c3-303c-885d-32995fb573e9 | -22.22236 | -43.05865 | 2024-10-09 04:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7f4689e0-ff84-36c6-9eac-1cfb29342e61 | -20.99511 | -43.06448 | 2024-10-09 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4128cb87-c7c6-3088-9dc6-e3bc3133681f | -20.9927 | -43.05509 | 2024-10-09 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 327f619e-0b01-33cf-8140-ae933488a221 | -20.99209 | -43.0595 | 2024-10-09 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 66b2a8ab-58b9-3bd9-8ced-275113f022ed | -22.90876 | -43.30916 | 2024-10-09 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| adc53007-0c01-3d67-9adc-6221ad6faa53 | -22.78571 | -43.75566 | 2024-10-09 04:17:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e929f75-5211-3fcd-945f-dcd53aa3dce9 | -9.89505 | -42.57682 | 2024-10-09 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1281357-e598-3b10-89b2-c9ef6130af1e | -11.56452 | -42.18476 | 2024-10-09 04:17:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c690337-648c-30fe-9833-ed1811e75a47 | -11.23975 | -41.59435 | 2024-10-09 04:17:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 39d7dd8a-92fc-3ce8-bdc2-4d3311bd373d | -13.54388 | -43.54026 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b58237-f4fe-3b3c-ba86-b7ebae7de36f | -13.78399 | -42.43047 | 2024-10-09 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e9156de-2764-3870-a0d1-f97595cf48d4 | -13.71408 | -42.50375 | 2024-10-09 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be2715ef-1880-3d9c-8ddc-c6efed2f3181 | -12.41351 | -42.34277 | 2024-10-09 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| aa001ff2-5534-374d-b0a6-81a53d3a403d | -12.37327 | -42.51793 | 2024-10-09 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fa77c60-7c0e-3102-937d-e9c22396dc65 | -12.36986 | -42.5174 | 2024-10-09 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3aeaa940-a9b0-3534-95f3-899d148d0d1c | -13.53538 | -43.18692 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92bcbf04-3808-3ee3-8d10-03be65714e18 | -13.43717 | -43.20965 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7c059b94-aae8-34e0-98ea-fc7edb757943 | -13.4338 | -43.20911 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21dbc3cf-2daf-38d4-86d0-fa3499d17fc1 | -12.97654 | -43.17589 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0453d1b7-90eb-3a93-a8f2-6cbe4eff7d99 | -13.80954 | -43.60051 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9bc6a30-33ed-3575-aeb1-d507d7139b59 | -13.80899 | -43.60414 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 430e9ecd-0703-3dc3-b6b2-2a8464480a14 | -13.80619 | -43.59998 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640f9edc-83a0-3cb9-91b2-4b6fccd27393 | -14.51189 | -42.2966 | 2024-10-09 04:17:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa548746-55e5-3cb4-8727-81d79f405fe7 | -13.81233 | -43.60468 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 522b6d64-01c9-3ca8-a935-c353ee161ebc | -13.80564 | -43.60361 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a99fad-5d9b-3613-85ec-a5a43dae916f | -14.03513 | -43.569 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60d4880-5154-3cff-abd1-db65bd2882b9 | -16.49072 | -43.81295 | 2024-10-09 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5101fa81-3e21-38bc-9c0e-49cda49250a1 | -16.48734 | -43.81239 | 2024-10-09 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eafa7f5-c17e-3d78-8288-677c274e3a5a | -16.48677 | -43.81632 | 2024-10-09 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f8b46ab-32c2-31f2-b3e4-74f3533e793c | -16.3499 | -43.69523 | 2024-10-09 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aee3f31d-8364-3301-89c1-79c9a8ac3575 | -16.21535 | -42.8709 | 2024-10-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa013fc5-ad2f-3dae-8013-3de1065dd299 | -16.21478 | -42.87488 | 2024-10-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f029ba9-4c7f-3a50-b599-3767a9bffb52 | -16.2142 | -42.87885 | 2024-10-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c3a0d10f-ba75-32c8-ad64-9a53726b43ba | -16.2113 | -42.87429 | 2024-10-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52d102c0-4874-330a-871c-5f9a3c5f8842 | -16.14825 | -43.66006 | 2024-10-09 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52b09dc9-de99-3708-a6bb-74c7c054967b | -16.04692 | -42.85514 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4fd22d00-3def-3c1f-8882-1120aeb5df6a | -16.03996 | -42.85404 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 765e008a-e7c6-3bb8-9db8-8ca92f48c6c6 | -20.10736 | -44.22092 | 2024-10-09 04:17:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 258e03d4-f336-3171-b89e-4c46ec0e79ac | -16.03707 | -42.84946 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d1b248e-4d3d-357b-94a0-46e487635606 | -16.03359 | -42.84893 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c4c8cc2-4c22-393e-8271-9b74b0526ff8 | -15.89747 | -43.03792 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 69d1fce3-3e0d-37a3-ba94-85794dc6f145 | -15.89689 | -43.04181 | 2024-10-09 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e96b152c-677c-39a6-812a-ad7bf7735a1e | -17.09435 | -43.80275 | 2024-10-09 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d864ed1d-1e43-3b47-80a5-cadce5feec0b | -16.68 | -43.88494 | 2024-10-09 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce94d563-9333-3fa0-ad50-3a21453d42b6 | -16.66995 | -43.16037 | 2024-10-09 04:17:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e1a0b3d-26b5-3801-a4b1-4361934473a9 | -16.66746 | -43.16052 | 2024-10-09 04:17:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1e5fb64-6ec4-3f3a-9034-67309329ba3e | -19.82195 | -43.80247 | 2024-10-09 04:17:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68517288-8ae2-346a-bbd1-8f43df6039ed | -19.82886 | -43.80375 | 2024-10-09 04:17:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca8f3d8-6473-3766-9ab1-52908b6cb0b6 | -20.42453 | -43.93932 | 2024-10-09 04:17:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fee3920d-9c79-3856-9d28-f1e0f8630866 | -20.42053 | -43.94249 | 2024-10-09 04:17:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b226c166-ac8c-3908-80d1-2fdc7bdae940 | -20.23696 | -44.43819 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9254e6d8-43bc-3b58-8eeb-dde39e3ffb53 | -19.83291 | -43.80027 | 2024-10-09 04:17:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c401daa5-f122-37ee-a5f0-3cce0ec1b3c1 | -19.83234 | -43.80424 | 2024-10-09 04:17:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8a016fcf-5dec-39e1-b7d8-454d844eea8d | -19.83095 | -43.80327 | 2024-10-09 04:17:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e185fc48-f826-319d-9cb2-9dfca854e6d5 | -20.39793 | -43.90167 | 2024-10-09 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5e2de2b4-d9ef-3e38-aec1-f058a578ebfb | -20.16484 | -44.40323 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 32c17bb2-5a64-3f9d-86ab-4558847aa974 | -20.16427 | -44.40713 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dfd7d465-7051-3538-937d-d728b5e8bfdc | -20.68628 | -45.0025 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f3c020d-3468-31df-9f57-d99f2de93d91 | -20.40139 | -43.90233 | 2024-10-09 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2dc9c8d7-8226-305a-9798-2dcb01c70933 | -20.40083 | -43.90633 | 2024-10-09 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 57f7e845-fd6c-3fe5-971c-5902ef4cad97 | -20.39737 | -43.90568 | 2024-10-09 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ae1c053c-437e-3bc9-8230-1403b2847585 | -20.3968 | -43.90965 | 2024-10-09 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 374156db-5e81-3740-8fd7-4949f7525bac | -20.23978 | -44.44275 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 37a12d80-219c-3e1f-8907-7b9b5548de4b | -20.23356 | -44.43755 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c5adb5e-531e-3f0a-83c6-18f3e1b86a38 | -20.22336 | -44.43576 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22792a49-b7c7-3eb8-9b9a-6ebecce6c3dc | -20.15744 | -44.40612 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6041dad2-9386-35bf-9643-0627521f4fc2 | -20.10509 | -44.21223 | 2024-10-09 04:17:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ee82c086-2a50-31e0-ba0c-ab87ea20abc5 | -19.86654 | -43.62582 | 2024-10-09 04:17:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e6bce2eb-6700-3134-9a9d-471ee8c2a912 | -20.22394 | -44.43179 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fc608075-544b-38a5-8b27-86f41f31e664 | -20.21938 | -44.43916 | 2024-10-09 04:17:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1aad0a3-c6d8-3f3a-afc6-ef196b68cef4 | -20.10167 | -44.21164 | 2024-10-09 04:17:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 620f63bc-a238-3984-8fe4-8cf884f3fb16 | -21.19707 | -44.93884 | 2024-10-09 04:17:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e3b84df-1fbb-3d88-b090-34ec2b48aa0d | -21.95734 | -45.35885 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b2ae5bd-b84f-3523-8782-f5d5db97fe4f | -21.95676 | -45.36275 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42489e5d-a5b1-3a84-9fb0-ab95d131a461 | -21.95397 | -45.3584 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c46af6d6-5fb7-3a1f-99ae-6d21083ec8fc | -21.94837 | -45.34977 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eefb1063-e77b-352e-834d-d927b8a1bef2 | -21.94778 | -45.35373 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49064414-2808-3c13-916a-58abe67014a8 | -21.94499 | -45.34932 | 2024-10-09 04:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d63d018f-5372-3533-ad23-bdbdb1b4f3a1 | -21.62912 | -44.63672 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 92369b6a-a900-3846-ad15-1abd9b112cb5 | -21.62854 | -44.6407 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README84.md)
