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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97ec6d7f-4955-3b09-a9a8-99c8c8bf44bc | -7.75863 | -49.55514 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d62079d-56f9-3c65-bccf-1e44e82a3119 | -6.78954 | -44.45383 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 194a5d19-ec38-3a49-b207-00f8cd0a3101 | -8.03633 | -45.36956 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc55fad4-a33b-39f3-aa64-37039e8ab244 | -5.70675 | -45.1591 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cb5939d-f83f-3dc9-a0c5-55d9c72a6ff8 | -8.5304 | -51.31307 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab833acf-af34-39bb-ab11-6a1b94a28529 | -6.67016 | -60.03104 | 2025-09-04 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b89ef6b-188c-305d-a2fc-9af4cb48c8d9 | -8.05631 | -44.13303 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f55009fb-0301-332a-8d34-d0c158e156c1 | -7.97003 | -46.34375 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6951801-c4a3-34f5-8c6e-27a916a6b2ec | -10.43035 | -50.27559 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0f5d12-fdbb-331f-acd5-1189d297d7bd | -11.05697 | -45.40481 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff826f4b-c682-3e65-aa74-b14fc065e3b0 | -8.85866 | -52.01641 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa1d895-2fe2-3721-aa58-f69b5aaf7e08 | -10.99826 | -45.91824 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e27e07cb-0fd9-3634-8a00-bc589136893b | -6.75837 | -63.13026 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5811008-7ac4-3ddc-b8f1-ae4bd3b956e8 | -8.4746 | -45.06123 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4aaae10-ad53-3c17-8ada-19316630bcef | -11.05378 | -45.15431 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af7a453f-3bb9-3661-962d-acc79a4724b2 | -8.00412 | -50.10189 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 518938eb-6bf7-3722-b4ba-09b8c84272fb | -7.71882 | -50.32196 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b6cc05a-5d8d-3f18-81c1-193a82347175 | -6.22852 | -43.55095 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc1cb6ca-77ca-3910-b464-cf49d7138052 | -9.45733 | -46.79798 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e6f16d3-cf1c-3ffc-bba2-95bbe99308a4 | -6.82969 | -44.27994 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b671013-f99a-348c-b573-e1da43a3e44d | -6.62331 | -43.96883 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c72efa62-2925-33a3-851d-bba6ad567d34 | -9.82939 | -47.8185 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43c6cf82-5489-335b-9d54-a8629f193926 | -9.30099 | -47.08689 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bf9bc37-a707-3820-b40d-349844168606 | -6.26161 | -43.50767 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94fd89d1-92f3-3c7e-aa7e-86667d274ff9 | -6.21007 | -43.39171 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a29da392-4cf9-3e76-bd28-ccbf402b68bf | -5.31321 | -55.86012 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78b8405c-d0e9-3af5-a3ca-805792f65856 | -4.98473 | -49.90531 | 2025-09-04 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7073207-2c0c-3e40-8d29-9d0d33eb1845 | -6.7405 | -58.72384 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 13169f26-0258-34dc-8192-6fb32638e86f | -7.93728 | -44.94618 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ec7f7aba-e464-31d9-a5ff-6fbcb522ddba | -6.49588 | -43.07574 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 077f7d89-8f7f-39e6-8c36-b54cc0098290 | -8.89561 | -45.79547 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32949cb0-cb03-3d4b-baa0-328401974d26 | -11.13602 | -44.63903 | 2025-09-04 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19b2efc8-775b-302c-a40b-8ef6811f7119 | -10.14256 | -46.24837 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa5c066e-2734-3e56-ae97-3f255986c73f | -6.85991 | -44.27349 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67a4f32e-c82e-3b5a-ba11-cda4aa10e831 | -6.58077 | -44.56126 | 2025-09-04 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbfddd71-5dd2-36a8-94ba-265749951869 | -6.27844 | -43.5038 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6179b5e4-03eb-36b2-8094-231661eaa322 | -6.22808 | -43.3805 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e9f7377-e03b-3ed1-83c3-2445b29554fe | -6.3512 | -42.57149 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3593444f-b32a-3f38-a6f0-8114e8529914 | -8.01113 | -44.03751 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b39ff814-8bb6-3598-b469-af288e0da61f | -6.26761 | -43.58057 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 393aa4be-8825-3814-b9ba-ff1daaf4d709 | -6.2561 | -43.30044 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dce2f5a2-a64c-3a47-a2fe-e2fbb79530e3 | -6.27824 | -43.84983 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32c85ecc-4e86-3046-8381-d0d27788904a | -7.71603 | -50.24425 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b654e569-db2e-399b-8b08-bcb7b930a914 | -10.52915 | -46.76187 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aee0fc04-0a92-32ee-95ec-7b8eb07d4958 | -11.04868 | -45.15369 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6d0775b2-2f25-30e4-8037-29e16a3dbd41 | -5.69089 | -45.39965 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b3c8616-47da-34f2-89a0-95c91394566e | -6.62892 | -43.96646 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1afc0ec-e61d-3131-9a37-a2c7145dd380 | -6.74207 | -58.74099 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 850e6bb0-3925-3964-9614-f51abb039930 | -9.76987 | -49.44567 | 2025-09-04 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7176a075-b0b0-3ab4-982d-ea76f584cfd3 | -7.76458 | -43.96772 | 2025-09-04 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6bed981-f7b5-3494-87fd-6199d1513fca | -6.8925 | -45.56799 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44ff300b-ce69-3b4a-8883-05c02e6b31ef | -9.61663 | -47.03205 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d50f7f1a-eb7c-317f-b2db-688be9b4a1e4 | -6.8905 | -45.56939 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9f53ee7-b9b3-3ec4-84ca-50de75436548 | -6.24511 | -42.6354 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdf70267-2fb8-362c-87c8-b30256b9947a | -6.24272 | -42.61195 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5fcf12b1-1b09-315d-9390-ed03d90cf525 | -5.31393 | -55.85576 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcc3f660-ab24-3752-8cbc-dc6dc5bea0db | -9.61283 | -47.02716 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c56f9bfd-e6cc-3bf1-8241-2b1d87f4c864 | -9.62101 | -47.03272 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4a24187-f02f-3672-90ba-e09dc81f749c | -11.05456 | -45.14825 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa2e3b61-11fb-3333-ab9c-19c615a1a6d9 | -9.43507 | -46.795 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d85883d-6ac5-3be1-bf94-576d646574a5 | -6.81376 | -44.46373 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f2ad1c0-8907-361f-a29a-8082edcf55d8 | -6.7748 | -63.13153 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbc5f913-b706-3031-ac1c-d71b8853b3bf | -8.89352 | -45.81021 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| afb68c18-9471-3d3d-a240-1c98eb487f83 | -10.05813 | -46.22453 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e259a1e7-7e84-3d80-8677-5df6672d12be | -5.70135 | -45.16326 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f5200ad-d87d-3086-9cd5-fc69140cc501 | -9.97966 | -51.62158 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 721c5704-6fb1-3f32-9ed9-6fea28b311a3 | -6.24851 | -42.63454 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb843db5-8e73-3408-a808-1f19983401d9 | -7.75961 | -43.96858 | 2025-09-04 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15d98c83-870a-3485-a443-2d97200568cd | -5.70064 | -45.16819 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01b59cd8-2fd3-3ec7-b126-2c92a3ee9458 | -9.49852 | -46.53539 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ade977c4-0291-395f-9868-4c9f8cc3098c | -5.60986 | -45.01887 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 87381199-4eee-3273-a858-0872db09e690 | -5.69091 | -45.94305 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f8c55cf-dbb3-3f1a-bb41-41247d004e0f | -10.02639 | -46.09168 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 342b36ee-09b6-300c-ae09-ea26ba347d63 | -6.56981 | -48.6454 | 2025-09-04 04:53:00 | NPP-375D | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4d4506f-2419-3a37-910f-2da3cdf3b521 | -6.122 | -44.11457 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a896f555-d35f-3281-acbc-ccc50442fa2f | -6.73341 | -42.27285 | 2025-09-04 04:53:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1fc93986-f5c2-32cf-8884-6cf3432b1c7a | -6.87843 | -59.98968 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98a7ad2e-168d-3cc7-b0ff-00ac0f0763bc | -10.03111 | -46.09224 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b311c9b-41b1-33dd-b2fa-110704523c5e | -6.68848 | -48.41299 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3931760-6be0-3b23-8f32-6c40b117df88 | -9.04301 | -47.00937 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce05ca5f-40a4-363b-95d0-a74cdb441b33 | -5.69552 | -45.40033 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa142dab-bd9b-32e2-bd90-0b8bd6025b2e | -7.76486 | -43.96943 | 2025-09-04 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77a8bce6-0886-3b32-a855-ee3b3e829d69 | -8.52872 | -51.32413 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0e7c5e1-b99b-3b1f-87b7-174af1e6688f | -6.2676 | -44.51324 | 2025-09-04 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190a4a82-4fb8-39aa-88de-c25395d5d962 | -7.68578 | -50.27764 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1a95b90-ff94-3cc9-975d-c797c6fb84fb | -9.48371 | -54.42428 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d145409-38ec-3317-8c00-82488235825c | -6.34188 | -53.44617 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88552390-f4f4-3ef1-b85a-8796c668cf0d | -10.43398 | -50.27613 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128de197-a040-3045-8e06-af78da5b953d | -6.23392 | -43.378 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f003abd-db3b-3ecb-8854-1869a3450a20 | -3.69872 | -53.75425 | 2025-09-04 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4807bd2b-b1bd-3e39-bcba-e6ae56c05363 | -6.77316 | -44.49736 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3c72d26-8de8-3e39-8c4a-6c3e43912b8f | -8.89142 | -45.82497 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd4a5f3d-ee20-36a4-a3c8-eb0b4d7ef108 | -5.30607 | -55.97208 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abf01ed3-9cef-34b1-a459-10be15b4bf05 | -8.03977 | -45.38011 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9fdd2d41-8608-3472-b393-76785bf55aa5 | -10.5343 | -46.75795 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 523a39a4-c5d4-3d3d-a28c-d5533993a855 | -8.52586 | -51.31995 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbf1ac91-d162-330d-84af-beca9bf776d4 | -9.69183 | -49.00729 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 572eb1f3-cc5b-34cf-80e3-6576fc01b245 | -8.43781 | -47.33097 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f164be5f-c41f-324d-927e-3ec337c532dd | -6.17347 | -47.28164 | 2025-09-04 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 746cbbc5-a004-31d2-9183-e6c159e9b3ee | -9.48313 | -54.42787 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README60.md)
