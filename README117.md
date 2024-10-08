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
| 0d6ed227-0dd9-3b58-8103-fe4d76e4a8af | -17.08628 | -56.83684 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4c657cf0-3334-3b13-a208-24f10f2a482e | -17.08524 | -56.8452 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2cd3f297-6709-310e-a7b3-ff3fcbfc3dfc | -17.07054 | -56.8362 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 94468fae-49c6-3dc8-a627-091c41f080d7 | -17.06626 | -56.83562 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 565bf5ec-8b53-3958-b3c9-d4a003b17485 | -17.05716 | -56.83862 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0be67852-45c9-395e-8c6e-7baf5e4733bd | -16.87076 | -56.73739 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| acbf2035-017e-3565-9b58-69fea3032f81 | -16.86769 | -56.74287 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 40ece842-7ba0-3c71-8917-bf1146218b89 | -16.86723 | -56.71284 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 519a71e9-1868-3315-8e13-7136ebeb5c52 | -16.86474 | -56.71512 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cfd707a0-15c3-348a-86ca-0d801ed98ef7 | -16.84947 | -56.71472 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef35b6eb-2960-34f4-ad11-e7d6d3286c9a | -16.84676 | -56.73576 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 69132aa1-8819-3e79-8522-d9c6df8afcfc | -16.84571 | -56.70992 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 696d6f29-cfd2-3fd0-b828-d46768be3dc6 | -16.843 | -56.73096 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1a27a90b-d5a7-376e-aff6-8eee46fdcab0 | -16.84246 | -56.73516 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41873e94-9b4e-393e-b44f-8b0ac1949454 | -16.84192 | -56.73936 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 731afb33-e897-31ac-a531-23254ec2dccc | -16.75099 | -56.71198 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a325561-baf3-386a-bc97-1f2a19186dc2 | -16.74669 | -56.71139 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3a5d8306-46ac-3055-8a7c-394c015e41bb | -16.73864 | -56.70601 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f572183c-b113-30b6-8654-3c27c4dbdd9a | -16.68522 | -57.11776 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 18760572-61b3-303d-ab34-30d85ddbe337 | -16.68156 | -57.11322 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8cd62686-046f-310b-83c9-3a9f051e1a2e | -16.67841 | -57.10472 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 08d8d743-2c7f-3336-b22f-bae3927e6d5c | -16.67583 | -57.12452 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7a35529d-5e5a-3c28-bc9e-fe5d17e7e381 | -16.6748 | -57.13241 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9ca0f93c-1d96-3bdb-8d67-2851efc37182 | -16.67474 | -57.10019 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7a963090-dff1-327c-8241-8e69518eb7be | -16.67371 | -57.10811 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 376acee4-34f7-3ccf-ae08-695fc82cd619 | -16.67106 | -57.09564 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 803e4253-dc85-3e5d-a978-892ddff90307 | -16.67011 | -57.13578 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d43dbedf-7280-3f68-9041-ba86ae02bde7 | -16.6696 | -57.13972 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 41f4cf87-8cf2-3ca2-8428-1cabf4c520f1 | -16.66952 | -57.10754 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a3c02fd4-76a5-3f42-8d9d-8560b5c97a62 | -16.6685 | -57.11544 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 60ac7398-a0e1-3863-8290-957cb5ffe852 | -16.66696 | -57.12729 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7e21f224-2e7b-3780-b50a-6c1686d6531d | -16.66645 | -57.13125 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b4fab602-4a09-3084-ae1c-3fc7f71c2299 | -16.66594 | -57.13519 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0f3e8e7e-f4db-306f-a130-6d803ddb03a5 | -16.66585 | -57.10299 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3335d3e2-66d9-34ca-a609-72a0f45190b0 | -16.66543 | -57.13914 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f0c1620e-bb1a-3217-9ad3-48f29697f504 | -16.66534 | -57.10695 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3b915875-5b89-366a-a08a-97a5d8296fac | -16.66381 | -57.1188 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c7b8add7-29c9-3caa-96a8-943eebe68ee9 | -16.6633 | -57.12276 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e548d6f6-2531-3a3f-9f89-353941e038e7 | -16.6632 | -57.09052 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 91ebacf3-daa3-3f62-a537-a412299ec401 | -16.66176 | -57.13461 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 3989099b-4a39-3999-b40f-0904e9ae3367 | -16.66125 | -57.13855 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 6db63af9-7999-3813-baec-c2dab7222591 | -16.66116 | -57.10636 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| bed36558-d262-3a98-98b4-7b6de0d5146f | -16.66074 | -57.14249 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8c4153c5-81df-3d33-8e69-9d76580d357e | -16.66065 | -57.11032 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b98742e4-8289-35c6-a4bd-c0a1f7449338 | -16.6581 | -57.13008 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 4bbd3a9c-02e0-3336-a321-815385d95084 | -16.65759 | -57.13403 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 32d00ab9-b609-39ac-9f0a-dd9577d71579 | -16.65708 | -57.13797 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| a5f9e76f-e05d-351c-978b-efa74e6de7ac | -16.6529 | -57.13739 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d29b1b62-015d-3eb4-924c-677bdb3d94cc | -17.73321 | -57.09424 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3bf969f1-b941-374a-9c9e-77456c7e38f1 | -17.73206 | -57.06892 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c6a72e42-c4ac-3be7-a4dd-e4dab7e6835f | -17.16294 | -56.74868 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8d5d54e6-36bf-3b98-afd3-f2dd02b9d317 | -17.14035 | -56.8229 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a4fa1751-96fc-3e0a-93d1-b9ff18d17e28 | -17.135 | -56.83071 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9c4f01e7-ee61-38eb-ad18-24ecee5cba4d | -17.13446 | -56.83491 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 82ed2946-5780-3944-8699-41537f6562e8 | -17.11574 | -56.84513 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9eb82aae-ee6e-3d6c-bedf-ff5c79601733 | -17.10237 | -56.84755 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 834c1ac1-a2a9-3569-b205-832f8812afc9 | -17.08576 | -56.84103 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2b76b637-21ce-352d-be7e-a88232daba4b | -17.08148 | -56.84044 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e80ce51e-928c-3c29-9597-b203f808b6d8 | -17.0577 | -56.83446 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 866b9f3d-714d-3191-96e1-41edb325d787 | -17.05342 | -56.83387 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d25d3136-8f90-3cfb-85fb-9eee8f5d4395 | -17.04432 | -56.8369 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 409070a6-ae26-3c60-b76f-a4e777a92031 | -17.04378 | -56.84107 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c39994a1-ca29-3a56-b6da-ed50acea6d05 | -17.03522 | -56.83992 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2d9dcfca-7884-36c4-8b5e-526f79abc524 | -17.03469 | -56.84408 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c898c82-bcb3-3c6f-9e2b-4ed0eb76c995 | -17.03041 | -56.8435 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f8abe0c5-855c-30eb-b9df-2df1d14db6d9 | -17.01757 | -56.84175 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 954ed21e-118e-334e-b41d-03315580780d | -17.0133 | -56.84114 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9684f9c0-b467-3185-a3d2-1781c1567dd1 | -16.99249 | -56.69265 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4969c6a1-69e4-3a73-90c6-e9d6c20991d6 | -16.98883 | -56.72239 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18448fa7-26ee-31dd-8ac3-1048aab0085e | -16.9883 | -56.72662 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ac7b30e5-4d0e-3048-af8e-445b0f623dab | -16.98817 | -56.69203 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eb7554e5-8527-31b7-a47d-686e514173f9 | -16.9866 | -56.70482 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 868f1402-2bd7-3147-8e08-02c99f828c67 | -16.98608 | -56.70906 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 25660a17-26c5-3226-9f15-2786b2135fe3 | -16.98452 | -56.72179 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| be1f273b-9a3b-36c7-8991-f1746461efec | -16.9843 | -56.70554 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a5cced2-20dc-3c13-91bd-2e6f3a1f02e3 | -16.984 | -56.72603 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b3e1dd08-9ebc-3828-b75d-7ca545ce3fff | -16.98295 | -56.73449 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 613cd7cd-76d6-3255-a971-d398ec45ce64 | -16.98229 | -56.70421 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5870c400-fa93-3026-a206-613d4ce9b9ad | -16.98209 | -56.7225 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 93d6b06f-f397-3fd4-a8a4-23147f561156 | -16.9731 | -56.81442 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 53bc0518-7e78-3cc1-a725-ef18f3b9a673 | -16.96985 | -56.80547 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 20aa7740-f6f2-3b53-94db-f496741b74bd | -16.96797 | -56.74962 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a747f5ad-f8f0-3461-988b-4b4448ec2b57 | -16.9663 | -56.81016 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 318dbfd5-b10b-3c05-93f1-34c9c1e0a98f | -16.96608 | -56.80069 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 34fe9eb5-9d2f-3a4c-ad02-9d9a9a5de6f8 | -16.96535 | -56.7503 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 27228f22-356d-325b-97cf-f35cc39ba4dd | -16.96505 | -56.80906 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 4f3ca2be-5718-3fa4-aa8c-c78260ce1e75 | -16.96454 | -56.81325 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e8c11613-1c4d-35d7-8e7b-984ab006f300 | -16.96099 | -56.78391 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b461052e-0a38-36bc-b767-8681b85d6634 | -16.87043 | -56.72185 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 003ea0d0-b62c-3cdc-b7d9-3a58cd37ca44 | -16.86824 | -56.73868 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9f54aae8-e1c6-3d28-8ecc-d5897f04725a | -16.86802 | -56.72415 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a867ec17-351e-355f-98a6-dac8b4e6a675 | -16.86613 | -56.72127 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d047120e-8584-3bd1-bb20-40522de247da | -16.86595 | -56.741 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1bd97a4a-b9e2-3f16-b3e8-1e4b7ec48e1d | -16.8634 | -56.74229 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4e668241-3ab8-39d9-b1cf-ccd2bf78d7f2 | -16.86165 | -56.74041 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4c1d133a-c215-3184-bb2e-c743c2d77a7b | -16.86113 | -56.74463 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 84a4f35a-81b6-3d5c-88ef-56506053485a | -16.8591 | -56.7417 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 018d9926-a733-35c3-b278-c9709e9ba93f | -16.85377 | -56.71531 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59686a5f-9259-321b-8678-73d6883e3a7c | -16.85001 | -56.71051 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3c9426cc-1050-30f9-a6bd-d55789a55840 | -16.84943 | -56.74891 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README118.md)
