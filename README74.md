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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 939cc728-a398-3b9c-83b8-22471bab61d3 | -11.5283 | -45.4933 | 2026-09-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 6c69991d-a36e-3b2f-a0ec-196b0041ea55 | -12.1128 | -47.0886 | 2026-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 0a2d2002-7801-39c6-b4b9-4184c4d2587a | -10.7965 | -44.7437 | 2026-09-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 7490598d-fde9-31b6-9586-eb8d044bb640 | -10.3193 | -50.0425 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| efddf5d8-0e4d-3522-a488-2da48c6022a4 | -11.8248 | -46.0448 | 2026-09-02 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 89dd29da-24d6-35cc-ad2c-3055ae36e984 | -11.093 | -51.5556 | 2026-09-02 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c992ccc7-f98b-3806-a6a6-1268e799e955 | -8.4671 | -54.7035 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 311.0 |
| 352a7821-e8f0-395f-9c03-93deaa46136e | -11.3048 | -45.1575 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5bf83abf-5956-35c3-9022-3fca9605976a | -11.6434 | -50.1976 | 2026-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3a4fa387-326b-3943-b06f-424e776b95d7 | -11.3579 | -45.4027 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 7c17af1f-142c-3f16-8ece-aeedea973c01 | -11.5479 | -45.4676 | 2026-09-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 29888cbd-2885-3ed7-8809-77d0f5feb85f | -3.3688 | -59.3887 | 2026-09-02 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7355b713-ae5e-3a99-9fbc-11850c6c70e6 | -11.677 | -50.4939 | 2026-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 68c408ed-a692-3705-90e6-01662ddd6375 | -6.6542 | -59.426 | 2026-09-02 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| eb0dda59-3e28-33e6-9c31-52f3951a02c6 | -10.4334 | -49.9878 | 2026-09-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| cafbeacb-102c-38ce-9c4c-37f7e4dc21bc | -11.3575 | -45.4257 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cdfd2d4d-bd43-3aef-9d0c-7f53aa5d98db | -12.3615 | -50.5632 | 2026-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| bff2f78a-600e-3db2-828d-9a4ce1dfb4ac | -8.4483 | -54.725 | 2026-09-02 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 0a5d343f-b698-33ab-b401-799c20d1a27f | -10.442 | -46.7235 | 2026-09-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4a3b3d65-100a-3379-9141-38b795fe4ce0 | -17.0878 | -56.8534 | 2026-09-02 13:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.8 |
| 934b48da-8bf1-3c39-903d-48fdf415bd31 | -11.3044 | -45.1805 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 64082cb6-271d-36d5-93a5-56bd5fa0cec9 | -11.3771 | -45.4 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 25c24d46-b6fd-387d-a15a-afb5205109e2 | -13.5531 | -59.7574 | 2026-09-02 13:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a8b30dfb-63b0-3723-984a-ccd970847b21 | -6.8613 | -41.6532 | 2026-09-02 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| c1829b1d-d0c1-3add-8c39-c41cebd50581 | -6.1475 | -57.741 | 2026-09-02 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 24f60c74-044c-3e1e-b3b0-ce81120141aa | -13.9664 | -58.6736 | 2026-09-02 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0bc30fa0-4bc9-3376-b0ae-a1bf7ddf6e62 | -10.9562 | -50.4884 | 2026-09-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0449b5b3-76a2-3f1b-b629-87cb4c93231b | -7.2191 | -60.6699 | 2026-09-02 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 28fe1a61-c2de-3e61-b835-da601b9fdc16 | -11.1123 | -51.5325 | 2026-09-02 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 0e6d2c2b-a163-3ab8-be07-aa2369a39ff1 | -9.4349 | -45.625 | 2026-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f960a454-60a2-3452-9001-dfbbfdf0a609 | -10.9565 | -50.467 | 2026-09-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1597f615-6c32-375c-8554-9d86d04ebd99 | -10.1008 | -46.7195 | 2026-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7a5d1819-9d40-3182-b11d-572d1e8ffc4c | -11.3052 | -45.1344 | 2026-09-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7899a880-da85-380a-bb08-3d3a2959e6ff | -11.6624 | -50.1954 | 2026-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f8278135-66d1-3e8e-bd4f-def26f155603 | -6.8422 | -41.6791 | 2026-09-02 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 8ce38100-6c10-3cd3-b4aa-2f00ec42779b | -12.0741 | -47.1164 | 2026-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c724e02f-c83e-37fd-8d05-039986eb9518 | -11.8439 | -46.0421 | 2026-09-02 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 238.6 |
| cd381428-3896-354e-9542-dbbca410ba26 | -10.3196 | -50.0211 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9b2c7724-c101-3f2c-a7c5-d7d13c07ae58 | -12.0741 | -47.1164 | 2026-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| a6fd478e-1de4-3b5c-b21c-c70c7be4a776 | -11.315 | -50.5774 | 2026-09-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4dede75d-7661-3ffc-a096-e7fda23e97dc | -10.4334 | -49.9878 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f165d65f-0702-3481-ac04-99eb4465f0cf | -10.4142 | -50.0112 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 60d266ff-f897-3ec9-97a0-bb9499684412 | -10.9006 | -45.3738 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5d0d89df-05be-322a-9463-7e84bec2a9af | -5.6016 | -60.211 | 2026-09-02 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 5c531a8c-27a7-3da2-8852-2c491608717c | -11.2857 | -45.1602 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 9e936478-47ad-308e-ac30-c9aebdbdd9c3 | -13.5531 | -59.7574 | 2026-09-02 13:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c2df425c-217b-331c-a373-aaa10a27c08d | -10.3193 | -50.0425 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0e46b8f4-68de-306b-b73d-87e31f39afcf | -6.5486 | -58.5413 | 2026-09-02 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 8da172ad-8c80-3911-9b03-e8e16461c5ae | -8.4673 | -54.6833 | 2026-09-02 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 52adf1bd-0037-3e70-b38c-d48485dc0c1e | -10.5788 | -47.7306 | 2026-09-02 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 79e7636a-7bc0-3141-a62d-c1db192d600b | -10.7774 | -44.7463 | 2026-09-02 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 49f19f36-1b23-3ab4-ae92-1b360dfdffb7 | -8.7817 | -46.4623 | 2026-09-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bf71652e-9285-378e-ae78-35be0933482e | -7.3487 | -60.5883 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 938956d2-baeb-3618-994e-d8983e091d5e | -10.301 | -50.0016 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 08802d10-aa9f-3279-8b48-f1cc6662c71f | -9.9912 | -46.4409 | 2026-09-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 94c31cc2-4147-3a06-842e-0297912fe7f5 | -6.8424 | -41.655 | 2026-09-02 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| e4ddbfbc-6b59-344e-8adf-0e5340212858 | -11.3575 | -45.4257 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8e1022d8-56f2-39cb-8aa4-66563bf661b8 | -10.7618 | -50.8707 | 2026-09-02 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a4574ffa-0250-36ee-819e-3b6446461fa4 | -3.3688 | -59.3887 | 2026-09-02 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9063ec0d-294f-3f6b-9b9f-9868e8b05e6b | -12.1312 | -47.1309 | 2026-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 106fd107-acb8-37ff-944d-9c974d2d9d06 | -11.1723 | -51.294 | 2026-09-02 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7a816286-afd6-3c71-a6ec-58ff24cd3743 | -3.2455 | -47.9187 | 2026-09-02 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f2e5c5ad-c1b8-34b7-a07c-3c7c0e716e31 | -11.3579 | -45.4027 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| c0fc690d-3f5b-3a0e-a236-416dc6abc5d1 | -8.7613 | -62.5869 | 2026-09-02 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c132dff4-9095-39cc-83dc-95c1b96a766d | -13.5533 | -59.7377 | 2026-09-02 13:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 24c63ebc-f54c-3f98-9f3a-4d1261bf3e1d | -11.3052 | -45.1344 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d0a02ac5-5a43-32f5-a132-e41d416c728d | -7.2191 | -60.6699 | 2026-09-02 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d1327552-5fe4-36df-a984-45e284671288 | -8.446 | -62.6752 | 2026-09-02 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fe17e752-b800-3dda-87fc-4c03f7af6fb2 | -11.6434 | -50.1976 | 2026-09-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 6591bef3-d964-34c1-a90e-51fa38d77b59 | -6.6541 | -59.4452 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a1402506-76a4-3734-8078-59a0548b34cf | -11.304 | -45.2036 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 83443581-df08-3900-95b4-3c87f31a7362 | -13.9664 | -58.6736 | 2026-09-02 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 91a9d350-65a5-3ed7-aa84-dd0c34c6394c | -5.5832 | -60.2116 | 2026-09-02 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 5ec0e110-d859-3bec-b955-be76620ad6c8 | -6.3892 | -45.489 | 2026-09-02 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e94dcc60-f895-3d09-95a7-20aca0c72531 | -10.4145 | -49.9898 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 12a8d2e5-1600-3f95-9b6c-501325eff477 | -7.3486 | -60.6074 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 6407644c-de83-325d-b5bb-0df668d73c8f | -13.5724 | -59.7362 | 2026-09-02 13:50:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 12cba054-bd7c-3694-bdc7-1e04e2c28a4c | -10.9565 | -50.467 | 2026-09-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7f8d5131-9828-3a02-ab9c-9cfcc90ba505 | -7.2255 | -42.7616 | 2026-09-02 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 66765ac8-4fd6-3233-a55d-b9a525a5f4a8 | -10.3007 | -50.023 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 64c367e4-c9ed-3bd8-a1f0-86f8faea89da | -6.7648 | -59.4408 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9b7eaac8-2199-3f94-9cbb-66d30c5d35cc | -10.9752 | -50.4864 | 2026-09-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ab6fe508-4226-34db-9317-40f940572ba8 | -11.3239 | -45.1548 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 206c3557-7c38-3a2f-928c-3da2a69097f3 | -8.4298 | -54.706 | 2026-09-02 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 1d8f86a9-a0b5-313d-bc26-d821022c2b15 | -6.1474 | -57.7605 | 2026-09-02 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 72fed045-5edf-3b83-84d8-9fd1b62008bd | -11.8248 | -46.0448 | 2026-09-02 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 1eb6e5d3-1074-3b55-8714-9d9a0ddc8a97 | -12.1504 | -47.1283 | 2026-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a27a998c-f519-3e11-9b32-f4403fcccea0 | -7.6147 | -44.9062 | 2026-09-02 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 67062016-c1bd-395c-b17c-6b3e5f5df67f | -9.6633 | -48.2721 | 2026-09-02 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 646acb72-4690-38e5-8aa7-7791297f36b8 | -11.2106 | -51.2688 | 2026-09-02 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0e063138-00ce-36d4-8805-fa5b028e756f | -6.6358 | -59.4267 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c0eda08d-3536-3101-b4f6-0bbfa8650700 | -10.4148 | -49.9683 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f407deca-d7b0-3eaf-bdbd-26fd7b3b12f9 | -6.8756 | -59.4171 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8ab2eeba-9aee-3c70-a59b-2f671579a29b | -10.3004 | -50.0445 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7692839c-37fa-3b8e-a604-367994b840c5 | -6.7832 | -59.4401 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2e83d18d-75f3-3836-9338-1a3df55f2f39 | -10.9562 | -50.4884 | 2026-09-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1f118b02-6128-310a-af0d-6c2076a16e86 | -5.5833 | -60.1924 | 2026-09-02 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| ee8ec32d-cd2c-3c3b-b865-30fd1e29b6cf | -11.3771 | -45.4 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 0ae6820a-0342-3e6b-8306-9b6eb2833f8e | -6.8568 | -59.4757 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 43b8c468-1420-360c-bb8d-16a64a93af64 | -12.8843 | -45.8183 | 2026-09-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |


[Clique aqui para ver as próximas entradas](README75.md)
