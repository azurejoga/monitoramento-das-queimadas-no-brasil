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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d7915f-494a-3802-885f-cc56bd7057fd | -7.05543 | -43.9594 | 2025-07-14 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a026677-0bca-342b-ac38-014bf0168a19 | -7.02071 | -44.37511 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6837c69f-1b61-3e0a-8cf5-56d5d2cdfd66 | -7.02302 | -44.38474 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c3581d-1e4d-36e2-b664-dd640d9322ac | -9.49871 | -47.56658 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 67f7ec4f-9532-3563-8b8d-ada24fab43f6 | -6.84253 | -42.76778 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e627dab7-dd59-35eb-9ca6-604ddf4d0cc6 | -11.58397 | -47.32716 | 2025-07-14 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88c91c3d-e982-36d7-9647-82926cf4b0bd | -6.46239 | -45.36197 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8887164-79b8-3166-913b-34dff7f0e425 | -9.38891 | -47.97146 | 2025-07-14 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6e2ec1c-57a8-38bf-b211-c0879f8804a5 | -6.14376 | -44.0864 | 2025-07-14 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38269cca-7bb4-3d92-85ce-4345a90f0f43 | -10.66008 | -49.4434 | 2025-07-14 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62c2857e-39c9-388a-975a-77c77aeec433 | -7.58752 | -44.72454 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27de9750-4d5b-3ccb-9e4d-46bedd8069c9 | -4.30506 | -48.10249 | 2025-07-14 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 923aa854-59be-3d36-8713-4f0f7dbbfe12 | -8.24896 | -41.69035 | 2025-07-14 04:02:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6113b25a-1e6b-386a-bf5f-67338f7acdf4 | -8.23587 | -44.91684 | 2025-07-14 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 067b324e-076c-311b-86fb-11e0134f6d3f | -6.8454 | -42.77229 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eda3650f-a3da-3a8c-966e-847a31284133 | -7.26589 | -45.31072 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9eede589-233b-3749-88cb-d115594854d2 | -7.02685 | -44.3617 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63905207-5d1e-32f5-a35d-f7b47f38330f | -7.29093 | -43.04467 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40bcb7e8-4354-3b64-90fd-01b389bfb357 | -7.35629 | -44.62828 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6047761c-c126-30bc-87ed-dbe6103097c5 | -6.8176 | -42.83226 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44d0130d-01a5-3668-90da-4ec373ed6824 | -7.02148 | -44.37049 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aac70119-9385-37ef-9dbb-7fe730f7b6f7 | -9.49198 | -47.56733 | 2025-07-14 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ffeff660-703f-3141-bb1e-246bd42dac7d | -7.54238 | -43.9467 | 2025-07-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53dddcfe-032e-3c52-81b9-07bd1c9009f7 | -6.74901 | -44.69961 | 2025-07-14 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c97ad34b-9e56-3cca-b7b5-69bbd200420e | -8.51529 | -43.30456 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| c6080ac8-e6fe-311b-a4d0-5db63997e1b5 | -6.85434 | -42.76154 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18616ebf-1667-34f4-9e39-94fd211e6dfa | -8.2681 | -35.85347 | 2025-07-14 04:02:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c596f99-0c23-3671-a179-d91adf62b6d3 | -4.86466 | -43.22508 | 2025-07-14 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2a746cb-c35a-37db-b514-013f42bbbc36 | -4.24843 | -46.63136 | 2025-07-14 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75fb1df3-c0c8-3dda-b4d8-f2c0505e1705 | -7.5807 | -44.73076 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b7944dc-8f27-393a-bf32-18d2be9c9a28 | -7.548 | -45.05213 | 2025-07-14 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c2b108c-7849-325d-af01-505ef368b507 | -10.99567 | -47.08167 | 2025-07-14 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 758b00d0-d13d-32c3-8b3b-937e4aac4caa | -7.27114 | -43.49755 | 2025-07-14 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22b32e1c-4164-3782-92d5-4eae2a6d2a7e | -6.82937 | -42.87071 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cab4b78b-621a-360c-bb6d-7eafc2f28bb9 | -6.43277 | -45.33865 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50109943-a9eb-3887-b553-ebac8d5963d3 | -7.02762 | -44.35704 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88ae0756-06f3-3fef-96c5-67493308cdd8 | -10.28314 | -47.61626 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 420e4216-572f-3651-a1bc-11c7b3d6a38b | -5.25277 | -44.46786 | 2025-07-14 04:02:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c4d3cb-39e4-3907-ab86-ad05aa90d97f | -7.26406 | -45.31363 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a946d75a-2eaf-3839-8d12-cee887e4ea20 | -7.58203 | -44.73355 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10f9a296-f6f2-3f42-87b1-e391e466a91e | -6.27194 | -43.41059 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f8ef9bb-b382-3fd8-8370-bd1bcc92a59a | -6.94669 | -42.73138 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a2cd5b4-2186-3def-891a-8288143917f1 | -9.45864 | -40.37933 | 2025-07-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 24e79dcb-6369-38cf-838a-b729033e0842 | -7.04899 | -44.32215 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ca24b57-4f46-325b-adf3-62e396b34e70 | -7.16747 | -43.00088 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6f79373-9e41-3a25-9567-2bde20216982 | -6.83354 | -42.86731 | 2025-07-14 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f3fe9c9-6878-3788-b05f-e6d5f778055a | -7.05546 | -44.02775 | 2025-07-14 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a20b362-c0f5-3515-b958-e82fc5dcae92 | -6.27279 | -43.42804 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9aa01da-a9b1-3cb2-a6de-a175df243e45 | -7.01843 | -44.38884 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 102464f0-9068-31f1-a607-77846291515b | -9.48769 | -40.39141 | 2025-07-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb6e434d-3bd7-309f-b8ea-888bda47c172 | -7.26464 | -45.3101 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4762199f-a75b-3382-bed1-87031842f42a | -4.86848 | -45.31539 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16b4a0e4-7861-3a62-b952-a2f979ff4089 | -9.41755 | -40.46923 | 2025-07-14 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86934ac2-0c32-3be0-8e65-2aa34404a860 | -6.81754 | -43.72215 | 2025-07-14 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f25420bf-1e08-33d8-98c6-be7e92ba5d04 | -7.3081 | -45.35418 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a63478-0756-388d-9349-b5a22e0af54e | -8.91279 | -47.35055 | 2025-07-14 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ded95894-3076-3e16-adcd-728979e3e308 | -6.96352 | -42.73814 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3d40e14d-a30d-3299-8208-686602c39e71 | -5.27249 | -45.12847 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6848cf4-a023-3455-8b19-d4a2c0ecfb7e | -6.27198 | -43.40746 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b09eef-ad68-325f-8885-45dd5df0e668 | -5.74749 | -44.9852 | 2025-07-14 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95ff76c-6d5d-3f97-9392-9d9d25bb594e | -10.55534 | -45.11345 | 2025-07-14 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e1241a5-2ac6-3f46-ae45-f4095bd11994 | -6.1217 | -44.22269 | 2025-07-14 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be40ddc3-a50d-34d3-b7eb-18e22227076a | -7.2693 | -45.31488 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b66c2f1-1b76-3069-b9ef-d7eba490b2bc | -6.41352 | -42.42994 | 2025-07-14 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e20ec57-9686-336e-a9fd-2c214ffc9fc9 | -7.579 | -44.72808 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7abf325d-80a9-3a5a-815c-f2102e1ac493 | -6.26809 | -45.27354 | 2025-07-14 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 276d2b7a-18d5-374d-aabf-7bdeba8ba6d4 | -6.87697 | -42.77721 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34942cf3-a48e-34a6-a42d-8106581a29e8 | -8.04432 | -50.0974 | 2025-07-14 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1835d627-6868-3996-ac9d-2461f279d59f | -10.82416 | -38.57954 | 2025-07-14 04:02:00 | NOAA-21 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b813645-9124-3f68-97bc-6097cb3e8e8f | -7.27111 | -45.30431 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ccd1c6c-90cf-3070-b455-2246ec1c26d1 | -5.86956 | -45.15638 | 2025-07-14 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d4ad6be-9e4a-3ae1-b8b2-d731a6466f1b | -7.26348 | -45.31718 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 54e2cc1b-0428-3aa2-97a3-c29acc49c0ef | -4.86692 | -45.3157 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68ddac77-cb0c-3c36-badf-b6ec699a931a | -7.58534 | -44.72655 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf8cb6dc-e3ec-33dd-a4d5-a65b02ea33ea | -7.59747 | -44.73592 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7686c23a-c8b2-34e2-9fd4-723c83088398 | -7.05279 | -44.3227 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c824d3-01d5-3b54-9dc2-77c11c84274e | -7.26871 | -45.31837 | 2025-07-14 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07f140c1-c189-3473-bcd5-efa13fd37547 | -11.5956 | -43.2058 | 2025-07-14 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6158ede3-9347-3c85-8cd7-81f1cac338de | -8.51594 | -43.30058 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 64b7afd4-7f53-3074-97c1-06196804dc64 | -7.26753 | -43.49697 | 2025-07-14 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c067d747-0423-3c31-88bf-063f1ab296dd | -11.2267 | -46.41964 | 2025-07-14 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b88bc907-54db-33de-8d14-f6ea392bc64d | -7.58455 | -44.73138 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 868b9eef-1acd-3b62-88b0-1a15876db4d1 | -4.11174 | -47.9282 | 2025-07-14 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33aeecb2-bb36-3be4-ad27-ac4e172de149 | -6.8264 | -44.01847 | 2025-07-14 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| defc0123-6a96-3954-a1b5-2390c01cce95 | -6.2713 | -43.41166 | 2025-07-14 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65223501-fdba-3537-b7e5-a83414f5a66e | -6.25767 | -43.35722 | 2025-07-14 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67e5a18c-22a5-3f0d-8adb-020b20203ce5 | -8.51816 | -43.30912 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3564ca5f-8cff-3558-bc30-153abaacafdd | -7.01919 | -44.38426 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a57d9b5b-c962-3e66-a3c9-4e26456ea46f | -6.12094 | -44.22737 | 2025-07-14 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 068ea8ad-e507-341f-a01f-df544c78a322 | -8.51464 | -43.30855 | 2025-07-14 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f24ba42f-8fe0-3337-80f3-dfe3f70a145a | -8.24879 | -41.92955 | 2025-07-14 04:02:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bd9daa44-ae3b-35d7-83bd-ff87595d4a86 | -8.87649 | -46.91238 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7fca8c7-fbaf-3201-9434-d82b0161a5c1 | -11.59901 | -43.20637 | 2025-07-14 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1201822-5702-3bae-aaac-c9a250851614 | -6.46587 | -45.36628 | 2025-07-14 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95d6bd0c-efd8-3d02-9954-155caf3cc8eb | -6.94255 | -42.73473 | 2025-07-14 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27708202-98f9-32f9-9ad7-51295a034918 | -8.87722 | -46.90823 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 176ab9de-549e-34a7-8686-15d73b174a5a | -11.58469 | -47.32306 | 2025-07-14 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dd5f9364-56a0-36bb-bd8d-f83cf8ff8828 | -7.58671 | -44.72929 | 2025-07-14 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24fcb241-15d2-3139-9a4f-c81003426373 | -8.87361 | -46.90326 | 2025-07-14 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c30e05-6b08-36d9-a57d-3d69ad31ab03 | -7.03981 | -44.37773 | 2025-07-14 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
