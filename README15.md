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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 536efdb2-68e5-35a3-8ecd-e2e32d6b41ed | -15.0632 | -45.32648 | 2026-08-22 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 016c393b-262d-383b-8a8d-a6f93315f40c | -18.66075 | -43.17203 | 2026-08-22 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cad96f82-37db-3322-89a4-657511b08b20 | -10.2944 | -48.21435 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfde28cd-a9e1-3116-a1d4-f586b58db184 | -11.34929 | -46.35836 | 2026-08-22 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c091e170-a5ef-32b3-bdc7-650a9173eeb2 | -12.26117 | -43.13545 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69512339-53d1-391f-91a5-429a8b144a57 | -11.59682 | -46.54748 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 547b588c-e774-3b0f-9e03-8125e059cfc2 | -14.79756 | -44.23062 | 2026-08-22 03:45:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 085cbf78-9190-3d72-9706-0aebbb3d9fdd | -17.9205 | -44.41842 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96699640-1b50-3653-aca2-2830a2d17a1c | -12.72477 | -46.46375 | 2026-08-22 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51b98b4a-9e3e-3209-8baa-98da5e09ca34 | -15.0685 | -45.32767 | 2026-08-22 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 394662f6-985e-3eec-8570-c344f546769c | -12.76612 | -48.40565 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90b0e405-b74b-33ab-9814-19349bdb3c17 | -12.82453 | -48.45995 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2836a1c-2226-3d15-93c1-e8a2e692a42e | -13.4755 | -44.04126 | 2026-08-22 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7427e117-9c16-3807-9481-c4b92279197f | -14.40103 | -43.79203 | 2026-08-22 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91074618-a70e-328b-b2b4-ac3bab51aa3f | -10.3004 | -48.21767 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15373565-29c8-36d3-8a2f-9b52db7be64c | -11.59587 | -46.55213 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e63d26fe-04ef-3991-ab5b-9496037e218f | -14.79814 | -44.22768 | 2026-08-22 03:45:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7347890e-b56f-3053-b447-aae4ed94f307 | -12.76813 | -48.3961 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 39436e74-5cc4-3219-a9b7-e6eed6b8cf25 | -17.55915 | -47.88412 | 2026-08-22 03:45:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a3fb7f7-866f-327f-a209-14c168bdf3a7 | -17.96932 | -44.37194 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 765838d6-ed8f-3e58-8f41-51d329e0320b | -16.48458 | -47.94712 | 2026-08-22 03:45:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6235a944-667e-3d4a-8ba4-443d68bae64e | -17.91686 | -44.4118 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52b870ae-348b-3f05-88c9-34167c64a8c7 | -14.72095 | -47.14462 | 2026-08-22 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 092c0501-103c-39f2-bb83-0e1fdfd60d4d | -11.94668 | -45.49408 | 2026-08-22 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2eba35c8-9537-37da-9ad0-130c7c590c91 | -15.52125 | -45.86098 | 2026-08-22 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfc9d775-bde0-3e75-b484-81a241f1dfb1 | -18.7274 | -42.22851 | 2026-08-22 03:45:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a2d124a4-641a-364f-8ee5-5d52b67b47ea | -11.44657 | -44.55307 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3232f40-e297-3f6c-928c-faeb8de3b622 | -15.51512 | -45.86305 | 2026-08-22 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb79d8fb-0e9a-3ca9-bfc9-67f30d337f98 | -15.44311 | -41.38824 | 2026-08-22 03:45:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2c81de7f-76fd-3914-b8f6-d0b4335ad4ee | -18.55783 | -43.30642 | 2026-08-22 03:45:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2a561c39-7784-3a2c-b217-f23fa55d8017 | -12.83021 | -48.46622 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 182719d8-bd3a-3f2a-9b74-282d578baa32 | -17.15545 | -39.51208 | 2026-08-22 03:45:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8ef27a39-3372-35f1-929d-e092d4b3649b | -18.87356 | -41.98764 | 2026-08-22 03:45:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 985e2e84-eef6-3d7b-a2c9-b5ee54f4bc08 | -12.82638 | -48.46349 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 20bc630d-a253-3bfa-9857-0e6b986474da | -10.29402 | -48.2138 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09660c55-0a54-3639-a399-f827ac92c8a8 | -17.69182 | -44.44754 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 745cc177-19f5-31da-97f6-2a0396337894 | -14.40168 | -43.79918 | 2026-08-22 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4058e2a5-4f08-3e29-a1ea-e0bda32ce187 | -12.25539 | -43.18068 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 22d6d1bd-1df0-3a16-8788-2d65b97c7d68 | -15.06581 | -45.32978 | 2026-08-22 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d9b4a01-0038-3baf-ac53-81a47090d126 | -15.0625 | -45.32997 | 2026-08-22 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a442b16b-9a87-3541-ae1b-0c973640e4e3 | -16.18996 | -43.12892 | 2026-08-22 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0c5f48b-c643-3f92-9b22-b06318c7e19d | -11.44922 | -44.53892 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ed0391e-b4be-380b-a646-f73fc54ed2b1 | -17.91552 | -44.39381 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48af0368-0b8e-3ac8-84d7-5896adc0c4e3 | -20.63238 | -47.45163 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 65f3f439-c678-3092-8be3-2b1fbd29d9a3 | -20.07819 | -44.22355 | 2026-08-22 03:47:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f494d538-339f-395d-b162-8ea086eaf688 | -20.46996 | -43.39996 | 2026-08-22 03:47:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7cddb4fb-85a8-31e5-aa3f-5077195f5b41 | -20.98208 | -47.35217 | 2026-08-22 03:47:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9564b0d-5c6c-3353-9929-43997c52f163 | -20.89 | -43.0343 | 2026-08-22 03:47:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a90d969-482c-3aaf-a195-38f195e4ae03 | -22.3025 | -42.42462 | 2026-08-22 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b1c3fed-d07b-31a3-9ad1-942405735fc8 | -21.75024 | -45.45303 | 2026-08-22 03:47:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5c7d488f-3dd3-3698-87f7-918dede34e27 | -22.01141 | -45.31804 | 2026-08-22 03:47:00 | NOAA-20 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c225942a-c683-3503-bab8-8746ea31b247 | -20.63424 | -47.4433 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 38.2 |
| e808c502-bdea-30be-83ab-8b5c8927e926 | -20.98285 | -47.34869 | 2026-08-22 03:47:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd578b9a-4a61-356d-88ce-200c3b06ea45 | -18.08333 | -46.94865 | 2026-08-22 03:47:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 83a8f7f6-48e4-33de-866b-d53a83e47a02 | -23.34987 | -46.1863 | 2026-08-22 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3082016a-9495-35dd-9452-19b0e4a01b35 | -19.74442 | -45.09935 | 2026-08-22 03:47:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d336cc10-6134-323e-8734-e13030e18dea | -20.62694 | -47.45032 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 32.7 |
| bab49307-57da-304f-87fc-39412979350f | -19.74327 | -45.10493 | 2026-08-22 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6b1da25-cacd-3aed-8f6b-5ea0378274c2 | -20.62789 | -47.44605 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5f4104d0-7ee3-3458-80df-86ed26b47b4e | -20.63333 | -47.44738 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 27.7 |
| bf23e26c-d647-3468-b4c7-00417c3d95e4 | -18.91822 | -43.59875 | 2026-08-22 03:47:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6fa1ce19-3168-36bf-9293-1a8a40eea9a5 | -22.30711 | -42.42171 | 2026-08-22 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2282efb4-8d43-36ac-ba45-e85a71407b30 | -21.59311 | -44.01117 | 2026-08-22 03:47:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0445e3fe-48cd-3a2c-bcd4-636f00a7bd4c | -18.52404 | -48.24957 | 2026-08-22 03:47:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 632eb6bc-5b1d-3c1b-b4b8-e82ea5127da2 | -21.59399 | -44.00679 | 2026-08-22 03:47:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 3dc337f5-8592-38d3-9bfb-6b3b18092ebe | -19.74921 | -45.10041 | 2026-08-22 03:47:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 354b118f-3f6b-3b06-9a94-641ffb34bbd7 | -21.06231 | -47.34743 | 2026-08-22 03:47:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1a4ae963-ddac-30bf-8fe1-0fe6f074ab99 | -21.59743 | -44.01217 | 2026-08-22 03:47:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f6f69760-9303-3db4-8755-54f43b198ddc | -19.6673 | -46.04378 | 2026-08-22 03:47:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 752be311-e74a-3ac2-a7e9-b289545f2486 | -18.91058 | -43.59882 | 2026-08-22 03:47:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c43041c6-1178-3569-bfa5-018fe3ea6375 | -18.9138 | -43.59779 | 2026-08-22 03:47:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a6eb1d98-34d5-3d5f-aa0b-bd3041e6ed49 | -19.66796 | -46.04064 | 2026-08-22 03:47:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1473481-bab2-3d79-9bff-ec04f2329430 | -22.30322 | -42.42094 | 2026-08-22 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6ad23761-7436-36f3-a3ef-711a035891ab | -20.07791 | -44.22984 | 2026-08-22 03:47:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54f21312-d994-34d1-a74d-2b3150cafa66 | -20.89078 | -43.03032 | 2026-08-22 03:47:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fbc3943-3c53-35bf-b68a-80506deb9e9e | -20.63513 | -47.43931 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 38.2 |
| a5476fb7-897a-3ba2-8706-311091416aa9 | -23.53138 | -47.31709 | 2026-08-22 03:47:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d507bc37-9a1d-33fc-99e2-7c2b4d6812bf | -21.06442 | -47.34529 | 2026-08-22 03:47:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2f25deb7-130c-3ff0-8f65-cef75c352fd2 | -23.52623 | -47.31609 | 2026-08-22 03:47:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bdee1e8d-d198-3d78-b79d-de8745f6e2bc | -23.34871 | -46.19174 | 2026-08-22 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0363747c-0f46-3bd6-adee-d2b7e7d0317f | -20.62971 | -47.43789 | 2026-08-22 03:47:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c62488b9-593e-37a9-a360-f402300abca3 | -19.63997 | -40.46513 | 2026-08-22 03:47:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d2ffc92-5e73-3644-856f-f0e6b6895976 | -23.82512 | -48.71844 | 2026-08-22 03:47:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bf13f4b-3c95-30df-b796-54eea3dcc865 | -21.51588 | -45.23938 | 2026-08-22 03:47:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 66175329-4350-3d78-adfe-d2059560437c | -22.00674 | -45.31706 | 2026-08-22 03:47:00 | NOAA-20 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ed79b33b-b865-3727-a013-3e8db57836e6 | -19.10664 | -42.17741 | 2026-08-22 03:47:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de053b92-2f03-34a5-bc3b-6097fdfe5ac2 | -20.20662 | -40.36638 | 2026-08-22 03:47:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 21e2b851-344d-30c0-ad9e-8877bd2a9cce | -21.60262 | -44.00875 | 2026-08-22 03:47:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cf196712-bdd8-3f60-90fc-b0b69662663c | -18.08417 | -46.94473 | 2026-08-22 03:47:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 972a3f5a-5e3e-3cb6-a28c-6ac5ecb901a9 | -21.59831 | -44.00776 | 2026-08-22 03:47:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3039ddcb-0de4-3144-a56d-7cbe4802a37e | -19.74807 | -45.10601 | 2026-08-22 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 408cc065-7be4-3f62-8b9b-2813462dff99 | -21.51727 | -45.23981 | 2026-08-22 03:47:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b1a8038-1ba0-3cd3-9a08-aa332c3792cd | -21.06312 | -47.34367 | 2026-08-22 03:47:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d63a3e6-3c2e-3442-8620-fc899a53b73f | -19.6475 | -46.03642 | 2026-08-22 03:47:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5739de16-5730-359c-ae98-87ed177ca427 | -20.07886 | -44.22517 | 2026-08-22 03:47:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb238e0d-d701-3484-82ee-b48cafb63f8a | -20.1229 | -41.55995 | 2026-08-22 03:47:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 141518ad-6778-36b0-931a-5a358b77f559 | -20.82905 | -45.41628 | 2026-08-22 03:47:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c825a9d-1a1a-3a84-bb26-c729da75792e | -23.82604 | -48.71439 | 2026-08-22 03:47:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f24b426-bc26-3688-8684-a868bf77e0fa | -19.54609 | -42.09532 | 2026-08-22 03:47:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 892c6408-5bd2-37ea-95e2-6c539af5eb4f | -18.52996 | -48.25108 | 2026-08-22 03:47:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README16.md)
