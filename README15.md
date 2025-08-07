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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5c5d9e-2270-3f73-bcb8-5ee87af45288 | -8.90287 | -60.55551 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 82e1d941-0c99-3a70-8fed-70ba70bec672 | -6.42379 | -53.36824 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448cb7df-7866-3d32-9741-71a84af9a4c1 | -8.90332 | -60.59917 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd9198c6-2e65-35c4-9b4b-281570951ed5 | -8.91005 | -60.59686 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9e7d691-9146-3b82-b7bd-aaafbdb2db6d | -8.91673 | -60.55144 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50dc55ed-3120-3f8c-9c72-9406dc4f2cdc | -8.9214 | -60.55875 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c822b7f-1b29-3e06-a64e-7ea70c49f4cf | -8.91004 | -60.54166 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2e242a97-aab8-3780-914f-3d0d134417fd | -3.5205 | -47.21213 | 2025-08-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b78e2d4-03be-3d94-b7ad-561ae4c52985 | -8.92351 | -60.57426 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3047de27-24a4-3c83-a1ab-2f48e4cf4c69 | -6.52932 | -45.57391 | 2025-08-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ca24360-fc30-35f7-a94d-2156ed3d1fbc | -8.90305 | -60.5742 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e74f038c-8b48-360d-a5e6-dc9d794c6c82 | -7.94446 | -43.89121 | 2025-08-07 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83164a3e-7b84-3f21-8227-2d8240e10447 | -8.92308 | -60.54899 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de85faa3-2f0c-38b7-a761-76da5234cbdd | -8.9075 | -60.55632 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5bf01cfb-98f1-3203-868d-bbddaa67a80e | -8.88632 | -44.78609 | 2025-08-07 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93364bf6-99c3-334a-983b-10ab73b4bd5f | -6.91688 | -52.84696 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28daf4f8-841f-3b90-adea-2b07fbfbc55a | -7.82378 | -46.88142 | 2025-08-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05034746-d96d-3339-8ead-c8e95425c503 | -6.84064 | -46.39277 | 2025-08-07 04:51:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24bc3020-460e-36a9-97ba-3e0b57292c32 | -10.64168 | -44.74015 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dbf539d4-0c82-3d0b-b9d5-527cb94df172 | -6.7588 | -59.4808 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0205741-d9fe-3f18-9acb-d36e563a6c00 | -7.81813 | -46.88196 | 2025-08-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6d16822-24fa-3690-9303-d14906c1eae2 | -7.14734 | -44.08872 | 2025-08-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00c76cbb-649d-3e2a-bd6b-0c84cec3c9af | -8.92266 | -60.57917 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f3a9b8a-7bb6-3a37-8656-ac2d95995c45 | -8.90455 | -60.54579 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d48ff56e-d501-3597-baad-cba533f2ecb3 | -7.75825 | -43.59882 | 2025-08-07 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee278fcf-545a-3102-9315-5e776a719994 | -10.78272 | -47.43775 | 2025-08-07 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71714773-ed54-3254-898f-f9ab2c011ee5 | -10.43924 | -44.39425 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12a87713-b82c-347d-86f6-57404cba3a1e | -6.75957 | -59.4763 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe9eb26-0f67-3186-b4fa-9e6819147e7d | -10.43795 | -44.4045 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08b3e118-244e-32f9-9eff-04278a112624 | -7.38272 | -44.24727 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c63b197f-5771-3acd-b9a7-2599323cff5a | -6.53435 | -56.20945 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe05dfd-8e8f-37cf-b68e-b33b6a2b6753 | -8.92418 | -60.75124 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 8df3234d-2fb0-380a-b97e-2bcfc5297b07 | -10.48465 | -44.38125 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cfdcc2c6-4f46-3a14-bfdf-33e3c59ff06f | -8.91682 | -60.76537 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4cf77747-f4c2-3cd2-8a9f-dd0dddf87e29 | -8.90792 | -60.58152 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbf8d6c7-22b2-301c-8ec5-6b012f039041 | -4.3173 | -48.07984 | 2025-08-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33e3588e-f2b7-3007-b3f0-b7cc2c79b3c6 | -8.9058 | -60.56613 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eea72d67-9fb7-3927-9ecc-4a8d76680350 | -3.9348 | -48.90939 | 2025-08-07 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ede54940-fce8-3d30-8732-08fc435e31b9 | -10.62784 | -44.76469 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c298e20-846f-3f18-aa69-afa8fdee3280 | -7.18766 | -45.48203 | 2025-08-07 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4714b23e-78d3-3a3c-8f1c-a563f53daf18 | -8.51664 | -43.2951 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 91ad25fd-03ab-3b6a-b029-0c8ec42146c7 | -8.91482 | -60.74949 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a04b2d7-e50e-3588-8334-6e4c8a6b8662 | -7.36905 | -44.15225 | 2025-08-07 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ddc5185-e401-376a-8f9f-58eb00c2917b | -8.9176 | -60.55308 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0023a4d-4fd6-32b4-9f0e-5936fe0db9b2 | -8.9141 | -60.56602 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 165e5312-e421-3c8e-b654-bde15f97c69c | -8.90835 | -60.54496 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c0239181-be8d-34e0-859f-b808f7f13bec | -6.94904 | -51.63094 | 2025-08-07 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d18cacec-986b-348f-a930-75dfcee2b68c | -7.91772 | -45.53846 | 2025-08-07 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f86493ee-ef9e-3c37-957c-c5afb8bc418b | -8.50928 | -44.74994 | 2025-08-07 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 597d5731-033a-3160-b4e2-87b30e95de5b | -10.42272 | -44.39521 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e84e999e-ad39-32a8-b503-dfd7b18c9924 | -7.86454 | -47.87437 | 2025-08-07 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5995255-96a4-3796-9ec5-5fb84c7ef019 | -8.19306 | -43.75379 | 2025-08-07 04:51:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 79c67c17-1eba-3e93-8fb9-7c96e8c692ec | -8.91129 | -60.56198 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2008a524-01ee-318f-9bdb-ba27238a9167 | -8.91467 | -60.54247 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d50eb3a1-3027-311c-a7e9-a5d65bda368e | -10.43387 | -44.39344 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b87e662a-61fc-3fff-bbcb-4d2d3e63f2ac | -10.4285 | -44.39267 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b462e525-4090-3d2b-b55d-712f7341ec94 | -8.9185 | -60.60339 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23006b4f-89bf-354e-8cf2-bf09387216d2 | -6.53402 | -45.57452 | 2025-08-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e4b64ca-831d-30e5-a343-073438368512 | -5.0022 | -56.03587 | 2025-08-07 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d852985-6a3b-30b2-8652-5063d0fb786f | -3.58242 | -53.26666 | 2025-08-07 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd563b14-531b-3264-85c1-15ddd9208d3c | -5.87648 | -57.75264 | 2025-08-07 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d248b6a-6792-31ab-844f-2c400bafb696 | -8.92597 | -60.74117 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ababcf98-3962-3055-ab7a-a5a5229c9d65 | -8.92329 | -60.75626 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 497711ef-02e9-3a8b-8fa4-2504a8ff74c5 | -8.92687 | -60.73613 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a26a704e-849a-3f79-b9fb-82c63c39aa48 | -6.92018 | -52.84748 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2e5c8a5-cd38-3685-acd5-880f58a2f718 | -9.65349 | -43.85146 | 2025-08-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0ebe8a46-963f-3744-80bf-d3b6b4d54954 | -8.91233 | -60.57579 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d45469a-b1f6-35d7-9a5f-c25bb2a62d91 | -8.52129 | -43.30362 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eaadb523-8e49-326f-a50c-0ecaceb72190 | -6.54739 | -56.1984 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc7377c9-27d9-394f-9675-fa5d7cf56d9b | -8.9175 | -60.73447 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 161864e5-0d57-38d9-a9b1-3c259809cf01 | -8.921 | -60.58884 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2680337a-ee05-3716-89e7-9183c7ff94e4 | -8.30929 | -55.1029 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c0fab7-2f45-3f28-8ac9-232e1573d6c7 | -10.64569 | -44.75059 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b917ea2-4a8f-3e13-ad01-3e8397078572 | -8.2462 | -45.06846 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6addf727-08fc-3c27-9c12-5523b8d3b28b | -7.03062 | -42.55116 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13eb6f1b-4633-3b05-8dba-7f56afe7ff9b | -8.90946 | -60.56522 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5f78722-4175-3918-91a0-1ee7bb1f5f57 | -8.91661 | -60.73946 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5eae9ed-8f34-3b9f-a8a4-dfc3714d6176 | -8.90571 | -60.55954 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2c90619-c319-3b31-a39f-3432997768b4 | -8.91417 | -50.04093 | 2025-08-07 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fa44b45-be73-3f69-b14d-e6ca47515a19 | -6.41275 | -53.37363 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1f50b39-2d37-3bfd-a8ec-ef742d0c386d | -7.80456 | -55.20642 | 2025-08-07 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e75f028a-60e5-3b59-bfa5-e082b0b8d959 | -10.64127 | -44.74337 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ea84ef9-9a80-3b6b-a5ed-b2100b32c335 | -8.90857 | -60.57016 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a681239-e379-3429-a266-6cf07acbfb2a | -8.91171 | -60.58723 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfca8b2d-52a3-3c98-a58c-c03b2f99876e | -5.00087 | -56.0386 | 2025-08-07 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96a7ed32-93cf-3890-814d-b49c7da55b6a | -4.00132 | -47.09159 | 2025-08-07 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00574f81-eaf7-3d07-bae7-7c3440b9fb75 | -10.44333 | -44.40517 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92cc5e99-db95-38d3-9164-940f8b8f2771 | -3.88318 | -54.21295 | 2025-08-07 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 820b9c89-e68d-3cd1-bc93-77f8c854ebbf | -7.18696 | -45.48711 | 2025-08-07 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e45d6a1-0109-3aee-b44a-2a0cc1a50aee | -8.92364 | -60.59273 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1d96df-a287-3daf-8c56-009a077d126b | -8.38744 | -42.26554 | 2025-08-07 04:51:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 282139b5-6df7-3386-bc3e-754032c8e377 | -5.8538 | -45.22566 | 2025-08-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ca8312f-23b9-3527-9440-b671a477f3ff | -6.9524 | -51.63145 | 2025-08-07 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3745bf9a-9eed-324d-9064-61ee6bc22c8f | -8.90594 | -60.58467 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29fa31ca-51d8-3f58-8ec6-267e49c05295 | -7.94401 | -43.89462 | 2025-08-07 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f02826-5d43-3728-9358-6127811403b3 | -8.91213 | -60.55714 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33fe09ba-efac-38b8-8b11-1712a9b72cfe | -5.80669 | -59.22973 | 2025-08-07 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6195aee-2725-36ff-96bf-7b495e1ded94 | -7.82248 | -46.88264 | 2025-08-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2a8daa8-fdf5-31a3-998e-a74aad8d2351 | -9.74517 | -48.57058 | 2025-08-07 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd8b709f-7606-3f4f-a14d-e6536cde65b8 | -8.91349 | -60.5959 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
