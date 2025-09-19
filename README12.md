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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 587db0d9-087e-34e1-8e6c-3183694a44b8 | -8.37464 | -44.67239 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1ed238a-672c-306c-af90-a75de34344fa | -7.55725 | -45.49263 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f4e5a07-83b6-3df8-b3f6-6b5c85a97cbd | -7.70096 | -44.47322 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ede1a7c0-ad43-353e-b6c5-b27bbb9aee15 | -7.65339 | -45.13685 | 2025-09-19 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fe2396e-4072-3a9d-8267-eb94a075978e | -6.85406 | -44.1479 | 2025-09-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d355e23-43c5-3e48-b8b9-efb2e4e38aa0 | -8.13588 | -44.46824 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b29be27-1132-3638-bf8e-b1f99d643897 | -9.51744 | -43.06227 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 970876e8-9609-3007-8bd3-2105a851f695 | -8.95447 | -44.20148 | 2025-09-19 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 206bdfcb-ddbb-31d4-89d0-c4edc718cd20 | -5.20664 | -45.17519 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5db6e330-d5e4-39c4-a85b-ae8bff354501 | -6.85827 | -44.14869 | 2025-09-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3326ab2-7cbb-348a-ab4c-53629ff1017f | -7.56555 | -45.49903 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4772f010-2357-3366-92a6-c6b0f3bec932 | -9.17813 | -45.31073 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10e01f57-359b-395a-80f5-a4e4d90e6c60 | -7.09008 | -41.40576 | 2025-09-19 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c3750b4-ec29-3ca6-a481-781f8b17560a | -7.33512 | -39.70828 | 2025-09-19 03:53:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e925bc58-5df9-3aee-85ed-7bd4c2d89830 | -6.32729 | -42.39101 | 2025-09-19 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25ae82f4-474b-3ad9-bb66-740d9299644d | -5.79477 | -45.36486 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 272b9dcf-b612-32dd-9982-6e224a49a18b | -5.77199 | -45.97551 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cf297f4-13e9-3a11-a5c2-c235e9007765 | -8.94974 | -44.20452 | 2025-09-19 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a3cff5d-989e-3962-9230-8a41d4e864d0 | -8.04817 | -44.07584 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0868e718-ac5a-3f7b-8e50-c78e5694cdfc | -7.33456 | -39.71184 | 2025-09-19 03:53:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ad8cc23-50eb-36e8-b41a-ae1b8af57000 | -6.05119 | -42.69899 | 2025-09-19 03:53:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9c44087-9852-3b9b-8ae8-4045d2e4f1ca | -6.91173 | -44.80577 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 868eaffe-5d6e-3b60-939f-71229b7d5323 | -6.20617 | -45.10712 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ee0a97-fd10-3793-9b01-f61d9fc65337 | -8.96903 | -46.26878 | 2025-09-19 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a74caf2-3507-31cd-9c93-742e9f21d089 | -7.54197 | -45.49948 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d7fa030-2da2-303c-99f9-7a15b0ec8c74 | -3.28156 | -49.148 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 690edb61-12a7-3dac-9c04-c13d1b8d5e08 | -8.62671 | -45.71042 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09bc7054-82ed-30d4-8b7c-94b29ae1fa96 | -5.79849 | -45.71243 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aed41fec-b301-3ac2-86b6-10057e31c6ba | -7.56717 | -45.48957 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14cd4c77-1fe8-3c07-b3f2-90a7b3dcf953 | -5.77152 | -43.90466 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc918ed4-2988-3fa2-a211-ff9b47d86396 | -5.04451 | -47.90551 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1525e572-7341-31f9-909e-070ed89d1c1e | -9.15086 | -44.64771 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f87445-fa72-3831-9502-962aeda0a36b | -5.16535 | -37.73024 | 2025-09-19 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c54e2ae3-2dc1-343c-88b0-d6a377ab7675 | -5.89462 | -45.72443 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01785c03-6204-3c33-8ddb-98f2d26c145a | -6.8476 | -38.37083 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 947bcab9-707c-3fa4-867f-0da61fed2770 | -5.13209 | -47.83089 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3bfd0045-4b3b-372c-9491-0cb0b96cd2c5 | -6.28842 | -35.21626 | 2025-09-19 03:53:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae72c1c0-aa09-37d6-a573-f8db8b03b8a9 | -5.79656 | -43.75361 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2822707b-437e-3429-a300-f4d38a3ec104 | -6.72326 | -38.25552 | 2025-09-19 03:53:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59698b16-f42f-3599-b58a-2b86386b47dd | -5.14385 | -37.73748 | 2025-09-19 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0fdde25-c9e1-3274-804e-f3974bc7525c | -8.02161 | -44.94656 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa82423b-1106-338e-a912-88c8408382ca | -5.79328 | -43.90413 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ee63f74-7862-38a8-93e3-f4d140c808d5 | -6.85491 | -44.16811 | 2025-09-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73749ed1-1f6a-3250-9a6e-ddd0071d9184 | -6.31129 | -42.39336 | 2025-09-19 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd4f8d09-bd40-347c-90d2-fdd016a13ba1 | -5.79097 | -45.35915 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42889755-5a78-3fc5-a39f-70f42c9d17fc | -5.48009 | -44.11546 | 2025-09-19 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 513af29f-3316-3bf2-94e3-dfb72b2e0883 | -6.2107 | -45.10796 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 249ce055-623b-396f-8883-ee9678e1df46 | -9.72507 | -45.92256 | 2025-09-19 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa974c4-fa72-3f0e-867b-c12b67cc5414 | -5.08407 | -47.51866 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ada58e33-303e-3e40-8c0c-0c33b38235cc | -7.8669 | -45.63513 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ccd0020-8c0d-39a8-ae6e-5311847bd379 | -8.1389 | -43.62533 | 2025-09-19 03:53:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f5b082-4ab1-3dbd-9601-3176581522ff | -7.8509 | -45.61855 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ddfebbf-7e94-387f-bcd8-da9688ab1a36 | -9.16763 | -44.65406 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09e7ac7-4b29-3731-9c55-95d0566e8c16 | -8.37599 | -44.68287 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4caabf8b-3956-3f94-8ce0-5e9a2b6be89d | -5.43636 | -46.68305 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baa886eb-e5f0-3d8c-bf4a-c7cb2f530483 | -5.08968 | -41.14346 | 2025-09-19 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f696347-3f3d-33e2-84d5-c12cc09df4f2 | -5.34554 | -46.14391 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff551d84-67d1-3efa-9c27-2fd3e841a4fa | -8.15807 | -46.78023 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f2a90c6-6adf-342f-b10d-823ae367da12 | -10.19762 | -43.85155 | 2025-09-19 03:53:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e6b03d-db58-3ffc-b3b0-8edab759239d | -7.92696 | -43.88535 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed40e100-fb0b-3ac4-9c4e-2ea7784f8f64 | -7.5618 | -45.49347 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45f0f243-c533-31ca-a7f0-f5523017aa09 | -6.56496 | -37.17856 | 2025-09-19 03:53:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2819e17b-910c-3af4-844f-d347bbf9ffc7 | -7.00345 | -44.64111 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec620f9b-9308-3b0b-8e9f-724ee065006d | -8.13644 | -46.77921 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 95b8f4cf-ef25-31f7-a1f9-ff509fd1be45 | -8.63593 | -45.71126 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbd7f80b-3e1b-3f3c-8281-c297e6539d99 | -3.27447 | -49.15186 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 938b91ce-59cb-3a2a-82e5-7d38a54c9437 | -9.13895 | -44.64148 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70ace37e-9bde-3385-bfb9-0ee42f85d1ea | -5.2146 | -42.3146 | 2025-09-19 03:53:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| de73f2bb-81ba-34c0-a220-ea65b4d3f1e0 | -7.45258 | -42.64502 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 36a3f438-73f1-3778-9200-69aa0773c467 | -9.17663 | -45.31928 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 39d1f6ff-1e5b-3fd8-9e2b-4236a4269c77 | -5.32689 | -44.99205 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff5f09b-4a77-31e5-8192-4658c2b03a48 | -9.14438 | -44.86086 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c59cc06b-f316-3c4c-a097-2a409fc9a12e | -5.15718 | -37.54474 | 2025-09-19 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5bccef26-8f24-3c1b-a3aa-b121672e8c40 | -7.18013 | -44.34678 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59bd0c91-1add-3ffd-b9c0-e9bdc0112b5e | -5.63479 | -45.95263 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d69ed9b-1474-3c20-ba9b-d0d82a384e58 | -6.32347 | -42.39052 | 2025-09-19 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c8da8ad3-f26d-3948-a503-8edd857d7366 | -6.81247 | -41.60377 | 2025-09-19 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c07d7d9-4a06-3857-8f78-a067d7877c5e | -7.18553 | -44.41786 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6e569c5-5d0c-3e17-9fdf-7208758009bc | -7.44812 | -42.6252 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 379f0d91-1a92-3a7c-99bc-3b2a21d6c0ca | -5.46714 | -46.68816 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0a27dec-62a1-3568-bb4e-882a2cdd1e8d | -5.08058 | -41.17633 | 2025-09-19 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 773ecf63-e5c4-37ac-b462-e0612aed47e6 | -3.68778 | -49.02521 | 2025-09-19 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e3eee4b-b698-3d5f-b7b1-1cc80fd5ddd8 | -6.95995 | -44.76094 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b019c50-a056-3def-837f-92f2d770469b | -9.32909 | -40.87397 | 2025-09-19 03:53:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b52bf336-d8d9-3415-b1ee-8f445cacb1e0 | -6.58159 | -45.58501 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d4419e5-4055-3890-9005-6909208f44e2 | -7.0042 | -44.63678 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d896c260-1db5-3d20-87f9-9f1c099a933d | -3.73901 | -49.05877 | 2025-09-19 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cc99c75-e829-3c7d-8880-17779c1f11c2 | -7.54846 | -44.78002 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7e9856c-d02d-343b-b34b-fc3fc9d67811 | -6.90389 | -44.77213 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| cb8ab2f9-1cd8-3e12-83e0-3cde7d09c413 | -7.99661 | -43.94186 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7835aab-40e8-3d02-a247-4de216faab8e | -5.8081 | -45.71368 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3a2c41b-0bd0-3fd2-9d14-456874085f7b | -8.13742 | -46.77349 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6dbdd918-9c66-3325-9cbf-776ef0d77d28 | -5.82305 | -45.91158 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 380f4901-7d9d-35f4-9f70-c9353cd5bab1 | -7.3565 | -44.58323 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 725b8dbc-8942-3006-a221-5165593faa48 | -7.58373 | -45.69062 | 2025-09-19 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8306e39c-748c-3381-9969-2d9e6ea23873 | -7.43975 | -42.62858 | 2025-09-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 066bd436-8197-36be-83a0-9498a6a6f267 | -7.84396 | -45.63129 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0fb30603-738f-35cc-a944-ecbb1c10be02 | -7.94509 | -43.87717 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d69a41b1-cc1d-3f04-bd89-de7f4d0e1bd7 | -8.13839 | -46.76793 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f3f2d52-4158-3ee6-9f5f-d2ac56d8154d | -9.14379 | -44.63842 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
