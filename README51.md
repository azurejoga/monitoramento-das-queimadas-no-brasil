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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6712630-354d-33bf-b0b0-05847bdac0db | -14.60888 | -54.54307 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38f0ed30-5ea0-321f-b4ea-30907b4cb181 | -20.26226 | -46.02002 | 2025-08-31 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9991dcd0-b890-3940-9f61-084579a97473 | -17.61281 | -52.6876 | 2025-08-31 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ac6929f-35b9-3d38-b446-f6082af276a5 | -14.79941 | -59.72325 | 2025-08-31 04:32:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac9027e9-c00f-3b08-96fd-3319f09f5333 | -20.26351 | -46.01109 | 2025-08-31 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 545106db-8ff1-3cf0-9035-3278a083883d | -22.692 | -46.85245 | 2025-08-31 04:32:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3af4f16f-2e4b-333f-8f67-1e2018439ef9 | -15.71244 | -48.95627 | 2025-08-31 04:32:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c61df458-a3d7-341e-97d8-3829b751d366 | -20.55047 | -56.25893 | 2025-08-31 04:32:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d8961cc-c1f3-3195-88ed-6e78c9e165c4 | -16.21923 | -52.65631 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c57cad6d-dfda-3c8e-99cd-cde292e1b96d | -18.05302 | -45.94957 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeca480d-ccf0-3aea-9ca8-66f923cf2283 | -17.2007 | -46.99171 | 2025-08-31 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da188aff-4c10-319b-95b1-872d98f14ba5 | -16.9917 | -49.33057 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9490d62f-028f-3728-85f5-39e7d914aca5 | -15.30052 | -52.80063 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37373d97-cd33-3eb6-a258-20655eb2fd66 | -18.44284 | -47.23164 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de2a7957-31f4-3d02-abbe-e178f9694a8c | -17.62239 | -44.25708 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e29fa6c4-4e45-32a3-bb68-84d74e200687 | -16.21544 | -52.65559 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2ccd211b-79a8-32ed-8fad-a083f10070a0 | -14.60417 | -54.51969 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b33a73-d5da-343a-9b1d-e0752b5e7022 | -22.278 | -49.06586 | 2025-08-31 04:32:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90a7697e-0fd5-30dc-b00b-d7bd5a3d7aa9 | -18.66041 | -49.0923 | 2025-08-31 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7c90fb6-2386-3b8c-8158-6cd780ce3723 | -16.99898 | -49.32808 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdd656ab-f77d-3625-a8df-01001064a2e2 | -18.04945 | -45.94896 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dca6089-87ae-30e6-a439-d5229e5bc97a | -17.15173 | -46.08028 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b129941-0388-32e6-8ea2-5f7278c86275 | -16.97378 | -49.3009 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7a9104-a068-39d2-a4fc-cac4928ecffe | -14.59244 | -54.55805 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f101cd9-b349-3e77-b3cd-570cd2943fa6 | -15.23188 | -56.07707 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f387e1ce-653b-3e8a-bc82-fcb32fda504c | -16.22303 | -52.65705 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ed77d4-bcc7-39c0-87dd-88fed183176e | -21.01424 | -47.12644 | 2025-08-31 04:32:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| e16488ca-c066-3553-be01-4ae71cf22e15 | -21.01016 | -47.12995 | 2025-08-31 04:32:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 3abc9b39-be87-3e5c-b980-66b36cbd2a2a | -14.59684 | -54.55883 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8aa5a1d3-3c3a-33af-bf3b-cf570418dad1 | -18.05599 | -45.95442 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d9bb3f-0ff2-3926-806a-f23652653911 | -18.56701 | -45.37097 | 2025-08-31 04:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43cbb0ec-a1ba-3db1-a0fe-f22485e0fd74 | -16.22374 | -52.69689 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| faac3c6d-d711-3028-9ff8-1c467caaf879 | -16.40878 | -45.64918 | 2025-08-31 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b4a8d42-efac-3860-8e71-ad2ce95378c3 | -14.605 | -54.51526 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db30e7b1-9299-353b-9ffe-e7af216b5475 | -16.98145 | -49.31725 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9600f2b-4abd-3c97-af96-85e338fbc459 | -17.49966 | -45.17653 | 2025-08-31 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03b67a1c-56af-31ec-b5ab-fc3efcfba91d | -14.79819 | -59.72907 | 2025-08-31 04:32:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c42c73-6375-37b2-8b1a-0310c578b076 | -18.43828 | -47.23878 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a34c74c-3afd-3ae5-b621-c1eec8413209 | -17.15934 | -46.07753 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ac58d04-e46e-3631-8ad1-c5fcd179638b | -15.21589 | -56.06464 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1e5ea82-0804-378f-b78e-45f1f9241fdb | -15.22909 | -56.07375 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1282ffa8-f98d-3131-af32-8f14bc618e7f | -22.38263 | -46.96928 | 2025-08-31 04:32:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35f1a66a-9a05-3047-9c1d-c3f68925a130 | -16.22082 | -52.69122 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 72a8bc6f-63bb-3773-a6de-e6ce80146af3 | -16.97811 | -49.31668 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee9fd25d-292a-37a6-8bd1-725acb529c70 | -17.15526 | -46.08083 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b462e03-2fde-3f06-90d8-ceb161d7cfef | -18.06077 | -45.94643 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11ecd53c-023c-3c52-b654-61b181d2710e | -17.86203 | -44.30758 | 2025-08-31 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6745f3ba-0d75-3a22-86c6-751904e1e1ed | -16.77174 | -50.30397 | 2025-08-31 04:32:00 | NPP-375D | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea4b63c8-6194-3b77-a5ee-3bcfded88e90 | -20.55398 | -56.26433 | 2025-08-31 04:32:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98e4e09c-2b09-3589-ae01-9abf26eb015a | -16.33462 | -51.6028 | 2025-08-31 04:32:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de172c55-316f-3297-aa83-e462d126f156 | -18.1166 | -45.01377 | 2025-08-31 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d297d2c-485e-3a91-ae85-039bc98b576c | -16.22009 | -52.65157 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e5c295fb-df9d-3d7e-b556-f527939c4e21 | -16.96499 | -49.7485 | 2025-08-31 04:32:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04549fab-6be5-3e0b-8018-679acad7fd28 | -16.16123 | -45.84475 | 2025-08-31 04:32:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 564981f3-0860-3e37-b525-71a0153af8ba | -16.23907 | -52.65529 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c029c12-b1d4-39a3-a68e-17923f53db11 | -16.96163 | -49.74791 | 2025-08-31 04:32:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ce2b999-3eb1-3a62-b3f8-4248a9de0c7b | -20.26288 | -46.01558 | 2025-08-31 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c37d4cf-4696-37b8-860e-c182399f185b | -18.4343 | -47.24205 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86984404-251a-3fb3-93ba-0b19ce3eb378 | -20.25924 | -46.01497 | 2025-08-31 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0ff939e-8394-3a52-84fe-c16b5702e54a | -23.02309 | -46.46568 | 2025-08-31 04:32:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05e2c0b3-cba2-3e8c-9722-c021b3768e5a | -18.43487 | -47.2382 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2f481c3-02e1-3032-bd08-64e5f4a8c93a | -16.41234 | -45.64971 | 2025-08-31 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a0cb031-db98-3ba0-aef1-741c47008329 | -17.47775 | -46.99894 | 2025-08-31 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0df7a54a-7bc4-3b9f-bdfa-7af0342bad6d | -17.73662 | -39.52655 | 2025-08-31 04:32:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2e188c7-4972-316a-b94a-7da51a2580da | -16.97869 | -49.31302 | 2025-08-31 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ace0cf8b-8173-3ec2-97d0-f692e880053a | -16.53975 | -55.05769 | 2025-08-31 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6ec94b46-8956-3288-9f79-1de0b9f34a37 | -17.1585 | -46.08004 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4c201fa-72fe-3617-b0f3-3dde478476db | -16.33102 | -51.60212 | 2025-08-31 04:32:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f896c3a-b4c7-3a27-8715-c3e828141a6e | -15.68514 | -52.73953 | 2025-08-31 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 332a3b51-68f7-34d3-b102-b22ba249436b | -14.60582 | -54.51086 | 2025-08-31 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bc420ea-5898-32c1-ae17-78eb56e96642 | -16.22389 | -52.65229 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4f9d1b1-1faa-3b8b-ac5e-230271307f8a | -22.73518 | -46.13151 | 2025-08-31 04:32:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0d5ec1b6-29a9-3469-9937-d4b6b1cb0632 | -17.7202 | -44.39165 | 2025-08-31 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1a74f2c-a37c-3f40-8ac8-17b76179a56c | -17.15583 | -46.07693 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba4c0fb-1466-3a14-ab62-6989c5182f3d | -22.32982 | -48.99708 | 2025-08-31 04:32:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f2c1240-7746-35ff-8666-21a56ea779e9 | -16.21993 | -52.69613 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 53be43b4-4382-3225-b6a7-11e3a763e71b | -15.21684 | -56.05973 | 2025-08-31 04:32:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 576cedc8-784d-3c98-a178-447b6029f44c | -22.81933 | -47.32956 | 2025-08-31 04:32:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0dc006e7-56b8-3afa-9575-c42d0499a1df | -18.05719 | -45.94587 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b932199-22b9-3ca5-a110-db28e41615b2 | -16.25436 | -47.94284 | 2025-08-31 04:32:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e101a272-1dda-345f-b77f-e11f2d1b19c7 | -16.22133 | -52.66651 | 2025-08-31 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e97e5074-2730-3ce2-9b33-165468686c2a | -18.43886 | -47.23493 | 2025-08-31 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f520e08a-44ad-37b7-9b30-a92eb1eb781f | -23.19701 | -49.41775 | 2025-08-31 04:34:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0693a7a6-1242-37e6-80b6-435dc3a85015 | -23.54955 | -47.45007 | 2025-08-31 04:34:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3cab7247-dd71-3192-85dd-ad4bd76b4eb8 | -23.55568 | -46.3669 | 2025-08-31 04:34:00 | NPP-375D | FERRAZ DE VASCONCELOS | SÃO PAULO | Brasil | 3515707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e554cd6-7f5a-3557-97d1-b08526e93d49 | -28.51693 | -55.23286 | 2025-08-31 04:34:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 25313492-b83b-35e6-8687-733537588497 | -22.66687 | -53.37646 | 2025-08-31 04:34:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e38efb7-86ef-34dd-9f2a-48efb44bca7f | -21.9857 | -56.02292 | 2025-08-31 04:34:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d888266-f238-3bb1-a8b9-1dbb222b05f3 | -23.50281 | -48.20916 | 2025-08-31 04:34:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ebe7f30-e129-341e-a437-484d2d5f1c0a | -22.24259 | -56.11382 | 2025-08-31 04:34:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e26949a7-4f96-35d5-9bad-cd8e4de72ba5 | -28.71472 | -55.63655 | 2025-08-31 04:34:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b48cac27-4654-32c4-80ad-2646612c1202 | -21.98685 | -56.02408 | 2025-08-31 04:34:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b4e54ea-5cc2-3c85-9b20-cb55ba7f388d | -28.90859 | -51.79053 | 2025-08-31 04:34:00 | NPP-375D | FAGUNDES VARELA | RIO GRANDE DO SUL | Brasil | 4307864 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c69a8de1-758f-33b9-a6c3-bd3b1b46e93e | -29.04367 | -50.87651 | 2025-08-31 04:34:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 521d19f7-9478-34d9-aa5b-5eef97f029e0 | -22.24939 | -56.12403 | 2025-08-31 04:34:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fdae443-d13b-340b-b30c-73a3d69c9b4a | -28.3146 | -55.20993 | 2025-08-31 04:34:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| fac4245b-75f8-349f-bf7e-fb0df82662e7 | -28.31096 | -55.20906 | 2025-08-31 04:34:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 992b486a-b32d-3dde-b1c4-5c3ead5bf2c5 | -29.77914 | -51.1749 | 2025-08-31 04:34:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 0792a587-0f2c-3de4-bdd9-bb371dd60d66 | -29.47312 | -51.33442 | 2025-08-31 04:34:00 | NPP-375D | FELIZ | RIO GRANDE DO SUL | Brasil | 4308102 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81890f8e-0762-3c06-b986-096cbc4bafbf | -23.18595 | -50.94472 | 2025-08-31 04:34:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README52.md)
