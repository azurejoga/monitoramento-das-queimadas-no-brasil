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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd5c62de-8e21-371c-ba5f-27dc47b693ee | -8.1686 | -54.7634 | 2026-09-20 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4f44d369-c2a5-3fe5-91ad-c3df22fde6bc | -7.8025 | -44.9337 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cfed9f4c-0bcd-32ef-ae0a-4589d834fffe | -11.3787 | -51.4412 | 2026-09-20 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 36f72562-b193-3db4-8e41-db089f243077 | -11.893 | -47.6545 | 2026-09-20 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 706629c1-a329-3152-b9ea-6abad261cdb9 | -10.3168 | -50.2352 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| b1c2bf06-47b1-3b56-ac53-d69a5188f0d7 | -3.6946 | -60.5835 | 2026-09-20 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 20d175b7-f28f-3979-b672-9d435f763689 | -10.3914 | -48.9133 | 2026-09-20 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9693d84c-ab60-367d-a212-787f99173e15 | -8.1688 | -54.7432 | 2026-09-20 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 664e16ec-6dba-30d8-b046-d3f9c75e029b | -3.6946 | -60.6025 | 2026-09-20 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e53f51a4-88c4-39af-96b0-824f71039360 | -9.2374 | -46.2344 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a8010507-3330-359b-8715-249a420a38d8 | -11.0994 | -54.008 | 2026-09-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0639f47d-74a4-3930-ac2d-385ee8ec54de | -11.4541 | -45.3662 | 2026-09-20 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0c8f660f-cee5-3e26-8616-01d98103c455 | -9.26 | -45.9616 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 486b99b0-a44f-3f07-9ff2-a4c3d1a19fa9 | -13.2606 | -51.7335 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 28638e07-876d-3342-ac4b-f31e39d7311d | -3.3454 | -42.7597 | 2026-09-20 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 00d47762-532c-3239-86b4-fcde26c3953e | -8.1376 | -46.8155 | 2026-09-20 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| af9702f6-8991-3833-b638-343d0be7ceec | -5.8408 | -53.5408 | 2026-09-20 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 45f0582d-702c-30e3-9d55-d037bca61a34 | -14.1458 | -45.5638 | 2026-09-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 261.2 |
| c241b212-c86b-339a-a08e-963e13f73a19 | -8.8639 | -45.937 | 2026-09-20 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e7d39089-e3ae-3daf-bc20-5a6263c40363 | -10.2793 | -50.2177 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 17438276-41e4-32c2-a5da-78577038b787 | -3.3492 | -59.867 | 2026-09-20 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b80dd244-7caa-310c-a3cb-508a7d71002b | -9.5539 | -46.5807 | 2026-09-20 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e0ca66e7-342b-307c-9bc2-28f542950bec | -7.8003 | -45.1163 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4656e73d-b004-399f-8d2d-4c0b44ad8239 | -9.2676 | -48.2472 | 2026-09-20 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6b9d1cad-d06d-3931-82d0-0db38fd87c66 | -6.4485 | -59.9909 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b3748952-7011-3fdc-8db9-fb34d5381b9d | -11.6609 | -43.4239 | 2026-09-20 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| d42612af-ce1b-3714-9d29-fa1e9b2d4abd | -14.1268 | -45.5439 | 2026-09-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 87ffa9de-12ea-32d7-8e11-226af9a98773 | -10.7708 | -46.3453 | 2026-09-20 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 92cee84c-e464-3086-9c90-1ff6b4a7d8df | -10.7899 | -46.3429 | 2026-09-20 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 77428e8a-6aad-36b4-b7db-27be9dbc23bd | -3.364 | -42.7824 | 2026-09-20 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0cbfb89c-86b3-3c3d-9b3c-d228b818b0ea | -8.845 | -45.9391 | 2026-09-20 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4c25a767-fb29-3520-8399-9d3791eb8093 | -8.8636 | -45.9596 | 2026-09-20 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| a20db325-bf66-342c-a8b6-dd5c3d2bda73 | -11.118 | -54.0268 | 2026-09-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 0aafb326-d93b-3d92-a045-5d8679226479 | -3.3367 | -57.8673 | 2026-09-20 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a7216459-1a7a-30f1-8422-1ff7e3428acf | -6.8945 | -43.7531 | 2026-09-20 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c2e7fd7d-876b-3473-83de-0aface613232 | -8.7729 | -44.2568 | 2026-09-20 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 40afb7f7-df86-395c-ae8a-d59bb8c21d34 | -8.1874 | -54.742 | 2026-09-20 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5d374cbf-6305-3bb7-8f44-60526ae5e651 | -9.2865 | -48.2453 | 2026-09-20 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| d1ebbb9b-b5b3-3d6a-8760-ba082af13e8b | -10.3171 | -50.2138 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f36aed42-7f92-3f79-a6bc-ac4a252db297 | -10.2787 | -50.2605 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 67b5bcbd-e213-3c80-a0e6-980389da5862 | -13.2602 | -51.7548 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 189.3 |
| c1007709-1ba2-3837-94c8-efc5a1a54a5a | -6.4486 | -59.9717 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 311994d2-a4c3-309b-bafb-73ed8a9ff6d5 | -10.2784 | -50.2818 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3eadd657-cea0-3afc-8a3b-4944f13fd557 | -12.5269 | -50.9711 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ad4d5b0a-06b2-3673-9e4c-0c271cc720b1 | -10.2976 | -50.2585 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ec5aec74-16e3-3e5b-8afd-9f317cdad172 | -12.7653 | -52.8661 | 2026-09-20 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 24982093-29a6-37cf-97c0-feb12d43916a | -14.7046 | -46.7081 | 2026-09-20 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 235.1 |
| b74c32d9-2a18-3300-a487-0d3d6282daa6 | -10.6 | -50.2486 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8585f9c6-1353-3d0d-88c1-d8d419fb0108 | -11.0256 | -48.3164 | 2026-09-20 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f9115fd8-7a10-3058-902b-6f13eaace0e4 | -9.8313 | -48.4073 | 2026-09-20 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| b40f409c-f299-30a7-996a-f13b1d4d5bbf | -6.4671 | -59.9711 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1a8363dd-4d9b-38cf-bf0f-5e22f6f92563 | -9.5536 | -46.6031 | 2026-09-20 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 9bde1c64-b3d3-3736-b888-9a66a4890ca6 | -7.3259 | -55.6153 | 2026-09-20 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 04104e4f-606f-3a1b-a0db-474b412aa18b | -9.84 | -46.4136 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| c89dcc14-1aff-3c2e-bd2c-fbd40da60352 | -12.7625 | -46.1572 | 2026-09-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 143f0e62-642e-380b-8d95-65c391cae1e3 | -6.3199 | -59.9381 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 726839ca-5a4a-3cb1-9bd0-9e0664d19f9f | -12.1328 | -47.041 | 2026-09-20 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fae5568d-47b7-3310-809e-3aeff4922b0a | -13.241 | -51.7571 | 2026-09-20 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2d5232e8-9b74-3413-b23a-17d02944786c | -11.155 | -42.7885 | 2026-09-20 13:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 01985120-e2b3-3fef-bb42-98c468f1cf07 | -11.3793 | -51.3989 | 2026-09-20 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 11222840-0c1d-3128-97a2-d8ed08526814 | -10.8364 | -50.9479 | 2026-09-20 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 66efe921-a2fc-3190-a853-45fbbb364f0a | -11.3603 | -51.4009 | 2026-09-20 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6881f041-fe25-3aca-b363-b17a03183db2 | -12.5224 | -50.0484 | 2026-09-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6a35964d-4021-3bcc-b57c-e35e1765e3de | -6.9225 | -42.9088 | 2026-09-20 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| afff673a-4cfd-3fed-8df8-f0f3244c2acf | -14.1258 | -45.5904 | 2026-09-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 66efb3a4-403d-3363-9576-3d4126c21a38 | -11.8747 | -49.9983 | 2026-09-20 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 04bb8015-f065-3070-b01a-0cdb52a8afdf | -8.8825 | -45.9576 | 2026-09-20 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e49f5e28-2758-3838-97d5-b14a5f8d01fe | -9.8394 | -46.4586 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 17a79462-0cad-3680-aa5d-e2a4c53a5af7 | -3.6947 | -60.5645 | 2026-09-20 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 013922ce-9d68-3443-84ac-1e8c9d36a183 | -6.3198 | -59.9572 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 47a71595-4501-355c-b77a-58621ada9159 | -10.8553 | -50.9459 | 2026-09-20 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e74fb047-b350-3d56-a26b-b745ebf614ed | -10.3917 | -48.8915 | 2026-09-20 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d05525f4-c9b1-30d5-9253-02646721e9bc | -9.8502 | -48.4053 | 2026-09-20 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 0b66b1ec-d973-3f33-89e9-dd4c5f1a16da | -12.5227 | -50.0267 | 2026-09-20 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7390651e-6330-3f89-8e7a-0ebee2bfc5b3 | -14.1263 | -45.5671 | 2026-09-20 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 9952b27a-f1f5-3998-80f7-82882fcf6f5e | -7.4286 | -44.7409 | 2026-09-20 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 85c7aa21-05ac-35a4-bb4a-66277e4ce150 | -11.0065 | -48.3187 | 2026-09-20 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 79a9aa6f-394f-38c3-b984-3f335263f817 | -9.2414 | -45.9411 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a4414435-97c0-35ae-8de3-ffa6f7339cd7 | -7.7489 | -44.6873 | 2026-09-20 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 807b36a0-c696-3d51-ba4c-2ad3e5444379 | -10.2598 | -50.2624 | 2026-09-20 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 62688dfd-aa97-35b1-b483-eb21333a638d | -12.152 | -47.0383 | 2026-09-20 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 71739529-12e9-3a1e-8ec8-e140285616b9 | -3.3675 | -59.8666 | 2026-09-20 13:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| aa76f25a-0f2e-3691-a922-ddda072072ac | -14.6861 | -46.6657 | 2026-09-20 13:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| dc67ce40-ae39-334f-ab63-95158ef64c3a | -3.7129 | -60.5832 | 2026-09-20 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 176306cf-ac70-33e7-ba5a-af8353243d68 | -7.2519 | -55.5994 | 2026-09-20 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2b4d96ae-e1d1-36ec-b396-54228f8435a4 | -10.8757 | -57.1554 | 2026-09-20 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a64af9d8-846b-3c9b-95a4-a9daa82bfb0a | -6.9414 | -42.907 | 2026-09-20 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| ad335c5d-3c73-3014-8d8e-33777ece49c1 | -11.4714 | -47.776 | 2026-09-20 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d721fc15-d5e7-3b52-a4d7-59c81f87f02d | -11.1545 | -42.8124 | 2026-09-20 13:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 098af570-900d-33df-824e-23bd8308f01c | -9.0541 | -48.7686 | 2026-09-20 13:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7baba459-c156-345a-9010-13f945663835 | -7.6312 | -46.7729 | 2026-09-20 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6fbea7dc-329f-3ff7-8903-789c25910a88 | -14.6856 | -46.6886 | 2026-09-20 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 1e4b3531-b1b1-3b97-b713-9ebddd4005c8 | -9.8397 | -46.4361 | 2026-09-20 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 295.7 |
| b97b73b9-927b-398c-bf4e-102f6eeaed43 | -17.5795 | -44.9765 | 2026-09-20 13:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d089e084-3f9d-397f-840a-cc1c77f17422 | -7.6314 | -46.7507 | 2026-09-20 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b8fb8b28-6ee2-3aee-b15b-ae268837040a | -12.7621 | -46.18 | 2026-09-20 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 1c3dc53a-1602-3674-b2c9-b9a5c08e7b5b | -11.379 | -51.42 | 2026-09-20 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 690c37f4-7987-30bb-8b05-4145de5f2192 | -10.8367 | -50.9266 | 2026-09-20 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 4deff0cd-2bec-3761-9856-c82e3d900c85 | -6.467 | -59.9902 | 2026-09-20 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 15bb49dd-d29b-3f10-a929-f93a64f0e5cd | -11.0991 | -54.0285 | 2026-09-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 177.2 |


[Clique aqui para ver as próximas entradas](README118.md)
