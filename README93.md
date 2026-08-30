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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e9c3f4f-4fbf-318e-a505-a96e32a98062 | -10.8253 | -45.3152 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 242aeccc-f1aa-32a7-9a84-94636a1c1082 | -11.2314 | -54.0164 | 2026-08-30 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 219.2 |
| 8d0e06a2-8e9c-3104-82ba-8c817f034c0f | -7.9907 | -46.5177 | 2026-08-30 15:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| f224ad30-dbff-3c27-8afa-f3c95e777b09 | -7.9422 | -44.277 | 2026-08-30 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 5ec16c63-1b63-3905-99b6-85a6148eff8d | -6.861 | -41.6772 | 2026-08-30 15:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 300.8 |
| 6efbdfdd-2ebd-3579-b123-e15766ca60e4 | -11.2443 | -45.3497 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.1 |
| 64485c9e-ff54-3154-8267-a79c8fafba4b | -12.9221 | -45.8582 | 2026-08-30 15:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b1c415cd-cd8e-3dc2-a918-c00977ee93dc | -11.6243 | -50.1998 | 2026-08-30 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9ae7859f-c90f-34c6-a96d-33343aa41c53 | -11.2298 | -45.0759 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 223172ee-131d-34b1-b438-9c781f6fa5ac | -8.1531 | -45.5131 | 2026-08-30 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6288b638-33fe-39ca-9b38-a089102888cb | -8.615 | -54.8348 | 2026-08-30 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 79eef835-caa5-3fc0-b0b2-5b9da775c7f1 | -6.8598 | -58.9545 | 2026-08-30 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 133ffa09-b438-3d1e-8399-3cb2fd8ec5ce | -7.1309 | -42.7945 | 2026-08-30 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 89c57d0f-d644-3459-ba80-8672be6c065d | -15.2283 | -57.6517 | 2026-08-30 15:30:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5513a3fc-4fdc-3e6a-951b-97fbb8313168 | -11.6247 | -50.1783 | 2026-08-30 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| dc848c13-4556-3402-902e-76e5a5ea9ab4 | -7.1312 | -42.7708 | 2026-08-30 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 538.8 |
| b0dba144-dba8-3326-878a-b3935d57ade5 | -14.5032 | -52.17 | 2026-08-30 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bce12f31-01a9-34c2-9f94-64797ceea016 | -5.9635 | -57.6899 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e28531cd-e7f9-38bb-bbea-8da81d102ac8 | -14.3523 | -53.1191 | 2026-08-30 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6ec9e066-9191-3bc4-8ae9-6c46cc2367b8 | -8.2229 | -54.9412 | 2026-08-30 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f40ee9f8-2a73-30a0-bf61-d5085835bb0a | -10.4774 | -59.6207 | 2026-08-30 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 7087e4d1-587e-372b-8216-93e87b07b2bc | -11.6396 | -50.4553 | 2026-08-30 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 066f08f9-921c-34d3-a6de-62bf74c10f57 | -9.9284 | -60.4856 | 2026-08-30 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| cb617c1b-e8c7-3823-b9c3-b09fc303c54e | -7.9611 | -44.275 | 2026-08-30 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 1507cc5f-6150-3c0d-9809-bc9be4153bcf | -14.4838 | -52.1725 | 2026-08-30 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 6b2e83c6-e235-32bc-b763-306949ec1a47 | -10.8987 | -50.5372 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 60c6584d-14dd-30cc-8c0a-37561e2be1f3 | -6.9363 | -55.6958 | 2026-08-30 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a720de13-1f6c-3f37-83e0-aa5557112653 | -10.7409 | -54.0196 | 2026-08-30 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 42675667-b461-3b9c-84c2-2db6c16b9ce9 | -10.5596 | -50.4449 | 2026-08-30 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| fdda9a45-9456-3d2d-8409-e0b1bea13c4c | -5.9749 | -55.722 | 2026-08-30 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a45d4b31-c23b-374a-8f23-9e91a5b06d9f | -7.9425 | -44.2538 | 2026-08-30 15:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 24526d71-7b34-3e75-809f-1c9e329d3ca1 | -10.7839 | -50.6346 | 2026-08-30 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e9dcdbfa-1226-3502-9ad9-e1ea0074102d | -10.8046 | -50.5046 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 97ac1586-ce76-3e8d-9f76-601334f33e24 | -5.871 | -57.7715 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 47a1485c-b088-3e48-974e-0d9de11ac27a | -6.7884 | -55.6635 | 2026-08-30 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c03ab4d3-d8d2-382a-8817-ae918800e76a | -10.9177 | -50.5352 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d856fbc8-fac4-3379-8f58-8717c5bffcec | -11.0057 | -49.6677 | 2026-08-30 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0f0d2741-b29d-3363-bce8-c0acb50f0e9d | -8.5925 | -66.9564 | 2026-08-30 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| b844db34-85d6-3949-8f15-47de25dd4917 | -6.8568 | -59.4757 | 2026-08-30 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 2563fe1a-f5dc-3fd5-9885-b9c07102c3ab | -6.7883 | -55.6834 | 2026-08-30 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5e059843-45f2-3a03-b167-2a21de74e679 | -10.8798 | -50.5392 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 17a8e936-2fb3-3893-96e2-82d3b4afba50 | -11.0434 | -49.6851 | 2026-08-30 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7d681762-ac01-372d-b5ae-81cbfa0376db | -5.9819 | -57.6892 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 93562018-1027-339a-bd78-9ddb989c1b04 | -5.8874 | -52.1271 | 2026-08-30 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8e577f71-4eff-3a60-8cf5-02a4fd38590d | -9.1712 | -59.5987 | 2026-08-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 201bb8a2-a51f-3151-9332-dada87e43269 | -9.9282 | -60.5049 | 2026-08-30 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 175.9 |
| c3d48cad-676b-3e9a-a84f-b2542cec2f1b | -7.3294 | -55.1555 | 2026-08-30 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 244d3382-7636-3d4f-9061-8315143b96be | -10.7647 | -50.6579 | 2026-08-30 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 33b05951-3558-35ee-aa31-c095fe7112d2 | -8.574 | -66.9569 | 2026-08-30 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 619f090f-fa65-3881-ab14-e8e45b00deae | -5.9819 | -57.6892 | 2026-08-30 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9a8768be-95a5-342c-bcdc-d37597f62a72 | -11.0244 | -49.6872 | 2026-08-30 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3910c030-ac68-32ec-afd1-2fa9c4724277 | -10.3205 | -49.9567 | 2026-08-30 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5b621022-096e-348f-865b-2866104467b3 | -7.6963 | -61.1664 | 2026-08-30 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7c2d1be6-7bae-33ee-8da3-d4f19a74073d | -11.1807 | -55.1024 | 2026-08-30 15:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 4f2a89cb-ef4d-39ca-b683-94ff86016be0 | -10.3526 | -50.3809 | 2026-08-30 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| fa62d5fc-11d4-3b88-ad62-c9205dfe7d4d | -12.9216 | -45.8812 | 2026-08-30 15:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 739e9744-244b-3794-aa58-e816a2eb2242 | -5.9636 | -57.6704 | 2026-08-30 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9f811d3e-f457-3ffb-90ac-e31ac5f892e8 | -7.7863 | -61.5818 | 2026-08-30 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c6d01894-d22b-3e49-93f9-b9bdf2c68b6d | -11.2298 | -45.0759 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 04427336-2f81-393b-a0ec-7cb7b4c786b8 | -10.4794 | -64.5012 | 2026-08-30 15:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d9e78258-56c6-3e57-a72a-8f13548d3d87 | -10.7647 | -50.6579 | 2026-08-30 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b2ef0c95-04a8-37fb-b027-44103a144332 | -11.0627 | -47.1385 | 2026-08-30 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 266.8 |
| dd1b62a3-7847-31a0-b39d-2cd4a1a08af2 | -10.9559 | -50.5098 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b82e3484-02cb-3be0-a564-f6dba69a9fa5 | -7.5272 | -44.3413 | 2026-08-30 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e283afc4-5259-3774-8171-35bd93bb9c61 | -15.4601 | -52.806 | 2026-08-30 15:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 8ff0ffbe-bd8d-324c-99de-416fdec1e72b | -10.5644 | -46.1683 | 2026-08-30 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 80f7fb6e-99fd-3fb6-8ba3-8b157ee8960a | -10.8993 | -50.4945 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 95147262-a953-3363-8156-d8ac39fefea0 | -3.8947 | -60.9399 | 2026-08-30 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 026b5ce2-5bea-3bfe-ac73-2923f6b8784a | -6.7884 | -55.6635 | 2026-08-30 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 79e44ff0-e00d-3292-b30a-b3e6611cec6e | -7.917 | -61.3481 | 2026-08-30 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7df2ba12-6e9d-33f3-8de3-070069b9cde1 | -10.8253 | -45.3152 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d8756828-96b7-36e0-bac6-17c58b1d6de7 | -10.5779 | -50.4857 | 2026-08-30 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 68529e91-78fd-371b-bc1f-bf8b072a1cb9 | -10.937 | -50.5118 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f4f58505-d15e-364b-8b96-a20bcc1446e2 | -3.4943 | -54.6567 | 2026-08-30 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| dfdf7ab8-219d-3dc6-8985-e1a02272aa81 | -8.1534 | -45.4904 | 2026-08-30 15:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 35794628-d250-376f-aa84-47741cab6487 | -6.0 | -45.0889 | 2026-08-30 15:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ed4006ab-3c1b-3484-9432-1f527cc496f3 | -7.3479 | -55.1544 | 2026-08-30 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| d4686b2e-7476-3dc4-b5a0-6466ab1584ea | -11.0054 | -49.6893 | 2026-08-30 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a1697f3e-b628-371c-96b0-39d112bb3211 | -6.5232 | -51.4488 | 2026-08-30 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e5359b3e-ff83-3fbc-8e3c-917f045ba48d | -8.231 | -61.4304 | 2026-08-30 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e00e38d9-f381-3054-bbc8-14d454705faf | -15.2283 | -57.6517 | 2026-08-30 15:40:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 63746d9d-7345-3742-98d6-42c8dd81b98a | -7.1121 | -42.7963 | 2026-08-30 15:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 971e3590-b2cb-3c0d-9031-f9a8f37f8ad2 | -10.1538 | -45.6982 | 2026-08-30 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 3d000f1b-bc19-3b66-a027-d77a521064b5 | -5.982 | -57.6697 | 2026-08-30 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f0103544-f4d9-3488-b37a-d526dc61826c | -10.3337 | -50.3829 | 2026-08-30 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d95b246c-01e7-3ca1-85f6-3dfd55e28718 | -8.1531 | -45.5131 | 2026-08-30 15:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 773cdf33-3bd9-33de-9dde-fa1f10584bd3 | -6.5234 | -51.4279 | 2026-08-30 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| acd0c31b-bb45-364e-8f0f-a5ebf11568df | -8.631 | -66.5473 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 66489f3f-0863-318e-9dbb-5e9368e6daf8 | -10.7867 | -45.3433 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 6d6fe3cc-4230-38c9-87ef-66476a50230b | -7.2932 | -60.6096 | 2026-08-30 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b8f88b0b-1339-379a-9b2a-db06e406fa6d | -7.9907 | -46.5177 | 2026-08-30 15:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| b9a97b3d-46c0-3831-bb6e-813e434eef42 | -10.8804 | -50.4965 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1f6c2e49-7d29-3552-8a30-b28544b36395 | -10.918 | -50.5138 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5d0fb5b6-b588-3d5c-8502-772b9d194646 | -8.574 | -66.9569 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 9be3730b-766f-37e1-94e3-706c62c7561c | -11.1634 | -50.5727 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5afd1588-8ad0-374e-bb35-c9e8496670d0 | -12.9221 | -45.8582 | 2026-08-30 15:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| dfa6dc75-2883-302b-ab11-545c2a9e9eaf | -9.9284 | -60.4856 | 2026-08-30 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 904b27ad-5aff-386a-a7c8-32b681609d78 | -4.9605 | -55.8226 | 2026-08-30 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c66e1ccf-629b-382d-ac8a-9127d0a5596c | -11.1631 | -50.594 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 182fcdbc-5361-342b-a92a-dfed8bd9a156 | -11.2125 | -54.0181 | 2026-08-30 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |


[Clique aqui para ver as próximas entradas](README94.md)
