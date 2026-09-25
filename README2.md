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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b473257-4431-32b9-ac80-0187b2e8f169 | -5.1944 | -45.373699 | 2026-09-25 00:18:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30692f71-b197-3302-b0c5-7f998dafa3b1 | -2.8646 | -49.627998 | 2026-09-25 00:18:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0140bca7-13f1-3ae1-b384-61bafe9037e2 | -12.0626 | -50.2897 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e21287c3-e3a4-3377-86aa-4227fa1a62d1 | -8.3242 | -44.138599 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ee6ec5b-e186-3e39-898c-d62c91948449 | -7.6066 | -46.4576 | 2026-09-25 00:18:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df7a7d6a-1348-3db4-ab0b-bec97b65be43 | -9.6327 | -43.9599 | 2026-09-25 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd00193a-2eb7-348a-b008-07d6c6fecb7c | -11.295 | -51.310902 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92afbfbf-b116-3818-91a7-e636066e89ec | -9.6228 | -43.962101 | 2026-09-25 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c30a299d-2ee7-37d3-be41-26ebb4563a6e | -7.3454 | -42.061798 | 2026-09-25 00:18:00 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd843578-64e5-33bb-9e9b-8ab5609551b7 | -5.7925 | -43.9245 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8010c9e5-a9f1-311b-9a0c-56620ef8f29d | -5.3574 | -45.001701 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34e41d53-ca99-3359-88d3-69fc793c2989 | -11.948 | -50.7327 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75d1d3c9-1004-36b0-9bb4-29f843315432 | -5.1969 | -43.259399 | 2026-09-25 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9653d566-30c1-32d1-8017-4c92003bcb90 | -5.8209 | -47.757 | 2026-09-25 00:18:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 557d5604-e9d1-3946-b070-abe94468609e | -5.3769 | -45.999901 | 2026-09-25 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2253869-ff7d-3a57-aa89-6b76c7750c51 | -8.2802 | -42.8078 | 2026-09-25 00:18:00 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7fb0c59b-4c5a-3165-824f-cdfd77329d00 | -4.4714 | -43.558998 | 2026-09-25 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb7746f2-bd77-3cb8-90a3-6b2c4958aca0 | -3.233 | -46.9403 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650ab459-8706-3f24-9d98-4ea2dee2ac49 | -8.5914 | -48.3484 | 2026-09-25 00:18:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59970e42-5339-38d6-b725-2e7a99adef4b | -7.3874 | -44.779999 | 2026-09-25 00:18:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77cb0749-e7c6-3231-bd95-0ce3b0c58496 | -0.9327 | -47.552898 | 2026-09-25 00:18:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29bbc6a7-ea65-3a85-b361-92f8cd2ba01c | -11.673 | -43.511101 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc39ec0-52f6-390c-8b29-b2706b2e676e | -11.9345 | -50.715599 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c81c20c-7ab4-31a9-a6e8-320dd06b493f | -5.7329 | -42.451 | 2026-09-25 00:18:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 302f3851-fe22-3d4b-995f-2fa42d69d9cd | -5.8785 | -43.804001 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18e2d63b-6290-3248-a17e-ce7e5bc0df2d | -11.9577 | -50.730801 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8699f242-4b13-3e8c-abad-5c97c880d8f3 | -16.627001 | -43.143501 | 2026-09-25 00:18:00 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78e2f453-54d2-3e2a-894d-ae79f798ce80 | -5.8188 | -47.747299 | 2026-09-25 00:18:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2f335a-00b2-3758-9b7b-5504f9db4015 | -5.7894 | -43.910801 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c735fe0-e2bf-3af2-a3cd-a79ad2d456c3 | -5.1868 | -47.674301 | 2026-09-25 00:18:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34efa350-ad4b-3926-a665-632d9226e605 | -3.627 | -42.759201 | 2026-09-25 00:18:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6675b7-a825-3b81-a8b0-b5c5b98e37bc | -5.3845 | -49.166599 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a633b408-b38b-33c5-85e0-c52083916392 | -5.3942 | -49.164398 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795f68f7-555a-39f7-9a5e-218c2c784022 | -11.6534 | -43.515499 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ca28306-e2a1-3b90-bdda-c5a87205ce78 | -8.3372 | -44.1507 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2156cb5-6280-3cf8-959c-5a8583fd7ec4 | -8.3258 | -44.145802 | 2026-09-25 00:18:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e67b4bc4-e294-3324-b5f9-17a041f0a1a5 | -5.6176 | -45.241402 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7042d90d-a948-3072-859e-9fc7f32b3e5e | -1.2029 | -46.753799 | 2026-09-25 00:18:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b45f2eb-8da1-3baa-9199-89a38106058d | -5.7693 | -45.092602 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05bca0c4-232a-3b7f-bbde-29ed1c1446f8 | -1.956 | -48.382801 | 2026-09-25 00:18:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6fb594d-9fbc-3946-9923-4e2a99876e5b | -5.5187 | -43.718899 | 2026-09-25 00:18:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8519ccbb-20ba-3bf2-9dfd-7c96da62f26b | -7.3857 | -44.772598 | 2026-09-25 00:18:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0236763-2b01-30f6-ac50-994d2b939462 | -11.3665 | -43.382301 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0a1cf99-a2c8-32ed-aa8b-ebb11e21aa67 | -16.6287 | -43.151299 | 2026-09-25 00:18:00 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f519f47e-de4b-3f39-81d7-4cd68447373a | -5.1286 | -44.312698 | 2026-09-25 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7558a298-b6a9-31f2-a85c-3ad27ba01d4b | -3.2312 | -46.932098 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f25683a3-dbd7-3377-a3c7-27d7ae537fd9 | 1.8787 | -50.6614 | 2026-09-25 00:18:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 349fdead-54d7-36d7-a6b5-05c875008643 | -5.616 | -45.2341 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59cf550b-3977-35cc-b382-97f98d96a22b | -2.1969 | -48.944801 | 2026-09-25 00:18:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9b8218-5ce7-3f36-8a24-009279cf448a | -11.6517 | -43.508202 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 193bb070-efef-3076-9620-1a1fe03e9ec2 | -4.3708 | -46.238098 | 2026-09-25 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a14f13b9-7835-3efe-85bf-b094446a1431 | -11.3697 | -43.396702 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01be394d-7a13-3dbc-a626-0842335ba42c | -11.3403 | -43.403301 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a56bac88-856c-3c96-b3a4-5127e4707a8a | -11.9351 | -38.300499 | 2026-09-25 00:18:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 652b97cd-679a-311e-aee5-2b21431f4e4a | -1.2046 | -54.554199 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3baa8d-da91-351c-b0b4-aa9b89d0935d | -3.9697 | -48.428699 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 946300e3-6699-3829-a5c4-daaaa4ffe0c7 | -11.4596 | -46.7449 | 2026-09-25 00:18:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 629e003d-80a4-3d62-a68b-e7be134aa287 | -4.5595 | -44.0779 | 2026-09-25 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9df3aa99-0bc0-3ed5-bd5d-0372997841cb | -8.5939 | -48.360001 | 2026-09-25 00:18:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f78fad37-cfdb-36e5-bee2-df37bf61e8fe | -11.6679 | -50.5937 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b425aee7-05b0-372b-a03c-bafe9cd8ab1d | -6.5358 | -47.186001 | 2026-09-25 00:18:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6b21cb7-dc70-3cae-92a0-3edb4c4b131e | -5.4701 | -45.090401 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7750683-c1b0-3967-95c0-709341614c66 | -11.9232 | -38.294102 | 2026-09-25 00:18:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef75f83b-7e7b-32b0-97e3-74dad9353a9b | -5.8769 | -43.797199 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7972774f-22d8-3856-8a0b-28a31c3f8761 | -5.1927 | -42.972401 | 2026-09-25 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 965f4869-aaf2-315c-8f9b-fddab825beaf | -11.6713 | -43.503799 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6af545d5-0ecc-314a-b747-dbfaa08e7962 | -5.245 | -41.238499 | 2026-09-25 00:18:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d51cdd7-ed02-3dc7-adf4-2f0019be6f32 | -21.0436 | -48.472599 | 2026-09-25 00:18:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f203b2c-465e-37d3-8581-401fa9b1d59e | -11.6485 | -50.5975 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12eed946-5498-3c7c-9eed-7792cb41a500 | -5.3752 | -45.9921 | 2026-09-25 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6c0dcdd-fcf7-3c33-ace3-a5f089277c71 | -11.7937 | -50.923 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af3aff82-83e8-3eec-8e23-0150d741cf71 | -3.2428 | -46.938099 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae9f623-da71-36b5-bf84-988560e36379 | -3.2579 | -49.188499 | 2026-09-25 00:18:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5931d673-d7e2-37dd-931e-eb1e2b23cf85 | -3.4143 | -39.2822 | 2026-09-25 00:18:00 | METOP-C | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c1670688-bd2d-3453-80a2-d03b81d12d6f | -1.2142 | -54.551998 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2873958-886c-3594-8b35-6d4f354f1ba6 | -14.7088 | -48.768398 | 2026-09-25 00:18:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfdf5353-02df-336a-b9ee-bae9fb97fb24 | -14.6961 | -48.755001 | 2026-09-25 00:18:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77f3154e-481d-3b8e-9691-fdeff84eb3a2 | -11.7041 | -43.4659 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bda45e2f-9f39-3149-8495-743e3b39da04 | -7.4115 | -39.043301 | 2026-09-25 00:18:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d458d326-ec4e-30aa-bc9a-0a419727afe5 | -3.7223 | -49.064098 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982cab7d-4814-39e6-88ff-6771cf7b0a2d | -11.3517 | -43.408298 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2f56647-d44d-3cd2-9041-ce018b18c14f | -9.0193 | -49.6446 | 2026-09-25 00:18:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1aabd923-e8f6-34f6-89b7-d798a93c800b | -4.561 | -44.084702 | 2026-09-25 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71eccc6b-bc54-391d-9aaa-c24610b81ed0 | -9.5766 | -40.336498 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a143679c-142d-32e2-a6da-6088a6700bdf | -11.3387 | -43.396099 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 865cb658-7285-3853-bd4c-fd0a5fed0f0e | -5.7726 | -45.107201 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa44c9e-4531-31e8-a48a-e0ebaa51e5ac | -5.1984 | -43.2663 | 2026-09-25 00:18:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed9cd7f7-b008-382a-9756-5d14a6c1e3f9 | -9.5784 | -40.344101 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc2eeed7-32a4-32b7-87f4-8fe713b0d01d | -11.6501 | -43.5009 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43f4d9e8-6606-3317-a98c-3b70e75bfb09 | -5.7812 | -43.919899 | 2026-09-25 00:18:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f363f27c-f94b-3fe3-9dd5-18223aaa669d | -5.3968 | -49.176201 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17b20f9-6d04-328c-8cb1-03c21c99f79d | -0.4992 | -49.1623 | 2026-09-25 00:18:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08c83f7e-e4c5-3bb8-83b5-66f9a9c55bab | -3.7633 | -43.395199 | 2026-09-25 00:18:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18a23316-d05c-3479-8d00-c8d37273bc32 | -7.5925 | -41.791401 | 2026-09-25 00:18:00 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2374f6e-fbb2-327c-99bc-61155130e577 | -12.0688 | -50.27 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 821dbe28-73c2-331f-8202-03fdc375007a | -4.0229 | -42.463501 | 2026-09-25 00:18:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 061e4670-b8e6-379d-b096-cd5a7e1ee25c | -5.4784 | -45.126701 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08f753df-7772-3489-9ac4-5ef7c8b71130 | -9.026 | -49.628201 | 2026-09-25 00:18:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89b3d1f8-2a79-3e66-95e5-7137cca9b088 | -5.1498 | -45.176601 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc926c64-2334-31ce-83d0-f66e3f16f262 | -5.1515 | -45.1838 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
