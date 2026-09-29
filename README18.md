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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07834587-1956-3761-aa49-4a93f7c8e7a4 | -5.01348 | -48.04675 | 2026-09-29 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 52764714-abfd-3c2b-a2a3-55c1240d1f7f | -3.01612 | -53.86837 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a9deb12-e632-3ca6-aa80-d8e4d87ac311 | -5.74083 | -45.17588 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc01fbd8-50ce-330d-a5ea-1873882a83a2 | -7.72101 | -44.5705 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b726b13-2941-3025-bc3c-66d09e139269 | -7.38914 | -42.11497 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d587bc90-9934-3b34-adff-726c29f1e449 | -7.21715 | -45.08423 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c536b37-936b-399b-b830-2e713ab47cc1 | -6.16357 | -52.9125 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c02e30a-0a3c-3a19-9885-c7c3a48ec413 | -3.02151 | -53.87378 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 900c1281-4ead-3d57-baa6-d62cbb05d145 | -4.37343 | -40.62026 | 2026-09-29 04:14:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd77b0c6-bb0a-34ec-bb29-cd6d9da5e920 | -5.43135 | -43.44307 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2aa56a2e-e41f-3dc2-95b0-e918c3606e24 | -3.14478 | -54.07845 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09dfcd0d-4a7d-3698-8665-723dfbccfa23 | -6.69545 | -45.64109 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15d9fea1-da39-3775-bdca-da347ed0fdf8 | -7.4323 | -46.88311 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5488de4e-25e2-3f59-9e26-10f0e25d7124 | -6.72045 | -45.61784 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c77565de-2dc7-3c3e-a26b-a899ded9ffea | -9.05059 | -45.00536 | 2026-09-29 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd76e6f9-a79c-3182-944c-4b10be4532e2 | -7.24595 | -43.37311 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d725e6f1-1cd6-3459-a423-c239517e2822 | -6.7239 | -45.61839 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 819f8610-7ee9-3857-b651-8b9d1201329b | -8.24644 | -45.45766 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89d9ee2d-a8e5-3bf0-b863-6d4b235427e2 | -3.02231 | -53.86912 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e69ebbea-d4b5-336d-841c-1d00bd49c84c | -7.40604 | -40.22632 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9e6285a-a8cc-30dc-81c6-57bdcdbaea1b | -6.77094 | -47.15947 | 2026-09-29 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2e29225-9329-396f-89c8-81eb59844eca | -7.07453 | -41.74464 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8e849b1b-f45f-360f-9ffc-832e8f1b8d16 | -3.01628 | -53.86837 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85b76ac3-d1d3-3c60-98e8-5217fad2d752 | -8.43188 | -44.85123 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3b4fe56-915e-3ff0-8a4c-969bd9dd159f | -3.15714 | -54.08087 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96f6e0dc-23ed-3d47-bee3-ce932189f57a | -4.45743 | -47.9223 | 2026-09-29 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a0ea5445-d1f1-3d19-92f5-f8392f11c6ec | -5.73468 | -45.03765 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44cbcb55-aee5-33ba-971a-22d3987397bc | -6.38075 | -45.81046 | 2026-09-29 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25729ad2-29aa-3dc9-bb6d-380dd775edfc | -8.73604 | -44.92905 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a7a98a4-0fa2-3732-b281-32c9871bec16 | -7.42857 | -46.87944 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a6373a7-482f-3ef4-ab2f-bc72e7a3664a | -7.50584 | -44.55403 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaf4ebdb-b822-31b2-b0a7-d5640da0b59e | -9.76753 | -36.97758 | 2026-09-29 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 12.6 |
| aab27ece-fc4c-319b-8dbf-d659fd061bc7 | -5.52778 | -43.95562 | 2026-09-29 04:14:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb1a18de-f51c-3581-8f3d-9e893ef2c224 | -2.86891 | -49.0545 | 2026-09-29 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9967a3d7-7034-3543-8c5e-defe8cd23524 | -4.55436 | -43.784 | 2026-09-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb61deaa-2bf9-3dd0-b02e-801de135fb46 | -6.08178 | -44.00401 | 2026-09-29 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6abd03ea-cadf-3cd7-bc08-a7e9d710e667 | -7.21773 | -45.08059 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c11b63d8-9b99-37c4-8e88-82ebf8273557 | -7.72045 | -44.57404 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 510bc5fd-433c-33d2-beb8-2470c5210a95 | -7.43008 | -46.87404 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc38bf29-bf2e-32f3-bf18-937d03519a94 | -7.61214 | -46.45655 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 41728e0f-48cf-30c9-be23-390b11569ce2 | -6.31671 | -52.61922 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a97e1d19-e047-3656-bc13-08c503b424e2 | -6.32089 | -52.62702 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 82c43600-2380-394f-8df4-cd9fd955d35a | -7.84301 | -45.8223 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6939438f-768e-3759-96eb-43e312c3e7dc | -7.84363 | -45.81847 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a30750e-2a7e-3b63-9f0c-b682895cb613 | -3.15176 | -54.0749 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d75a19d7-3353-339d-a8ef-5b7d7929feab | -3.49928 | -48.56993 | 2026-09-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e7bd47a-2914-35ab-8424-f9e49d00a939 | -4.32247 | -48.63238 | 2026-09-29 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 588a7ea5-afbc-3f5f-950e-2aca34befb6d | -3.95901 | -49.04672 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2940064-1198-3357-be71-26d8374998e7 | -5.63518 | -43.72645 | 2026-09-29 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12f9ebd0-93b9-376a-95ef-ab9c3c369869 | -3.15095 | -54.07974 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1a8ea89-1e43-346f-a253-c9872d2709f0 | -4.55881 | -44.07991 | 2026-09-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b577855-f29f-37a3-aa94-ac71502e744e | -7.39195 | -42.11907 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9821d02b-0b48-3975-a852-9bf75d59feb1 | -7.01024 | -45.29898 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5101782-3dc8-381a-9ffc-54eab1415fb0 | -5.87091 | -43.59025 | 2026-09-29 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44ae93fc-ed66-30ff-83f6-e078174cfafb | -2.30084 | -48.54879 | 2026-09-29 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc483f88-19a2-316d-9eec-4118b0efe878 | -5.73458 | -45.17103 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e7fbb9b-177a-3758-a8c8-e0d384afd05a | -7.27973 | -44.30539 | 2026-09-29 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ebb042-0849-3197-a133-351d5a692d4d | -5.42643 | -43.45291 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80e657b6-b1d4-3398-9445-7abfee48421c | -7.2435 | -45.35884 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 314cca2f-2495-3640-9980-c445e352266b | -5.74143 | -45.17213 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8659a0a3-287b-353d-95a4-0e7cdda1e00c | -5.73916 | -45.05351 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f57e45ac-6366-3784-b4ba-6ec8c81cc64d | -7.50251 | -44.5535 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4ed6faf-8a69-38ca-aff6-5cecb010ce3d | -3.55623 | -43.00946 | 2026-09-29 04:14:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e7bdd7f-eb44-3860-a015-4e068d86c4b4 | -1.99795 | -47.63256 | 2026-09-29 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcc87897-a78d-3af3-b0ac-a49ffb1e9b0c | -3.99543 | -49.04391 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1a8fd22-ea9d-3e9d-8ac6-99b649e23100 | -7.40242 | -40.22577 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| da03bc14-6464-38fa-a3e8-e76e72744abc | -7.00683 | -45.29843 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dca4d35-7ea4-3b29-a86a-db98dd763eaa | -7.37857 | -42.13901 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77438188-9694-3a51-9e8f-1e93f2f542bf | -7.692 | -48.85999 | 2026-09-29 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e149a3f7-d3af-3be2-ae6d-d97687358895 | -7.38806 | -42.63026 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f307d861-9f15-3aa6-a169-0f7207430166 | -5.19441 | -46.079 | 2026-09-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a751bcd-db4c-3f54-a420-4a903cbfc7ab | -7.51467 | -47.33951 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| de8ba0a8-ce57-3efd-bb54-73185045e48f | -8.73105 | -44.91745 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f18b4d4-ec4e-3b2f-8276-c526912979e7 | -7.40666 | -40.22208 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4b5cc64-c4e8-3c62-9623-0071029b5ea5 | -7.26414 | -45.33928 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b908ecd1-0dcd-330e-a585-c395dd824204 | -7.6082 | -46.46042 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70654270-8168-34cb-a86e-8c1e56f023e2 | -7.38752 | -42.63377 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 153830ff-c507-36c2-91cc-9237a0b2c925 | -5.48546 | -45.12514 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f44a82cf-bb40-3acc-bdce-09babde37723 | -3.02309 | -53.86457 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86e8e6a3-3983-34c7-8a9b-816d8873b200 | -7.0885 | -46.71032 | 2026-09-29 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c62657c8-cec3-3e86-93f3-70f242ee2b54 | -8.22029 | -45.46867 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bf400de-d242-3037-9f11-faa0cace2e85 | -5.61017 | -45.00345 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d2f5221d-39a9-382d-8b37-f15a43da2481 | -3.70609 | -54.22683 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26349fe4-d91e-3323-94b2-ea71be63eb4c | -14.21558 | -48.50941 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2b55ed7-a18d-3d10-aa89-2b8f057855bc | -15.08762 | -48.33569 | 2026-09-29 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f7d375a-cdec-343b-9743-4659701523ab | -12.01533 | -50.97062 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17c60a59-4f6b-3202-9513-af05242db23e | -11.43313 | -43.47514 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2741013c-cf60-3a5e-985a-34339d307393 | -11.41915 | -43.43277 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1649d336-5938-3d8a-9f90-01eec281dd6f | -12.26855 | -46.48788 | 2026-09-29 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c286a9b-fbc6-3b92-920f-b69269babbd7 | -14.51055 | -52.48354 | 2026-09-29 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23040957-98ec-3c4d-a09e-fd4dd1308872 | -21.24124 | -45.3746 | 2026-09-29 04:17:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a2308d13-4559-3ef5-a15e-e654cdddfc6d | -15.45734 | -46.13206 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd541413-a4ba-32c0-8cdc-92406af6278e | -12.00788 | -50.98703 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4f5608e-0f5c-30f9-bd74-c02cb2921ec2 | -11.1298 | -50.06835 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 363d1111-a756-3888-8db0-fdfc58a6d3c6 | -11.42363 | -43.44808 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7be9f56-8006-380c-8889-ece020ba90b5 | -11.38998 | -54.04205 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1e3fa1-d2f8-3f4b-88da-32774bdd2e71 | -9.76927 | -44.85336 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b14565a1-6c98-3e45-ba66-bbf48be49446 | -11.67736 | -44.53418 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39005331-9e1a-39cb-bd5d-268b6e6f9f17 | -12.7024 | -47.37184 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27b799b1-cff2-39a0-ab26-7d2069d394d2 | -11.96772 | -50.93536 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
