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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 227711db-beca-3dee-9d2c-03217ad9d3db | -6.9592 | -42.9994 | 2024-12-11 03:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| ea2acd16-0baa-3837-b3d6-81fc3caf28e2 | -2.9482 | -53.1206 | 2024-12-11 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b8a65165-9e38-3a3a-a7a3-f6b6881abe21 | -6.1178 | -42.5559 | 2024-12-11 03:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 06f5d86f-0772-3278-9fa2-f943da533ad1 | -6.12917 | -42.5401 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 60246480-e319-3d8b-8ff7-ec21b6ff06d1 | -6.90126 | -43.50811 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2e6e745c-4aca-34c5-b028-85130d9a17ba | -9.38398 | -36.00834 | 2024-12-11 03:40:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ce0e5d6f-22bd-322d-850d-1b6ddc2fc418 | -5.98057 | -44.60055 | 2024-12-11 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 415acc32-780c-3a88-84b3-d06e0835522f | -6.12655 | -42.55584 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 188352b9-fa27-3cee-9a3c-ca72aa619bb9 | -6.12375 | -42.54064 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| a2ad9dc0-bf25-3816-84b6-3d4794fd9be7 | -6.11986 | -42.53466 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11843079-3164-35e7-8232-6bad22c214ce | -7.26754 | -34.93428 | 2024-12-11 03:40:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4543b15-b142-3ffe-b243-4401230c745e | -6.12943 | -42.53632 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 35c24e32-36b9-3990-81b9-965a6b51d016 | -6.12077 | -42.5295 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e5848fbb-3ca8-3024-a854-d998bb48bf00 | -6.735 | -42.53165 | 2024-12-11 03:40:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 447fa0b9-8f99-3ca6-b463-d1a608fc62da | -6.66823 | -39.23764 | 2024-12-11 03:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 672969b5-2dc6-360e-b216-82734ba082d0 | -6.9494 | -42.99587 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 12d0f707-3e91-303c-b81f-6898211f1c55 | -5.29501 | -43.28298 | 2024-12-11 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9591b064-0341-31d6-b10b-dc13feca047d | -6.10063 | -44.04875 | 2024-12-11 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 032e4a3b-8258-3842-aef0-e5fe69cb2bfa | -7.31739 | -37.25467 | 2024-12-11 03:40:00 | NOAA-20 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c7350ed9-3f57-3e09-af67-262578f07b2b | -6.12524 | -42.53411 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| a9b538ba-c295-389a-b6b0-4f96826a16dd | -6.11599 | -42.52866 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0c7e07bd-4e76-3898-8cfc-f63f78c52478 | -6.93506 | -39.76873 | 2024-12-11 03:40:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a769edf8-77f1-388e-ba3f-13ac0f21f4ec | -7.86701 | -35.20296 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 59b9a735-a9ce-3096-9612-fb0518043a68 | -6.9582 | -43.00301 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b4e877f7-0ef5-3af1-ace9-435799424339 | -8.23376 | -35.0081 | 2024-12-11 03:40:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 25c6aa81-d28a-329f-8fb2-2bf1da76e15b | -6.89468 | -43.51611 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 7c1f4383-0433-3ba4-aebb-e498ccbedbcc | -6.90682 | -43.50601 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b310bb88-7c06-3c1e-a434-f2ba8bf0375b | -6.12046 | -42.53328 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f72a9c1d-a28e-330f-8b84-84edf747e6d5 | -6.83375 | -44.39078 | 2024-12-11 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a570597b-986e-3ead-b704-3ef3605c551b | -6.26221 | -43.56531 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93875e8c-acca-36cb-b930-7857c06d2cba | -6.12763 | -42.5466 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 97f9610c-eae1-3091-9fce-b624c73ebcae | -6.94845 | -43.00135 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 5b98704d-b6fd-390e-8052-f6f299e8339b | -6.91135 | -43.5099 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cf0b60e-dcff-3369-8ace-c421f5034d04 | -7.03837 | -39.75208 | 2024-12-11 03:40:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 70b15e3d-3e6d-375a-88a6-edecfc67a375 | -9.40629 | -36.65725 | 2024-12-11 03:40:00 | NOAA-20 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a944e8e-5705-3545-bc7b-490367351960 | -10.50941 | -44.93366 | 2024-12-11 03:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a081f14d-6af1-35d8-a754-36dc195b3796 | -6.26276 | -43.56221 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f239843-e21e-3c1b-9bae-bdc1e66107f8 | -7.8825 | -35.14886 | 2024-12-11 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9801b8b3-d96e-3083-997c-6fa8deee4a11 | -6.26027 | -43.56181 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07fded9d-3bfe-3378-9c64-4dbd879ab819 | -6.96402 | -42.99838 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 189ccccc-d0bc-31c5-b731-df4104ed5c76 | -9.59227 | -36.40834 | 2024-12-11 03:40:00 | NOAA-20 | TANQUE D'ARCA | ALAGOAS | Brasil | 2709004 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56d77a76-4d46-33b2-9673-875eb19002b7 | -6.24332 | -35.18358 | 2024-12-11 03:40:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ce903756-0bb7-335f-aa52-55f025d84d07 | -8.28401 | -35.29396 | 2024-12-11 03:40:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 85b53e83-d0f2-3a61-a18d-f55b4f2be51f | -6.93656 | -43.53757 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e1c6976-4cf6-3d3b-903d-e754b3d7974d | -6.12191 | -42.55113 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 9502178f-a7ae-3bd7-996f-edbbd2fffacb | -8.03716 | -38.18531 | 2024-12-11 03:40:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b904c15-5eb8-3c9e-9864-895e3cb0c1f4 | -6.37428 | -37.80419 | 2024-12-11 03:40:00 | NOAA-20 | BREJO DOS SANTOS | PARAÍBA | Brasil | 2502904 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| da638919-7ade-3369-adcf-bd21cc9961a2 | -6.11895 | -42.53984 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e715f9e-1926-3afd-a795-74757a633c7b | -7.78545 | -35.22562 | 2024-12-11 03:40:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7a8d51ff-8270-3023-9ff4-88ea487bb3b0 | -5.97994 | -44.6042 | 2024-12-11 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 12d2a469-8bc4-319c-9714-1ecccf4b9c91 | -7.78491 | -35.22908 | 2024-12-11 03:40:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54e9cbfe-3296-3b2b-a20a-c41337f18019 | -11.54956 | -39.23722 | 2024-12-11 03:40:00 | NOAA-20 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3f3e669-6ac4-3851-be23-dc6d412a2186 | -6.90074 | -43.51112 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| eeeb705d-3cf4-3dab-8797-6382696242bd | -6.24663 | -35.1841 | 2024-12-11 03:40:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 435ddc75-1875-3f8f-b27d-c62f8c5a2db9 | -6.8957 | -43.51022 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 60e6a72e-6547-3cbf-8780-e41a60099b4c | -5.85359 | -42.42598 | 2024-12-11 03:40:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ebc8075-7a1c-3487-a216-6c2a5c6ef688 | -6.89366 | -43.52198 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ea21a6c-e740-309a-900b-5af76fe392c8 | -9.59891 | -36.40942 | 2024-12-11 03:40:00 | NOAA-20 | TANQUE D'ARCA | ALAGOAS | Brasil | 2709004 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4b25b488-f5c4-357c-bc85-4ceca222d033 | -7.47459 | -35.19452 | 2024-12-11 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a00b74c-2c34-32be-9c66-f5b5af7187f2 | -7.54054 | -34.83869 | 2024-12-11 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c2fc9cbe-96b5-35bc-9dcb-d09f742e845d | -6.89973 | -43.517 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cd5b65a0-ff3c-3a32-9465-0cb8a3afd879 | -6.91033 | -43.51584 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87efa740-20f0-3382-a5d1-dfaba16c7fe5 | -6.90427 | -43.52084 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 85f24c4f-1054-3789-9e3d-b8029c2d3b9e | -9.94092 | -36.30991 | 2024-12-11 03:40:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2c91d1c1-ce70-3edb-bf3c-56cd0d70289b | -9.57559 | -36.04303 | 2024-12-11 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 275fcda7-df9e-350f-adec-374aea786734 | -6.499 | -39.01427 | 2024-12-11 03:40:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 942ae7ca-62a3-3213-8755-3b247c2d54cf | -9.38785 | -36.00539 | 2024-12-11 03:40:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7937369a-b3a8-3e11-8a61-cd84b2112b5c | -6.26486 | -43.56579 | 2024-12-11 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 088fcea0-3c0d-3128-a49d-ad7b04570f07 | -7.14723 | -40.26386 | 2024-12-11 03:40:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1384ec57-1bb7-3410-941e-9492da4003ee | -8.94328 | -35.68069 | 2024-12-11 03:40:00 | NOAA-20 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 478f060e-4668-3b5a-868f-a70fc51f9068 | -9.78002 | -43.99652 | 2024-12-11 03:40:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72978a8a-7724-3a4c-a2e0-42dadb62410d | -6.12831 | -42.54525 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 960999c5-3f4e-3d22-9340-8a35e5ca6588 | -4.7907 | -39.93511 | 2024-12-11 03:40:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91095cf3-80b4-3581-9d9d-3909999cd432 | -6.96497 | -42.99292 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| b3880707-bfbd-3d0e-8886-26bbdce87800 | -6.68788 | -39.06892 | 2024-12-11 03:40:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4aa96c9b-a825-3824-8f3b-3abf39061078 | -6.96308 | -43.00382 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 64139e74-b115-3d87-98ee-99da56131473 | -6.95428 | -42.99672 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9bba7bce-2b3e-3dbb-925a-a4877e754c18 | -7.15126 | -40.26456 | 2024-12-11 03:40:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6ef36a0a-f685-3332-a665-858f8ba14bfa | -9.38453 | -36.00486 | 2024-12-11 03:40:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8d112bd6-1380-3296-add9-8afe0dcdafca | -7.52954 | -35.10374 | 2024-12-11 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e78ffad5-654a-3544-8f05-5ea10b30980d | -7.37241 | -35.19576 | 2024-12-11 03:40:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1b6d6bc-38eb-3338-9df7-43069a06a1bb | -7.87819 | -38.04871 | 2024-12-11 03:40:00 | NOAA-20 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f79d8c27-c96e-38fe-aaf7-cbdc21ee0757 | -6.12438 | -42.53928 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 07df1475-c7e5-3c26-a19f-2722c6cf963c | -6.11872 | -42.54369 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fa101b3b-63a7-3cbb-94f9-637effa0a359 | -6.0739 | -42.63353 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0cbabb13-ad12-3216-8d49-f425a359ad86 | -6.93204 | -43.53365 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb5273a-5675-3290-a0d5-cda260ebe1d9 | -7.67591 | -35.08041 | 2024-12-11 03:40:00 | NOAA-20 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 01ab4b74-dfa8-322c-9595-b8f3e4305e91 | -5.88033 | -40.15228 | 2024-12-11 03:40:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 92a8599c-48d7-3103-8c2a-b4fef183b375 | -6.38021 | -39.93552 | 2024-12-11 03:40:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6d882de-2793-3a3f-8648-a5f15c5de44a | -6.90477 | -43.51791 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e35c5e43-8c89-3215-82d5-319b37ec72e5 | -12.11994 | -39.39782 | 2024-12-11 03:40:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 51ebb141-d2f0-39e1-9fe4-63a3236a1469 | -6.12175 | -42.55504 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e5cbf6e2-fb84-3bf3-b542-5c541a21b025 | -6.12555 | -42.53033 | 2024-12-11 03:40:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 63e338bc-1059-310a-9bfc-17e7c6f9f83a | -6.90023 | -43.51408 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bd524396-44a6-32f3-8dec-9cbdf263e2bc | -6.90579 | -43.51201 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0bbdb0ab-61ba-3d78-a32a-770bf80d73fe | -9.77327 | -36.1247 | 2024-12-11 03:40:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79b5ac7e-0b24-3bbf-b5ff-16ec5c5f9a5a | -6.91084 | -43.51288 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba9d463d-1514-3fdf-bf3f-4b7380c1d079 | -6.96009 | -42.99212 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| b23c164b-25d4-323a-95dd-c9a1b889c8fe | -8.32186 | -35.1186 | 2024-12-11 03:40:00 | NOAA-20 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7351ea42-9319-33ba-bc75-08d9e97f2bdb | -5.07097 | -37.71591 | 2024-12-11 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
