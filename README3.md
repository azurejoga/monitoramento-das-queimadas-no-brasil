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
| 3cf7658e-3297-3b01-b9d7-8124d5432936 | -3.7649 | -43.402 | 2026-09-25 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9ab6097-65a5-307d-939f-c80afac02c4f | -9.848 | -44.1875 | 2026-09-25 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4d94255-1881-3485-8ec6-e30fcbd2555f | -6.3992 | -46.201401 | 2026-09-25 00:18:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 899ae789-16e7-3922-b3a5-c40fdeb032ff | -3.9393 | -42.994801 | 2026-09-25 00:18:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4080d901-3fed-3a11-8a0d-698c521af7a7 | -5.3492 | -45.011101 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1803766d-e6fc-3d79-b581-d5636e48675c | -0.4946 | -49.142399 | 2026-09-25 00:18:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0b344bc-fa4d-3f17-8a8c-84de1a3ed1f8 | -7.5968 | -46.459702 | 2026-09-25 00:18:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 468b00cf-592c-33e9-9bfe-0c3341b6a6c2 | -8.3226 | -44.1315 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04d1d3dc-78ba-37c7-b131-fe74f1ff68ed | -5.791 | -43.917702 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6958e1-e1d0-3478-92c7-190ee43b848e | -0.509 | -49.160099 | 2026-09-25 00:18:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7212c939-62b9-3d6b-ac19-a809bb9187eb | -5.4767 | -45.1194 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0efe77-da28-3a2b-938c-8534a9c5853d | -5.7427 | -42.448799 | 2026-09-25 00:18:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddc9077d-1d7f-3264-ad22-512d79cb08e1 | -0.4969 | -49.152302 | 2026-09-25 00:18:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0456d6b7-1ca7-3f42-bd8d-7c54fbdaffeb | -5.359 | -45.0089 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2b8e8c7-63b6-3772-ae83-2eddd6520dd4 | -8.9228 | -43.870098 | 2026-09-25 00:18:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68ced998-a184-3499-a9bb-edb7037d4300 | -5.4718 | -45.097599 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 699c2db3-f5b4-3312-b14e-7663159435ad | -14.7058 | -48.752998 | 2026-09-25 00:18:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ef7b6491-2b6d-34d7-a4d2-d4391b5ebe4f | -8.3356 | -44.1436 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30b9c7f0-6de7-34a3-b587-d8da9a11be96 | -5.8738 | -43.783401 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 428151e0-a542-329d-9d23-64f418717b17 | -3.9795 | -48.426498 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f435fca-39e0-3a2a-86dd-3d904665a3d0 | -11.7878 | -50.944401 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06a194be-e766-365c-af7d-5dfe3bcc89a4 | -3.4046 | -39.2845 | 2026-09-25 00:18:00 | METOP-C | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f9b18b93-3051-3a14-af72-23f8186e24b6 | -5.1485 | -49.9995 | 2026-09-25 00:18:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42056b17-2c8c-3934-a076-796c40ed2486 | -5.3074 | -49.049301 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e54a35c9-cec4-3320-90cf-ba273b11f166 | -11.3533 | -43.415501 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 115004c1-9293-3fe3-a01e-74ab17d329f0 | -4.3725 | -46.245899 | 2026-09-25 00:18:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5566abe7-4901-3ff8-8fde-6b342a041b5c | -5.7808 | -45.097698 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8c16208-1256-3166-a5bf-6f1f4ca54242 | -1.2012 | -46.746101 | 2026-09-25 00:18:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f4a522-f6bc-387e-afb3-09a8bb877c1a | -1.1384 | -54.087898 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 572276b0-6ac5-335e-b2ed-06baa60b3fb2 | -7.1237 | -41.727798 | 2026-09-25 00:18:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9622f3e8-6e33-3766-a371-7a7550ccad96 | -11.3501 | -43.4011 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3f7181d-ddd0-3535-bf31-59d8bb544e05 | -3.2373 | -46.9137 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf9187e-e1fd-3590-b66d-06bac525299a | -4.4895 | -54.934799 | 2026-09-25 00:18:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb0450c-89bf-30af-a60c-f1d4876ed0c8 | -5.3543 | -47.919498 | 2026-09-25 00:18:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cb1d43f-ae0c-3249-a536-9ad303104f8c | -5.1912 | -42.965599 | 2026-09-25 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 5571aed9-60a2-3b6c-a9d5-c7843f39b2d1 | -3.4936 | -50.741501 | 2026-09-25 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 473bf5ce-61d2-31e1-9bf9-e67b821664c9 | -5.3916 | -49.152699 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7d4ae7-4ac7-3a7e-a7c0-2e1471e0ebf7 | -11.6582 | -50.5956 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61683309-35c5-3506-9a73-e8b64ec8c4f6 | -11.2812 | -51.2925 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9d7b6dd-3246-3c7e-8d95-2356d58c597c | -5.0921 | -45.512699 | 2026-09-25 00:18:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 548b6070-d003-339d-be9b-c494e7e5c9a2 | -5.0163 | -41.7188 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d317717-1709-3eea-bc35-a0bb028e62ed | -4.4498 | -47.914299 | 2026-09-25 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b33ed5-860e-3104-af66-a8f08f71a8cc | -5.462 | -45.099701 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eedd0a9f-70d5-3fb5-a63b-a5d0bed350c3 | -11.3681 | -43.3895 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b077280-720d-3218-bac1-a2df4be3474b | -11.3485 | -43.393902 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91db4f45-3b2d-3c9b-9d63-05ce3529ecbf | -3.4699 | -41.7691 | 2026-09-25 00:18:00 | METOP-C | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b095d897-c98f-3c9d-9f9e-5fc57a4e7664 | -10.6114 | -53.9837 | 2026-09-25 00:18:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79e5c98c-a8df-32af-a3bf-e3e05439348b | -3.2275 | -46.915901 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0abb3a2e-2ff1-337b-8aeb-f334d618aacf | -5.4865 | -45.117199 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b36bb56-b338-3d2e-bee8-d98a9676e819 | -3.9409 | -43.001701 | 2026-09-25 00:18:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c64e225-d272-347c-8fd1-8cf101270777 | -5.14 | -45.178799 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 013ddb40-e348-3d15-bd67-d06170071e16 | -5.5171 | -43.712101 | 2026-09-25 00:18:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49cd3b51-0de6-3580-8dc3-9c5b95dfe9e3 | -12.0723 | -50.287701 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99ba0c29-fb5e-365e-bbca-dc3467c80ef7 | -1.9538 | -48.373501 | 2026-09-25 00:18:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89bd3648-9463-3fca-bbb9-d47f4d252c39 | -11.9253 | -38.302898 | 2026-09-25 00:18:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 563fb07d-7188-33f8-bf1c-0c80672af811 | -11.6546 | -50.577301 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21eb160a-4726-32df-92ef-fa4b4e6a70b8 | -11.6619 | -50.614101 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 622c8e1a-6f54-3554-b80f-701746ef17cf | -7.3568 | -42.066502 | 2026-09-25 00:18:00 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5da77748-88b6-36e3-ab9f-85a4ee575ce3 | -4.9293 | -45.658199 | 2026-09-25 00:18:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5c68796-5823-30aa-878d-c5c94934a335 | -6.5338 | -47.1768 | 2026-09-25 00:18:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 311d9b9a-ab0e-3926-afe8-6618357e626a | -3.241 | -46.929901 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b35ece51-8593-3c5f-801e-20ac1c1cf81f | -5.0938 | -45.520199 | 2026-09-25 00:18:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 397a9c89-f854-3b80-9971-c57da378cdaa | -8.3274 | -44.152901 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cff0666f-cd3b-3914-9506-e3644fc2ad3d | -15.0289 | -42.263599 | 2026-09-25 00:18:00 | METOP-C | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0cb5c56b-3c82-3bcb-a802-313cac15762c | -8.9244 | -43.877201 | 2026-09-25 00:18:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab558747-e56b-33b5-a6da-68a5266bb699 | -5.0049 | -41.713799 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb1d2e86-cc39-3027-94c4-1a567c0a9971 | -3.7297 | -49.051102 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5378c7d8-f4bb-3413-adf4-a63d835467b1 | -5.8379 | -44.8951 | 2026-09-25 00:18:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96020046-e222-3f3b-b6cd-cc96180a6c11 | -5.7878 | -43.9039 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95facc1f-6c82-3366-b6dc-eb5a6d3ab1bc | -3.4904 | -50.727501 | 2026-09-25 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef3d634-dd50-3c63-871b-f273d9e3fb2d | -7.5909 | -41.784302 | 2026-09-25 00:18:00 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71d149e5-2f17-3ce3-b031-2cbf575e22eb | -5.1301 | -44.319599 | 2026-09-25 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18282e0c-e477-3e3e-a2e3-f77c6422b344 | -4.9569 | -45.1436 | 2026-09-25 00:18:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5469919b-62dc-3234-b50f-4f0736964b19 | -5.0954 | -45.527599 | 2026-09-25 00:18:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e16c145-dd37-3128-ab1c-9d0a70ad0351 | -3.9377 | -42.9879 | 2026-09-25 00:18:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30d308c6-7e08-362b-8294-25c279c861ce | -4.452 | -47.923801 | 2026-09-25 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34b688c7-aabc-38a8-bd0e-69dc386097a4 | -14.6991 | -48.770302 | 2026-09-25 00:18:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9d2349-44f8-3c37-a99f-cc0e368be202 | -5.32 | -44.248001 | 2026-09-25 00:18:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5242d01e-87f3-3fb9-9973-7e1bec87ba02 | -14.4009 | -41.6157 | 2026-09-25 00:18:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 10fd0260-faee-3498-b613-b15ef5a206f3 | -11.6522 | -50.616001 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78e9018a-aaae-3411-9fd0-ebc584c9f749 | -4.62 | -43.712101 | 2026-09-25 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 628319d2-3d58-3bcb-8e3c-ada323404b68 | -11.2909 | -51.2906 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1222ac4-3e77-3526-91d4-508d000abbc7 | -1.21 | -54.577999 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14022261-219a-3d68-9974-d4f8f23760c0 | -9.0163 | -49.630199 | 2026-09-25 00:18:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e239564-152c-35bd-b3ab-1dae6bf86f31 | -1.1434 | -54.109901 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745579e6-ab2e-36ba-9000-14b83d7a69f2 | -2.444 | -49.219398 | 2026-09-25 00:18:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef338917-8add-3d86-bac0-93d2b609179c | -5.7791 | -45.090401 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba056575-dca3-3dff-b780-155304a601fd | -1.1236 | -54.068001 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353db22c-eca5-381a-ac27-98525dbeae41 | -7.1254 | -41.734901 | 2026-09-25 00:18:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9b0da3c-1044-3d11-b87e-c06ddf383593 | -11.6615 | -43.506001 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cda1d7c-56ce-3471-ac94-725a4c4b2e0e | -8.5841 | -48.362099 | 2026-09-25 00:18:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35971099-af19-3e1e-9ff1-83a6f0bb5c81 | -6.5573 | -46.542099 | 2026-09-25 00:18:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3528a65-a25e-36a5-a703-3fc7f0c2f648 | -11.3583 | -43.391701 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41557b0d-1fa2-3952-8d76-26f960776bcd | -5.0147 | -41.711601 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d2d7c51-7e5d-38e1-ac50-a33f0cf61de3 | -4.369 | -46.230301 | 2026-09-25 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32d8b6b0-26af-3f34-b303-7268131c4a3e | -11.933 | -38.291698 | 2026-09-25 00:18:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9253372f-51ad-3747-aa73-5009ba84fb1d | -9.4016 | -41.179901 | 2026-09-25 00:18:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e7fcdad3-e3f2-3123-b7a5-f006bce3b67c | -5.4636 | -45.106998 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d42151e-c49e-35ac-bbb5-d7a046528cd4 | -5.8753 | -43.790298 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 063f918c-1dd9-3b33-850f-0e11d20be7ab | -10.4421 | -64.5028 | 2026-09-25 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |


[Clique aqui para ver as próximas entradas](README4.md)
