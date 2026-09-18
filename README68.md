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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b877f725-b66b-3e3e-86f9-b1a311fd3f2f | -8.49248 | -45.64988 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00614e86-3834-37fe-afa8-3a404e679778 | -7.08324 | -47.47806 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 726f3374-cdc5-32b5-a995-ae3389a17729 | -10.02018 | -45.50256 | 2026-09-18 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af343cb4-98ba-30dd-831d-70afedc4623b | -11.2999 | -43.38329 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04ab97ca-f7a2-385a-897a-727c308e0303 | -11.31325 | -46.76787 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0142bed3-c36e-3dba-ae37-1486530eda11 | -5.89763 | -51.65454 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b25115-2a81-368e-b270-2ed79e79831c | -9.91973 | -46.50847 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e5c7a6d-4330-38b7-9864-8a07c4708be3 | -8.91255 | -45.00755 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0072a75-8159-3387-b74e-c8d1e8ad936c | -9.90173 | -46.5167 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0b7d046-50d6-3aa4-acac-207a9ba7b6e1 | -8.3491 | -45.9852 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a501182a-8302-3333-a1e4-c944566ede6d | -11.28786 | -43.35291 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27708500-5505-38f0-b87b-5b4a83dee2d2 | -7.80513 | -44.90099 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16654726-b038-3433-968f-9c16a746a1cf | -6.44714 | -44.94941 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b2783b6-0cfb-3f1f-b371-37c858385f4e | -10.61166 | -46.56133 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 161d5f67-f747-376c-87bd-f8ca7ded2e13 | -9.76617 | -46.59935 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc006146-f765-3a42-aca4-8555af07d982 | -8.90428 | -45.01434 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbb31dc1-404a-3342-bd75-80907e64f58e | -7.3505 | -44.62953 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b72bc2ea-e51b-3732-99f6-21fe243709b8 | -10.6427 | -50.24094 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b12352a2-6270-304a-bece-33b258baf73d | -7.03484 | -42.08221 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dc5de2c8-7960-3b77-ab68-5fe509b83226 | -6.14377 | -57.69015 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5961ad38-569f-311a-8531-30fef405faf5 | -10.39146 | -46.62715 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88db144b-a8fc-334a-a8e2-54a9ebf0c679 | -9.71661 | -54.81908 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4dbcd1d2-6128-3adc-b3a8-51c07a57489c | -10.91696 | -53.98677 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0112562d-90e0-366d-abeb-64d0e260a359 | -11.52016 | -46.88287 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d988e7dc-cbfa-31d6-980b-d8407f5d6608 | -10.3782 | -49.96658 | 2026-09-18 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420845bd-f9af-31b5-9e64-0321dfee552f | -7.60429 | -46.62614 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46a707dd-d8a8-3c6c-bba2-57e5348fecc3 | -6.02553 | -51.81176 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6b1bfb6-d3ce-3b3f-a0c2-04e9835427c8 | -8.10628 | -45.51505 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 340f38da-3c06-32dc-9442-3b6fd3e806ca | -13.24747 | -46.90581 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ba1e223-162e-3c13-ac70-6c50709fbcf2 | -5.75606 | -51.92822 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18109967-ff19-3d6c-b007-66095447d7d3 | -9.57693 | -46.5648 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 101dac7d-8be7-328b-bac2-6e59e796f08d | -10.66782 | -50.26016 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e13abe5-45da-3001-968a-8a73f0c4a0a3 | -12.16912 | -46.98278 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 890e768a-f6c7-3864-8fef-7653b01e8698 | -12.30621 | -50.73726 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba67f26e-3652-35cf-b1ca-54c30a77d795 | -10.66896 | -50.27561 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c0972a0-4ae4-38de-b20b-77d52127c5ae | -7.3754 | -44.51767 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f30c1b90-b976-3d1a-948a-ddffcfcf3fdb | -8.47593 | -46.88461 | 2026-09-18 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3981f00c-ea74-3d0a-bde6-5774cbc7e445 | -5.67426 | -51.93367 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc44753d-19a4-3447-9c3c-3ddeb0fc47dc | -12.33294 | -50.76818 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25a110fb-ff8b-3316-b3bb-d388469fa8ba | -7.80637 | -44.89242 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e442a5a-1c19-3827-b0bb-853b776b6573 | -10.63699 | -50.2324 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df04fbc-d1bc-3237-ac3f-9c857c141bd7 | -9.94486 | -45.2862 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1f74c5f-7ea7-3638-835d-4003e3270935 | -8.51101 | -48.49933 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29eaa01d-e25b-3ef6-a0cd-5d9a48ff8520 | -9.71774 | -47.14217 | 2026-09-18 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2fdd031e-9751-33a9-ad84-5419aee3cc9e | -10.31854 | -45.31965 | 2026-09-18 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa78437-2475-375a-b465-bb8e25fc12a8 | -13.69795 | -43.62 | 2026-09-18 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b684762-3909-3900-9769-a6b65af488be | -10.66097 | -50.25909 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a9c7e0ab-9852-3268-8fa9-cdd830b3a36f | -8.95261 | -51.46351 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f0a17c3-a8da-3c29-aab8-854c2592a6eb | -9.9305 | -46.52155 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1198d30f-29d9-30bd-8c56-fba389a79059 | -10.48953 | -46.30701 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f9c968c-6c93-300c-b948-4ac533f9f0cc | -8.88077 | -45.89552 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceacafe0-eb89-3933-831f-e343a3bdf458 | -9.5536 | -45.48912 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5e0a481-2612-31bb-b14f-756e49c5a21f | -9.78013 | -45.04094 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 433df1c7-99b2-3e31-ae16-99b0a8134e3e | -9.90861 | -48.38282 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aaa8971-7b0e-3e90-86a3-d08ce508428b | -5.75047 | -51.92015 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9090cdff-d688-38aa-b3dd-f2c09a015921 | -8.49571 | -57.63158 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60da84c0-bacf-3a0e-9006-14b9f374a54f | -5.72962 | -51.75045 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdc1295e-affa-34f5-8e42-783f433f387e | -12.5532 | -50.71804 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28a5026-6495-3b68-ae7c-6276af9376ff | -5.96764 | -46.63299 | 2026-09-18 04:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f793aa4a-2df7-339f-be3c-a31beaee4c0d | -5.45974 | -51.00686 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 077608d1-670b-37e8-b9a8-2d041a9d46ab | -4.79394 | -56.12017 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2037698a-1727-322f-80f6-be1cb2a17385 | -7.20273 | -44.10506 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6c5ce6a-78c3-30b9-9daa-7ebbab2373dc | -7.01828 | -43.63145 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d2bdde1-eee3-33a3-ba72-01cfe2593d03 | -9.28195 | -50.31655 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fcdcf01-bfc6-3013-bb1a-b084c9a922d3 | -9.91445 | -46.54569 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf9b2605-cf53-332f-a141-a52ab874acfe | -7.80696 | -44.82467 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f4cc7e3-c54e-3f75-a5af-a218580f9b10 | -5.73943 | -52.24783 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2068c523-703b-3c63-ae33-b8f3541cca10 | -9.8601 | -48.37982 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8998fd3f-c76c-374c-8099-7248bc975362 | -9.40108 | -46.86265 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7bdb7419-74f8-3dce-a979-cddb1ae5e023 | -5.73663 | -52.24364 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c50eacf-70b0-3f0f-aa69-e5b530d929b1 | -8.44405 | -45.71286 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29a18bbb-acdd-3123-b82d-0ef5f826cd8f | -8.5354 | -44.54659 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 159f33f7-0d00-354b-9f6c-adff3a53abea | -7.67758 | -46.09523 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cda5246-1008-3d8d-a81a-bc363375f6ce | -10.6484 | -50.22653 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61f4190d-ab2e-3200-932f-4534d779e0b2 | -5.73296 | -51.75098 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 466e9c71-9d77-3392-b0eb-b367e3323175 | -12.39974 | -48.48076 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0644c965-9d28-3b77-8247-7acbe6f666db | -9.75838 | -46.09946 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4058bfd2-f41f-34f6-9108-e6f5cf07a843 | -10.90946 | -53.9894 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29f9e15a-6fa6-3cab-9d41-cef6dd38da24 | -11.31378 | -46.76419 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 192b0843-86ff-3907-8121-ecf31f1b83ea | -7.00822 | -43.87024 | 2026-09-18 04:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c75fff8-deaa-3747-92a4-0e962fbde079 | -5.89429 | -51.65401 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0fba7ac-8ec0-3f86-b21f-d94a803f4e3c | -8.93876 | -51.46487 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ea6d8bd-9495-3b64-bc0b-c31f587b306b | -8.84896 | -46.97355 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d90a92f-b066-3544-9d6c-4bbc6ea3053d | -10.112 | -45.64991 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32485055-85b7-3870-add9-3aba7b4fcda0 | -6.66341 | -50.90292 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd74d3be-d341-350e-b342-f2e427d6f7b6 | -12.57341 | -47.08918 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ffe7438-5891-3da5-9dda-83040b145ef7 | -6.59465 | -45.91484 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65f5015a-7284-36a5-99d7-561f09160193 | -10.11391 | -46.28984 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b229402-be36-308e-a62f-a256ba50cc43 | -10.67295 | -50.27242 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 154c71e3-a608-35b3-9d08-cf2752864156 | -10.37289 | -50.45692 | 2026-09-18 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 206a5265-602e-3e05-a14c-4202c7e9c312 | -12.67535 | -43.91182 | 2026-09-18 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c8723ca-734a-3079-bcfa-58cae57a4d20 | -7.79115 | -44.90326 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c55fb64d-0dda-3397-a552-55b052cef269 | -12.28804 | -50.76491 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d442b664-51b7-3a5a-8e28-694adb39d061 | -6.66286 | -50.90639 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 156e6957-0183-3463-8a09-ee7ed04d3a37 | -11.10434 | -47.10167 | 2026-09-18 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff92aed-4ea5-36db-9407-51ef229f954f | -10.6758 | -50.27668 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 703060f4-c30f-3eca-8dff-20ff4707f4cd | -9.5956 | -45.85415 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45997e3c-5141-3682-986c-789496a4c21e | -8.94929 | -51.46297 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a0016c-c8b1-3d03-b5aa-0a350ab2cc7e | -10.6296 | -50.258 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af98c354-e8ee-3837-9268-01fe10c69fa1 | -11.99781 | -49.94087 | 2026-09-18 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README69.md)
