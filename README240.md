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

## Dados Diários - Página 240

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e2a3469-df8e-3d1f-afef-75a37646ad1f | -7.18893 | -44.34159 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a95a5bc-fdb9-3fd9-bc47-770e6012ebf1 | -8.59628 | -44.87357 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f59e35bd-b16f-3d72-81da-23bc818acdb5 | -9.7579 | -44.79147 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eeb583fa-b22a-3b2e-bcd8-cdf040b6eb37 | -7.91768 | -41.13549 | 2026-10-08 15:41:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b1a10f95-6365-342b-b52c-1f7a8bbf7515 | -5.74188 | -42.06921 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f424a896-4f36-371d-aeef-4dca30a67d36 | -6.9345 | -43.67055 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 167933f2-2204-3fdd-bfde-ce7c669cc7fa | -7.48332 | -42.8311 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 91287829-238e-390c-8a7d-23b5ea8f3fd7 | -8.21847 | -46.37616 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 7b25fcd6-16ff-3625-a56f-4f975904f938 | -7.7606 | -44.16513 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 34e44ea7-7239-3e90-8980-3aff1106d6c8 | -6.30988 | -46.41204 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09daa402-72da-37f7-93a9-c44b1ed915b6 | -6.67931 | -45.35938 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b26c8167-9049-33ec-a126-a34751a6e298 | -11.20658 | -44.86811 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 079b8983-4807-3d98-bb21-a1eb2088522d | -8.20592 | -46.38958 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| ad530346-b02b-3794-a59f-bc25ddc2a2e8 | -11.23512 | -44.84341 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c709725-bdd4-3384-b3b5-de39bd2d5bac | -11.01262 | -45.43385 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| acaae4f8-d2cc-3135-8d54-f16f178e7265 | -6.15793 | -39.43677 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 1dd9fc6e-0d40-3533-a789-f040f7c6c975 | -10.60497 | -43.84133 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 430bc4cd-6821-3fb5-bbe5-41b30a929df9 | -10.38315 | -46.3133 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2dba966c-e0b3-3723-a87b-0fb9fe6f48ca | -6.40623 | -44.94778 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b46b90d8-7e3f-3692-ae08-403b004471ed | -5.71066 | -41.67134 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7806d056-fb30-3a05-8bbd-92b5ab94ff37 | -8.8071 | -45.80113 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| dae6dd52-ba9d-3039-8be9-ad90a3a66eb4 | -9.802 | -44.77475 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7502c533-300d-36cd-908a-7ed77ffca7eb | -5.99514 | -43.61501 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58faac69-0517-3523-a147-0d66a6f2ce69 | -7.25686 | -39.40733 | 2026-10-08 15:41:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 86aa1906-c819-3836-afee-9a1648b85d22 | -6.49665 | -41.83469 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 17158bfc-bade-30f8-85a0-c8c94703831f | -9.77344 | -45.88572 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4ce05417-6beb-34c7-a9cb-35c9023b7263 | -7.47518 | -42.85433 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 1d4359f0-438a-3969-9271-c3e7291fc58c | -6.58835 | -41.54763 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d34ba6c6-78a7-3c1a-bc58-71fdff0be34d | -7.06239 | -40.94282 | 2026-10-08 15:41:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 305ace47-4d3f-3893-9b40-614a9af36c5d | -6.33755 | -35.12456 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1923275b-4b84-3090-b922-32ef600708ca | -6.90295 | -45.89401 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 712be42d-b31c-3bc9-9903-bdfd42092c2e | -7.60802 | -44.8145 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6b309683-b042-3cb9-bd76-189cba90c31e | -4.57477 | -38.94959 | 2026-10-08 15:41:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 76f40248-a5f6-3d10-bf2c-d59f3af5cf5d | -6.93115 | -45.26284 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 793d31e0-58b9-3eed-bba3-a46810bb526e | -7.46047 | -42.82963 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 71d7b1ff-da3f-366a-9c66-44e011315a5e | -7.69218 | -44.74566 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dfe782da-fe5a-35e1-b998-bc917fed1200 | -6.15816 | -42.58346 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 2c32bd2c-b2c9-3b15-8c76-2a81eb0693ba | -7.0036 | -43.4381 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5d709efb-5674-3f4b-b0dd-7652ad537f9e | -5.71607 | -41.63823 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 249e108d-7f2e-3c46-9d26-1485219078b6 | -5.74528 | -42.05627 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 1af83654-da2e-37e7-9d9b-fdb064872ec1 | -5.9644 | -40.92215 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 693759c2-8f41-367f-a3a0-9686240f4dc4 | -10.93052 | -45.3951 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 19ad5fc1-1e03-3fd7-b478-189317fd853f | -8.59158 | -45.69265 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 560b40ae-9a34-3a21-9051-2349afdee6d4 | -7.08018 | -35.02853 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 20dc5a6f-59de-3f1b-8408-8037490a6cc1 | -4.93485 | -42.81143 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cb0059ce-6356-3ff6-9017-3941ca0fae74 | -5.48865 | -41.40071 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ffaca78c-4bf8-36cc-8414-7415303914a1 | -6.36006 | -44.50783 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9744d49-8840-3112-a412-7fa296900918 | -8.19047 | -46.37962 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ba8d9bfd-6447-353f-b816-261489ee6eb3 | -9.45952 | -44.62179 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 089ea628-7ce7-393e-89a0-9ae4a2f669e8 | -9.53278 | -45.62617 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d182f812-10e7-30a2-9b75-f5e63f066add | -7.34884 | -44.36864 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ffb1f25-1acb-393b-ac94-046b8a2e80d0 | -6.05946 | -42.9178 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ac3ae973-7f9b-36c2-9145-a83c6ae599b3 | -8.20145 | -46.41084 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 386.6 |
| 032a3afa-e2bc-3245-a797-aa73ca3c6e78 | -5.6263 | -43.04235 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3128800a-5248-38ac-92d6-a534d67ea1be | -7.25075 | -43.50924 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b931def5-02b1-3de6-8810-0ce23a83c14e | -9.0836 | -45.11621 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d45395d3-fe52-3e45-a1cb-7b1e4ce17e72 | -5.02258 | -42.44468 | 2026-10-08 15:41:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 387ecedb-9446-37ea-94ec-d3f227bae62a | -6.57183 | -41.60876 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 26e596f2-521c-3bf7-8676-ad477aa34237 | -5.71294 | -41.65071 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c214d4ae-4c89-3211-beec-388f9fef4e78 | -7.39334 | -44.47049 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 808ca120-79ec-32fd-bcb6-4c43605a39c3 | -11.2647 | -45.19266 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 17d11fef-dce7-3afd-a345-04024728612f | -7.21744 | -44.27589 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e36d08e-c89e-3b25-bd2b-1069ca86d4bc | -6.36989 | -44.44276 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d6e4a07-6adc-3291-a2e9-1158ba7a1d21 | -7.82098 | -44.57709 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9eeecb41-a324-31ea-a619-5b9c1f7ac737 | -9.89104 | -44.85391 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 30355eff-cbf9-3aca-b8f0-11d247a1f54b | -10.16061 | -44.67738 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| df348602-4a4e-3842-a35c-c44cad641d45 | -6.85192 | -41.7534 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 112fafe8-7b25-316d-bbf4-6522bf7c0938 | -6.32815 | -43.83092 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 495f224a-f5bb-39a0-8ce8-e49944075277 | -10.22333 | -40.04633 | 2026-10-08 15:41:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 6b7c0f35-dc81-3a79-aa51-fe1d4458281e | -9.43188 | -41.7386 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9a565f86-73d5-3b41-908a-b0a2b286c519 | -5.44273 | -45.67997 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e5d9fa54-49bc-3e18-b513-d4e4d82ece73 | -7.76722 | -44.17552 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e304d0e7-97fc-3fbe-bd11-be094bbddb6f | -6.72747 | -45.18142 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c9489e1b-1b76-33d0-a1cc-91c5a63970e4 | -5.67835 | -43.41805 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed554eba-0959-3bd7-b9e1-0b5516bcb97c | -5.73478 | -41.77245 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 114eb581-754c-3900-9948-5cc97b8ddf24 | -5.88081 | -43.46176 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a756f7ea-7eb2-36fe-b1d5-5969aa368274 | -6.36612 | -45.5958 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8196cb90-59b5-3000-bf37-92155e6c74be | -7.7526 | -43.81652 | 2026-10-08 15:41:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5e717de2-bd5c-32f9-8468-e2689c355c33 | -7.05482 | -44.32622 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d3fc0f20-df14-3a79-847a-9c3de7204018 | -9.43719 | -41.73792 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 8926d0ec-fe89-393e-9b5c-7462358739ac | -5.62332 | -43.06126 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 008d8850-bbcb-3c89-8579-75165a94d3c0 | -6.83804 | -39.56194 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0660742e-3b41-3646-a3cf-104cf20b75cb | -7.26733 | -45.34846 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b90f8766-266e-303c-b0a9-baa8f750cd44 | -6.46946 | -44.03522 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6385e1f9-e4aa-3554-9fdb-e14fd3379716 | -5.74264 | -41.71771 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0f2c21d1-a54c-3923-95d5-7e36ba01f63c | -10.87211 | -45.5586 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 72cfebd1-c2ff-32ce-8b36-8dd87c80c2e9 | -6.61579 | -37.8954 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 8515b143-7a20-3a25-b614-f98094e8ce65 | -5.95349 | -44.26757 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae80adf3-1393-308b-9fb9-7482948dedda | -11.20265 | -45.21239 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 21715861-2521-380f-b012-ac04dd0a1bcd | -6.84675 | -41.75384 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 2a609dcc-5876-360d-ba90-90731717b83b | -10.16611 | -44.67203 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| eae4b2b9-171e-3bdf-823e-6f6864401b9a | -7.87063 | -44.14552 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e209eb5d-7964-3da1-a6e1-c99f3d550cf1 | -6.92232 | -45.88609 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 189018a3-fcca-392d-80a8-60381ec89583 | -6.70179 | -45.28141 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f769ddf7-9b4d-31cb-ba0e-6ef3f1263483 | -11.21719 | -44.86354 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 567e0909-87c4-3662-9567-a6cd3831d347 | -8.4013 | -38.85104 | 2026-10-08 15:41:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 60bcee55-874a-3d6d-baa2-d7cc9fec1dea | -5.95698 | -40.93883 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f878ee57-7bdc-3a9c-a143-f93896b2dc25 | -9.43835 | -44.60808 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2f17e657-4464-39e6-8c2a-4ff33b967766 | -8.93021 | -40.27391 | 2026-10-08 15:41:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e5817fdb-3df2-306d-8458-f9b29e0d7d78 | -9.5313 | -45.61346 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README241.md)
