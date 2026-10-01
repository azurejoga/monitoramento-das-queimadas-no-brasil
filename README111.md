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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efbda08e-0d44-3160-87d2-57b323af9502 | -14.47175 | -40.70486 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| ee686e8e-cfce-3c2c-bdcf-3979b168b57a | -14.64607 | -44.68405 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6654e005-3977-3f62-b895-2bd4746ae07b | -15.25815 | -40.91027 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 3a064e8d-e08f-35ef-8670-2cbb500e3cbb | -14.39061 | -41.91613 | 2026-10-01 16:11:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 76ebdbc4-8cb1-3188-a73f-142873460f54 | -15.10054 | -48.40874 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 67c5a076-336e-3e34-be8d-0f362e66031f | -15.59056 | -49.19953 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| abedc372-3325-3701-b0cf-505b200d8e2f | -15.25232 | -41.01437 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 8dcd8ed3-dcf3-3c16-b03f-3160530fecb9 | -15.58834 | -40.72838 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| b3fe631a-98fa-3e81-b990-9cb3484cfd3a | -14.2355 | -39.46487 | 2026-10-01 16:11:00 | NOAA-21 | UBAITABA | BAHIA | Brasil | 2932200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d41b1634-7131-36dd-90d7-79742ee13117 | -14.88607 | -41.66171 | 2026-10-01 16:11:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0e250d76-83cd-3713-8b05-efb99190dc94 | -15.96132 | -45.96122 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 03f319fd-42d8-3407-a1d2-ca2b1d69978f | -14.71506 | -41.02681 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 6730f5a0-b2ea-345a-a4e7-c500f6842fec | -14.07175 | -41.39553 | 2026-10-01 16:11:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0d71c4b4-02d7-390d-9522-d09af1abdb9f | -13.66522 | -39.91699 | 2026-10-01 16:11:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 77467b6f-2099-33ff-9c89-78cb7db43dfb | -15.89709 | -47.76231 | 2026-10-01 16:11:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4e039fca-af6e-354f-a056-4c634020294a | -16.39323 | -46.90804 | 2026-10-01 16:11:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da0d8890-a884-39e4-a8c8-a4282c120461 | -15.22425 | -46.15401 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d5087b98-4873-3fbf-9f69-d3ee725df08e | -15.63073 | -44.74022 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 31964e87-facf-3063-b44f-63ac60792462 | -15.96191 | -45.96591 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e29c9a7e-d800-3176-ae00-69da5e1ea65f | -15.71905 | -44.96611 | 2026-10-01 16:11:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2d073c8b-7b00-37fd-9fa6-35bb1fcc478a | -14.63889 | -44.94396 | 2026-10-01 16:11:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 59907cae-8cd5-324a-a225-c1f2088deb85 | -13.66853 | -39.91646 | 2026-10-01 16:11:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2710fb0f-9234-3c09-9585-9df050b06e74 | -15.29101 | -42.78705 | 2026-10-01 16:11:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b92a9488-0da3-3a94-9135-95e796ea05fd | -15.25287 | -46.15071 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 0be2c044-450d-3261-b6be-bca5d13cc0e8 | -14.36367 | -44.77633 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3c6f942c-ced8-3e39-b4f0-e9385b781166 | -15.80669 | -42.17595 | 2026-10-01 16:11:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cfe4a039-fc8c-36d0-b5ad-cf1b74ce4d43 | -14.36873 | -44.78322 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 05ca47c9-21c4-32d2-b09a-85a94ee06960 | -14.35014 | -44.73618 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6c80290b-a92d-3f7e-be3e-5a313fe14c96 | -16.43712 | -43.3644 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8fe69a2c-9576-310b-92c4-736b44556092 | -14.93338 | -41.69498 | 2026-10-01 16:11:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 598cf0a9-c6b0-3188-b26c-ea2cd972c9dd | -14.5072 | -41.35662 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a7c11594-f02b-3443-8ecb-8f3bc8f7c1ae | -14.74094 | -40.94267 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5a3887d1-d1dd-3a05-b77f-1d4b941e87e2 | -15.34059 | -42.79269 | 2026-10-01 16:11:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 41287a9e-0884-312d-8a18-d2781a4784f8 | -14.88495 | -41.65377 | 2026-10-01 16:11:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c92f2389-eca8-3fb6-b777-ed03ea26c2c1 | -15.65588 | -44.70536 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 43c10706-48b8-3b8d-a96d-e417e9840ee0 | -14.53435 | -40.84958 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| e2761949-d87d-3ca4-be36-44f8c982cc48 | -14.47228 | -40.7085 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| fc05c1d9-b082-3473-9c96-a5d5b1ba7be2 | -14.71166 | -41.02732 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 50d8248e-f934-3b38-9ee0-94455b601df8 | -14.30018 | -40.46296 | 2026-10-01 16:11:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5cef07cf-538e-3c14-818f-5b22bde22ef8 | -14.99733 | -39.7415 | 2026-10-01 16:11:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b0b07e7d-5769-3b69-ab6f-5a6e0c81fc7d | -15.72232 | -41.19374 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 3941f603-88ef-39a0-bc76-2d157cf9f091 | -13.91314 | -39.64824 | 2026-10-01 16:11:00 | NOAA-21 | IBIRATAIA | BAHIA | Brasil | 2912905 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 480fd34f-170f-31aa-9175-960d047e030b | -14.42199 | -41.20258 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 182c51c6-84a0-3f73-b116-6215a8ca2a4b | -13.95464 | -41.6754 | 2026-10-01 16:11:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 3fc75287-3667-39b4-86fe-d6b03ffb7039 | -14.32164 | -44.98991 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b75ba44f-489d-3895-b1e6-09ff5566c9f8 | -15.62704 | -49.27124 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b0643d1c-5df9-37b2-8a6e-3aff463dba75 | -15.49727 | -42.11145 | 2026-10-01 16:11:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 3fbeacce-afa8-3a1d-b6d0-67b98ef73140 | -15.37282 | -47.96024 | 2026-10-01 16:11:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 58ab39c9-a429-3cc9-923f-9e129ba68cc3 | -15.75355 | -40.84947 | 2026-10-01 16:11:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a790c611-e7a7-3974-9116-4692d34dabc0 | -14.36433 | -44.74943 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a9bb1379-bc7d-3ade-8473-f59cba2d6330 | -15.33672 | -40.84769 | 2026-10-01 16:11:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 89b9c445-9d8a-318a-917e-069ba8f1f347 | -16.11966 | -42.22107 | 2026-10-01 16:11:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 5cebb1da-0395-3da8-a88e-337234c11a0c | -14.4333 | -44.76722 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff0eafa7-460c-3768-9f54-49e36357e2e1 | -15.94829 | -45.96743 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5b430e6c-0c4a-3fe8-b6d7-11b96a2d137d | -14.6797 | -44.68695 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75f0eac1-eead-39fb-85ae-784b50c1dcec | -15.96481 | -40.52176 | 2026-10-01 16:11:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 20b8b783-c778-3791-b229-1264361c3271 | -15.65737 | -44.71701 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5bbebe5e-e0b4-37d9-b03a-adcf4b81f839 | -15.2644 | -40.90548 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e84f67b3-a171-3838-9a6b-8538e5bda2a9 | -14.86972 | -49.2165 | 2026-10-01 16:11:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| aad053c8-d62d-3a15-80b7-654f8c2fd994 | -15.21694 | -47.94295 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df6db876-6412-3427-a2bc-2f2066847d43 | -15.71082 | -40.48162 | 2026-10-01 16:11:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 61f7aa9e-9b9f-36f1-bd9a-017c10c1534d | -16.13815 | -43.74014 | 2026-10-01 16:11:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6cdef50e-eead-3be9-97a0-968c786322fb | -16.07826 | -42.6233 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 29f35b87-cd22-3543-8dbf-5fdd6f4d835b | -16.11662 | -42.22566 | 2026-10-01 16:11:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 04dc7c17-0f93-3586-9b40-34bb58e0ba4e | -16.13888 | -43.74579 | 2026-10-01 16:11:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| bffa7121-357e-39b5-a1bc-94779c12fa5d | -15.62611 | -49.26307 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 398de767-5d1a-3174-b59c-3d6824280bd9 | -14.69563 | -41.57295 | 2026-10-01 16:11:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 9b665a02-c17e-316e-9de0-d0b4c709ea8f | -13.95174 | -41.67979 | 2026-10-01 16:11:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 2371fc13-4a67-3783-9333-5ac4cfd1edbf | -15.11509 | -40.74448 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4e2c5974-35a9-3ef6-8979-ad4ff336a7ab | -14.38345 | -41.20074 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c888925d-f34d-3717-95bd-8186ab6c258f | -15.71482 | -44.96661 | 2026-10-01 16:11:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 45ddc05b-c892-3f07-b838-5b66cdd7458b | -14.96423 | -40.45485 | 2026-10-01 16:11:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f664fed2-3331-31e9-aada-061a0ed503a0 | -15.72641 | -39.82541 | 2026-10-01 16:11:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e9b7d09a-d0c0-39bf-a2fa-26a1c4fa5393 | -15.09975 | -48.40208 | 2026-10-01 16:11:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| a89a2bdd-3d7c-3551-91b7-7a10ae90f077 | -14.91405 | -39.28073 | 2026-10-01 16:11:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| fb37a7fe-c091-30e5-80cf-3a690c6068b3 | -14.65535 | -41.87667 | 2026-10-01 16:11:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3ab0a55d-b92e-3733-9900-1a04c550a274 | -16.03258 | -45.13099 | 2026-10-01 16:11:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 728d2030-f5a4-37e1-9c95-7a598ceb87aa | -14.35111 | -44.74367 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2b05b1dc-fc2c-3257-87b0-cafc2f06aade | -14.67867 | -41.30814 | 2026-10-01 16:11:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 2f4ab656-322c-3a51-b844-5ea38df125fa | -14.09988 | -40.00678 | 2026-10-01 16:11:00 | NOAA-21 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 57adbda8-8b84-381b-8ec3-c00ed0522653 | -15.32755 | -40.76045 | 2026-10-01 16:11:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 68cd2908-ea11-3b2a-99b5-25d43e488b6d | -15.95806 | -40.52284 | 2026-10-01 16:11:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1410d613-c66a-329d-80fb-7f61e503f059 | -15.24425 | -40.64897 | 2026-10-01 16:11:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5f423ce7-1543-33fb-9501-9b2f31b1388b | -14.36647 | -44.73396 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c4e3178-8055-366d-ad71-ccd6a61fa527 | -16.15075 | -42.86057 | 2026-10-01 16:11:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7cf4b2c-44e9-301e-ba04-e4eff81f57e0 | -14.63896 | -40.20568 | 2026-10-01 16:11:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 996a656b-4cb0-3d42-98e5-7cd11f11ce82 | -14.65827 | -41.02444 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 05f27997-2664-3e11-98b6-c4f287df438c | -14.39005 | -41.91215 | 2026-10-01 16:11:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 6f380813-d6e3-3012-8fbf-1c49da03d053 | -15.76274 | -43.65265 | 2026-10-01 16:11:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| df4c58b1-2db3-320c-ab36-5cc0bd346334 | -16.30089 | -45.63728 | 2026-10-01 16:11:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0c566ccc-b06c-3e99-883c-bfef18c6bf90 | -14.35423 | -44.73564 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3053b8c5-7d29-36b9-b43e-8df9329c271d | -15.95795 | -45.9711 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f2395699-2230-314c-9fbd-bb3929e83a68 | -16.02829 | -45.13154 | 2026-10-01 16:11:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9776637d-e723-3839-b9ac-fae592d9553f | -14.2953 | -39.36811 | 2026-10-01 16:11:00 | NOAA-21 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a27cefe9-3a3d-3bde-b43b-358768b34fa1 | -14.46839 | -40.70541 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| d77de788-869c-3c60-8708-719952ff7b52 | -15.24292 | -46.15576 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 31e6b7cf-599d-3b33-bc8d-3e800828c4fb | -16.0861 | -41.31578 | 2026-10-01 16:11:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 7f0d568d-d798-300f-b34f-e245cdd529d0 | -14.37251 | -44.74837 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1b8545b3-5ced-3479-888b-cb59ff606ae5 | -14.70868 | -40.62941 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2774cfae-1c3e-3602-90ec-d66cd5da7c89 | -15.76418 | -40.77857 | 2026-10-01 16:11:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README112.md)
