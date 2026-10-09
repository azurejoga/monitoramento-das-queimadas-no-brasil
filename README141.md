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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33b48720-bc49-3ddc-af22-2361c8e4fa63 | -2.99496 | -57.75449 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0adfeb6-7e27-31cc-9bc4-bc70dce00f20 | -9.69456 | -58.09149 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d6a3e7-7559-33f2-b336-50635dd1ca4c | -5.68621 | -53.47291 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22fc845c-beee-3794-87c6-b4f2e5d61917 | -3.279 | -54.26804 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce595e7-d03b-3d59-91a9-a765e5321d5a | -2.85844 | -59.11054 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfbb8c64-e548-3ce9-8c34-12faeca0272d | -8.99506 | -45.91132 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05f679ed-32b6-3238-84ae-39afcf5b5910 | -3.58198 | -54.31457 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae08e10a-6334-38be-bf10-1d71f238adba | -3.06031 | -54.21499 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb1226f7-b2e8-372c-a93e-fe764253d9c6 | -3.31245 | -53.70516 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a9dd61-32bc-3337-8692-3f324892fd85 | -11.25185 | -45.25339 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6399202-a391-3922-96a2-210064114442 | -5.98092 | -55.35707 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93eb591f-7312-34c7-a9cf-5d8932065850 | -8.84164 | -61.46199 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe070945-beae-34ce-b6fa-cdb4ee0ab01e | -5.88469 | -43.42114 | 2026-10-09 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acb53f0d-6854-3239-a30d-5fe63711ba55 | -3.27392 | -54.05379 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 327d5d47-77b2-3e8b-8247-7c04714fcdf3 | -6.48646 | -55.30647 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d178bbd-585f-38f4-a725-064d18f64cf2 | -3.00377 | -53.91563 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d75b8af-7b27-35db-9059-e38f5bcd05fa | -3.08246 | -53.94292 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e53f748f-4839-395a-8ab8-2fca5d0dfdb0 | -5.7008 | -53.46801 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c65efa51-6e10-3239-b134-4c69c1a2a1e9 | -3.5056 | -59.27811 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67b144bf-3668-3b08-b021-384deef98ddb | -8.4934 | -54.62966 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6cd1be-ed26-38d7-a3b5-1a3b20f37108 | -4.52665 | -54.98535 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fae70f1a-6562-3036-a9d3-c4e573d8c335 | -3.12518 | -54.17287 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2704a7a2-b7e8-38fc-beb2-98765c5468b7 | -3.02125 | -57.78406 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb94a296-3a85-306f-8792-4a7e101f77d1 | -3.26982 | -54.05706 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7db9010f-ba0c-30b8-bd39-fee4099fb7f9 | -4.11283 | -54.62307 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9467c4d-1e59-32bb-84c1-8fa842b7b23c | -5.70359 | -53.47215 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e00cc460-27d3-3903-9175-adc135354ae0 | -5.88075 | -43.41077 | 2026-10-09 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1bc5314-2260-396b-888e-48321ba3526f | -7.08049 | -52.68296 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3894fcd2-5b98-370c-a336-968c9690749b | -3.29992 | -53.69544 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ffa76a8-ee72-3b01-bc27-b5e1aa284c35 | -3.793 | -59.37392 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d966a8c8-387d-38bb-92a2-9f3f07346c40 | -3.5822 | -52.6806 | 2026-10-09 05:04:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 701214cf-e1b1-37a1-8524-d35b424239f0 | -5.95818 | -46.38232 | 2026-10-09 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f62878d-35cc-37d1-a311-069a8ca1bb81 | -9.9074 | -44.78803 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb25805b-4744-36f1-b5fc-10710820f99e | -6.14615 | -52.64456 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1623383-3b9c-3e75-b6bc-555a4f98a276 | -5.09242 | -56.19648 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24df4675-a5a3-39dd-81de-18bc87e78f35 | -3.5726 | -54.48591 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4187a9f7-9621-37f4-82ca-f24969434489 | -3.1253 | -53.76432 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2b91775-4edb-3eb5-8349-9305748464d5 | -2.88429 | -54.18814 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef383bfd-fdeb-333f-bba7-4d3710680068 | -3.93974 | -56.02261 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bedb947d-0e16-390b-bf19-c8a3693a7aa8 | -5.70519 | -53.4901 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a579f8f-8f1a-36c8-9648-8c7c3867e242 | -11.19966 | -45.31248 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0309dced-2c40-3565-ac81-3171a29cb8d2 | -6.11093 | -55.72239 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc1f0d79-8e00-31ef-b9d4-2d50fc08897f | -2.94744 | -54.17818 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8f3de77-f06f-3e82-b7bd-8d1618e226ab | -9.90267 | -44.78419 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a04f938-5373-31b8-907a-d0c445f131af | -5.86046 | -53.45645 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba821c5d-27ac-3803-9a4d-af1fbc78e94f | -10.45831 | -47.86017 | 2026-10-09 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8682f2d-5361-343a-b245-3feb0cbf1845 | -9.21463 | -57.72651 | 2026-10-09 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45ed74d-0cc9-3757-9431-821d04d5461d | -2.6334 | -57.73808 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be167f2-beb1-36bf-98af-2e94271ab13b | -6.44822 | -52.7031 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc11371c-7be2-3e84-89f6-d47c80a0e5ac | -4.53796 | -54.24916 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f779a1-ffc6-3204-9526-9f20d27101d8 | -6.16378 | -44.86183 | 2026-10-09 05:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a65b39-9d38-3657-8fa6-0720cd2aa8a9 | -9.62978 | -48.88494 | 2026-10-09 05:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd8ef63-7d6d-34b9-9713-dc066e515302 | -3.25263 | -54.03092 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67d0790f-4620-38f8-907c-2712c70341bb | -2.99929 | -57.75521 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5f49f1f9-121c-3626-87bf-af50521c2482 | -4.12341 | -55.0307 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8142a98-356a-3e28-87ca-fd7964be0ec9 | -7.18027 | -44.28195 | 2026-10-09 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ee10aa4-79fd-30c2-9803-86094c77fc6f | -9.27832 | -47.42967 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 166f2d59-fef4-3009-b1f4-174f8e353663 | -3.30672 | -54.70378 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2638e48-6581-3b70-a3a7-61da07c961f1 | -3.60312 | -54.67299 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87773192-68ba-3d3b-8650-ba84d061e4ad | -5.87898 | -49.87476 | 2026-10-09 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7c5b40b-3e4c-3a14-afc4-b6584da006e8 | -4.28595 | -49.09066 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 71c64749-f15e-3e99-84ca-ede7e4486460 | -10.28289 | -47.82448 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc35b6c-310e-3197-94d7-05b9971ec006 | -8.43248 | -47.03087 | 2026-10-09 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b55f5b4f-5cbf-3b4a-9ac6-56c10333e516 | -6.00184 | -40.94812 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 07130cda-2c25-3de6-bd4f-bad81fbe5678 | -3.15551 | -59.08677 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c1b6a97-12cd-399c-ad0b-644bb4582eaf | -3.59808 | -61.61765 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 479524fa-5343-3188-a8c2-c84f1c0ff87c | -3.02395 | -54.10606 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 707e23e3-24fe-37ed-acf6-59ea40a9fcd3 | -3.59999 | -61.64066 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3020c8c8-fa67-3ce2-8dba-560bfb575185 | -2.56563 | -56.15355 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 576959cb-4ae8-3a76-947d-23926afc587c | -10.73868 | -52.02936 | 2026-10-09 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59fda650-f92b-3340-84d6-f68095a063a8 | -3.5618 | -54.66791 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1764588-e21d-3f47-8b27-11ccf0d22f53 | -6.18222 | -55.27166 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e262dc19-e503-324f-a855-d3cf52cd0a7d | -7.0877 | -52.68054 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a0267c-ee8d-34ec-aded-82adf287b58b | -3.05769 | -59.08842 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe128a39-d81c-343f-b20c-3e032e4ad128 | -3.42008 | -59.58025 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfeeca2f-0d85-3991-b59d-e46a1ad0ae2a | -4.12703 | -55.03121 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f41d7807-ce7e-37c7-988e-29c44086eded | -4.79706 | -56.13988 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90ccb075-5820-35fb-9acd-42118fe53bde | -2.87314 | -54.19033 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40cc2b36-4029-3620-805e-080a17e64f8d | -4.69494 | -56.22163 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248d4da0-6059-3f00-87bf-13b3af132ddb | -3.00673 | -54.0766 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f2be08d-123b-33c7-8ef8-cbcf6cbd949a | -6.20009 | -53.14952 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e1e280-ed71-3227-8ccf-656ae6bf7510 | -9.89636 | -44.79255 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 467f7e56-868b-3ecd-9d4e-62778d6c4827 | -6.84862 | -59.3984 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c97c69a8-85b3-369c-8769-b03a59b3ab68 | -2.87541 | -54.19868 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05da2a12-ef80-3e2d-b691-f156e81b8f4c | -11.01612 | -45.42881 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| a15dac7b-ed94-3990-a447-ea55632227ee | -8.13842 | -49.43397 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57d9fe35-ddd0-3919-96cb-23c7162126a9 | -3.50056 | -54.61685 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a77c926-4742-3392-b4ee-00aaa481ba00 | -6.22764 | -52.79288 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60824c12-7f8a-3cd5-8932-7c13fddccc89 | -3.30996 | -54.05173 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bea1120-4068-32d0-b283-28b26ff9758e | -3.55083 | -54.69082 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c7d3185-7d13-3527-896c-1abebd5b1a68 | -11.09277 | -43.99334 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 067496ea-c7c4-369b-a8c8-9ff6d63a8299 | -5.69184 | -53.4593 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 532a089f-f16f-3cce-9cee-ac1691e88638 | -12.00358 | -43.47559 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efac6a50-b068-3ddf-8ace-360dcca3798b | -3.02134 | -54.078 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d45833cb-d3a8-34fe-9adc-392064fd6016 | -3.02725 | -57.85717 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ed7915-fe44-3a7f-8572-edd03feb6011 | -9.87268 | -47.47235 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81db38bd-283e-39d7-b73d-5bc5892efc17 | -3.07308 | -53.95694 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af86e475-f030-3145-a1e4-ad1660ff4d35 | -9.07803 | -45.10865 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b3eeac2-3479-3431-8b96-15389928351b | -6.67932 | -63.02423 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2789a56f-abc7-3771-9172-aec6e867a761 | -3.40759 | -59.59476 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README142.md)
