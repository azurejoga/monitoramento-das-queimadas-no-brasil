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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c706fb4-31ca-311b-82c2-636b428759ea | -11.90925 | -55.91926 | 2026-06-16 04:19:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bffe1e17-3a7a-3a66-91f3-992091c6694a | -12.91638 | -54.22721 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d209bca1-ae90-3cb5-a8a0-1972c4ce8d78 | -6.46723 | -46.89874 | 2026-06-16 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7137128f-a14d-3f64-8c2b-b16f4ab06ea6 | -15.18355 | -41.8084 | 2026-06-16 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49507589-d8f4-3bc9-af29-448f92233023 | -6.13637 | -48.52105 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0c0aaf-ab51-3c27-8337-b2e94bbdbe34 | -12.91724 | -54.22291 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cda7f04-0ab0-3b27-bd03-13d130aa353d | -10.80213 | -54.18106 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf9c34a2-3ac8-3e6e-a903-6b80b1aeda11 | -10.90528 | -54.1397 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8de9598-ae58-3851-9547-035d25d46ea6 | -12.90369 | -54.22923 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 620de01f-d636-3ef3-888b-55c345164031 | -11.58475 | -55.34563 | 2026-06-16 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 981098dc-f254-3dbf-8bd9-3058364dac0b | -10.89921 | -54.13845 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c7f1e0d-73c2-32c7-9a5b-c7b851e0ad1e | -5.80074 | -45.07047 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 72e673a2-a498-3115-b086-93d8d1627bde | -12.80028 | -54.86738 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c6509ca-4711-3db1-8372-912619657d21 | -7.71891 | -44.16974 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8250be5a-5ad2-3389-827a-27712796e5b3 | -12.59615 | -52.91857 | 2026-06-16 04:19:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b500cc3f-df47-3791-8b23-f4d437044c51 | -11.26815 | -53.96262 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea97e3b6-2f85-324c-8afe-7d0a6930f5fc | -12.15054 | -48.46088 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 656527f2-8f0a-375c-8a16-a8cc6a5c00f0 | -11.59231 | -55.34153 | 2026-06-16 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf14c4d-b165-3f7c-b558-e6c190bc14b5 | -14.8562 | -43.37272 | 2026-06-16 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 86c03dca-d41d-3936-b16e-6ffd94e9e087 | -16.63502 | -46.86255 | 2026-06-16 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9441baa7-3a00-3033-95f3-3e136bf93388 | -10.80307 | -54.17635 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 819a004d-59fc-3a4a-8664-b941e7af3584 | -11.718 | -54.49791 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7ff3e26-3f21-39ed-878e-27822f592547 | -6.0128 | -47.1084 | 2026-06-16 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08763632-7a3f-312a-be5d-b48dd89999e0 | -10.80406 | -54.1754 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eafc0589-dd00-32e1-8753-fb22e66e32bb | -10.71454 | -56.256 | 2026-06-16 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 544be722-a664-3f96-a8a6-2022002c313c | -11.54736 | -52.79864 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb0f70d5-f749-32d9-b926-52668906ff88 | -11.26415 | -53.95894 | 2026-06-16 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a4272a3-4e2a-3455-8667-45ab8cbe4aa7 | -6.13598 | -48.52335 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a788aebe-0106-34f8-9601-728611a43a51 | -6.14089 | -48.52213 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11170380-8909-3524-af67-cdbb8c87d69e | -6.18052 | -48.51029 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4e56740-a530-390e-a9cf-fbf8670cd3ff | -14.85344 | -43.36859 | 2026-06-16 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ad2e3ac3-e16b-38cc-ac5e-b3ad477a1ba1 | -6.1842 | -48.51624 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55e45200-777e-3736-bade-801787d86a88 | -10.90006 | -54.13577 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fda86f19-f8dc-3a08-9379-35795d0a9ef5 | -11.53845 | -52.78542 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aaa56885-1348-3a46-85e0-af7b32b4fe2d | -12.92314 | -54.22414 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a4fe94e-aefb-3894-a066-dd8f45a5719a | -11.55097 | -52.78006 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80ce59a0-dfeb-3eb4-bfa6-680845d319b5 | -13.56114 | -47.85648 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 978349bd-e6b7-3a3f-b08d-691af5ed4058 | -10.15118 | -56.60754 | 2026-06-16 04:19:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b74cc5cc-cbc6-3e9b-8fd6-35d647bd8959 | -6.3978 | -44.1747 | 2026-06-16 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 432c8574-2e46-31bf-80c9-761bd8ac12a3 | -11.47755 | -57.10997 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1dc5fd36-2fe2-3a7f-9d25-7fe51b379a31 | -12.90458 | -54.22478 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7fd988d-0c11-3a11-b09a-277553b4ec9c | -6.30487 | -43.64404 | 2026-06-16 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31adaddd-dba4-385b-975e-e55c8d3cff38 | -12.84521 | -44.37312 | 2026-06-16 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 46d0ed47-af58-3b9a-9c4c-912186927d6e | -6.30426 | -43.64777 | 2026-06-16 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c210f9c-f0e2-322c-9e92-458c3dca0675 | -11.4791 | -57.11122 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50a9ca1d-5315-3010-95b0-62c68aaa9bbc | -7.72143 | -44.16552 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed6e5b63-4689-32fd-905b-9c2ff0ba45ee | -14.8601 | -43.3697 | 2026-06-16 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bec071b4-b179-3065-a799-9098f383ab1c | -11.54473 | -52.78267 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 405fa840-cc78-3208-954b-0e5bdf9141b3 | -13.55424 | -47.85027 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0c77a79-47b8-3930-9da0-955ab0643e5f | -11.35536 | -51.40845 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8213bcf-0b3a-3c91-9819-6e61bfd9f95e | -6.54213 | -44.68736 | 2026-06-16 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55dd6390-ba27-3020-93a2-83be06d10986 | -18.96579 | -40.37251 | 2026-06-16 04:19:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccd375fe-0671-3364-9f25-9d6e19d6aaa1 | -11.55168 | -52.77639 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8655c41c-ad82-3d28-ae85-490c4b164244 | -13.56326 | -47.8672 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c31e5350-179d-3204-a28c-af28fbf7fbce | -11.54544 | -52.77896 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07c7424e-0804-3fbe-af22-e9514dd2f32d | -12.8548 | -44.3625 | 2026-06-16 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0e46d0f8-8f19-3813-96a4-2184bc30cc96 | -20.81986 | -45.17622 | 2026-06-16 04:21:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56a9ff54-b27b-3b59-b381-c4654dd8a835 | -12.8548 | -44.3625 | 2026-06-16 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 87d3ff31-3429-338d-973d-d9befb657a9c | -1.18163 | -50.52837 | 2026-06-16 04:34:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee841859-a1f7-34e3-b3e1-a03d56bd60f5 | -0.08661 | -51.28037 | 2026-06-16 04:34:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3154505-605d-3145-abf9-1684886b8677 | -7.72074 | -44.56854 | 2026-06-16 04:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88d22748-7517-3adc-842e-05c53e3acb78 | -4.35634 | -47.76364 | 2026-06-16 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2f4b9d83-0c2e-3c9d-8f24-376fdfbe3f59 | -8.94257 | -46.95604 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33e8d14d-6370-3942-9d22-16fc9e4020a5 | -7.72273 | -44.16096 | 2026-06-16 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef4030a6-248e-351c-bde0-16ee54ee63ff | -5.51862 | -37.48375 | 2026-06-16 04:36:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a9d0ea61-fa58-3c9e-92e1-5b39b6cc57ff | -4.35358 | -47.75967 | 2026-06-16 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d4c172d-2479-3ecf-9a6f-357274bbed4b | -6.13912 | -48.51927 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1ff2c58-669d-3df7-89c5-6a070762c170 | -7.36321 | -49.86746 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9308ea74-31ee-37cd-9bd6-37a783e2ad7d | -6.13801 | -48.52622 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf5130b6-8cc9-3ee2-a147-6dcfbcf2b12e | -5.80139 | -45.08565 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| babacdc3-926e-383c-b02d-63b963a902f4 | -5.79906 | -45.07726 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdaaf136-9074-3e8c-a65b-8b28feb1b620 | -6.46656 | -46.89949 | 2026-06-16 04:36:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e73447dc-e8d8-3c32-9521-d5d4ce019a3f | -7.71894 | -44.1604 | 2026-06-16 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e863f79f-fbe8-383e-873e-0270565c89d2 | -7.34886 | -46.21005 | 2026-06-16 04:36:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fcf8f79-7169-34fa-bfa9-bc33a152f37f | -5.58919 | -43.50556 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 447d1c03-aa14-3049-bd7c-856b6ffda180 | -5.3608 | -46.01821 | 2026-06-16 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31a90d1d-d950-388e-b71a-7287c710f879 | -5.80319 | -45.07381 | 2026-06-16 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f254c354-96fa-3247-83d1-945d9b4fa29d | -3.96249 | -43.11634 | 2026-06-16 04:36:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3dfc0fd9-e3ca-30d2-83ab-82c386b7f420 | -8.94538 | -46.96021 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ab07683-a290-3490-9356-051f590a0f4a | -6.97983 | -42.88655 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f7f3e7ee-78d5-37ca-8b3e-5de38f8e3fbb | -3.49695 | -48.03882 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f575ed9-c7e9-3483-a4c4-98f6d86ff8b6 | -6.97686 | -42.8787 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| de793ab3-9733-3d2c-90d2-be03efbcc9be | -5.83558 | -43.48846 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20f62435-9303-3aec-a91e-ed62f0a8b76b | -8.94933 | -46.9571 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 951762d3-ff39-3525-9d80-631191bdec70 | -6.98008 | -42.88681 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5e277166-4cef-3cfe-92b1-4da7fe4bf22e | -6.13746 | -48.5297 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 184e07db-e879-3236-9ce8-974e902fa027 | -5.58536 | -43.50502 | 2026-06-16 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a40aa8f0-7a4d-3aa2-b02f-798130742237 | -8.96342 | -46.93319 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67a6a2e0-058b-3c03-9c60-03c8685362fe | -8.71572 | -47.82393 | 2026-06-16 04:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0cf9e14-bf84-3a02-9b1f-96b353f75978 | -6.18115 | -48.51175 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10ff1fa7-7e96-3bd4-a8d2-597a6550e4c9 | -7.37239 | -49.8539 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05e1177c-73fa-39ab-bf0e-a0de13f1295d | -4.35304 | -47.76311 | 2026-06-16 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182e224e-08e8-3621-9033-7ed179d6f4f7 | -5.98483 | -47.06846 | 2026-06-16 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff5a75f0-88c9-31d8-ad89-01becbc545a2 | -6.30753 | -43.64752 | 2026-06-16 04:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77f5c5e4-5984-3a2b-9446-3598aad3d971 | -3.49418 | -48.03483 | 2026-06-16 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669edfb1-d5da-338d-af7e-9934708a4b1d | -7.27513 | -49.56935 | 2026-06-16 04:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e18a990-01bf-35a3-9426-7be05fd58c58 | -8.95383 | -46.95036 | 2026-06-16 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 415dca32-2d5b-340e-a92c-140ae38aec75 | -6.13581 | -48.51873 | 2026-06-16 04:36:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c91dbf73-9aa9-3b58-930d-7b5692dcf774 | -6.9774 | -42.87508 | 2026-06-16 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b30315c7-8cd2-3838-9f94-59787cf89156 | -4.48875 | -48.27805 | 2026-06-16 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README9.md)
