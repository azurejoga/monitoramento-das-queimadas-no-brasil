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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de13bf71-e8e2-3d82-98fd-44628df13bc0 | -10.8382 | -46.8985 | 2026-05-29 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| fb6e051f-ae90-3a06-8996-5c8385bc9c85 | -10.8192 | -46.9009 | 2026-05-29 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d6674fd8-0ea4-3004-8283-6ba9120be917 | -10.8382 | -46.8985 | 2026-05-29 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 7d3a8281-9ede-3e20-84b0-4209ef2f4c93 | -10.8192 | -46.9009 | 2026-05-29 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 66d04aa4-bd72-3493-a7d8-75e3f409197f | -10.8192 | -46.9009 | 2026-05-29 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| b56b3431-96c8-31ca-8fa6-7700f0bcdb48 | -10.8382 | -46.8985 | 2026-05-29 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 5a91c066-0bfe-3d0e-b8c0-20293b6ffb59 | -6.09945 | -44.74341 | 2026-05-29 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0339d79c-633f-3986-afad-c3632b3f198e | -6.99272 | -42.88556 | 2026-05-29 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 998bdbb9-7feb-3ab1-81b9-d105d48922fe | -8.83941 | -46.72417 | 2026-05-29 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 50993396-7ec6-3aa9-a106-29793a8f48e6 | -6.11091 | -44.73377 | 2026-05-29 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c986e978-895d-3461-aa9e-710faa40c8d6 | -6.10112 | -44.73236 | 2026-05-29 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 56d8cda7-9ce2-3042-9160-0f7300309e1a | -5.05715 | -42.6194 | 2026-05-29 11:34:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3479a016-0581-3ffc-aabc-dffa5df5ae49 | -6.94114 | -42.74056 | 2026-05-29 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 068f50b1-dd90-3b19-a9f1-024f149bb370 | -8.83685 | -46.71711 | 2026-05-29 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b9e0ea05-3e59-30ac-b775-0ea87bf830f3 | -5.01869 | -41.66807 | 2026-05-29 11:34:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| feaefd13-2611-3c37-9f81-2cc04d08df34 | -5.3335 | -42.68612 | 2026-05-29 11:34:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| acbf8436-fcf9-3f69-b41b-a8337a3c4270 | -6.99699 | -43.87015 | 2026-05-29 11:34:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14efa22c-4d19-3d02-84e6-4a820ea45d46 | -9.78905 | -38.1266 | 2026-05-29 11:34:00 | TERRA_M-M | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 8c0c8ee7-b50d-3676-979f-a76de46ff346 | -9.1096 | -38.21336 | 2026-05-29 11:34:00 | TERRA_M-M | JATOBÁ | PERNAMBUCO | Brasil | 2608057 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5680c4ce-b192-3e01-ab47-552fb3986c15 | -8.69156 | -48.30387 | 2026-05-29 11:34:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e6f93ff3-22b1-3e89-90b2-bdf555b19f6b | -5.32754 | -44.68887 | 2026-05-29 11:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5f10d13e-28e5-30ec-b294-b7d36f903f50 | -6.99402 | -42.87655 | 2026-05-29 11:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 0782a8cc-0732-3eaf-ae64-4fc67881cc55 | -8.83479 | -46.73084 | 2026-05-29 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| e9706188-75cf-330b-9588-665a5736cdaa | -8.84157 | -46.71048 | 2026-05-29 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 72fc81b8-861c-3bff-9eff-2e7767484af9 | -8.82953 | -38.93088 | 2026-05-29 11:34:00 | TERRA_M-M | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0323499c-9d16-32c3-afe4-c8bd6fcd1af3 | -5.33481 | -42.67706 | 2026-05-29 11:34:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| eb23efae-97a9-3128-b011-3d78b06278a4 | -6.94244 | -42.73159 | 2026-05-29 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a382b171-5210-3e4a-8c80-1be1a6558175 | -9.11135 | -38.20019 | 2026-05-29 11:34:00 | TERRA_M-M | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f073c095-c180-33d7-9edb-d3732e5cfd2e | -6.99842 | -43.86044 | 2026-05-29 11:34:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 267d012f-21f0-33a4-b825-72a5a153ebca | -9.8321 | -37.2372 | 2026-05-29 11:34:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 15.4 |
| bb059b13-a285-340f-a1b1-13d1f1cd72bd | -6.10923 | -44.7449 | 2026-05-29 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 506be932-2877-33ea-8311-7e34312cdada | -11.59792 | -47.44006 | 2026-05-29 11:36:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 39b54bde-0c14-3e54-86b2-2144725aec61 | -12.44265 | -44.74306 | 2026-05-29 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cacacd9b-9417-3c6e-b4e3-558288761fc3 | -12.4232 | -47.89746 | 2026-05-29 11:36:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 79df0adb-a5b5-368e-a6e3-b63a63c9e49b | -10.82752 | -46.92461 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e313f60b-c3e3-3571-a844-f5d76f313871 | -10.98676 | -45.09673 | 2026-05-29 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| be691ff2-c6a4-362d-866a-a0c8a03f8cb7 | -10.82335 | -46.9172 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| eab2be87-f41d-323d-a2e1-0a2139342009 | -10.82541 | -46.9038 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 277.8 |
| e54d2cd5-3d3a-30ce-9518-24e799194d53 | -10.81686 | -46.88881 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e552af7d-cbb4-3648-86c7-4861873f092a | -10.81483 | -46.90202 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 831c93e7-4eb7-38e5-868b-8575b7894c20 | -12.00694 | -45.35835 | 2026-05-29 11:36:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 967a2492-16c4-322d-bcee-ec942cca479a | -10.82748 | -46.89024 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| be293f27-6308-3155-b43c-4d4bf895aa9b | -12.6156 | -44.50932 | 2026-05-29 11:36:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cdfd22a-6f82-3ef5-8392-c9ba1b1e1764 | -11.59571 | -47.45385 | 2026-05-29 11:36:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 708ca379-8029-37b3-bb47-8ef5f6641902 | -11.16828 | -46.79455 | 2026-05-29 11:36:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 840c885a-7366-3a9d-be85-de1a4166acd8 | -11.58704 | -47.4383 | 2026-05-29 11:36:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c6b43e1e-fae7-33bf-ad84-5b42fac075d5 | -13.35352 | -44.32769 | 2026-05-29 11:36:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4b91f09d-3b58-3c98-b081-bc6cba4b8f68 | -10.82966 | -46.91127 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| bca34d18-226c-30c4-8744-10823c3cecd1 | -10.83183 | -46.89769 | 2026-05-29 11:36:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 144a62ca-458e-3202-ac1b-fcaa54441670 | -10.64347 | -49.73037 | 2026-05-29 11:36:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 712370fa-1556-3a64-8535-e214095009af | -11.61982 | -45.18382 | 2026-05-29 11:36:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32b7eff2-1b32-3c6e-a0e3-bf8093fa544e | -11.14722 | -45.80269 | 2026-05-29 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f1472d35-fba3-3a62-82c7-2b409a1ef00c | -11.47152 | -46.69348 | 2026-05-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 143de03b-cd4f-32dc-a93e-994a33887e8f | -12.44123 | -44.75267 | 2026-05-29 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe7d8f6c-1ff3-3ec5-8a53-d5725e696a62 | -21.80773 | -49.12925 | 2026-05-29 11:38:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 442d3c3c-7c79-313a-b412-0ec187cb790c | -10.8382 | -46.8985 | 2026-05-29 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| ef03ea60-9f3e-32d9-9e9d-879151dcc273 | -10.8192 | -46.9009 | 2026-05-29 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 375.3 |
| 30186089-6fbe-3783-99bc-33543d681d43 | -10.8382 | -46.8985 | 2026-05-29 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 1a3774a6-b11f-3603-8d14-3103a937eb5d | -10.8192 | -46.9009 | 2026-05-29 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 22e7735f-d51f-3cc5-bb1d-5f4b29442225 | -10.8382 | -46.8985 | 2026-05-29 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 3e872d2a-d556-32d0-95dd-7b20fd6b788c | -10.8192 | -46.9009 | 2026-05-29 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 289.5 |
| 1ec53a41-10c2-3073-aa7b-48c1d3bc4114 | -10.8192 | -46.9009 | 2026-05-29 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| fb586632-c6c1-3e4d-b0fa-a9947078e989 | -10.8192 | -46.9009 | 2026-05-29 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 09880792-b20f-3d5b-89bf-be3de5f55d61 | -10.8192 | -46.9009 | 2026-05-29 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 037320d8-3e13-3195-8abb-ee2baa11f608 | -8.8537 | -46.7228 | 2026-05-29 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 819ee0c2-8726-3e1d-ae68-4ed2859038ef | -10.8192 | -46.9009 | 2026-05-29 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 25234bc8-8da0-3378-8bfc-ae2dec9860eb | -8.8537 | -46.7228 | 2026-05-29 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f5fc45a2-f855-37e9-93c2-fc7245ec3c92 | -11.9493 | -43.4019 | 2026-05-29 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| a478d5a4-1bad-3d12-aa6b-ac8e7e24fca4 | -10.645 | -49.729 | 2026-05-29 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 73faf9e4-ea5e-3858-b1f6-4dbfe5a21e2f | -10.8188 | -46.9233 | 2026-05-29 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2c03437f-533b-35a1-8e3a-b5e3a98817ed | -11.9493 | -43.4019 | 2026-05-29 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| fe106755-4a2e-30b4-9ca0-a88e112d4ba9 | -8.8351 | -46.7024 | 2026-05-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1c30c361-d2c7-32a3-9e9f-5f626f869fff | -10.8192 | -46.9009 | 2026-05-29 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5e81827b-75d7-34ac-90a2-2ccb1038d9b0 | -8.8537 | -46.7228 | 2026-05-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| eaf74e2d-0482-3751-93e5-716fa381f19e | -8.8348 | -46.7247 | 2026-05-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2dbec9a1-10f8-3e85-ae53-06c455ba2a5a | -10.8188 | -46.9233 | 2026-05-29 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 8b284169-8779-3f6b-a5c8-06c94de40425 | -8.8348 | -46.7247 | 2026-05-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| b0e6f5f4-7f6b-3b42-86bd-6a0bda939f82 | -8.8537 | -46.7228 | 2026-05-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1f9ab823-e6c4-3b4a-ae3e-99035932f33f | -11.9493 | -43.4019 | 2026-05-29 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6bc4d92f-0a7e-3455-87fc-919ff3e12a33 | -10.645 | -49.729 | 2026-05-29 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 37be9655-e41f-33cb-a37c-1fd4549e2938 | -10.8192 | -46.9009 | 2026-05-29 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 48ccf632-2554-3a0f-89e2-7cc81cd689b3 | -8.8351 | -46.7024 | 2026-05-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 97c341d0-488d-3e4b-8276-befd96035660 | -10.7746 | -49.93 | 2026-05-29 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1a30cf99-276c-3fb2-acd4-f7b7967cf9b0 | -8.854 | -46.7005 | 2026-05-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5cdda9bf-d095-35e8-bf9f-6f0b88dc32b9 | -8.8537 | -46.7228 | 2026-05-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7006111d-40b2-35d3-b5fb-a987f36d9a8f | -10.645 | -49.729 | 2026-05-29 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 2e0451f4-e082-3034-ac9d-1e4fd02f1117 | -10.8192 | -46.9009 | 2026-05-29 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 065b7da5-6cff-39f4-aec0-980e1f528698 | -8.8351 | -46.7024 | 2026-05-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1e08f684-1256-316f-9cb9-27a7928c4c48 | -10.8188 | -46.9233 | 2026-05-29 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 2568bbc5-ed1a-312a-a7b7-98c099f02cf9 | -8.8348 | -46.7247 | 2026-05-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| d59d382a-17fc-38fb-852a-c22ea802ee20 | -11.9493 | -43.4019 | 2026-05-29 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5299a41b-d9f9-3ddc-bb27-0b9c7f973078 | -10.645 | -49.729 | 2026-05-29 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3476ce0a-5ea9-3647-a419-5fcefdd05c24 | -8.854 | -46.7005 | 2026-05-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| dddb37ff-b2cf-31a4-bd43-da97766316be | -10.8192 | -46.9009 | 2026-05-29 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0eb7de68-db5e-35ce-9cc1-214ee67a8077 | -8.8348 | -46.7247 | 2026-05-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| d556c784-d304-38df-817a-4d21adae5913 | -8.8351 | -46.7024 | 2026-05-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d0303238-d599-38ea-a231-66a87d12011c | -8.8537 | -46.7228 | 2026-05-29 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f520d930-19e8-379b-a0d6-b45929e48185 | -10.8188 | -46.9233 | 2026-05-29 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 0874f485-0869-3ae2-843f-70dddff42d91 | -10.8382 | -46.8985 | 2026-05-29 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d473ff78-79b1-35ef-b92d-4febc1746d8f | -11.9493 | -43.4019 | 2026-05-29 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |


[Clique aqui para ver as próximas entradas](README12.md)
