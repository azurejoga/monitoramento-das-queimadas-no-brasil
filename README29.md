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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 523dad35-2a80-3983-a793-45181da97a71 | -8.90881 | -44.85608 | 2025-08-26 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c0eae7b-2253-3d0b-8408-9a397ba854a9 | -11.14104 | -44.69231 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9bb4d37-56d3-3699-9e81-9bb967a85e3e | -8.07509 | -44.99911 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d9f77cd-62dc-3168-9fb2-93628bb1e61b | -11.63124 | -44.86194 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b0fdf6f-ddd0-34a7-935a-928de5d6f4fb | -11.62988 | -46.21268 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f512de44-6418-3a00-8bbf-e9750d9f25bf | -12.37251 | -46.56636 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c25c55f4-ff9d-38f5-94c4-ea9df818646b | -8.26834 | -47.23261 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f58ed3f-f6bf-39e8-ba5f-2822ab2ae935 | -10.80603 | -48.32181 | 2025-08-26 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c1dccb1-52a4-3ba0-ad8b-c28ce43240c1 | -9.17066 | -40.60153 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8bc59f0f-8b2c-3caa-aa22-9a2dfd6f796c | -9.64832 | -40.59718 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8ececbea-a5d0-3078-9ff4-73bd51078fde | -11.30501 | -43.29197 | 2025-08-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba407c41-843b-39eb-a707-44286c5b696c | -11.28232 | -44.99074 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f47c281-d883-39a1-9635-b1fa9bf903a5 | -8.24613 | -45.08651 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffdf783d-385a-3279-9f9b-45007a5fba62 | -10.53546 | -46.79135 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a63ad475-db61-3b28-b0fb-68e1542d20e1 | -12.40706 | -46.50257 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40778085-6792-30c8-8a81-11e238fadd6a | -5.87563 | -42.41417 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c6838498-5bc1-3b8c-a17a-91540a693344 | -8.30434 | -47.23282 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dc9a0c4c-df76-38be-8d9a-3ceba3c13edc | -10.51565 | -46.76773 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd10e18c-2faf-364d-9f24-98ceaa07cd5f | -5.87203 | -42.411 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67f65fb8-bc11-3aa4-9b7d-0d420e331ab1 | -8.15992 | -45.05926 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 216d61bf-f1ca-3fd1-9f89-9c65cb72f97a | -8.16924 | -45.05676 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb2275dd-ea6a-388e-b126-3a48e09abcbc | -10.6832 | -47.17826 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 07b58082-e888-389e-84ad-0500c3065f3b | -8.24464 | -45.09495 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c90f8bb0-50ee-37e8-ba6a-c47c1fa06326 | -10.38311 | -43.47141 | 2025-08-26 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c163afd-85eb-34e5-9615-70c8a44bd35a | -11.33756 | -47.84319 | 2025-08-26 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| adf5c206-f1fa-3e27-a334-7414d37d113e | -6.50318 | -42.94468 | 2025-08-26 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ccdd1e9c-da4c-31d6-91d5-729cf8b85d1c | -12.77879 | -48.13054 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58355fad-2457-3c61-be2f-b2930279d99c | -12.4408 | -48.71666 | 2025-08-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03d05cf2-1a7e-33ff-b126-1e3e043da51a | -14.98281 | -48.84708 | 2025-08-26 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6abde4af-f838-37df-8664-72097331f32c | -12.75489 | -48.09596 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32f62c9a-4988-3d23-8abe-b6d29c43870f | -19.9094 | -44.63032 | 2025-08-26 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 717bdca3-0a5b-34f4-a623-4cb7d66df3a5 | -12.65802 | -47.85352 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5097d631-69dc-36a9-b790-10dd50d78e84 | -12.7297 | -48.14856 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a8e293a1-3e26-337b-be28-2ba52d3fda13 | -11.55503 | -52.13237 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 407b0a2f-4ddf-36c5-9a0f-7fb2a6cf4464 | -19.12358 | -46.45492 | 2025-08-26 03:57:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40d1d163-e2b3-3f0b-95d0-4d6afeac4b4c | -11.55614 | -52.1269 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f250adf-0213-32c2-9af7-1c9f4f99d2ff | -12.76775 | -48.10836 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffa953ed-dad1-31fb-b347-7f5abafb1cb6 | -12.9924 | -45.22027 | 2025-08-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e21b1d6-72cf-3ba3-8a4b-3a4f0f7952e9 | -13.62917 | -48.15115 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc40508-6904-3214-b245-dd98d3a9b44f | -11.52177 | -52.13136 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0448b444-1073-3882-baab-56bec7cba12e | -13.41744 | -46.90308 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7b658a8-36d5-3b8e-b04a-03ec2eaeb6a7 | -20.38406 | -42.19498 | 2025-08-26 03:57:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 09c92d7c-e551-3ee9-b160-54db1116ab62 | -13.5207 | -46.90832 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a3ff037-4dae-33dd-8a30-96d68c5a63f9 | -19.07893 | -48.14886 | 2025-08-26 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 586ab9bb-7fbd-3ede-b9ab-2813566946a8 | -13.41853 | -46.92218 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da1358e-b892-38ce-b7c4-a74546033b90 | -14.34961 | -51.94997 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df3646c4-ef0d-3ccb-8657-85cd0d04328e | -15.08 | -48.66066 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2221125-3174-3814-b7d2-c570ea206b28 | -20.49692 | -44.08557 | 2025-08-26 03:57:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 394e4f2b-b4fb-3d0c-b6dd-7c92a317dd95 | -16.80576 | -51.91395 | 2025-08-26 03:57:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4820f925-9647-3563-9b61-22ddc688ee3f | -19.92506 | -44.62432 | 2025-08-26 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| edf7f6b7-3507-3d1e-b824-621357cd682a | -12.73852 | -48.15565 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed848106-adeb-3b43-89e7-a3ee8d275bda | -13.51535 | -46.9123 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 270bda6f-08cb-3987-b652-c052e1257f50 | -11.56585 | -52.11191 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ba32a3d-0d74-3524-b8f6-1e1fe9a35c67 | -14.34358 | -51.94858 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d3652547-29f5-3abf-8407-b32aa0e70d2b | -15.02393 | -48.50954 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb3d3a5a-48e7-39ef-98b3-3621ac2bcfc6 | -17.60977 | -46.7041 | 2025-08-26 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b48d0bd1-dc35-3fc0-99e0-92d519d156a9 | -11.55302 | -52.10925 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55b4f5d3-d4d5-341e-843f-2aa36c4c7639 | -18.24139 | -51.26789 | 2025-08-26 03:57:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4566ac8b-5797-31f6-bfff-ad776209b6bb | -17.37719 | -48.0872 | 2025-08-26 03:57:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f478a5da-fdd8-3298-b7e1-2a1d0db75661 | -16.62642 | -49.3724 | 2025-08-26 03:57:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06528df7-afb5-3ac7-a3b1-e41c6c62bebf | -11.51426 | -52.13537 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5dab46a4-aa02-3e51-9cbd-7f6aa98e3a7a | -13.60876 | -48.15319 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46790b22-18d5-3c09-b256-27185d7a7d73 | -19.76686 | -42.05338 | 2025-08-26 03:57:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7b06854f-8cf8-373c-a124-fe3cecc60690 | -12.74508 | -48.0943 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8210426d-c1ad-3e93-b84e-d1c5178316ea | -19.94175 | -47.03609 | 2025-08-26 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 245dd102-2e19-3b57-b047-e4bd3c4ac509 | -18.86821 | -47.004 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90457850-3f79-3dd1-83de-43b0bc31d536 | -11.54656 | -52.10816 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be71d80f-5d40-329b-8699-90d27c53bc82 | -13.61472 | -48.14819 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1d8b86-4ce2-3687-8c53-d07dcb3fa3a5 | -11.56696 | -52.10641 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f97e825-4f91-382a-b16e-9dfcbec4f707 | -14.26015 | -48.03297 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 055b0106-fdcb-3208-9486-cb826a59fba1 | -13.45858 | -46.99335 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8202fa5e-75f2-3391-a6a6-3578be450d3b | -17.78194 | -44.48174 | 2025-08-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29b978a0-3d19-3f99-bf41-241f9005bcf3 | -11.56163 | -52.09973 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3607466a-11bf-32af-a9f4-6b40c1fb7c2e | -18.71959 | -41.27411 | 2025-08-26 03:57:00 | NOAA-21 | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8787d58-3ab2-3f38-897f-3a3a84dca0a8 | -19.03775 | -43.4315 | 2025-08-26 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cc7dd445-639a-3753-bad3-72e223ab514a | -14.23701 | -53.04472 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06487bbb-d697-36ae-8b09-2513fa7be56f | -18.34546 | -44.96012 | 2025-08-26 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a0c5c2b-5d21-3e04-86c9-6d6e70e7718b | -13.41253 | -46.87966 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f669019e-56de-3f85-9780-57c951ef8f55 | -14.27827 | -49.13567 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d2177ef-97d4-3b42-b568-6c4876c2ba67 | -18.80859 | -47.59752 | 2025-08-26 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bdffdee-c95c-3582-aa30-0aeb6d9780b9 | -20.19071 | -44.58182 | 2025-08-26 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7538e109-2959-30de-8967-5b06b6c96b92 | -13.4878 | -46.8708 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ede11385-4f53-36cc-be87-ca98628ee108 | -12.94072 | -46.33821 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deeef120-5fe2-3e18-bd71-bd2162f92cc3 | -12.94235 | -46.32933 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39cc1ee2-8085-3acf-9968-b6916c04c9a3 | -18.38603 | -44.33379 | 2025-08-26 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5150a864-73f2-3420-81f3-599bb5842e7b | -15.18075 | -48.19065 | 2025-08-26 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f701550-2ec9-3e95-a94c-fda058af6c62 | -15.11643 | -48.72089 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d668f210-3b6d-39a0-8892-25354e89ad0b | -21.09503 | -40.93781 | 2025-08-26 03:57:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 21d6e2e8-faca-3017-8067-2202ab8a02db | -11.55834 | -52.11598 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 726ee4df-f903-3194-a6b4-b5d142151aa8 | -12.73069 | -48.14334 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e25b6e3-6ad7-3263-95e9-6c89cd2246c2 | -18.87226 | -47.00497 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e8a61074-0267-330a-8437-12c441cc49f8 | -13.41104 | -46.88777 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 25d99e03-381c-3f54-b84b-08a4f6022666 | -19.03182 | -46.91496 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9522084a-d16d-31e5-88b2-c021f18be404 | -11.50674 | -52.13937 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 308226b6-e5a8-3009-81ad-1f6ca5c04f6f | -13.77449 | -42.70192 | 2025-08-26 03:57:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3d29bf8-82a5-3fd0-84a7-8f609093036f | -15.10721 | -48.74203 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| edaa0218-0a6a-3ce0-bf5b-84aefa2965e0 | -14.28457 | -49.13051 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e82b1d9a-f63e-30f6-808a-a654b0e424a0 | -12.77639 | -48.11628 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03f6da67-1853-352b-bfb4-18309face773 | -12.95457 | -46.33595 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60321b29-52bd-3b1e-829c-12f5f29d0cdb | -13.64763 | -45.70757 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README30.md)
