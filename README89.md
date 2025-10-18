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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f80ebe8e-0723-36f6-8fb5-9f731436c841 | -8.5759 | -45.44239 | 2025-10-18 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0bc5e223-ce07-3773-b5b1-e46802b54570 | -10.49693 | -43.42481 | 2025-10-18 11:38:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 93fc8470-0b4c-3524-844a-29f4122b6e68 | -8.24666 | -44.00268 | 2025-10-18 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 18ae84a8-9b83-37cd-b80e-da3dfbac3718 | -6.40499 | -41.47925 | 2025-10-18 11:38:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 37df1404-fec6-323a-80e5-593f439927bb | -7.68322 | -39.82721 | 2025-10-18 11:38:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| afd5a38c-b5b6-39d6-93e2-01acec9c6c3a | -6.41168 | -41.50625 | 2025-10-18 11:38:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| cf773820-73bc-34c0-ae8a-231e95791569 | -8.56675 | -45.45829 | 2025-10-18 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c68d4654-4df7-3226-9e00-0654cef5f236 | -11.9332 | -38.32552 | 2025-10-18 11:38:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 6068fe98-126f-356d-aba9-ef304472adb5 | -7.1687 | -42.37868 | 2025-10-18 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| cf6daa55-458f-319c-bc1b-25b3628f6a3c | -6.41691 | -41.51365 | 2025-10-18 11:38:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0c5055df-cdbb-3085-9f45-18135ad797bf | -7.76582 | -42.47019 | 2025-10-18 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 04e02e40-64cb-325c-bcb3-25116deeeed6 | -8.19839 | -43.30881 | 2025-10-18 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| ddba1a64-82f1-300f-a600-b6c5416a2c9f | -7.76356 | -42.48462 | 2025-10-18 11:38:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 34cdacc3-6408-358d-b15c-0cff7955fca7 | -9.35694 | -46.89636 | 2025-10-18 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b2eb094b-1062-36a7-86af-01e2434737e8 | -8.36147 | -46.26186 | 2025-10-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6e5b02b6-8293-30e7-a23b-e5b138acf05c | -10.23644 | -44.05132 | 2025-10-18 11:38:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 4c5eb5bd-def8-36b0-b573-4c0df19abbdf | -8.3663 | -46.23864 | 2025-10-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 49f8fabc-ec8c-349c-ab80-2aabb637bfc8 | -6.31977 | -40.947 | 2025-10-18 11:38:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 54d6774e-2790-302a-81ac-fc60bd75f63d | -7.83205 | -44.1179 | 2025-10-18 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2fb0f29c-e13e-39b8-852f-84c61881c420 | -7.18817 | -42.17853 | 2025-10-18 11:38:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| c7b18239-ed81-3775-ba65-740703028c71 | -8.36618 | -46.23224 | 2025-10-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 443cbe83-6faf-3a64-a539-8fd05cd654f4 | -6.40978 | -41.51907 | 2025-10-18 11:38:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 6c590025-6910-3ac7-a163-9b2272eecd27 | -7.87921 | -38.92805 | 2025-10-18 11:38:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d57232ec-52ac-3c73-8f93-7675b1dde1eb | -6.61898 | -35.34572 | 2025-10-18 11:38:00 | TERRA_M-M | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a932a2ce-88b5-3e30-bae2-4341f29cdf40 | -8.57117 | -44.59512 | 2025-10-18 11:38:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9985ca91-fe9e-3eb6-96d5-6afebb1fcdc4 | -10.69653 | -44.5496 | 2025-10-18 11:38:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 01167509-4beb-3f4f-8537-c10710db5f6d | -7.18602 | -42.1925 | 2025-10-18 11:38:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 669c1e1b-f328-39a4-af0d-336c6cb769dc | -8.2343 | -44.00063 | 2025-10-18 11:38:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| c66bed29-a9ab-3e76-ba82-d9abd88b2c42 | -11.42987 | -38.43251 | 2025-10-18 11:38:00 | TERRA_M-M | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 30be3359-0fe6-3f17-921d-4b43339e3d14 | -8.32173 | -43.41778 | 2025-10-18 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 506d6c17-7130-359b-a99c-7f2a52bb41f4 | -8.57197 | -45.46606 | 2025-10-18 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 876bc075-6f33-3ec6-bc2f-0cb587590bbc | -7.17092 | -42.36418 | 2025-10-18 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| f68b2035-800c-3e16-b267-e2d679f5a149 | -5.88777 | -38.59935 | 2025-10-18 11:38:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 88fd5aea-2285-35c6-970b-405e939fc6f4 | -13.9132 | -45.5576 | 2025-10-18 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 43312a86-8ff6-3df4-a148-cf2f234fe301 | -13.8573 | -43.6193 | 2025-10-18 11:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dcadee6a-819f-3e95-bc7d-8591a087d0f1 | -11.19731 | -44.22815 | 2025-10-18 11:40:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d9e2668e-d2d2-3970-8376-abcdfd684977 | -12.16322 | -45.07948 | 2025-10-18 11:40:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| fa1fcdeb-7cd2-3fa1-9b8b-cad6d8a9f174 | -13.69884 | -42.17739 | 2025-10-18 11:40:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ea73f7f0-8740-3faa-b33c-9363c82724ea | -13.85479 | -43.6409 | 2025-10-18 11:40:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5e30f6c3-a7cd-3425-863d-db8f2aff7df7 | -11.38241 | -45.26031 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 39e87164-fe8e-3b1d-a406-b48d9430d30f | -13.98539 | -41.44324 | 2025-10-18 11:40:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bb0cfd59-9c22-3b11-85e3-4041ddf8ec18 | -11.77894 | -42.05973 | 2025-10-18 11:40:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 82137828-43fe-32bb-8e23-36f3d112bab8 | -13.9619 | -41.47138 | 2025-10-18 11:40:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e840dbda-df48-3687-9dc2-c1d281dbe6b3 | -12.49359 | -45.46492 | 2025-10-18 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| c5acc352-6985-3a30-90f4-fccd9dfded25 | -13.81355 | -42.88731 | 2025-10-18 11:40:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 78006608-7fb5-3b14-8e5b-b76f398bdad5 | -14.89751 | -41.32819 | 2025-10-18 11:40:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e2017b9b-a855-3b73-ab0f-aba3cc9d5b05 | -14.09793 | -43.62279 | 2025-10-18 11:40:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f7812309-bab2-3397-92a1-c844f55733bc | -11.3789 | -45.28122 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 12365311-5af1-34cb-bc5b-80774630b3b2 | -12.16005 | -45.09842 | 2025-10-18 11:40:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 20ccb2ae-87c6-3c18-ae67-995181649659 | -11.58442 | -44.04277 | 2025-10-18 11:40:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0628369f-bd3f-3676-aafb-2a3caee672ea | -11.61411 | -44.08139 | 2025-10-18 11:40:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f2be3683-e88f-3316-b9ec-a578abb76f4b | -15.62336 | -39.72831 | 2025-10-18 11:40:00 | TERRA_M-M | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 09d8a65b-abf5-38c5-bbd2-9b2c1ef106ac | -12.48072 | -45.46293 | 2025-10-18 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 57a518eb-f51e-3e0a-85db-dc784e7b3dbf | -12.46787 | -45.46084 | 2025-10-18 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ecf1f756-b1cd-397a-aebe-d494bfa98bac | -10.96536 | -45.46811 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 427b644c-77e8-32ce-8877-266641f86380 | -11.36013 | -44.28536 | 2025-10-18 11:40:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c514dd26-f35c-3c2f-974a-326cab0e109f | -11.61677 | -44.06491 | 2025-10-18 11:40:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 107bed15-89c1-3c60-987e-b4ce1b53820f | -11.37136 | -45.25166 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e8f4d70a-60f2-3eac-a71b-969cb2a9e7e9 | -13.32436 | -41.60505 | 2025-10-18 11:40:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e3c73d9f-521b-3d8a-b116-2eb4464711b7 | -13.36207 | -40.05098 | 2025-10-18 11:40:00 | TERRA_M-M | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7333c14a-46ba-355a-9b66-96d232576ab0 | -14.71435 | -41.25602 | 2025-10-18 11:40:00 | TERRA_M-M | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9aa13d05-6d7a-3f84-bebc-72661973f917 | -14.5818 | -41.86529 | 2025-10-18 11:40:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7df7e22a-a957-3537-8d1c-f08c640d55ee | -11.9624 | -45.33516 | 2025-10-18 11:40:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 602cf945-86a9-3cdd-8735-8897f6412cdd | -12.87996 | -42.17267 | 2025-10-18 11:40:00 | TERRA_M-M | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| dd32556b-6c12-324e-b0ec-720b26bb633a | -13.60821 | -41.55928 | 2025-10-18 11:40:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 448aae3b-63e3-362f-94df-36642a347499 | -11.36947 | -45.25842 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 9d400556-775a-3d7e-bac3-4f36a6f7f0d0 | -15.01038 | -40.82544 | 2025-10-18 11:40:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 9ef3446c-71b4-311c-8e02-a104dfbbe15b | -13.19822 | -46.41526 | 2025-10-18 11:40:00 | TERRA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1aa040f9-cb4f-3e04-8e24-a39132a034ec | -11.95896 | -45.35593 | 2025-10-18 11:40:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b8419dc9-c8bc-396a-b897-a0324fedbe10 | -13.29665 | -42.5871 | 2025-10-18 11:40:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f72d58e5-773a-3753-8fd1-513225195d63 | -14.03576 | -44.70087 | 2025-10-18 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 5f0043fe-8c08-39ce-8475-ab9a40784a20 | -11.77802 | -42.06566 | 2025-10-18 11:40:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c8dacc6c-bf76-3ee3-b248-f6c5129fd6b8 | -12.07963 | -42.75791 | 2025-10-18 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 96a3d505-9db2-3658-a9aa-3f3b5077479c | -14.44883 | -41.90916 | 2025-10-18 11:40:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 4b28488e-f6af-3f13-995e-e493129ba39d | -11.36796 | -45.27274 | 2025-10-18 11:40:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e9d41d94-485e-33ee-b520-d7c42be4977d | -13.54809 | -41.57166 | 2025-10-18 11:40:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1fc75895-3662-3836-806f-99e61ad8a41d | -13.70134 | -42.17287 | 2025-10-18 11:40:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 274d5a96-884f-3f34-ae8b-5484f5bff1a2 | -13.90324 | -45.54707 | 2025-10-18 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 48220ec3-b4a0-321e-87ae-93c10790db9f | -13.60978 | -41.54892 | 2025-10-18 11:40:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ee0e704e-0395-31a1-b833-d5f88077afc9 | -13.87868 | -43.26055 | 2025-10-18 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| d951febb-b03c-353f-a91e-640dfa3d2734 | -12.49018 | -45.48537 | 2025-10-18 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 834e3bbc-9d59-3f14-ac8c-56f5977c4bc6 | -14.89447 | -41.34816 | 2025-10-18 11:40:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 29e22d5a-9358-399d-aeef-551e585a692d | -13.96034 | -41.48165 | 2025-10-18 11:40:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 8c35bc13-4feb-3ede-90b6-102d9b774276 | -14.09571 | -43.6367 | 2025-10-18 11:40:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 25735475-a153-34bd-9633-8161a5f49d01 | -13.03618 | -43.56342 | 2025-10-18 11:40:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 51c284f6-0e0e-3b5e-858d-b5de6bb1a331 | -18.40341 | -41.83274 | 2025-10-18 11:42:00 | TERRA_M-M | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| dff8ec4a-82ea-3b79-bb00-0d5a1b19eab3 | -18.02641 | -42.19015 | 2025-10-18 11:42:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 2c4399c1-0bc4-3d2c-b72d-e603bdeaf93a | -15.78356 | -41.32712 | 2025-10-18 11:42:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4dd6c6cf-9636-3773-9d73-8eb772244aff | -15.57693 | -43.5445 | 2025-10-18 11:42:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 74841b85-8a57-3465-93c4-363cb6825fac | -16.97275 | -42.31078 | 2025-10-18 11:42:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| aabaeca8-8d5d-34e7-ab4f-840741462651 | -15.82288 | -42.51294 | 2025-10-18 11:42:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6c1eef4f-a37d-3e42-aa32-11f7b7ac39bb | -16.9711 | -42.32138 | 2025-10-18 11:42:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 9a03bc34-e31c-3ab8-8dbf-5b796d34255d | -18.02481 | -42.20061 | 2025-10-18 11:42:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 88302ee2-4334-3b33-bb73-bfa9ef1434e4 | -17.84106 | -42.60453 | 2025-10-18 11:42:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e77f38e9-3785-338c-98c4-72f699ea1b73 | -17.83936 | -42.61536 | 2025-10-18 11:42:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 1b82ece5-0068-3990-b00b-917a500dffa6 | -18.09426 | -42.44871 | 2025-10-18 11:42:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| d40bce46-1e3d-3934-b873-3c74bec1ecdb | -18.42498 | -40.45107 | 2025-10-18 11:42:00 | TERRA_M-M | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 47f9bd9d-f01e-3d3a-a1c0-db7d4a384028 | -18.93515 | -39.84348 | 2025-10-18 11:42:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 73fda1d9-e765-304d-a7dc-796f8b401212 | -18.25665 | -41.64486 | 2025-10-18 11:42:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 988c3bc9-e4fe-3783-897d-95d1d2012ec3 | -19.40519 | -40.62568 | 2025-10-18 11:42:00 | TERRA_M-M | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |


[Clique aqui para ver as próximas entradas](README90.md)
