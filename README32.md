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
| be231c54-b2b9-39aa-9c97-a70c17daf211 | -6.05519 | -41.93602 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72035d7a-ca32-3e14-8762-2c4e0bf783b1 | -4.65851 | -44.08344 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a1a658e-37f1-3df2-b6b6-1ecc503a9384 | -6.24837 | -45.38723 | 2025-10-16 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16df3fb5-8849-3b5f-8bc2-5f925c0a2c6a | -3.28621 | -40.89758 | 2025-10-16 03:47:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80dcca35-3c77-3b6b-9dd6-e236ecc9e0ec | -6.45436 | -41.82515 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe4fe9fa-29e4-383f-80d5-98f09b126fad | -10.51042 | -43.37024 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30a5867b-11d4-35d7-9947-386ae7028851 | -4.95992 | -45.10413 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ec7be5-9981-3e54-aef0-7dbefb06bcd0 | -6.39654 | -41.49656 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 14401d79-b0e2-3fbe-a5c8-a3988018736a | -10.12903 | -44.58406 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a077509-e845-3fd6-95e6-8fd4c53abafc | -10.05256 | -43.85877 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40125c2e-3a4e-3c53-bd93-17e89c0f85dd | -10.13164 | -44.56925 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67892b0b-65f4-329f-8a28-9966f76dc945 | -6.90186 | -38.2614 | 2025-10-16 03:47:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37d95039-e457-3b5e-8516-9e54620fa5ae | -10.18242 | -40.95129 | 2025-10-16 03:47:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8aae754-4716-3625-bc00-4db017b41917 | -4.66461 | -44.10717 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe5867e2-5d84-3143-9185-cbfb777c3ab3 | -6.03836 | -41.92176 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a491f35-6ec0-36ce-a6cb-94b24da9bc48 | -12.15487 | -45.01332 | 2025-10-16 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d49177f-bca2-3bc4-a194-1373efbfa3ed | -6.14119 | -41.777 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 54f99b6e-cd1d-3756-b8da-88fcd4f238f2 | -4.15396 | -46.79533 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2064872-8efa-3c9b-9edc-a51a7d11cf06 | -4.63992 | -43.13125 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe535c52-df37-3bf4-86d0-c791a38fece6 | -10.66278 | -45.3211 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24f1c87e-a391-3a36-a551-02836dc87e2f | -6.23367 | -41.54909 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3355b09d-6591-3104-9035-d4d8b916d4b1 | -6.3737 | -41.48563 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| db50f6d3-9ce5-335c-9745-e87120492668 | -5.47628 | -42.94428 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b9b5ffe-7f7f-3668-97e0-5f0a6aa8ab74 | -10.05135 | -43.84037 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f44776da-7d85-32c1-b38c-5d322ce2d9de | -10.66663 | -45.32736 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7514bc51-9db1-3e63-aab0-80ad2a8776d6 | -3.69711 | -38.82806 | 2025-10-16 03:47:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ce40035-0f6a-38d6-8148-6cd295b1eec5 | -11.54078 | -49.92963 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc7f8731-8636-33ae-941f-367d5e052b68 | -10.69999 | -44.42631 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 383ad282-ce9d-3116-aba9-aa121533bb37 | -3.85224 | -41.56416 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0227fdb0-223e-39c5-97e9-872f83aa61f5 | -6.04792 | -41.90388 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91ba19a5-7b6a-31e0-81e9-5783afb4d747 | -4.39313 | -43.38762 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae3fb6aa-c3c0-39a5-8bae-1a6d7bf10c27 | -6.25579 | -42.90057 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ddf8967e-7720-3d4c-a1ab-f43e5c091558 | -10.66186 | -45.29847 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6b70431-c39c-3975-a9c5-fe52932c3ae2 | -10.82515 | -43.94202 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b64c82d-ef38-3301-8e02-575a73cad343 | -4.15324 | -46.79942 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d800795-365a-3b47-9de2-79cfbbfa56bd | -4.41807 | -40.18303 | 2025-10-16 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddcca0fa-4902-3138-a34a-59910f4f5a8d | -6.26067 | -44.33904 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9878762-7bf5-3e1c-8517-90babc060eb9 | -12.64875 | -41.2738 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c65b6ac3-b8fe-3db4-8dd7-882f182c542c | -9.70911 | -44.49937 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00bd2171-894c-3c7b-a3a2-5b6528e76276 | -5.87758 | -42.81519 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ff231612-cd30-3baa-9642-392da5507752 | -5.5359 | -41.32678 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 18155e3d-f419-3c1e-8fad-697428088315 | -6.06795 | -41.91104 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6c63f44-5ed7-32d6-9613-ad2db6401ec5 | -11.47227 | -44.14392 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8193464-a719-3622-974d-4cd3016caa9b | -4.36653 | -43.39163 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 6b3dbbc3-09ee-3ebc-9334-86168558f81e | -12.22309 | -43.30608 | 2025-10-16 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b102d5a-1965-35af-9312-be67484df6a5 | -6.31879 | -42.76738 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4ecc91b-1c13-3f53-bd4c-8d26171d76fb | -8.81312 | -47.30763 | 2025-10-16 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d186da9-77f0-34e9-a251-2da8ea3d108b | -5.23554 | -42.00758 | 2025-10-16 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34194bc7-8743-38d7-9610-5cd92d770d8e | -10.66736 | -45.2916 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0f6581d-dfeb-3f84-bc0d-862b7fb6d5ef | -3.84485 | -41.58278 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ceb5e48-1800-31bc-8db5-0b1778731ddb | -10.14413 | -44.54734 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0022f076-5cc2-327d-bc0c-1f3fc40604aa | -6.15976 | -40.9118 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 76661a56-8114-3c72-b02e-47f8a1b806b2 | -11.2087 | -43.99797 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cab678c-fe45-3486-9762-68fd5dec0816 | -10.12421 | -44.55737 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1d5bf722-cef7-3ef0-bc8f-a01079228b23 | -5.87811 | -43.9015 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5122528-f3b4-345c-a7a0-2158805af5d5 | -5.23359 | -43.67564 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2a1f721-a529-3d4f-a6ba-2cda9e01222c | -6.22965 | -41.54838 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85a8eaf4-4059-3908-9b5e-98cf5ae356ae | -10.66344 | -45.31259 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b689087-692f-3d22-8108-ac213e91b9c8 | -4.75925 | -40.87156 | 2025-10-16 03:47:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef30a920-2b17-38f5-9aab-b812e02f21c0 | -10.13953 | -44.54647 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e4a2694-ab52-3011-acdf-3470af27f124 | -6.40123 | -42.55299 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42f1e0f8-8542-3f41-b0ef-e05b0e0dcb53 | -12.65307 | -41.27023 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d1c3e11-0d73-3df0-9dc5-d0c91536d12e | -6.70832 | -44.39523 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12453599-fcae-31f1-98f2-2c9d8d074fc7 | -15.57415 | -42.38081 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49aca467-b928-3506-a6cf-ffbc8bfa73f8 | -7.04653 | -43.9734 | 2025-10-16 03:49:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e2106d7-0e66-3092-a2ad-902b66371655 | -17.20528 | -42.20827 | 2025-10-16 03:49:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1c39da9-aa3e-3d9d-9478-d638fb85fa99 | -6.99252 | -42.79643 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66c7e12e-5f7b-33f0-a014-6eb32563a008 | -7.95802 | -44.14297 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cad8b28b-2ff7-308e-b31d-9264c55bf426 | -8.25328 | -44.10399 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adf01b48-4040-3fe8-8125-8e9d46d696a5 | -7.66777 | -42.37818 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 431c6eb5-a6d6-3b3b-b833-fe413f32b1dd | -6.4528 | -44.57835 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e00bd371-47c1-33ae-ac5a-2a84974adde5 | -7.39412 | -39.69129 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 34c4034d-8045-34ae-98a1-aaadc6a79b0c | -14.46915 | -43.82933 | 2025-10-16 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48eb27b5-d960-3cac-85ec-48424424f74e | -8.28981 | -44.9627 | 2025-10-16 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1da0977f-5ee7-3913-85b6-2984705cab8c | -8.45736 | -46.19441 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52298d9f-6f21-35c9-b897-02523614969f | -6.32594 | -46.32768 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efe2cec7-bb87-320c-b7fc-eb6d8a90edc0 | -8.19155 | -43.96946 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16d1a2a0-449e-3b8f-99da-dd764de66d30 | -7.39625 | -44.74977 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d562f025-916a-33db-861d-cde5f59371de | -7.39553 | -39.69859 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 08b3a5ee-8da7-3ec5-a74b-1a9d9fb30c0a | -7.28411 | -41.95467 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a8b8a2a-4481-36d7-a985-0ed778530562 | -7.75007 | -42.48269 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eee0c71e-25da-3fdc-a587-86a3a4fff076 | -7.4817 | -42.75862 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 38996b37-4669-3fcd-80b5-c061123a00ab | -8.25648 | -43.43073 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d48c3f00-0761-3e01-98f0-6b1ad3487253 | -8.22168 | -43.31789 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26983866-6968-3bb2-bbb5-79e7945e2524 | -8.19622 | -47.0204 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c2ff6baa-d114-3a79-94c2-257353ed83c5 | -7.94735 | -44.13409 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c949e16-34a4-3067-af8e-7a3800535cb5 | -7.92409 | -44.12989 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95ce4433-a049-3ced-83d9-e4c32b2bad47 | -8.27102 | -45.91407 | 2025-10-16 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 091bc8c9-2633-3cb8-a217-f40b60a99285 | -7.10254 | -41.5261 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cd324705-ec65-376b-a5e2-5b38bd9652f3 | -15.8857 | -43.46377 | 2025-10-16 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78ddeaae-c932-32d3-9472-ea4aa1b7effa | -6.95229 | -41.56563 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88ee8008-dce3-3518-983f-e64fa1af886b | -8.67455 | -40.91124 | 2025-10-16 03:49:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6985a2e-e039-3b48-9539-78c6cae3d4d3 | -8.27564 | -43.37188 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e817e46-1c18-3ac7-a955-e129395293e9 | -8.47148 | -44.1968 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f632f14-834b-3ead-a0ea-0290c8011bcc | -7.3584 | -41.91167 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d70ae914-a3e9-3560-80b3-2d37db3ec799 | -8.18697 | -43.96865 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81d6c1ea-3d59-3c61-8ecf-892a4f640491 | -7.11056 | -44.73026 | 2025-10-16 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a7fc386-aaaf-3823-9f15-268b946b8f20 | -7.39921 | -44.75044 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d29cfd1-dbbf-3986-a63e-aead038bb636 | -8.24195 | -44.03251 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3c0eac02-185f-31da-bbca-f68a10b25f28 | -7.61473 | -46.4784 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
