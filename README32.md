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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a70593c0-ed4a-3aca-b56c-f3d8083f084a | -4.2419 | -42.65855 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9f454363-7aee-31b4-a102-ba3738e2a8d7 | -6.70108 | -35.02689 | 2026-10-07 03:23:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d80e0737-2fca-3a1e-b05d-826b0a939e4c | -4.4793 | -38.17732 | 2026-10-07 03:23:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83e687e2-6e07-3ac7-8534-06a80dd9fa5a | -5.97617 | -40.91753 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 59cf3930-4072-3f73-833d-b41d6a1e4a24 | -6.22757 | -41.99146 | 2026-10-07 03:23:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| f6fde0a6-4bf9-3bba-aa54-9c849ef8d664 | -8.71986 | -45.19257 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 151a8582-6719-3147-8321-0280fc94a21b | -6.92191 | -43.66621 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8bc82dd3-20b5-374f-b48f-ca1f67cfac65 | -5.9734 | -40.93324 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 462d3ad5-6dab-367e-bd96-bb023db7301a | -7.88004 | -44.19714 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ab51403-060e-38e3-ba24-5edecdf4fca0 | -6.31874 | -43.34042 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 20eae6d8-4609-393b-afca-2b92be7ebe45 | -8.71284 | -45.19075 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 35159728-be1b-33e5-8984-6d38c3ffbe3b | -7.86421 | -44.20586 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ef55bbe-da61-35df-b850-dac95806ebb7 | -7.87767 | -44.20925 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbcc481a-3094-3fd7-868e-7de6d4368b22 | -5.41733 | -39.10818 | 2026-10-07 03:23:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2ccfb88-561e-38f6-95c2-c7c0738bbb1a | -12.16083 | -44.70125 | 2026-10-07 03:25:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39f97d43-f19e-3db4-a933-3e155bd68e81 | -12.16964 | -44.71914 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7257662-6099-391b-b289-37839f242558 | -17.36978 | -42.13621 | 2026-10-07 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99495b5e-f884-365d-a4d5-6b3751cea138 | -15.32726 | -43.09538 | 2026-10-07 03:25:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34d904eb-f21c-34f2-851a-2f61ea1c2498 | -11.69721 | -40.11253 | 2026-10-07 03:25:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 963ab36e-eb6b-3887-8b49-af2adb4641ec | -13.39748 | -43.87455 | 2026-10-07 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfffd5b1-2877-31c7-ae36-87cc25fad41d | -11.67375 | -43.62643 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a400e121-30c4-3ebd-abc4-648bb1927ac3 | -13.63513 | -44.42088 | 2026-10-07 03:25:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c63a0ee0-adad-33fe-b0a8-54f9d27f084c | -12.16622 | -44.70813 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 769abb9f-aabd-362b-b6cb-661cfcdb162b | -14.7843 | -42.89586 | 2026-10-07 03:25:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0aa22037-2838-3c55-8632-2bd3127810d6 | -13.00736 | -46.00243 | 2026-10-07 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b01056ee-5b92-3385-b164-5aa3a3e2ef1d | -12.17576 | -44.72809 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c89c279c-c0da-3e65-a8ad-08fa99ffdfa0 | -12.19159 | -44.71202 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 324a3c5e-9fc3-303b-b2c5-2dfd3aee459e | -13.5038 | -44.3748 | 2026-10-07 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3a033a38-7e0d-3084-a570-1f685509250e | -10.97571 | -45.41225 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01250dcb-d9a1-3365-b64b-efeca69814b3 | -11.68209 | -43.62494 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8f6f980e-408f-33b5-bf52-5c1a0fc62c48 | -11.73048 | -43.66441 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0d93dc4e-f0a8-370b-a77e-65e91f094ec7 | -11.1146 | -45.73384 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba6e3a81-3289-33ab-8616-38af5f7827fe | -12.18028 | -44.73333 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fda41124-6c41-366f-aab2-1974a2df59d3 | -15.42513 | -43.7038 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 12.9 |
| c8186868-d3be-3e87-af12-934adc842b55 | -15.24359 | -43.27368 | 2026-10-07 03:25:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 80bdafe3-a080-3056-94f1-25b3a26e86b8 | -11.70213 | -40.11357 | 2026-10-07 03:25:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b6c4df1-a74e-35b4-a0fe-a358aca87d51 | -11.70472 | -43.66433 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6475b540-80c4-3ef7-ba5d-36af4171447f | -12.17694 | -44.72228 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc813ba6-040b-3a01-8f9f-9255a7f7d5a6 | -13.00825 | -46.00233 | 2026-10-07 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a60c215a-949b-37b3-b38c-a8affde6f9f8 | -12.16739 | -44.70243 | 2026-10-07 03:25:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb005ec-eea9-32c8-824e-6951554c9f78 | -11.74782 | -44.93665 | 2026-10-07 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77b460f8-ed97-37f1-a411-009d9d4f978c | -15.72737 | -43.92918 | 2026-10-07 03:25:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b15556d-ba52-3694-aad6-16248690d2be | -11.10898 | -45.7257 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba3a2ed0-7bf7-3082-9b4a-d2a68354b3ca | -11.10882 | -45.70366 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6d163eb-4ad4-3030-8708-951b50213491 | -11.73764 | -43.66079 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4f85fa14-6164-3a31-9804-ad93358f4968 | -14.78916 | -42.90065 | 2026-10-07 03:25:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76ab997b-8e01-3128-b2ba-3f75a67eb713 | -13.50588 | -44.36483 | 2026-10-07 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 72bac8e5-a1ca-30bf-b1c5-fa141cec526e | -11.73145 | -43.65955 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 64b0160e-5716-3187-970e-3e0482918839 | -11.63432 | -43.67127 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d26b2b4e-5b62-3dfe-bb50-cebbe8975409 | -10.89113 | -40.69405 | 2026-10-07 03:25:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b9f7796-424d-3791-acf2-f7f6c3076d45 | -11.23709 | -44.8715 | 2026-10-07 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5b679c39-4cf2-31d5-9d14-3c04e7f3078a | -11.69654 | -40.11061 | 2026-10-07 03:25:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1978288-95ad-3529-9ffb-0d4b11046baa | -15.42024 | -43.69826 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 4333fe69-0b74-3bd7-9f55-f907cc481a07 | -15.16214 | -41.2914 | 2026-10-07 03:25:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b34d26ad-705f-341a-8fcb-21d33dae39ea | -11.74673 | -44.9419 | 2026-10-07 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 504faa39-4fbb-3201-8d9f-fbf2046839dc | -13.63402 | -44.42627 | 2026-10-07 03:25:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f2d2903-6af7-3b59-8f71-d33227c57a20 | -16.40972 | -43.72659 | 2026-10-07 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b62a9d7f-9f75-3334-bea1-39fa46b46330 | -11.60745 | -44.14572 | 2026-10-07 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83dc78d6-c9a1-39e7-927e-6d090507ec80 | -15.23707 | -43.27654 | 2026-10-07 03:25:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 47.4 |
| d64a1ec3-0882-31e3-b470-078a8e876995 | -12.95337 | -42.4353 | 2026-10-07 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4c2866a3-bf33-3e2a-847d-b52f8eae1ce4 | -11.00435 | -45.44378 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 517fb119-153f-3990-b91c-12fb204b7027 | -13.5049 | -44.36955 | 2026-10-07 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 29133c0c-b357-3525-9db2-8b5218553ea3 | -11.68104 | -43.62222 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c74c4296-bb40-3d58-bc8c-5253489a1bdb | -13.37821 | -43.87562 | 2026-10-07 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d04c6319-ad60-39dd-b551-4fca2d6bcfa6 | -11.72723 | -43.64841 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12bb2099-0568-3b19-b044-249cac714aad | -13.5812 | -44.42854 | 2026-10-07 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23258b02-27d9-39cd-8626-f1e6012ac5d7 | -11.73242 | -43.65465 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4a8a7bdb-9375-340c-a067-258c8b35d5b5 | -11.01347 | -45.46964 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a08ed7c8-0959-3607-87db-f6d5c0777eb2 | -11.64062 | -43.67202 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d13fe3e-6907-3824-8ad4-4e7615187d66 | -12.17085 | -44.7134 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0c0c256-a6ee-3c88-be5a-5eb335e04333 | -12.19343 | -44.70822 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1efafd2-0d4a-32fa-9864-e10db19b1631 | -15.3362 | -42.76818 | 2026-10-07 03:25:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5691eca6-d5dc-395d-993f-b56337110d7c | -16.61434 | -39.58942 | 2026-10-07 03:25:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90499917-b33f-3af3-b8bf-221b2c7ff3c2 | -11.01137 | -45.44481 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccc994e6-9c69-3d74-832e-be0b7c6836cd | -15.42051 | -43.69999 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 70612080-2de9-3892-a086-662bb2156764 | -14.8899 | -44.81179 | 2026-10-07 03:25:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4759f679-543b-33cb-a1e1-cb2227609191 | -13.97236 | -42.50306 | 2026-10-07 03:25:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 54395625-df7d-3c7f-89fd-e4ffa72ae892 | -14.25148 | -41.62453 | 2026-10-07 03:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| bde7b124-a22f-3d5d-ae0e-a5892853c0e2 | -11.67585 | -43.62397 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 303024b4-5b89-3dbf-b516-66bbe62f1517 | -11.74347 | -44.94069 | 2026-10-07 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d78aaac-818e-3f33-b9f3-fc78041b4f5f | -11.72823 | -43.64342 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 31f441a8-7582-37d1-9c0d-6bb978b54839 | -15.41933 | -43.70256 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b856c8c1-89b5-32b9-b6b4-e81e2a9fefd6 | -13.7551 | -43.62478 | 2026-10-07 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb006fb1-3cba-3a43-aaf9-df6661b59da9 | -13.20672 | -43.90487 | 2026-10-07 03:25:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55b41bf5-74d5-35d5-b320-c85ed7306d5a | -11.62716 | -43.67479 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81ce237a-8512-3a32-81eb-1d275e7f1bf6 | -11.23032 | -44.87045 | 2026-10-07 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 84232a8e-a5fe-35f2-95df-edf26072fae6 | -11.1105 | -45.71857 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73ccb505-9bcf-3bee-b07b-217c0810eb96 | -15.24275 | -43.27776 | 2026-10-07 03:25:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 8b43cccd-26c6-3bd7-9597-0740774b0453 | -14.25214 | -41.62121 | 2026-10-07 03:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| e14fb8ba-4126-3709-b485-2c625d222f36 | -11.66963 | -43.62291 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21024938-f964-352a-ae11-57913697a773 | -12.16748 | -44.1744 | 2026-10-07 03:25:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87661ea4-d6da-34e5-9d28-d9325ff6da2d | -15.72873 | -43.93098 | 2026-10-07 03:25:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d4273f5-e578-3212-ae97-37678df78c2e | -11.00594 | -45.43613 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf27daaf-fb60-34ab-8c75-dc7170cb42c2 | -12.17159 | -44.71514 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a903d305-370a-38b9-aa48-106f92323fe2 | -11.23161 | -44.86421 | 2026-10-07 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c85a2c88-f1ba-3889-8b6e-a6337ed28f89 | -15.16282 | -41.29181 | 2026-10-07 03:25:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 447bb036-8d26-3f25-b52b-b8aebbb1bede | -12.17041 | -44.7209 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8075423f-3a2d-3c06-ab33-d68384bb232a | -10.97483 | -45.41198 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3505e1b6-2414-3396-b388-bd65412f5dc5 | -12.19229 | -44.71379 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10d8ad6a-244b-3ffd-b541-90cf37b911d1 | -11.68005 | -43.62709 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README33.md)
