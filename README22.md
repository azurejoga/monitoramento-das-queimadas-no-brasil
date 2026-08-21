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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51f7a68a-d697-3ed8-bdb0-b9b02266a2b6 | -7.35256 | -45.80844 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fedfb8e7-7362-356b-a1e7-f861f1375069 | -7.77598 | -46.04519 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1245dd2e-1c1c-331c-99ca-2371503f11a3 | -11.48846 | -45.10682 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8ebe89b-2283-3968-982b-718c3159d02f | -7.37174 | -45.81123 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 92272c09-1bf2-3f40-b0ce-16d6e60ab504 | -6.34297 | -44.08229 | 2026-08-21 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| afd9d2d6-42e9-3151-96e3-f3740c4d25e4 | -11.48927 | -45.09052 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea450b8-0962-3b53-bd24-0fcba96385e6 | -7.35007 | -45.82142 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0ddc3ea2-61e5-3b67-a83d-af89e14ab0dd | -7.36767 | -45.80466 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f3447dbd-c309-3911-8552-114c7f6ff322 | -11.32756 | -45.0204 | 2026-08-21 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e6424e3-b916-3a59-b7f8-3b30c707408d | -7.37338 | -45.81249 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 56a00264-2ed7-3434-98c4-4c3ce3d51138 | -6.87525 | -43.73528 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 02d76b1c-a961-3c75-b8d0-fa540bbb3fbd | -7.36351 | -45.81644 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c55fe078-b372-37a2-bde2-abc768d29aff | -6.27307 | -43.27849 | 2026-08-21 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbcd57f4-94f1-3b87-9386-3a6c67c4a6e3 | -7.37302 | -45.80475 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| cff633c6-92dc-3539-9695-53c3be7c2945 | -7.36519 | -45.81768 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3f2a8639-8740-304a-881c-b2602065c44c | -7.37462 | -45.80597 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 14b539eb-b795-3c89-8139-f8d10da97a0b | -11.32885 | -45.014 | 2026-08-21 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f7433ac-f834-3611-be58-67f327f7f41c | -6.8797 | -43.74584 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7372795c-cddd-3467-b6b3-4622c0873fd0 | -6.47643 | -43.54419 | 2026-08-21 03:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0b23f67-432c-3568-abd0-4c8abe2502db | -7.35701 | -45.82283 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e59cb05a-fee3-38a0-ac85-50485f232cec | -10.72512 | -44.78217 | 2026-08-21 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1ef2e53-9563-3493-8656-b9deb5b51e05 | -11.49244 | -45.10667 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e12227ea-818f-3cde-8683-2f4f0c968d8b | -6.2739 | -43.27383 | 2026-08-21 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b002ddf-33fb-3c87-aef1-9b002b5851aa | -14.45623 | -45.61561 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d624bd21-9657-3dd9-b437-9b1411999c21 | -18.10664 | -40.89035 | 2026-08-21 03:45:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a64583ac-d892-3479-bc57-2f1d40ea9bc7 | -19.33896 | -44.15359 | 2026-08-21 03:45:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6086f4f-9cdc-3f87-8176-2b4d2334eab1 | -18.033 | -44.61673 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5da3ced-63b8-3bde-a5e5-0278cae488f3 | -19.84173 | -43.16454 | 2026-08-21 03:45:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 940a2ae0-9960-3e96-a32b-0a34f3c133f0 | -15.16463 | -48.78868 | 2026-08-21 03:45:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41342d1e-9125-3a91-bf5b-687373636bc4 | -18.06154 | -44.42703 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2ab884-2cca-33fe-afa4-6118732f6f09 | -18.88047 | -41.09052 | 2026-08-21 03:45:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5af3d5ec-c807-3044-b701-d05c69779d20 | -14.45117 | -45.60945 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f198762-e9ff-327d-949e-e0ce03376176 | -14.45424 | -45.62509 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e08fcf91-845f-309b-ae76-be9d8b8a1190 | -17.334 | -43.62411 | 2026-08-21 03:45:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fa44e53-8958-34ab-aace-0353c89eda9b | -17.96096 | -44.44407 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52c3bd1d-916b-3305-9a08-565b1520538f | -17.95394 | -44.39798 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d076d6-188c-3272-a1e4-e13897954890 | -18.87379 | -42.02782 | 2026-08-21 03:45:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c8f73537-5ef8-3613-9bfe-93b58ad7fe7f | -19.85959 | -41.086 | 2026-08-21 03:45:00 | NPP-375D | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31261607-10cf-3a04-8467-4091ae1c2d2d | -13.44147 | -43.84161 | 2026-08-21 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6b59ecac-fc12-3688-aa8e-647eaeb9cd4e | -15.44128 | -41.38571 | 2026-08-21 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 60c87610-9d10-3fc2-913e-a9a32901a5f7 | -15.71956 | -47.79213 | 2026-08-21 03:45:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72fc6f9d-c7a9-3fda-ae1a-85cd3f9678e5 | -15.16841 | -48.78027 | 2026-08-21 03:45:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037f88fa-846b-3c78-9958-4cfa251e7d83 | -17.94866 | -44.39677 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1bd28d-5bcf-38d1-8741-63487aae56bd | -14.44917 | -45.61895 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7630a2fa-2d5e-386f-9d1b-582097160b76 | -19.85186 | -43.87196 | 2026-08-21 03:45:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b5c3bafd-776b-353a-803c-ebe6c41afedf | -19.41485 | -44.34243 | 2026-08-21 03:45:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e10db4d-b82e-3e79-9c5f-b5b1edc75cf6 | -18.9787 | -47.03723 | 2026-08-21 03:45:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce794d4f-71b3-3041-b0d7-25144f2e151d | -18.87554 | -42.04274 | 2026-08-21 03:45:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b7ebcc6e-4dce-3742-ba07-d30c434f516b | -18.023 | -44.61094 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb67b8f3-4feb-35d5-86fb-f922afed3abf | -12.43762 | -43.40561 | 2026-08-21 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 544bde3a-a006-33d3-8a07-4bd1e44d2625 | -18.87774 | -41.08764 | 2026-08-21 03:45:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6ec0bff-61c6-3559-93aa-e0964368fe85 | -18.02763 | -44.61559 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5012b33e-c6ed-3e87-afff-283f933e67c9 | -19.85065 | -43.87768 | 2026-08-21 03:45:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f6b676bb-86d5-35b4-bca6-c02ee09ffaaa | -18.10585 | -40.89447 | 2026-08-21 03:45:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42de8092-e5ae-3341-8e79-7698ee0ef65d | -18.06441 | -44.41331 | 2026-08-21 03:45:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd97bed9-2e37-33da-b628-abaa0c440609 | -18.05922 | -44.41166 | 2026-08-21 03:45:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5817d3ee-fd29-3c21-929b-5274cd91a40f | -19.85618 | -43.87653 | 2026-08-21 03:45:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 27ae6da9-2fc1-3773-b8c3-7cccbc9f83d0 | -13.15904 | -42.41387 | 2026-08-21 03:45:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1677eb80-f0c5-3803-9835-c86a3830e8e1 | -15.16651 | -48.78838 | 2026-08-21 03:45:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97d3c20e-3e0c-3130-8851-ce792120df85 | -12.43906 | -43.39822 | 2026-08-21 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c9f6fd3-fe24-3f38-a17c-dc3a64568e5e | -18.65438 | -43.17921 | 2026-08-21 03:45:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d94caeca-e09c-30a8-8394-76c3d96d64eb | -15.44584 | -41.38673 | 2026-08-21 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 79f30400-396e-3099-b4a2-db38683604e5 | -18.87289 | -42.03242 | 2026-08-21 03:45:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7f9cb310-5b07-3381-a0c5-31fee2995ecd | -16.91341 | -39.43398 | 2026-08-21 03:45:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 641845c6-b1bc-35dc-94cd-8797353ae566 | -13.15845 | -42.41689 | 2026-08-21 03:45:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0c1630af-2989-3ce9-b6bd-0fbafa1e2400 | -13.78708 | -43.18293 | 2026-08-21 03:45:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5e07904d-c433-3f90-8913-4b54b51f733a | -17.33333 | -43.62737 | 2026-08-21 03:45:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d684d24-9bda-3699-af48-6464a86a8a4b | -12.43834 | -43.40191 | 2026-08-21 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afcffd15-9e3e-3621-8936-cc1a91af9244 | -18.11712 | -43.73888 | 2026-08-21 03:45:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a93af89-d79a-33e0-9e4c-a165d52a1a48 | -14.45932 | -45.63125 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7ea8a7d-8487-3d4f-96c1-32709c3ff108 | -16.21558 | -43.50138 | 2026-08-21 03:45:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3588eb38-a89c-373d-8308-68a3d36c484e | -18.05633 | -44.42548 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 907a97cb-60a6-32cb-b2c5-ce792f771349 | -12.44311 | -43.40683 | 2026-08-21 03:45:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe50601d-463e-3029-8901-decfb1bfd59f | -15.71145 | -47.79669 | 2026-08-21 03:45:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2987530-62b3-3f30-ad9e-a46e6a22606c | -12.50124 | -47.85418 | 2026-08-21 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7df90c1b-e5da-3856-85fc-b2e0449f352b | -18.65909 | -43.58738 | 2026-08-21 03:45:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c40da801-b319-3c86-978f-f155eed23358 | -18.0585 | -44.41511 | 2026-08-21 03:45:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ffa84a5-4369-35c2-8625-968147caa4d7 | -19.8601 | -41.08912 | 2026-08-21 03:45:00 | NPP-375D | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3706334d-f810-34a6-9a2c-40c29da2fefc | -14.45017 | -45.61417 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 415d1d03-fd00-3cb8-86ac-c4b589313f59 | -12.50293 | -47.84655 | 2026-08-21 03:45:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 732b4c58-6406-3a9f-bc98-1e3af3d51d65 | -14.72697 | -47.13815 | 2026-08-21 03:45:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8e7b7f-1277-3bd8-b0b8-69ff55c222aa | -18.97976 | -47.0326 | 2026-08-21 03:45:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed3432e8-b608-3070-85c8-0f283863df19 | -18.88128 | -41.08635 | 2026-08-21 03:45:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2713dff0-83cc-33ae-a69e-2bc68efe5c5b | -14.46031 | -45.62656 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f9bc17b-4d06-3d4b-b68b-fc659e3fe835 | -14.72564 | -47.14417 | 2026-08-21 03:45:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eccb7632-3570-392d-adfe-5f66efb2c920 | -18.03661 | -46.47006 | 2026-08-21 03:45:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9274222a-7e86-31e5-8d2f-fb09858f4a83 | -18.88197 | -41.08846 | 2026-08-21 03:45:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e3b2f07f-1053-32af-b25b-d26fd2ffcc4e | -19.86086 | -41.08524 | 2026-08-21 03:45:00 | NPP-375D | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5c8636d-96ab-3846-bdbd-3157f7b75d22 | -18.0245 | -44.60379 | 2026-08-21 03:45:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c26f13a4-65a9-3ef2-be3c-66c65dea8bbc | -19.33829 | -44.15684 | 2026-08-21 03:45:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28ad4dec-7d72-3615-862a-0c939096ba03 | -15.44035 | -41.39064 | 2026-08-21 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2a5d82be-eb90-3fac-94ef-67ea3564c69e | -19.85564 | -43.87851 | 2026-08-21 03:45:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dd7723a6-405d-33a4-952d-2a5a82374975 | -18.02838 | -44.61202 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fea116c-1e23-3e0f-aabc-bf86c612b053 | -14.71903 | -47.14266 | 2026-08-21 03:45:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6786e896-8547-3fb2-bc24-466f1f0bc936 | -18.03373 | -44.61325 | 2026-08-21 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0a70597-8eec-3108-aa40-9c69be0b3974 | -14.45723 | -45.61091 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a6c4dd9-a4eb-3c7b-8e22-82bc9de00b57 | -18.03168 | -46.46389 | 2026-08-21 03:45:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2374cc04-2c70-3864-94b7-3569a8cc6582 | -13.15394 | -42.41283 | 2026-08-21 03:45:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f569fa8f-5cf3-3d1d-9d99-c9e8085431c9 | -14.7224 | -47.1425 | 2026-08-21 03:45:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0efa7a65-6b79-3d08-8d67-01a4af7da993 | -13.44227 | -43.83759 | 2026-08-21 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README23.md)
