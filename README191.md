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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20d989ba-04be-3120-94e5-c12513614931 | -16.18974 | -44.56644 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ec140564-58a5-3581-909f-70cb0848fc81 | -6.59058 | -44.19424 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d23160af-91c4-38fb-a895-a969bd182ff2 | -8.53583 | -54.59319 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bb756d1-b6f9-37de-86b3-2456941641a7 | -9.11112 | -45.11082 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 300.5 |
| d8364588-6cf6-3f7e-b7a0-84697f586706 | -6.93273 | -38.29084 | 2026-10-07 16:37:00 | NPP-375 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1548ecc4-502c-3305-b52c-33d2a04f0fd6 | -4.79498 | -43.22756 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01d7650f-1ade-3ab7-a550-de36249fb3be | -3.30457 | -42.27768 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7f8a4d52-518d-374c-9bcd-a3eae441fda2 | -6.67304 | -55.09876 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7cb4b5ff-e61e-3786-b201-a50c5b656478 | -8.79659 | -47.22039 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 10a2307e-3b08-39c6-899d-6081cb5406b4 | -3.50483 | -41.94391 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4e061a1e-760b-3acd-933c-b9096750b487 | -17.01472 | -45.91413 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d06b50ec-4f65-31af-bd56-df80c3ca4973 | -7.28829 | -43.87012 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e93dc092-6ea7-363a-839d-421241aa98d8 | -7.80321 | -45.50213 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b1c447cb-3a3f-382b-aad4-3e286c0d2671 | -9.96919 | -43.56323 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7a7351fd-654f-3019-89c2-f54073ec6d19 | -6.41342 | -54.97537 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3dc65ada-8cd5-3b4b-9664-404fcaba47d8 | -3.90705 | -44.11002 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 38374af4-664b-37dd-8497-9148b3988ba3 | -5.72683 | -41.7184 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 047ee0b1-78dd-34a7-b241-696efc6b50fd | -10.29556 | -47.82679 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fc6212dd-28dd-34ef-bcfb-510f3bf4d180 | -3.19584 | -42.95549 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a55340ad-8237-3fda-a74b-8fbdd42d5f11 | -8.00633 | -47.18284 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d0284864-63c9-3e6b-acee-3fb2529dc46e | -5.97259 | -40.94699 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 7efe085d-2567-3231-bb9e-d34dc0400ced | -15.80585 | -47.85053 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e4b11d1-2d1c-3218-9c5d-f36860db9e0c | -10.99656 | -45.47007 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aebff6fb-a1b2-3c90-b59f-b1c95d4cb8ac | -10.79903 | -46.55178 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 941678e9-5f8e-326e-89eb-9c6827e18258 | -5.73266 | -45.15408 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 4eb4e63a-04cc-3b0f-88c0-10e322ed93bc | -9.03254 | -46.90271 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b53f8b2d-2620-3739-b4cf-037572ee3f02 | -11.05938 | -45.85238 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 71d1503d-2436-3ba9-b1c5-2b1c7bb10fbd | -8.44159 | -48.91809 | 2026-10-07 16:37:00 | NPP-375 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1df7d8aa-9afc-334f-8bfc-3f6e357462a2 | -10.3545 | -46.25028 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| fee2957d-b62a-36fa-ab32-684a4b7118f7 | -9.10716 | -45.10764 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 354.5 |
| b564bbdd-2cac-3a42-94a6-955fa29f8ae7 | -6.26031 | -52.85624 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d4754b64-5826-3375-adc4-bd8e6a235044 | -6.80359 | -43.70901 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e423842f-fc38-346f-a35b-da9506ddbc6d | -6.64982 | -47.91484 | 2026-10-07 16:37:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 12bdd727-15a1-343d-b0c0-73ce7340793e | -17.01299 | -45.91702 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2f038a2c-8459-39fa-8667-de5a219c993e | -4.27756 | -39.55075 | 2026-10-07 16:37:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 37b6c7cf-6732-3516-ad64-627a464e04f4 | -5.74193 | -41.70005 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 072ef361-0f2f-3bc3-b4d5-0c1d7e8b9f8b | -5.97447 | -40.9119 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| ab01a120-4bb7-3352-b4a3-aaa92a69a155 | -4.57338 | -40.72395 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 06fb4bca-c187-32f8-bd9b-72665c02e18c | -11.08265 | -45.6441 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8659355d-43ff-3935-bf33-6f753eddb66b | -6.22228 | -44.84074 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fb60f864-03a3-32d9-893d-40f5f69cbe76 | -9.91809 | -46.80283 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| c8aacc7f-c4b3-3e06-814e-44181c74c49b | -8.59377 | -45.68952 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8e69f99e-7a14-3d3a-a9b3-79363105d0a3 | -7.82227 | -55.12548 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b4d34575-cbdc-3e3d-9c0f-cfd638cd7d09 | -10.24106 | -53.93343 | 2026-10-07 16:37:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12d0b690-29dd-3067-bbf2-611cd8390467 | -5.83015 | -52.12717 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18b60d0e-9482-3dd3-a019-1e9a4e66c581 | -6.12927 | -55.68853 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34c0f8a8-c2ad-3fe4-a242-0fd36ce5fcad | -10.07838 | -45.984 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7bf4a60c-d2be-3da5-9773-6ab25cf4e2cc | -10.92585 | -47.26067 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f03dd50-e8d2-3b24-b54e-dde9cbcaf2ca | -3.39118 | -42.71092 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1bcd84a3-1ba2-3f81-9d45-1a081902ecab | -3.63056 | -45.19799 | 2026-10-07 16:37:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| baaf387d-9399-3c83-afc4-d2fbb1ae221f | -7.52598 | -38.37724 | 2026-10-07 16:37:00 | NPP-375 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f4dc0067-2bb9-3b8c-9c4b-ebcd6984b87b | -3.86699 | -44.13744 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5fb65627-f21f-3305-bcdf-1dae9f1612d2 | -5.72168 | -41.73126 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c01aa3d3-2404-3b81-837d-9afa32904bd6 | -3.76214 | -40.76704 | 2026-10-07 16:37:00 | NPP-375 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 93bfed87-fb6a-3620-ba74-76aa915f1091 | -6.94794 | -45.26033 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dca6e51f-089a-3b3a-9bfd-9ae5ac767951 | -3.95112 | -41.5347 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| ed9a4230-58cc-3ea0-874c-90e97b4ea0cd | -6.87892 | -43.6903 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a03abfae-0b70-35c7-a4d8-6cea0d19ee3e | -6.59603 | -47.40944 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4356cd5b-47fd-3bc0-8748-79d4f427deb7 | -7.10104 | -45.23707 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe0c0d6f-d955-3293-ad19-6d1c22bddb5f | -6.04716 | -53.48388 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| df0489ec-2cb4-3877-a858-fd756d82aa54 | -15.88889 | -40.72196 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 77d51187-555e-357a-a74d-998cfb1c921a | -8.72764 | -46.67538 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 322383b9-887c-3aee-832a-eaf9946dc9ac | -7.20332 | -55.1079 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3889958c-c02c-392d-a571-da036fcd7f42 | -8.98098 | -48.93661 | 2026-10-07 16:37:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d021da79-f601-3e20-9fdd-4b5c7310b12e | -8.95088 | -45.10904 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8425ff3b-1b64-3b5c-9ebd-5a2bc9bd1ee8 | -6.00764 | -42.27231 | 2026-10-07 16:37:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 55703aa0-d369-3094-a26e-5b7b2d4d730b | -11.15572 | -46.10604 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d1bc7a3a-6587-3cb2-8e17-ce71872d5820 | -5.71344 | -37.71386 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6ed8c9c1-37e0-317f-8e7f-4e6ffd7f6f55 | -4.10961 | -39.16195 | 2026-10-07 16:37:00 | NPP-375 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a36dba88-31ee-3c1c-bd69-71b157b9926a | -6.22029 | -52.83632 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8fb15d71-7114-3a5f-a949-d032f2038fd5 | -6.12261 | -52.71557 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4c6ae448-b9f9-31bd-87fa-b8ce16c707c0 | -5.27548 | -45.17181 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68453a36-ceb6-383c-9d37-704e63ce73f4 | -9.79943 | -46.24018 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ed8a5331-4c5a-3993-b5f0-bb3cc870f5f2 | -5.67775 | -53.4947 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b50c6fb4-cb68-37f1-8ec7-28b798d301ad | -6.24426 | -44.87322 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 268d146c-b708-346d-986b-b52ef9bd5634 | -6.38456 | -42.92348 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a8400b8e-9825-3828-8701-07a0d22881f6 | -7.41277 | -35.0927 | 2026-10-07 16:37:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 1f57ab30-88ed-3386-a460-dcb4f396fdf7 | -6.5801 | -41.59406 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 0d95e8fd-a2af-367a-a2f5-0a548fc7f759 | -5.97094 | -40.96001 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 14dc4c46-9126-3c4d-9ffd-b41b7f470e41 | -10.46133 | -46.8347 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc11d294-5605-39fb-8a5c-db44b6952c18 | -11.1575 | -46.11858 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 5741e5a4-5029-3a1a-a617-724e625a0349 | -11.11951 | -45.95403 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dab57a97-ab8f-3772-b3a1-e7b842d9f566 | -17.20422 | -45.09307 | 2026-10-07 16:37:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8beabac8-13f0-32c9-b49e-4c21d75847ad | -7.00448 | -56.49068 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1cf3cb84-cde3-36d3-8471-56f8dcd72eb1 | -7.19992 | -55.123 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8fde5841-fcd2-3ca3-a282-cf22e426d19d | -5.72706 | -41.74241 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 105101bf-504b-3aa2-ab18-65f057855b54 | -8.52919 | -54.58942 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c1794c0-0f85-30b5-9cb6-bdcc80d6308c | -3.5165 | -44.98519 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a7809e2-11c6-37b0-b625-65c9e0e60795 | -10.96822 | -45.39811 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2928abf3-2a6e-3665-850e-6203b6282469 | -7.76193 | -54.95071 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 10a32606-a325-3767-b818-aeaf1b133980 | -9.81805 | -47.48074 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cb7077e-de12-3737-b8aa-79e3ce65eafc | -5.49451 | -42.83404 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 0adf741e-592f-3595-9d16-1f14be094a02 | -5.97689 | -40.9506 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 487591c2-9673-39b8-aa64-02a7ea74f452 | -8.95985 | -47.55466 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 449dbbaa-af28-3ba9-ae80-016fbe6523a3 | -9.86877 | -46.05112 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 0cae29a4-99dd-3920-9871-cab6554bb7ee | -5.83298 | -53.52846 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 256a152b-1685-3fc8-9f65-cd821410b6d5 | -3.88363 | -44.1349 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2780d3da-7443-3da4-937d-26db7920e331 | -7.6869 | -47.34169 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6894930-6019-3710-86cf-45b5bcb3f067 | -7.00295 | -44.06128 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fde065e2-ef83-3827-9661-ec9010077fa4 | -11.10127 | -47.62841 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |


[Clique aqui para ver as próximas entradas](README192.md)
