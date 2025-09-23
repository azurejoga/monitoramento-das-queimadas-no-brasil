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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10bfe14e-f263-38b3-9186-5b320fd78f6a | -8.37196 | -38.65302 | 2025-09-23 11:36:00 | TERRA_M-M | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 39fe4dff-1188-30a8-8a43-32c0fea6170c | -7.4346 | -39.13219 | 2025-09-23 11:36:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 86397d48-3ec0-322c-8fe8-cc3163f9ff69 | -7.35491 | -38.85515 | 2025-09-23 11:36:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 39b6fdf7-ebfd-3b9e-b6cb-cd5ccd3c8c65 | -7.44795 | -39.94712 | 2025-09-23 11:36:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c3b57221-fd5b-3f0e-9c35-1107479b9936 | -5.05636 | -37.03657 | 2025-09-23 11:36:00 | TERRA_M-M | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c04ef9e9-f62d-39e8-b2e1-12b443d014bc | -7.91848 | -40.01708 | 2025-09-23 11:36:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 8ad9d80a-d291-3b3d-a803-95b49d6bc3a7 | -7.46587 | -41.83539 | 2025-09-23 11:36:00 | TERRA_M-M | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 2ee2a978-3290-3d66-b49b-548977a6db1a | -7.97947 | -37.99511 | 2025-09-23 11:36:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dd98a17b-e519-331a-b5b6-2152f61b2e15 | -8.53396 | -44.94339 | 2025-09-23 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 8e9db816-45e7-3357-afb0-1a09e3a082fd | -13.95876 | -42.4933 | 2025-09-23 11:38:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 2c9bcae5-741d-3af8-a122-969266a0c00b | -14.24419 | -42.19996 | 2025-09-23 11:38:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d0a35d5e-d5c1-3e7b-bd96-e738620e3f5e | -11.51288 | -42.6927 | 2025-09-23 11:38:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| e5d34ebe-cb2a-32fb-8c77-f2eaf80ee7fb | -10.3088 | -45.23677 | 2025-09-23 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a5e83227-49c6-3eed-a00a-c9eb5f4b1871 | -11.2247 | -39.07615 | 2025-09-23 11:38:00 | TERRA_M-M | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7838b9d4-d057-34d9-b2a1-2176a6c0472c | -9.61851 | -37.12356 | 2025-09-23 11:38:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 81e58763-28d9-358b-8b87-fab36f589531 | -13.28911 | -42.4017 | 2025-09-23 11:38:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c14e7da1-75c7-3e71-9167-306567eac968 | -9.20897 | -41.02185 | 2025-09-23 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fbade906-d74c-3175-bc9f-0de4693b5067 | -14.62803 | -42.17383 | 2025-09-23 11:38:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| b2094d54-8bac-35d2-8514-69dba2d4fdf3 | -10.30398 | -45.23016 | 2025-09-23 11:38:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| db32ace0-1d72-3afd-a357-747f34c984d7 | -8.80801 | -37.11639 | 2025-09-23 11:38:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a7df86e1-301b-32c3-b9b1-cc85bb2fd46c | -13.86444 | -42.70636 | 2025-09-23 11:38:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| e48e588b-59c2-31e0-a9b8-ae48cf16ce75 | -12.70414 | -42.39211 | 2025-09-23 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 8c0757d3-809b-3299-a30c-1740c022e093 | -11.91285 | -43.42637 | 2025-09-23 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c6d1fd60-f3ab-3eb7-ad9d-0220d0c7f546 | -9.19065 | -44.6079 | 2025-09-23 11:38:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 90ad184b-0b4b-31e6-ba9d-e376b3d7c0f9 | -14.25084 | -42.29145 | 2025-09-23 11:38:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 166d81f1-4bd5-3421-ac49-463aa5f83587 | -9.0864 | -40.03021 | 2025-09-23 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 67bd1ea3-7af0-391a-8d0e-95ece1e0577e | -12.91242 | -43.16719 | 2025-09-23 11:38:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 60280f8c-9d39-3530-b75d-8001d845a0e5 | -13.48169 | -41.57334 | 2025-09-23 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 35.1 |
| d460f0bc-9332-3781-b4b7-835dffb455bc | -9.19366 | -44.62423 | 2025-09-23 11:38:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4bbd951d-f1ce-39dd-a641-c1c564cca97c | -8.51589 | -44.9649 | 2025-09-23 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 331cbe47-235f-3de9-b37d-3ec54c926e4b | -12.21735 | -43.04712 | 2025-09-23 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| a72c69e9-489c-337a-b1e3-113299f0533d | -12.26463 | -43.10897 | 2025-09-23 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 6e1d2bb4-d0f6-3f22-a17d-5871d1786a37 | -13.76052 | -42.14025 | 2025-09-23 11:38:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 8494676a-73bc-371d-955a-e34b098fc195 | -12.93541 | -42.58282 | 2025-09-23 11:38:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5bf0c8bd-fbf9-3a06-93a9-5aaa3945a928 | -13.0453 | -42.06015 | 2025-09-23 11:38:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b259b476-a31f-3eb2-842e-8f5f4dc0e1cf | -11.51051 | -42.70774 | 2025-09-23 11:38:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 6d4fe4cd-d574-30a5-95bd-3815ae847c93 | -8.19609 | -42.54492 | 2025-09-23 11:38:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 486930d5-b776-38a2-9adb-8082065ce326 | -12.77879 | -42.33519 | 2025-09-23 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 186e7462-befa-3ea9-b90f-3197a734d502 | -8.28526 | -44.38769 | 2025-09-23 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 699d2fcd-2475-3a98-ae84-666fbff500ec | -7.88438 | -44.01993 | 2025-09-23 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 036631f8-4715-3064-bdb4-747ed917024e | -13.76255 | -42.12766 | 2025-09-23 11:38:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 245e445d-dfc7-3bf7-8192-96f68b6ad340 | -12.04085 | -43.35361 | 2025-09-23 11:38:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 17df2fd7-2f13-350b-b014-6b243857e18a | -14.29419 | -43.80103 | 2025-09-23 11:38:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 222a9a1b-7dcd-3557-9df0-7432777d82fb | -12.78496 | -42.32846 | 2025-09-23 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| eefc6ac0-e915-3e50-8f55-06ce4ead6a41 | -11.65352 | -44.35942 | 2025-09-23 11:38:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| df9d2c98-1757-3f25-b1c1-0a38d8ef168c | -13.95421 | -42.48598 | 2025-09-23 11:38:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 8676ee72-21ab-33e4-aff5-7b49eec4a9cd | -12.78277 | -42.34185 | 2025-09-23 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 9776bf94-1223-3097-a69d-e3655786bf5b | -9.18695 | -44.62994 | 2025-09-23 11:38:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 5f92b36a-b920-3f1f-a948-c71485c0471a | -9.082 | -40.0345 | 2025-09-23 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.3 |
| c9ff01d8-d20f-3134-ac74-661431e5b95c | -8.39611 | -39.9093 | 2025-09-23 11:38:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 5b6f6f66-b726-3778-85c5-e2658a13a368 | -12.21809 | -43.03714 | 2025-09-23 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 8053dc12-72dd-331b-bd1c-4155d9fa6724 | -11.52277 | -43.63226 | 2025-09-23 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 05aa1fc0-870b-3c5d-9349-f27e45f26299 | -12.9149 | -43.15171 | 2025-09-23 11:38:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| dc289f10-24f4-3e10-af38-aceb417fe964 | -13.61778 | -41.5536 | 2025-09-23 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 6e2c389b-870b-334c-95fa-9f0f43678c4e | -13.616 | -41.56503 | 2025-09-23 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7b4f5b82-353d-370f-8c4e-1c1dd9fe6291 | -8.2803 | -44.3801 | 2025-09-23 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| ffc78283-954b-382e-a744-e0873298dd0d | -8.5179 | -44.9749 | 2025-09-23 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 56b9be0e-7dfc-3832-ab67-38eeeafccaca | -8.5179 | -44.9749 | 2025-09-23 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 04fae2ba-32fc-3738-bd88-16fade9cfb28 | -8.2803 | -44.3801 | 2025-09-23 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 71eff7cd-7249-3905-bf14-5d0d84b475c4 | -8.8609 | -46.1625 | 2025-09-23 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 487d5e28-c3f9-351d-84df-a8cbd989427c | -8.5179 | -44.9749 | 2025-09-23 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| fb0bfda9-f325-33ef-b9a1-a7221b87d0c3 | -10.9519 | -45.7324 | 2025-09-23 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 105cc6ea-7188-3fa7-a9ab-9c289821a1cf | -10.9519 | -45.7324 | 2025-09-23 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 268.7 |
| 325ea24c-9685-3290-94ca-5809ddfce23c | -10.313 | -45.2219 | 2025-09-23 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 960e500b-e9a0-369b-b60c-31c48c1eb9a6 | -8.8609 | -46.1625 | 2025-09-23 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 3b696cc5-7c41-3387-9fab-dde943202acd | -8.2803 | -44.3801 | 2025-09-23 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 70985ac5-1bdc-35a6-a9bc-e522631f2586 | -8.5182 | -44.952 | 2025-09-23 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2d962250-0169-3e3a-a69f-d1db06ccfcd6 | -10.3188 | -46.0859 | 2025-09-23 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f451eb62-0de3-3bd0-9a89-1668d4c70b09 | -8.8798 | -46.1605 | 2025-09-23 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 561eb023-445a-3394-9270-58540726f5f8 | -8.5179 | -44.9749 | 2025-09-23 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ace7cb22-7f19-37e1-8bfd-6790ebe6df8f | -10.3382 | -46.0609 | 2025-09-23 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 574ccb5a-ad4c-38b9-b1ba-43b0f329cc11 | -9.1671 | -43.1588 | 2025-09-23 12:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 27ac700b-0a7d-34f3-9d84-9d1502221b89 | -10.3572 | -46.0585 | 2025-09-23 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 16520b4c-352d-3b45-9eb2-f88a6ab175b1 | -10.3127 | -45.2449 | 2025-09-23 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5e8a518a-eb48-3158-8d94-12331f1399fd | -5.678 | -41.3987 | 2025-09-23 12:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 9e9f29bd-1e63-38f2-8355-44bb578e25b2 | -8.2803 | -44.3801 | 2025-09-23 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 60fca77a-be49-3080-a085-db3a3682d062 | -9.1671 | -43.1588 | 2025-09-23 12:20:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 4c999365-27a0-3071-9d7b-1a152b5a75d6 | -8.5182 | -44.952 | 2025-09-23 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 74ab8f68-220e-373c-83ca-ac995657fad4 | -8.5179 | -44.9749 | 2025-09-23 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 4c805dab-4e0c-38dc-8a55-349052cc165d | -8.5179 | -44.9749 | 2025-09-23 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c79e17f5-ebe6-3aba-812f-d9b1e26581cb | -10.9519 | -45.7324 | 2025-09-23 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 391.3 |
| 4020717e-5041-3461-8648-bc0159c355dd | -8.5182 | -44.952 | 2025-09-23 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1ddadc42-fac4-3c83-bea0-43c9b598d4d3 | -9.1671 | -43.1588 | 2025-09-23 12:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 477d9ac1-4747-3543-a803-3355543177cf | -10.313 | -45.2219 | 2025-09-23 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| fb6720bc-6367-3511-8986-a7c4280cc9b8 | -11.5229 | -43.6344 | 2025-09-23 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1aa6211a-2754-3124-b306-af43ff9539b5 | -9.1671 | -43.1588 | 2025-09-23 12:40:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| c824a636-b3e7-398b-acc6-61fda3b31819 | -11.9108 | -43.4081 | 2025-09-23 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 61661ed5-561f-3842-affa-1ee766eca104 | -11.9296 | -43.4288 | 2025-09-23 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 651cf463-e1e6-3231-a866-466d1df81b74 | -11.5229 | -43.6344 | 2025-09-23 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9a3ec905-e63d-3113-ac60-43fb2caa14cc | -11.9104 | -43.4319 | 2025-09-23 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 61b9e189-c84f-3fc0-aa47-a0ebb4b9af80 | -8.5179 | -44.9749 | 2025-09-23 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3f1922df-3d80-3bd4-bac9-c81d27a2e765 | -11.9301 | -43.405 | 2025-09-23 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c7ba54ae-9e54-39e4-97e2-8d1249e731d0 | -11.9104 | -43.4319 | 2025-09-23 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 69ac1f47-ac8d-3ce4-91e1-ce715906f1f5 | -5.678 | -41.3987 | 2025-09-23 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 7621f948-7aa7-3a12-a23d-2c224e30af96 | -11.5233 | -43.6107 | 2025-09-23 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 853c9364-fd2d-3a9d-b30e-e2bad2361671 | -4.5192 | -55.7589 | 2025-09-23 12:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 65e04d68-447c-32c9-9476-058bf1f2c87d | -7.3493 | -38.859 | 2025-09-23 12:50:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 91.3 |
| c3e46e2d-7029-3fff-91d4-d01b4a44f878 | -11.9301 | -43.405 | 2025-09-23 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 1030fb4b-62c7-3991-9d75-9f2f3760cff8 | -11.9108 | -43.4081 | 2025-09-23 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e4a41355-d8c3-3666-a5d2-352d72cb72c0 | -8.5179 | -44.9749 | 2025-09-23 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |


[Clique aqui para ver as próximas entradas](README28.md)
