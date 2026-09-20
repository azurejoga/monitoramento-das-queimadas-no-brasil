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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32be739e-4876-3dc1-a964-011d66b11f59 | -9.55849 | -46.55868 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56a50864-21b1-3915-8960-23792f2fbe75 | -7.49321 | -46.71734 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ee877e-c1f4-3631-80ab-2d36fa0f152e | -13.73226 | -48.78995 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d689dd2-4e82-305b-bc0f-80c33e886020 | -8.76072 | -48.66827 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f93ae644-4257-3e14-bf18-c2f3342dd170 | -5.84909 | -53.52691 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 704e46e4-0fdb-37fe-bd00-462fb54f1b55 | -7.88552 | -47.64698 | 2026-09-20 04:40:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 190f936f-1f37-3ebe-9a92-a5740409b8c5 | -7.20559 | -44.09044 | 2026-09-20 04:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff0dec00-a80a-3afc-9988-8f153e08e77c | -11.09051 | -48.297 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3c92fb9-8fad-3eee-9fa9-d875a0bc3c09 | -9.68498 | -49.28572 | 2026-09-20 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67fd3194-6c4e-331e-a3d6-e4b8d5f3745c | -12.13347 | -47.03456 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e1e8c60-ae9b-3f25-a795-e51408b77dbd | -11.0118 | -48.32463 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67c34e8b-e076-3f45-95ef-6ec94c741e5d | -11.10266 | -49.51288 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6b7ea8-3bfb-3cfc-8482-15a6bb4d6a57 | -8.07355 | -45.48832 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5208acb0-de08-3982-a2bc-770ac6e546f3 | -11.04139 | -54.18113 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f16576-f02d-319e-9dea-d9c5f6853a05 | -6.45943 | -48.44151 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bfb3b94-b8c3-3c01-87bc-252f46d567fe | -7.75156 | -54.75848 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad0f8a22-b55e-3e76-90c4-26c38db7d0d1 | -11.31888 | -47.28965 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| acd3aecd-e87f-355a-a01f-d6b28779764d | -9.77016 | -46.07196 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a216d95-1353-320a-a157-acf6aa1d8081 | -9.79168 | -45.07233 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ef92955-3039-3033-9ec5-44c1bd894af1 | -10.27966 | -50.239 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbcba9a0-bb19-3366-b0aa-047f81779b14 | -12.33498 | -50.70065 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9493ccbb-b2e6-3b22-8dcf-00faf87b4dcb | -9.2258 | -43.18507 | 2026-09-20 04:40:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb631e0f-5adc-3d79-8edc-c300a64cb807 | -10.2785 | -50.24622 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1ad54ec-93d1-3516-8f61-702f6cbdd553 | -8.43308 | -45.85696 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c9e0866-d43f-3de5-8c69-d2f4e1e80ba5 | -8.17878 | -54.76994 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0683d41c-7d94-3890-88f2-dc2c66f85df9 | -10.87698 | -54.07468 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92d4e996-0610-30cf-bb4a-1a0f9b22b7fd | -13.21167 | -51.76663 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13a2131e-7cf4-35a1-bc85-91bd6f715d4d | -7.62545 | -45.46301 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6da55b7-9642-3d26-a638-8e9e09be913a | -7.51791 | -46.23616 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64b1016d-dfc5-36ac-9db7-8c7ebbd895ce | -11.02126 | -48.28598 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0db2c655-4e1c-3244-bebb-fa17d493cc2e | -10.88465 | -54.05451 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b3b6fc1-3398-3e5c-8059-08d9d512eeb0 | -11.74124 | -54.55711 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c4fc92-c102-3da9-b793-0dab430d0cff | -8.76879 | -44.25534 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0acd7b38-603b-3653-ba0f-1020a6473ac0 | -16.59114 | -45.33447 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54a278eb-50a7-381a-8f5f-dedb0948ac0f | -15.86483 | -49.91581 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cea40ba-ae57-3127-a232-14f98157934b | -14.92851 | -49.91047 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f54a4448-2fdd-3086-9e47-8bc96ef6db08 | -14.04367 | -52.08152 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 517b96ad-04df-3f20-b25c-d10c08c27dc9 | -19.87651 | -49.00945 | 2026-09-20 04:42:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7f3d503a-8567-3dd8-8ae2-11e89effd9ef | -15.61951 | -49.83444 | 2026-09-20 04:42:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d349682a-cd25-386f-bacc-0c0626208d98 | -15.86814 | -49.91636 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34b737ec-1884-39f7-b3ed-9c3040011e14 | -14.78959 | -48.53429 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94e913ee-f3ce-315e-b5e5-bb2cf5db5355 | -14.79069 | -48.54968 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2298b88c-8e71-32bd-81cb-2ac0727103c9 | -15.46123 | -48.44418 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91ccf673-29b5-3d34-ace6-9c9994419429 | -16.5942 | -45.34225 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caefc1a8-ce29-3c50-a931-c3b0f944711e | -14.66847 | -46.67625 | 2026-09-20 04:42:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0da0711-8372-383a-b8c1-64f31cf941dc | -16.32154 | -53.85606 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f5e71d-c88c-3322-87a7-539dee6c779d | -16.57964 | -51.62677 | 2026-09-20 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cad67b9-0cf3-3ebb-8cdf-a12b48733627 | -14.79634 | -48.53537 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01f382d7-ebfb-3f3b-91c1-1ca5747cf4ba | -14.78845 | -48.54173 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dea993d-dd3c-3cb4-86b9-949bcf5a7f2d | -16.49577 | -49.21576 | 2026-09-20 04:42:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee05701-52d8-3e88-b31c-ec0fbc4c16ef | -15.61784 | -47.84222 | 2026-09-20 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b0c41e4-b237-3e4f-a58b-0de7d738f065 | -14.69199 | -46.69301 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a2a622ca-fd61-3531-afea-8a6d6b2d9610 | -15.86652 | -49.90507 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca2ba7f-f485-3249-85b0-ba94e1fdd671 | -14.92464 | -49.91348 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 266879da-6207-3bef-9400-63612250c9db | -14.61309 | -48.1081 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cee11f86-8fcc-3d6c-a7a3-d5b017719b99 | -15.47208 | -48.42256 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30623900-0b9c-30a0-a3e7-235aacb75eba | -15.47437 | -48.43054 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95005dc1-5351-3760-8102-add613be596f | -14.04713 | -52.08216 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a9ec5a1-2f99-3f58-acba-7b6c22231931 | -18.37587 | -49.39745 | 2026-09-20 04:42:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6b4df190-d5be-3d61-8832-e311839f3c35 | -16.31505 | -53.85001 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc0f829-0b5b-34d0-bf58-d4f1df4c8ecc | -18.352 | -46.19468 | 2026-09-20 04:42:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4658bbc-fecb-3dfe-acfd-5cb538248a01 | -15.32267 | -49.5619 | 2026-09-20 04:42:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02c5c22f-d46e-3006-96fc-487f6b256551 | -16.54065 | -49.10214 | 2026-09-20 04:42:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fecf484c-38af-3bbe-a266-9093b48ae68c | -15.0142 | -48.56117 | 2026-09-20 04:42:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c411959f-ac3b-317a-9a3b-2d16466768a5 | -15.31935 | -49.56135 | 2026-09-20 04:42:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 613fbab7-8be1-3cbc-809a-ad3988950714 | -20.26432 | -45.56448 | 2026-09-20 04:42:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffa3a978-2501-3268-b18d-079ea441e0bc | -14.67026 | -46.68969 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa765c6f-c822-30be-987f-cd773c3278b5 | -15.47152 | -48.42632 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f38cf0c-c2fa-3ea7-bca6-b8e768f4ab7d | -16.97652 | -48.62684 | 2026-09-20 04:42:00 | NOAA-20 | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abf23f48-8260-34a6-93b4-a0dbc7eb9018 | -16.57629 | -51.62619 | 2026-09-20 04:42:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c5d8fa7-9a27-3f5e-9555-18545623c54a | -14.76027 | -48.40844 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92ec949f-cf03-3b1b-86d2-7e4d3f8f7a2a | -14.68236 | -46.68275 | 2026-09-20 04:42:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5f2a5b6-9329-367f-94fd-4eb6d6603689 | -20.33999 | -47.49482 | 2026-09-20 04:42:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 70413caf-c78a-3bd7-8672-60b207fff77a | -14.03202 | -52.0873 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1d8deff-a60e-3ab4-acc1-1c87420d0763 | -14.79915 | -48.53962 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca1d1416-b832-39f6-8aee-b84c79a80582 | -14.79693 | -48.53159 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09587904-6974-34b8-a31d-bbcc154ecb00 | -15.62131 | -47.84282 | 2026-09-20 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 494a5a59-fc3a-3ab6-9bb3-f7d306b81f04 | -16.4306 | -40.55507 | 2026-09-20 04:42:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 62dfff68-fdf9-3635-ad1c-dcdaca198c3a | -20.39623 | -47.86891 | 2026-09-20 04:42:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca8f13c7-17f5-36aa-9deb-7e491af9d62f | -17.59221 | -51.12222 | 2026-09-20 04:42:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 690ce3ef-446e-35d5-8869-7911800835c5 | -14.91633 | -49.92305 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13e1d098-97d3-3ef9-a6dc-61150559507e | -15.8831 | -49.90779 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1512ba94-0ca5-3610-9353-d23fb775143c | -14.04993 | -52.08667 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ec21979-8c38-3d99-b97d-ba175a4ee960 | -16.88573 | -50.59035 | 2026-09-20 04:42:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b716c1bd-c64f-3d72-be47-fe57f21f4e3f | -15.1688 | -48.15828 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04f9a2a7-6f66-3cd1-9c62-d3a03ceeccf1 | -16.31868 | -53.85081 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd8dc7e8-512c-349f-9c80-f8baffb9e3c0 | -15.46868 | -48.42202 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b66d2104-0524-35b0-a27d-829e14d7fc83 | -16.59515 | -45.33504 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cf06f5b-f278-3c46-961d-9190926dcecc | -14.78565 | -48.53747 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 472e1735-f092-3c64-a41a-f30ba8923ec5 | -19.08227 | -46.65286 | 2026-09-20 04:42:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e13e6b31-39fd-3be1-b9ba-f7440b5a1c06 | -16.52564 | -48.74361 | 2026-09-20 04:42:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e94b79f-5506-3a56-8c08-d41c28fa645e | -15.87978 | -49.90724 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15593a13-2a12-360e-a011-4dc752cf6971 | -15.17106 | -48.16652 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bf8f7da-0c70-3321-a264-5e880accbbc6 | -15.47549 | -48.42301 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d06cae9-e795-3837-af2d-6d4d6a586f27 | -15.46862 | -48.41846 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f5a2bca-febe-3d01-a851-a96915b7c8f4 | -14.60626 | -48.10706 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2c88aaa-f1ed-39d2-be9f-a160ea71c618 | -14.68051 | -46.69565 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bc2c1e5-a4cf-32d4-8501-2dac23c75a69 | -16.10003 | -49.64811 | 2026-09-20 04:42:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9061bfd4-0b62-3822-87d0-6646fe554f80 | -14.59023 | -48.09744 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff651dd6-1773-321e-8981-43ce6b4da66d | -16.32088 | -53.85892 | 2026-09-20 04:42:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README82.md)
