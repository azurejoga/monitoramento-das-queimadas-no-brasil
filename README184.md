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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d1720e7-9727-355c-a528-7c2d4020ba33 | -3.1839 | -60.1559 | 2026-08-31 18:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 4b896042-f774-3fef-99d1-dfdd8a9eb4f2 | -14.5028 | -52.1913 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 78be707e-164f-345f-89a0-fcfe0faf8a23 | -7.529 | -61.3635 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 71d489c8-ae87-3f25-9a3b-0ea541af4f00 | -7.0982 | -45.7689 | 2026-08-31 18:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| d6bb2e86-e03c-30d8-9ef9-34b9efbc8019 | -9.8927 | -60.2752 | 2026-08-31 18:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b6ea879c-1260-338a-a437-1643ee26ed91 | -5.9451 | -57.6906 | 2026-08-31 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 4b81c20e-6774-3e84-a81b-2f85dba4e20c | -15.653 | -56.3854 | 2026-08-31 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8c66e772-18ba-3a33-b53b-5fabb024e714 | -7.3453 | -72.9539 | 2026-08-31 18:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ae4eeaa3-13dd-32d4-aeab-6c72647a39bc | -15.8844 | -56.4819 | 2026-08-31 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 43ec400e-b2f5-3eb5-bf77-3c0ee6f45554 | -11.0744 | -51.5365 | 2026-08-31 18:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e8244e24-50be-3282-ae81-ae5c86108745 | -15.6336 | -56.3876 | 2026-08-31 18:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| aa11113a-cb39-3f14-9fd7-27ce65be5a58 | -3.4002 | -61.3276 | 2026-08-31 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cfe0b937-c89c-3321-b46b-43bc5ef3dbb1 | -9.0534 | -60.4542 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 467050d5-5a0f-30b9-b2de-eace385dc27e | -6.6542 | -59.426 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4ea21838-adb7-3ac0-8b51-21b684a2f767 | -9.0058 | -65.4373 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 34ea0f32-422b-3bf7-85a2-cad41fe7815a | -9.6676 | -47.9429 | 2026-08-31 18:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 80aa54bd-24f8-3399-94e1-4847f510c9c7 | -10.8218 | -50.6306 | 2026-08-31 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5ea4f2f6-131a-3ef4-ad22-f3ef783cc0c9 | -9.2277 | -51.5847 | 2026-08-31 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9234ddf2-f02e-372c-a941-1de5f922b182 | -14.4835 | -52.1938 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 475a7258-0953-3342-b06c-e8bd3319a0b3 | -7.4449 | -59.9324 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9e5ced6f-4151-39c1-a550-f40a0b729644 | -3.6399 | -60.5466 | 2026-08-31 18:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3ad8e4b3-2fb4-3c1f-88e3-6b86fb55e148 | -8.8644 | -68.5034 | 2026-08-31 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 72b1eedb-e045-3541-a77e-ac36ab235426 | -8.5555 | -66.9574 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a15302dd-0083-30e2-bb76-53bd342c098d | -9.2256 | -59.7894 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5887abd8-3f35-3754-85ec-42df04dfff3b | -10.1968 | -69.343 | 2026-08-31 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d26d3e41-8118-3eed-b453-ffc1e5a2b8a6 | -9.173 | -59.3659 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 44202801-1d9d-343d-9a86-c8c58bac1052 | -3.6076 | -59.0769 | 2026-08-31 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 348bc363-66aa-30ba-a926-c7ceb159ae0c | -7.2932 | -60.6096 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 49f88fa2-da75-35e3-841f-dc0a87d61af4 | -11.6247 | -50.1783 | 2026-08-31 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 0162adb9-fa92-3f81-9b23-ecd664c49b2e | -11.0747 | -51.5153 | 2026-08-31 18:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ec8629e3-2d28-377d-a026-1315437c08ab | -8.8705 | -66.7822 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f1c992d7-004a-388c-8f5a-d511f95b970f | -10.4961 | -59.6195 | 2026-08-31 18:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9c97fb39-e4dd-35f1-b764-f070cbf25535 | -11.7973 | -47.6672 | 2026-08-31 18:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ce71e3d8-9041-386e-b87b-52eeabf497bf | -8.9874 | -65.4192 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f3d935c1-3fc5-340a-aaf9-69ca961613e9 | -12.0733 | -44.999 | 2026-08-31 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0746163f-3087-3c10-b59f-b1ff2b3191d4 | -14.8316 | -55.7399 | 2026-08-31 18:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 194bddf4-171f-30e8-9a1f-af2af66ae5fb | -14.4641 | -52.1964 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| c8de64c3-f546-3f83-981c-a0693ae4983c | -9.02 | -57.5377 | 2026-08-31 18:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d9646d40-ad7d-37c5-9583-fea7e86f8cd3 | -6.1109 | -57.684 | 2026-08-31 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| a3e58a4b-3a88-384b-a611-e2bba604cd73 | -9.1532 | -59.5221 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 64445ac8-b8fd-3115-abaa-57b84c22524b | -8.8953 | -70.8938 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0d4c84f9-86ac-35d7-9f35-5dca4819b3ea | -12.9221 | -45.8582 | 2026-08-31 18:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0d22b2ea-1886-348d-b0da-8364c4766a76 | -5.8537 | -57.5576 | 2026-08-31 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 05763bd4-a3db-3f9d-bae0-94ec58969f0c | -11.2485 | -45.0963 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 2ccd206a-657e-3606-853c-2699b822ec57 | -7.7752 | -44.0628 | 2026-08-31 18:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| fc413014-5b87-3d78-b87c-898018cf98e2 | -10.107 | -68.4008 | 2026-08-31 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 121.7 |
| f2644793-23f7-3f1b-848e-3f819f759507 | -10.8444 | -45.3126 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| b3d44165-e49c-33be-bc68-9c3f2eea8895 | -8.3601 | -70.8641 | 2026-08-31 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e6f81026-ebff-31a6-a9cf-9bd06852a2c1 | -11.2286 | -45.1452 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| cdcb8bd1-2310-3f7d-ac8e-bef8c306ab34 | -6.6541 | -59.4452 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| df807ce5-293b-3567-918c-b37402f31191 | -9.0722 | -60.434 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e1234a1e-8d4c-3bd5-9224-ecdb77400e95 | -6.9367 | -55.636 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 347.0 |
| 2cfd9f71-fc31-34b7-944d-23298cb07415 | -3.1267 | -61.1811 | 2026-08-31 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 224.3 |
| a3d34ea2-7951-30b0-8151-058ba65acab7 | -10.844 | -45.3356 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 693b6848-d198-324e-a59e-76e44260691f | -14.5623 | -52.0984 | 2026-08-31 18:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4eda414e-4942-3843-85b8-6ffd301b1c99 | -9.1709 | -59.6374 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2a9b5f87-a07e-3b35-a3c4-18e35129380e | -8.8026 | -71.0783 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a4396db4-fd5d-3764-83ef-930ab0934b6c | -7.2934 | -60.5713 | 2026-08-31 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 04f6b376-2772-377d-8fda-d8690b5d51f3 | -7.6253 | -55.2787 | 2026-08-31 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 3d280568-d1ca-33f0-a176-2918c8ac4547 | -9.4153 | -45.6726 | 2026-08-31 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ac2ef08a-82e9-37d2-8ac3-312be30de827 | -7.4734 | -61.4037 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a2655675-aa4d-33c1-a910-162c0fca64af | -11.1809 | -55.0821 | 2026-08-31 18:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 33a5ce40-f5dc-3c2c-8d04-86f186186b20 | -3.4002 | -61.3465 | 2026-08-31 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f22664d3-7f6e-3a51-999c-065e0d12c8e0 | -9.6939 | -65.1145 | 2026-08-31 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 248.5 |
| b81b80c4-b93c-3efe-9d72-7193791a6002 | -8.6026 | -69.65 | 2026-08-31 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 81017709-b1b7-3bee-86ec-973e3d6f1876 | -5.9636 | -57.6704 | 2026-08-31 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d76c4f8b-4d86-3932-b59d-8d67f32b00d6 | -8.574 | -66.9569 | 2026-08-31 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 51be3c9c-fe5d-33f2-8021-96768b420136 | -9.971 | -53.9214 | 2026-08-31 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| ca7753ad-d20e-33e4-a7ef-c02524f656c6 | -9.2098 | -59.4221 | 2026-08-31 18:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 272a1eaf-3430-3cd8-9ed5-6e5f03a9b269 | -7.917 | -61.3481 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c68b685a-6317-3b21-aa59-353764b511be | -10.7268 | -50.6618 | 2026-08-31 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 789c7d73-6723-3a5d-b16d-dba6a32e4509 | -5.8692 | -52.0868 | 2026-08-31 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 107b7179-d885-3dea-ac05-c0ff5a5e10eb | -7.5662 | -61.3049 | 2026-08-31 18:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 125fbcc6-6749-3d7b-8d3a-ba3e90e7d12d | -3.4185 | -61.3461 | 2026-08-31 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c7c227b9-8eed-3df2-b7d1-5c054848fce5 | -10.7856 | -50.5066 | 2026-08-31 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| b45ebd10-8405-3f6a-a6ce-58fec3f75778 | -7.7938 | -44.084 | 2026-08-31 18:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| acb9c36c-e793-39ab-891a-db7d98b10b8b | -11.2103 | -45.1017 | 2026-08-31 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| a8c77ad0-8e2a-3b8a-b497-c1cf25fb5f9c | -3.9708 | -60.0067 | 2026-08-31 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dc9fca0e-fb0f-3d9f-a599-c7c496c9f323 | -12.1113 | -45.0163 | 2026-08-31 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fca610d8-d351-3e7b-969c-69cb003e5de3 | -3.4185 | -61.3461 | 2026-08-31 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6bff79c5-688f-3c13-a318-83ac952da9ce | -9.1711 | -59.618 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d83247ed-d586-399a-b5f4-3a73d902d11e | -7.6149 | -44.8833 | 2026-08-31 18:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 8d371001-46ac-3dba-8710-ba19714d192b | -8.8926 | -62.3348 | 2026-08-31 18:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 01a37579-2ab1-370f-802e-fb975d776d3a | -3.1839 | -60.1559 | 2026-08-31 18:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 6216b461-7db9-3af2-ac43-e3ef7087536e | -8.8706 | -66.7636 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 57ab0d63-8670-35dd-87f3-f8f1f641a53b | -10.1087 | -50.2776 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b9b28647-2909-3488-af60-37a5d52930a3 | -3.1267 | -61.1811 | 2026-08-31 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 223.4 |
| c1d47e87-3f1b-3cd4-a946-9fac9d1e8954 | -3.4185 | -61.3273 | 2026-08-31 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 703801db-07bf-3ad7-a8fc-f4acc322dae4 | -5.5831 | -60.2307 | 2026-08-31 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c6220d91-8680-3860-961d-b9bee3e8adfd | -3.6399 | -60.5466 | 2026-08-31 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9ed814eb-bab5-3765-8f61-e4ac670f69be | -11.4828 | -58.5159 | 2026-08-31 18:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| fea7121a-ce19-386e-80e2-1dfd87fa66f4 | -9.0059 | -65.4186 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e75d0a76-8f39-3f77-9757-33423697cd6c | -13.1837 | -55.6682 | 2026-08-31 18:30:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f8201e15-0d56-3307-b762-09b61507ec52 | -9.1532 | -59.5221 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b2a5c314-3068-3576-ad25-ff6e0c27dc24 | -11.2319 | -53.9753 | 2026-08-31 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 72411f8b-5142-35d5-9328-1eaaab437e6c | -10.9865 | -48.3869 | 2026-08-31 18:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ef001352-6fc8-3464-81c0-e9df45f650bc | -11.6837 | -47.6154 | 2026-08-31 18:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7f14cdda-f113-39a9-88db-a2f06d52d938 | -8.87 | -66.9121 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6bbe4897-ed6c-3f2e-94a0-6c774bbf2370 | -14.6145 | -53.59 | 2026-08-31 18:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 81e4c796-f5aa-3592-b37b-94c96a83d496 | -8.5555 | -66.9574 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README185.md)
