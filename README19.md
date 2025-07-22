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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0b84172-f472-3bbb-89f5-8ae2e30a8fff | -11.94401 | -63.85357 | 2025-07-22 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9dc5dfa-ba6c-3c0c-ad31-0436e8fc50cb | -12.50188 | -57.766 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa33f06a-ed42-324e-b311-a0e0822e27b7 | -10.051 | -59.0981 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae973d18-79ae-3c94-bd70-0cac164d016d | -7.23196 | -60.19648 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed75883-3d60-3fdc-95f7-91dd900cb749 | -11.23598 | -50.36659 | 2025-07-22 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78592ce2-0521-3040-a67f-6f681f92ae4b | -11.72798 | -48.18308 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8afb7602-bc77-3a72-8393-f69387288970 | -11.19503 | -48.62141 | 2025-07-22 05:21:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e9af8fa-e9c6-39e0-a8c7-57eeab0f250b | -7.2637 | -60.17937 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 755a3733-0b43-3170-836d-3ef4ab358d80 | -7.25921 | -60.18591 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1fe9ed32-2bbf-3f66-9203-56e40fc02906 | -14.77084 | -48.25861 | 2025-07-22 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f88a142-01df-32b1-ad2c-c4082872f9e5 | -14.39305 | -47.76286 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0d995323-aa20-37b7-8aad-7b4231e5b9d5 | -11.18886 | -48.62062 | 2025-07-22 05:21:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00adb076-d670-3bcf-a647-89b8e9a3d0db | -7.29001 | -60.16539 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfdd0fb7-e5bc-36cb-959a-6be9556ccb7b | -11.18944 | -48.61577 | 2025-07-22 05:21:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f83e4529-d761-3c27-9bce-c19a62ff1f9c | -7.26648 | -60.18344 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 721c6bc2-ff17-356b-89ba-8ae4f9e36a04 | -14.38622 | -47.76282 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac0ceaaf-659e-397d-8e4f-6374c80b63e4 | -7.27097 | -60.17689 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8224ae8c-3f67-3aa6-9b51-0bfa19169e64 | -9.38736 | -57.85635 | 2025-07-22 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffca9095-8a87-392f-9ad3-311cf1daef5e | -10.29383 | -60.54094 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4665eb5f-7f2a-3451-9b80-1cf2d14c89da | -7.27154 | -60.17334 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27084984-1a68-34a5-b8a9-c0c8ac578720 | -7.23401 | -60.19284 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1e1684-23c8-33c5-8502-07fb16e154ae | -7.24857 | -60.18787 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b90c6f3-988a-31e7-a130-36f5a0c226fa | -7.27824 | -60.17443 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e997ef5f-04d0-3c16-9b74-e59820ad7ff9 | -14.38222 | -47.76131 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 39411558-cc07-3161-bb89-0bcc2ab935a6 | -8.96095 | -62.24142 | 2025-07-22 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1542d93-a01f-3a6b-847e-483f6b39616a | -11.94225 | -63.85205 | 2025-07-22 05:21:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e44b7c7a-6521-3fe8-b643-460d13ac0d9f | -9.69105 | -56.11006 | 2025-07-22 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 656f53cc-20f0-31f2-b9e8-250d2d4f7ece | -10.23043 | -48.06002 | 2025-07-22 05:21:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8cd5d2f-71b7-31ca-a55e-8b5d2b09e9f7 | -7.25978 | -60.18237 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c679586-0052-3edb-b274-d009de0e0aaf | -14.90475 | -59.45652 | 2025-07-22 05:23:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e8bf94-975d-3cc5-822a-108b6931d444 | -17.59858 | -50.64449 | 2025-07-22 05:23:00 | NPP-375D | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd99533f-be29-3630-bc8b-2dd6cf1111e7 | -21.28838 | -56.20513 | 2025-07-22 05:23:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbc4f144-e2bf-3c1a-b562-d5bce2d5ad29 | -17.02242 | -47.19848 | 2025-07-22 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2364c573-081d-35b4-a9f6-e73800d650a0 | -21.68252 | -57.39982 | 2025-07-22 05:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b580fde-a841-3192-9056-01e4de78d47c | -21.02224 | -56.00286 | 2025-07-22 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68ca287a-b079-3da3-b0a3-cea765ca74ae | -22.17342 | -52.70001 | 2025-07-22 05:23:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28f5d698-cf13-3664-a3fc-32ff85f2be00 | -22.48256 | -51.52826 | 2025-07-22 05:23:00 | NPP-375D | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b729ee68-ab26-3e8e-ad98-1209c17c0c75 | -20.64014 | -56.55045 | 2025-07-22 05:23:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b909ee65-0e75-3c8d-8099-63fac2517d1f | -17.02373 | -47.20841 | 2025-07-22 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 048eaeae-d7b8-3159-96a7-7afac7039326 | -21.0174 | -56.00658 | 2025-07-22 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| defaaa78-adb9-359a-aa99-b762163a3c6f | -22.48217 | -51.53265 | 2025-07-22 05:23:00 | NPP-375D | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77afb850-d43b-3031-9a21-bd125cc1b9d6 | -21.04167 | -55.98756 | 2025-07-22 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06dd7ab6-d4d0-3368-9ee4-837e670cabe1 | -17.59813 | -50.64884 | 2025-07-22 05:23:00 | NPP-375D | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab10d9c-5036-3687-b867-35844b30e975 | -21.6857 | -57.34397 | 2025-07-22 05:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75702a3a-58eb-3708-84cb-56783f17ecff | -17.0217 | -47.20635 | 2025-07-22 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6710a1c0-bd4f-3285-a330-535e3788cf87 | -22.17416 | -52.69241 | 2025-07-22 05:23:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a15edfe9-1762-3646-83b8-1abc59f7b856 | -22.1687 | -52.69196 | 2025-07-22 05:23:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 81e110d7-7483-32a8-aa39-c0b0196c0152 | -21.68323 | -57.39438 | 2025-07-22 05:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 742f029c-aa56-3a0c-aeb9-b82071c8692d | -21.01791 | -56.00223 | 2025-07-22 05:23:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbefe84b-e973-3f9b-8b50-c8d7bd0e8b69 | -17.0244 | -47.20051 | 2025-07-22 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 211184b6-80fe-32ea-ba32-d9ea9c198205 | -11.7317 | -48.1849 | 2025-07-22 05:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 984b36a2-a706-3faf-9aba-7d6026a275cd | -8.5211 | -43.3063 | 2025-07-22 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d2bf9499-be27-3585-ba58-accabdc78c2c | -8.5211 | -43.3063 | 2025-07-22 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3818830d-2d45-32aa-831b-174207f5ec19 | -11.7317 | -48.1849 | 2025-07-22 05:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 982cb12e-1e27-39a2-82b5-5a82daaa2b41 | -4.9968 | -56.296 | 2025-07-22 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46c4cc6d-c6c0-39c9-b69a-d8ce4ecbb859 | -4.99726 | -56.29283 | 2025-07-22 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3c88609-a76f-3921-9569-b17a31ddb8c3 | -5.306 | -55.97446 | 2025-07-22 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9591dec-5546-3d32-b1b4-b87d5f05c51a | -7.291 | -60.17122 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61cc67c0-1fd7-373d-a3ab-ee2d01dd8bcc | -9.4604 | -63.14899 | 2025-07-22 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8de56c64-1457-3dee-af15-b7c46b67649b | -7.28741 | -60.16684 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5bd3138-b5b2-35f7-aa94-b1dec2c50072 | -11.30541 | -55.11602 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23a55de-142b-3c79-a08e-aa8b05a50f97 | -9.62212 | -67.27843 | 2025-07-22 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cb41b3e-65e1-3b5d-bc2b-0342dfd49344 | -7.25925 | -60.18579 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87ad2f68-b627-382c-b192-9eeabf120a25 | -7.2598 | -60.18203 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6d04f56-979a-3d13-a838-bdc2a6f3950e | -7.94994 | -71.46239 | 2025-07-22 05:42:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16940ac9-533a-30c1-bfd3-317925c62988 | -7.23642 | -60.19753 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e2c4eff-70d4-3741-a9d6-3f038f9b0693 | -11.30482 | -55.1208 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0127b32b-fad4-33d4-af50-5aea373a697f | -10.05334 | -59.09717 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90340e31-cd68-3792-a533-7bad0e58d9c0 | -10.29417 | -60.54079 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f37fbe9c-e146-3fa0-859c-c8ff4080d39d | -10.0487 | -59.09649 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 924f86e7-5bba-3ae8-b3f2-6779a741c76a | -10.10044 | -67.74802 | 2025-07-22 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| efa757f5-84bb-3b99-9c85-08f9c9deb61d | -8.95802 | -62.24192 | 2025-07-22 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82d37ced-5b33-35d8-9572-32c5d13fb205 | -8.48958 | -64.03072 | 2025-07-22 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4efc6cbd-a822-363f-96a9-81d029f61f9b | -7.27332 | -60.17628 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 140bca7a-2d51-3dd1-bf04-6601a6568e32 | -7.26863 | -60.17946 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aec7d30e-6dc0-3f98-b8b2-0ec9cd38d56b | -9.97351 | -62.25439 | 2025-07-22 05:42:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d281b036-ceb6-3162-9e69-75241644ae6d | -9.38039 | -66.58163 | 2025-07-22 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 089bbed9-d91e-3208-b92b-f7090ebb430d | -7.24629 | -60.18768 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 337b523c-ed46-3251-935b-210524193ade | -7.27387 | -60.17252 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee1a4e60-83fd-31f0-8a32-d41c02ab1c0c | -7.25565 | -60.18143 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5183f5fb-6074-3e33-9115-1f06903cf62c | -7.24109 | -60.19447 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64ad6c39-58b0-3001-859a-ec6fa615747b | -7.26338 | -60.18642 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67de9577-f25d-33f5-b259-b02b9697c0ca | -9.97728 | -62.25496 | 2025-07-22 05:42:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7bab65c-5b04-349c-ac54-fa8468a11e93 | -8.96175 | -62.24248 | 2025-07-22 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f91e386f-056f-38bf-9f42-5f63b1396fe4 | -6.21593 | -57.77748 | 2025-07-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fd87635-7988-386e-8bc1-06c4abb98bb7 | -7.24162 | -60.19078 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d229d01d-bb21-3aff-9d24-ce17887557a6 | -10.00317 | -65.29684 | 2025-07-22 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1810ffdd-1209-3e5d-a081-4db590a510af | -10.0527 | -59.10206 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 603a9a8f-0114-3e56-8135-fc795f0be2a4 | -8.99907 | -69.53316 | 2025-07-22 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f74a9c1-aa9b-3d98-b6af-77cf9859f265 | -9.45978 | -63.15308 | 2025-07-22 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3078df05-c8bc-30a0-8aaf-b2796044fab5 | -10.0404 | -59.09773 | 2025-07-22 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84725365-be02-3670-b3c4-da57686ede36 | -11.31098 | -55.12154 | 2025-07-22 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27acd536-19a1-379c-bee5-2200feba70a0 | -8.49528 | -64.03921 | 2025-07-22 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cac75812-f8ed-39ac-80d9-86323507bb9c | -9.98106 | -62.25549 | 2025-07-22 05:42:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16002729-8e4e-3f71-bddf-5fefb045e7cb | -7.26394 | -60.18263 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f18d42e1-75e8-3497-aee6-03424b095370 | -9.02273 | -61.23818 | 2025-07-22 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2c9d9a5-ffbe-3381-b591-34a2c723808e | -7.23229 | -60.19688 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d82fef4-fb4e-38ea-b703-9712a0d76b8c | -9.38094 | -66.57814 | 2025-07-22 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18941743-55c7-3032-9621-fb7211fcb94e | -7.25511 | -60.18515 | 2025-07-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d14e47ff-a9c9-3cec-81fc-346da79744e5 | -7.97028 | -55.29675 | 2025-07-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
