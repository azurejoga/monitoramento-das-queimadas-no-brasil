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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 224ff199-9390-3de1-8cc6-f279eb6cd0ba | -6.64 | -43.75 | 2026-09-23 03:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28770878-a2ed-3c6e-85cf-9a8ffb3aedfe | -12.82 | -50.92 | 2026-09-23 03:45:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 578302e8-7adf-398e-81c0-947b933703fa | -12.79 | -50.91 | 2026-09-23 03:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9de4bed-48bc-355e-b7eb-66ce41350c83 | -17.16868 | -40.77652 | 2026-09-23 03:47:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 140a98de-09e0-3214-88cd-ac4d5068000e | -15.27158 | -47.63242 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5c73565-511e-3146-bde4-d719628bc6ca | -17.09283 | -43.20657 | 2026-09-23 03:47:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bfa0668-95bf-3ab2-bf8a-406d37b2ff35 | -18.16235 | -39.79918 | 2026-09-23 03:47:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c72610aa-2ba6-358f-bae9-2c11066a2cee | -17.16776 | -45.18203 | 2026-09-23 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 487eb407-14de-3a14-9582-6a07a4c03428 | -17.16335 | -45.17775 | 2026-09-23 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2daa2f24-c7a1-3e40-8041-d11d6c0771d6 | -17.15763 | -45.17981 | 2026-09-23 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18a8cf26-85ff-3144-b9f3-816d1cc3513f | -17.27013 | -42.32807 | 2026-09-23 03:47:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5aa0f7d3-a543-3d8b-acb1-c869ceac776f | -17.38431 | -41.6371 | 2026-09-23 03:47:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 956e2ad0-3e47-31c2-a3b2-ca24ae719cbb | -15.24418 | -47.61131 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 875706cd-a064-3801-92c0-ad588f228998 | -16.82216 | -41.9084 | 2026-09-23 03:47:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a1d77a08-5006-3b57-8526-aacc4770b852 | -16.63807 | -42.32774 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05c5d40e-55f3-3ca7-b55a-ede0beb8baf5 | -17.34977 | -42.13726 | 2026-09-23 03:47:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f68b3de-99a5-3306-b455-d51a9292cf56 | -17.69209 | -44.13587 | 2026-09-23 03:47:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31bb0d88-afee-31ff-a85c-436def968106 | -17.16204 | -45.18409 | 2026-09-23 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aab94fe6-30e7-3f88-b7ac-b247ec0577b8 | -15.25022 | -47.61293 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb9572e9-abef-3bfd-996e-9d088ad6ccbd | -17.1627 | -45.1809 | 2026-09-23 03:47:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32f6b717-c326-31f8-b3bd-cbe9abf7346e | -17.08735 | -43.21108 | 2026-09-23 03:47:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f7672da-bd09-3800-b927-9888cbce3e1a | -17.08555 | -43.20653 | 2026-09-23 03:47:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96b17ec8-93ea-3c21-bc08-adb999bde58d | -17.07485 | -43.20353 | 2026-09-23 03:47:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7681b263-5ae1-3792-ab1e-b420f6f7639f | -17.09004 | -43.20731 | 2026-09-23 03:47:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b97b5a79-4043-39b7-8157-b7b9df05f503 | -16.64234 | -42.32854 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d26404b7-cefa-3339-82b7-b6ac309efb03 | -15.27881 | -47.62851 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f668d66c-ad0e-3e2e-8509-07deac17bce3 | -16.64155 | -42.33271 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f42ef54-a30a-3461-842e-c0bddbc3e18f | -17.2582 | -44.45053 | 2026-09-23 03:47:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de94fb71-59d5-349a-bd07-1ff71ab06468 | -16.84364 | -39.18674 | 2026-09-23 03:47:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f1504ff5-2c0a-3044-a166-a706a2f616c1 | -18.18489 | -42.83561 | 2026-09-23 03:47:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da103434-7a46-3180-8bbc-88159cbd20a5 | -18.27617 | -43.70183 | 2026-09-23 03:47:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed7777bc-d440-32f9-9392-61056b489be7 | -16.60244 | -42.37508 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b018911b-f69f-3057-955a-9af6f51577b4 | -15.47555 | -47.9012 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5eba1bdb-ae20-3bb5-8390-8c2b5ae47919 | -17.38499 | -41.63333 | 2026-09-23 03:47:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb55ccf7-e8d5-3183-8007-221f7e3846c7 | -16.64583 | -42.33347 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e53f4584-4f7c-3a05-b0e9-843d91da2706 | -18.26539 | -43.7089 | 2026-09-23 03:47:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0a7c0c3-dcf8-383b-a39a-81c9a538fd15 | -15.26233 | -47.61598 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1fe65f7-15b3-3625-a5c0-732dfa0ad1aa | -16.60415 | -42.37697 | 2026-09-23 03:47:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a9b8b7b-9d87-3c3a-bddb-716780ab5387 | -15.25625 | -47.61459 | 2026-09-23 03:47:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcebf402-12c7-38ae-9e4d-ca91a695d31e | -14.6507 | -45.5902 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f48ace87-b593-3cfc-8fe4-e0550ca76614 | -12.0599 | -50.3419 | 2026-09-23 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0a1cac88-9000-3bf4-b73d-6f5feecb4f9a | -9.1025 | -61.4299 | 2026-09-23 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 55d4cbc9-2358-3dfc-85df-15ae449b5d02 | -3.6946 | -60.5835 | 2026-09-23 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| faa8c5ac-03a5-3794-b8c5-f482f6607026 | -8.8105 | -44.2757 | 2026-09-23 03:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 4123a942-5c11-3128-b2cf-41cd6ca4dcb7 | -14.6898 | -45.5831 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| da2a3703-da28-3a77-9a18-68e6194739a9 | -14.7284 | -45.5993 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 20761141-de53-3745-90a5-29d32261e0af | -12.4216 | -46.9551 | 2026-09-23 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 613da614-2387-324d-8c72-3112798a649c | -14.7089 | -45.6029 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 204.4 |
| dd4aa7d8-dbbc-3866-a20c-1a3d570fe2bd | -5.4071 | -49.2596 | 2026-09-23 03:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 274db997-43e6-3892-b70f-ba3170522536 | -11.8675 | -45.788 | 2026-09-23 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9f60720b-7688-318d-87ee-3d8c18996215 | -14.6111 | -45.6205 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c8d08e99-7d56-312d-9eb1-cf1b0e058306 | -14.6893 | -45.6064 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c86994a5-abd9-3ead-a769-f9132d5d62b5 | -6.6146 | -59.9272 | 2026-09-23 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| e793dd40-186c-3bec-a9de-d1030cadfdba | -14.6302 | -45.6403 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 40d1a0ff-87c9-3cb9-afdd-324e1d82633e | -12.4212 | -46.9777 | 2026-09-23 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 70ca5536-bb78-3810-a95f-eea18a4ca31c | -9.121 | -61.4482 | 2026-09-23 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8921dd52-5aa2-3f48-8727-3ca40ca8a6b9 | -12.1192 | -45.6368 | 2026-09-23 03:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| c0ed83b6-fb7b-3211-a548-c3f55a314c8d | -3.6947 | -60.5645 | 2026-09-23 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 221279df-7566-32b6-ab50-4c0c52d53445 | -11.8867 | -45.7852 | 2026-09-23 03:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5fff293b-3970-306a-80bd-5a56eac1ebdb | -12.3679 | -50.1539 | 2026-09-23 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cd0e7a67-97bd-3430-bdbc-f070f049302a | -5.4069 | -49.281 | 2026-09-23 03:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4c597c04-97ef-3790-8da6-fc73c2329972 | -14.7289 | -45.576 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aafc9cb2-371d-374a-aa5f-90d7ad009a13 | -11.6324 | -50.947 | 2026-09-23 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2affb2b7-2544-3e02-ba88-f3622f1aab74 | -14.6297 | -45.6635 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 05f4de4a-c5f5-38cd-8483-e75228110155 | -9.1211 | -61.4291 | 2026-09-23 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 128efa5c-9dd2-3be9-9b69-6b2aa293546f | -14.7094 | -45.5796 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 5107eb34-cf62-31ad-8399-33586b7bf232 | -8.9164 | -61.4958 | 2026-09-23 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 840f6196-87bf-35f3-9e2c-794aff8eaa14 | -14.6106 | -45.6438 | 2026-09-23 03:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 4cd0cc0f-1d47-33c3-b036-f04876ac3a87 | -6.6145 | -59.9464 | 2026-09-23 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 223e77c3-6da3-386e-8415-ca46fbcfe7a6 | -12.0595 | -50.3634 | 2026-09-23 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b118763b-c3e3-3013-88c3-30da6335b3b0 | -11.8871 | -45.7623 | 2026-09-23 03:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| cea5445d-f03d-3f39-b6ef-32a96e2cf1b4 | -6.6148 | -59.908 | 2026-09-23 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4e343aa5-93a7-3201-9e70-51eebd03faa6 | -11.6321 | -50.9683 | 2026-09-23 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 25c71d86-aaf4-3e3f-8281-97aa508e0f80 | -11.8679 | -45.7651 | 2026-09-23 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 4b4c7fa4-276d-39db-931a-aae8fa1a36b7 | -11.6514 | -50.9449 | 2026-09-23 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3cf7b44a-fffa-38a7-a226-6ddcad007997 | -6.633 | -59.9457 | 2026-09-23 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6acbb7fa-f39a-319d-82cf-c6384b999615 | -3.6763 | -60.5839 | 2026-09-23 03:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 96163840-75df-3cb4-ad52-2bcea2e74be2 | -6.6331 | -59.9265 | 2026-09-23 03:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 88d8be2b-a6c8-37cd-8b1e-95d4b958e59a | -11.8875 | -45.7394 | 2026-09-23 03:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d6eb90c2-3aff-3861-8f45-24cf92199996 | -9.1024 | -61.4491 | 2026-09-23 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 0d62760d-e80c-3b27-9fe7-f3818115f479 | -12.7952 | -50.9171 | 2026-09-23 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| a0f17978-a1a5-39a7-9e54-453e21eda313 | -12.0599 | -50.3419 | 2026-09-23 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9759261d-57c8-3c6d-b6b6-64ae6a950958 | -8.9164 | -61.4958 | 2026-09-23 04:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5e4b8ea5-a791-3201-9e19-36888a5ba75d | -6.6815 | -55.0703 | 2026-09-23 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e37e6828-d767-3109-b434-1515ce776f18 | -12.0595 | -50.3634 | 2026-09-23 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a77dff8d-25cf-32ff-a4e3-1712cf53cd6b | -6.6146 | -59.9272 | 2026-09-23 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 863578e3-3f6e-36b1-a04e-f4a3ab063240 | -3.6763 | -60.5839 | 2026-09-23 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 74f26c55-5df5-3943-8333-a6c3ac0901bd | -9.1024 | -61.4491 | 2026-09-23 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 764180d0-72ba-3cbc-9590-90ea1ab4bbb6 | -12.7948 | -50.9385 | 2026-09-23 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a8ea28b2-2d55-3d09-9051-a536b2a5b232 | -11.8679 | -45.7651 | 2026-09-23 04:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 391584c8-1795-3d9e-8b94-2cb3821d894a | -12.1196 | -45.6138 | 2026-09-23 04:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 296698a2-b58b-3708-b2ed-8ac57b0ec177 | -12.814 | -50.9362 | 2026-09-23 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cddaa678-e386-3355-b83f-66bf0d4b689d | -12.738 | -50.9027 | 2026-09-23 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 4a04b348-6bad-3401-9578-3754cafc39bb | -12.4212 | -46.9777 | 2026-09-23 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 10425697-8d43-3164-ad19-72270376b180 | -14.7089 | -45.6029 | 2026-09-23 04:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fec009b7-6ad4-3946-9ee5-53b5637e17c0 | -11.8871 | -45.7623 | 2026-09-23 04:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 16eab851-3fc6-3c01-bb7d-31bf60ab2cca | -6.6331 | -59.9265 | 2026-09-23 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 943d4f80-a9cc-33de-b9f9-68875e2fb54f | -12.3679 | -50.1539 | 2026-09-23 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ba1f4221-7a6a-3067-a273-580f1b772454 | -12.7192 | -50.8836 | 2026-09-23 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ea4036d1-3cff-3ecc-87be-44d8a77c7203 | -6.6148 | -59.908 | 2026-09-23 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |


[Clique aqui para ver as próximas entradas](README48.md)
