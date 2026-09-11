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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54f23229-2605-30f3-8120-cc4fe8a035d0 | -5.20752 | -45.55447 | 2026-09-11 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6bc9393d-4200-33f6-a786-49180ff373fe | -10.7532 | -45.92417 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69402a38-ca82-3702-9b9f-76f81d176162 | -5.03384 | -42.47763 | 2026-09-11 03:49:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 18df6029-1583-3f1d-a72f-08d93bf1a14e | -10.46657 | -48.66054 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34bbf789-1276-304d-9bac-5c05b4d3f6b5 | -10.27996 | -45.27753 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ce9ab82-3c09-3bfd-ac93-672982d5019b | -10.36119 | -48.13472 | 2026-09-11 03:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37a23db4-62d7-36bc-93ec-d3925cf2869b | -10.78143 | -45.9438 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9c75b263-c292-3e9c-92e1-85a397ad7df7 | -10.27474 | -45.27308 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3680f44-9860-3eee-a50e-fad5d8685145 | -13.76912 | -43.64033 | 2026-09-11 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a51d02c7-8d6e-3205-94ba-fa61427f2480 | -10.48629 | -48.64859 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c4988da-5853-38e1-aab4-265a776b4bea | -6.12376 | -35.21729 | 2026-09-11 03:49:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 35c218cd-a3df-3257-8ae5-faf3194728f6 | -14.67494 | -42.85216 | 2026-09-11 03:49:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a112d462-205d-36b0-ae68-3cbe2568c8e1 | -10.78484 | -45.95835 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a47f0798-a1a2-3c86-a911-f4cb9dcee674 | -14.65998 | -44.12271 | 2026-09-11 03:49:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68767695-b53c-3eeb-a5ee-e9f6dd73b168 | -10.77972 | -45.95241 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e35f37da-e97a-3b7d-8290-8a5013eb3a88 | -10.7866 | -45.94948 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50284733-5ce1-3415-b388-416799b3edc6 | -5.0285 | -42.47666 | 2026-09-11 03:49:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 45374f0b-18c3-3e08-af56-c0394184c76f | -10.48496 | -48.65484 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73afee17-06b8-3ee4-bb6a-c1d2d3e66857 | -10.97653 | -47.88015 | 2026-09-11 03:49:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7d7d1f7-db1e-336c-9cc6-3b8957800841 | -17.7195 | -42.28117 | 2026-09-11 03:49:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99de8918-fddf-34e0-8ed5-00ebb0763305 | -14.06741 | -45.63239 | 2026-09-11 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c96f8401-40d7-3b84-b33d-c61bbb88cfe9 | -10.78569 | -45.95405 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ce66d19-3ba2-3497-a179-749184427a0a | -10.46807 | -48.65329 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5665b47-0566-35c5-b80b-41c15fa78d55 | -14.6109 | -48.84776 | 2026-09-11 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 869f02e2-1ba6-3e5c-b560-764244fb7a10 | -10.48234 | -48.65606 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c8ecd62-3be4-356f-9d52-510af69e0554 | -5.20105 | -45.55324 | 2026-09-11 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2bee27e1-7091-3a52-b796-7c146ee756c3 | -5.199 | -45.56463 | 2026-09-11 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 91b0b967-744a-34a9-8a31-9405e99ca304 | -11.40732 | -43.94867 | 2026-09-11 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 495912e5-8538-3fb6-9712-91fec1082735 | -5.42079 | -41.85028 | 2026-09-11 03:49:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02d8c623-793c-3bd0-865a-43d44b5be890 | -10.22003 | -45.21114 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d2f1310-9dca-31c3-930a-e43ae558f1d9 | -13.77407 | -43.64136 | 2026-09-11 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfe3550e-16d2-381a-ac93-ec2033209b0b | -5.47711 | -45.131 | 2026-09-11 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b94deff6-dbe0-381a-bda6-d4a67c0848a6 | -4.77712 | -46.4962 | 2026-09-11 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d5465ef-8af7-3b2a-9ba0-f3d0bcc45b4e | -13.85177 | -42.44598 | 2026-09-11 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef8fab72-57ab-3d08-8680-680c273bff81 | -11.19415 | -42.78475 | 2026-09-11 03:49:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6c4373e7-addb-3746-b54e-d2d66d3ce1c4 | -10.78749 | -45.94497 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 697dd4bd-0d01-3cd3-864e-294a50136e31 | -4.77496 | -46.50115 | 2026-09-11 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 34ad0015-7c6e-32d2-a577-258e7197f789 | -14.89251 | -41.7004 | 2026-09-11 03:49:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8d44ca9-9b82-346c-9079-16aa195eef00 | -13.00409 | -44.11423 | 2026-09-11 03:49:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 028ceb57-280d-30f0-8b9b-d9e610902faa | -14.60966 | -48.85345 | 2026-09-11 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 166af9ce-c4c9-3486-9a76-9bada9949526 | -14.91595 | -44.66956 | 2026-09-11 03:49:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3147a7-7c8f-364c-b8c4-6423add16742 | -4.77605 | -46.50229 | 2026-09-11 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5250f89d-f661-325b-9909-bcfc65e00010 | -14.67689 | -42.85436 | 2026-09-11 03:49:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ae5fd288-5882-3673-a8f2-34beaa05e5c7 | -10.06017 | -46.27128 | 2026-09-11 03:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2e1039e-f6a0-3fe6-9ba1-1c856f641dd5 | -12.99891 | -44.11317 | 2026-09-11 03:49:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85a434be-0818-337c-981e-00eacd725e49 | -9.60474 | -46.77545 | 2026-09-11 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab2aa8b-194d-384b-9c31-a3530c497487 | -10.2209 | -45.20676 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b752f50-0252-35f9-a28c-95091202575a | -14.06818 | -45.62864 | 2026-09-11 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da52b2cc-5a89-34c2-aa58-81de1d2ec43c | -16.51421 | -41.6255 | 2026-09-11 03:49:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 905e1325-4f42-341e-b7e2-b76c476670e4 | -10.05402 | -46.26952 | 2026-09-11 03:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7b1784-a5ff-3f7a-a5e4-970fc712df86 | -10.7481 | -45.91798 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f63f4c-21bb-3f6b-80da-df394a97e2ae | -9.90601 | -45.90546 | 2026-09-11 03:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15a45871-6fc6-381b-a318-bd4d2815b8b5 | -10.78057 | -45.9481 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b6ca6c1-f1b6-3d22-be71-e2ef2484ba2d | -4.77607 | -46.49508 | 2026-09-11 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c843582-05b9-3e9a-9c36-81f09dece9c6 | -14.61747 | -48.84991 | 2026-09-11 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26e9bf5c-06e2-340d-b201-b9b45b470d3b | -9.60361 | -46.78108 | 2026-09-11 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d35286fb-2901-3e11-86ac-a25ce4cf7531 | -10.75389 | -45.92405 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94f3c6b9-654b-390d-a94f-52648611fea8 | -12.3493 | -48.20089 | 2026-09-11 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af490d20-a697-3f8e-8730-d2285543ebab | -14.06894 | -45.62488 | 2026-09-11 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f61bca54-2b40-3f0b-ba11-8e714be66ee6 | -10.98099 | -47.88573 | 2026-09-11 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2000aa8-690e-35a3-a252-59ccda6b9010 | -10.98218 | -47.88688 | 2026-09-11 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc95596c-fe8f-32eb-b6f1-d4e454b3e62f | -11.56775 | -40.07095 | 2026-09-11 03:49:00 | NPP-375D | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 55f65147-39b6-3185-b2cd-53ba61e6dafa | -10.60022 | -45.22425 | 2026-09-11 03:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2673bbdb-b6fd-3a4d-95b1-33e30b801353 | -10.35952 | -48.14289 | 2026-09-11 03:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 334b0ee8-fb0c-3cae-9b5a-0eb7ed4b7f39 | -9.60448 | -46.78387 | 2026-09-11 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e877906c-2fb9-3cc5-b1fc-472db3a25678 | -10.21844 | -45.21916 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21210f81-c962-3a01-bb87-7cccfa32f0d1 | -10.22034 | -45.21692 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f0d760d-2c5e-3db9-b644-4f704ca08b42 | -14.65796 | -44.12264 | 2026-09-11 03:49:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cb33aeda-995d-33c0-9d68-e6b5ca0616be | -9.60556 | -46.77828 | 2026-09-11 03:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d33a1dea-5084-3bdb-81e7-14f745441ea9 | -10.48366 | -48.64964 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2462c391-23af-30a8-9c53-afabb2a3289d | -10.21958 | -45.2209 | 2026-09-11 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6181394-4508-32a5-8b17-86a40c06ac2f | -6.59611 | -39.06415 | 2026-09-11 03:49:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5255fc4c-3f45-37c5-a3cd-e48b9c36ebb4 | -6.17448 | -35.22879 | 2026-09-11 03:49:00 | NPP-375D | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed510939-4812-35e3-b464-3047762761a5 | -14.57989 | -48.86079 | 2026-09-11 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b937600-3ffe-336d-88d0-c9c185fa5b44 | -6.12717 | -35.2178 | 2026-09-11 03:49:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| aa1a79a5-5425-306d-a7d8-380ca6ff60e9 | -14.67785 | -42.84942 | 2026-09-11 03:49:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| abdb837c-138f-33a7-a625-b43b7c345435 | -10.60605 | -45.22528 | 2026-09-11 03:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b6fe9dd-9706-30c1-a48a-5188596bf5e1 | -4.95452 | -37.44334 | 2026-09-11 03:49:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4e50bd8-7adf-324f-bc47-032d0308bf77 | -12.24373 | -40.27454 | 2026-09-11 03:49:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bb3cca52-d055-32b9-bba2-85f6a5dbc0b2 | -14.58137 | -48.85407 | 2026-09-11 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9cca1ed0-0754-3564-a67a-2b92c06aeeee | -13.55477 | -44.17061 | 2026-09-11 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70f9d9d4-3096-3655-96c5-4c6b82407ada | -12.9983 | -44.11634 | 2026-09-11 03:49:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcb475b4-5a83-33d7-b228-95228e5844b5 | -9.1799 | -68.2194 | 2026-09-11 03:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a6ff975c-bf6b-3cf7-8aac-774352f39f57 | -18.0851 | -46.85627 | 2026-09-11 03:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ca35cc-63a1-3edd-9d7b-611515de133f | -18.86921 | -48.92887 | 2026-09-11 03:51:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fdcb8a7-729d-301d-b8d6-a87ac0e91809 | -18.08046 | -46.85049 | 2026-09-11 03:51:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0737caf-fb06-3c60-85cb-497eb24420e3 | -18.08596 | -46.85224 | 2026-09-11 03:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8a3b140-5f78-3c47-a41f-4774b35263c8 | -19.8719 | -42.63716 | 2026-09-11 03:51:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b2c2da41-9887-32a0-ac0b-20e1069bcf88 | -18.08288 | -46.85238 | 2026-09-11 03:51:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4020d6a2-9647-3a9b-a220-573e10ccc533 | -18.63942 | -43.22518 | 2026-09-11 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d40174d-4eb5-38c5-a9bf-6afd33dad2ed | -19.06622 | -43.07945 | 2026-09-11 03:51:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b1d96ca-7fb0-3fd8-8097-66a289f3ad1d | -18.08381 | -46.84816 | 2026-09-11 03:51:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d88607-ecf0-33da-ac96-dacf0f6c4c2f | -9.1799 | -68.2194 | 2026-09-11 04:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 28b4ea2c-2fdc-32ed-a399-fe64df29077b | 2.51326 | -50.84895 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65179978-f64b-3d65-86c1-08b42ac4b3ef | 2.51412 | -50.85489 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1309280d-43f5-3909-bff9-7e8171fb6110 | 2.515 | -50.86094 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9f58f97-251c-3340-b8b0-8743aef19619 | 2.51829 | -50.85626 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ce99c92-cdba-35df-bab5-1b4fab2af307 | 2.51738 | -50.85028 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ddc79bdf-e105-3fc0-b394-94b492f7b095 | 2.51158 | -50.85736 | 2026-09-11 04:04:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a911cba9-e823-3393-8a7d-8ee9dc9033cc | -4.7753 | -42.71929 | 2026-09-11 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
