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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9de390ff-8365-397b-b73d-4d36c8e8ebe6 | -9.9054 | -45.95298 | 2025-10-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9008d4b5-2ca2-37f3-8b73-77bd7a6efd56 | -12.18753 | -45.09419 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c65ee8-27be-35d0-aff9-25a49bb75d2c | -16.78482 | -42.75824 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e6f412b8-c535-3eb4-bfb1-656638678ca9 | -10.85975 | -43.94221 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dffe106f-b128-31a3-855f-73b5812b637a | -9.89302 | -47.65943 | 2025-10-19 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7333bb50-850c-3430-992d-4573aa8232e6 | -16.7865 | -42.82351 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b38981dc-5cb0-30b5-8cb4-743e6d340aa9 | -12.98787 | -47.26497 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfbcb984-f558-3818-a1db-9bb5812cecfd | -10.53925 | -44.50725 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f24805-38e7-32bb-ba23-78f8e1269adb | -10.91116 | -43.82167 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2c4656b-2781-3361-925c-e91f59d85198 | -15.51498 | -41.54063 | 2025-10-19 03:45:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61b3d0f7-3603-37a7-93a4-57810d133695 | -15.52613 | -41.67829 | 2025-10-19 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8bf387b5-7e7c-33d5-b888-4f05c6a2c47d | -10.68114 | -44.54973 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99c2b98-20f8-3dec-b9c9-b449426c932d | -10.88995 | -46.08074 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1497a63f-e5e4-3a07-8463-4ca22c293732 | -13.93607 | -45.60995 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b8c81eb-d7ba-3b12-b9a9-5980f262c01e | -10.22413 | -44.06238 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df951e04-a0e5-3bac-93d8-563af3901336 | -13.93099 | -45.609 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48e3bbbd-ee15-39e3-98d1-886a3c190c1b | -13.88457 | -45.47041 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e83f39f-aca3-300f-b74e-3db521cc2113 | -16.78985 | -41.46838 | 2025-10-19 03:45:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a10aefbf-4e8d-33a4-bb7f-5b3bdc6f1c60 | -13.93786 | -45.60061 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e4eceeb-0efc-3de1-bca0-687c17233917 | -16.81056 | -42.82848 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6dde3047-01f3-330c-a3c8-0584dfbbeec6 | -15.02775 | -46.61441 | 2025-10-19 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 548af6bf-d479-3ee6-b14e-68edcad7f869 | -16.80324 | -42.82302 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1b7827b-0071-3326-99c1-43caaf771a6a | -12.6921 | -46.96018 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97c1712e-f498-37f9-9926-e2eebcafc879 | -14.74571 | -42.46043 | 2025-10-19 03:45:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7e69123-8270-344c-8fb3-7fb02b7b9d45 | -11.89503 | -45.43913 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b94744f-c1bd-3ec8-b71f-492431efa44c | -13.86057 | -45.4643 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb1f5b5b-6701-3081-b745-402fb74c0169 | -10.95639 | -45.46916 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85c76c9e-eede-3ca2-a4a1-57047ae8092d | -15.32271 | -41.73975 | 2025-10-19 03:45:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 459d23f1-1a94-3719-97af-aa47e6801665 | -15.51461 | -41.67635 | 2025-10-19 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ad6e1c6-c36e-32a8-9e0d-b90d5aee01f6 | -15.25791 | -43.57523 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aebe795-6697-3590-a770-18b068e3aa0f | -10.71991 | -44.53638 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f840666d-d8f8-3235-a3b7-01f69b38c1aa | -11.63841 | -44.08558 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef597517-e854-352b-b820-bef1b2d6fb7c | -16.78021 | -42.76085 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b88c7932-5aa2-37e5-b230-6d1864d2ce2c | -14.13661 | -44.68604 | 2025-10-19 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35bf675d-dcd4-3cb6-aac8-79de1b3b25b9 | -16.76214 | -42.76912 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a06d043d-17ad-3db3-8d26-cdb4dbe57332 | -12.1515 | -45.06308 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c0463f0-d6bd-379f-9aa5-aae48352298b | -16.7749 | -42.76736 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 94d87c84-69fe-3700-881a-95f71ebcae38 | -12.46074 | -45.4302 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 68e534c1-2e2c-3af6-bef5-263948d07ecc | -10.97578 | -42.29357 | 2025-10-19 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9968bf68-4b8b-30c7-ba0f-985622058625 | -13.62364 | -44.10291 | 2025-10-19 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da70898f-d7c7-3c9d-8395-e5c1ed9a7e4d | -13.95975 | -41.7197 | 2025-10-19 03:45:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 032681d5-30a4-3279-a1a6-2b91c521a610 | -10.53202 | -47.76659 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b835e09-05f1-3d10-8bb9-0fee16fee2b4 | -10.12749 | -44.52972 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c29bf070-9506-3b16-b7be-664897ded511 | -12.44947 | -44.74507 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a5a2949-7d2a-331f-8cb2-e40d980fee09 | -16.75489 | -42.78631 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ebcfaa51-96b5-3e65-8a72-da107c8ab013 | -16.75748 | -42.77196 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e7de568-5587-319b-9795-cbfd51bf9efb | -10.12471 | -45.51547 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94e5e20a-7492-3cbc-aeab-f58117c71512 | -10.53424 | -44.50629 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d2e111c-4e78-318d-bb35-29f44a2b60f2 | -12.18803 | -45.09156 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 301485a4-8aa8-3c48-9319-6d6d6a0d5cdd | -10.30348 | -44.04268 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 383322bb-be42-377f-9699-f5df791d4f94 | -9.98691 | -47.05444 | 2025-10-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e272dcb-7370-34f2-bea6-bcca15ecb7da | -16.75891 | -42.78704 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be11ce65-3af1-34cd-ad2a-525040074807 | -12.47106 | -45.43203 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2348d035-dee2-3b43-98bd-c2aa7247ec5a | -12.47265 | -45.43325 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84be9ff9-9274-3836-90fe-ec84a142d192 | -10.53221 | -44.1459 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 476d65bd-feaa-367b-8e0e-09bd696b3d58 | -12.33953 | -41.38615 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aae73a76-3069-31c0-b2c1-03cc77b1fd6a | -12.45836 | -45.44286 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3314e73d-9920-3f91-8a37-fca82244dd92 | -10.95712 | -45.4654 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1be4dae7-f9a5-35ac-a351-975ed9644b46 | -10.55705 | -43.38939 | 2025-10-19 03:45:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 20705076-977c-3562-976b-4e66f9b42561 | -10.72435 | -44.54037 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7128ba9a-0002-3fbe-a601-080324ed7e4e | -10.6815 | -44.54877 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0abd70f6-9a6f-3b25-819c-6fc1c9c6e917 | -15.79339 | -43.25292 | 2025-10-19 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b837fcc-feec-3f10-9586-d0f5da6bd3f8 | -12.18703 | -45.09686 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f57d492f-136e-3056-a457-56b800a7c9ec | -10.81862 | -43.92323 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e101c17-995e-30d0-901c-67d9a0800fd6 | -10.68704 | -44.54677 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 924570a5-e187-32f8-aa7a-865dc34b09f4 | -14.09164 | -43.6196 | 2025-10-19 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae2be10a-636c-3664-8659-ca4d6965c6d3 | -13.71151 | -40.98347 | 2025-10-19 03:45:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4bb4df60-744e-3e8d-bb70-7dcc312d504d | -16.82289 | -41.81493 | 2025-10-19 03:45:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4cd6eaef-1f6b-3376-ba9a-4a186962497f | -16.03746 | -42.36986 | 2025-10-19 03:45:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be896e28-a228-33da-adfd-b3502e12daed | -11.64223 | -44.09179 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e619efcf-b1ff-39a3-84b9-f9b928573244 | -12.98705 | -47.26903 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 513f60e4-8ec7-3e29-8de4-a4d36656a846 | -12.99106 | -47.27315 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b4e4f5d-9ffb-32b5-8222-eb69adcf5745 | -11.89445 | -45.44219 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c6b8ff4-c8cf-33fc-9728-e85bdbbee9fd | -12.33865 | -41.39122 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8327c0ae-171d-35d9-b64d-22c75e4be96f | -12.45499 | -45.43239 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 050c0505-f47e-3b0e-b127-2019d0e389b9 | -16.81122 | -42.82484 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc5a95e5-76ce-3af0-9240-6d3650a70eb7 | -16.78522 | -42.80802 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60ca370a-afdf-3d0a-8cf9-34c45e4f1dbb | -11.78189 | -47.54986 | 2025-10-19 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 580a0114-a6bd-3448-bfc8-18daff971d44 | -10.11931 | -45.51451 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d329c47-2bae-3f32-9217-8cf4c57ae5e0 | -15.79385 | -43.64909 | 2025-10-19 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18baae3d-f477-34c2-8fcd-2eaf8b4a9e37 | -13.89579 | -43.45008 | 2025-10-19 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d97f51de-23fa-39ab-bd7b-935341592ab3 | -12.65617 | -41.25687 | 2025-10-19 03:45:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 427f7257-adde-3324-b777-311f860bcf70 | -16.97903 | -41.15667 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 0d9d86db-113f-332d-9d0e-a80a220829c1 | -13.01914 | -46.94944 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bf8a84bd-eec0-32fb-9321-66323cbcb295 | -16.78528 | -42.76299 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0765ed80-7fcc-39b8-a9b2-8343b82bfae5 | -10.22519 | -44.05672 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff0576ea-3f1a-3c31-a4a0-61c6249026f9 | -11.14574 | -47.7117 | 2025-10-19 03:45:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7542fc51-2e49-36e4-aa56-bdd47b58975c | -13.92651 | -45.60497 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1203516-8d77-35b1-85c7-925aedf32e60 | -16.75087 | -42.78558 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e0958359-c7bf-3824-9f27-ecaec716f305 | -15.56695 | -42.35326 | 2025-10-19 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ab59c7c-c2c6-3ba0-9ab0-eb1e7b8f9320 | -18.13054 | -41.50132 | 2025-10-19 03:47:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e11024a-50ac-3444-af02-61a01e6203c6 | -18.91448 | -40.0846 | 2025-10-19 03:47:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d62b5e66-259a-3a12-b2ba-16ae29828aa9 | -18.1269 | -41.50058 | 2025-10-19 03:47:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef4c7cf8-9633-3aa0-8d62-08bb9127a461 | -4.82 | -43.0294 | 2025-10-19 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 67929759-f2c5-31b3-927e-eaae74db1b7f | -8.6032 | -40.1834 | 2025-10-19 03:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 086cb7a4-4ec6-3ce8-b697-f50c32c42971 | -4.8389 | -43.0047 | 2025-10-19 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1f6d883d-584d-3ba5-a55f-86a4bbed9d87 | -2.6841 | -49.5427 | 2025-10-19 03:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 5c64e8ee-0ce4-343e-9cb8-4de60afcd38f | -8.6029 | -40.2083 | 2025-10-19 03:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 16cbe5b8-f68a-3f26-9647-6a1056b9423e | -4.8388 | -43.0282 | 2025-10-19 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 36b13439-f500-3e83-9050-973406976466 | -10.8891 | -46.0814 | 2025-10-19 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |


[Clique aqui para ver as próximas entradas](README18.md)
