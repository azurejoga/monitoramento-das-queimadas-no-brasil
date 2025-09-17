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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1664e5e-3105-397c-b1b3-ddeb07cade21 | -7.34747 | -46.75078 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7fc8595-3cf6-373e-9b71-e462755a2179 | -5.61118 | -42.90764 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ef5fb80d-27d9-37d1-941d-bfe48a3ec78d | -6.29055 | -35.20122 | 2025-09-17 04:10:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d359f05e-08d1-3ff5-abdf-655e08d1c651 | -7.5915 | -44.58055 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 537e9e4f-d44d-3347-9b95-0158c64d7b60 | -6.34972 | -43.15925 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 884d8391-ce19-3724-a0fe-71235d260300 | -6.96477 | -44.77983 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2e2b7e6-2e12-3b83-904e-208686252fe4 | -7.26536 | -46.59861 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f1e115-425d-38f5-8836-ec95d4e695be | -6.45263 | -43.32265 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e51f738-25c3-3855-8881-966027aa3d07 | -3.42081 | -47.60905 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 029a7524-88c8-324c-bcd8-7847985ae82e | -7.58505 | -44.57534 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 649e574f-27d2-3246-8919-8e71dcf9b7d0 | -6.18474 | -45.11515 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e321974-4aee-3b48-8cdc-682dbd9e02a5 | -6.52257 | -41.818 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d23e9ed-4c09-35c6-acad-7d2b4b80dfab | -6.9574 | -42.44285 | 2025-09-17 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f6347ba-91b5-3fff-9ac0-bfb9c22a7502 | -7.68223 | -44.47187 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec4aebd-c6c9-397b-8116-9fe2c4fc55ce | -7.61533 | -47.46067 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01821101-e9c2-319e-a75b-9932bdc063c9 | -9.0587 | -44.87611 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc74930c-9898-3699-b9ae-ab15415eeb70 | -7.67869 | -44.47129 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e25a819d-464f-30dc-9cd4-aa07c028d5ac | -6.88205 | -43.97625 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 703fde9f-a614-3acd-94cf-a67d29d967e5 | -7.83701 | -43.85217 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 878e22e6-3815-3eff-8184-c47c72c59aa6 | -7.34021 | -44.59109 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 802eb61b-1869-3fc2-a2fa-78dcb867f135 | -6.87343 | -43.96295 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9c1402fb-43e8-3f3b-8bb7-c7cd2f056249 | -7.06951 | -44.35133 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 043e394d-8f86-3aa2-8384-6ed4a3f06513 | -3.0734 | -49.46452 | 2025-09-17 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c715a476-cc5c-344f-b850-56e7b0674a49 | -7.58371 | -44.58342 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 845474fb-20a2-3282-acd8-8e7c93293984 | -8.96084 | -46.00909 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd8d61aa-0ce1-324d-911d-9d68adffeab8 | -8.12992 | -43.64162 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1291516-de99-36b4-b668-8f1e7168461b | -4.71616 | -47.22057 | 2025-09-17 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e0a5bf4-589c-34c8-9311-149984ef6fd1 | -8.34845 | -44.71868 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4a442cd-cc0f-3066-82a4-d85810956d98 | -6.29647 | -42.38415 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1d602a5-a681-347c-90be-d35ea559f27c | -5.39752 | -46.52747 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24bb96d-3b8b-36eb-8c74-3318f942ff35 | -8.57128 | -46.34185 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68f3c652-a480-3093-8337-fb739b9aa2ae | -3.84835 | -40.35154 | 2025-09-17 04:10:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4b479b4-74e3-3895-8c56-c07218154ecb | -5.67034 | -45.04548 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a19764-8718-379b-a2c3-53a5c757fc75 | -5.66213 | -45.04875 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ebab226-17b2-3163-af81-543110073e39 | -7.2544 | -46.61462 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ed128a-3595-3236-bbf3-17657ba6fc08 | -6.40271 | -43.34877 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c615e01d-f340-34a2-9dd1-41b7ba5cdc1c | -8.62419 | -40.1977 | 2025-09-17 04:10:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0efe4f93-56cc-3c39-8ac2-a2b2f0634608 | -8.98912 | -45.75321 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 033d9e12-f816-3723-b5d4-4218304f69d3 | -12.72396 | -48.02943 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70819d74-d727-369a-889e-33d4b0556f25 | -16.02846 | -45.16779 | 2025-09-17 04:12:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7b43c95-7e9b-305c-8159-58ed725b4c33 | -13.2823 | -54.18123 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3e6d3a8-37e1-378f-b8fe-e482cd9f9479 | -13.95139 | -44.91869 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8ec3425-9fd7-3835-8d21-811437c02db1 | -10.79086 | -45.97451 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2ffe673-3122-3e54-b2d2-7a2aa33e7fd7 | -13.2666 | -43.29708 | 2025-09-17 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8e00dd74-1e24-3590-ad6f-fbd649fae090 | -12.71821 | -47.99105 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 112de575-40b0-3b69-b4c2-4fec7b3f79a1 | -11.93809 | -38.33118 | 2025-09-17 04:12:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e140358-99ce-38c9-bce4-5570d116a14f | -13.14977 | -51.61406 | 2025-09-17 04:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 456b5cac-9c74-38a4-a64d-bd2175c8a094 | -12.35521 | -47.05702 | 2025-09-17 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08a27201-b6cc-3776-8393-61e9c4d23766 | -14.62347 | -46.39016 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed6f7062-32f5-3ff6-aa9c-254722c5dde9 | -13.18099 | -47.3134 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b178a337-df9d-3c4f-9fce-8930df739f53 | -12.64312 | -44.86256 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cd2f09f-4896-3dd3-b980-4cb2b1211fd5 | -12.9494 | -47.95817 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d373f92-68f8-3d59-8e48-a217e928d600 | -15.04973 | -42.47737 | 2025-09-17 04:12:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd3bbb51-dcaf-35eb-adf9-438269dfeca8 | -15.42239 | -46.14931 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 460dec61-236c-350d-816b-9b1763c8b34f | -12.6957 | -47.95385 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6a88ca8-ce95-3576-9eb2-9226f7250eea | -12.85817 | -47.13106 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c90b0173-fafd-386d-83af-b000c271b4a9 | -15.00329 | -49.24988 | 2025-09-17 04:12:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0fe5238-d713-3b2d-b2f7-d44fd0f53c56 | -14.6012 | -46.39105 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a173293c-ea00-3e02-8b4b-a7b870501331 | -12.11374 | -44.81036 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b910f6dc-de98-3288-9907-0ee0b04053c3 | -14.86161 | -45.12222 | 2025-09-17 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b1a756d-cfc9-30e0-9204-5508785267fa | -12.35139 | -47.05632 | 2025-09-17 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a84dbd54-420b-382f-92fd-10d6f9cd5172 | -10.87263 | -45.43562 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9179b643-2e01-34de-ba80-553b59d0f3e6 | -16.28546 | -45.68296 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06f548ed-dcf3-3204-af09-f6d9386d075a | -11.49053 | -43.61548 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63d35b66-7b0f-33b3-be5f-9ad6e9b752c8 | -10.80281 | -50.7067 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6458a505-f4d0-36b9-bfe4-d96844296c9f | -11.46507 | -43.55979 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 105cabbb-26e5-3868-9ee8-31eb39aaeccd | -11.02789 | -45.06403 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 266ca422-5f36-3e4c-8296-ed7c733a79ed | -14.83117 | -51.70761 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e392a6f9-f392-36f7-82af-c79e4d85b272 | -12.1062 | -44.8131 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf65ab7d-0d4b-394a-8431-eaacaf36a296 | -10.83817 | -42.80342 | 2025-09-17 04:12:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f05fa12e-1a20-3349-ba24-c43ff75a32a1 | -10.81143 | -50.66134 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 44780f6a-1ea6-37f1-92f5-fb104337902f | -14.61193 | -46.37118 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df569543-bca1-37e3-93e1-3a6f54f922ea | -12.96556 | -47.96004 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6813563e-69d8-3afc-bf88-bcce15fb74cf | -12.10647 | -44.83285 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb1915c6-0c20-3907-be53-4732393460da | -14.84263 | -48.35154 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64d0301e-0bee-3d2e-9656-ed16db8dd3d2 | -11.16866 | -45.32414 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67ad26ee-97a4-3493-9319-4dec7c83aa56 | -14.14086 | -46.98489 | 2025-09-17 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb29fac6-17dc-30f8-a02a-b1db16c5b176 | -13.28142 | -54.18552 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a7c451e-4b8d-3d6d-9154-2765e63e3318 | -16.85597 | -44.05115 | 2025-09-17 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bedfa003-0edc-3e87-83d5-d9aa73177a22 | -12.3638 | -43.20712 | 2025-09-17 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a1f7bdd-c5e8-3a85-8303-eee081ed77e3 | -14.79942 | -51.71283 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 805bcb9f-f2cd-3afe-8814-1e0d9655c59f | -12.7142 | -47.99032 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 770240a2-8937-33c9-8fbe-b319ffc061b7 | -12.70352 | -47.76873 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07775cc9-03fd-3df2-970c-795449d46712 | -15.92796 | -42.63538 | 2025-09-17 04:12:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f8b29660-a642-3612-a5a4-c8b783f17856 | -12.24529 | -46.75646 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b875b0-723b-3f2b-8772-6a563464ced5 | -10.30027 | -46.63909 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd569358-bfa1-3d04-84d6-53eef892885b | -16.11254 | -42.61558 | 2025-09-17 04:12:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 512207e4-e65b-3caf-aac6-9d0c0a8f4da4 | -15.43025 | -47.32088 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81aeb1dc-332a-36f1-85ac-c2b50ddf67d8 | -12.71205 | -47.97882 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c009f61-e9a9-3d16-8220-32872d835f42 | -14.60695 | -46.37884 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39e5a7bc-160d-3a75-8d1c-101c1feefc0c | -12.72316 | -48.01081 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 75d44f62-ed3f-3b21-b850-1e10a6e0aa1c | -12.06327 | -46.55397 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac3dc5d-c47c-3d8d-991c-cf89fc98841f | -13.64973 | -43.6525 | 2025-09-17 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7c87ff1-c8b4-3c0b-bae7-d96b73575334 | -12.70169 | -45.80702 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6790da0c-1fb1-3839-b281-fded1fa692ad | -15.39631 | -46.13228 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30d69467-e046-3509-8d65-aa8cbeab7806 | -11.11965 | -45.11902 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 957821ee-7e64-3208-9db6-fa68fdaf4a81 | -12.72042 | -48.00296 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 186b395c-cb2f-3885-b36b-c120e0475761 | -15.41673 | -46.13992 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88533668-cdab-3e72-bdc5-30f72c0d2ff7 | -12.06265 | -46.53511 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af01680a-ba66-355a-b81e-c4c0c9cc3821 | -12.70047 | -47.76279 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
