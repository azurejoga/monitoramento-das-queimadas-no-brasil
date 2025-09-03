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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5bf1f9b-9268-353d-8615-29034a395354 | -8.88931 | -45.79541 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4b21dbf-d6c7-378f-bac0-6611928dba04 | -11.82248 | -51.44923 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09fcae5e-fa60-3ff5-9eea-ce12aac70dc9 | -6.07938 | -46.81798 | 2025-09-03 04:46:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f3004e4-e65e-3f95-9979-df1d3eaac439 | -6.95802 | -42.97407 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15e50232-84ec-3868-bbd4-03de3acfa9fd | -10.4882 | -50.32874 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b440ffeb-2326-36de-a239-94348b87e9de | -11.59071 | -52.11411 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4488fd6d-ba9c-3623-89da-21fca475bdd5 | -6.9387 | -43.29723 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5737cfa4-a9e5-3bd5-92c5-0dc71b93602d | -8.34427 | -52.52998 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06b64d13-0cb4-30c3-9ed0-94e198e1baf8 | -6.17291 | -43.31893 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9134f17f-b057-3a4c-a677-24836557f676 | -11.80539 | -51.49404 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8024ada8-e8e6-3d7b-a148-114f4189174c | -7.25718 | -43.85227 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01b56001-25e6-3151-a5b2-98db975ba19d | -5.44208 | -42.84232 | 2025-09-03 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad03b3d9-e2d2-3de5-8181-187b0e94c942 | -8.06403 | -52.36583 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16741402-ee5d-30be-99ba-2d6db1185df0 | -10.44985 | -54.78586 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c35686-e866-37a4-beff-2b4f624db849 | -9.39381 | -48.05105 | 2025-09-03 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff0072d-d513-3e54-a55c-d759f695efdb | -8.14849 | -54.92921 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 212cc6f1-418b-3bdf-9d38-9384fb7a07f9 | -5.91497 | -57.73153 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a0d9bacf-704a-30bc-b1ca-3be880d99915 | -6.98163 | -43.09935 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea7c4752-703b-3f7d-b425-4b8ae038d51a | -11.60229 | -52.12673 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec756e91-e59d-350a-a956-2738e7a26736 | -3.53172 | -59.513 | 2025-09-03 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82b4ea6a-1c9e-3cc1-ae56-585e34b82a37 | -6.82539 | -52.81686 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77dce659-7676-3a41-8db1-335da992fce1 | -8.01954 | -50.0968 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ceb1e2e-cf41-3fe5-aab9-532e124ea36e | -5.92695 | -57.71489 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 791b4ce2-8a3b-3403-9560-d1024ccccd1b | -11.95208 | -45.77719 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b85ee7f2-538d-3cb1-81fd-4ed6a7f8f692 | -7.60092 | -46.22813 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7397d23b-0d75-3de5-af96-aceb166e2bd3 | -9.13911 | -49.65194 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e0a2ee8-b86e-30f9-ad61-ca8c6cee3e81 | -8.1278 | -45.02686 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2f98376-3bbf-371a-9ef6-1beaaacf6b37 | -11.61708 | -52.07519 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 556482bc-4ac7-3195-a395-c36149bff7f2 | -7.93489 | -46.54278 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54f8d102-e895-3b38-814b-4ddb0772cc5a | -6.27294 | -43.58063 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad9e0f15-7f6c-3b84-9e88-d50e12c30456 | -7.71683 | -48.75425 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f630cc72-f838-3967-a160-dd75e450ee83 | -7.70179 | -50.25802 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 04602337-1345-376a-9cfb-e6e749aba68a | -10.75535 | -46.3505 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa2f782e-059b-3982-bc92-14b98a81970d | -11.94796 | -50.59819 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d7183dd-cd82-3769-874b-df2b3faf25c0 | -6.26775 | -43.51413 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e10ca268-e7f9-3013-8720-1ca4ab9985f6 | -6.82531 | -52.83917 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b06fd8e-3796-34bb-91b9-2df63a68e699 | -10.30433 | -46.36345 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32121bad-8071-3a9e-b06e-82cd30029af1 | -11.65283 | -52.04136 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7d1ab8-78ad-3e9c-a659-712623654a9e | -7.93024 | -46.4231 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e52458-0864-38d4-9d5a-ce45106f1b4d | -7.00652 | -43.21759 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cc9d2567-ef36-3b94-a52d-e6e5220a1bca | -5.91946 | -57.73223 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5b990bd-84d5-3bd0-8f05-96fc1b0dcdc8 | -5.44746 | -42.8402 | 2025-09-03 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 49f446e4-5dc1-3f4a-b20f-6ec68e183c64 | -11.59401 | -52.11464 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc36c9dc-ee18-3841-87c4-aa41e69c7267 | -8.82395 | -52.01255 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa570dc-f6d0-3d39-88bd-e2f3c75d4f9a | -9.3308 | -55.22557 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e2b63c-d6d3-3d13-9d32-fcdf3d4001f4 | -5.80276 | -43.23311 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7900a36-e0d3-3c40-b124-5730f07a7f32 | -9.73486 | -49.00071 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7feae07-2d59-39d4-ac76-b332146b52ea | -7.49497 | -45.33731 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 198eb415-de99-3c00-82c7-ce8414b9a6d1 | -7.5309 | -47.44986 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bcfd6811-2231-379b-9fce-f574cbeef593 | -6.48895 | -45.13017 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b03a67b-06e7-3e22-9350-b03261bd8f14 | -11.59204 | -46.7688 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e64829e-5aa5-3561-bf9a-f46a1a8e7ee1 | -4.8892 | -55.8517 | 2025-09-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd495f67-a1af-3221-8035-fd01d712d29d | -9.13968 | -49.64815 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd252f2d-782b-390c-b4e4-9d12e5a70ebc | -7.94593 | -46.55162 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0509729-600c-3637-b301-5e68b77f87c5 | -11.59953 | -52.1227 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db923265-b5fb-31f2-89dd-154dbc3812fe | -6.95168 | -43.27644 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1b07f682-ee88-349c-a435-fd1e7473718b | -11.67991 | -52.19709 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad0994c9-4948-3b43-82b1-9fbdee0f41fe | -8.07651 | -47.60868 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227b8e99-282b-3195-98c5-e25d67e65eed | -6.98123 | -43.10223 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60aa7dd9-3206-3b47-baf8-88ee0d1190e2 | -8.02207 | -44.0815 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f85d76c-bb47-38f6-b126-4c2b30beb73e | -9.7026 | -51.04393 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63db1e64-e63f-30cd-b87c-f4db10cc53d9 | -10.5487 | -50.43984 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b44ca23c-614b-33b3-a26d-f1772bb22189 | -11.12305 | -44.63658 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2333e7fc-dce1-3419-b4fe-7160aa04ff7e | -9.74354 | -49.40792 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b5b31cc-d334-3ecf-9e4b-d62adfc1b220 | -9.40193 | -48.04771 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d40df4a4-50d9-3de2-9cdd-9550db254360 | -6.07868 | -46.82272 | 2025-09-03 04:46:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99c5f011-0e99-3223-b735-a14b17877557 | -7.90932 | -46.48166 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c53aea12-fb79-307d-91ca-0f87befbbabe | -6.83659 | -52.83352 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 847439c8-da9d-3238-a10e-54cd6ae0683c | -10.10293 | -46.25986 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a80774f-fd97-3801-8b61-8ff0e64df028 | -5.81404 | -43.22345 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| dfb14369-d43f-3f3f-9578-090779134fa6 | -11.5915 | -46.7728 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecb4256a-19c4-3410-8a67-d82f6ef77969 | -11.6056 | -52.12726 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2538c48b-1a95-39ea-bf2b-c4a7e5b20bf9 | -6.84966 | -52.79469 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3ede6d6-667e-3230-981e-7a04bf63f018 | -7.69525 | -48.75211 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 19b4177a-9691-3c11-bb48-4ce232468f7f | -6.30133 | -44.75094 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee06f152-6359-3bfd-a001-85eaf18ee848 | -6.4658 | -55.88798 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97732ac4-10a7-3a93-bb93-12154d2cb459 | -6.28701 | -43.58466 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ffc860f-6524-3b8a-b7ec-17a5e7b3019d | -11.58088 | -49.50974 | 2025-09-03 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1aea767-93f9-3f13-9a6d-8379adff36fc | -7.48035 | -44.8364 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89a07829-6697-3298-88f8-3f6c07aaef34 | -6.54554 | -42.9626 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 717ce59d-d953-381a-9d54-82abb0c26c7c | -7.29038 | -45.2887 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01272ee2-7f15-34fc-bf7f-4a374d352bef | -12.57345 | -44.77871 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93ab2ee1-7ca4-3b06-b5b9-47bcdfcd61ce | -7.4759 | -44.8356 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bce088b-1cd1-3e84-be90-0dc5b59cd8c2 | -6.2329 | -55.93401 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e1751add-14ac-3e49-888f-0caf7579929a | -10.26013 | -51.10952 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a920dbf-3df5-3e7e-9d83-295d78d59fe6 | -8.06624 | -52.35191 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 955e2227-4e19-3a3c-abd6-9fd25c93a2b9 | -7.11482 | -44.30693 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79c5a36b-cd5d-3b05-9d35-a5c985d5bb91 | -7.54153 | -47.45624 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b87b80e-ecb0-3a0e-b948-cb1e2f61215c | -6.85304 | -52.79519 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac08bd6a-042b-3e4c-9399-29f4950e74bc | -6.84909 | -52.79832 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d727cf6b-80ee-37f1-b033-45d10ba948fb | -8.5451 | -55.25148 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30223489-78ef-3c96-9c55-2b2843da9b2e | -11.12174 | -45.12055 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c9a04d7-d98e-3bec-b6ea-a9b301c7e47f | -7.01842 | -44.35997 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 499e2700-dead-31e4-a6dd-64c7fb4a34cc | -5.92245 | -57.71427 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 34d3f448-8960-3a70-834a-76ba4def47ea | -7.50362 | -45.33855 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f1dbf8a-f752-3b97-b992-717a7aaf3c49 | -11.62819 | -52.13446 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af69f54c-7e2f-391e-b671-6bd66305afbe | -6.24533 | -42.61779 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8d0dfad-8a5d-35f0-adcc-4025c5549e39 | -11.38554 | -43.57217 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9c91380-5a0c-3672-9135-01af6e9ced04 | -11.61111 | -52.13533 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9e219f0d-1e74-311a-a173-2eb64f0b63f4 | -5.81892 | -43.22413 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |


[Clique aqui para ver as próximas entradas](README57.md)
