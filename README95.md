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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e723240-499f-3ad7-ab81-60cb4d1d7ba5 | -7.80542 | -46.97734 | 2025-09-28 11:38:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| d317a400-9cba-316d-96cb-964201d5691b | -12.98737 | -40.92143 | 2025-09-28 11:38:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| f94920f7-aee9-381f-ac05-771d53a5a19a | -12.13409 | -42.65938 | 2025-09-28 11:38:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 38.9 |
| fd64497a-0691-360f-bd07-820fe205871f | -10.41412 | -46.14189 | 2025-09-28 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d003270b-02ec-3b74-a249-70190731998b | -11.97477 | -48.02724 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ca0df444-e93f-32bb-9550-0ed1d3012f06 | -11.40464 | -46.96612 | 2025-09-28 11:38:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 299.1 |
| 21384fd0-9d29-3fe7-a926-680f3f4d1bb4 | -12.27194 | -44.09356 | 2025-09-28 11:38:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f4b01310-ad25-37f5-b0c9-f670e258601f | -12.93141 | -45.18634 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b296b115-003f-3ab1-85b4-b26674cc2b04 | -8.51172 | -44.75852 | 2025-09-28 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 6a4ce2c7-db82-38b2-88f0-b1be50c71926 | -11.95556 | -47.9076 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d6bd8db9-7386-3356-bfd3-3f50a5e1bf81 | -12.71302 | -42.49836 | 2025-09-28 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| fcd17e00-3942-346f-b013-6db490ef7a62 | -12.29409 | -44.06708 | 2025-09-28 11:38:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 5b9fd72d-dfe1-36d5-aa6e-b3e97090ba54 | -11.69263 | -44.42418 | 2025-09-28 11:38:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e4218985-f9a5-38b4-a995-12e48314b4e1 | -12.39744 | -45.00649 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 06e72090-c869-3a15-9b8f-addcc5b2ba28 | -12.96042 | -45.18468 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cd8a67f3-f7a7-3b36-9f90-744bbc5ca4aa | -11.98424 | -47.05573 | 2025-09-28 11:38:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d6dcacb1-fc4c-3a6a-86de-4aef55c434cd | -12.98897 | -40.91086 | 2025-09-28 11:38:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| fc08d40f-149d-365d-a332-01e60d7b13f9 | -12.93842 | -42.2392 | 2025-09-28 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 4b0cc8ad-5c8b-3412-814a-3b32d8977e3e | -11.68936 | -44.44347 | 2025-09-28 11:38:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ab28943e-57fd-3924-831c-0c557beed43c | -11.45142 | -44.99632 | 2025-09-28 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 8c004ff1-e7ba-3d73-a044-97725e0b21ab | -11.99414 | -47.08902 | 2025-09-28 11:38:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 1a1d353b-03a9-3cd1-8182-16f967e4a5cd | -11.44783 | -45.01761 | 2025-09-28 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| a5efd353-09af-381e-8b1f-340b0bc95554 | -13.37361 | -42.47355 | 2025-09-28 11:38:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 9073c2a1-f3f7-355f-b489-7755ebe5d15a | -7.74989 | -47.00587 | 2025-09-28 11:38:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c361675e-ead4-326e-aa9d-4749bef9983a | -12.68923 | -46.88678 | 2025-09-28 11:38:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f5b1cbb2-c8bf-311c-923a-508b4feb8fd7 | -9.058 | -45.5313 | 2025-09-28 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| be467755-732d-339a-8ec0-190bccd8a04b | -12.2829 | -44.0568 | 2025-09-28 11:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| bb4d6eec-e76a-312d-98e8-63295c62f76f | -9.0913 | -45.8673 | 2025-09-28 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 308a0c9e-4344-320c-8b3b-d9391d4ae339 | -11.979 | -47.0847 | 2025-09-28 11:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 7f3ea219-53b9-3e48-9e01-047d0291bdc1 | -7.3849 | -47.0157 | 2025-09-28 11:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 160.6 |
| ae10748c-b17d-3eef-b700-716e0b336c92 | -12.2825 | -44.0804 | 2025-09-28 11:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 76370c15-a77a-3af0-9612-ddc125c4552f | -11.4083 | -46.9597 | 2025-09-28 11:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| bcbf1ecf-d7b2-3dff-8ed0-7db2546fbcd0 | -7.3847 | -47.0378 | 2025-09-28 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 310.2 |
| 06bfe0cc-a1e7-3369-b912-8fbeca6d4813 | -12.9547 | -45.1618 | 2025-09-28 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 269e54a9-bc8e-3cf0-838c-faf2c2fd6464 | -14.89269 | -45.58503 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| bc2e262d-755b-3ae1-b94a-52221e43244b | -13.60679 | -47.33713 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 355.2 |
| 11419aad-2c7a-3b55-828c-52b8f1d45120 | -14.8939 | -45.57051 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| f6ba5b79-64fd-33b2-bf3f-3d06df918b0b | -14.38845 | -39.25497 | 2025-09-28 11:40:00 | TERRA_M-M | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 0f4c1667-d1a4-340c-8bae-042751972246 | -14.77953 | -45.69485 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2730a6be-fe31-32ac-90f5-ed7295b2a811 | -17.18523 | -43.39038 | 2025-09-28 11:40:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08dbc594-b3e0-3a80-9bd8-135aa9da9e2e | -15.90026 | -46.21156 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ff006c59-fbfe-3750-b32f-b4539947f8b8 | -15.15122 | -46.42606 | 2025-09-28 11:40:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| ced8015a-b00f-380d-9018-f5391f9af553 | -13.60162 | -48.08499 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9861f6aa-a3f4-3e8d-b6d9-c102141a8bff | -15.11162 | -43.92848 | 2025-09-28 11:40:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ce7dc5b0-cd78-36b6-a143-9d1cf7dffa23 | -13.61891 | -47.34539 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| c97011c6-0264-3514-9d8c-95fca3577d1a | -13.62489 | -47.3123 | 2025-09-28 11:40:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 56f852bd-7fe5-3ee5-9109-5a903e9b3980 | -15.49819 | -45.89442 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| cbe03da1-e8cb-3725-9445-f7e03c76253e | -13.77262 | -47.86949 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 88ffa3c9-4b4d-38a8-855e-ba89c020bc93 | -15.9054 | -46.20606 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0232b642-3664-3c60-afdd-955a1c3b2815 | -14.77318 | -45.66561 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c557539f-86b0-37e0-81c4-3180a63bf3ad | -13.60979 | -47.30924 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9db76cf6-a06a-3d49-a8f4-d5892379cf07 | -14.78257 | -45.68938 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fa100ebc-dbe6-3124-a8bd-a60e215f7e0d | -15.49886 | -45.87838 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 549ce848-a5ae-3db0-8170-c92a6a4e96e8 | -15.33147 | -47.88686 | 2025-09-28 11:40:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| a78bed64-9591-341a-8c04-0b0655924efb | -14.89628 | -45.564 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 257.1 |
| b564577e-3bdf-38d9-ba01-2f12e0e1b766 | -14.58658 | -48.267 | 2025-09-28 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 405461bf-1bed-31b4-b257-96f487e94f65 | -15.49503 | -45.89972 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4cc579e1-acbc-3b01-a56d-74d6e8016280 | -13.78815 | -47.87362 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 25e30d79-6f1e-348e-a798-c0c94c8b0e96 | -13.61006 | -48.07959 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 8e1ae890-4d3e-3ec4-b3b0-4112ad097079 | -13.60372 | -47.34265 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 2479e3b2-d184-38a4-8719-a02c8dcfefe1 | -15.50187 | -45.87297 | 2025-09-28 11:40:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 96b9c79e-9c73-35fe-bad1-0806f4f2dd17 | -13.6125 | -47.30429 | 2025-09-28 11:40:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 0d2e6fd9-2d79-352d-a1f0-4873afb9dd05 | -13.78159 | -47.87716 | 2025-09-28 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| f515588d-3e18-3cc7-ad1b-732b4483c0af | -14.43467 | -44.87286 | 2025-09-28 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e66e25be-e313-3a9a-ade3-eedbd1aa18aa | -19.49864 | -41.12378 | 2025-09-28 11:42:00 | TERRA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 8746e30e-51e2-310f-9987-3ad3939c9ae5 | -18.21017 | -40.23603 | 2025-09-28 11:42:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 736cce14-e0d0-3dde-befc-2e62e34165ca | -19.6764 | -43.71745 | 2025-09-28 11:42:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 237b3ed8-40aa-36db-b96a-a5740171fec7 | -17.72451 | -46.71607 | 2025-09-28 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 15fd2521-cff3-3185-b49e-cdccebb12d30 | -19.32441 | -43.80224 | 2025-09-28 11:42:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 35e93cde-329c-346f-a461-d97158a43b08 | -17.73693 | -46.70164 | 2025-09-28 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 13a77faf-4e0a-385d-a327-1fa377134430 | -22.06071 | -43.00975 | 2025-09-28 11:42:00 | TERRA_M-M | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f98d5d05-50b7-3a66-9866-32ab4f334aae | -17.1586 | -47.29448 | 2025-09-28 11:42:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| aa2f100a-3b9f-354e-a1c1-3718923562fa | -20.05253 | -47.0475 | 2025-09-28 11:42:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2f92b347-2ca4-3981-af1b-597f448faf58 | -21.55954 | -41.16351 | 2025-09-28 11:42:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ca9712ea-e912-3b53-8da1-91b7e30c26a8 | -19.32222 | -43.81547 | 2025-09-28 11:42:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5220cd4-0367-3e9c-95e2-4f69ca4befa4 | -21.5506 | -41.16202 | 2025-09-28 11:42:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 30ef4a00-3b09-377e-87b1-7f5d7fc2fbf2 | -19.71836 | -40.64113 | 2025-09-28 11:42:00 | TERRA_M-M | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b779fd14-2d37-3a56-9d65-d996b22bee38 | -19.86799 | -43.8048 | 2025-09-28 11:42:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 5a1da4cc-0733-3c58-bbe8-e8f2d79e582f | -17.41302 | -44.87053 | 2025-09-28 11:42:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6bc79022-52a4-3d2d-9383-ded7eac203f0 | -7.3661 | -47.0173 | 2025-09-28 11:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4a439c91-7d8e-328d-9fe7-bd7af7c677ef | -7.3659 | -47.0394 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 6b5b53c8-361a-349c-bb55-1ebbfbb786fd | -12.0214 | -47.9703 | 2025-09-28 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8bd062d5-61fe-33e5-8b16-d7b5e3621ef2 | -14.7851 | -45.6818 | 2025-09-28 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d76fc547-d020-3524-a081-40d685553cdc | -7.3849 | -47.0157 | 2025-09-28 11:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 159.7 |
| f90bbc39-5f22-30a0-9e38-e20273b94ddf | -11.9982 | -47.0821 | 2025-09-28 11:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 13d520f1-622c-32dd-a225-fae0856bb34f | -12.2825 | -44.0804 | 2025-09-28 11:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3fd5ebdf-0f28-38cb-9236-b19d2f659eee | -11.979 | -47.0847 | 2025-09-28 11:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 5dd91093-6b6f-3b8e-a2f4-46e018448976 | -7.8163 | -47.0003 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d4a44fef-af60-32ef-b8ba-3c159f059fbb | -7.816 | -47.0224 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| be0b466b-edd2-35d0-bbf0-2ca420696d6b | -7.7785 | -47.0258 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f6b3b63d-7edc-3b88-b65d-f065e1a80be2 | -7.7972 | -47.0241 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e25c8003-4e83-3543-865e-7948086962a4 | -7.3847 | -47.0378 | 2025-09-28 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 305.3 |
| e29d44d7-17dc-3051-be23-75bef4fb0191 | -12.9547 | -45.1618 | 2025-09-28 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a08bfc33-5ea2-32a9-a06c-b906f91d8af6 | -7.3849 | -47.0157 | 2025-09-28 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 9b723c71-714f-3750-9910-1ac523da9b5e | -12.0023 | -47.9728 | 2025-09-28 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 942f457d-3ee1-3609-87ed-c8ab5ee4b078 | -11.4083 | -46.9597 | 2025-09-28 12:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f87cc0f7-759a-3902-bc03-5288ef7f3381 | -7.7785 | -47.0258 | 2025-09-28 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a5aa55e9-8b15-32f1-ab5f-7fa72c91eebb | -7.7782 | -47.0479 | 2025-09-28 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6e3678a4-2f99-3d4a-b6d1-ce6eb8c07537 | -7.7972 | -47.0241 | 2025-09-28 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 9e137947-3f4e-3cdf-abaf-945e9291ae14 | -12.2829 | -44.0568 | 2025-09-28 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README96.md)
