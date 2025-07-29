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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ea1cb6-6070-3b38-92a6-e725fa1d0bdd | -6.3952 | -53.32809 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2540bc72-fb33-3d1a-8dd7-5f2df6e6ce03 | -6.3933 | -53.33966 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c63c111-330f-3590-942f-961ce551a516 | -4.129 | -54.89899 | 2025-07-29 04:46:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48767199-7894-3eaa-b66f-0987e42cbf4c | -6.84373 | -44.76439 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 068d4292-6e13-3a46-9737-f95c1fade79d | -7.9346 | -44.0905 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0a39dac-2572-313e-9db3-8becfd6d6f01 | -3.11372 | -46.79868 | 2025-07-29 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4384df1b-1a11-3435-bfc3-f45e5be5ce91 | -3.29852 | -48.9234 | 2025-07-29 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2c7d9a3-3680-3d64-82e5-ca7ac34959a8 | -2.77317 | -49.19751 | 2025-07-29 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fec8940-08dc-39f5-b975-c1531186ff03 | -2.9008 | -48.29387 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f48e14fd-242f-3e55-8392-a7fde30c0415 | -7.24611 | -43.06903 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 0b0fab86-192a-325a-baa1-dd95bf615eae | -2.44525 | -47.33036 | 2025-07-29 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 368be96d-611b-3447-9425-960efe122288 | -4.12402 | -49.27214 | 2025-07-29 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c85e6c9-c469-39a4-8a7d-596b74a8af03 | -5.27479 | -44.47514 | 2025-07-29 04:46:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9219f87-d6a1-35a4-8739-b2ddff8c4a20 | -5.9869 | -52.20266 | 2025-07-29 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28254133-3645-3375-9c2d-7fe4f16d82a7 | -5.18864 | -44.95514 | 2025-07-29 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aa6e7bf9-ec33-32c9-89af-006476faa687 | -2.66407 | -47.40704 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dc92113-518f-3c42-8259-83b5c61a0e10 | -2.79442 | -49.57619 | 2025-07-29 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3907645-c81a-3181-ab49-3a157e7f43f3 | -6.41105 | -53.31876 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da876dd1-66c9-3bc3-943b-1199c83fd4a0 | -6.38052 | -53.3458 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa85eb7f-90c2-35be-a720-d2e98a1d2595 | -3.52984 | -53.02874 | 2025-07-29 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a45441-de31-3893-9afa-196c0528e259 | -2.48203 | -49.36721 | 2025-07-29 04:46:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3bd3ada-3887-3b3b-b7a3-ff94266e8323 | -3.88413 | -54.24531 | 2025-07-29 04:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea1b0e7e-7363-3017-bc8a-e82fa75341ba | -3.74629 | -49.05008 | 2025-07-29 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13dfa2e-ba89-3522-82e9-99fedae0f6c4 | -3.73844 | -49.05616 | 2025-07-29 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1106a40c-b206-3cdf-9b71-f2c267e30e9d | -6.69593 | -50.6133 | 2025-07-29 04:46:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e08f2cae-0f6e-3764-9672-1a1345fbf9ed | -2.89109 | -48.28857 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2dbebeee-5b1f-33b5-8f08-17f2b695c1bd | -6.84346 | -44.76351 | 2025-07-29 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 033626d9-7f5f-3633-8fa4-fb4b593607c8 | -5.19137 | -44.95794 | 2025-07-29 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15db84d-c918-3f71-917a-ffe2d64884d4 | -6.39267 | -53.34353 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de927edf-35f5-3b85-ae85-c25706ad2182 | -2.82902 | -52.35556 | 2025-07-29 04:46:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1a91e56-ce4d-3a26-a079-7ed67ab07cd1 | -6.41521 | -53.3591 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d25812d7-5801-34b0-bbed-f9e82db42302 | -4.11095 | -47.92951 | 2025-07-29 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95ec5427-d4fc-3708-99e1-91b01ca1d043 | -3.8253 | -41.55483 | 2025-07-29 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 539f55fe-3f52-3fee-8b12-ac04440ee6fe | -6.77571 | -50.49006 | 2025-07-29 04:46:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fc177a4-12d9-3474-ae72-ba8540575ade | -7.23695 | -43.06181 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 163e7249-98c5-3c34-88be-3b15119780d8 | -4.94211 | -47.43649 | 2025-07-29 04:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2666070-0c8e-3910-98e4-ae7c8e0fa6e7 | -7.24693 | -43.06321 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| bfcbf55e-29dd-3231-bea1-f1f5f35cc74a | -3.48395 | -51.1876 | 2025-07-29 04:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71f5d9e4-bb76-3fd6-91d6-b40502b9cfc4 | -6.17202 | -44.42481 | 2025-07-29 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e01339e6-f094-3b5f-9a25-93859e4b89cf | -2.89795 | -48.28963 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0312fb9d-350d-3a19-8b37-1c44b3955dc9 | -6.42219 | -53.36026 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d9457e-03b8-39ef-b566-0517afa3d55b | -3.17989 | -48.80614 | 2025-07-29 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a2c5c4-9d9c-3e72-ad03-3515d8bc0ae2 | -7.24194 | -43.0625 | 2025-07-29 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 20e42ffa-adc3-3185-b903-7496335db1da | -2.39544 | -47.62378 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 002299b0-60cb-3a18-bdc2-cdcd13f234d1 | -6.38176 | -53.33804 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f06b7f0c-178c-3ecc-a9b8-fc7ea4d57350 | -6.39615 | -53.34411 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbea2a60-21be-3537-ae3e-94f3745e8903 | -2.58337 | -51.92416 | 2025-07-29 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cab9b823-370d-39e0-9531-873931a72443 | -3.25357 | -43.26274 | 2025-07-29 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c35f7c47-0794-3e8a-a4cb-6ace464fe969 | -3.1759 | -52.87488 | 2025-07-29 04:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24e08193-8a2c-3ecb-9cbc-7614c241ec65 | -5.99085 | -52.1996 | 2025-07-29 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2afee11-c3f3-3efb-934c-af39a08331c9 | -4.11156 | -47.92553 | 2025-07-29 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f0c2931-3f52-3832-ac60-81673a056c86 | -6.1258 | -47.73249 | 2025-07-29 04:46:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 839ada02-173a-3e4b-81b7-3b2ca1d882f5 | -4.12066 | -49.27161 | 2025-07-29 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c660769-5630-3426-8b8e-e23c0d1c527b | -3.15613 | -48.60266 | 2025-07-29 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59f81ca3-9dac-3270-863f-d31b75b720b9 | -6.38278 | -53.35408 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dbda2ac-f8f4-3f81-8306-b000c1680a3e | -6.08917 | -42.9349 | 2025-07-29 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 93d825ea-4c4c-31fe-b0d3-b162a452b119 | -6.41933 | -53.3558 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38f08c5c-6249-3e47-ad1e-e8d463700dd1 | -6.38092 | -53.34957 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0788a83-2440-3481-a026-f6e86d9a932a | -6.39108 | -53.33139 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a712f6-c6eb-30cb-902b-49f18c8593ab | -2.89452 | -48.2891 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0c06820c-0819-35fc-ae8e-cae024b52a58 | -2.74516 | -48.68446 | 2025-07-29 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cbba4ba-9c27-3951-bd76-de436732d4d9 | -7.93929 | -44.09124 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65dff33a-fbd4-393d-a9fb-2865d6a5bd9a | -6.38632 | -53.33852 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b51eda5-c11a-32be-8421-a7f9d11efa9b | -6.39139 | -53.35128 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e226d7f-9b38-36f4-91c2-ebf82fe6842e | -6.40281 | -53.32535 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628d4340-55a2-3994-8ea8-e120db1f983f | -5.88388 | -50.58828 | 2025-07-29 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d1339ba-5107-39a4-86f6-23a281be1004 | -5.99422 | -52.20014 | 2025-07-29 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a182d75-7f8f-3ce3-be49-e253005597d0 | -7.92992 | -44.08973 | 2025-07-29 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad9a5f63-1d59-30fd-8cd2-5651ece938c1 | -6.49547 | -56.20427 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 891c058d-8fb7-3a0c-94e4-4e653ace9a99 | -11.99637 | -46.97255 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53fa1b6b-e32f-3436-ac56-24e88d54acdb | -13.06817 | -47.37236 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df68b00f-8422-3e38-a9af-1dae747ddc78 | -9.36565 | -45.73794 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e708eb8f-4669-30cd-b9ac-cdfc6db96928 | -9.28308 | -46.53544 | 2025-07-29 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 101e450a-d39b-3e16-af9a-cb1e0d8e8d77 | -13.11588 | -47.38593 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17217f8-de4b-31df-904c-1df88586eaa3 | -8.88515 | -47.3414 | 2025-07-29 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2b872cd-408e-365a-ac82-8ec9e467e400 | -11.98772 | -46.70273 | 2025-07-29 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f977d32-1ccc-3175-86ab-7941870d05e5 | -11.34158 | -51.25378 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f22bffc-3f55-3e05-a927-1e2ef4dd8caf | -10.96452 | -49.57124 | 2025-07-29 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 903627fc-8ce8-318e-bb83-00a1984e20a3 | -9.87208 | -44.68951 | 2025-07-29 04:49:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcdd8232-f08f-3858-a9b3-fe888c4cebd3 | -9.7084 | -48.61369 | 2025-07-29 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8860e8c-5089-3bd1-979d-98727f16cf9a | -11.52042 | -54.68483 | 2025-07-29 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa385222-9d9e-3e81-a4b6-03b9d1959981 | -11.42654 | -45.13464 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| cadb4484-512e-382c-9b92-6ad7b0952d83 | -13.13688 | -47.3532 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ec71f2a-6682-378d-ab9e-feb775421e9d | -8.95005 | -46.75576 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c8370182-b8b3-3bc0-9258-093a2969fd08 | -12.00151 | -46.96576 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2a962dcc-18e3-35e0-b9aa-d5c3e37a5c03 | -11.99994 | -46.97681 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4e8213-88b2-3e07-9e0d-69db9c5205aa | -9.32813 | -47.59582 | 2025-07-29 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fe1a833-bd1e-33c2-9159-f7b3430043aa | -13.00791 | -44.88694 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cf5fa79-a653-37fc-ba2d-9b591592b8d9 | -10.52516 | -42.55095 | 2025-07-29 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5b546395-479e-3753-b2bb-4bb75e09e22b | -13.06925 | -47.36449 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd90ccc6-370d-3f0c-be98-e41f3c66a835 | -9.40156 | -45.48704 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 145329d7-435e-3dee-9af8-204d0ec40009 | -10.23777 | -47.74959 | 2025-07-29 04:49:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc2fd551-5c15-3c9b-9ab4-db175236ee65 | -6.5059 | -56.21724 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca42cde5-2939-30d0-9d70-971e603a6af4 | -7.86562 | -47.87404 | 2025-07-29 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ccab2dc-579b-3c47-95a8-a365451127f9 | -9.99674 | -48.13015 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3924d05c-07e4-3c7b-ae22-ba38bfa60792 | -9.23222 | -43.15612 | 2025-07-29 04:49:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 461cf62e-986d-382f-b573-17361230201f | -13.06717 | -47.37965 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 026baeb1-7ac0-34ee-8bca-66ef79783c39 | -9.36194 | -45.73331 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd2de7c6-910e-3e5e-a992-12d5ed8e264b | -9.59129 | -44.4594 | 2025-07-29 04:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b164d17-fb5f-3551-af0c-17e2ef3b00bf | -12.00005 | -46.96464 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README17.md)
