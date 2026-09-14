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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ca54ed7-53ac-395d-bf5f-0a2781d4632e | -5.67476 | -45.53481 | 2026-09-14 15:48:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31f4a822-78ca-3ef3-9268-874da1fe3ac4 | -3.66567 | -40.56575 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 86e6f1ee-886b-3d64-84c2-0278566d367f | -6.80144 | -43.18469 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a87975ad-3642-347a-b950-b09356f9e0ee | -6.77505 | -42.74313 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7badd4c0-36f7-3b13-bbdc-00769a9f5707 | -8.83895 | -45.89697 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 634f7823-20ce-304a-8372-221616ec368c | -6.70687 | -43.14663 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d5069d4-178b-3074-86af-7b96d69f896d | -6.38246 | -44.88743 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a2a252b9-1c0f-3e78-9a14-9397af36e5bc | -8.49755 | -44.57689 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5c44697f-6758-3138-8f5a-73221f08b8bd | -7.0971 | -42.10787 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ea58d73f-3cd0-3ed6-bdce-55de8863c833 | -8.83807 | -45.88982 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 98a87748-a927-3150-9d1f-3abc34bbaf9e | -7.09022 | -41.81868 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 00509581-bd1d-3127-8571-b99b4cad2148 | -6.23383 | -45.9635 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ebfc17e6-1310-36d2-82e2-0c5029581538 | -6.64377 | -41.78091 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 499b886f-d4d9-31d4-855c-69603a34ec9c | -7.02306 | -44.63261 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 381024d6-388e-3348-bfe4-35721a85209f | -7.73978 | -44.72486 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 62998b6a-1e0d-362c-a59f-644381beedcf | -7.19708 | -46.12603 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f3b7a361-0df9-3a6d-ba04-64e3613aa5cf | -6.64634 | -41.77991 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fca93d40-5aac-3555-bbd8-5f98637179ea | -7.12273 | -41.78622 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fdbe7e72-4b06-38fb-9c65-bbed88d4ae7d | -6.98562 | -39.50915 | 2026-09-14 15:48:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 46a4cb60-5488-3da2-997a-22aaa78e70ec | -6.8289 | -43.51472 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ecdd7381-fbcc-3e93-9ea4-5357c49aeaf8 | -7.02342 | -44.64617 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f66c7cdf-1106-32c6-894d-553f4fc4983c | -6.34167 | -43.36636 | 2026-09-14 15:48:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 6dd069ba-eb6c-393c-82db-c85d47a6fc58 | -7.09228 | -42.11189 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 05c8b263-ddb9-34a0-8b56-d713f558359b | -5.92398 | -45.30801 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8788a961-94e6-3696-adbc-48e26a355d01 | -8.48811 | -44.57887 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a7facdae-06e5-34bc-824e-b9c5dd9ecc7e | -6.29266 | -41.68341 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0b4ec922-4506-31aa-ac35-a1f5a634cc77 | -5.19372 | -38.97235 | 2026-09-14 15:48:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 49c48d6d-8299-3317-8336-fc02590d964a | -7.17099 | -43.59265 | 2026-09-14 15:48:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c59dd51-9008-3f37-a861-b01d399757a5 | -7.0224 | -44.62777 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0d240e35-b9de-33ec-9e95-6ecb26d2c727 | -7.10932 | -41.80389 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 40925d4b-e6c2-3251-827d-40cb36bbd857 | -8.48456 | -44.85581 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e43d419-361e-386b-9dcb-bceb38511916 | -6.77135 | -42.7574 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ac4f6660-90ad-33e2-a7eb-c967bbc01218 | -7.14296 | -43.42835 | 2026-09-14 15:48:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 744b1e4e-ac6a-35c8-943d-393c3520afc3 | -7.04454 | -45.28005 | 2026-09-14 15:48:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| df9ae0f7-1806-3c7b-b93a-fd7a3b3d448a | -8.07946 | -44.02705 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a73d3517-c2e1-36b1-ae12-894acc62dbf1 | -6.09758 | -45.47289 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc898a5d-ed2d-30c6-a225-0c327f7f1e49 | -5.41017 | -42.2262 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 881e0f20-b621-3d8b-a8e2-f361ccde25e1 | -7.97293 | -43.97897 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f10d254b-2ebc-3b12-b1a5-f040cd3182cd | -6.78889 | -42.88774 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| feeff206-6376-350a-a8de-94767ab47913 | -5.1138 | -40.61342 | 2026-09-14 15:48:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 64aa5392-634d-33ac-9ef4-61ff6c414af5 | -7.17325 | -43.60938 | 2026-09-14 15:48:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce67fd7e-41dd-35f3-8792-790aace9af2e | -4.45888 | -39.35563 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| b8fd0128-66f5-3024-968f-80d83da797e1 | -6.62282 | -41.68242 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f21a7314-00f8-34f9-b3d5-21817f5b543f | -9.87066 | -45.96509 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b148d6f2-7896-3d5e-8cc9-b9e23da3af4d | -5.18062 | -40.68283 | 2026-09-14 15:48:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2fe3ba85-8c75-368b-8e69-ede0edf69dff | -3.70393 | -41.7162 | 2026-09-14 15:48:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 429058e8-0258-3abe-9c12-8e9f23027a68 | -7.02372 | -44.63749 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0b26a976-08df-3b38-9e72-4892bafed800 | -9.94036 | -45.78151 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 26203ac2-510f-3b23-afc3-6a3e83e80efb | -7.61569 | -45.19662 | 2026-09-14 15:48:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5b0f40ec-d39d-377d-a120-2afc2a422b1b | -6.2385 | -45.9735 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d69647e1-a9a8-30c6-828c-2e700f919493 | -7.55794 | -41.83788 | 2026-09-14 15:48:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1cc5b506-f41f-3ca2-9eb5-57039bb49252 | -3.92795 | -42.99082 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 2cb6aa20-7730-3a13-bd32-cca7271abb7c | -6.87374 | -38.73578 | 2026-09-14 15:48:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 6ac7804e-149b-39f2-9e88-302881a1dc30 | -7.0908 | -41.78377 | 2026-09-14 15:48:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 111498c3-d419-31cf-bdba-41044baabb97 | -5.19222 | -41.70896 | 2026-09-14 15:48:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 260b5e8d-eb94-3e1d-b02d-d70e44a557e2 | -6.58016 | -44.82674 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 583f839c-ee93-3bef-924a-53c349fa42e8 | -8.84001 | -38.77248 | 2026-09-14 15:48:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b0ae62a4-4a3d-3e16-981f-2efc7aadf26e | -3.44571 | -39.14994 | 2026-09-14 15:48:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 65aab301-cd69-3a95-8169-b80365c7a693 | -7.48867 | -44.89083 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2905890e-1ee9-3b41-bc0f-03c02e39b702 | -7.60271 | -45.19786 | 2026-09-14 15:48:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4d3cb2d-fb5d-3507-bd11-695ccc97078b | -5.23682 | -37.9106 | 2026-09-14 15:48:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 38cc25b0-d3e4-33e3-a66a-760b03ccc051 | -7.56362 | -41.84058 | 2026-09-14 15:48:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3f3b4fd7-e034-3c9d-950d-74d329548322 | -7.96146 | -43.98534 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 52c02e5e-feb3-3906-8b05-3a17818cf4a2 | -7.48801 | -44.88593 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b41e3bad-5e00-36d6-9f30-6adbd666d9de | -9.98664 | -45.87565 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aeddbd61-527d-3d6b-bec2-f9611b6f9a02 | -7.34475 | -46.79554 | 2026-09-14 15:48:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7f3824a-6d50-3d62-8757-de8751251b1a | -6.68626 | -44.82533 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3accb706-c9e3-3408-99e1-b58f8e8bd20a | -4.97894 | -37.38558 | 2026-09-14 15:48:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 32.9 |
| cff1b7a8-e1e5-348e-b8b5-efa1943205cb | -4.38167 | -39.24199 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 248f2332-3117-3d31-9e5a-d2b9430d1e75 | -7.56025 | -44.92336 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| aa001442-d32e-3637-8a0a-8d2466aa628d | -3.49436 | -39.36002 | 2026-09-14 15:48:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 964cb3b6-eca2-3531-9ad6-8a99028869e2 | -7.02175 | -44.62297 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b912394c-3468-3687-86c0-10f481e13131 | -6.12428 | -44.68902 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 74441874-22c9-35fd-a9c4-3ac4c98d7347 | -8.58943 | -44.49192 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 49c8b643-8ba4-3d8d-bd60-e50eb1930ce1 | -6.34113 | -43.36234 | 2026-09-14 15:48:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 421125d7-8fc8-3a56-a78a-b49a5e5ec884 | -7.56094 | -44.92869 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 982c7534-0a06-3ce7-819a-feeb7b71e02f | -9.98816 | -45.88857 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| acea8995-219d-3f7f-8699-af5fcbfaecd2 | -6.21303 | -46.88383 | 2026-09-14 15:48:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 842848fa-1ad0-303c-a350-5c95a9e2d9b2 | -7.21039 | -46.18579 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 84c3f12f-0eb5-3381-91fa-5e92acf93e86 | -3.96832 | -43.12024 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 357d57ea-391e-3263-b362-f03850df8657 | -6.62633 | -45.12324 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 65eb73cd-a8a4-3855-ac1d-11824e87fd81 | -6.61335 | -42.21167 | 2026-09-14 15:48:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5c016994-f175-3768-b93f-5edd392f013f | -5.18721 | -41.70961 | 2026-09-14 15:48:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 62469909-ca51-352d-9ed1-118a9f0d68fb | -7.28269 | -42.29758 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a0447587-6aea-3606-a046-3f9e056e32c6 | -10.08843 | -45.55472 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2d27bc00-b764-3b6c-a6a4-7d3971adcf4b | -6.46638 | -43.72279 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3abc7c3-c5d8-3a10-86e2-0b0c64d2f9c3 | -8.8123 | -46.5953 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| da82363c-cbc8-3661-9219-39ebe4f5a811 | -6.11813 | -44.69004 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2cce8d4c-3a65-357c-ae2a-fd836d0720a5 | -7.27312 | -44.12465 | 2026-09-14 15:48:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9e4f388-74d5-331d-980e-339f3cc760fb | -7.02279 | -44.64123 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 514b2810-2648-36e9-b815-d558d6fe64dc | -7.09499 | -41.81495 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7e847ff0-b6d7-3680-a44c-5e47241f9494 | -5.40926 | -45.85893 | 2026-09-14 15:48:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 09dca480-f219-39c3-9eaa-ad0ad1e58c19 | -6.2302 | -45.96245 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3cc97d9d-126d-302f-89c5-b12979497214 | -7.15957 | -42.0959 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c672aad4-af1c-31fc-9b4a-bdee8ee973e7 | -6.79701 | -43.75639 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b9c34b0b-4363-3cec-ae2a-c5bf5708447e | -7.09164 | -41.79 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 8c406205-63e2-383e-b9b2-e64b5d080f25 | -6.57342 | -43.16211 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 354582b2-ed26-3efe-a565-96c9c06b2d0b | -7.10629 | -42.09975 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f13f9e05-569b-34c6-add1-8a88f94b9adf | -6.53294 | -44.09228 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 89e8f78d-92fe-3363-89f4-2f34abd60b7f | -7.1618 | -42.11234 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |


[Clique aqui para ver as próximas entradas](README87.md)
