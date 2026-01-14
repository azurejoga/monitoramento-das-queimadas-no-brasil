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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e11c128-ec47-33de-afb8-b8da7918fed7 | -10.2117 | -36.35696 | 2026-01-14 03:42:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 94396511-3fd6-3e12-ba76-79d82c8e5d94 | -7.7431 | -35.31575 | 2026-01-14 03:42:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fbeffcf1-16e4-3b88-a046-2ba18a15af46 | -5.10298 | -43.23308 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36a4e01c-41f4-34c0-ba42-2fcdcdfbfb1d | -10.16962 | -36.55386 | 2026-01-14 03:42:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb510f57-0cb8-31d8-9ae2-69ff5bd54536 | -7.27025 | -41.03397 | 2026-01-14 03:42:00 | NPP-375D | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69730549-a93f-39eb-bf0c-1b69ea26bfc7 | -10.16895 | -42.217 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5ae9d8be-d300-3bac-867f-3e7cb5a21eaa | -7.2237 | -35.05285 | 2026-01-14 03:42:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 10af0a83-03a0-3628-b45a-7b427d867652 | -8.03488 | -35.95146 | 2026-01-14 03:42:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 032340c8-7dd4-3f95-8817-1db2e10f6e4f | -5.10233 | -43.23683 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1375409-f24b-375b-8b8e-ff6ad4df7756 | -7.01932 | -39.65363 | 2026-01-14 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f6875aa-bcc2-367d-b256-643d97d53a77 | -5.10167 | -43.24062 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a542dd6f-46b6-302b-b70e-1e1838049afc | -6.54447 | -43.09087 | 2026-01-14 03:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be1116fe-9539-3220-a207-222c86b41c18 | -10.16989 | -42.21176 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fa529658-f642-30c7-bd5c-cc904861fb36 | -11.16272 | -43.57605 | 2026-01-14 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fad9977b-02e2-34ac-97bc-cb7225bcbd4a | -7.01504 | -39.65307 | 2026-01-14 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d310cb0-b8cc-39d0-80d7-5053446c1ea3 | -7.01866 | -39.6575 | 2026-01-14 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fed7d273-b322-3bf5-b5c5-71c932957bdf | -7.25258 | -43.05574 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef385c89-5835-35e9-9251-5d441005efdd | -8.03831 | -35.95204 | 2026-01-14 03:42:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5b2bbde-81e6-3348-8e78-a82cebd0b861 | -7.4592 | -37.13147 | 2026-01-14 03:42:00 | NPP-375D | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5657bfb-defe-38e7-bcd8-3b0e79e62289 | -7.26384 | -43.05427 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 526cc24d-0e81-3d57-b91e-a137a122b1a0 | -5.10853 | -43.23427 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23da0b59-b624-3157-bc04-f234e660aeda | -6.48472 | -42.94368 | 2026-01-14 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a0a6962-c4ef-3e92-ab8d-c35a50f18378 | -10.41104 | -44.63897 | 2026-01-14 03:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14c86c84-4119-37d8-8ef1-8b93d5320200 | -7.25791 | -43.05669 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 63d8f247-e0d1-3995-9ba8-19162bf41c79 | -7.25319 | -43.05239 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 951629ee-792c-307a-9745-d3d0adba872a | -6.59831 | -44.32886 | 2026-01-14 03:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4df7c82c-45db-3b30-bb21-96a6c40faf8b | -7.22499 | -35.00188 | 2026-01-14 03:42:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87f1fd13-8565-3d05-9411-c039b497db63 | -8.64307 | -36.22882 | 2026-01-14 03:42:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2c93fb5-4f8c-3c53-b9da-fc3947ef0e21 | -9.0028 | -39.88683 | 2026-01-14 03:42:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e98b837d-ddc7-3ee8-85cb-4c8d2e81ba08 | -10.55906 | -44.3395 | 2026-01-14 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a32ee517-68c9-3b90-a743-ff3fd074f2c6 | -7.34076 | -35.10426 | 2026-01-14 03:42:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f04278d-36d1-351b-b6a3-490f9882b681 | -11.15756 | -43.5751 | 2026-01-14 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bebe960f-d148-39df-9cba-6316af5745b5 | -7.25851 | -43.05333 | 2026-01-14 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d884d3e2-711d-3270-bc59-63a70e4254a3 | -5.88815 | -39.29399 | 2026-01-14 03:42:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f226e145-09a0-3f8c-99a9-d7613aa10d5a | -5.17498 | -43.27064 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b82e0b0-4563-3928-a856-3401a5014e80 | -10.55975 | -44.33594 | 2026-01-14 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31524da0-36ef-3583-8543-ac5145561bca | -6.59245 | -44.32789 | 2026-01-14 03:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d60bbae1-2052-3f3a-a253-3e3cebcac7b9 | -5.10101 | -43.24442 | 2026-01-14 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 429015f7-322a-34fc-b803-d09edec0770c | -6.73373 | -38.95993 | 2026-01-14 03:42:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8e432b7f-3ab2-3f6b-a1cf-9d9ff4d2340a | -6.66963 | -39.67839 | 2026-01-14 03:42:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0cc2e0f8-b82e-30ae-bec1-832b1cc9c443 | -6.69416 | -39.12196 | 2026-01-14 03:42:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6543815f-5c7b-3201-b6d1-2e3242dcce9a | -6.50984 | -38.25564 | 2026-01-14 03:42:00 | NPP-375D | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acf73223-8ee8-31fd-945f-918fa8db05f4 | -5.8888 | -39.2901 | 2026-01-14 03:42:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75c4c0ae-65e9-3994-a06c-37ef021c613e | -10.21512 | -36.35753 | 2026-01-14 03:42:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a54de727-7482-3b73-9cf2-e017604b5536 | -6.66889 | -39.68273 | 2026-01-14 03:42:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 54dd2855-52bd-3ec5-9235-6fffbe7fbe24 | -10.16417 | -42.21609 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 59bb2944-583e-3b2c-8905-39d7c63edaa1 | -7.22034 | -35.05229 | 2026-01-14 03:42:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bb80517c-8538-3f8c-b827-e44fdde531be | -10.16511 | -42.21085 | 2026-01-14 03:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 23a05c5d-f7f4-31f2-94c3-6ebc5584d878 | -7.4279 | -35.27994 | 2026-01-14 03:42:00 | NPP-375D | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 49133344-6763-3f15-9d18-44e3db26d119 | -6.482 | -42.94338 | 2026-01-14 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7eee4d2-4541-352a-8889-f259b95ef939 | -7.45305 | -34.9942 | 2026-01-14 03:42:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4e59b4c-bbca-384d-8686-b3557388f6da | -7.74252 | -35.31933 | 2026-01-14 03:42:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 50c822d5-6e4d-38b4-9449-0c745690e37d | -8.5496 | -35.03641 | 2026-01-14 03:42:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e41d1e72-a14f-395f-bbad-1785d0cc9131 | -6.12138 | -39.21676 | 2026-01-14 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4f62d0f-dd8f-3c19-a47e-35a3f3c015d6 | -6.54506 | -43.08747 | 2026-01-14 03:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3ac8ab-75e1-303c-a08d-0d4d2c9ab772 | -6.12719 | -39.79699 | 2026-01-14 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d98bbae-06b3-3b70-a698-de919feaa9b3 | -7.73972 | -35.3152 | 2026-01-14 03:42:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 917f6bec-f825-3c14-a68a-8d62087bde5b | -12.11521 | -45.58783 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb2bcbe6-72f5-384e-9e04-7e1094a01bc2 | -12.11601 | -45.58152 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58871056-cc36-3023-bdef-cb85f180181e | -12.64256 | -43.96725 | 2026-01-14 03:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be97714b-2f8f-3192-a140-d82f247d526c | -12.08701 | -43.76527 | 2026-01-14 03:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 981b86f3-7488-3d66-ac23-64de8bf83e41 | -11.85169 | -43.72744 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd7ad63c-966c-36dc-a426-d1ffd45db28e | -12.21177 | -38.98069 | 2026-01-14 03:44:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7fa253b2-820d-3456-a2d8-5a46d4ae3d19 | -11.85109 | -43.73054 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65ad5102-5e9f-3d0e-9c28-ae815893631b | -12.08315 | -45.56824 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45ae4988-ec9f-32cc-8728-8cd0965e7f5e | -12.64193 | -43.97043 | 2026-01-14 03:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3907451f-18af-3ece-8749-a9ecd374e4f0 | -11.85347 | -43.71818 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b434a53-2974-3a90-a610-65ce69805991 | -11.85228 | -43.72436 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| add83cb7-7108-38c8-913a-503a15c3e444 | -12.11681 | -45.57958 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82a13620-d0d3-3cc7-9179-6143a5ea9f86 | -11.85623 | -43.73154 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7fb79c-6d56-3c62-a9c9-00857df14570 | -12.16489 | -44.33845 | 2026-01-14 03:44:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 500e87ce-e67b-31d5-bead-2a541c252595 | -12.11518 | -45.58562 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee7a36c8-1976-3fb0-8003-376b85099475 | -12.08643 | -43.76829 | 2026-01-14 03:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d89d3fa3-4a2e-36d3-9f8b-4b9419e29606 | -12.09158 | -43.76919 | 2026-01-14 03:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e7ab84-1a27-3b13-91b8-ea62f6c06db2 | -12.09103 | -43.77204 | 2026-01-14 03:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5da1179b-c0fb-3b59-bb36-a57d44e03c1f | -12.16422 | -44.34187 | 2026-01-14 03:44:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4033962-2b3a-3ced-aaf1-5a89848d3d4b | -11.16399 | -44.85213 | 2026-01-14 03:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bbab455-a389-3e89-b50c-b413e00c40ba | -11.85288 | -43.72127 | 2026-01-14 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e53da87-177f-3935-b428-d63e5c7e7db6 | -12.11601 | -45.5837 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc1cd19c-d4b7-3ef6-9570-4c4b07c5112b | -12.10947 | -45.58657 | 2026-01-14 03:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a10c8081-e084-35ca-8fa4-008a77aba76d | -20.30562 | -41.6247 | 2026-01-14 03:46:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9aec0ac5-451b-3068-888e-7da8456708ed | -12.8468 | -52.5216 | 2026-01-14 03:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ee950067-c41e-3358-a958-47494a96c470 | -5.099 | -43.2444 | 2026-01-14 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a0c278d8-83c4-3c46-b29c-172bf2e4a40d | -12.8468 | -52.5216 | 2026-01-14 04:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9c808f15-08b0-3387-b709-167e60fd8948 | -6.42055 | -39.2526 | 2026-01-14 04:01:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 396b18d8-e857-35fe-aa8e-435e8553dc4e | -6.67079 | -39.64954 | 2026-01-14 04:01:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42c1c1d2-1b88-35cf-994d-e9ebee406caf | -6.20504 | -39.73959 | 2026-01-14 04:01:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66351d6c-54fd-347a-bfbb-a9ba77522c93 | -6.67024 | -39.65303 | 2026-01-14 04:01:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26da1770-246b-3774-8ec8-45913d8374be | -5.52169 | -38.92201 | 2026-01-14 04:01:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53e28ca8-95cf-3870-8035-a358dfbb36c7 | -5.09752 | -43.23447 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 32997dd8-7b6a-3de0-ab20-42ee133bccce | -5.28744 | -45.8254 | 2026-01-14 04:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8226232-5050-3d37-a988-1e3fdff9d8f7 | -6.69561 | -39.12275 | 2026-01-14 04:01:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 168c1114-d59b-3d46-99de-e3c4fb24a581 | -4.66052 | -40.41959 | 2026-01-14 04:01:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f156e44b-b8d0-3ada-a195-0d8d7e847b03 | -7.25531 | -43.05545 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2af02764-dd94-392a-a89e-c62a15831aba | -7.24756 | -43.05831 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2df965cf-a0e5-357b-b1ad-3034fd06ec55 | -5.10345 | -43.24438 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9d121cb-e057-381a-9957-76d9d421a2a9 | -7.45686 | -37.13497 | 2026-01-14 04:01:00 | NOAA-20 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 339d6f4e-23b5-3f34-8554-ecabfb112e9d | -5.4453 | -40.86739 | 2026-01-14 04:01:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32405945-4224-31d5-bd13-16aa80585d39 | -5.10415 | -43.24005 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89a6ac4e-800e-3df7-a0bc-cfd4ed933706 | -8.03619 | -35.94955 | 2026-01-14 04:01:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
