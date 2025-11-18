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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4787738-a382-3946-841f-c950715d2da7 | -3.69699 | -42.35928 | 2025-11-18 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 5934182d-65ba-3635-b975-4f649fd5d43d | -8.45805 | -47.98759 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4d878661-6547-3a05-bd47-fabe17032087 | -4.14031 | -46.3558 | 2025-11-18 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d2d88c12-aa23-30aa-886a-672e99e95276 | -1.10192 | -48.10354 | 2025-11-18 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f54232e6-5872-39c6-b9a4-e87d76261202 | -5.17221 | -43.23887 | 2025-11-18 12:16:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 27bacb61-e777-391e-8a6d-89e2f7461a0b | -1.51586 | -47.79215 | 2025-11-18 12:16:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0283e15a-fa7f-3f15-9b66-770f85774a82 | -3.36647 | -41.45091 | 2025-11-18 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| b5028abc-84ca-30b7-8360-bd1df0d74ebd | -3.2769 | -41.91162 | 2025-11-18 12:16:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| dcf58454-7076-3d89-a38a-f36d2623f2ed | -8.46814 | -47.97994 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9e8fd454-f763-39b3-9cd6-6ee659811278 | -2.59745 | -45.13803 | 2025-11-18 12:16:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 788cf208-6848-34a7-9aa4-14818c6e1a4d | -8.4714 | -45.13654 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1b8e27ca-b25c-3cff-83f2-4c45b48bc9c2 | -5.34471 | -43.76176 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 19cbdf85-254d-3f53-941f-d8e4129add97 | -9.93326 | -47.26491 | 2025-11-18 12:18:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 4554cc39-3463-3eb3-a573-4b285e969467 | -9.25047 | -45.79995 | 2025-11-18 12:18:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 8af78646-c758-31ba-b8d2-8088410f3683 | -9.94232 | -47.26615 | 2025-11-18 12:18:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f673b515-d482-3340-8735-9d8555aa6dca | -10.86603 | -44.08577 | 2025-11-18 12:18:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3bd9acd6-0a5f-3934-ab55-14ca876cf333 | -12.55009 | -42.95388 | 2025-11-18 12:18:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 86b5fd6b-b1d3-3aad-8442-d726214af714 | -12.42352 | -44.45531 | 2025-11-18 12:18:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ce048879-737e-3d2b-90f4-8e8d65db2ba9 | -14.98094 | -46.57435 | 2025-11-18 12:18:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c838796e-f3a0-352a-9d79-b9fd1ca62ee7 | -9.00282 | -48.42708 | 2025-11-18 12:18:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07e096ad-1e65-3bd6-ba78-a2d728500812 | -11.49677 | -43.98857 | 2025-11-18 12:18:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 6d4fde84-fdcc-3086-abc3-da4190e890c3 | -9.60159 | -44.38192 | 2025-11-18 12:18:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f791d222-c920-3aa8-b844-525bb7b84672 | -9.97637 | -44.78481 | 2025-11-18 12:18:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| e92aebd0-596b-334a-9585-1f0699c085d6 | -14.63801 | -43.82995 | 2025-11-18 12:18:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 80b66628-ac42-3d34-b583-5b449ff9820a | -12.76033 | -45.431 | 2025-11-18 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ad57587a-92d1-3821-b6f4-59b0f4ddcbd9 | -10.28929 | -39.58562 | 2025-11-18 12:18:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 036bbac1-ea86-3b7c-a47c-d9efcb430c99 | -12.70778 | -43.36957 | 2025-11-18 12:18:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 87d7d5ec-d807-353d-9cba-cd4b3cf9f594 | -8.69969 | -48.81377 | 2025-11-18 12:18:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e2526e9c-91da-3cc0-8a10-0f5e67be9217 | -13.28119 | -43.29185 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 8a2c203d-cf6d-3840-a7b2-2dc29e955aa8 | -10.516 | -43.95536 | 2025-11-18 12:18:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9716699b-064b-3490-9550-877427cf307c | -9.39912 | -48.44224 | 2025-11-18 12:18:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fe3a17cd-bcea-373d-ba14-a86c2186568d | -12.48281 | -40.78154 | 2025-11-18 12:18:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 64.7 |
| eb415ad1-ba34-39e8-a59c-9070f46613a1 | -9.97088 | -44.77816 | 2025-11-18 12:18:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 45a1da4f-cf75-3da1-ab2a-0967a2f49149 | -9.79469 | -41.77806 | 2025-11-18 12:18:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 878365fe-0217-3f54-ab9c-ef6e1c4d115c | -13.48524 | -44.29154 | 2025-11-18 12:18:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| c2938e84-2a6d-3d21-850c-3e8fb20c76bb | -13.25745 | -42.92771 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 4ce28242-0cd6-30e0-8075-ecfb2564154f | -12.51004 | -43.38898 | 2025-11-18 12:18:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 004fea0c-97bf-3bf6-a2d8-341b4ca530ba | -14.68125 | -43.77949 | 2025-11-18 12:18:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| dab7a4de-2592-3354-b58f-52abab5fe77b | -9.96915 | -44.79108 | 2025-11-18 12:18:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 05a4862a-d274-33be-a351-b9f35d93bc0c | -12.52227 | -43.3904 | 2025-11-18 12:18:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a8a137ca-0511-3639-9b13-6e7ad08315b0 | -9.93196 | -47.27433 | 2025-11-18 12:18:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 01fbe63f-3299-368a-a71a-5464281f60d5 | -12.88403 | -46.06076 | 2025-11-18 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e7906cfe-0b2a-3907-ba38-c8ba4284391c | -14.68487 | -43.78577 | 2025-11-18 12:18:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d965eaa5-2fe3-3ebe-8b3c-cd7e045b80e9 | -11.93075 | -44.55439 | 2025-11-18 12:18:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 331aa15d-2d4d-37be-94e1-ded803a9df2f | -12.87555 | -46.04766 | 2025-11-18 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b97217f6-734a-3f28-a20c-cba80ba0760a | -9.32956 | -46.10907 | 2025-11-18 12:18:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 544bcbfb-2faf-34a7-9b88-6b6d4984691b | -9.39786 | -48.4511 | 2025-11-18 12:18:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 71dd8046-670a-39f7-9ded-26794eaea590 | -13.2892 | -43.3063 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 311f2028-55eb-35e2-b125-86a44d34a1c7 | -15.50246 | -46.64564 | 2025-11-18 12:18:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 237e4baa-b3cd-347b-b32b-c0aeaeaa434e | -9.99656 | -39.18525 | 2025-11-18 12:18:00 | TERRA_M-T | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 724234ca-6c54-3211-bdbd-9d42473e9d3b | -13.29154 | -43.2873 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b137dd00-1e60-3005-9b93-ec9c7579d2c3 | -12.51227 | -43.37078 | 2025-11-18 12:18:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8ed004d1-e6ef-360a-b77e-db5b3a293d7b | -9.74947 | -43.9448 | 2025-11-18 12:18:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f4740ec1-ef78-3f4d-82a1-0e22b72d6661 | -11.15941 | -44.03195 | 2025-11-18 12:18:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 64a9a127-a989-3fa4-8da3-2c5a778acc3f | -14.65242 | -46.51433 | 2025-11-18 12:18:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0d9e3792-ef71-37c4-bbda-7ad27e0c7dab | -12.73697 | -45.3953 | 2025-11-18 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9b06bc7f-29a0-396d-8ae5-a4f654171d1f | -13.25532 | -42.94611 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 134.1 |
| fd43bfc5-aeb2-3ffd-b955-b25514ff1b36 | -12.48431 | -40.77595 | 2025-11-18 12:18:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 54.0 |
| fcd6d6f8-8f58-3731-a131-35d889a51f7b | -15.66225 | -43.65582 | 2025-11-18 12:18:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d687d2e9-f5cb-37bb-9602-de414d8302b0 | -12.6955 | -43.36807 | 2025-11-18 12:18:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| baae022a-4af8-3faa-94ea-c987a38de273 | -13.93799 | -43.35544 | 2025-11-18 12:18:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 4be0154a-6a00-302d-8009-84e5f57a57df | -12.70553 | -43.38788 | 2025-11-18 12:18:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 07997e48-9feb-38cb-aeb0-2945ff46c3fc | -10.00648 | -39.17984 | 2025-11-18 12:18:00 | TERRA_M-T | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 8885ff03-af73-337a-99b2-36ea3adc96a7 | -13.23492 | -43.54427 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1f65e9d0-e06b-3f64-81c8-42e9e76cfa7a | -12.3788 | -43.80896 | 2025-11-18 12:18:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b1a66a69-e35f-3b09-9f68-1f11b3568734 | -12.85764 | -41.47393 | 2025-11-18 12:18:00 | TERRA_M-T | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 40.8 |
| f5e18130-5bec-31d1-90b5-0c97a239fefd | -9.87707 | -44.188 | 2025-11-18 12:18:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a2ffec54-3c07-334c-be45-73c910828f18 | -10.8642 | -44.10004 | 2025-11-18 12:18:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c82a679a-8348-3876-87ee-afad1fa505cc | -14.65021 | -43.83141 | 2025-11-18 12:18:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| b93b2ca5-bd4f-31f3-88d8-961a2717c4b1 | -11.16139 | -44.01658 | 2025-11-18 12:18:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 5607ff13-3cbb-30e9-af1a-007a26d9fd37 | -12.41685 | -42.07182 | 2025-11-18 12:18:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 1c214567-ce79-3de2-b081-915e70a29bd6 | -12.86556 | -46.04613 | 2025-11-18 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| dca2f144-67ed-3475-a2a3-8069175b73cb | -13.2327 | -43.56239 | 2025-11-18 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 31f56918-0e6c-3600-b7fe-9b02c3e0d63b | -18.0355 | -47.65641 | 2025-11-18 12:21:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8cc32385-47bc-3662-8c82-d1c10ad73d13 | -16.20908 | -42.30873 | 2025-11-18 12:21:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| cd43d4f1-f8df-33a0-8b6a-dc105c14f9a9 | -16.20636 | -42.33536 | 2025-11-18 12:21:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 27ab7ed0-42e3-3d07-9190-89c1011cc876 | -15.80694 | -47.96006 | 2025-11-18 12:21:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5288cc85-b4e7-334c-a981-75fc6a6c0bb3 | -16.49558 | -43.76963 | 2025-11-18 12:21:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4cc487ff-5686-3d58-a889-7ee0000774ad | -16.20179 | -42.328 | 2025-11-18 12:21:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| 00843be8-dc57-30e9-b7c6-38561bb8a957 | -18.03695 | -47.64522 | 2025-11-18 12:21:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e15adaea-6313-3abc-85f5-578ea389b95a | -24.94204 | -51.51363 | 2025-11-18 12:23:00 | TERRA_M-T | BOA VENTURA DE SÃO ROQUE | PARANÁ | Brasil | 4103040 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6ae1e058-a4a4-3dc4-8a60-4f273a5b33ed | -20.8933 | -45.2687 | 2025-11-18 12:23:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |


