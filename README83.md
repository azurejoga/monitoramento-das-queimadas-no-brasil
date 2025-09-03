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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8806ade-d2c7-3fab-8880-0e5073499ed3 | -6.43583 | -58.13602 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85696822-a90f-3e16-849a-d043da312d4e | -6.8543 | -52.81704 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f8773d9-3249-3400-9e11-17536013eaee | -7.90058 | -46.45562 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2673aa51-e1b4-37f1-8b80-ee77690e7310 | -5.89144 | -57.75502 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ce50fc1-68bc-3293-9214-47dceb83497b | -5.9031 | -57.74615 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d7ef07fe-2abf-3ecc-b791-1081f37dcd5b | -7.91028 | -46.42833 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d44d6df8-b27f-3d77-8290-aaeb62a3a8a2 | -5.9053 | -57.7108 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c637998-7342-3e85-93dc-5ae3d0f28e47 | -5.59978 | -51.94561 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df642de4-1df1-3fb8-badd-407d8dd33c4a | -5.91752 | -57.71985 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f98d0c71-e85b-378e-849a-7960cf14cec1 | -6.47998 | -56.0084 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d6912a3-87eb-3fbb-be4f-8aa3a7eb3b9a | -5.89754 | -57.73814 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9efa2be-aedc-312d-8d3d-296345075ceb | -6.47038 | -45.41481 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 115acca9-76e1-385f-bd71-d1f7378613c6 | -6.80571 | -52.8232 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c5101f5-ff10-3357-9e9c-885c4236396e | -3.52622 | -52.92553 | 2025-09-03 05:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdb108f-4b40-3bee-8548-eed4c09d4481 | -3.23486 | -47.12785 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 099b4cd8-1793-3294-b03d-9449ca67d469 | -6.9488 | -43.27679 | 2025-09-03 05:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eedb9df2-b2ee-3716-9d66-f5658d0b837e | -7.69531 | -48.73393 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 123bfed4-d968-3667-8afb-01e982d746a1 | -5.90421 | -57.73916 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| e6116e20-ac0b-37bb-a243-1e1b8ec75daa | -5.85867 | -57.76769 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2a70f9e4-2fb7-33ba-8a0e-60ccbcabee79 | -6.05927 | -57.99662 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 344c1ac3-4127-3f02-93bc-5378aab1b45e | -5.91807 | -57.71638 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9284daca-c522-345e-9103-5421a23ba3ed | -5.91474 | -57.71585 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b91071d-7a84-32b0-9434-39c3fafd29ef | -7.48679 | -44.81118 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 983c66b9-78e8-3095-9e78-6510cf243a62 | -4.89444 | -43.20642 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fdd6dc8b-008e-394e-9d93-382e8efe031a | -5.11264 | -56.96688 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a3c1771-dfb2-37ef-9d18-4a1d1f0cbe54 | -7.93894 | -46.54402 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2265127f-04bc-350e-bf9b-c09950e9cb8f | -7.93715 | -46.5578 | 2025-09-03 05:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6712470-5189-334f-94b0-a3ebb5517c40 | -7.69971 | -48.74081 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39b54984-84c6-3049-8560-59cbf94af3eb | -7.48804 | -44.82266 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 852ef851-f31d-30b0-9e55-52c6a41bd592 | -6.46667 | -53.40629 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 701cc09f-6300-3174-b60f-816d94f50484 | -6.85009 | -52.79088 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e935fc-a204-324e-9054-cf4f32393d47 | -7.71378 | -48.75514 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 311893f1-f4b7-3a6f-9da3-7ce2b89bf9f0 | -5.86477 | -57.77226 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2d772563-229f-3896-9559-902ec9bd769b | -7.96817 | -46.51067 | 2025-09-03 05:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a376d006-ee66-3679-b8bb-c314b985143a | -5.89976 | -57.74563 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 8c5f1a53-14fd-371e-9e61-095f3a9177de | -4.16357 | -46.78661 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02b5f270-e62d-30fd-9c84-7cf733917d6f | -6.19958 | -43.35994 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d4ddda1-1076-3b34-9700-432c2e729da6 | -6.46262 | -44.67545 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac1ba07d-bd3f-3f12-a305-25acb1a6884d | -6.7922 | -52.80605 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8891a074-6f53-3311-a9ab-bdf9155a7611 | -5.78412 | -46.45825 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b25fe894-597a-352c-b793-b34e800d6664 | -5.91085 | -57.71881 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feb65af3-33d7-3285-93c7-3e3c9769edef | -5.70849 | -53.69053 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2e88eb4-67fd-3644-a800-de7eb9d88d06 | -2.14226 | -53.64772 | 2025-09-03 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5cee949-1145-37b2-abe9-b6dbf02af86e | -4.89007 | -43.22177 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6313af80-043f-3c53-8b44-963380f3ba65 | -7.48062 | -44.82715 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30f7d7ea-ea36-3461-8d97-ae7e15cdff6e | -5.87533 | -57.77039 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a21aa6b1-51ed-3306-a46e-1bc77ab8f72c | -6.85356 | -52.82206 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fadcb6db-53a0-38ce-8ac4-c7ddcc46d59f | -5.69736 | -45.94821 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33e19e01-b261-31dd-a242-6b8e3cde3253 | -8.05695 | -45.36945 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 43d6871a-7a92-365d-9725-f77c79ab312a | -6.80009 | -52.80712 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee61e526-ac32-34fb-a978-a4e6737f10b2 | -6.46577 | -49.51831 | 2025-09-03 05:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ed180c48-38d3-382d-9715-839198a19a0c | -5.86311 | -57.76126 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03927cd1-2e6c-3832-9145-22845c6cae8f | -7.93464 | -46.52943 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36ac65fc-6880-3e13-a9af-b9eab558061a | -5.91975 | -57.72736 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 89deac39-9568-3e5c-965e-79052586c0db | -5.92308 | -57.72788 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c34e20f4-0cb6-3243-88ba-9e5b02c2e053 | -7.96267 | -46.50519 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff6ae48e-49c8-3fc4-b5e9-bf379bcec656 | -7.69888 | -48.74675 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6478a88-7135-3521-97a4-2601eabfe303 | -7.90238 | -46.44139 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ad8449b-f318-3d28-851c-d3a8034a2cf5 | -5.89365 | -57.7411 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ee0b08-327f-3a00-b7f3-df146f93f0d2 | -5.86366 | -57.77925 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4e9ab13-3c15-33d7-83bd-8fc752122827 | -6.80083 | -52.80218 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdce8ae5-7817-3ac9-bf98-282f58dd8806 | -7.92259 | -46.42982 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a03d82be-04f0-34fa-8766-d13a11c5d30f | -4.16162 | -46.79002 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a419cb3-85e7-3d59-8342-8cf81b157cda | -6.9726 | -44.36095 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5e197a4-d43e-3ba3-a9d2-5a1c32607c03 | -6.80099 | -44.64062 | 2025-09-03 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d70a4d0-6ec7-3953-b1e3-5cb1bbfd8a2e | -5.86089 | -57.77522 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bb55bf54-45da-3159-975e-01b3429437c5 | -7.7058 | -48.73561 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b24da26e-b40a-3bca-a655-b1ce212e7baa | -4.89724 | -43.22269 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbb8c68d-0f76-3f14-a302-1ff5483d6969 | -6.94809 | -43.28328 | 2025-09-03 05:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bcd81675-fd43-3a28-827f-582df3e93dd2 | -6.05815 | -58.00365 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d957bbd-342e-3b0a-b3ab-fbc59f28e3df | -7.90227 | -46.44211 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 861f0ebc-a482-37e4-be76-9736a32830c6 | -7.72115 | -48.74088 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d3e65cb-38c2-3773-a4ec-c55f7043a52f | -6.33777 | -58.17808 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4723aa7b-a9f3-3916-b220-01613541221a | -7.92979 | -46.46929 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0b00a0d-dd19-3298-990e-a64d20075cdb | -7.90291 | -46.43729 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bebf1b7f-d3da-3021-9801-f2f4ed1aa6e6 | -6.83143 | -52.80833 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edbd6e84-a780-359b-81df-7a4faffd4cfb | -5.86755 | -57.7763 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a07a5fd7-5340-3b9a-9531-9cd5d361ec4b | -7.92486 | -46.45964 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5077c678-777d-3f09-bfa4-985b7bd2873f | -6.86192 | -52.79264 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 309b87df-2c8a-309e-9047-2b194baeb8cd | -6.43361 | -58.12846 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c569714d-d4b7-3291-b96e-b97bd6cbf44d | -7.71772 | -48.72713 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d6af0f4-281e-3498-aef9-9bd28da05577 | -6.85498 | -45.54398 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ac98657-4c37-390d-b452-52f0dcbcf1d5 | -1.98835 | -56.74453 | 2025-09-03 05:12:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9120b46-4bb3-316d-8f1e-883f80d26b4d | -6.64825 | -45.90754 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb080f1-e157-3563-bc21-184fe38a3503 | -6.41534 | -43.75808 | 2025-09-03 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1625a67-f361-39e2-a86f-bc1fc441a3bf | -7.90728 | -46.45195 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 709f8f2d-7655-3f39-ba24-78b1d8f4f35a | -4.89925 | -43.20876 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| deedc7b5-83f3-3ca2-b600-ff88f921927f | -7.48014 | -44.80959 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9376687b-96d6-36bd-90df-da98412e7662 | -7.48378 | -44.83381 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb3ecc34-8179-30a6-ad11-4fcfdd6a0887 | -6.84427 | -52.83059 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13407e52-1589-3565-9586-8e61de0a1e91 | -6.47045 | -53.40686 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ad6cd63-4920-39e9-aaff-c07136116615 | -7.72148 | -48.73075 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb48555a-7aac-34a1-9868-f7603ed8488c | -6.33051 | -58.18053 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b7da05f-93e6-3765-824f-9184c1ca7467 | -7.70013 | -48.73784 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1d16e6c8-e455-3e4f-9654-c0fb5a52bf32 | -5.92807 | -57.71793 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05a0be06-e46a-378b-93cd-563ae80bc6f8 | -7.10766 | -50.77626 | 2025-09-03 05:12:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95c8c769-b05b-37c1-bf9a-bc0808a80293 | -8.0697 | -45.38264 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80347604-ea3f-30e4-a9f9-1786f49aeae9 | -6.22646 | -43.37921 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7c7ca10-1a28-3c8e-bc9f-653b1e9dfe4b | -8.06423 | -45.36463 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 524d3ae5-6c87-3ca6-b217-60c3f5126b96 | -5.8681 | -57.77281 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |


[Clique aqui para ver as próximas entradas](README84.md)
