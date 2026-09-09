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
| f96a62a7-3675-3486-b809-911f0e3abe83 | -6.76009 | -44.57032 | 2026-09-09 03:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c01ef4b-a799-39a0-a72a-8aaa6fda6023 | -12.85614 | -44.39771 | 2026-09-09 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a6b221a-38e8-3a95-a647-fbd9bc02538b | -9.77242 | -43.45025 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27899fcf-d8da-3d33-89cd-c9af6e028b6c | -9.69904 | -43.4458 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96c324cb-1e04-30aa-b1c2-f39e4176d0e8 | -8.09817 | -45.67678 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26d31093-10cb-3640-a3fa-c5e317b84240 | -7.30841 | -39.26383 | 2026-09-09 03:49:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| beead895-7288-31a7-b3eb-ddb44680f79f | -12.13689 | -38.05895 | 2026-09-09 03:49:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bacb91e8-4f99-37d8-afb1-7b12bbb89cc8 | -7.2636 | -45.3521 | 2026-09-09 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22c20ff4-27f5-3bdf-a298-d1b5399c3b5d | -7.13136 | -42.11912 | 2026-09-09 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1294e89-57a2-3fd2-8822-b11613682649 | -12.38159 | -40.58331 | 2026-09-09 03:49:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c35ffd23-d3bb-3390-9a6c-e73a0e6e4e03 | -9.84242 | -43.31873 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e63dc46-8781-307e-9be8-29d257cb6a81 | -9.77973 | -43.50812 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbdfbee-a897-3ae3-bd83-bea274478444 | -5.7698 | -45.08141 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c556347b-b4c8-3de7-bb56-29131484ed92 | -8.84819 | -36.53037 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 12f4626a-21ef-3246-b9fc-928fedabcc25 | -5.77181 | -45.06993 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d3e37d72-c064-3574-b777-9885040e63a0 | -10.10694 | -39.06948 | 2026-09-09 03:49:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07f7f7ff-ebd1-3308-8163-b3c2a06dcb1a | -5.37399 | -49.14806 | 2026-09-09 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2aa2721-33a2-390a-95e2-40dd2aeeaf65 | -5.37907 | -49.15065 | 2026-09-09 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0de9d85-8db8-3141-a959-28d677b80a74 | -9.69507 | -43.49427 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26a05b04-c3fa-36b4-86b0-51a5d8eba65e | -9.71644 | -43.4728 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4d53c90-c311-31ca-949c-ee5383b07bc6 | -5.77585 | -45.0764 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 09aca30f-670e-34f4-be04-17c77cbff3a8 | -7.31185 | -39.26437 | 2026-09-09 03:49:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f7c8159-3a3b-3a85-bb4d-7d3b806493ac | -11.18521 | -40.88451 | 2026-09-09 03:49:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5d29eea-c0ff-37dd-81bc-d24504bc188c | -7.19282 | -43.62622 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 080c6c6d-0705-3283-8e7f-312f68f1a6b0 | -8.85152 | -36.5309 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5e72932-4ce9-378e-9880-c03aaf5b1c39 | -9.70502 | -43.41089 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ad02f45f-37ba-3e2e-b2cd-6d388366af19 | -5.77232 | -45.067 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2b09402a-f421-3741-9302-635e534c1b88 | -9.71598 | -43.47354 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7df2bf5-5a2f-38ed-8d23-4bf1727078b4 | -10.71886 | -46.05553 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8b31705b-4dc6-3ed4-9099-de2e21b3b602 | -11.00531 | -45.08127 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| da0cafe8-fde4-37ed-ba80-ccb1fadbbe36 | -6.1593 | -44.66185 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4d27c901-eaf6-3c3b-bf84-7ad2ba669d3a | -5.76475 | -45.08075 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 07bf803f-e116-36c3-8dfd-a877cbe54b3e | -9.69969 | -43.44197 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d9b920ab-fdcf-3a05-8379-b15c905db3e7 | -5.77031 | -45.07852 | 2026-09-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d179bbc3-1f8a-37cc-837e-7147860ea344 | -6.16234 | -44.66437 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3bfaaa1f-4a82-3aae-81cf-023223db3bdd | -11.39528 | -43.92318 | 2026-09-09 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89b3a05f-f8b4-32f0-9734-9d21908512b0 | -11.53852 | -44.89624 | 2026-09-09 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5bf65f8-76fa-3983-96ea-aa284f7e82bc | -9.7026 | -43.45033 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6ae56fd-4494-39ad-803c-a67233769279 | -9.77459 | -43.4627 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d7debcc-ea60-3077-b940-3cfcefe9ef0b | -6.16593 | -44.65201 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 953c2d66-9da9-3acd-80f7-6bd41cf85f0d | -6.62353 | -42.22728 | 2026-09-09 03:49:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8364f978-21e3-360f-b372-aacb4c23f0c9 | -6.16503 | -44.65738 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0816868b-fead-3eb9-b3b7-c07f0dc07bfe | -12.27384 | -45.8166 | 2026-09-09 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcf4846a-56f6-3111-a6c4-940178d7b33a | -11.32203 | -45.75495 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c07eccbe-510c-3a7e-8a4b-822e8b509aa3 | -5.41794 | -44.79136 | 2026-09-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a29a438a-8eed-3eb9-a560-fa200abc9b90 | -9.72019 | -43.47431 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5802db3-d906-3d56-8d36-a34e969542f2 | -8.85098 | -36.53445 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dce14c89-d80d-3791-93ea-8dbb5b0d6fe0 | -10.36701 | -45.16574 | 2026-09-09 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 807bc6b0-2cde-3c9e-b10e-7104a0601e40 | -9.74881 | -43.51093 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9889497c-8ed5-37e5-8ed3-88e21b3346aa | -9.70167 | -43.43045 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8486d349-67c5-3bb0-976e-4269e5a0a2f2 | -11.42852 | -47.68316 | 2026-09-09 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 421e55b9-d807-3245-9ef7-322f22e64446 | -6.16682 | -44.64663 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ef7f03b2-cfbf-3778-9cb3-b087bc1e651f | -9.71056 | -43.40374 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 06ed7e7d-2efe-360d-9e01-df54a3210dd2 | -9.25741 | -45.65797 | 2026-09-09 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6abd3d19-10db-30df-afb7-ef2aae278682 | -10.37078 | -45.17163 | 2026-09-09 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33900b3d-c2c8-3c61-8cfd-28f4eb9b4011 | -9.69846 | -43.47453 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 890b1224-24f3-3a0d-a23e-bae6f72d111b | -5.73827 | -43.27943 | 2026-09-09 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f77703a-e195-32c5-bd8d-0a6a02428505 | -6.86521 | -46.0149 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 556f624e-3571-3ed4-b938-43be84957998 | -9.71127 | -43.50124 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 505512a5-4794-3a26-a5f2-610c685257eb | -5.83713 | -42.28171 | 2026-09-09 03:49:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 24cf2f8b-4edf-3297-8518-56412c4e522c | -9.78401 | -41.99996 | 2026-09-09 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cf189de0-ed23-30f8-a3e3-fe3fab39bc54 | -9.26229 | -45.65902 | 2026-09-09 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f7001db-455e-3d9b-bc07-577598ec9e14 | -6.8704 | -46.01616 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2df6dd50-3b21-3acb-83ca-7ffc78c61a6b | -10.4705 | -40.57482 | 2026-09-09 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8bb633d-20fb-3416-8d2a-0387ff5c7daa | -6.03315 | -42.64236 | 2026-09-09 03:49:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 35b98085-b201-36ed-a6dd-0f01bea0dee3 | -7.5288 | -45.92763 | 2026-09-09 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d33f55e7-552e-3cd7-8ec7-5f104ff6af5f | -9.77483 | -43.51134 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d378cd75-821e-3258-ab96-9616467a4ede | -11.54061 | -44.89587 | 2026-09-09 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade79d2a-89c5-353d-9f60-cf4058eafdf4 | -9.71951 | -43.47828 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8040c559-f014-3cd4-afe7-b11d849286e6 | -9.72583 | -43.39011 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e10d554e-dd29-37fa-987c-c24747e8d7fa | -7.19908 | -43.62296 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 039a3415-849b-3047-8ab2-d729da7fa89a | -7.19538 | -43.61776 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 94fc35f5-ef31-39d3-ad54-5023a09002b0 | -6.761 | -44.56506 | 2026-09-09 03:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bd5f015-76fc-3d78-bb8a-36be51db7bfc | -9.50193 | -41.99361 | 2026-09-09 03:49:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c78030cd-9e81-35d5-a33a-10ba42aa7f7f | -6.16514 | -44.64829 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bec8da25-d695-353d-81bb-79a2eed20ef9 | -6.86626 | -46.00885 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3dff3b6-c55d-3edc-acd8-712eb7649b37 | -6.36696 | -43.59155 | 2026-09-09 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8434a2b1-7cb0-3400-a291-fe79bb66d754 | -8.42083 | -46.8956 | 2026-09-09 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d31b6c6-af85-30e7-9319-e83a9990260a | -8.21389 | -46.00593 | 2026-09-09 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a12ec98-43a8-3fd1-8ebc-7d9f16265bbf | -12.43596 | -43.41652 | 2026-09-09 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 768e2ef1-5384-39c3-9cb3-cb9979d60e29 | -10.99441 | -45.08906 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5da7570c-480a-341e-ab4e-7f1ce1b83222 | -10.17677 | -36.30504 | 2026-09-09 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f993a360-9435-3849-aaff-5261c9c1832e | -6.36249 | -43.59066 | 2026-09-09 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5974f855-2ee1-3f79-ae6b-5bebec5ec59a | -10.75492 | -45.96941 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ebd348f-dfba-3ebd-9ec1-bb7a0dd9ed3a | -7.1996 | -43.61354 | 2026-09-09 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f574f69-0137-3265-aca7-54157fb55f12 | -6.86986 | -46.01923 | 2026-09-09 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 925a9812-1c13-35aa-8122-4f8a93a8a04a | -6.16414 | -44.66274 | 2026-09-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e3f63041-b2f4-306a-ab5f-8ecd06b9bb68 | -9.70035 | -43.43816 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d43528c0-b2d2-3556-9bfa-d75970478c9a | -7.68448 | -44.32286 | 2026-09-09 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a0cefb8e-dd32-310e-a6f0-211aa8bb51c8 | -10.14314 | -42.13385 | 2026-09-09 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5f3375cc-1074-3c3e-9d9e-ea62ffda4e25 | -9.70435 | -43.41483 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| da152c8a-34f3-3e5a-8af0-517bf3ea33f4 | -9.76669 | -43.40869 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb4c597-7368-3c2d-9f63-023889006a00 | -9.7153 | -43.47752 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf73707c-0a62-39ce-9d26-8feb70323b91 | -9.78098 | -43.47583 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e786e01-adc4-3b5c-a616-5452ca7f5516 | -9.69771 | -43.45357 | 2026-09-09 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 54a1c250-3a26-3bf6-b555-15d9e885a2af | -10.71991 | -46.04985 | 2026-09-09 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9e322ab9-36b2-3249-8d12-c7e15d3c396e | -8.84486 | -36.52983 | 2026-09-09 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 791bc590-6487-3d4b-8dfc-7ddfda5fa83e | -2.9392 | -50.4622 | 2026-09-09 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b9df3319-f9fc-34f0-9fbc-f7f743e954c7 | -2.9391 | -50.4832 | 2026-09-09 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f5a23ad2-b42b-32b3-8132-871c6098c754 | -13.41044 | -44.17833 | 2026-09-09 03:51:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
