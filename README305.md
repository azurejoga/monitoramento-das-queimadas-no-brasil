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

## Dados Diários - Página 305

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9db9dc0b-198d-37e0-bc7b-f66f3a60ded7 | -16.34746 | -50.0994 | 2026-10-08 16:35:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b88a3a43-801d-3871-8b0e-859ccc5b4f8f | -16.85552 | -40.56371 | 2026-10-08 16:35:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9db141e6-8352-3026-b3d7-882b0fe74209 | -15.0908 | -41.35341 | 2026-10-08 16:35:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| ccfe9cc3-bf04-3693-be72-4f51ff6d0d41 | -15.79197 | -44.68635 | 2026-10-08 16:35:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 12908cde-800a-3ee9-9b91-bdf5f7c42d80 | -17.46949 | -42.71563 | 2026-10-08 16:35:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9480f494-4913-34d0-9587-a1a104da36a5 | -16.93171 | -42.10291 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fcafb290-98ec-3978-b84d-2a485b87b87c | -15.56314 | -44.51572 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 157ce463-be2b-3721-b3c8-2da4fbdcb13f | -20.74876 | -44.3745 | 2026-10-08 16:35:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 18a6505a-253c-3358-91c6-73114024f77e | -15.85768 | -40.79629 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| aabca8ee-2ca6-3eb8-b51a-c2f5008afb1d | -14.73531 | -41.79171 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d0d41408-751f-3b4a-aa61-b59ff66704db | -15.63025 | -40.12696 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| cb8e3e71-8cdf-3a1e-a519-fb8e61aca8f9 | -15.5725 | -44.53272 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a7bf6676-1fa7-3e61-8a56-664d548135ea | -15.6915 | -40.47093 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 8e65f1fb-dcde-346b-bed9-6e3386fdb240 | -17.18344 | -48.83058 | 2026-10-08 16:35:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 437468e2-98e8-34b7-9aa6-00612f1ed030 | -16.55876 | -51.0682 | 2026-10-08 16:35:00 | NOAA-20 | AMORINÓPOLIS | GOIÁS | Brasil | 5200902 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 25473daf-358d-3952-8133-cbb57b851659 | -16.03012 | -39.82031 | 2026-10-08 16:35:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a493953c-93e3-37be-9949-2327cb1e9ec8 | -14.79834 | -39.84657 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ef0b5e6b-99a3-3425-b2bd-6f4c5e38cac8 | -15.24223 | -40.91544 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2ae61796-779f-3d02-aded-a66b12d9c0f7 | -16.65452 | -48.24663 | 2026-10-08 16:35:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bd011f8-96c0-3f97-9597-c5cdc21002c6 | -16.6911 | -42.52007 | 2026-10-08 16:35:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0132df46-ec64-3926-9944-8ebd6be272c0 | -22.07134 | -47.30658 | 2026-10-08 16:35:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 94523d64-2f2a-322f-8f50-10d13e1de1b6 | -15.57529 | -44.52859 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 7797583b-7b1c-32b5-99ef-8ed28bb7b4b9 | -13.95255 | -44.85394 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1fd39187-851f-354c-9f47-284177afc97e | -15.31331 | -40.64949 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b53bc377-8fb3-3b50-9b65-458e2a41c774 | -14.26153 | -42.4404 | 2026-10-08 16:35:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8f79106f-933f-3e06-9ebc-670ef51a5ab7 | -15.88331 | -40.77968 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| f9f503c7-5abd-386a-9805-29a319f80e35 | -15.38452 | -40.76529 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e0690000-5e6c-3db8-a754-7040e3aca490 | -19.47602 | -40.01012 | 2026-10-08 16:35:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 316bc888-85d9-30fd-bd66-3e3ebb4592ba | -20.95154 | -44.17639 | 2026-10-08 16:35:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d4e46e68-3846-3c6a-873b-c21efead2404 | -15.32052 | -40.64829 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.9 |
| 8d3680e5-c6cc-3cd5-99f3-38e719f54300 | -15.56637 | -42.90131 | 2026-10-08 16:35:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7c4a4bc9-59d5-399f-875f-7fb217047366 | -17.18879 | -44.43763 | 2026-10-08 16:35:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3981553c-537f-3068-9403-8e0e4243fd6f | -17.11031 | -41.38047 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3fe17041-091b-3a01-a5ba-5ec6c1728b31 | -15.39443 | -44.34083 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a7431ea4-8e17-382a-b063-c4105bfd7f1e | -18.04214 | -49.55758 | 2026-10-08 16:35:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 61abec07-5b4b-3a2a-a537-d6b108a9a4e1 | -14.6617 | -40.97422 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e4d3522e-e0bd-3dea-8c40-fb17fd36e21c | -15.1666 | -48.22367 | 2026-10-08 16:35:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f547ff7-552a-3618-904d-88a681e93a2d | -16.94803 | -49.02219 | 2026-10-08 16:35:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c57d130-7079-3d5d-99d3-0fea92db5e93 | -15.31982 | -40.64412 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 5e64d51d-af6a-3a2d-91ad-35df6050fefb | -14.43916 | -43.92549 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fb2289ac-cdaf-32f4-9727-4b26af4d7541 | -16.72001 | -44.89856 | 2026-10-08 16:35:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a0bf5b-8046-397b-8a10-39953e43e07e | -15.42695 | -42.68589 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 237c4af4-7698-3470-b81d-c124d06a42f0 | -15.77098 | -40.34072 | 2026-10-08 16:35:00 | NOAA-20 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0d955455-0d3e-3d75-b32f-fc30b1f1dac8 | -14.76442 | -39.80816 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| c957795a-84ec-3b33-a2cd-23c79b170467 | -15.68102 | -50.57113 | 2026-10-08 16:35:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 928f5e4b-e109-3d02-97ec-de98b71eaff6 | -20.95136 | -44.77277 | 2026-10-08 16:35:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3dff9a6d-b5cf-3540-a74a-d11e143d7fd8 | -15.79576 | -39.52517 | 2026-10-08 16:35:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6b61e397-caf5-3b34-9688-121ab4ef464f | -21.65852 | -42.46177 | 2026-10-08 16:35:00 | NOAA-20 | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37f49b6c-c252-3ff1-98e6-170cc3ba9ca6 | -14.79083 | -39.91636 | 2026-10-08 16:35:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 14cc0b62-feb8-3e4a-acf1-05cc976bb5cf | -15.64363 | -42.42165 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6676195c-a4bb-3ce6-b097-ea29d3506327 | -13.3456 | -38.9878 | 2026-10-08 16:35:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2fb8230c-7b8c-373b-accf-13cdacefbe38 | -14.53446 | -41.67646 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| cb9362bc-fdda-3c7d-ad1e-dcba87e3cbbc | -13.45495 | -41.92134 | 2026-10-08 16:35:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 471204d6-8a02-3d35-a691-3cafce1aa6fa | -14.05457 | -43.8297 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 296.7 |
| f301b519-5327-31b9-9661-cb1552472b75 | -15.51663 | -42.6522 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| a57545ef-ba21-3041-b2eb-50c90d735343 | -14.05824 | -43.54748 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3dc05b4d-3345-32ee-b603-345ad8473ca4 | -16.45946 | -41.26009 | 2026-10-08 16:35:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d61b4908-59d1-3c89-85bb-4d24dbd18563 | -15.99486 | -53.69884 | 2026-10-08 16:35:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b9dd49d2-dcd4-3c82-827e-329dc32d675e | -17.03358 | -42.3634 | 2026-10-08 16:35:00 | NOAA-20 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cef20f2a-dfc1-3680-8731-028850072db8 | -15.69527 | -40.46688 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| e8924608-333d-3dea-9143-7dadd854c9be | -15.02289 | -42.26427 | 2026-10-08 16:35:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 60c266d8-9c70-3bd6-a0b6-c6886f295a5f | -15.34788 | -41.71487 | 2026-10-08 16:35:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d57ccc8f-2461-3126-8c16-9ae821f8a27c | -14.11459 | -39.22223 | 2026-10-08 16:35:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ae2cab32-7ac4-37b9-89e9-cfb1f42b2698 | -16.12506 | -43.74653 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| f789a82b-e236-3ca4-af28-151744a9967b | -23.32214 | -52.31395 | 2026-10-08 16:35:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8df049c9-4401-3e80-ad35-97244453a67b | -15.45053 | -40.66351 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 056cc556-16cb-3798-9088-00ca048cb7c2 | -16.00956 | -40.64392 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7f72f914-0cfb-3707-b0dd-ed9b42e8f2ce | -14.73498 | -40.29306 | 2026-10-08 16:35:00 | NOAA-20 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 22d140a8-e459-389a-b6c7-0d279a867f38 | -14.46241 | -41.32647 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 7a47ce28-1425-305f-a87c-0b11c0319707 | -14.79535 | -39.28986 | 2026-10-08 16:35:00 | NOAA-20 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ea86119f-a23b-3bb8-846a-8a70bee69f63 | -16.93566 | -42.10605 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 88ac1051-d40a-30a7-8085-448c55df2397 | -14.52236 | -40.6558 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 91059e9d-176f-360a-b9cd-215d09ab2a4e | -16.73947 | -40.43268 | 2026-10-08 16:35:00 | NOAA-20 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7b8810b0-addf-3138-ad9e-afe49c9258ff | -15.3339 | -39.63771 | 2026-10-08 16:35:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 00759f13-75cc-3565-b17a-a33b2e5ac7f5 | -21.51207 | -55.08569 | 2026-10-08 16:35:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fcf3bcd8-8a29-3363-9a98-78310ad7fb32 | -15.5758 | -42.89601 | 2026-10-08 16:35:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7a9ace9e-db24-3756-983c-a97f2f107b61 | -14.85358 | -42.06418 | 2026-10-08 16:35:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 10a677d0-6568-38ed-9efd-1eec59956e36 | -20.88209 | -43.29622 | 2026-10-08 16:35:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c1e9732c-103d-3247-ab82-f8425cfb8506 | -16.76104 | -40.99366 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 57c80aac-b1eb-3d3a-b8bb-23c8a975872c | -16.1488 | -43.74633 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7aab5727-7235-33b4-abe2-3219a2305d62 | -14.05733 | -43.82561 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| a0f4e531-3579-395e-8980-9571527b3039 | -15.57088 | -44.5219 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 68595a6a-c860-32d7-a511-2100c8aa66d6 | -21.57209 | -44.1483 | 2026-10-08 16:35:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1d8d61e2-eca5-302b-9c30-bc40dc738b21 | -17.28389 | -43.89617 | 2026-10-08 16:35:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 525b7ae7-9a6d-33cb-b534-977ced6649ac | -19.65372 | -40.22588 | 2026-10-08 16:35:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 31f03cc2-c826-386e-a6eb-7392d460f674 | -13.96755 | -44.84059 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 62f4c431-ed2a-3af1-9d75-00dfc8af5c9f | -14.55661 | -41.34814 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 008061c1-5c42-369b-b174-b30be5965b6e | -15.39667 | -44.33313 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 893a2810-fa17-35f7-a0a8-978ad30bb190 | -15.05941 | -41.25476 | 2026-10-08 16:35:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 4c28671a-6e0a-35b8-98d0-556b7f617e4a | -16.9106 | -40.89346 | 2026-10-08 16:35:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| ee1b4790-122c-39c3-b5cb-671f4c05b9db | -16.66781 | -39.66454 | 2026-10-08 16:35:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ed69b8f6-5576-394c-8058-d5c9132434a3 | -15.78218 | -49.75704 | 2026-10-08 16:35:00 | NOAA-20 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8dd9b713-a92e-3047-b04e-248e5212e66b | -16.97171 | -41.2202 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 6e26412f-06bb-33b9-b753-053ddb7f013c | -16.56445 | -44.16296 | 2026-10-08 16:35:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ab2778dc-5f09-3bef-aad7-a1321dc6e49a | -17.44816 | -45.05681 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 205108e0-c213-383c-93e1-b8a68f68866b | -23.185 | -52.08188 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a596e6bd-ce53-3c37-b935-b2a27143e9cf | -15.96503 | -41.43187 | 2026-10-08 16:35:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5e9f1dc1-fcfc-3313-9f0b-511fa337ba66 | -15.65734 | -47.83044 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83573cf7-efa8-39bc-82ab-3ce690ad4b18 | -15.39891 | -44.32544 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ab5c647b-8f5c-3adf-9967-5c5076161d2b | -14.634 | -41.53326 | 2026-10-08 16:35:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |


[Clique aqui para ver as próximas entradas](README306.md)
