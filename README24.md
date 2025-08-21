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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef141773-2b5c-3cca-a3f8-881e39c982e8 | -6.68921 | -43.67155 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e14428-c4fb-3c1a-92ba-0e980d5c37c9 | -6.45707 | -53.38313 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50ff616d-4c27-39c9-a5cc-ec523e7c9ab7 | -6.03126 | -44.36151 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c01430a-95d1-37fb-b3c0-819b51df73bb | -13.01431 | -45.17463 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3fc4837a-bc90-3e59-866a-686cf13a68eb | -6.55937 | -42.99501 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1dcfded-3660-385f-81fc-f0a90effa081 | -6.58329 | -44.46733 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b41da2f4-2573-3ad6-b3f9-86644d5b985a | -6.01798 | -42.82426 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30099603-c94b-34cb-92b4-89d76e88a3b9 | -7.25854 | -43.68367 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f08f1f6f-b3a4-3046-8400-31a82b0fd242 | -6.2646 | -43.72591 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fcafcae-39b4-3b7f-8d93-3e426aec0665 | -7.94795 | -42.64296 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 083a7199-5b30-37b5-84fb-9ecdff974519 | -9.92481 | -48.68846 | 2025-08-21 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b6dc90-d9a8-319a-aa8f-3f3e153516c5 | -12.08114 | -47.91653 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00bad9f0-be76-372c-b738-25fe85e6dd68 | -6.21477 | -44.1358 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c2f6f3d-ecf1-38b5-8b1f-c99159acb49c | -7.55254 | -44.00709 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1129258b-a964-3c9a-87a0-23824a20b643 | -8.16128 | -47.35499 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c87655d-439e-3654-a897-4eacd38b28bf | -7.64603 | -45.2495 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75a43d2f-2ad7-3b3f-8886-7587eaaa899a | -9.83182 | -45.95698 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2a6d5aa-65a3-36e4-b291-684db9969fc8 | -7.02242 | -44.62975 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9210bf17-cdf6-3a1f-a32e-d2712f3e349d | -7.38997 | -45.98438 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69f25cb7-9e51-369f-a58f-1007873b2b27 | -7.03037 | -44.62365 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 9b0a24ac-782b-334e-ab9e-8026fc1768c3 | -6.27073 | -43.70882 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a49f7fa-4fec-3863-9567-6e3f8776531c | -10.72187 | -48.23613 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1acf247b-718c-3dec-9cd4-d351dcdb4203 | -5.4434 | -45.10411 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7476e51e-9b3c-340a-99a6-3b691fb0c451 | -8.84833 | -52.04736 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9994a2c-a5d5-3471-9e37-058546f03b35 | -7.79454 | -49.32475 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10ee1117-d10e-3388-95e8-2e7c66503af9 | -7.88754 | -46.72799 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a0809ac-6dca-3e4a-8fea-f151425dac33 | -8.14445 | -47.3454 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 342f9910-3255-3967-8ed0-7783b8e407f5 | -11.2962 | -44.93212 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 081d3ec4-bb58-3b4b-afe7-a9f0455b3de1 | -6.86345 | -44.42286 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2016ac7f-1355-3451-9258-f366207a7d84 | -12.08731 | -44.72631 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b42e6799-3d97-3d6b-9c76-ed68e49fbbff | -11.57576 | -47.00533 | 2025-08-21 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddb311be-b6c0-3b9c-9349-3c959f298da4 | -8.38535 | -44.60349 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4511732-87b5-379c-96cc-400e2ab9fad0 | -7.8517 | -45.18543 | 2025-08-21 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6297b44-02b8-37c8-8371-7486b8fcc3ae | -7.65905 | -45.24687 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c7d0b41-425a-3b34-bd21-ecdf1be0fc0d | -5.79 | -45.07874 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 237e5f7d-1191-3294-ba57-eb32b2095804 | -5.74514 | -42.75253 | 2025-08-21 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f71dd870-b0ea-3c48-b4b8-e29b9db0137d | -6.03118 | -44.3838 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c755cd0-aee7-3fa1-801d-ad964c6ac6ce | -5.99969 | -42.81073 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3edd1ff9-318e-31a3-8eb7-caff7ccc02d5 | -11.02121 | -44.59954 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea20964e-3026-33e5-a702-f3cfdad23253 | -12.223 | -45.42039 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60733d5e-aea4-325a-bfa6-7844fa59bb52 | -7.60649 | -44.38701 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e91c65-7b1e-3674-b432-49c2b613127d | -6.50565 | -43.44207 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a21c2d4-f6fe-32ce-9337-9d215f360931 | -6.66203 | -51.57226 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 377e6ce7-829c-3863-aab7-32abf9d1af25 | -7.95517 | -42.64048 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71812d2c-a25a-3ddc-9984-333407a4680f | -6.00246 | -42.81472 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3fb782e-b30e-3ec4-832f-c5b93fb391bc | -7.65843 | -45.25063 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16bfbcc4-95e4-37ab-878a-beb9dd38fafd | -7.63927 | -46.22234 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6fed91e-1d65-3965-ab1d-14b386316559 | -5.88973 | -46.5111 | 2025-08-21 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1a57572-81d8-34c5-b538-5f36f141ffcc | -11.11179 | -43.19346 | 2025-08-21 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73a702b1-45b2-3d3d-a4f3-4bc87797541a | -8.34249 | -47.50352 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef141ea-a94a-3cc7-ac67-39c4d1cb08dc | -6.94833 | -42.8645 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7f2515c5-a7f2-3e4b-9ea2-24562e5fe9fd | -13.01925 | -45.18646 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fe39b54-7b00-3c33-8565-732023f672fa | -7.65154 | -45.24955 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f1d4d54-3b0c-3559-8ae9-1ac081e6ee2d | -6.01391 | -44.44827 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa06e778-d9cf-3cc7-837d-3cd957ced994 | -5.54683 | -45.19937 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90686e3d-3cb5-392b-a0fd-be430fead4b9 | -7.65118 | -46.26209 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 510b1523-e4fd-33c2-a0ca-0c0e725b15b3 | -9.32038 | -48.93112 | 2025-08-21 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98fe67bf-c003-3b95-9e4a-2c94e9ba86fe | -13.01154 | -45.1705 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0dcf316f-7eb2-3517-9ffa-f1f9af07b4f5 | -9.91795 | -49.25087 | 2025-08-21 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9d39546-670f-3b9d-ae09-92e746840426 | -5.80153 | -44.76634 | 2025-08-21 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463fe485-3164-37e2-9c22-8f515eb2b289 | -6.49036 | -43.10854 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e99dd097-098d-3b3d-8818-a787cb648a9f | -5.95593 | -44.15377 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8f6b3e0-d000-342b-83db-957c46898e70 | -11.09222 | -44.81136 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f8918cd-62f2-32ed-9d24-3bafaf3302aa | -8.43121 | -49.57423 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37d19676-f893-300b-8bbf-183722b9f9ed | -6.01371 | -44.36251 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed63e440-9cbb-3920-9a42-be1dc6639711 | -6.12739 | -44.71861 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47ab0080-a8db-3f20-a280-91ab51a0fbf6 | -11.81663 | -44.25858 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7744b7e-4e02-33fa-ba6b-89a36c25f8f2 | -12.22139 | -45.409 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e95bc17c-a001-378d-8922-b24437d58aab | -7.85513 | -45.18599 | 2025-08-21 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 616ca7ea-ee8e-333a-a75f-2e0f6c2b79fa | -8.2856 | -47.28583 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f8fa740-cbff-3ccf-8f47-b95a7d1bf04f | -6.95347 | -44.16228 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82e74d64-d296-3fa0-bcdd-f6b0f4a69d5c | -11.43767 | -47.32059 | 2025-08-21 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a248581e-df49-36f0-b86b-5ebfa97cab1b | -6.43188 | -45.48445 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 738b18d7-6efe-30c0-998d-f3d75a0c3889 | -6.00301 | -42.81126 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 360d23ef-47eb-3e7c-83b8-5f8c79421c6c | -8.06964 | -43.6733 | 2025-08-21 04:17:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d0036b5-97a5-3c17-b9ef-4dd50d738ab1 | -7.95768 | -42.64066 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76833aba-933c-3cd7-9294-7ca5eb4a5198 | -5.68075 | -43.86522 | 2025-08-21 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bef9568-2924-37f3-a179-dc03a169aa0e | -12.20779 | -45.42903 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a7f9256-7bee-35b5-b602-589f0dca0818 | -7.25238 | -50.16219 | 2025-08-21 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61e6e073-40a5-3456-af79-53b2700f9078 | -12.08388 | -47.9103 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f53aeb-902d-384d-82c0-93feb5abc14b | -12.1866 | -47.21843 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fec433a3-1220-30d8-9ba1-371e44d3dc09 | -6.26905 | -43.71941 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9581c6a0-4300-35cc-91f6-897c3bcdc8d0 | -11.91225 | -44.87296 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 939c5894-c16c-36d4-ab47-1c0012e0bcdf | -7.14966 | -44.18218 | 2025-08-21 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 780335c2-6f5b-3b2d-abba-36e90e827a8e | -7.25798 | -43.68717 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3d2521e-e9ac-3f01-ae32-64ff39fc4b65 | -6.20403 | -43.56897 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b17b251-56f0-3b55-8ed9-a9d3510cc199 | -7.11919 | -44.65695 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 798ea350-ce18-3221-b7fe-7875a9cf2a76 | -6.77312 | -44.33117 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8fe64d0-a72d-386a-adbe-c862d31cb29f | -6.95442 | -42.86903 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df06664a-a8ab-3a17-ba46-19fe2090a161 | -6.45244 | -53.38023 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c32a9d94-79e7-3dad-b06e-8e9a2a591d9e | -6.95455 | -43.7464 | 2025-08-21 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 114ede99-ce99-3829-b870-8119220b751c | -5.85412 | -48.79647 | 2025-08-21 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ba61047-8809-34bf-8455-3dd48deb785f | -8.30777 | -49.02822 | 2025-08-21 04:17:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45724373-f257-3aeb-b70a-ab9d2293b766 | -6.74524 | -43.93691 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2803fc2e-6f72-3b45-99cd-918e0607ab11 | -7.01622 | -44.62502 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6bb55de-d572-3c4b-aad6-836139d2246d | -6.07151 | -44.10936 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa5a96ca-bafa-3b0b-9ba8-6aedecfda668 | -9.48938 | -40.28539 | 2025-08-21 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 63995861-81f5-308b-ac7c-545e8f461331 | -12.98519 | -45.20646 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6177f31f-46ee-322d-a8ca-1756d47793a6 | -6.28912 | -43.69416 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 475b75f9-83f3-3654-a7b2-d2c5b2cea5b3 | -11.81799 | -50.64787 | 2025-08-21 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
