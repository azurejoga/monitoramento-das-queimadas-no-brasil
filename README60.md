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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a920dc-9b7d-370d-b4e0-b669057d0bbe | -6.91073 | -40.57777 | 2024-10-02 03:51:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aeb3bcc7-09e3-37e4-a17c-e0f0d756db1d | -5.9054 | -35.43322 | 2024-10-02 03:51:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b581dded-03d8-359a-a8c5-ef063c55f38a | -5.9048 | -35.4372 | 2024-10-02 03:51:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27764d1d-fcc2-3a70-9d9b-6694d1fd53bf | -6.18213 | -35.25572 | 2024-10-02 03:51:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 68ec4979-cb19-3935-a68c-6057cd27deff | -6.1815 | -35.25982 | 2024-10-02 03:51:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f41ac8ce-e9f8-3cc7-a6a4-59425baca77e | -6.17918 | -35.25113 | 2024-10-02 03:51:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bd2a6eee-ab4b-3542-aa22-0d9c1c99b57e | -6.17855 | -35.2552 | 2024-10-02 03:51:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3d78cdd4-27f0-39bf-b98a-cd2685a855ef | -6.17793 | -35.25928 | 2024-10-02 03:51:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fcd717af-5618-3581-83ea-aa11d9d24d06 | -8.16789 | -35.40303 | 2024-10-02 03:51:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 717a02cb-0c5d-3c32-9141-1af32fde4781 | -6.13527 | -37.22393 | 2024-10-02 03:51:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01c448a6-1ca8-32d0-8a29-459fd58107bd | -7.01702 | -37.27369 | 2024-10-02 03:51:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1fc81fc-2993-3075-9f81-d249e4e05eef | -5.07057 | -37.71681 | 2024-10-02 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 965e6d8d-9502-3cf0-96b0-9dd886e6f3db | -4.92573 | -37.38299 | 2024-10-02 03:51:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7695ee3b-fa4d-335f-a9d1-2ca96965f927 | -4.02113 | -38.31847 | 2024-10-02 03:51:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62da4150-925d-34b1-8611-e1d2f06fe590 | -5.20377 | -37.62449 | 2024-10-02 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f7bea86-0c19-3259-9a8e-f3a17e94d69a | -5.20323 | -37.62794 | 2024-10-02 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ea244d54-2eae-3aa5-aaf5-af82a6c4d767 | -5.16669 | -38.14143 | 2024-10-02 03:51:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a939ecb-aea2-3768-920e-c60aa45dac15 | -7.21867 | -39.00221 | 2024-10-02 03:51:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1438bd2-8b34-3889-b5f1-20798295f996 | -7.1833 | -38.92523 | 2024-10-02 03:51:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 81a066e3-17b5-3a12-88b0-db7d435e489e | -7.17998 | -38.92471 | 2024-10-02 03:51:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 539f021d-b8c1-3e0b-8de3-91284f978163 | -4.69994 | -40.02035 | 2024-10-02 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f99230f2-02c0-3634-921c-0dff2348e637 | -4.69931 | -40.02425 | 2024-10-02 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cd35ea08-ced1-3d86-a82f-ccfa6ad052b5 | -4.30326 | -39.28 | 2024-10-02 03:51:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7cd6e78-cccf-34a1-956e-7da5e69d194c | -7.46232 | -39.22289 | 2024-10-02 03:51:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ba6f518-a234-3574-b6af-c5d13ccdd9e4 | -7.1771 | -39.39404 | 2024-10-02 03:51:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b741e3d5-176d-30c1-bfe3-d2a4f3cb7187 | -7.09173 | -39.26867 | 2024-10-02 03:51:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 12e76b37-d54f-300e-afbc-bb00b6f217e3 | -7.07625 | -39.15118 | 2024-10-02 03:51:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bf75941b-3dfd-30d8-939f-04ddbd7e6ef5 | -7.07292 | -39.15066 | 2024-10-02 03:51:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b92cd240-4df1-3783-9439-e01c6e8d4d1e | -6.62062 | -39.59682 | 2024-10-02 03:51:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bdb0221c-42e9-340a-a82b-8e04eedb2d5e | -7.69197 | -40.49948 | 2024-10-02 03:51:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7057a338-55bb-334c-b9c6-39f2421293ba | -7.95548 | -40.79695 | 2024-10-02 03:51:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f1de7a0-2f6a-3a05-aedb-32b3a0c2b2ef | -3.86261 | -40.78294 | 2024-10-02 03:51:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9577c34-bcbf-3109-bfbd-83513b5632ce | -3.85901 | -40.78237 | 2024-10-02 03:51:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91c556f8-962d-306e-bbf9-49f76b1028c0 | -5.6517 | -41.25681 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45a9e4f2-35bd-3b8c-84c4-f2915a3800ae | -5.60295 | -41.37372 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 17bcd4dd-c514-38fc-b6c0-d46ccf896ea5 | -6.48093 | -41.38979 | 2024-10-02 03:51:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f1934868-0fff-3eb8-b6c2-29d8b2e9ecfe | -6.25485 | -41.85096 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee0ee61c-90e2-38fb-bec6-aad12fdf47a6 | -6.25411 | -41.85538 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c7e3a65-f97c-3ca6-8056-2d53a2e36de0 | -6.2524 | -41.85256 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 45fcd744-8388-3dca-8238-7a4a629a88db | -6.25169 | -41.85699 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3749fca1-d362-3bbb-8b1b-da4d93edefed | -6.25041 | -41.85479 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d3340c0-b3e2-312a-aa61-4a0dadcf65d1 | -6.24799 | -41.8564 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13dc0812-a426-341a-9e29-7ec9db426302 | -6.24597 | -41.85863 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 720cda85-4575-3abc-b291-3fd7907abcee | -6.24429 | -41.85581 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c81fc9f1-e317-3e02-92d1-2c005cacea98 | -6.24226 | -41.85804 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8bdef98c-0553-3bc9-9194-3839390e3e11 | -6.24058 | -41.85522 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eadbd086-1cd1-360f-a8b1-803120d88383 | -6.23987 | -41.85966 | 2024-10-02 03:51:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9bd9102f-3e53-3036-bd7d-5bc44930c74d | -7.2712 | -42.05696 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b090f410-c6da-38c7-8784-25717c7db4c8 | -6.91418 | -40.57835 | 2024-10-02 03:51:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af3abdb3-b6e5-3ee1-8f6a-f9787d4f6f25 | -6.84772 | -41.82744 | 2024-10-02 03:51:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53847f77-02b8-34c1-a539-b67a0c3de493 | -6.45464 | -41.95676 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e01450a-e718-314e-98c4-34d1a31c03ae | -4.85575 | -42.78886 | 2024-10-02 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89b2604d-8647-38a6-86fb-4452cd5eb85c | -4.85518 | -42.79234 | 2024-10-02 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f64d42b0-bff2-306d-bc21-108c09e78e7d | -4.85062 | -42.79515 | 2024-10-02 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7282c8c-5be5-30a7-961b-9d0f57ee833b | -4.84663 | -42.79446 | 2024-10-02 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa5420fb-1d23-3587-91a7-34fc548a9822 | -4.84607 | -42.7979 | 2024-10-02 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 79f8a17e-98e6-344d-a5a3-26052c03392b | -4.46399 | -42.89092 | 2024-10-02 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| befb8e16-6278-31a4-90ff-d2da86047bdd | -4.45995 | -42.89028 | 2024-10-02 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b72ead21-37da-3cb5-aef3-50f564449244 | -4.45936 | -42.89381 | 2024-10-02 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c3470e-5eb1-33fd-ab4d-c152be7cfbaa | -5.9579 | -43.2678 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9598c3f0-5e74-3e1b-9ebe-095fb1242117 | -5.95386 | -43.26707 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b947ead5-1a0e-3091-92aa-d2f520487a6f | -5.95327 | -43.27063 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9a6c4dd-3840-3582-bdfa-5c547ac6509e | -5.94922 | -43.26998 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b92cfc4-de53-34cd-b0d4-122098109895 | -5.53376 | -42.77243 | 2024-10-02 03:51:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 66b0f86d-bc5b-356d-9922-d0cc07fbb755 | -5.96414 | -43.43246 | 2024-10-02 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c9c5ffb-7dbf-3986-b92e-5c80178bec4a | -5.87375 | -43.42462 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac71943d-a33c-3f10-82fb-6091baafac9e | -5.86497 | -43.42685 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b510c5e1-5b8f-31c8-88c0-595bfb7c2e09 | -5.64516 | -43.36798 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3e8eb99-da3e-3adb-8f56-cbe962a945b5 | -5.64046 | -43.37095 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef143ee-611a-3738-b9b4-34461d4d5d50 | -5.63865 | -43.38194 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22ed89b7-ec4a-3647-a76b-434ee54821df | -5.63576 | -43.37396 | 2024-10-02 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86cd5459-757b-34e2-95ad-a3b1649070b3 | -6.21431 | -43.20486 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9aa1a45d-4add-3fdd-971c-e2ced0c59c65 | -6.21029 | -43.20421 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 94a4ac8d-b76b-3304-87b1-09ebf1205e64 | -6.20969 | -43.20782 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3d7f864e-6c9f-30e2-ab5d-0d2692b6207e | -6.16002 | -42.89887 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8e8a0897-31c3-3dd9-b94a-2b259f9361f8 | -6.15922 | -42.90376 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2e7986d1-139d-3bc6-9fb5-6160691bdd2c | -6.15523 | -42.90337 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a8dcdda5-a0f7-3dba-8170-d1035570f067 | -6.15436 | -42.90875 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ea2808b4-cc4f-34b6-989c-662b47b697ed | -6.15037 | -42.90833 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c69f71fd-070a-3472-981e-c661242ae36c | -6.14639 | -42.90789 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bdf8fff7-171f-3738-903b-09e9c168957a | -6.30724 | -43.02654 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01576d00-9033-3490-b3c0-305e87a5aeb8 | -6.30329 | -43.02579 | 2024-10-02 03:51:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a6985c5-599c-3843-bc02-6cbe2b3f4d7e | -6.18559 | -43.43005 | 2024-10-02 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f0940ef-89e2-36d4-b7e0-fdd6ee1858a2 | -7.6493 | -42.44822 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07708d68-df38-33ec-8c97-96b54a2a0986 | -7.6478 | -42.43388 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89569d16-9c3b-3b3d-ba40-4fcad27d0c7b | -7.65306 | -42.44883 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8f159b65-de7e-3537-8138-85d6c090ee59 | -7.64479 | -42.45221 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5aa7aaeb-3a8e-3aef-a2e6-15c36d8d445e | -7.64102 | -42.45162 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f66da7bf-9ba7-3149-ba57-8419b1928e77 | -7.63651 | -42.4556 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d1634bb0-17da-39aa-8e69-19b0f31e677b | -7.63275 | -42.45498 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 53a37fe7-e186-3227-a511-4391a55784c4 | -7.45177 | -42.51628 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d2054485-155c-3702-b743-38b779dc6b0e | -7.32555 | -43.33152 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77da1aaa-d77d-3635-a1ba-0b3dbeebe757 | -7.64404 | -42.43326 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39566a40-e2df-3ed6-8d58-b81700e29144 | -7.64027 | -42.45621 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9017a3e7-296d-344a-9e58-b358f94520d7 | -7.6335 | -42.45041 | 2024-10-02 03:51:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ec839d6a-9123-3bf8-aba5-e87c42205d3a | -7.45256 | -42.51161 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 39c720c0-c82b-387c-ba3a-939cda952d7d | -6.65651 | -42.09575 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03386e64-10c1-3ceb-8b18-4fb6b342aed8 | -6.65572 | -42.10048 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b092ac78-f970-35d8-b121-dfff161733c1 | -6.63932 | -42.10683 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f21aee6-a040-3dfa-885a-28fb0e06e0c0 | -6.63783 | -42.10866 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README61.md)
