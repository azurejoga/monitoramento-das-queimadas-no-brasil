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
| 6f50339f-84bb-39a9-a833-1027c75e8594 | -8.00466 | -44.81665 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3212886-2e9c-3102-9446-480aa4fd5969 | -9.74408 | -46.06918 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9c73d15-9cab-34cd-829b-7122e528d538 | -14.98303 | -43.08864 | 2026-09-21 04:02:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 2dd79065-e16a-3c44-bf18-bbfe85327d93 | -8.13524 | -46.81899 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9adb5c1-51df-3b90-ba8a-9554f197b5b3 | -8.79581 | -48.74907 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 121847cc-f3cf-3248-9a25-167da71556fb | -10.39258 | -50.23175 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d2302ac4-97aa-3da4-a162-889d160f42ba | -9.60822 | -40.61958 | 2026-09-21 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 399be8a7-092f-32da-a457-7f7b10f44e94 | -10.39368 | -50.22615 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be5217b5-a1a5-3f8c-952d-869a5b848fe5 | -10.81101 | -50.78144 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4070f2a9-b65c-36e6-8f69-cebfbe2e2d4a | -11.38344 | -44.04779 | 2026-09-21 04:02:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7e80942-10e1-3469-9b99-75ed6d5cb534 | -9.75635 | -46.05969 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49a087e9-7ae0-3ed1-bae7-164eb3db1888 | -7.87374 | -48.92625 | 2026-09-21 04:02:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df5cb8b2-bd54-3cfd-952b-dcb711aa01b9 | -10.75452 | -46.32066 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588c527d-9df9-328b-b7a1-3f0ebefea17c | -10.38716 | -50.22476 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f06a137-f593-3285-bee9-0041f8bef722 | -10.48953 | -50.33905 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e780367-0149-33a9-974f-e4120456d509 | -9.45088 | -45.42237 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a041c345-76d5-3476-b432-30a7509c2c63 | -11.93847 | -46.50117 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aed8c6e2-7514-3738-8013-f24b0ace6ee5 | -10.15032 | -47.6824 | 2026-09-21 04:02:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6645e8-ad70-39b8-8cf2-ac8228d88022 | -12.48333 | -44.71958 | 2026-09-21 04:02:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92ad2223-390e-36b0-8595-25a075e9ad9f | -9.4607 | -45.40308 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fdcc09d2-e4f7-319a-ae45-c535da47b5a7 | -11.67044 | -43.41617 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75feb6b-1aaa-36f3-bff2-2be02a78559e | -10.5574 | -46.73691 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6603f4a0-2bad-381a-a3ce-d46a79e5dc51 | -11.79341 | -46.84291 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9a85b68-e06e-3520-917c-8d6cbd00e574 | -11.09192 | -48.30928 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 655fe753-35fa-3809-b9b8-6215054bfcf3 | -12.30053 | -49.18336 | 2026-09-21 04:02:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7e80d2-e146-3b7a-b740-c999ea6b67a5 | -8.30632 | -46.87212 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3e094f6-3726-3430-8cd2-537ec152eee3 | -12.89499 | -50.97284 | 2026-09-21 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3382fbc-9ef6-3830-b446-cd97f353711e | -10.47305 | -50.33251 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20f82183-f4f0-34b7-82ad-05c4ba6bad66 | -9.02159 | -49.83036 | 2026-09-21 04:02:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e494889a-6748-3f92-b5b1-2b347ed64a5f | -6.65824 | -50.89649 | 2026-09-21 04:02:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f19b599a-944c-38c0-8d47-f0f464e10a13 | -9.46672 | -45.3903 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| fe1f06e8-435e-3a74-b36a-d4243966fca6 | -9.27353 | -46.19904 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 277d2ed7-f51a-30cc-bf9a-07db9de4270c | -10.67642 | -50.74483 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e9c13b2-c365-3642-a34e-c71d9679b7f1 | -10.79999 | -50.84391 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdc9c2c0-fdeb-3370-ac20-28d63fe1071d | -11.94677 | -46.48471 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d976b6b0-69f5-3aa4-84fe-043bda0c7112 | -8.7967 | -48.74439 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 063a067f-563c-3d4f-88ee-fc9bd47ea264 | -9.26943 | -46.19222 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed9352a3-3723-342d-9842-d000a8a6eb3c | -9.45983 | -45.40057 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8985fb5e-ec5c-346a-98a3-f3f5c955b2f7 | -11.95852 | -46.49767 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ff88055-61cb-3b78-bcf9-c8fe4d77d224 | -11.34231 | -43.38512 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ba27997-bc59-3ab2-bcdf-eef986a3c263 | -7.42372 | -44.78399 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 45f8707f-abb3-3cba-a37d-62aa4fbcea34 | -13.58443 | -43.71233 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6cd3abd-98dd-319e-8075-b3173b57c822 | -10.4796 | -50.33393 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7e79f1ab-e966-3311-b1de-47dee247d56f | -11.86054 | -46.8866 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c68ef4e3-ae1e-3a7d-b9ae-aff6012e80a4 | -13.40617 | -40.96939 | 2026-09-21 04:02:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fa20141b-d6a1-3f28-a727-d58f802d0845 | -9.54281 | -45.39635 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e129dd00-40ff-3353-ad4a-3997f47a28af | -11.79383 | -46.84285 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff174fe8-a484-3806-9f56-7ad55f9fe9f4 | -10.67979 | -50.74064 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14a09bc2-4572-3d34-beae-acaf5161a1b9 | -10.47364 | -45.10279 | 2026-09-21 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed82ef7-fe4b-3515-bedb-d3bc43cb5a6c | -10.39148 | -50.23738 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a37eee1-d3fd-3ea9-909f-2ddf16f86f52 | -7.43529 | -44.77501 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37928f00-733d-3c3f-95d9-22eeb10bfded | -12.31802 | -50.69792 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79c39bfa-2f54-342f-b6a8-14498fdb5306 | -7.43638 | -44.78155 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bca0bc99-6a50-3cf4-a2c2-4db4a51d5daf | -10.39194 | -50.22707 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 58d51bb2-94ff-3290-963d-d0fc73f86789 | -11.79004 | -51.11927 | 2026-09-21 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62f376cf-020c-3a3e-8bd5-5fe672955f4f | -9.45473 | -45.42917 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db4580b1-84fd-36f0-bdf1-e6da92d81471 | -10.75813 | -50.80128 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee7d86d8-2715-3398-9586-35f312d8f6c5 | -11.11735 | -47.51717 | 2026-09-21 04:02:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f5fe26-0434-3465-b14b-281d06738eef | -10.67094 | -50.73742 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fd7e950-6c09-3d87-af3c-77dcfab31214 | -10.78127 | -50.82521 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43765c12-f272-368b-883a-26ddf25787e2 | -9.23962 | -46.17976 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e32c87b-64b2-3d96-9a0c-bd0e5db4b2dd | -9.83047 | -48.44543 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c7edb99-a4e4-372c-bb94-07e645382701 | -10.4678 | -50.29007 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 80b3389a-62ea-30c7-9760-10d254e53aea | -9.44884 | -45.43374 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08896e81-78f7-3bce-a630-3834cdbd8e8b | -11.95741 | -46.50339 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 296ecbc1-e5f6-32f8-a1d2-0eb1f3726f7b | -9.54671 | -45.40268 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 467cd5d3-591d-3711-9aa7-b06b21535676 | -9.37006 | -40.31885 | 2026-09-21 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a264e86e-a8af-3fdc-b23d-f3e0924abbef | -10.09001 | -50.26709 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| dea49b2d-6608-3a64-8d96-7ec95a44f3a0 | -7.43438 | -44.78028 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a263b74-f725-3255-b105-60089bd05669 | -9.26832 | -46.19826 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7030af52-3f88-3c35-91e2-ad148c3bf29a | -7.31744 | -46.77398 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcbbcda6-b18c-3c82-aa52-b39088cf74dd | -10.08459 | -50.26001 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a7db41cd-fcf9-3a17-8550-b298e1b2a97c | -7.41673 | -44.76645 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 739aa8b0-1b75-3ea3-aab7-97300d45a4f3 | -9.94838 | -45.68249 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bac742a9-6fb6-3d0d-8a1f-145234140aa8 | -8.82974 | -50.48599 | 2026-09-21 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94c02604-d743-3444-bf82-26f2d358f0d0 | -8.37573 | -45.63272 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d0587f-d01a-35c3-aadb-d59950313132 | -10.76361 | -50.80875 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2084d28-d787-3f68-accb-847563b1b3b8 | -11.93901 | -46.49828 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fe8eda6-e60e-3420-80f2-524d5da9fb8b | -7.51398 | -46.22619 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcff736a-616e-3661-80a2-642c2aaf0bb0 | -11.7967 | -49.8063 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c233055e-2501-3c66-9ad7-5e1af0c0af13 | -9.46474 | -45.4014 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7357db1c-3354-30b4-bf86-ee79ff42bae9 | -10.3991 | -50.23315 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7aa23061-a0a7-3abe-b5cf-6548884e2229 | -8.7897 | -48.74767 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db9adb9a-b52e-3444-ac9e-adf3d7946666 | -9.09945 | -44.70026 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 967633d8-6a3e-3636-90f6-21a272a5ef61 | -10.44873 | -50.27163 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a2923a10-e6fa-34d0-b38b-29b40995d930 | -10.45697 | -50.27599 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5f6b5f49-bf76-391b-ad3f-639207d05089 | -11.79834 | -46.84724 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 788fafd6-1161-3cdd-9198-70e3e4e2c42d | -13.28896 | -43.54823 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bd01ed5-2027-3714-a423-68a527fab2bb | -10.67883 | -50.73287 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c135fab-2c67-30a0-883d-e0f9d845536d | -7.41298 | -44.77225 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0b30ab08-cc4a-3cfa-9fec-60ab6a288f66 | -12.41503 | -47.03622 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 974ec556-74ac-3778-a549-a13f17dd819c | -12.30648 | -49.18457 | 2026-09-21 04:02:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c45c66-3c6d-338e-9b74-c8fb58f50ee5 | -11.99634 | -44.89077 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22be4ce7-0072-326c-a8e7-d3bf85e17c76 | -8.77845 | -48.73988 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d85ea2f7-b7e3-378a-a103-4fdf14fe1f18 | -10.79885 | -50.77252 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1235677a-bb12-3228-a496-1d7ad54eccc4 | -11.02996 | -48.32209 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 659f9445-4e0f-3d8c-9475-b1a66b2872ce | -9.45105 | -45.39318 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 84453de9-16f0-3412-825c-71a013183ab7 | -9.26888 | -46.19524 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a767249-0fe9-357d-a0b7-9b04b748144f | -7.45472 | -44.73508 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8da4e85f-9355-3523-bb04-c5f995daa99d | -10.69954 | -50.76868 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README27.md)
