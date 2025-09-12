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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad42a90c-5285-3a46-9ea0-8f702ab6b840 | -11.47075 | -43.612 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 629ae8b7-2ea5-38f3-a65a-b4c2260c3bf6 | -7.32951 | -44.38162 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4a5198b-f660-30cc-baa6-f876eaeb01d7 | -6.67076 | -44.1499 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f0f5fa1-0962-3e41-b975-8b93bc3f030a | -7.45035 | -45.00171 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ab3bae6b-e4e7-3e2e-b007-51f6d2a99196 | -7.32827 | -44.37256 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a2287176-a550-364f-9c27-0b5923094ca2 | -6.59202 | -44.31327 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d57fb8da-ed20-3741-b54d-e3468e33bed4 | -11.98005 | -51.11795 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| dc583320-a99f-362c-b696-d138bfc639bb | -11.42043 | -43.71379 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 812650be-d07b-38b9-8015-e40a70fb237c | -6.24806 | -43.41793 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f7093873-5f91-394c-924c-e3ba0764972c | -7.21976 | -43.9758 | 2025-09-12 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4bc107c2-36d5-383c-a74d-83db5e3ff67a | -9.03755 | -47.08072 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7e21502d-019a-3559-ab65-5311021e581c | -8.19532 | -46.09549 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f037dc12-730a-390c-93b8-5378d71276d7 | -9.49103 | -48.65222 | 2025-09-12 00:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d92fdc2f-5d10-3d45-a5b2-7e6f2cf23c1b | -9.67904 | -47.53601 | 2025-09-12 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| af7c6d6f-66bf-3df9-8ea5-275cb03bd1ac | -6.12851 | -42.96238 | 2025-09-12 00:11:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6de33618-85a2-380d-8dd7-45933e1406c7 | -12.59381 | -45.69186 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2f502dbe-f2ab-301e-bda7-25d4debd0f88 | -6.60213 | -44.32098 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bdc241e3-da57-356e-bbcc-2e51fed397e5 | -8.30722 | -44.93602 | 2025-09-12 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe473c42-f566-367c-9100-dbe8a042ba59 | -6.83502 | -47.87932 | 2025-09-12 00:11:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6b126aa-2ff2-3077-a26b-e263a430e710 | -7.14935 | -44.34531 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc8c5653-ad4f-3873-9b21-6522193f7ab6 | -13.4721 | -51.7648 | 2025-09-12 00:11:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| c6ec1c3b-4fb2-3eac-8473-7eeeb1f5854c | -9.35213 | -46.58784 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c3107563-9752-3680-849d-35f984be7f06 | -8.89767 | -49.94321 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 335.0 |
| b7448bae-3655-35aa-9970-34778ceca41b | -6.24684 | -43.40912 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b3551bc2-955e-3384-b4bf-ce2a3e98c870 | -5.31812 | -43.89462 | 2025-09-12 00:11:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e22d7248-3025-3cc7-9c70-1a6c0bbb21f5 | -12.15539 | -43.70437 | 2025-09-12 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 72cb73d1-e5ff-3e97-8b3b-86a447d2ea9c | -9.06574 | -47.04883 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| fb0eefc6-747d-3b2b-8665-b075ce8675c9 | -6.15256 | -42.60513 | 2025-09-12 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fe7558a3-0f51-39cb-b61f-128213e21071 | -11.67452 | -46.55799 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 330.4 |
| 9b0d642f-a879-324b-9ec1-c6d2509e830d | -11.365 | -43.51079 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9e71b3af-78e4-3ec8-b33b-814f9ccf9f10 | -6.56167 | -43.15082 | 2025-09-12 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7b756e03-0db5-3ffe-b5bc-91d467bdf19d | -11.6762 | -46.57123 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6749e429-f2ca-34bc-b1ff-95fc46e5f2b1 | -9.46488 | -47.65025 | 2025-09-12 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d6bb3696-6d1c-37fb-a6d5-5e296c1f3746 | -9.01961 | -45.74661 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f0084baa-6b5a-3dc0-8f0c-20f6e6e00617 | -6.17588 | -43.49694 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6bf159ce-c178-3622-b25a-65ed1daf51c2 | -8.95747 | -46.06952 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f647de85-1571-32df-8de6-4e9bbd6e8112 | -11.95596 | -51.15642 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8e5b0f45-1731-38cc-832f-f67e89855e2c | -6.65948 | -44.13342 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ad853504-d4e6-3c38-a0ed-3ddfeb78a397 | -9.11414 | -47.13225 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| f1dc481d-b4eb-33dd-ab19-31555a85994d | -5.70029 | -49.18694 | 2025-09-12 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| dd91125b-731f-3d68-a7d9-286affbd740a | -8.59151 | -41.46357 | 2025-09-12 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 094b997a-9d52-3882-83fd-10f02e5bbd92 | -5.52888 | -44.34739 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 05d9d5c1-e0de-30b4-9bd0-ef1be871fe93 | -8.21902 | -45.80202 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1f961332-03f2-36e1-b887-415e25474376 | -8.18845 | -46.11874 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3ae911d4-b5b7-3626-a565-3b659af85486 | -8.36814 | -44.84277 | 2025-09-12 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 63682f47-9d05-3ff2-a905-c589816b5804 | -8.95057 | -46.09307 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c1fc8abe-dd04-3d3a-a368-ee3f52826dec | -6.39121 | -43.52597 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 821eb58b-13e4-35ae-b94f-84d7412f5e4f | -11.15624 | -45.31733 | 2025-09-12 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b1719aa6-7e0e-3693-aba9-4c3568889a61 | -7.40582 | -50.64093 | 2025-09-12 00:11:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 155.8 |
| d40089b5-6997-3b3d-bd55-3a0eae3f3eea | -9.69198 | -47.54894 | 2025-09-12 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 8a9339da-b42a-3296-9e1b-0db71e94cde7 | -7.0766 | -44.14466 | 2025-09-12 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4155f360-250a-3213-97c0-176bfc51af59 | -11.98672 | -51.1529 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f0bc6b00-261c-3596-9196-fdf7ca3882b7 | -8.88435 | -49.94491 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9c00c7e6-a891-3226-8125-71adb5b3373f | -5.11247 | -45.34914 | 2025-09-12 00:11:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| af964891-5b10-368c-a0a3-22168bc41e46 | -5.54108 | -44.17416 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 95556da7-8a7c-3115-b993-e3a47b392d11 | -11.42498 | -43.54328 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 70434578-16a0-3c17-81ee-85f31242ca32 | -5.34318 | -44.81204 | 2025-09-12 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a7437087-0dfd-3c23-9444-37a2cd19a628 | -9.10641 | -47.11206 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 10b98aa8-5b5f-3249-8d35-71d331f6e49a | -6.53798 | -43.70844 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d0808776-5102-3055-a1c1-507ebfff17e6 | -12.59243 | -45.68621 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9a4536f1-e5f9-34f1-bb9f-5d308e7b7641 | -6.31737 | -43.44667 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2f2aa79a-1185-3985-a0e6-ea0bb3e5e78e | -6.05178 | -43.33215 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c6ccccbf-6908-30c9-b7fe-ffbd10f45da6 | -11.68813 | -46.53617 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f70e6fe0-154b-3d3b-bbef-a98da7ee00a3 | -8.48531 | -47.2769 | 2025-09-12 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 64689c22-3883-377b-8e35-1fa6eee7bee5 | -10.1376 | -47.90807 | 2025-09-12 00:11:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7244aeac-c5c8-3137-ad6c-5f4df267c7e3 | -10.79182 | -47.26888 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6175ac83-e50b-38e1-ac8f-c5bbb694e52e | -6.03171 | -43.59245 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 156f3108-f1d6-3d51-b9d2-8cfd2b420ff1 | -12.18761 | -40.88256 | 2025-09-12 00:11:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 404f69b6-8ece-3b2a-b197-edd0b751bd46 | -10.48252 | -49.37519 | 2025-09-12 00:11:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 7afba5fd-8b6c-37e7-a4fd-0aa79f9b12cd | -8.33162 | -45.40491 | 2025-09-12 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 04673cd0-db3c-3971-9241-28b4a712206f | -6.28172 | -43.19085 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d2538b3-222f-34fc-9bfd-14713a4803b1 | -8.64431 | -45.71933 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50efb4dd-3565-33c2-823f-0b8d73223b5d | -6.21429 | -43.36882 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ee014903-3b4d-3f34-9b53-429b4ca5a680 | -6.47471 | -44.9357 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 394.4 |
| 6260b26c-cfb6-305d-bd3e-5076cb0294a0 | -9.01822 | -45.73582 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1c289c6a-95f3-38ad-ae08-ce4641e48ad0 | -9.35371 | -46.6001 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 70d0a216-dbde-3c72-a5ce-659f88dfa760 | -5.98593 | -43.71554 | 2025-09-12 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 290ca537-f152-3ae9-84a2-b1d239239ec2 | -9.05515 | -47.05016 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e6a34045-46a7-38e5-ab6d-7f9853702ce4 | -9.06402 | -47.03563 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e3e92bfe-8756-396b-aaed-f60c655fb183 | -8.88165 | -49.92318 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7f0eef2e-8448-3c9b-88be-8fb8a6379181 | -9.99438 | -51.73073 | 2025-09-12 00:11:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5804a9be-4816-3ff9-bd26-225e6238a719 | -8.60061 | -41.46212 | 2025-09-12 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1a8e5552-3fc4-3da2-989f-7b20e82eb354 | -6.19706 | -42.66326 | 2025-09-12 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 35b44b06-537c-3a84-b862-39779a656ad2 | -6.40256 | -44.06405 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 094a19f0-a795-35f0-bb79-89d71f1e8fd1 | -5.69064 | -49.20514 | 2025-09-12 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 641901b4-bbdf-3a2d-a573-12e852452b43 | -9.72134 | -48.30835 | 2025-09-12 00:11:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 2eeefeee-af0f-3ae0-ba01-bc6d61917f2c | -7.40128 | -44.36533 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| afbaf0c8-f6ec-3b08-b5df-06a9879c12a4 | -7.07777 | -43.8903 | 2025-09-12 00:11:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb3430ae-c5e2-3dc0-a044-f311bb106a97 | -6.47343 | -44.92633 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c80ff68-dbfc-3961-8e4d-4272a5c1764b | -6.82772 | -45.64256 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61677e42-6b84-3239-834b-25d8401a8b4e | -11.69741 | -46.56823 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7282a11c-f7dc-3c90-a48a-7db0c53f36ae | -10.57868 | -47.20703 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 99911722-67e1-314d-a265-9e41cb7f02e1 | -6.08727 | -43.26406 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| dca1fe8d-6796-34fb-9b78-76385ee4d4cc | -7.43896 | -44.98038 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1a2bb09e-2cf7-3ce8-a1f8-406f922c6d05 | -5.88513 | -43.93034 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7941387-03bd-3010-8c55-898ba00788dc | -7.78891 | -50.78769 | 2025-09-12 00:11:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1c65ebf9-32a8-3b2f-bf82-d7338fa90e88 | -12.01874 | -43.78385 | 2025-09-12 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 3b63d867-f165-3610-854c-dac7a78e1479 | -6.82089 | -52.7875 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 9e443ca1-b8ad-3556-9149-659ad17bf959 | -5.66336 | -45.95384 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 36279895-9c6c-352b-b1b4-063597eac644 | -7.447 | -44.43325 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |


[Clique aqui para ver as próximas entradas](README6.md)
