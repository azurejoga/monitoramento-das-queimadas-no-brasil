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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1118f7fe-8507-36e5-995a-055d97ac5a24 | -2.82279 | -50.49901 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c762d9b1-b440-3ba0-a35f-5544ad5be6c0 | -2.75484 | -51.55576 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8ed8143-47ba-3c86-8427-ad00e006440e | -3.51606 | -54.61805 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ac437e4-2591-3dca-a31e-c51620ac9339 | -2.59928 | -51.8497 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf3bca55-8f08-3982-903c-06603be33022 | -7.08975 | -41.74483 | 2026-10-04 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea52f48a-032d-36f7-b72e-2a0abd984c53 | -3.07323 | -49.54428 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 13617fdc-f239-3867-91de-f6d452088992 | -6.00334 | -53.52713 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d566cd22-0854-3792-ac18-ea01066995d3 | -4.14371 | -46.82806 | 2026-10-04 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 868728c9-7936-3e88-b26b-3989fa975951 | -3.1252 | -53.73352 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fd4afe1-6433-30fe-9c69-aff52a9bb77f | -3.10695 | -53.74163 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae3ff655-eb4e-322e-95b7-66e69d75593a | -4.1076 | -42.5016 | 2026-10-04 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6bddecac-c347-3d49-973f-b3d5497c9b52 | -3.51673 | -54.61401 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e237ecc-d57b-351d-a3b1-a2a3f2e7e301 | -2.90312 | -49.40332 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 205e791c-22cf-3fa0-9850-6f8e943fc889 | -2.89025 | -54.11879 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 297d6480-bb54-3cbd-b19c-cccb401c04df | -3.18201 | -54.07586 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d574709-a8b0-3a22-901b-b4fb8a795692 | -5.00833 | -45.14172 | 2026-10-04 04:19:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db331ef1-447d-3f9f-b36f-2b7786f20a03 | -0.34707 | -52.05569 | 2026-10-04 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9076e4d-6cf7-3b3a-b485-f204a6fb2e30 | -2.95231 | -54.12918 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aaac2692-66f1-34b5-ac56-d1f764098731 | -4.13578 | -54.16422 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c921941b-6bcd-339c-8a72-ffee668726f9 | -4.45359 | -47.92559 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa897548-724b-3cbc-b0d8-1a663d29ba75 | -3.17756 | -50.53778 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5e55097-925c-34a0-9790-1efad7f9a5d8 | -3.19313 | -54.10223 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4affeb0e-a97e-380d-87c2-28e7bcc39611 | -4.25516 | -46.36864 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83138777-0793-3e85-9753-24764d1e6656 | -2.44232 | -49.02514 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8072f796-cccc-332b-92d4-eab92ad0c34f | -3.13557 | -53.73894 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf9fb01-b545-36e4-a811-aa2fd7c36fc8 | -2.81087 | -42.31002 | 2026-10-04 04:19:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d13e198-8716-339f-b6a0-73b3855c370b | -3.27877 | -53.83389 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 487aa79d-f7dc-3912-94e8-8bf1b23cd414 | -4.27204 | -50.26781 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3fbeaf5-3681-331d-95e5-1c751a5edf79 | -2.21071 | -48.22647 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93b69fed-f821-39c4-b8aa-aa0c1d8d4ce8 | -3.89112 | -49.70011 | 2026-10-04 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6684eec2-193d-37a0-a214-d4f89bef0e47 | -2.77642 | -57.68717 | 2026-10-04 04:19:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d85497c-a407-3fe5-ab24-da86586f9da6 | -2.2136 | -48.22445 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 376e37f7-0adc-38f0-b9e7-acfb3068b80c | -3.10755 | -53.73805 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bbada335-4f29-3c18-9fba-8c5d08954ec5 | -4.46679 | -50.97061 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b472c4c-8a50-31b3-9771-07f97bb6a6a2 | -2.88631 | -54.1421 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ee71ce9-dd37-3efd-bd44-71cc3d91e8ed | -3.01488 | -53.88781 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 823cce10-767d-3f66-9520-0fb1a84d51fd | -2.92966 | -54.16087 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cba36e5-011f-3480-9734-eb6c47a48577 | -6.06599 | -53.47183 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d8e0bb6-1126-3f5e-8282-304d5f5f2dd4 | -3.00809 | -50.46883 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fae6a568-7027-3940-b241-f4cce4a99317 | -1.46301 | -49.46961 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54607b8d-02a6-3567-bc17-0d66cd315ba1 | -2.97548 | -54.08102 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bfc5d85-95dd-3ee9-bd23-a95f7b797236 | -5.22753 | -48.41331 | 2026-10-04 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9381bdd6-2aed-3f90-aee0-431bf56aab9d | -3.20719 | -50.74874 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7ce46cb0-da34-3518-9cea-306d2091bc47 | -3.36348 | -43.38382 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b6c3f4e-ce7d-3a80-8c82-a4fddacbdbb1 | -2.82911 | -54.11935 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e248c6c0-f492-36cf-a1e2-bf4a4626adb3 | -2.82473 | -54.11074 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02ae2480-314b-3b6f-ab28-518bc504c30f | -4.29035 | -50.26265 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 86243224-dc65-37ae-93f2-60f155a192ee | -3.46789 | -50.0898 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| de3c1cc4-3e66-3954-aaa0-5ae206cb1067 | -6.19739 | -52.79584 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba345f0-35fe-36c2-b925-bef01fd55b98 | -2.56239 | -54.72515 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f434b25-fb1c-3ef3-a5d9-befc0f75f9b7 | -2.80714 | -54.11183 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 275d6391-1c3b-32d2-a655-40f17542b3e4 | -2.96804 | -54.10397 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e701d8f-2524-3ca0-9764-c849dbbf50cc | -4.46091 | -47.92675 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dab9eb8f-7a77-30f1-b894-74c199f6ec71 | -3.18753 | -54.10121 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9199b35a-83d7-3724-81fd-9dc8c791c486 | -2.79211 | -54.09764 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91f85d58-3531-3ac8-be56-baac6af5aa13 | -2.7504 | -51.54791 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad33cf94-8848-3a32-bc31-d2d4c0648d64 | -3.11422 | -53.73178 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7f649359-1b71-346c-a59f-a481b58e64f3 | -4.26343 | -50.7486 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b19755-fdce-317c-b07a-63d20b651f65 | -3.07735 | -49.54494 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d93073b1-19a8-3e7a-8076-4414230432f7 | -3.3607 | -43.37983 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5316967c-ca2f-3ec7-948b-e3beba2ef370 | -3.0803 | -49.55303 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f41b34a7-6e20-36c2-886f-0b6ebebf50c2 | -3.17025 | -54.07731 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46fe5cb4-2752-3243-bb68-00dbcaf24922 | -2.7813 | -51.36855 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 091c878a-052a-3af5-b3b4-cc12e6916972 | -3.18267 | -50.53418 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6156bf73-f88c-395d-8f2b-d66a0dc57faa | -5.74203 | -45.14794 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83b7730d-56a6-3014-b9df-abc3d5b9c7ed | -7.25143 | -48.06343 | 2026-10-04 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4a9251f-be7e-34ad-aaa2-3b94635dc1dd | -4.44237 | -54.96653 | 2026-10-04 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65af508e-a740-3a48-8469-41757e228b74 | -2.80391 | -54.13111 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 379793e5-39fe-3b0e-abd7-2f9a026de7d7 | -3.15917 | -53.06895 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 429e1e32-2edd-3ff6-a25a-336c02a66e80 | -4.26779 | -50.26717 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 014652a3-0c45-3775-9c84-c8774709f0d8 | -2.22341 | -53.70554 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 415b365c-99ea-3e52-991c-c82f244bfb17 | -3.07264 | -49.548 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c398fb80-86dc-3261-8bcf-28cea730fa19 | -6.07579 | -53.47634 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4f7a141-9e20-3842-beba-643d149a76f4 | -5.99377 | -53.64194 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bd5ad4a-38f2-325a-8710-e4773df7c87f | -4.45725 | -47.92617 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2fe2af-0508-38bb-8d11-9fcc032f1acc | -3.30576 | -53.84168 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13963b55-d95d-3626-a0bc-daf9c8671f2f | -1.12315 | -54.15233 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83941960-e239-3692-965a-5734fa4f2590 | -3.08447 | -49.51926 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61bbf913-a04b-3f91-9193-d47f5f27e65c | -3.06615 | -49.53556 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36abec8c-bfc5-3e23-ad28-b81fd8b17849 | -5.9681 | -41.31101 | 2026-10-04 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3d8e4916-1674-3d32-8adc-5402b94e542d | -6.00445 | -53.52084 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d17b8c9e-3b35-30d1-b4e3-a7084e46b549 | -0.35809 | -51.98609 | 2026-10-04 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2188e56f-b90e-3f0c-a0bd-19e5337513d0 | -4.26809 | -50.26807 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afe61c67-521a-31bb-b2e6-6cbaa188e810 | -3.13381 | -53.74969 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d98283-a310-3aa7-a6bb-623331d4b9db | -5.96444 | -41.31044 | 2026-10-04 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 930c7a1b-941c-376d-98c3-0784ad1d4bb7 | -5.55361 | -45.26664 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25b1e2c8-892f-3b95-8050-923b176dfea6 | -3.07381 | -49.54055 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b6138921-1bef-3f33-8dcb-056c9e0ecef0 | -4.11418 | -49.06557 | 2026-10-04 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 720db4b5-d94f-3246-b2ae-ad970d3435b4 | 0.44354 | -51.06565 | 2026-10-04 04:19:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 091d2777-8e7e-3307-a6fb-f437b4f1c812 | -5.96537 | -55.3523 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff19442c-f9f5-301f-8659-0464753a6c9d | -1.16969 | -49.2638 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f82b29b3-fcca-3e0e-8ef6-8e90a1cb0ebc | -3.01929 | -53.89192 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a8adfc6-8422-37cb-aea7-3bcee943fa14 | -3.12714 | -53.75596 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7491776-c731-3c37-a0b2-044c0fd53519 | -3.20344 | -50.74352 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c445a023-1cb8-3fda-a95f-79885ebdfe66 | -2.9768 | -54.0858 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5510687a-afe6-36b6-a80c-2bbc96844781 | -3.47152 | -50.09434 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 81a4a680-ca11-3167-aa35-d2ee7ef5e909 | -3.17582 | -54.07845 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47a7202d-ba36-37c4-8364-d86994de3027 | -4.28676 | -50.258 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2c52687-fbd0-3c0f-88f6-c5428836327f | -4.05817 | -54.31718 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 536dba9e-06ff-3ac6-8ecf-e8888c4374e8 | -5.54841 | -49.76337 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README27.md)
