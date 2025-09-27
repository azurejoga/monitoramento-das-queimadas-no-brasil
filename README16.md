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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 416855b5-8b0a-303b-a924-0cbde43f4cf2 | -11.55226 | -45.2911 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50768359-6d7c-3587-a6e3-aa04a0b8e29e | -10.45547 | -48.20985 | 2025-09-27 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f7340cb-c653-3f73-b5bd-05f5a4c95d53 | -12.27477 | -44.06602 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60011a7c-c3c7-305f-ac8c-de110bc247e5 | -6.89607 | -44.16063 | 2025-09-27 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88f9cb42-0b56-3785-bccd-f9dfca52997d | -8.36755 | -41.40201 | 2025-09-27 03:55:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f612a2dd-93b3-310b-8e03-1d973a7aff38 | -11.43469 | -44.92749 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d55269c9-4bf9-341e-ab2b-8cbb8cfe5de4 | -7.72355 | -47.30405 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24d64e0-a898-355d-99c7-636945409af7 | -12.03793 | -47.06382 | 2025-09-27 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b2ef78f-c080-3d13-a171-a143b91b4530 | -12.30152 | -47.21992 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e04cdb99-fa5b-3e1d-86a1-6456ba336d2f | -11.42069 | -44.95913 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d00fff-6cbe-3e29-a71f-fc6e5f5e749c | -7.72299 | -47.3071 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4298229-f10d-30c0-8d19-3c7b4aad8355 | -12.36631 | -44.14527 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6d0c864-84c9-32b3-804e-5c717ecc4459 | -10.55913 | -43.7199 | 2025-09-27 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19e1f770-6f95-3336-96c0-4ea79da3f3fc | -11.69804 | -44.41549 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23e88c23-80a4-3b92-9bcd-3447b0d81292 | -8.91398 | -46.09762 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dac04427-f3de-3a47-8610-d9497b1e2cbf | -9.09681 | -48.90797 | 2025-09-27 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 13e9a4cd-8bbc-3472-8268-6459a90d916a | -11.62664 | -44.43221 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a1be715-d3ff-3d4d-8f92-0724a8555dfc | -6.95827 | -42.30528 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4aad9da8-1015-37b7-82af-0b2a5e7c06f7 | -10.04961 | -49.20209 | 2025-09-27 03:55:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21dcad48-3307-31ff-85c3-a7124021cb0a | -11.47674 | -43.52055 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35ba3ceb-30e4-38c3-b193-65d64f0423ec | -11.78251 | -43.75861 | 2025-09-27 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c83deff3-f1a8-3e2f-a5fc-23ff92d9e3e6 | -12.87899 | -47.09582 | 2025-09-27 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1516a597-7b34-3754-b29c-52120748f6d5 | -11.38237 | -44.94079 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cda39e7-a12a-3aa2-b521-697c91320d4b | -11.66943 | -44.46626 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 88a4cec2-f859-3d01-b309-6c3eaba6fd67 | -11.70892 | -44.42267 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 624387ba-d9b2-358c-bc4a-249fb78d4cbd | -10.8624 | -47.79275 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8c02552-73e3-3fc8-a95e-8e02e67ea64e | -11.69178 | -44.40681 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47715391-b565-3701-a070-a031860fdfff | -11.68523 | -44.42146 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b8a24f5-ca77-31a0-981c-d5c1a776251a | -9.75554 | -46.14317 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a76146-8100-3c40-893b-682ca1b05706 | -7.27534 | -42.97389 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8aed4e05-0a68-3b75-8099-4562d3ae87d5 | -7.78666 | -46.95071 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6654d807-7d89-33f4-90c0-d3b7cb949a3b | -11.5006 | -43.53869 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2e9ae5d-ff81-3529-ab13-47356137d68f | -7.71526 | -47.30284 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac8d1317-34b7-3551-aaf3-52ecf9686e4a | -8.72253 | -46.69085 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2117563d-747e-3b15-80b0-87831ac9d0d0 | -11.36024 | -45.02003 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d9664dac-1e58-3c27-b597-8ac9fc4e7015 | -10.28551 | -45.21857 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2bc48c0-124f-3ca4-add2-1736ccc957fd | -6.92307 | -44.25581 | 2025-09-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f23b483-346f-3e49-8545-e99318f1afa0 | -11.69658 | -44.44988 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c0b4562-5521-3dc3-92a5-e6d279bc5daf | -6.80769 | -44.47485 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 940f81fa-9cc6-3d67-9540-1c0a461db646 | -7.85147 | -39.08933 | 2025-09-27 03:55:00 | NOAA-21 | PENAFORTE | CEARÁ | Brasil | 2310605 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4992c541-4105-33ea-948b-40ce6ae8b960 | -12.27261 | -44.05574 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7685b338-4801-33f7-83e4-534eb534aa52 | -11.38434 | -44.97824 | 2025-09-27 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b478057-c23a-3b82-a98e-f42dd5cec578 | -9.08674 | -48.02362 | 2025-09-27 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b9e5ede-248a-3417-8f9f-d8490415e3b7 | -12.03237 | -47.06789 | 2025-09-27 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 59334aac-d065-3f12-9f49-6555c7e9a466 | -7.72244 | -47.31016 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae7eb8d-b09a-38d6-a778-62dfaaab27a3 | -13.1513 | -43.31141 | 2025-09-27 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0cc0a2c9-a525-32c5-aa15-0e5dc3dd6eb9 | -8.72828 | -46.6864 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb2bc869-b448-3a20-a1ca-b1382a5a528f | -7.05538 | -43.02389 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ca3e8b3-a746-322d-b8d6-6c50676b1a74 | -6.8169 | -44.47228 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4c71d5ca-886d-35c1-b810-81d35ad9af41 | -13.72787 | -43.72323 | 2025-09-27 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3169c5a-a2df-33c1-b64b-6c09cfa5fcbb | -6.78621 | -44.85949 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcca7db1-e910-34d5-a61c-2d42b622304d | -7.80633 | -46.95982 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18854199-71ed-3026-85ac-787d026ca472 | -6.70857 | -42.75387 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e77941e4-0529-305e-abc3-d6b61a12ff5d | -11.35744 | -45.01181 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f388181-0635-3cf9-add5-e2b4b9752fc9 | -9.9719 | -43.60838 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81319535-21f7-36c4-ba77-dec182c232e8 | -12.2978 | -47.21404 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce4acfd-8059-369e-91a5-61c5f4e64183 | -7.26484 | -42.97947 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 678199bc-69da-3768-9263-80090c909266 | -6.70249 | -42.74321 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bd75ae4d-2b3c-3534-9d4f-e67fb0132ec0 | -7.71902 | -47.30009 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d138955-3a8d-3b08-a2e3-7a4d9825cc84 | -7.60662 | -43.05344 | 2025-09-27 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7790776-42a3-307d-af01-4c956fdf9448 | -8.85974 | -46.61384 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80f99c0f-2d23-37e2-b447-5cd17d7417fe | -11.37704 | -44.99612 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26e993b8-3a97-3a0f-98a3-f36f3126f0fb | -12.05644 | -47.65628 | 2025-09-27 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb7ee2bd-7619-31df-8369-abd403c85761 | -10.85893 | -47.7836 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7785091b-7251-3b7d-aecd-0dd2b11f60e9 | -10.86344 | -47.78709 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d23d8eae-1bc5-3926-b143-90516dc23af4 | -11.24019 | -45.5583 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c214d1f1-e652-393a-932f-9dd0fc459a27 | -11.35959 | -45.02379 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d593e5a-9790-3b23-b0ec-5285a7aea32c | -11.97135 | -47.86814 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e74090a0-913a-38cc-86aa-18bb235ad4b0 | -7.8122 | -46.89853 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f0866675-887a-327f-9267-2860260c9919 | -12.30666 | -44.35243 | 2025-09-27 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| f25c5fce-751a-37e3-aef2-cbaf0050a163 | -11.69168 | -44.45129 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 073def66-47a8-311f-82a4-fa317dbfc706 | -6.96125 | -42.31028 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 416962a8-8056-365e-b01e-7d9a44a570f9 | -11.62753 | -44.42708 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ff17cf-e648-3a9e-bc7d-a9cf43401330 | -12.29868 | -47.22229 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ca7557b-33ea-3305-ae6b-e517e17b73a6 | -8.37104 | -41.40255 | 2025-09-27 03:55:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf29cb8a-39e1-367f-b5ac-687d23ca963f | -7.19267 | -41.70481 | 2025-09-27 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 09bcc73b-6f52-34d3-86f4-458a4a64e245 | -7.0311 | -39.62978 | 2025-09-27 03:55:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5bd863d9-39cd-30a1-aaa7-3cde4ea0d8dd | -11.71645 | -44.40297 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52a422a5-4751-31cb-af11-cc19329cbded | -12.27769 | -47.84071 | 2025-09-27 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6964765-2b57-34de-8d38-b7f1d7cc7792 | -9.05219 | -45.50171 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650a13de-e0dc-31f9-8f09-01012792df9c | -10.8584 | -47.78649 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac52a1a0-470e-32b7-8e50-91676d9069a7 | -8.52385 | -44.64041 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e37172e6-6445-3676-90fd-0fee75e28485 | -10.1214 | -46.47919 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8447cd5a-fa30-3f85-b7db-cfb4f8b07013 | -11.37961 | -44.98123 | 2025-09-27 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b061dd88-9da8-3343-96aa-9895c0e568f3 | -12.9374 | -41.91728 | 2025-09-27 03:55:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf87cda0-1235-3b4c-a362-e15958fd43a3 | -6.61348 | -42.21745 | 2025-09-27 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6801c1b8-8d36-3f0c-98da-ae864a8f312b | -12.28104 | -44.05233 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d17c6b36-e560-330e-81dd-2d97d7ed5db0 | -11.43153 | -45.01716 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96c990bf-ec4a-3c53-9861-5e6b6fe55954 | -6.99774 | -42.38993 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7b15116-3900-3d2c-8c5e-4a38c56ed65b | -6.99614 | -46.99163 | 2025-09-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df776341-e182-3664-a88d-28099f223edf | -8.82357 | -46.26084 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b4ad71-0c55-3b86-bd39-3c83e8319390 | -9.89277 | -49.1265 | 2025-09-27 03:55:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a37e8371-d5e0-3ba6-a65e-13fd3f9d0b26 | -10.80297 | -45.37091 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b41beeb-2056-3e0f-b82d-1e525db564a5 | -8.14118 | -42.37486 | 2025-09-27 03:55:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e8edc6f6-7158-3fac-abb6-4024997c5a4d | -11.79451 | -44.93036 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f519f054-6ba1-387a-9ec5-4daa614c74cb | -11.38766 | -44.93452 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1215ef0c-9143-3f49-8a9d-b9e693d6599e | -11.68828 | -44.42728 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c541d445-c33c-36a3-ba24-a7021a37d0af | -11.43129 | -44.92296 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbc73f6f-812c-3a64-b6fe-cf4ad630c2b9 | -8.5141 | -44.61563 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9818f28-2ca9-3efc-b05a-2118e057f058 | -9.04155 | -45.53636 | 2025-09-27 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
