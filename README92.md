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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 093e14ac-f8c5-3742-b110-2ac4fd3058ff | -13.37206 | -44.00809 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| c1b34517-3bc4-3747-b704-7b5d2af4a9a4 | -8.84776 | -41.1289 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| f0f5147f-8249-3298-bec4-b8f5cfda135d | -15.0835 | -40.85907 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 960b79fc-3216-36e8-9520-8f31dc1aa63c | -13.37736 | -44.00834 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4fae8c1c-acd9-327e-a91b-94388f679f99 | -11.35434 | -43.3562 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9fc2afcc-ec08-3dcc-bcfc-290c920a78e0 | -10.9094 | -43.85518 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a7ba84e2-feba-35dd-964a-a615bd2d5e4e | -11.61193 | -44.13901 | 2026-09-29 15:46:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8438a706-33fc-3a41-ab00-9d2b52f26048 | -12.91792 | -40.04473 | 2026-09-29 15:46:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| c6072c66-306f-3eab-878d-49b21b7128df | -11.44183 | -43.44598 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| d8f2ca5e-88f0-34a4-ae59-44573e54d906 | -11.32232 | -40.34262 | 2026-09-29 15:46:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 131f1a15-8de2-3b4b-9727-cfb1c91db327 | -15.24954 | -43.27458 | 2026-09-29 15:46:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d459afd9-16cb-315f-8399-f423284a2dbf | -8.98957 | -44.15012 | 2026-09-29 15:46:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 84cba5fc-7459-3457-b572-0b930766621b | -9.6211 | -42.84671 | 2026-09-29 15:46:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a824f60e-c882-37e7-8d9a-4bb324628b7c | -15.47118 | -40.83874 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 0eecac76-921b-389f-875c-4f8f359e31bc | -15.30018 | -42.76974 | 2026-09-29 15:46:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ca2d8b07-21ee-3c3b-918d-b75ed32b751e | -11.41152 | -43.43178 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 203899f6-2bf3-3e4b-8423-74fcfebcda16 | -15.465 | -40.83917 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 3c8255b2-4b31-3166-a6f1-810d90886e19 | -12.23946 | -38.35568 | 2026-09-29 15:46:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e15389c8-dd79-3316-8e0d-e4814c1a6f67 | -10.58533 | -39.45845 | 2026-09-29 15:46:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 93fddc29-f70e-3f61-a22a-4940e965cde5 | -11.42601 | -43.42864 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f7247324-98fc-3697-aae1-67282597986b | -11.40472 | -43.42456 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3b02a664-7c00-3ed8-b97f-73e3557a2d89 | -13.02843 | -41.03757 | 2026-09-29 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 89459a9b-ada6-319a-9f8b-cc25163e46c4 | -11.4584 | -43.46975 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4a8400d0-1374-32f9-96ee-c0c8369fdce6 | -9.61003 | -42.31011 | 2026-09-29 15:46:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 63eddd52-7408-3b5d-9fee-2fec41b99d1e | -11.7152 | -43.45753 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 56deef5f-4cf1-3df0-a27f-3ecb722a7d95 | -14.81368 | -42.77481 | 2026-09-29 15:46:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c76f72da-dfec-328a-809f-2d881c98697d | -11.40054 | -43.45016 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8515f580-2301-3302-8dec-baff14c55236 | -9.42575 | -37.77742 | 2026-09-29 15:46:00 | NPP-375 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bf07bc32-7ce2-3c9e-8e1f-8a20ca892eba | -11.42275 | -43.46867 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 64c810d3-8771-3629-85d0-36cc77100420 | -14.11346 | -43.62876 | 2026-09-29 15:46:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10d2e201-41e2-3f5e-bed6-f789ad99b013 | -14.24278 | -41.31199 | 2026-09-29 15:46:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| e7bc3b01-af3c-328f-a4c6-419a3e487534 | -15.5491 | -40.75383 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ed5ed0d0-174c-3303-a2e8-e6b2a34258f0 | -15.30403 | -41.77871 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 2035c329-7edd-3b99-ba34-f7cdafdb83b6 | -11.39381 | -43.38801 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4b478ef7-18eb-3d15-8bc0-26aa50a520f6 | -11.38691 | -43.45976 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a318acb1-0dba-38a6-996b-14316a8d85c2 | -10.27443 | -40.0892 | 2026-09-29 15:46:00 | NPP-375 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 99582804-e470-3955-b661-341c1ee644af | -11.39207 | -43.38355 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f3229869-ae74-31f1-a6e8-1fe9ed3599a8 | -11.41983 | -43.43566 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 33ee9501-fc32-3867-ab3f-dd3621f6a207 | -15.32879 | -41.12918 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a70846f3-7a6d-3ed4-92b4-b62dfece2da7 | -15.32825 | -41.124 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f8be239c-d193-3408-86ef-fa089585ef8c | -13.6372 | -42.70417 | 2026-09-29 15:46:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 8c842ac5-b13a-312e-979b-4dd0e4ffe374 | -11.37625 | -43.36635 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6a0860cc-568f-363d-a5ef-670d57036451 | -14.76275 | -41.20412 | 2026-09-29 15:46:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| b8cba5bd-f7f3-393c-be2c-07e8abe2bc3c | -15.51725 | -41.35349 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e4d9a614-7b9c-3f76-87d9-8888273cbd95 | -11.43357 | -43.43417 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f30ba382-1d73-36a3-a229-6895973e4ddd | -11.66775 | -43.53392 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ccfa4087-b54b-37f6-b13b-a524d3c06a85 | -11.668 | -43.5354 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e10fa928-6c70-315a-9ddf-6097fe6ec8cc | -11.6581 | -43.51054 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fdb1cddb-d99f-3185-8eb9-39b7acbf5843 | -13.6757 | -41.01661 | 2026-09-29 15:46:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| ddb98655-d98f-34fc-b8fc-38efa39a17df | -9.05901 | -45.00008 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ed274a1b-63b6-35f7-b2c8-493032dd0209 | -11.14813 | -40.30233 | 2026-09-29 15:46:00 | NPP-375 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9cbc57c-93eb-325a-a585-ac81d2fa3ed2 | -12.99816 | -39.75818 | 2026-09-29 15:46:00 | NPP-375 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| abfcc2cd-9110-312d-81b4-5ed02ab8a648 | -9.06063 | -45.01421 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae630fc6-12c3-324e-a4ae-e7b689d0126b | -14.99158 | -41.49012 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| bafa3e6b-2093-3294-a3e7-5006e3f2436d | -14.48575 | -40.82063 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8d5719a7-7ef0-3c2f-8732-4cdf890b9a73 | -9.4397 | -41.83028 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 155.5 |
| b326ae41-420b-3c65-a4c7-66aadfeb64e0 | -12.2896 | -40.31833 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b989962f-0555-37ae-b836-bbbba8ca7521 | -10.25606 | -44.6007 | 2026-09-29 15:46:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b55f4d5f-b3ca-37a9-8151-32087c0033c9 | -15.31047 | -41.77732 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 39ed5d18-36ca-3b76-a401-017ae0531765 | -15.30058 | -42.76895 | 2026-09-29 15:46:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 52c222bb-2505-32e2-b509-dfa95c63f606 | -15.82994 | -42.56007 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 529ea4f8-3557-38bd-a832-c92f048bce89 | -11.6511 | -43.50983 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bed3f734-d89d-3c8e-880a-67aa98f3c21f | -11.66261 | -42.60932 | 2026-09-29 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b46e576c-d5fa-39ce-823e-e6a66d555c68 | -11.40879 | -43.46206 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 223d9431-d9b3-3a44-b1df-981fb12578cf | -9.43804 | -41.82048 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 9299cd28-f43d-3d34-b230-e5b0d8098cb2 | -15.21374 | -41.98107 | 2026-09-29 15:46:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 307be13b-4195-3153-bf75-54fedc93e257 | -11.11168 | -40.08038 | 2026-09-29 15:46:00 | NPP-375 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 62045563-e211-37de-af3c-276b31823d68 | -11.31462 | -43.55558 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 16a25989-245b-3a54-95db-c19527909429 | -12.34351 | -44.27302 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c12cb21d-5d53-3536-88f3-9bfd2fa4ef16 | -13.75891 | -42.88474 | 2026-09-29 15:46:00 | NPP-375 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f302fdfb-5bf1-3f79-8945-150d1d6f053d | -11.68303 | -43.54533 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 23e478b7-895f-319f-94ea-4886c8b6668e | -11.64349 | -43.50421 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 504249a7-7a73-36c9-bf02-7f9d338d4279 | -11.25789 | -37.35937 | 2026-09-29 15:46:00 | NPP-375 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 1d29f1df-d5bc-3e71-8ff3-a3894d7bf40e | -14.49187 | -40.82034 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 61121f1d-f31c-3411-b041-e1fd285e05c8 | -13.22795 | -42.53474 | 2026-09-29 15:46:00 | NPP-375 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 13e29bf7-7e4f-37df-b221-c9e68f304dcf | -14.05832 | -40.5687 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b59a9fd8-6134-3607-9f06-a60e45348c87 | -14.10631 | -43.62948 | 2026-09-29 15:46:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3135d1a-0858-3d77-82c8-8743253d474b | -11.39987 | -43.4439 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f7c482a1-0772-3d14-9934-76c0166cacf5 | -11.59232 | -40.18734 | 2026-09-29 15:46:00 | NPP-375 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 315bb37d-49e4-38ea-b64e-6d27f0844652 | -9.45019 | -41.81909 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5eb2b495-54af-32b7-8b31-164f0ede760e | -14.8204 | -42.77237 | 2026-09-29 15:46:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4b523a59-5358-3574-a7c5-8ddf8c91be73 | -8.30602 | -39.38003 | 2026-09-29 15:46:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b79f5e04-be50-3fc4-a0af-1ad484c8e5a7 | -15.51585 | -41.3569 | 2026-09-29 15:46:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7f1c12ee-cf8d-371e-b612-31edc268d903 | -14.74022 | -40.94505 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| d8d435cd-016f-3164-8a2e-ccd5ceff5267 | -15.97771 | -43.00895 | 2026-09-29 15:46:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 85be270d-3f64-3560-ad2f-fe3b44d04539 | -9.06724 | -45.01554 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ef6769e7-2d58-3bf4-adce-ed2a6792f365 | -11.42454 | -43.42418 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 769e8d58-8920-3faf-b920-6f2e984729e1 | -13.37013 | -44.00922 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 1df15629-8c6c-3ff5-8fa6-efe938b6d1c6 | -11.6504 | -43.50345 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 00887e12-0909-331c-ae56-dc6c5fcc219b | -11.67874 | -43.50658 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| def2d9cb-d5e5-378b-b94d-70b13d15ab47 | -14.60347 | -40.77328 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 9d05a22e-71b6-3d69-abf3-4bd9d1e18408 | -14.82056 | -42.77427 | 2026-09-29 15:46:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b2a0a468-34c2-34d8-965a-f3e9e6eba4db | -14.74537 | -41.82349 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 46c790fd-6c88-3717-81d5-1b2dc3d57974 | -13.32736 | -42.70422 | 2026-09-29 15:46:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 5bb81c35-c59a-3e2c-b8ee-65335207e48d | -9.43914 | -41.82571 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 155.5 |
| c4ebbfa9-cb9c-3f05-ad5e-67cd6b8e7d9b | -11.39991 | -43.45179 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| be9cf957-6412-3e95-8149-583496f59fdd | -9.17197 | -40.47542 | 2026-09-29 15:46:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7eecc675-ca36-3a69-9d76-f01f0561700c | -14.48493 | -40.82404 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 46accefd-3042-3db5-8363-5887c9d29311 | -15.75408 | -42.28056 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9a66c404-a7b0-3614-8a16-c9222a2a5134 | -11.66325 | -42.61499 | 2026-09-29 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README93.md)
