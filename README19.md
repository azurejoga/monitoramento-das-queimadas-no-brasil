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
| 6c2a4e0c-c130-3b48-88ed-2011dc24d9f9 | -4.07982 | -50.0417 | 2024-11-30 03:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bb94761-6685-351a-b2e1-8dfba7622bfb | -4.91161 | -44.02927 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3baad0ba-7f10-3a33-8143-6e7972f1d2fc | -3.43942 | -40.82881 | 2024-11-30 03:46:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66525473-4e15-37a3-98e2-5c318add3688 | -10.20929 | -36.64866 | 2024-11-30 03:46:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 10fba4b3-ccd9-3c59-8855-4596eab40d63 | -3.84061 | -46.52446 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0685ee06-6523-35cb-8d76-f2fc7060400b | -3.82393 | -46.55407 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95f96f72-1ea3-3595-be34-550b3153b437 | -3.55557 | -41.81618 | 2024-11-30 03:46:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e158b4f6-5181-38be-9240-4fe0ee341cb8 | -4.08021 | -47.02996 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8822f1e7-3bf0-3e4c-90fe-b02cb16b2432 | -3.98315 | -43.38966 | 2024-11-30 03:46:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5327ff-58e1-3536-9970-574680ae6f2b | -6.08094 | -48.05059 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc304000-51aa-398f-b0b9-fc85ca736318 | -4.44207 | -48.57281 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 79029ad9-34bf-321c-95c6-bd707581c137 | -7.12408 | -40.07597 | 2024-11-30 03:46:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d0c7c21e-395f-351f-a5a3-0dd8daf08cab | -6.94495 | -42.7878 | 2024-11-30 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a6db6e31-99ff-3579-a493-3d4db61717b9 | -5.96713 | -39.68347 | 2024-11-30 03:46:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4f018a8-57d6-3af0-9441-bc23bc5eba64 | -6.93742 | -42.83263 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6af34b3d-3740-36c2-a5e9-7e862a2bd06d | -5.94643 | -39.66398 | 2024-11-30 03:46:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59892a1c-d8e2-37d8-9340-811bf641a0b1 | -4.87403 | -41.29245 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 70c0761b-ecf7-3150-93e1-126a0bebb10e | -6.25039 | -44.97235 | 2024-11-30 03:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22d82596-6771-35cc-81dd-844513691b6c | -13.37425 | -45.13321 | 2024-11-30 03:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5e03ca5-3687-3619-95f3-0028cc0d48e9 | -7.21892 | -39.05366 | 2024-11-30 03:46:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a7c57e55-ab7e-3f26-b30a-3fd1d8422544 | -3.94557 | -40.97503 | 2024-11-30 03:46:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ddfd1828-a72e-3c94-9422-7f46e1a3ff6b | -5.49257 | -46.77084 | 2024-11-30 03:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac575c88-c3db-35b5-bc83-c418a9e1430b | -12.27358 | -40.35941 | 2024-11-30 03:46:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a8ddeefb-d3f2-372f-b37c-1434fcf4d224 | -9.44897 | -35.92277 | 2024-11-30 03:46:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be1b19d7-60b2-3ab3-9faf-a479140d51ed | -4.3846 | -42.14901 | 2024-11-30 03:46:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9639c37f-8c67-321e-bcfa-eca67991d7b6 | -5.58366 | -45.21135 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 378bae84-71f0-3e7e-a021-cf27b84f1c89 | -4.15668 | -38.69493 | 2024-11-30 03:46:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d88e033d-7623-3cb3-9361-66ee553250a2 | -1.68879 | -46.78609 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cf2d2c39-e4ce-3920-8683-d4f71667b12b | -6.68454 | -39.26287 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f587641d-14d0-3fed-9be1-7b32d0a1a479 | -2.70335 | -46.12751 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950bb43f-d2b1-3534-a038-36693790ae24 | -1.67845 | -47.85219 | 2024-11-30 03:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3eaaf7c3-7309-3f27-b028-fafc91655730 | -3.69527 | -47.13338 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b9fe001-6466-3642-9a91-7acbc9611a6e | -3.97878 | -41.51032 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67a9b0d1-46db-30cb-8d0f-55f8fb719d54 | -4.86332 | -41.30732 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 15eb1dd6-b51f-3b00-937b-a6fb13a6d0ac | -5.04412 | -43.62574 | 2024-11-30 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 090350a4-9687-36f7-9a76-36be4c7adcf1 | -3.9995 | -46.94762 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c98bd9b-75ce-3eca-819c-6b6f534916df | -3.83986 | -46.53026 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b190c623-97cf-3385-b47b-f312e7d7cf23 | -2.82452 | -45.29063 | 2024-11-30 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac06788f-0eb6-397a-8258-59c89e75fb18 | -6.90153 | -43.55092 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f97d108-dfbb-3912-a5df-4b8631000899 | -4.36618 | -45.52273 | 2024-11-30 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc2da196-266f-306a-a5e4-7f65d5ad0d11 | -6.91742 | -43.53947 | 2024-11-30 03:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cd607690-0bc1-38c4-81d6-c1e1434f13b3 | -2.75874 | -49.40662 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3233dfc0-635a-3492-9602-a5b606385420 | -2.59924 | -46.57302 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17607d5f-5713-384a-9ddc-148ee3bb2a21 | -6.08713 | -48.05154 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32837153-702d-36dc-aeec-a2439bd3eb7e | -3.69606 | -47.12878 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6aa6b52-7554-3478-bd7b-4cde811e797c | -4.07803 | -47.02584 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1029bd9a-b518-3c12-b201-e52138424fc1 | -4.64949 | -46.37088 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cbde194-d33b-33f2-b872-4a23a3fadb34 | -3.99237 | -41.50487 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 419d3a75-135b-3d92-b4b1-574b3d435e08 | -3.27525 | -45.57474 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f380c862-1213-3c84-bd01-5716f7230a25 | -5.72827 | -43.77348 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e992b2b1-fc9d-3b01-97b6-7ef99d522d9e | -3.70763 | -45.69549 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 69972b09-e7cc-34c1-95fb-176eef265124 | -2.51435 | -48.18636 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6702834-2a68-3ec2-8b20-378a3c4e1a7f | -4.37156 | -45.52367 | 2024-11-30 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 009c316f-fbb3-3e21-8958-3534f60f8afd | -6.07479 | -48.04943 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4b951c3b-724c-3a67-874e-503200f4d94a | -6.94102 | -42.83754 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6303c3b9-60cf-3835-9186-41e5dd1a157a | -8.0031 | -40.87991 | 2024-11-30 03:46:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90ce5f7e-9de6-3d44-8dba-2bee54ae8ac5 | -4.59051 | -44.70417 | 2024-11-30 03:46:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ca2e7e1-bc29-3a26-9b0d-6dbe5ab7df8c | -5.7274 | -43.77849 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ea0cf42-69a9-3a7d-b921-3cac2d53ec7b | -6.7891 | -39.44758 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39934ccd-9c92-3c3a-af88-dae3ff3e2c37 | -6.9084 | -43.5379 | 2024-11-30 03:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 22f2a66a-d8f1-3160-ba32-baee6855f742 | -4.01407 | -47.00482 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e73b174b-290f-3f71-aec0-16bcbecfe17c | -4.08106 | -50.03464 | 2024-11-30 03:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b19671a-143e-386a-a527-26039c90cc87 | -4.88199 | -41.29408 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d929c26d-82db-3a2f-9163-d320463b235a | -4.67271 | -46.37162 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d664fc8-dd4e-3e65-b08a-6f043eb1a984 | -3.10273 | -40.08276 | 2024-11-30 03:46:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 70cd5dc9-ab71-342a-8c92-59a823bf98f6 | -4.00023 | -46.94349 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eb6c7e5-8c6a-3f74-a874-c7f03d6d276c | -6.92411 | -43.55481 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 236cff99-2b9a-3c1a-b26d-6de153f06c16 | -2.18216 | -47.14829 | 2024-11-30 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61e861c3-2e3d-3a66-918c-d8405ce6c4aa | -4.87575 | -41.30693 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 450b266a-f160-326c-87eb-06198a2a0459 | -4.68149 | -42.37075 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abaddf78-7dae-335d-b5ab-a03b35d6d94f | -2.28232 | -46.43757 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbdc09c4-f182-3cab-b723-1418dd62d170 | -6.909 | -43.56162 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbe83d73-7095-3199-a44f-ad2372f76d2b | -3.96745 | -41.52772 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 45b5c1a3-7817-393c-8864-e171e9fa509f | -2.85122 | -46.69534 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6afea63-c9f1-3012-a371-afd45f4c61e5 | -4.86637 | -44.01027 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae0c0338-cd99-3c34-9b88-6cd4b58359a3 | -6.22984 | -37.22907 | 2024-11-30 03:46:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 608d48f9-65e8-342c-ac3d-f771c7a360ff | -7.14564 | -40.26274 | 2024-11-30 03:46:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c9fb76b-eba5-32b3-95d0-826744785f6c | -2.24297 | -48.26274 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba74292d-7c0a-3a11-9ae2-5e22389af32a | -9.13787 | -35.78205 | 2024-11-30 03:46:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7e454d3b-4c25-3cb7-b457-4812d1817864 | -5.50792 | -46.25468 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca55c0f1-bafe-3e11-a38c-3449cea696a2 | -5.58418 | -45.20823 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87a4d45e-0e12-3ef9-9d5a-127fc8415582 | -4.07697 | -50.03324 | 2024-11-30 03:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bedc3ffe-822a-307b-a1e2-bb326097c774 | -7.49913 | -37.00102 | 2024-11-30 03:46:00 | NOAA-20 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98e4d92e-79ae-3dec-b604-08ab4842761b | -6.9263 | -43.56935 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7e4582a-786f-3c89-9d94-4f294dea3930 | -7.21443 | -39.77275 | 2024-11-30 03:46:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 74915f84-b589-3a06-a203-822242437e3a | -2.30516 | -47.08918 | 2024-11-30 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4472bbc-28af-371f-a403-eef1679dd89c | -9.10009 | -43.19884 | 2024-11-30 03:46:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 10602988-d3c6-3a63-a82e-6bf58eae6703 | -4.83399 | -41.28551 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 719ee3cd-eb82-319f-9f58-103d3c671dd6 | -4.88142 | -41.29755 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 543fc249-eb76-36a5-8000-385cf0326c9b | -4.44862 | -48.57382 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f1575df-f0ca-36c3-93ef-4a0932beb3cc | -2.27571 | -46.44078 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67d35e3-5b6f-37f2-af94-72b54b18b9b1 | -6.92463 | -45.20351 | 2024-11-30 03:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6f93eef-422a-3443-be26-9523201334e3 | -3.67714 | -47.13026 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ab217913-7619-3b62-a402-a2cdca174525 | -6.9143 | -43.55782 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 94b81020-0b90-3ce5-b067-d09e2b4519fb | -2.52165 | -48.46465 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77fc38fa-db72-37ec-a66b-bc308b098410 | -6.92785 | -43.56014 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b8108d8-3dc6-3595-9f04-913f1e85ffa2 | -14.33523 | -43.5275 | 2024-11-30 03:46:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b874113-93a4-3808-b878-270940afd1cb | -6.40798 | -39.73713 | 2024-11-30 03:46:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c275c29-f526-3212-a33c-14d55e58e637 | -5.03885 | -45.24849 | 2024-11-30 03:46:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 03a8b270-d4c4-3441-8a8b-cc103579388f | -3.25835 | -48.8952 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
