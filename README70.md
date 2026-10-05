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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5dfff88-9497-3cdf-940e-a96f43e678d6 | -13.5127 | -40.7705 | 2026-10-05 15:52:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 160cdfb3-bd61-37c5-a04f-c091f1997eec | -12.81273 | -43.3077 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b2876432-9ef9-3664-abc5-08070d81bbc5 | -12.81317 | -43.31148 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 734b6bff-af71-385f-a45f-eade11b7b9b1 | -18.3088 | -42.22644 | 2026-10-05 15:52:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 70b519e4-8937-30f9-bf85-39b26804e61f | -16.06702 | -41.34853 | 2026-10-05 15:52:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 02ca4c38-d462-3578-a74b-99e9500fc7e9 | -13.28686 | -40.45804 | 2026-10-05 15:52:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0a22adba-83a3-3244-8b43-69f42f4cb73c | -12.85591 | -40.41177 | 2026-10-05 15:52:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d228e7aa-c1f0-31c0-b841-36a7037f5d4c | -13.32681 | -39.07035 | 2026-10-05 15:52:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 22487c60-1056-3b10-aee0-59a9ef3df66d | -15.69022 | -39.77904 | 2026-10-05 15:52:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 020e9156-2b08-3197-9486-9a7148c27637 | -13.90112 | -40.76114 | 2026-10-05 15:52:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3a2d63f8-0b97-349e-bd3a-1cea53b99652 | -16.40215 | -39.42568 | 2026-10-05 15:52:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 17dce00a-038a-3b5c-837b-015e06520c37 | -15.14919 | -42.15916 | 2026-10-05 15:52:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f351ee56-840d-3108-9c98-7dc7cea70deb | -12.71723 | -40.23198 | 2026-10-05 15:52:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f39ccd28-3eba-34e1-b451-49867411b0c5 | -13.6365 | -39.29942 | 2026-10-05 15:52:00 | NOAA-20 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 867d67aa-66c6-3423-8f94-1a8a8b7d528c | -14.07426 | -44.03945 | 2026-10-05 15:52:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03360ff3-3d83-311b-940a-ec54f3e2b44b | -14.62784 | -43.66637 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5dec35cc-9a38-39e2-8e98-d953f6f05407 | -15.79239 | -40.79589 | 2026-10-05 15:52:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 2ce83cf2-a056-386d-96a9-bfc0b933c2ac | -15.79451 | -40.79476 | 2026-10-05 15:52:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1abc5c99-cc78-3176-be73-3b34b86e2763 | -15.47848 | -40.49607 | 2026-10-05 15:52:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2eae6180-8b2a-3905-9f1f-28d55ddbc562 | -12.76469 | -42.00431 | 2026-10-05 15:52:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 770b4e13-e48b-3a13-a3a9-e8084899601b | -13.18638 | -42.81613 | 2026-10-05 15:52:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5ebd29f9-86d6-3ea5-bde4-f2283f536229 | -16.32412 | -43.74257 | 2026-10-05 15:52:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d8179f7-1014-36ad-989f-0f208f3ea05d | -13.78583 | -43.50919 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b523cf0b-eb88-307b-9e95-2fe99d4a132d | -12.81832 | -43.30703 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8f4ca786-0053-348e-bbb4-09bafda4ed85 | -14.07207 | -40.60532 | 2026-10-05 15:52:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 294b9f6f-b7a6-319a-af6e-fa8bd536eec6 | -15.48947 | -41.19299 | 2026-10-05 15:52:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 80363ac3-8113-3aa1-90f7-cbfc88db4c91 | -13.26962 | -40.36156 | 2026-10-05 15:52:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b0c0d09b-c9fd-35e4-9fd3-911c0f0ddfb2 | -14.69292 | -41.20749 | 2026-10-05 15:52:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 012c9032-9f0a-3fdc-a38e-bae14328524a | -18.30951 | -42.2335 | 2026-10-05 15:52:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 0319d4d9-d3f3-3606-8e43-4bd69419abf1 | -13.97227 | -40.98088 | 2026-10-05 15:52:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 18f296d6-af0c-36f9-9b26-39b0e2a44734 | -12.8123 | -43.30392 | 2026-10-05 15:52:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 94cd9056-8c4a-3cf2-bcf7-cd68b0429831 | -18.43055 | -39.73305 | 2026-10-05 15:52:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 21878e98-a950-3e51-aa7c-aed4c62b3dc4 | -14.37286 | -41.89577 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7e47c846-fac5-31f6-b5cc-f21058143424 | -13.75648 | -43.62199 | 2026-10-05 15:52:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec47268f-fb73-39df-b33a-4d06349c081e | -13.60198 | -42.49696 | 2026-10-05 15:52:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 1f7db50d-0c0d-3d20-9952-ca72602bdb2b | -15.56964 | -40.92847 | 2026-10-05 15:52:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5b5c4feb-4676-3241-8e50-0b2bc5fb4f41 | -14.21685 | -41.31092 | 2026-10-05 15:52:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 871b55a0-7654-3f28-834d-e9c3f801a901 | -12.6773 | -39.10271 | 2026-10-05 15:52:00 | NOAA-20 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9d1b5687-de2c-3a1f-8815-c5d6c9c23bbe | -12.8579 | -39.92167 | 2026-10-05 15:52:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a251eafc-5f7f-304b-a019-e6e1e96867da | -13.75071 | -43.62264 | 2026-10-05 15:52:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 4de1c8cc-f798-3e5b-8580-663e00f3e61d | -12.3765 | -40.31159 | 2026-10-05 15:52:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8245e664-0fa9-3903-95a6-36b2c997f117 | -14.0491 | -42.49081 | 2026-10-05 15:52:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 754cf4d9-f53e-3632-818f-7b79b1446c2a | -19.32361 | -40.88025 | 2026-10-05 15:52:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a3ea4f03-2360-3afd-bb63-a84ed9054585 | -16.40159 | -39.42102 | 2026-10-05 15:52:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 27480dd5-55fb-377b-b5ef-ab983581c584 | -14.08017 | -43.77106 | 2026-10-05 15:52:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2766b00d-0be0-3bb5-99c7-b9bc08619f04 | -13.8476 | -42.37242 | 2026-10-05 15:52:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f64b9557-0e0c-32e9-8683-e77d73fe6974 | -18.30463 | -41.00564 | 2026-10-05 15:52:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 25a32b5c-0805-33b9-8853-726be13cdc65 | -15.64547 | -41.18198 | 2026-10-05 15:52:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 64946361-013e-3ea2-9b59-4b86138f4b55 | -13.26917 | -40.36274 | 2026-10-05 15:52:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4e894621-7ea4-3365-9385-6a38fc034725 | -18.31467 | -42.22866 | 2026-10-05 15:52:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| c1ca2af7-21d8-3f15-ad56-dd7014a1af16 | -14.37549 | -41.91815 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ec19525-5136-3dc3-9f5c-fc7cf3289695 | -17.34177 | -41.8429 | 2026-10-05 15:52:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f9302de4-5fe5-31e8-bd62-318ef010af3f | -13.63807 | -41.90695 | 2026-10-05 15:52:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 844e000e-06ea-3722-99b7-0e82802a6425 | -14.21614 | -41.3051 | 2026-10-05 15:52:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 5e5cd6ac-0d68-3114-af61-f131fd2f6c28 | -13.20429 | -40.51403 | 2026-10-05 15:52:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4a495ceb-1ccb-3150-b2b2-c3bf273e21c2 | -12.0394 | -38.27546 | 2026-10-05 15:52:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0d7f2206-a721-32a4-a795-084fe0c6015c | -14.5806 | -41.37621 | 2026-10-05 15:52:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5ff73efe-faa2-3b95-9375-14a0c5ef4b70 | -14.07969 | -43.76683 | 2026-10-05 15:52:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2e30e30b-712b-31ee-b782-0b33178eb209 | -14.21879 | -41.84781 | 2026-10-05 15:52:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 00c2d6db-2dd1-3b00-a8e1-3834ec166cc2 | -14.62712 | -43.66439 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae4e284a-6157-3305-9229-05089acc0247 | -16.15987 | -41.23002 | 2026-10-05 15:52:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 57d4e482-a29d-3742-8f06-6e04c3420d94 | -13.32733 | -39.07381 | 2026-10-05 15:52:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 135e7641-b931-3d9f-b966-9f3e17d4f7d1 | -14.63498 | -41.53511 | 2026-10-05 15:52:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 53eafe88-ff6e-3e7a-9baf-28a168b962c3 | -15.98555 | -41.78984 | 2026-10-05 15:52:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 75662a92-7ff9-38b5-9907-fabbddc48586 | -15.18873 | -42.12706 | 2026-10-05 15:52:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d74bfe1a-dd66-369e-b141-2d8165afd842 | -12.50745 | -41.21205 | 2026-10-05 15:52:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e76dec66-bb54-3817-97b5-c93bf2de8434 | -15.19414 | -42.12714 | 2026-10-05 15:52:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e35569a6-b37f-32ad-a015-83a0f7bc746b | -12.75638 | -40.03561 | 2026-10-05 15:52:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7ed69ec1-c0e6-3f36-8928-2d71159aa89e | -15.19234 | -42.1266 | 2026-10-05 15:52:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| bb6a7030-72ca-3ecc-9722-3be77a2226c9 | -14.69386 | -41.90493 | 2026-10-05 15:52:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7d6e6587-c56c-3cf8-9103-2c2c4c2caec0 | -13.60239 | -42.50039 | 2026-10-05 15:52:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| c48962e3-475d-3f5d-a6de-4518e0d4f81e | -14.28456 | -41.49659 | 2026-10-05 15:52:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3aab0d9c-c648-349c-90bd-bba24864cb30 | -12.67654 | -39.10239 | 2026-10-05 15:52:00 | NOAA-20 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c7abdab0-0021-3c07-adb7-4fa8cb914175 | -13.84879 | -42.37204 | 2026-10-05 15:52:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd623949-3257-37d8-9bf1-7c3b4d6628c0 | -14.04362 | -41.64366 | 2026-10-05 15:52:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7744a553-128c-3bf6-93a2-e331017f87e6 | -12.86347 | -39.92963 | 2026-10-05 15:52:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 38.2 |
| b056df0f-411d-372d-aec5-135293575444 | -16.16306 | -41.22845 | 2026-10-05 15:52:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| 0b348a06-9a31-3b5f-98f5-8b3f589b6404 | -18.43147 | -39.73156 | 2026-10-05 15:52:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 76b19f32-9a9a-3fcb-b399-dc703c45a6d1 | -15.13269 | -42.35147 | 2026-10-05 15:52:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 25677d36-b323-3a31-887b-f8aaaeb2f490 | -14.215 | -41.59304 | 2026-10-05 15:52:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 33de4868-0eee-3111-9a02-da0ae7f8c169 | -14.9426 | -41.34223 | 2026-10-05 15:52:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c1a072c6-f8cc-3e99-a19a-83cf1ea7213c | -14.38109 | -41.92085 | 2026-10-05 15:52:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 26253dda-cec3-3dad-bb4b-91aa9bc26f81 | -13.59834 | -40.71582 | 2026-10-05 15:52:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3fcf24f4-5264-3927-8a8f-b01a61c00ddf | -13.32887 | -43.84892 | 2026-10-05 15:52:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3715dfa0-679e-31e4-8ba9-9e0c9101ae0d | -12.31115 | -40.26862 | 2026-10-05 15:52:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9cc4ca66-f90e-360e-8f04-f20197848dc9 | -13.2068 | -40.45818 | 2026-10-05 15:52:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| eb5cd770-3286-384f-b35a-a6f1b6c549c7 | -14.82694 | -41.64268 | 2026-10-05 15:52:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 02a96cb7-b4c5-3ae0-884d-762c06a7f610 | -15.40446 | -41.78431 | 2026-10-05 15:52:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b17e5d0a-cde7-3d3b-a96d-9d25e1c438b7 | -15.96321 | -42.89745 | 2026-10-05 15:52:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c17ff56-71e8-30cc-badd-8b45a4e0f240 | -12.7 | -40.54179 | 2026-10-05 15:52:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e9d0130c-7258-39ba-8b86-126bea141201 | -13.00252 | -39.55289 | 2026-10-05 15:52:00 | NOAA-20 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2d330419-0dff-3e83-85c0-2b893f6b4b83 | -12.72071 | -40.23477 | 2026-10-05 15:52:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e00d7904-b6a4-3c84-95f9-9c364ab160a0 | -12.85597 | -40.40977 | 2026-10-05 15:52:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ef643a78-5b27-3fbf-9e8b-89257f336c94 | -11.64259 | -43.62469 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 40dc4439-3c9a-338e-8c8b-872ff1b6fdac | -10.97141 | -45.43447 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 307a5ccf-dea4-3804-970f-2ceab75b56ed | -11.6799 | -43.6653 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63321d00-0066-391a-8a50-f18937022f7e | -11.63511 | -43.61028 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96ab07c4-d304-3de9-a107-bf6f88351a35 | -11.72836 | -43.50247 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b4e9bb10-d4b2-3a76-8b0b-b5d04d32996a | -11.68508 | -43.66082 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 5a1ed7b6-41f2-3564-80ca-252be1df2e46 | -10.40154 | -40.5069 | 2026-10-05 15:54:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README71.md)
