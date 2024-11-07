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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5bd738-096b-36ea-9e50-9ad7c662ec70 | -9.26058 | -50.68705 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47810814-38cc-30b4-927c-c7a952bbe9f2 | -13.32481 | -43.28519 | 2024-11-07 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc6b17ce-bddc-3e0e-ba65-23fc8f5913c8 | -12.0618 | -51.21386 | 2024-11-07 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0c57c30-bfa5-381c-a4e8-03055bdde4a2 | -10.28643 | -44.27473 | 2024-11-07 04:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b791ecc-94fa-38ab-bd5f-68f35d5ab673 | -11.51415 | -43.27024 | 2024-11-07 04:21:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3ddd795-1f41-30da-8f60-a20176ee8679 | -9.10283 | -43.19125 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7257ece9-d060-3834-ace3-eab6b6d3d104 | -9.10247 | -50.63678 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e632944d-cbb9-3cf4-bf9d-2284328a21ab | -16.34879 | -43.69722 | 2024-11-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa086d9-a89b-3947-abee-06bed5fc0087 | -9.29804 | -43.12562 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1d6250a4-8e76-306a-8398-9edc11a4b4fd | -10.89769 | -50.8148 | 2024-11-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b883ca-dd55-3fcb-98d7-b0330a853cd1 | -10.07388 | -50.81702 | 2024-11-07 04:21:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c4aa5c-1de5-36ab-bea3-02ec4dccc941 | -15.22972 | -43.3303 | 2024-11-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88251225-6afa-3e40-bb61-b13606177577 | -8.29729 | -49.04431 | 2024-11-07 04:21:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c29d3659-d1b4-321c-8ea4-958cca3d8b75 | -10.24402 | -43.37424 | 2024-11-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a7ae26d-81d2-3812-a612-dbbf3152f59a | -10.13487 | -49.14354 | 2024-11-07 04:21:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de5ccf6e-d611-3441-b457-163450aeb5f3 | -9.9878 | -36.41406 | 2024-11-07 04:21:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b2859be4-1569-3038-b046-a2c701ed8546 | -16.19864 | -43.70828 | 2024-11-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761e43e2-b1f0-3852-b350-88057549bf11 | -12.27477 | -51.21807 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19fccfd9-f85b-3106-9596-11fc74a256ef | -9.74037 | -43.58085 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae70ef75-e86f-3976-a2fc-64d1a1fe5e2a | -14.9585 | -43.43071 | 2024-11-07 04:21:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4df3650b-3eee-3ef0-901b-74560137a52e | -9.73869 | -43.59204 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de83e3cb-adae-3cbb-a290-d3ae8f8582b3 | -10.51126 | -40.16803 | 2024-11-07 04:21:00 | NOAA-20 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 592a0c0e-29d6-3d24-83b2-a2cbd62266dc | -10.13119 | -49.1429 | 2024-11-07 04:21:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f13b9618-d8d1-3e9b-8739-45a04fe96629 | -14.01694 | -42.48857 | 2024-11-07 04:21:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fc3d17f3-cb64-3bba-9a57-7cc6964845d2 | -10.45036 | -42.5703 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c175ec08-714a-34e8-8ff9-b5c3311f8b94 | -11.05155 | -43.28921 | 2024-11-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 722bc12b-88f8-3d6f-9fd1-5445b3d8244d | -11.14028 | -42.73712 | 2024-11-07 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ab6745b2-475c-3a44-8df8-64c4cc14fb05 | -8.69104 | -47.96101 | 2024-11-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e298363-a27c-36ac-addc-5d484869b867 | -10.45319 | -44.89169 | 2024-11-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e71319c3-143a-3574-83cb-79d34d11ef1c | -12.20869 | -51.02612 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df986214-bcff-3e30-8f0e-13cc1e4cc2e3 | -8.38502 | -49.63815 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bed8c74d-ad4b-391a-b6e7-a7a4393ac492 | -12.21728 | -51.02406 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7348ba9f-a97b-36cb-9d83-0757f1a7019a | -11.51766 | -43.27079 | 2024-11-07 04:21:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b359613-47a2-3457-a91f-d4a5682f45d8 | -9.25994 | -50.69072 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f595e50f-3d5d-3ccf-85aa-c59f342b9fa4 | -10.0399 | -44.73239 | 2024-11-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4f8625-4dda-3b99-a3fb-9b6ee18937be | -13.64823 | -44.11335 | 2024-11-07 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b555b0f9-085c-3a0e-9c5d-d2ff0951d90e | -10.6395 | -44.13917 | 2024-11-07 04:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 968ea356-61a8-344d-9106-6afeb253dda9 | -9.74776 | -43.57817 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f08d0368-c58f-396f-ac31-9cc528843aa1 | -8.68462 | -47.95586 | 2024-11-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43dafc4f-5daf-3977-b958-67c4f2baf667 | -8.68398 | -47.95987 | 2024-11-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd1596e0-d6fb-3cb9-807a-691c3a1272cf | -9.15152 | -50.54348 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d47fdc42-7f69-3104-bba9-edc205f373f2 | -14.07516 | -44.144 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b77ea5e-9f22-30b5-b7ba-4cffc432b08c | -9.73981 | -43.58458 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d164b044-e969-3b68-a7cc-28428f62a2b4 | -8.38114 | -49.63749 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a225754f-b8b5-3354-8f47-fb68d63f6a14 | -9.30208 | -43.12231 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e06e9f70-5ea4-3bf5-8ac1-e61e9df2e9a5 | -10.37563 | -44.73449 | 2024-11-07 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9059e6e-1363-35b5-af14-64b467a44293 | -8.69468 | -47.96052 | 2024-11-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5300985c-012e-3d37-94ec-549813803337 | -13.71779 | -42.89441 | 2024-11-07 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd9c06dd-2a11-3714-a79e-15c53191478e | -14.10496 | -44.21962 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5fa08e9-f0f1-3f95-a6b2-15c2f4e3ce9b | -10.38714 | -42.46428 | 2024-11-07 04:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a14cfdf-e733-3482-a46b-b3a6df6eed6f | -10.45264 | -44.89523 | 2024-11-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1aa92ea8-134b-3620-a9ef-5cfdc50f7470 | -10.44516 | -44.39511 | 2024-11-07 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3f6439-fdf5-3e08-9015-b79c5f7b67f1 | -10.13478 | -49.14957 | 2024-11-07 04:21:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddbe3440-9c25-3e13-a342-b854c76fc3b4 | -10.13412 | -49.14791 | 2024-11-07 04:21:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72697fea-b7b9-30e2-9878-7e8cfc2c4f23 | -13.71839 | -42.89015 | 2024-11-07 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1846a4c5-b7a7-3e3b-9693-6956cea471d2 | -13.61468 | -43.29883 | 2024-11-07 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7132a045-51f6-32a4-bb75-460af6f87fd8 | -14.47542 | -43.36038 | 2024-11-07 04:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53d4a1fe-bb2c-348b-9865-39e676790199 | -13.37706 | -43.49297 | 2024-11-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a112b6b-3b78-3b4a-afff-a001d48dc248 | -9.74719 | -43.58191 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a790c2da-5fd6-3878-8e00-98ad679a96a2 | -9.15621 | -50.54057 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5151e60-2ca5-32a4-8f47-58c0a6aac266 | -14.07227 | -44.13956 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a37dddec-ab0e-345c-bfec-1b5f08a63636 | -15.13652 | -43.40641 | 2024-11-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ec0a0cd-e594-364e-bf59-30cf4f6aca2f | -16.21703 | -44.06928 | 2024-11-07 04:21:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b8c0631-05f2-3ac5-a9b6-368f5939c74c | -10.00998 | -48.83977 | 2024-11-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79f5795e-4e1e-3a2b-b234-ed159f9cde9a | -10.13182 | -49.14457 | 2024-11-07 04:21:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04d880c1-4a61-31fc-ae6f-e5e0eb665786 | -9.25584 | -50.69006 | 2024-11-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e479cd14-6c1c-3241-ba62-dd8c2e572147 | -9.14881 | -43.13895 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5800bde0-fbff-3384-99c3-2043929c9686 | -9.94096 | -48.96016 | 2024-11-07 04:21:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7c9730b-1bfe-3d49-b378-1856085d9b65 | -9.06606 | -43.08459 | 2024-11-07 04:21:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f278c163-3384-3604-82c2-81979bccfd4a | -12.27945 | -51.21521 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c95e2c6-ed48-3bf3-8960-2ca08dfec31f | -9.94081 | -48.96145 | 2024-11-07 04:21:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 224fd107-dce3-3b5e-ae51-c925453332b7 | -14.41083 | -43.18664 | 2024-11-07 04:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 202cf7f1-2fa2-305a-a23c-4649a5389bae | -15.61275 | -43.57557 | 2024-11-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f8a6550-5d48-340b-8426-7c50b271741b | -14.06261 | -43.5678 | 2024-11-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20244761-16a2-30e9-aec7-8b818ccb1ffb | -12.05712 | -51.2168 | 2024-11-07 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06d80eb7-eefe-3186-b764-17cc56a81976 | -9.74378 | -43.58138 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 553c3d2c-34f2-3947-8d68-1bc10bdcd349 | -12.05775 | -51.21316 | 2024-11-07 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f5a5d3-1ac3-396c-b4a0-a3dfe4bdd7de | -8.08099 | -49.34079 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f19367cc-3fa2-3b1e-b8b4-93d2a0e56a9f | -9.98737 | -36.41746 | 2024-11-07 04:21:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 65cc36ff-c14f-3aa0-84cc-0d497da10779 | -13.64938 | -44.11438 | 2024-11-07 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fc8aeb9-0b8c-3cca-882a-83889746efa7 | -9.59226 | -43.14542 | 2024-11-07 04:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e05cf014-08d0-3310-8504-c8d4363803c0 | -9.91672 | -48.57019 | 2024-11-07 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ea0c26f-0bcd-353e-8052-5b62072a41d5 | -10.8169 | -42.71085 | 2024-11-07 04:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c654a00-d2b3-3c0a-b55e-f83557d63b0f | -9.92099 | -48.56667 | 2024-11-07 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8a7c978-fe44-3a03-8eb2-8431bec190ea | -14.06822 | -44.14294 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc6ae31-1cae-3f9b-b890-179ab2741ae3 | -10.61057 | -44.92693 | 2024-11-07 04:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 787b716e-275d-3b27-bdfb-fc49b8ec67c6 | -12.22126 | -51.02479 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1452a18-2e7a-3ab7-8047-393f9d732883 | -14.1934 | -44.35575 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 01168ff6-8eb9-3fa4-b6c3-14572f34c15a | -9.14536 | -43.13842 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e4596ce-c42b-3989-8167-5d5b244001de | -12.05751 | -51.21553 | 2024-11-07 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe31c850-ca71-3b09-97e8-b5d9dee2c0e7 | -17.43192 | -43.65349 | 2024-11-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dcacfb7-1414-392a-a1f9-78397cd29c55 | -17.4362 | -43.64965 | 2024-11-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f8d18db-ffcf-3349-bb75-171d2333a995 | -17.43986 | -43.6503 | 2024-11-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16e5df41-7847-3dd0-afd7-641035bd36d7 | -20.60135 | -55.90375 | 2024-11-07 04:23:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c410163-91fd-3086-a70e-5514d987934f | -22.85519 | -42.98015 | 2024-11-07 04:23:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33cd91bb-d39f-309d-812f-a7e966a20ee6 | -22.9012 | -43.7524 | 2024-11-07 04:23:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fa6a8e50-6ad8-385e-b0a8-272bc1e4fcf5 | -17.43558 | -43.65412 | 2024-11-07 04:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2f7adc5-4b49-3374-a7b2-6074650e467d | -23.95838 | -54.05142 | 2024-11-07 04:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 60e4a56a-4562-34ab-9e07-f661fa0b71dc | -23.94763 | -54.0432 | 2024-11-07 04:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6319972-184e-3bce-9bc5-b09221d51860 | -23.95573 | -54.057 | 2024-11-07 04:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README39.md)
