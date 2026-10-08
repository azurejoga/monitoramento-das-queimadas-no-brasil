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

## Dados Diários - Página 260

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d0cb06-e61f-3e14-9326-0b130e2bbfec | -14.62667 | -43.68864 | 2026-10-08 16:16:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ca72180-1c90-348c-ba4d-5da50ac9d7b6 | -14.76228 | -39.80889 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 3f4b25d5-47c1-3216-bdd8-a12ef006586e | -18.2268 | -42.31211 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 122fed09-05c7-3d56-9fb3-210f095936e5 | -17.0717 | -45.40279 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6fff81cf-554e-394e-9d36-eda8be1fc25c | -15.39179 | -40.70737 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b74a2d2e-c4c0-3152-8381-5f0607cc924a | -17.06796 | -40.0216 | 2026-10-08 16:16:00 | NPP-375 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f7935a2c-e2ec-3722-8f22-9bf1e0b13537 | -14.73336 | -40.29201 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 098c26e3-3e36-35ef-a810-51bc1fb9e8f5 | -20.95481 | -44.77357 | 2026-10-08 16:16:00 | NPP-375 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 72f45c9a-50ac-3a89-afc3-da48e526a3d5 | -20.61937 | -43.10027 | 2026-10-08 16:16:00 | NPP-375 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c1dba651-77bd-3980-874c-467813270ba8 | -15.57769 | -42.89619 | 2026-10-08 16:16:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56d26da9-3000-3a62-ada3-fd59a8be3f84 | -14.73393 | -40.29612 | 2026-10-08 16:16:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 392311ff-68fc-3e4c-b7e9-ddbf05136baf | -18.05232 | -44.57381 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e7496e31-283d-3755-913c-380735360879 | -14.40324 | -40.67279 | 2026-10-08 16:16:00 | NPP-375 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c5087558-65b7-35d5-aa58-215aa86e6a62 | -19.36077 | -40.35167 | 2026-10-08 16:16:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 79985fb9-cdb2-358c-836c-ef6bdc4fcda6 | -18.96403 | -41.17355 | 2026-10-08 16:16:00 | NPP-375 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0467c708-e4e6-394b-9bcb-c0157fdbfde0 | -14.96914 | -48.18987 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 67491c76-ab7b-33c2-90a9-c72079c8a715 | -14.76284 | -39.81281 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 0dcc41a9-c917-35da-9848-ee876fa4ef03 | -19.2615 | -40.73896 | 2026-10-08 16:16:00 | NPP-375 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 33e340a0-b68a-3754-8d3a-3de11ec05c17 | -13.70534 | -49.08926 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 01592d19-8eba-3819-8704-df49bc9e5f6e | -11.68539 | -43.68847 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d699407-d881-3e33-a69d-1ae0a544ed6f | -8.93339 | -45.17303 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2f79efdb-0ec7-31f9-9c45-dcbeab4da168 | -11.61325 | -43.66315 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c69ee07d-105e-350c-b6b6-9543a5d56b5e | -11.73503 | -43.64653 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 8f3bbc64-2898-33ea-8b34-6c88b8ba072d | -11.20757 | -46.28049 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 71980fd4-83c5-33c8-808a-b4bbe05755f6 | -12.04852 | -47.38288 | 2026-10-08 16:18:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 187d08db-d8f5-3b62-be3e-9bc8757ed802 | -11.13748 | -46.12453 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c37d1d89-d630-3bc3-8f03-b9410617c829 | -11.21254 | -44.86897 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 91ce3f5e-512d-3494-a611-13b9be764a62 | -11.21643 | -44.86376 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| dfb5698a-7e9a-3d7c-8aed-59410cd8ff60 | -13.35807 | -43.88111 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 22fc5686-71ed-350f-8845-331ca824ebd4 | -10.75487 | -38.85834 | 2026-10-08 16:18:00 | NPP-375 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 067c04e5-815e-3064-84b8-43d361d69a84 | -9.82104 | -44.83886 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9e2ed87f-21a8-3f8a-a63e-77e15c418ad3 | -7.98214 | -35.04358 | 2026-10-08 16:18:00 | NPP-375 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d9aa3843-5230-3a4e-979f-f7da00dc9937 | -11.22574 | -45.24449 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ab788fd8-2496-391e-900a-3ad624737541 | -11.87156 | -47.40303 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f5936c7a-5a51-33e1-8408-789d7e94ed97 | -12.03004 | -43.44706 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 2741a417-d286-3425-bff7-5ccaa35cc2c9 | -9.90721 | -44.81853 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9e56e34f-d74e-3a84-beed-134105de1ce7 | -9.85459 | -47.85613 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b98c9bd7-8a6c-3e72-b585-22c63e1c5e74 | -11.59241 | -43.66613 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4e92545f-3fbb-3fb5-9e3a-2f7af2aa8dea | -12.03732 | -43.43876 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2106c48f-d58f-3f94-a47c-eabce748d5e2 | -10.47803 | -47.2304 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4a381f9c-d0fa-3dd9-8a11-0c6022188033 | -7.0317 | -35.20716 | 2026-10-08 16:18:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| 5e153f56-40bc-39ae-a729-09d717f44092 | -13.0199 | -47.20133 | 2026-10-08 16:18:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49d39a28-dd2d-3abd-9589-f854da523f4e | -11.48743 | -47.7303 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a975fcfe-4a1b-3580-b643-7e637e28968d | -12.22015 | -44.74493 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b3224793-e353-36cc-90e0-06b732cef417 | -11.06816 | -45.77076 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ca79bb5-739f-338f-bbfb-8186e37c823b | -13.14391 | -46.3463 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 328ded9f-c91d-3adb-a8c1-5150f01fdabd | -8.92545 | -37.32159 | 2026-10-08 16:18:00 | NPP-375 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ba4476d0-5f7b-3784-b771-8fef5fa55551 | -13.96581 | -44.85427 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b786758b-ea59-3f50-820e-58a688939c09 | -9.92682 | -46.10204 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ce6ba54b-811b-35f4-b329-7964b4d8f07f | -10.51646 | -47.32066 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0cd5fa59-f5c9-3100-9ddd-91ab35297695 | -11.13738 | -46.16317 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 97a00223-7015-3035-8f24-2cc2f828b71b | -11.5696 | -45.36247 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 22376ead-78d9-3cef-bce9-3fc94f89d3e8 | -12.15619 | -44.7189 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 866c28e6-4445-338e-bb43-e50f6c1a3fc0 | -9.79917 | -44.77643 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87b8a070-ab20-3652-9aca-c81b11db5f3b | -11.25401 | -45.25624 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ab9ecb2-32ce-3d1b-b5e2-b27d15f1c342 | -9.14474 | -49.92274 | 2026-10-08 16:18:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5791a195-7f13-3eae-81c0-8834d1bd3070 | -12.41632 | -46.44251 | 2026-10-08 16:18:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd90a2ed-93ac-3fe8-8a9a-120cdeadbe8f | -11.63151 | -43.70333 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0eb14882-dea4-3778-8504-9f5126dffdfe | -8.29181 | -45.71603 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9198ca70-a1d8-382a-9496-c8703bedd451 | -9.92692 | -46.09935 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| de3feb35-a178-3699-863e-a18ab0d02e00 | -9.90375 | -44.79284 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d36b2905-4cdd-38e2-929c-c07a2d102e6d | -9.01676 | -45.12913 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 330af98a-5481-3ba4-9724-58c21da69793 | -8.2956 | -45.74268 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b23c2f21-3395-34f7-8ebc-bd177f62d10b | -9.91694 | -44.79115 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4efc0ebc-a52d-34e1-84a5-9a96210750b7 | -8.37264 | -44.76574 | 2026-10-08 16:18:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaeab338-ed6f-37ee-8de7-b4aab0aa854c | -9.02684 | -44.3699 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1ff6647f-ed73-34e5-bc5f-f48442438647 | -11.2703 | -45.20137 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| db44792e-a78c-3707-84eb-41c1dd3f4ff1 | -9.35685 | -46.58572 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3149c269-62b0-3910-b9ba-a7fd47b01208 | -11.13885 | -46.13536 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 3fe99add-6e93-3b48-9ada-e8b43a2615a2 | -8.95755 | -45.15176 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |
| dda50293-9e5e-35a5-a50d-c3280b1d1b9e | -8.7992 | -47.04373 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| bac7a319-c0e5-3c47-8ff9-0dc96e057a35 | -11.96012 | -47.76759 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0bc09d50-9ade-3df3-9df6-24a0c7194391 | -13.9789 | -43.25952 | 2026-10-08 16:18:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c20002c8-44a9-3e19-bf18-6f71ec9a3b35 | -9.02442 | -46.90686 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25a65a5b-86e9-34db-b902-6a926dfc4b43 | -8.8868 | -37.23072 | 2026-10-08 16:18:00 | NPP-375 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 69f487a5-ca83-3fc0-ae8f-15844b969c20 | -12.62171 | -47.89359 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89fff21e-b8d5-3308-ad4a-2f1c397bf223 | -11.60548 | -40.50671 | 2026-10-08 16:18:00 | NPP-375 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 011d540c-474c-3473-b397-2b45bfdfcd7c | -11.23716 | -44.02063 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4c9b3ab8-754f-30bc-b946-288549ffba14 | -14.24362 | -44.43238 | 2026-10-08 16:18:00 | NPP-375 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d76d510a-c7b9-3f7f-a992-598c27a1b042 | -10.46388 | -47.24459 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 64b0eecf-0fb3-3bdc-98c9-2027f347e287 | -9.02364 | -46.90097 | 2026-10-08 16:18:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ace88fe9-7e6f-3366-8826-3bb61dd92feb | -9.82352 | -45.76054 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9cddf3f7-e928-35c5-b31d-a81b1ae32487 | -8.28791 | -45.72134 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 10d9d8f7-7417-3d42-9bd9-b889fa9c0cb8 | -9.82484 | -45.77044 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 019d6e0b-826d-355b-a1ca-7fb62d591516 | -10.81652 | -47.3349 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2e5464bc-cea8-39db-9a15-28aab952991c | -11.21704 | -44.86832 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 89e13cf9-4357-3b9c-b59b-1e8e06c0331d | -9.53058 | -45.61463 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c91dacbb-38a8-3729-b49f-962b702e5a3b | -6.9047 | -35.74519 | 2026-10-08 16:18:00 | NPP-375 | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe2d58b4-1fa9-3979-9620-e490f8214d93 | -8.2852 | -45.73512 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0126f5e7-5056-3572-86da-f0feecd1a33d | -11.62567 | -43.69186 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8fb100b5-9126-3a5b-885c-9208279c95c5 | -9.13206 | -45.8307 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3983c9cd-20dc-3fbf-af73-bebc37d8f024 | -12.61165 | -44.54481 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e0509a2d-3b75-3705-baf5-db0a4e33fd1a | -10.93641 | -45.38592 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 21be0f10-1883-3a10-b674-8f352e48d75e | -10.07291 | -45.99417 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e0a0d4ab-a95b-3830-993f-485134961cb0 | -8.3295 | -45.03804 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9c692d5b-db5f-3598-8ffc-1512d4315a7e | -8.93278 | -45.16864 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f10d0717-d86c-38de-85d7-0051d10fd14a | -11.13816 | -46.12986 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| ef075672-a345-39c2-b259-ffc3f8db169d | -9.51301 | -46.84152 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7a51181c-ac89-385b-bb7e-2efb4d3aa862 | -8.30336 | -44.16901 | 2026-10-08 16:18:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 119b3024-f6cd-3aab-b710-9fab842ac5b0 | -8.28727 | -45.7168 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |


[Clique aqui para ver as próximas entradas](README261.md)
