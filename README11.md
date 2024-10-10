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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45b79ba7-5cdb-372c-8848-c12b1eef0008 | -5.9996 | -44.654301 | 2024-10-10 00:20:38 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfdaac18-3510-3c79-af5b-f082c50504cb | -5.9911 | -44.708099 | 2024-10-10 00:20:38 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07ac0878-1a71-324a-ab73-cbdd4d4c5435 | -5.9929 | -44.716301 | 2024-10-10 00:20:38 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8654da-6512-37c1-8ff9-8372ab112211 | -5.6216 | -43.155399 | 2024-10-10 00:20:39 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 971991fe-1b51-331b-b835-182a3133949a | -5.8696 | -44.394402 | 2024-10-10 00:20:39 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a739ea19-af67-3715-bc5c-0da80ae53166 | -6.4603 | -47.113098 | 2024-10-10 00:20:39 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af93d31e-9d6b-31ef-af8a-d0b5c0822e81 | -6.4628 | -47.124699 | 2024-10-10 00:20:39 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed1ba6d9-233f-3500-817b-3cfac834b6c7 | -5.6189 | -43.6451 | 2024-10-10 00:20:40 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 919531f2-b19d-3eb2-acce-1385b28adc79 | -5.1252 | -41.295502 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99f85ced-3552-386a-a70b-d21edb9d036d | -5.1268 | -41.302299 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40017e7d-3cb4-3835-a793-9d270b333737 | -5.1284 | -41.3092 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea87db99-a24b-3e7f-950b-9c12da270e6f | -5.1299 | -41.316002 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8936469a-fc2d-3b33-941f-4abfaaaefefc | -5.1138 | -41.290798 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5c1df4c-053d-3a71-9f67-8a0dbde42748 | -5.1154 | -41.297699 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b07c5912-9d98-3a58-825d-c7f531d484a9 | -5.117 | -41.304501 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60de60e8-ced9-3d9d-ae74-ae3f275ae5b5 | -5.1186 | -41.311401 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3dd0f40e-b4c7-3be6-a2c3-9c631200c422 | -5.1201 | -41.318199 | 2024-10-10 00:20:40 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 04deb4c8-8a29-372d-aadb-0d8dd75618ea | -5.4681 | -42.750999 | 2024-10-10 00:20:40 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 04aeba01-f57d-3391-a1fe-d36c5b3d91ca | -5.4466 | -42.792599 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0523ccfd-b644-349f-b41b-0d549006a563 | -5.4482 | -42.799599 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e63ae27-4380-3334-8800-7cb010a91c6c | -5.427 | -42.797001 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1dba5c1e-a8a8-3c66-8588-a753de1b2887 | -5.4286 | -42.804001 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 246b6e76-b3a5-3afb-a3e1-faab6bb9dd3a | -5.4302 | -42.811001 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31a74479-5217-3142-ae28-53bee8b0b85f | -5.4687 | -42.935501 | 2024-10-10 00:20:40 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d32800ad-687a-3763-98c4-edc71e94079c | -5.8753 | -44.742001 | 2024-10-10 00:20:40 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 283312da-b450-314e-95a1-b351096b1646 | -5.8772 | -44.750301 | 2024-10-10 00:20:40 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01030f16-93eb-3987-bad9-e17258549155 | -5.8417 | -44.637299 | 2024-10-10 00:20:40 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9ea28b-45e9-396b-b673-10a62b943edd | -5.8435 | -44.6455 | 2024-10-10 00:20:40 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caba1fa4-6ed3-33ec-ab0f-32b22b92a7a6 | -5.414 | -42.785099 | 2024-10-10 00:20:41 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b254af2e-0e9f-3d28-9b7b-2c7fb3109d14 | -5.4156 | -42.792099 | 2024-10-10 00:20:41 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a468d986-ef31-30ef-8a4e-785f4cf04258 | -5.4172 | -42.799198 | 2024-10-10 00:20:41 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ed453cc-21de-3f63-ba97-9a91e866402b | -5.5103 | -43.255501 | 2024-10-10 00:20:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6502e8c6-0695-378d-b844-0becbe39879d | -5.512 | -43.262699 | 2024-10-10 00:20:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9665ce17-b04c-3567-b905-1f6e9f1d308e | -5.5136 | -43.269901 | 2024-10-10 00:20:41 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 327171ad-3ce6-3e1b-899d-ab1e199e1d59 | -6.5086 | -47.7108 | 2024-10-10 00:20:41 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 041aa5b2-e8a1-3b9f-978e-7cf77948fab8 | -6.5114 | -47.723499 | 2024-10-10 00:20:41 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78af24b5-d1c7-30e1-a6a7-47e534dfb618 | -5.4981 | -43.7029 | 2024-10-10 00:20:43 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00427312-2662-39fe-a4a5-d2af09cfb69d | -5.5211 | -43.9417 | 2024-10-10 00:20:43 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaa5e942-2231-39a3-87ca-8385f5191df1 | -5.36 | -43.273701 | 2024-10-10 00:20:43 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 964c6c8e-3e87-3596-a161-701e0987e760 | -5.3616 | -43.280899 | 2024-10-10 00:20:43 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18d01eb5-b19d-306a-ab2a-6c0591e81f97 | -6.2201 | -46.9972 | 2024-10-10 00:20:43 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0d1856-783b-380b-9011-7e870913fd58 | -5.5652 | -44.092098 | 2024-10-10 00:20:43 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc393f9-03ff-3b25-b4ab-9c4b2d7a36b2 | -5.6451 | -44.4939 | 2024-10-10 00:20:43 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf40d7b-5efb-34fe-b46f-c3062fc3856b | -5.8406 | -45.416 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9fde1ea-7daa-3d99-bf72-0d17bd5da8f7 | -5.8426 | -45.4249 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0379ecd-deba-39ae-a5bf-d69710287d31 | -5.8446 | -45.433899 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbfbd9af-1c0c-3bd8-a6ee-30c63c282177 | -5.8308 | -45.418098 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1670cf40-673e-3890-8d60-e66ac85f5582 | -5.8328 | -45.426998 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08a97855-84a2-3928-b84a-ef9072261e0f | -5.8348 | -45.436001 | 2024-10-10 00:20:43 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7fe2ca-28ba-3373-88e2-2ce65af771ed | -5.2208 | -42.8871 | 2024-10-10 00:20:44 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 486516eb-3953-3510-89ba-587df75ade4f | -5.1302 | -42.533901 | 2024-10-10 00:20:44 | METOP-C | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59cd8bcd-54e5-3d70-a3e9-bbb0b0026a87 | -5.6285 | -44.7873 | 2024-10-10 00:20:44 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2c93827-6630-3351-bbb0-861da2648d82 | -5.6303 | -44.795601 | 2024-10-10 00:20:44 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8530575c-eee9-3f4d-91a8-95b01db5010a | -5.418 | -43.940601 | 2024-10-10 00:20:45 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24fd08b1-b4e3-3ee5-9b89-821a96c2d3f4 | -5.9801 | -46.603401 | 2024-10-10 00:20:45 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e75b58d-a269-3a48-80cd-3ad98c41a44c | -5.9134 | -46.346901 | 2024-10-10 00:20:45 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58d3ebbf-ffd0-3969-950d-f18e04ec2843 | -5.9156 | -46.356998 | 2024-10-10 00:20:45 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3102978-100b-309b-8fe2-89945aa461ee | -5.9681 | -46.595001 | 2024-10-10 00:20:45 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f61a6b12-9243-3133-b908-98bdc88fd79d | -5.9704 | -46.605499 | 2024-10-10 00:20:45 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8078d8f6-f845-32c0-8170-47aa53e5fc72 | -5.9727 | -46.6161 | 2024-10-10 00:20:45 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c57441f2-0b29-3c7f-9983-7c66181201c4 | -5.4026 | -44.192501 | 2024-10-10 00:20:46 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4a454b0-fec9-32b1-ba26-f1aabe026fbe | -5.4043 | -44.200199 | 2024-10-10 00:20:46 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8234e25c-f952-36c3-8416-41bfa2b156b7 | -5.4235 | -44.285599 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02a8da2e-a146-360b-bd2b-20944c648982 | -5.4253 | -44.2934 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8c8d9f-57b5-391a-8486-53cfd4d0b957 | -5.4137 | -44.2878 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6735393-3ec1-3d21-a305-c8d2d78474dc | -5.4155 | -44.295601 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0312ab67-50b1-3e33-ac30-d1616dbdb72e | -5.4172 | -44.303398 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 682f425d-5b4a-3c4a-9cb6-a1c948d33fd1 | -5.4039 | -44.289902 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dc80e19-9601-3e58-864f-d0749f3af7f0 | -5.4057 | -44.297699 | 2024-10-10 00:20:46 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0966dd21-2abb-3e6c-8372-306d66c40c04 | -5.894 | -46.677502 | 2024-10-10 00:20:47 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1870c995-a925-33c1-800b-3626b6c3b2ad | -5.8963 | -46.688099 | 2024-10-10 00:20:47 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 899c2fbc-5ad1-33ac-8a00-ac53970e123d | -5.2497 | -43.7421 | 2024-10-10 00:20:47 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a413605-6894-3312-8663-367bdbfec827 | -5.1704 | -43.436901 | 2024-10-10 00:20:47 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e8de558-1348-372a-84db-31a67baff888 | -5.516 | -44.881401 | 2024-10-10 00:20:47 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3f27a6c-a7a9-3bb2-a7b9-03eeee29db68 | -5.5062 | -44.883598 | 2024-10-10 00:20:47 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e22f552-e242-35de-a206-e9e51a18e3f5 | -5.4179 | -44.535301 | 2024-10-10 00:20:47 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0bf0840-15c2-347e-ae95-86a6c3f47c93 | -5.4197 | -44.543301 | 2024-10-10 00:20:47 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99a880bb-d2c9-30a1-ad7d-7f033bbea1b5 | -5.1965 | -43.871101 | 2024-10-10 00:20:48 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0c78bc5-c518-3f5d-8bf0-8c6315b30d15 | -5.1982 | -43.878601 | 2024-10-10 00:20:48 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4135a6e1-30f5-3827-b138-38c0f46fd64a | -5.7801 | -46.439701 | 2024-10-10 00:20:48 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a12161f4-fbb7-3725-b7be-93b8a4f24c4b | -5.7823 | -46.449902 | 2024-10-10 00:20:48 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b25d13e-d27c-3bd0-adee-72e340f61aa1 | -5.7704 | -46.441799 | 2024-10-10 00:20:48 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e254d517-161d-3360-a210-df03a26e9ced | -5.7726 | -46.452 | 2024-10-10 00:20:48 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 074bffb8-e4c3-30b1-b96c-81174041c2d6 | -5.7749 | -46.462299 | 2024-10-10 00:20:48 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9a52d43-c665-3432-877b-2f4470065e78 | -5.4087 | -44.861401 | 2024-10-10 00:20:48 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02d955c6-c380-311c-8f91-4608120c187f | -5.0626 | -43.460701 | 2024-10-10 00:20:49 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e56e88de-7244-3623-97c0-a1fe6e334adc | -4.9132 | -43.029301 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35c36b2f-294a-3fcf-a56f-523b869cb77a | -4.8839 | -42.991501 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1c9c401-1b5c-3d9d-b8a2-dcff298d8882 | -4.8855 | -42.998501 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8c43cfb-4700-3b25-bf9c-b207f2ead576 | -4.8725 | -42.986599 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9119be1e-a673-3df1-b801-959d18fe3ee8 | -4.8741 | -42.993698 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70e64f43-62fe-38f9-a60b-c01cef44c401 | -4.8757 | -43.000702 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa9d2600-df46-31a7-b77c-f1d02474aaa4 | -4.8773 | -43.007702 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4e8104-01cf-37f4-8498-74097e98ea1b | -4.8691 | -43.016899 | 2024-10-10 00:20:50 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5773791a-8a19-3c27-9cbf-3bb170dd059a | -5.4232 | -45.385899 | 2024-10-10 00:20:50 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf370621-ce9d-3ea5-a6b5-f4d8afa85c75 | -5.6386 | -46.448799 | 2024-10-10 00:20:50 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c33c20bd-801c-3baa-84d1-96c4774279bb | -5.6266 | -46.4408 | 2024-10-10 00:20:50 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a36f1d19-f9a2-3714-aebe-3096537a374e | -5.6288 | -46.451 | 2024-10-10 00:20:50 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29ca976c-19bc-368b-94ab-e649ad1dc1f9 | -5.6311 | -46.461201 | 2024-10-10 00:20:50 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23fd0f7a-ef8d-3452-8a9c-7a17dd766e03 | -4.8185 | -43.020802 | 2024-10-10 00:20:51 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
