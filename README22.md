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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41415b6e-5cea-3f07-b183-bbcfc03e71b4 | -12.76299 | -44.88118 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dbf65eb-2ed3-343a-8e15-428c022d4ec1 | -6.87895 | -43.68218 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a3bf364-94c9-3d00-b81b-9b55f2859721 | -11.27523 | -45.51844 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 87e13840-8fc6-38a1-b517-c9688bd627fc | -9.79718 | -44.78575 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51aaf7e7-ce58-3fdf-8660-0d6a6edf685c | -11.71909 | -43.64481 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4df6daa3-9e6e-36bb-8ce6-41d55f62e74c | -11.27182 | -45.50776 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cd3a1230-aaa6-3cdd-a42d-91f1c11ff8ca | -10.36739 | -45.03421 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d363a785-b427-3551-8ec7-da2b2fb6b88e | -11.27122 | -45.51101 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4afbc3d7-70a5-3386-adb5-5721d313f072 | -8.90811 | -43.88395 | 2026-10-06 03:45:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24c3761c-fd8c-3a6e-b669-d0e3b433e627 | -12.76888 | -44.8766 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d26efbb-1205-3f7b-a28f-c8fbb9f1bd47 | -9.09502 | -47.0715 | 2026-10-06 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a76f124c-ccdd-339c-a693-430f04d0a8de | -11.27084 | -45.517 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 391e99b6-2937-3779-ad29-f8909172dffc | -7.19707 | -44.30279 | 2026-10-06 03:45:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cab330ef-5a66-3b07-9960-65dadb119c08 | -11.27062 | -45.51424 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| ce41ac2d-e0dc-32ec-badd-918d42d5c110 | -6.88492 | -43.67728 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 665f8555-9946-369d-97bc-013ceab828a9 | -7.88215 | -44.19344 | 2026-10-06 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 627f12da-5828-3fbe-a72f-47b0bb541996 | -7.47551 | -42.80612 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0f5f7bcf-9c74-3aef-bfee-bbd78e61bdc8 | -11.26782 | -45.50029 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f166dd71-0d48-35a1-a91b-a01dd186e0f1 | -6.89388 | -43.6846 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20ae8479-f652-340c-8c7a-afa02d272cfb | -6.87445 | -43.67862 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff76e15-3818-39e5-b7bb-12c91f23cdf3 | -10.36171 | -45.0363 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ba57245-7063-3368-89a4-5484fad434a5 | -11.27583 | -45.51522 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c923de61-b075-3a7c-ade6-356b006ca62a | -6.66836 | -43.82523 | 2026-10-06 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6147bdee-3aa5-3c9d-9a5a-9fbaab40afe4 | -11.05159 | -45.6409 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e73e1cb-3882-3549-a8d3-c81f84dfcfe6 | -11.6903 | -43.6739 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e99ce144-2ff1-31e1-8222-e28a18e8990b | -13.02467 | -43.12001 | 2026-10-06 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d98c25e4-cb66-36ed-af55-fa95cc2ad558 | -10.20688 | -36.39215 | 2026-10-06 03:45:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fe19c0ba-a4fa-37b7-9f10-1250fcc01355 | -11.27666 | -45.51474 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| ca6dbbb1-1cd6-39dc-8369-cf5d23029b5a | -11.26602 | -45.51003 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 4f556782-f270-3cba-8932-1291b7e18dd9 | -9.86118 | -44.80962 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9ad5cc9-f334-373b-aa1a-937d5a9b773a | -10.54812 | -46.39515 | 2026-10-06 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b7064c3-6703-3152-b662-46529eef5b53 | -11.05095 | -45.64425 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ddb1a66-7497-32d4-8222-20f0c3976a9f | -11.28943 | -45.50434 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d108648-5b80-35cb-bcb9-dba0293330fc | -8.58441 | -45.66353 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2db17e45-0b03-3318-81a3-e016845d781b | -11.77268 | -44.92099 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53ef4a19-dd31-33d8-bc39-d4f56e22a165 | -9.25623 | -45.6604 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bb1c1f5-206b-3bda-83b5-01a09b28da07 | -12.86857 | -39.9281 | 2026-10-06 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 62c30668-b3f2-3c86-bf47-ed566403673d | -8.69813 | -45.22488 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c49b3581-ae93-3a44-88e2-0bc40f97c705 | -12.20094 | -44.65969 | 2026-10-06 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 951e4d0b-4269-347b-b4e9-8fdfb52871fe | -11.68943 | -43.67868 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c448c43-7d30-353a-b2af-80e7cf2ba8da | -6.72504 | -44.27537 | 2026-10-06 03:45:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29f93eb1-906a-3a26-b6e1-1646574cc107 | -11.27852 | -45.50508 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 20f870a8-b52c-3daa-8f84-d3156b25654f | -11.26482 | -45.5165 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 208e1482-818b-34e6-bcc3-3833ee681d40 | -6.85172 | -41.80577 | 2026-10-06 03:45:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e19713b5-6bfd-3970-aa85-793cab094339 | -6.87994 | -43.6765 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5462b1ad-e535-34f7-bf9e-8e79ddb2a69b | -11.28309 | -45.50931 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 91772a5e-296b-3cd0-8cf3-438257e0ace0 | -8.82071 | -37.34308 | 2026-10-06 03:45:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c4efd86-1420-37a2-8164-4a025fa40448 | -7.10652 | -42.539 | 2026-10-06 03:45:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57be02f8-5163-3bd0-89eb-f29140b84ebc | -11.29739 | -45.51905 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 07b7b29b-d6ba-37e5-a96b-e014c71fa96c | -6.23243 | -47.00344 | 2026-10-06 03:45:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bc35f46-2b78-3922-bcfa-65ab74f10475 | -11.28797 | -45.50771 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 79981558-45da-339f-99e5-46faf5841d0a | -9.95344 | -43.47652 | 2026-10-06 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78200fe9-9cea-3a0e-8bb8-fa83f7ab1ddf | -12.64105 | -42.85928 | 2026-10-06 03:45:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 042fa8b1-8a3a-369d-979a-cf594ab487f8 | -14.05139 | -44.29023 | 2026-10-06 03:45:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecc071f1-672a-3158-9ba8-4d5b3aa07b68 | -11.82488 | -43.5311 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb6a7a71-1572-33bb-94cf-b424a9f9409b | -11.27542 | -45.52118 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e6bf0929-29b2-3b47-b66d-cedcef6c948d | -8.91298 | -43.88477 | 2026-10-06 03:45:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b40189bf-1494-36f6-b933-3155c83b16da | -11.27332 | -45.50408 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| bec6b849-f314-3f4d-bfd9-81ca956f3927 | -11.66526 | -43.63002 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82581a4b-bab9-3943-820a-6364785d7e85 | -11.27913 | -45.50189 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 51d600a2-954b-3c2d-815f-f925ccf8dba9 | -11.29341 | -45.5117 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c69035a6-33d5-3de9-be82-6edb51ffac36 | -11.65113 | -43.65571 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a52e5561-efb5-3a10-b124-f1b52ad7ce32 | -13.0282 | -43.12497 | 2026-10-06 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 101218d6-e0e4-3115-a4ca-e41d698c45a5 | -9.81188 | -44.79157 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1d07190-7f87-3d1f-a87b-21c914b03d6c | -11.28682 | -45.51398 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 04c19485-ae8d-3c76-9e36-85b6337017c9 | -10.97076 | -45.41167 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21cce35c-bd22-39ad-b2ae-29bf8f7bcdd8 | -12.76784 | -44.88213 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0a30a8f4-c47c-3243-b3d0-12dde3b490f7 | -10.49921 | -44.42053 | 2026-10-06 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5afd2b5a-fb9a-397e-9f1e-691bacdd12fa | -6.9311 | -43.67645 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a8c23ca-34e8-3d40-baee-549192fbc518 | -9.2569 | -45.65677 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c6e6921-b857-3aad-9562-9090f8d12e6c | -6.89439 | -43.68171 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a8f5c37-1e8a-3b05-83fd-78574114e6cb | -11.27146 | -45.51378 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 2f20fcc9-c3ab-34fb-b487-6f5d3b759d42 | -7.37747 | -46.22426 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d038912b-4890-3755-92de-f3abc1ca2b29 | -13.61284 | -44.35688 | 2026-10-06 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5f2fb1a-0074-383e-a649-8ce54d04a63d | -11.27242 | -45.50452 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a7e0eb9d-2d47-32ec-aeb2-f960f262c771 | -11.82438 | -44.69747 | 2026-10-06 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc6b19bc-a6be-34cb-929f-3aca3f3d37b9 | -7.69693 | -44.62458 | 2026-10-06 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6143bc99-fc77-35a6-b11f-b0daad8407bf | -11.28103 | -45.5162 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3762f7d1-3d0f-302e-82b2-0c85f17d1b8d | -11.76811 | -44.91796 | 2026-10-06 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc4c3f3-ef91-3b16-a696-a931b2749667 | -11.2779 | -45.5083 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 971aec60-ec8d-357e-a180-55df87849778 | -11.27464 | -45.52167 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2c0a1f25-c951-3449-8613-f087703c5826 | -12.2132 | -44.27732 | 2026-10-06 03:45:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b5b3622-85b4-3d8f-ac93-29efb9906caa | -9.60447 | -40.61262 | 2026-10-06 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 49600143-4b12-3417-84f5-1e0f58d93050 | -8.70471 | -45.21897 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ce7bd7c-bf3c-3ccd-96c4-b1ddf8352a6f | -6.88344 | -43.68579 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d6471a9-e161-3a28-9808-f3f5366a7d1c | -6.88095 | -43.67077 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffeb7b01-230c-37b5-9d18-5f4365413633 | -6.88045 | -43.67363 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0952b011-4d0e-3c8c-b731-70a6b6e77ae6 | -14.07122 | -44.48376 | 2026-10-06 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237c2bc2-805c-3044-863f-9ae901d73864 | -6.92612 | -43.67567 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29342bee-9893-3493-a994-b09fab1099f0 | -9.82723 | -44.79392 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0aa7b3-57bc-30d3-ad44-6db3ff3bce30 | -9.95254 | -43.48151 | 2026-10-06 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80721ad6-ed03-3f6a-b9fa-2d41c190fa53 | -12.75917 | -44.87474 | 2026-10-06 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48d311d9-c861-3105-94cf-14f692ef5ab2 | -9.83177 | -44.79781 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07c1657c-9a7e-39dc-b554-8b3b0a3b92c2 | -11.69571 | -43.67002 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4c7c37bc-ab4e-3d94-9130-a331955fb884 | -6.72396 | -44.2816 | 2026-10-06 03:45:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d481772-28fb-3b07-8d4f-cba52caab42d | -11.26662 | -45.50677 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 353afcaf-0348-3c68-ac85-b2883c3b126f | -9.81699 | -44.79237 | 2026-10-06 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70b59bc5-8d94-3967-a225-fafddaa500de | -11.23818 | -45.25959 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4091ca00-7219-3134-8fb7-0d8011c85163 | -6.71623 | -45.9743 | 2026-10-06 03:45:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0741fd7a-574d-32dd-80d1-fcfdaf079351 | -6.2285 | -47.00021 | 2026-10-06 03:45:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README23.md)
