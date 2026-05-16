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
| 1c59cb9a-b2cf-30e0-9cb0-77d2f3ea71b1 | -8.07957 | -44.13409 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f8aabcd-2562-36ee-a5d3-6b15f5804e59 | -11.50885 | -38.48473 | 2026-05-16 03:57:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6bd486dd-1311-3b90-a804-d168243d58cd | -6.63778 | -44.49396 | 2026-05-16 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bea543bd-8195-3458-8bae-326cb9abe139 | -11.87333 | -43.87124 | 2026-05-16 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9323f823-4fd2-32e0-8ae1-d0363a3e41eb | -11.7437 | -44.52737 | 2026-05-16 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25618619-c27c-3f44-9399-0c42e5fa3ffc | -12.04337 | -45.29009 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f6965c-c8de-37e1-aa47-43b2bf71e116 | -10.51999 | -39.15025 | 2026-05-16 03:57:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ffb8ff44-8e72-326d-98f0-1b84bc73ec77 | -9.66786 | -37.44859 | 2026-05-16 03:57:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8083b502-6f92-324a-acd5-9f6d01fc79c9 | -11.04336 | -48.932 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c68d656-de11-30c1-91b5-0e0862f71f40 | -11.86914 | -43.87046 | 2026-05-16 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 489e5167-d8f2-3595-b3e5-008baf3ad5b8 | -11.97602 | -47.37043 | 2026-05-16 03:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd1fd5cb-dee5-336d-9fb6-7378d3c6db04 | -8.08623 | -44.14944 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a44e164b-2e90-37ef-8aae-72f3269c9802 | -8.26324 | -48.23913 | 2026-05-16 03:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8691ec75-6ba0-32a8-9d23-cd996c8f2f07 | -8.10106 | -43.15826 | 2026-05-16 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0ddf42da-c36a-3f9e-a368-7a39b640ad32 | -11.60042 | -48.03074 | 2026-05-16 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d4d0a9f-d9ce-3bca-be25-1ae5b03ef253 | -8.08249 | -44.14404 | 2026-05-16 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07968949-11b4-3bd6-b78e-c593b127fa64 | -12.05253 | -45.29184 | 2026-05-16 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a318205-71a5-3de0-a87c-90b339c89786 | -8.8534 | -50.21421 | 2026-05-16 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b4241a7-d5a8-3b04-a4a8-620be7786b21 | -12.15633 | -38.09462 | 2026-05-16 03:57:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c2e861c1-92f4-3594-9d86-835c22359099 | -11.03966 | -48.93343 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b1ecee8-e73a-3a07-9231-fbcd161f5eaf | -10.66261 | -49.70478 | 2026-05-16 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b39ee183-6a8c-3ac7-9d79-5a89fcf31455 | -11.04056 | -48.9289 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90cc563b-e075-34ef-868e-fe5d5e6f5abc | -11.04224 | -48.92053 | 2026-05-16 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65438209-879e-34c3-9582-77a0d789f5da | -9.79222 | -48.0773 | 2026-05-16 03:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6df4e774-ae3d-3c25-bd8e-ab45ff6ea06b | -11.87401 | -43.86736 | 2026-05-16 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3dfdbda8-8234-3981-b926-7c98136c391c | -9.30105 | -39.15051 | 2026-05-16 03:57:00 | NPP-375D | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| daf3d607-78f3-378b-9b33-1dbeb84fc01a | -6.64256 | -44.49477 | 2026-05-16 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71f2cc49-60df-34ab-8f64-71372534ee33 | -15.90994 | -41.86061 | 2026-05-16 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b6a457d-4e31-3e8d-ba43-23e7270c5f4c | -12.85016 | -43.75893 | 2026-05-16 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73586abd-2cf8-3f9a-bd4d-93aa27228116 | -14.22744 | -43.65594 | 2026-05-16 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98ba05ba-7d3d-3499-b958-8b13cbdd4ab0 | -12.85425 | -43.75969 | 2026-05-16 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff3025a5-dc7e-36d0-8f2f-8ea475946569 | -12.85359 | -43.76338 | 2026-05-16 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26064b52-ff23-31fe-b606-f899d34719be | -15.91063 | -41.85655 | 2026-05-16 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f37fcd3e-0919-36ab-9b1f-5a5be3305915 | -17.61367 | -42.59961 | 2026-05-16 04:00:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 01d9b882-ca93-349e-8ca7-22798b74853b | -17.34841 | -42.62397 | 2026-05-16 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4900833f-ed5e-3297-92ec-2647a204bd0b | -14.65525 | -40.99708 | 2026-05-16 04:00:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f6712257-539c-32a4-9f02-e70b212be14b | -17.34481 | -42.6233 | 2026-05-16 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b2ff8c4-0913-3cf9-a5dd-0923bd032c90 | -17.34916 | -42.61969 | 2026-05-16 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a76c1206-cca6-3d0c-8a8d-44d4946ebcac | -12.8495 | -43.76262 | 2026-05-16 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b037c57-2add-37a6-8c04-25719c24280c | -14.6587 | -40.99775 | 2026-05-16 04:00:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5bf90b4-8175-3c5b-a4f5-fb75de0700d8 | -15.91347 | -41.86127 | 2026-05-16 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de5eb0ce-a109-3563-9410-28345fa101de | -14.65171 | -41.6656 | 2026-05-16 04:00:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9245e26b-77e6-37b2-a576-4b736c026e5a | -15.91416 | -41.85721 | 2026-05-16 04:00:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80bf102e-9df1-39f5-8c57-8c290231ca79 | -18.12341 | -44.26892 | 2026-05-16 04:00:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d4332b8-35e1-32f7-9419-35e72c17b0c4 | -21.93241 | -41.33545 | 2026-05-16 04:02:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3cbf76f0-d724-3632-83f4-c6246b4882ba | -21.92906 | -41.33482 | 2026-05-16 04:02:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad1fd8fd-1349-3eb1-8390-6cc955155fef | -20.53959 | -41.83129 | 2026-05-16 04:02:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0eb0cea9-f551-3d9e-83e3-1d32590ea02f | -21.87103 | -45.05925 | 2026-05-16 04:02:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e67f08e-9def-3bc4-b201-d7b379b76117 | -21.87239 | -45.06139 | 2026-05-16 04:02:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d54a5ff4-4d2e-3732-96c2-357ffbd3ef16 | -8.94987 | -45.69676 | 2026-05-16 04:17:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57a0d7f5-ac82-3db0-81cf-59d136ca2019 | -9.78783 | -48.08044 | 2026-05-16 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef74dd0-9d98-3727-ad52-0e17082a27e3 | -15.18578 | -41.8052 | 2026-05-16 04:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4712964e-fcf4-332d-be72-f2555072bf9a | -8.10385 | -43.15714 | 2026-05-16 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8405a170-e1c2-39c9-ac0e-866dbef4b25f | -8.08094 | -44.13475 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b492268-e5cb-3e22-8cde-f24dfbd56f9f | -8.84726 | -49.87152 | 2026-05-16 04:17:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df0a1080-07d4-305b-ae1a-25e999c4c794 | -8.49933 | -46.3858 | 2026-05-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88037061-ea97-3bd6-a3c9-aa4e6bfcec46 | -14.65016 | -41.66511 | 2026-05-16 04:17:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 08124eb4-d736-32ee-bd2d-296cd97275e1 | -15.5916 | -46.8113 | 2026-05-16 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cf46730-be81-3ef5-908f-312a04e28089 | -14.23025 | -43.65538 | 2026-05-16 04:17:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c21cea4-806f-339d-b8d2-e1cb62255dae | -9.52627 | -47.51154 | 2026-05-16 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f9387e5-192a-3557-b174-ece6640c26a1 | -8.0837 | -44.13879 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f13f82-4a5b-3f7e-8b6c-59eeeb972499 | -11.30955 | -54.03844 | 2026-05-16 04:17:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82373ebc-5da8-3220-be2d-784891144842 | -7.13441 | -44.06185 | 2026-05-16 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25b50a59-4922-3530-9468-3c680f06fadb | -7.27675 | -46.79867 | 2026-05-16 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55406f0f-8b09-33e2-bc4a-a9e87d873178 | -8.05617 | -46.75224 | 2026-05-16 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f4cd33-0126-3ebc-831a-03022e6cf5fd | -13.03371 | -49.93823 | 2026-05-16 04:17:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e970101-33c7-32cd-a559-096ef3cbd9f1 | -9.451 | -46.10862 | 2026-05-16 04:17:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdbf09c5-d951-394b-b971-cecd750b9ab0 | -8.85521 | -50.21483 | 2026-05-16 04:17:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e794f26-76a2-3757-9e50-18a29e2b5586 | -14.65535 | -41.00012 | 2026-05-16 04:17:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55cd2860-9e5a-31ce-9a96-8e76d2af1c0d | -8.26122 | -48.23234 | 2026-05-16 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2bb1f59-cbbc-3112-8cb3-d940d19044e3 | -11.44097 | -54.09473 | 2026-05-16 04:17:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ea7fb8f-485b-3116-a351-e54c7559c59b | -9.52407 | -47.50182 | 2026-05-16 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29ab13e9-a90f-3c5a-9830-cf103f3bbd4c | -9.79245 | -48.07641 | 2026-05-16 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e37a0b8-650e-3d60-a1ec-8432956768f3 | -9.4741 | -46.07663 | 2026-05-16 04:17:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29a25cb6-21dc-3d9b-a7c7-f9d31b33c3ac | -15.59222 | -46.80755 | 2026-05-16 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01c933c3-c3db-37d4-9056-e13dc4beefb2 | -7.27604 | -46.80302 | 2026-05-16 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 879bc082-56c4-38e6-a8c6-95b6b5bf5efa | -9.23474 | -46.65223 | 2026-05-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 030fa2e4-fcc4-3222-8c55-76d742475653 | -11.4417 | -54.09101 | 2026-05-16 04:17:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b40c6504-72e0-378e-bca0-f209d611380a | -9.48081 | -40.33996 | 2026-05-16 04:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f5ef433f-24bd-36a0-857c-670902470f50 | -9.78862 | -48.07571 | 2026-05-16 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3fb2741-b5ae-3e6e-a289-444f8a32b140 | -6.64095 | -44.49045 | 2026-05-16 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a0db36a-2e2a-3e2e-99df-9ba9412d35f4 | -9.7903 | -48.07863 | 2026-05-16 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8a1563a-58e8-3483-b45a-cf48fd8ea175 | -8.0859 | -44.14634 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ae3c87-4f17-30c3-b3db-982d76c75ea3 | -8.07818 | -44.13071 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db89697-d982-3353-9297-8fdb46dbf5f2 | -8.1044 | -43.15368 | 2026-05-16 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7f0a7170-45d3-3b71-9e90-f744f6abf36e | -13.50795 | -43.47779 | 2026-05-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f19f1072-0243-3380-b476-f20a5d831066 | -10.49702 | -42.40657 | 2026-05-16 04:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e3ff642-2dff-39e6-9da7-11046024b9e1 | -8.2643 | -48.23815 | 2026-05-16 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71808192-f6cd-37e0-b770-c922ae7dff22 | -9.78647 | -48.07793 | 2026-05-16 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79bd815e-82e2-33ce-9e51-dba0dbf80560 | -8.26517 | -48.23306 | 2026-05-16 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d32af80-7456-3be8-978f-4bcaa870f1c3 | -14.3627 | -45.55611 | 2026-05-16 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b9be309c-10ba-3106-a112-3e65a714e941 | -8.08037 | -44.13826 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9773c6e1-9d3d-3620-bf9a-18f0366a3efa | -9.47717 | -40.3394 | 2026-05-16 04:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a7ba4441-ce1d-335e-8aa6-728d9f449ba7 | -14.22689 | -43.65484 | 2026-05-16 04:17:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99d68987-1229-3856-9512-e985204a6ca6 | -8.85597 | -50.2104 | 2026-05-16 04:17:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9509c883-477d-3c24-b2d2-5d7da46eeff4 | -15.91275 | -41.85854 | 2026-05-16 04:17:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b15912c5-ef84-3168-bcaa-ed0e658f9a0b | -8.08257 | -44.14581 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 520db6c1-e247-308a-b936-53c64eb5d293 | -11.46043 | -55.12166 | 2026-05-16 04:17:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b1575c0-b9fb-3b6c-8002-e3c124a56d15 | -8.05571 | -46.75417 | 2026-05-16 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 475aaea3-ac5c-3e65-aec0-4cf536321527 | -9.52704 | -47.50701 | 2026-05-16 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
