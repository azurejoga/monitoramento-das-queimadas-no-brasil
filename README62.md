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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3f4646a-e67e-301e-b5b1-249af59cf792 | -10.30075 | -50.26821 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cdfc6fb-7042-39cb-ba43-f5246d371183 | -7.766 | -49.19543 | 2026-09-20 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 35.4 |
| c25dd4b0-1850-3622-bd85-8f5848877ccb | -6.33603 | -55.29145 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3d73e9b-a11d-3f70-9d6b-4209fa3f41d5 | -8.25481 | -50.82192 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61c5ff74-3acd-3802-98c9-2cd784bbfcf4 | -7.57706 | -57.68742 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0d5bc52-c57e-3949-beb0-a26677f9f5eb | -7.59184 | -46.34739 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9d4edb9-2811-3337-b3f9-27b0d4e8f6ba | -11.2238 | -54.07388 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80724624-5938-3c7f-ae06-611fe299ece8 | -9.02683 | -48.7249 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 546d23c5-8406-39ea-98df-3b2fe5d27042 | -8.61489 | -48.92278 | 2026-09-20 04:40:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a598cd5f-608f-31c4-a07e-f0033bdbb7a0 | -5.83942 | -53.53315 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 623375dc-24a4-3389-bcab-71640cb29c28 | -7.62189 | -45.46247 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 546ea67b-8af5-384a-9880-a1826ac77cab | -11.08829 | -48.28932 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8a797b9-8795-3c60-94a9-ca115b423931 | -8.23364 | -45.59793 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cb011e9-d1cb-32b3-a1c6-2504b4728579 | -11.41833 | -51.46905 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cfe0cb2-2223-3b42-9e69-4fe80cdde0b2 | -11.48127 | -51.47582 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec4ef766-65ce-35e3-aa1d-4eaa4ffbb0ff | -8.6112 | -54.60025 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 819dfab5-b9e5-3ca3-8468-a3d2e39b7a20 | -9.22517 | -46.23627 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9699220-3c85-3f7b-ab96-e8ea3b40ecf1 | -6.75863 | -47.92558 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cc0f8c1-e24f-36c8-be6d-05be10f04c94 | -9.79608 | -45.06837 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1613b043-7a11-3b36-ad41-48c294d3f1aa | -7.00586 | -47.43387 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6d54053-821d-3fb2-a88f-5a2606528ed2 | -11.13707 | -54.01869 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 215195dd-4697-3823-a31d-f457c105ed42 | -7.54012 | -44.94085 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fa5d3d0-404b-3499-898e-3d07304134c0 | -7.36899 | -44.86125 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 537a695c-e85c-3d66-a630-39d9aee82d75 | -9.04016 | -49.83389 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dca19e6b-ffb4-3002-b8b3-b0ca824d9458 | -7.54112 | -48.68941 | 2026-09-20 04:40:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95d164f0-cba2-366a-a3cf-a6c57ce67d3f | -13.03222 | -46.91512 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b83b02f0-1e3c-3c9c-842d-f26974746b37 | -11.02792 | -48.28705 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3d8688-ecd5-3795-86f9-640b3c04caba | -13.01868 | -46.90924 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e5222cd-b82d-3ccf-b1c8-4ea62cb7185c | -6.81537 | -47.88843 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b92704c4-464a-374d-be24-282a54345f7e | -12.1578 | -47.0383 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d79f2d90-ffbf-36b8-95ed-84f9949476cf | -9.77304 | -45.0696 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29e29b13-de1b-3425-8ea5-d39295ce0ee1 | -10.95517 | -57.20248 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb975a27-96f5-32c8-9cc3-7c8de5ec59da | -11.93879 | -55.92654 | 2026-09-20 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97e12bf0-0f3a-35b4-b111-a23ffbf59cca | -12.01203 | -44.68399 | 2026-09-20 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea2f26b7-b325-340d-9403-70e7cfdf4637 | -8.73168 | -52.3679 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a3252ed-3c32-35ef-9454-d97beb541fb8 | -11.03236 | -48.30234 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5cf05e8-a8f7-3ac5-9138-ded8b093b49b | -10.66512 | -48.71649 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd2f8b5d-5f2e-3009-b557-623857544721 | -12.52307 | -50.08381 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a128dfce-91dd-3a5c-bfee-e523b0b76a67 | -10.16221 | -45.56408 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d69e77f-4073-3383-a849-232251cb28fd | -11.02842 | -54.16037 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be1067ff-f3aa-3001-a0db-1ce45581765b | -8.05667 | -46.26205 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 508c109b-f267-30dd-a3a6-8b8a8085f48b | -9.70302 | -45.86719 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2230f758-a3bf-30d2-9d3d-fa1430271d7c | -7.74367 | -45.35062 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc813139-29a5-3963-bd47-ca921842ab08 | -10.56808 | -51.32612 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7225d0b-6322-3d1f-bfd3-926778e37466 | -11.12731 | -54.02775 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41a7b038-af9d-3d80-82bb-b9a2f0fff1c5 | -9.04559 | -48.71364 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd50ea3f-590a-3af6-b826-8dca82a702b7 | -5.84388 | -53.55737 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdefec2a-2dce-369e-8e55-d19e5098a0cb | -8.43893 | -46.00719 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a0d0c87-acd7-36a9-adbf-43616fb65000 | -8.65253 | -45.43935 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 556d0302-59c7-3cad-aa60-2114f7c42a95 | -9.0478 | -48.72113 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3d88b0e-2e35-36d2-a54a-23595dcf2a7d | -7.74202 | -46.71434 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6d16a4b-92c7-3bd4-a299-231dde36e299 | -11.73782 | -54.55268 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4237bbd-d358-39c1-b7b8-a5722ee15cfe | -7.55435 | -61.33749 | 2026-09-20 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138837d5-7924-32ac-acfe-85be5f35140b | -7.37253 | -44.71125 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20712bd7-4bcb-379f-8707-661a265d188f | -10.23815 | -45.35233 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f78c4c2-9fcc-3b8b-a02d-e80a1878c88d | -6.09768 | -57.68296 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e68c04c-f906-39d7-90bb-37773b78625b | -8.13405 | -46.80777 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cbebcc4-e1f3-36e8-8d6c-b72b5b6ce6f6 | -10.78008 | -46.32315 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fde1fa61-4998-3822-8bee-3e088f923b33 | -7.27993 | -45.549 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86cc2395-91ff-3686-9a9d-6b6ad0689d23 | -10.74983 | -50.60722 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14bb2504-32a3-31ef-b9b3-487d4cb3799d | -5.77544 | -57.58149 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad89ce46-67a3-3b89-968d-61b2fe86e51a | -7.5533 | -45.44069 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f6e1f1b7-da13-3f2a-94fc-c6639dce9e20 | -6.45612 | -48.44097 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 570cc5c2-ac7e-3489-8da8-e49fe3e17022 | -11.8538 | -47.63731 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 800a7b6f-5b51-3352-a08c-5cd4fd9f48eb | -7.88424 | -44.85993 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a0a047a-b091-3734-96c9-9afc03ea8bdf | -7.62688 | -46.75636 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d480ad15-6c75-3d91-bd3a-970102005d19 | -11.77848 | -47.46599 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afcdebee-002f-3c9e-8b2e-11fd4ce2ab75 | -6.38615 | -51.682 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1faa6d7b-f876-3e7b-b072-2b482379bc64 | -11.04252 | -54.18166 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0caa0058-2bb7-3e7e-aca9-89768c64e937 | -9.81266 | -48.32865 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59685cf6-dcaf-3afb-afac-2c6f343b561a | -11.03891 | -48.29957 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd06d945-0863-3ac7-9934-07da17bd8612 | -7.11207 | -48.41811 | 2026-09-20 04:40:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44645796-a24b-30c8-8f89-e2f52bd6962a | -11.42384 | -47.31208 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1be01fb4-16a1-39f8-8fbf-f51376f90ca3 | -5.84974 | -53.52309 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7726abc-a18a-3af4-88d4-a7b1f975caab | -14.10882 | -44.83835 | 2026-09-20 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26b183d7-20a4-3302-94c3-ad31b252dc05 | -7.43363 | -44.75621 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cb723541-e9cc-3ae2-9caa-4a44d201e9a4 | -14.19011 | -47.8736 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9c95c32-a129-374b-aff5-d257076b4352 | -9.93737 | -60.73434 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4f607aa-ad1c-3158-8807-132e05dddf43 | -8.30974 | -50.92263 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 144e2594-8c5d-35aa-a6ab-902ce5f36b2f | -11.3263 | -47.28689 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77a1561f-6eb0-3028-9c95-541533194727 | -12.58666 | -50.94463 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c185bdc7-17aa-3de7-8020-cd3f923e0332 | -8.05896 | -46.27015 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe9dab1-358a-319f-9adf-779f4d7721db | -11.07565 | -49.49043 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22dfe479-d1ab-393c-ad96-381a9b0e3284 | -9.7937 | -45.05887 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d11aff11-f0b4-3ea9-bab1-ad134251d6f4 | -7.57107 | -57.68986 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22aad12e-f15d-3890-97a3-58577fc5728c | -10.53677 | -46.72133 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c87eba8f-d070-3554-bbb2-54223ffd1331 | -10.10194 | -48.43278 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34404f7f-920b-3a80-ba8f-e10a384cad08 | -5.75231 | -57.58516 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a22b1ec-f90a-39bf-a248-2822bff51964 | -7.29636 | -46.74322 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b63bbb-3a23-3370-b71b-d0c59b05de31 | -9.27882 | -48.24754 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78c88624-6d4a-31e7-a22d-ac68bfa34ecf | -8.76807 | -44.26023 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d224cc02-94e4-3dfd-84e4-8c602c7bde58 | -13.0275 | -46.92274 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ec3a541-d4da-3f8b-8d90-19dd7b40e49a | -9.76369 | -46.06681 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a651a34-0b4b-3ad1-af9a-2575325e448d | -7.32784 | -47.43708 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d80833c9-2972-37e9-8d54-37453d7f24b6 | -9.85734 | -48.34684 | 2026-09-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09900d28-73f5-3525-8974-ed76fd06abc8 | -6.10171 | -57.62925 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c3ff2fa-02f6-3743-b4e3-cf1398c51d13 | -6.4644 | -48.43165 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf1f4042-9903-3c01-b02c-3b870ba743c2 | -12.3156 | -50.73473 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75a77a30-4473-3d98-827d-4d78cf423509 | -11.18811 | -45.38559 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f308025a-cf63-35d2-8693-5250d9e8f459 | -10.75477 | -49.28722 | 2026-09-20 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README63.md)
