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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8128ef29-839f-3f7d-9168-87287658ca55 | -10.12619 | -46.22876 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d4024a-6cb5-343b-a538-b7d99855ae8b | -15.93115 | -43.52596 | 2025-09-08 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c08e759f-efbd-3965-b74a-dd9ec345d0af | -14.99265 | -48.02205 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 598439a1-b978-330f-ba44-f73f0bc19b18 | -16.35443 | -43.64043 | 2025-09-08 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31c1ff99-b2c8-36ba-aeb1-4c13e019cf11 | -11.33938 | -46.57578 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 338ed06c-c802-388b-878e-afb02f2b1126 | -12.93581 | -54.79782 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f85457e3-8bb6-387f-bf99-fc0589a7dc79 | -15.16762 | -47.96667 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f9f9b7d-be19-38c8-a6ef-60c90d38c45d | -14.52792 | -53.99347 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eee79801-abda-314d-8363-0aefbab2992b | -14.51787 | -48.76218 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c0cd729-07d2-3016-997e-b83bfd873e1a | -14.52217 | -48.77072 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6600723b-3a63-3e8b-881f-8c02ec666e36 | -13.00671 | -45.21848 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76aba442-31b6-3893-b5bc-66d68267e512 | -10.17691 | -46.22952 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b32e4530-9498-3554-b84a-7675e57ef30f | -8.69622 | -45.31221 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bdc3cecb-17b3-3d5a-8d34-c51836f802fe | -12.94255 | -54.79931 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f712e222-e5f8-3528-a060-2f0c32a3c28f | -12.00141 | -47.76859 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| db7112d0-9138-384c-ad88-9092950c5a1e | -11.19903 | -55.01785 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a95e7256-ae2a-320b-84ba-1e914425e827 | -11.2845 | -46.46362 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ac1845b5-1be6-377c-9def-055a39c70daf | -11.32425 | -46.55105 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e88145a-e933-31e3-9e43-5c006d5647ef | -15.01732 | -48.00121 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61684343-ad9b-329e-b80d-0e11431df62b | -10.1432 | -46.20425 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b9457c8c-761a-32cd-ad3d-29a3bdd37405 | -13.8172 | -46.29206 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea91930b-67e5-3016-b70b-a1364029d460 | -14.79617 | -48.23478 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68237af0-3962-3d17-aefc-e64fafbbcdd0 | -14.78265 | -48.11541 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03d1052b-6aae-3b46-811e-ede9101e0f8a | -9.12551 | -47.02727 | 2025-09-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d239521-dc37-3122-9d93-ce1a418f8238 | -14.52405 | -48.76094 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 715dcb1f-a107-3ed9-842b-38bfa9bf27df | -11.36788 | -50.33941 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78b5e403-12b7-3f5d-a055-b62e02bb0997 | -14.81118 | -48.17785 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7aafe972-60ee-302c-be67-72d23c338d75 | -7.67158 | -50.29127 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2d5f89a4-196e-3e88-ac9a-997148859283 | -12.19301 | -53.91443 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3eceeeb6-f357-30eb-949e-a9c9451b8f64 | -13.74447 | -46.90854 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 882a8636-c51e-3719-a953-04c52bec47d2 | -8.92821 | -45.81536 | 2025-09-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e29f6bf9-ab59-39b4-9562-5f979944f5e3 | -11.35495 | -50.37865 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10354faf-2923-3091-a1e0-4272c2dca43e | -14.52234 | -48.76327 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 070060cf-e4cb-383e-92da-415ecc2c7283 | -12.84406 | -47.98524 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6077dec6-38e6-3ca6-b206-d39195b32a9c | -9.83947 | -53.29785 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8482f7f-75be-3d3b-bdb0-810b4b2d1050 | -11.21454 | -55.01392 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c1178e-8976-3d6b-8e55-31b5d938b088 | -10.08053 | -48.10253 | 2025-09-08 04:02:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53ee7197-813f-3b63-bada-3bed9d835216 | -11.0313 | -45.95668 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 877cdbba-b27e-31b4-a5a9-5e899b986c4a | -9.80329 | -46.23507 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a7cca1b-cdc2-30cd-a695-bf4bf610e1a2 | -15.28829 | -44.76544 | 2025-09-08 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db0ea042-24d3-3705-a106-fe9ec7e5e310 | -11.21308 | -55.02074 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71fae671-06be-319d-ae9a-28cec86209af | -9.95197 | -51.19633 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14d3b953-1c4d-359b-89a3-227ce0b54e09 | -11.81628 | -46.77116 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17400bd8-efd5-3056-9ac1-8f3f4f5f850d | -13.82458 | -46.25048 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e99fd455-c748-33d3-b323-53ce6c8cd945 | -12.81914 | -48.00106 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b015fb6-1e02-378a-8829-6b4b0d371b51 | -14.50969 | -48.75598 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20fa0386-737a-38bf-aaab-ac0446e57259 | -11.42707 | -43.65655 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 790181d4-7860-3b6f-9cea-ddd7bd387c97 | -11.83284 | -46.77433 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfbbf0fc-a720-3327-b879-69dae4146c56 | -10.81864 | -47.74617 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c341c504-51f5-3c3f-97c3-82f0880a9988 | -13.64596 | -43.80622 | 2025-09-08 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 30f7a85b-332b-3927-8125-86f50c82bc65 | -11.4234 | -43.63554 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47369144-b0c2-32ac-9100-3650f0198737 | -15.29772 | -43.3871 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59e90f67-8d2d-3c32-8fb2-1a69b12840ee | -15.54172 | -48.39317 | 2025-09-08 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f3b6cdc-2140-3af7-9ae6-6b176c92aa96 | -11.20752 | -55.01245 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a7c214b4-1220-31a2-93ef-a428da7b66bd | -9.95282 | -51.19195 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 171e6756-d879-36e1-971b-c1d6df57b562 | -14.80528 | -48.18557 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1f02fc8-a3df-390a-99d4-ddb610026c8a | -11.32488 | -46.54741 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cda989c-2793-3cac-a11e-82460a9ee562 | -10.12961 | -46.23347 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cfb567b-6734-3218-8248-4733c6794233 | -14.79292 | -48.10807 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 974ebb1f-9511-3696-8f9a-786a0de2f8f6 | -9.39741 | -40.30403 | 2025-09-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e3406ad3-70f3-3734-adc8-8f55def8ea3f | -13.92134 | -48.04134 | 2025-09-08 04:02:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b829f8b8-f86a-3306-bd05-1d63d72837fc | -9.79291 | -46.22136 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e541eaa2-d298-3906-ba83-06b4fc75efb1 | -9.86347 | -46.58561 | 2025-09-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29e0c4fc-2954-3e9b-8ce5-f27758a017f8 | -8.87511 | -47.90702 | 2025-09-08 04:02:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87ce181d-a881-3778-8acf-7cdb7d3db4b8 | -15.2916 | -43.38224 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 76504104-dcbe-36fd-85c6-9e185cb9e911 | -9.7205 | -43.98842 | 2025-09-08 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d16c3053-5d72-3d31-b866-101af3552188 | -12.16567 | -43.94437 | 2025-09-08 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1d846c0-ae8f-3b72-95f7-a80ba84dc9de | -15.53486 | -49.23732 | 2025-09-08 04:02:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a92b466-8682-31e6-a589-69d0bc232c90 | -14.51126 | -48.80311 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2b35bf2-2817-3bf2-a086-3b51dc71b95d | -11.3255 | -46.54383 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e0ddb8a-9447-315f-95a2-d4bcb0def339 | -10.79709 | -47.73708 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1aee58d-67d5-3f58-8082-a4da69185351 | -9.03003 | -49.79819 | 2025-09-08 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe4e851b-de51-3c00-9af7-2be26ce27333 | -13.81414 | -46.26408 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02de6d1d-0ad8-39ad-afd3-1393e6719b62 | -13.03551 | -47.1297 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32330b7a-747e-3641-a01d-a72069d1d46e | -13.81032 | -46.28549 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1195470-5567-3e6a-97c1-f6ec36d18f74 | -15.09208 | -48.13559 | 2025-09-08 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 034a2850-8c0e-3b17-b20f-46d1fc7c4350 | -9.07834 | -46.98787 | 2025-09-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4af2fcef-cc72-34a9-9ad2-8699373a081e | -14.29352 | -44.87523 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52dfc266-a4d0-3d86-8aa8-3a60c45e3a87 | -12.81855 | -47.9997 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69fd1266-26c9-3d54-8e6b-aab9b4fa1581 | -9.84096 | -53.29515 | 2025-09-08 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65f613e2-d00c-3df2-8365-9b478aee5d85 | -13.66317 | -46.96647 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 420633be-fbfd-36cb-b5a4-eccf36da4730 | -11.28173 | -46.45542 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 8bb35248-5ff1-3806-8d19-7aec91a929c8 | -12.12519 | -50.61906 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b597e353-c86d-3148-a12f-6fdedbd13a1c | -9.70702 | -43.51116 | 2025-09-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9a12307-00f4-3563-a4d4-35ddfd92bc27 | -13.09898 | -42.34165 | 2025-09-08 04:02:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af72fe71-43cb-3b60-8b00-2dfbad2d01d3 | -11.86929 | -50.96423 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9f6c183-2360-3c0e-892c-60b74be7efb3 | -13.72568 | -46.89659 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd242431-9612-327b-8a83-49c8d98ce3dc | -14.29137 | -44.86622 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad1d94bd-4d25-3de1-aa45-5569a4ea4816 | -9.20844 | -46.05523 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec8b504a-d4b0-31e3-beae-bc55287dba5a | -15.16382 | -47.98727 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d49d4e89-bfae-3046-b113-8c5e35999fcb | -11.20831 | -55.02148 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0be79cc-65e5-3666-be13-93983220b19f | -14.28474 | -44.99158 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 245b07ba-342b-321e-b092-761979f94f73 | -12.82186 | -52.9444 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38d36362-f6d0-3cb5-8d0d-cd5e282a5a65 | -11.40871 | -50.37553 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 387b1071-9d97-3423-9581-18f54c87475c | -14.52144 | -48.76819 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5c57f8e-c486-39e1-b8bd-40e0197182e7 | -13.35627 | -44.4329 | 2025-09-08 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e18d7b6-19d6-3c67-8779-720cd0133277 | -13.00379 | -45.2133 | 2025-09-08 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 27585d4a-a09a-3a09-8558-242043e3d9b5 | -11.86999 | -50.96063 | 2025-09-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876a22f9-d1e1-3e75-963d-4a8c37c8778f | -10.18098 | -46.68183 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424f359a-3434-378c-a417-f554849d40ac | -9.07615 | -47.00051 | 2025-09-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
