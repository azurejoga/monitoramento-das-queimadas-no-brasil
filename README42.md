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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6e8a4f0-581f-3658-8367-739d2fe50794 | -6.97962 | -39.68769 | 2025-10-18 04:29:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0b147b0-dc16-3b4f-ad33-713af843768b | -10.62929 | -42.30914 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7893210e-348f-3ee6-9ce6-1d7d504b9802 | -4.26671 | -49.21893 | 2025-10-18 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea8eae4-5543-335c-8883-903855fcf2cf | -6.35955 | -58.21559 | 2025-10-18 04:29:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29f04d74-fb2e-30d9-892c-53079754875b | -10.81774 | -43.92911 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 101e5b0d-da34-318a-8e7b-570cebc4fae7 | -6.41908 | -43.5812 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b778d348-db20-35af-beb0-2976916f6b09 | -5.64689 | -45.10863 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bdafb5b-4a28-3587-8cf2-1907aabf0358 | -5.92754 | -51.55917 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e43aba1-2d09-31e3-b107-6fd4764ed7aa | -10.14399 | -44.53199 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1cc41b4-6303-3f2e-88fb-88e1e62f33e6 | -7.98371 | -44.15408 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de50b984-54db-35f1-99fe-a0d74e6b460c | -4.83445 | -48.07871 | 2025-10-18 04:29:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17736f80-cc57-3f38-9613-b92176fc4765 | -9.08253 | -45.13959 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6627125-69fe-3340-9d94-6845b43c5393 | -7.12197 | -44.8024 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e810f17e-1e4b-3ee5-a0eb-d27aad954e47 | -9.76959 | -48.74607 | 2025-10-18 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a293dc28-f31b-3e4e-be30-05501b085912 | -8.78138 | -47.92782 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d4d9e75-bd98-34b0-9747-95f34a7dd053 | -8.29525 | -43.38912 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78efbe3c-74d4-3d92-84f6-520ed76e6e97 | -4.2463 | -48.37056 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 598b28ee-0013-3428-802f-e97713fe4360 | -7.20881 | -45.3896 | 2025-10-18 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f2d999a-797a-3422-ae63-9b63249e4300 | -10.81345 | -43.93285 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02f8ef32-2a9a-3ed0-b473-669189c28eb4 | -3.78073 | -51.7699 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9b91eba-d8c0-382e-aa74-56073fea7bd0 | -5.92502 | -44.75943 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a903973c-05d1-3560-b353-d604b2e1930b | -8.86297 | -46.01435 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef4f2a00-e0cd-3e33-8a3d-071f25a116a3 | -10.24443 | -44.03591 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81ea4ad7-0f09-38ea-b5c4-ffbc277ba96d | -4.25698 | -48.5497 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b762a2e-33c3-3c5f-96b3-f37a44f1b070 | -7.91918 | -47.92156 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3076a674-5dd6-33f5-a699-fb6bebf5742f | -6.15213 | -44.21625 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 499e00d6-ee6e-30c6-9d86-48b4c73cba90 | -10.51973 | -43.40656 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fa1b7e4-762b-3b9d-b039-ad832ff04c46 | -8.38729 | -46.24295 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce2ad83f-b74e-3e48-afd0-157f7315c5bc | -8.58156 | -47.02541 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c01fa12-ef78-3572-b917-21c71b032986 | -7.44112 | -44.74502 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 099f0c21-7ecb-345a-a89b-6bb62a422afc | -6.246 | -46.38981 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b69a28-9253-3457-bc44-6050f4615902 | -7.59456 | -44.97196 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91eb36fe-6076-3536-b7ee-162386fb04e6 | -6.1048 | -45.84786 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52b80cfc-a832-343d-9b74-e68ac62ea989 | -10.49445 | -43.44818 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 192fdf14-5432-3c7c-b1da-8ff5c128ba14 | -9.81588 | -47.74926 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37200fc6-a66f-3975-8e04-7b257fbf0659 | -9.71625 | -44.57588 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56fde4b7-5905-32e8-81ae-a4bc0ced2071 | -10.70894 | -44.55035 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a35e138-611a-3d7a-8361-5af8ec599db6 | -7.58431 | -44.99308 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56982e95-bd60-395e-b29d-6deeb4ff8890 | -10.53209 | -44.50851 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab60869b-2dfe-3013-84e6-cfb91aecd46b | -7.09979 | -47.04285 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca446bf0-6770-3af7-8d4b-67f2e43318c9 | -7.54822 | -46.90337 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b17f4fb-d82f-3618-a60b-cc54f2ea2fc1 | -8.3628 | -46.2031 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca18f387-bf32-3416-bf9b-243d4bb136ae | -9.64542 | -47.71786 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c1be337-b423-3553-a1f2-39c588c78b34 | -10.23658 | -44.03885 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8595eb7-4254-355a-b634-1728361b46a3 | -10.48957 | -43.42899 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 41dfa032-6335-38d0-aa3d-c4dadca4f096 | -5.55973 | -46.36984 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc4e06a-82fd-3054-b878-30f015bb6c83 | -6.31823 | -44.3222 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b799ef-7029-328e-ac3e-53233f692551 | -5.56306 | -46.37036 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b538cc49-ecd4-3ed8-ac23-df53ca696098 | -10.42263 | -47.74617 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07066383-c3c1-3f16-9c9d-1ad713154d98 | -6.48337 | -44.55972 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b87e952e-e1f9-39de-a5d5-77086e45cfe6 | -10.42828 | -44.91122 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d721af48-9a97-3185-bbb2-23cdc9f1740f | -8.81113 | -49.68033 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 766a23c4-1eae-319f-97e4-0e7d7d36fa4d | -5.36506 | -45.56773 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a84afec9-143e-3fdb-82ae-1c61b961d680 | -5.53786 | -44.03985 | 2025-10-18 04:29:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9741bddf-5070-30e9-985c-9b4d210a5dcd | -8.41677 | -44.72159 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65cf98e6-34dc-3508-9e46-b979ec79054d | -4.99356 | -43.85864 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f034a843-44f3-3bd3-a509-321e58f56fe7 | -5.89281 | -43.90988 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 906db597-9f4b-3610-ba7c-fb2e22d3d16c | -5.89102 | -43.9215 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0452c404-947e-3720-af96-93020b340122 | -7.39808 | -44.75399 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c4ceabe-1d1b-3fc0-99a6-277f057a56ae | -6.17843 | -44.8609 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f1d636d-d52d-3038-91b9-728893d30f49 | -5.99154 | -44.15372 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22a893f5-2423-3041-b4d1-dcd8c5733a34 | -9.6157 | -49.67942 | 2025-10-18 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 762bd4e0-ab35-37c2-b231-340162649f96 | -9.03846 | -46.61517 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af55a61-ee11-3b75-be7c-a748716f3ca7 | -7.36588 | -44.23899 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b65d2569-0573-3771-8d40-9f6d62d6d295 | -8.91895 | -47.96113 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2d795a-6fa0-3af5-868c-6302c1dfb839 | -8.17911 | -47.04314 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ba3213d-d4a2-3563-83aa-2bb5739d9449 | -8.26285 | -44.02334 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70f3b005-6eb7-3e82-9f17-da45348224e4 | -7.37206 | -47.036 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885e460c-7937-312e-a423-b11058b405ae | -6.74301 | -43.81334 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d787333c-dfa7-3015-a202-d894fcce6857 | -8.36009 | -46.24218 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 993e8719-855a-3fa1-96c0-907cf63b1169 | -4.24858 | -48.55652 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f4ab040-3595-341b-9b1c-e35db36f5c6d | -10.1848 | -49.51626 | 2025-10-18 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87530819-469c-3211-a561-b906d57c1232 | -10.27557 | -44.05148 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7c8a652-a13e-3af6-84c3-649b2f606285 | -6.96221 | -47.11784 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e96adb8d-ce05-341d-9760-8b8c50561c4b | -10.69969 | -44.54561 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b3ef81c-4d66-3ded-9561-98ace87b4ac1 | -7.66513 | -44.6298 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f29b52f7-a10a-31fa-a9e0-0c8710618484 | -7.75307 | -42.51711 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f8ee68d-4f52-38d5-b533-c190e78ec53c | -8.30467 | -43.39749 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bc0bc41-c297-34e2-b407-fe6cb20de410 | -7.98153 | -50.00728 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae9c7a70-72c1-32dd-b86c-115b0f3a26de | -10.23867 | -44.07609 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db1b4f7c-f44b-35d1-8306-01f24e22b2bd | -6.31766 | -40.9477 | 2025-10-18 04:29:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0376b263-d461-3b94-bc09-ce5ec5d6395c | -6.74008 | -43.80885 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| de2783d2-b174-3602-b55d-8f03a32d1674 | -8.29431 | -43.3915 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdd6f2f2-7800-31ec-aea4-b449ad3daa60 | -6.76667 | -56.86269 | 2025-10-18 04:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 338bc0a6-7e94-341f-9031-b3ac093991b8 | -10.24018 | -44.03954 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf7ddd23-8181-365a-b7a2-2d3da647ea89 | -9.89229 | -46.34968 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dd97140-0b18-3ccd-96b8-399e6e42d162 | -7.9561 | -44.12191 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f50646d2-ba9b-3aa9-a4fe-eb02bdad1d27 | -10.63028 | -42.30207 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dfc8b8bf-3baa-3cba-80cf-5e7c4376053f | -8.58544 | -47.02245 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44bdb566-0461-330f-954d-36b7466d86be | -8.22745 | -47.84587 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8207402f-56ad-3b53-b186-f849e758682e | -10.24974 | -44.04982 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d721203a-1aa4-3b86-9dde-37b0f95b954e | -3.85906 | -52.22724 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac108939-0fd1-319a-9989-b267457dc9a5 | -9.81197 | -47.75225 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d685dd8-2262-31ce-9c58-c8292394bb4d | -10.2474 | -44.04082 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb643336-b402-3dd3-a72f-db4b8cbae40e | -5.78618 | -44.88948 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c85143fd-09a3-3bd1-85de-bce85398b32a | -7.35646 | -43.85342 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2372f58b-900b-35e4-8e41-a62408857b91 | -10.6348 | -42.29911 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e94d384b-40ba-34e0-8dd4-8b1a07f14dd3 | -9.0072 | -47.84019 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e1f62d1-9eac-33ec-8187-e5dc22aa5cec | -9.11982 | -46.6137 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc0ab27-1ddc-33fc-a3da-b0e542c36537 | -5.301 | -45.47565 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README43.md)
