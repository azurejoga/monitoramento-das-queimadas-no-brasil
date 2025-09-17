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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf273a6-5baa-3a75-a59f-d065dcbed9a4 | -3.8228 | -44.1063 | 2025-09-17 12:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fa95c0ef-62fc-32b3-abde-bf1b8692a8d7 | -8.6885 | -46.3823 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f5a22109-b422-3183-8de1-e1e33f166840 | -10.6921 | -46.513 | 2025-09-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e08a89d1-7489-3bbb-af7f-a7abfd907e58 | -14.7732 | -45.3354 | 2025-09-17 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 0f286ffb-70dd-34b2-b411-80b65020bc8f | -12.7109 | -47.9426 | 2025-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e90a890b-d4fc-36d0-a1b8-4f12535a13cb | -8.9445 | -45.5438 | 2025-09-17 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e8a4ea6f-9ceb-39af-9450-ac31753ff3a8 | -3.8042 | -44.1072 | 2025-09-17 12:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 7d6f4588-11db-3a03-94f9-72c639bd8bd7 | -8.9536 | -46.2874 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 759d07b9-b721-3789-85a4-30fede7bf161 | -8.631 | -46.4553 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b0114b5a-918c-30dc-83b1-6d8b5e26c6e9 | -12.729 | -48.0068 | 2025-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3fc03fdd-419a-3b6c-bb3d-09483ee83d1c | -12.6825 | -45.2977 | 2025-09-17 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e5cc37c1-5f67-315c-b29a-547fb495a27f | -8.9731 | -46.2405 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 37b1ac11-013f-343d-8d98-c62e00fb2b1d | -8.4467 | -47.692 | 2025-09-17 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| aa84cbd6-a5bf-3851-a283-bb9532fbbaad | -8.9449 | -45.521 | 2025-09-17 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 73a54fa9-2b22-313b-add7-76d073d241c4 | -8.9728 | -46.263 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| a737388a-a5e3-33d7-90f9-6752741b4def | -7.8256 | -46.1754 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ddfc0693-3d6b-32f2-8edc-ad2c575de629 | -11.1108 | -45.3452 | 2025-09-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ab0e1845-24da-3d52-9606-9ff0c3b6cbd1 | -8.4279 | -47.6937 | 2025-09-17 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 92bf77b2-0527-3bd4-85e4-4a82d120608a | -7.581 | -44.566 | 2025-09-17 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7cb2852e-cda7-392e-9836-3756aacd7bef | -13.9653 | -44.921 | 2025-09-17 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 7bd2a17c-f664-391f-9ff6-9a4ba9c85781 | -8.9533 | -46.3099 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 480d174c-985f-3292-a3c6-ecf7ff4897d5 | -8.992 | -46.2385 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 342.5 |
| 90e5c65b-b3c9-314f-b8ae-ca9b7545dfb2 | -12.7102 | -47.9872 | 2025-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 11f526d9-60da-3096-8405-142c4028d945 | -7.8259 | -46.153 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 17051079-ba19-3ebd-9af7-63ade12aeebd | -12.7294 | -47.9845 | 2025-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 02fc039c-d362-319d-ad39-a7000537bf80 | -9.1187 | -48.1091 | 2025-09-17 12:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b670d5a5-ffa3-342e-9b7f-ddbdc3b0ab90 | -8.1572 | -46.747 | 2025-09-17 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ae51e7d8-50c9-356c-b346-c825aeb5ff5f | -10.3297 | -46.625 | 2025-09-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 03d7b15e-d85c-312c-91bb-7b82022144e1 | -22.45642 | -52.24924 | 2025-09-17 12:40:00 | TERRA_M-T | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e5d1b6cd-2fda-30fd-bb30-bc26d1780d8c | -22.45498 | -52.26046 | 2025-09-17 12:40:00 | TERRA_M-T | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 2c0525c8-cc3a-3b71-bb18-26f48fe48f5c | -23.03663 | -47.71908 | 2025-09-17 12:40:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| eded2f5a-966a-38a5-8f65-bb9ec50efa5d | -23.13544 | -49.83058 | 2025-09-17 12:40:00 | TERRA_M-T | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 815cca76-9631-3f64-84e7-1d230d478625 | -21.88973 | -49.85889 | 2025-09-17 12:40:00 | TERRA_M-T | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| b8d3605f-5923-3f40-9591-034578c939e8 | -21.26802 | -55.32574 | 2025-09-17 12:40:00 | TERRA_M-T | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1a5c5d42-8dcc-3065-a38c-725eadd1de6d | -21.78789 | -47.76812 | 2025-09-17 12:40:00 | TERRA_M-T | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4d0ff2e5-2954-3810-8fec-aee1256db31b | -23.13523 | -49.84016 | 2025-09-17 12:40:00 | TERRA_M-T | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 74825ab7-5df4-3e24-b90f-ee6a8295ddf2 | -23.0389 | -47.69571 | 2025-09-17 12:40:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 3b69c8d4-ba9c-3100-ac1b-fecb941922ee | -21.78598 | -47.77322 | 2025-09-17 12:40:00 | TERRA_M-T | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 16eb295b-efc7-31d1-829f-ea0b92110ba4 | -9.0661 | -44.9374 | 2025-09-17 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 752a59e4-7f4e-37ab-940b-b4502d8e0f53 | -13.9653 | -44.921 | 2025-09-17 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 248.1 |
| cde55729-1a68-34cb-9027-1107a6bcef23 | -7.6685 | -45.129 | 2025-09-17 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 116abd70-2b00-316c-9b0f-43f34de78df0 | -8.992 | -46.2385 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 142db366-7a71-3148-8240-92677c0c255a | -8.6702 | -46.3394 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 85811300-4c6e-3f8d-971d-68117581ad90 | -9.1376 | -48.1072 | 2025-09-17 12:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6fcfa5c4-c527-3cec-b3b2-41972186c9e9 | -8.9719 | -46.3304 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 566d1bdc-2948-3d5a-89cd-d349ed0b7576 | -9.0851 | -44.9352 | 2025-09-17 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f04c0337-9d40-3edf-9648-c904da36d8af | -8.6885 | -46.3823 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 132871e6-d945-3ad1-a821-cc8c739ff69a | -8.9536 | -46.2874 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6431c05f-0561-31ba-8c3a-d88a8af55de0 | -6.6127 | -45.6066 | 2025-09-17 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 15afb9a8-32dd-3f03-877b-f2a2879ae09c | -8.9725 | -46.2854 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 353.9 |
| e0069454-7bef-3f62-9b33-8ac93e00ab0e | -8.6887 | -46.3599 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a13ab367-b9fa-394d-9567-d9ee20434176 | -6.6129 | -45.584 | 2025-09-17 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f4848ee3-c387-3135-9098-c04e4f36cff2 | -6.8734 | -43.9636 | 2025-09-17 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f9918689-bcab-3c75-83be-6461feb88a30 | -3.8042 | -44.1072 | 2025-09-17 12:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 1497f7d5-538d-3568-a85f-c369d648949a | -8.953 | -46.3324 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 482fc1cc-f6e5-3b63-9ad3-839a7c404114 | -7.6683 | -45.1518 | 2025-09-17 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 6464bbb1-bc2c-3ffb-a99d-317eca5e8728 | -7.45 | -46.1871 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1bff3f89-1f46-3262-8a1d-06dcbad904c1 | -7.5996 | -44.5872 | 2025-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 1a4c4d34-ea65-3cae-a974-988befc97b33 | -7.5807 | -44.589 | 2025-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9392091d-ff00-3f8f-8e79-bdb614ce63af | -8.4137 | -45.7583 | 2025-09-17 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a6d7996a-1512-3bcf-9a06-29d91700bf00 | -8.0281 | -44.957 | 2025-09-17 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 34726fb2-2550-394c-8b4e-c7b20cda7f50 | -8.0092 | -44.9589 | 2025-09-17 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 07ddeb25-f83d-3340-8c45-19a8bdd092b5 | -9.1236 | -44.8849 | 2025-09-17 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| af4d4707-ff0a-3181-ad86-517646bb657b | -8.6699 | -46.3618 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b63d7061-b403-3ee5-a42c-79892312adc3 | -8.6882 | -46.4047 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4324c02c-0ef4-389d-9687-17c03b5f2702 | -9.1239 | -44.862 | 2025-09-17 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8920dfd6-3231-394b-b086-6062d6a4f02d | -5.4897 | -39.426 | 2025-09-17 12:50:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 1715281a-877d-3663-8f54-130924fae850 | -12.7102 | -47.9872 | 2025-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1ab27432-dd70-3206-9f2f-57733376c92d | -12.7294 | -47.9845 | 2025-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e1bcedf5-35d0-3853-83f6-715013afe22f | -8.9917 | -46.2609 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 223.8 |
| ae7611d1-a2f2-3be0-b48b-e2ddd778f7ca | -12.7106 | -47.9649 | 2025-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| d1103b9a-525d-3a1b-82ce-6faa59959cc1 | -12.0051 | -46.6763 | 2025-09-17 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a5f261ff-d45a-3bb7-ae93-2597397d6ac3 | -8.9728 | -46.263 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| c6a0cbd2-917c-3942-a83c-0a9ac40632f6 | -12.0047 | -46.6989 | 2025-09-17 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 9a981d28-0646-3d4a-957a-b0c9d62790f2 | -7.581 | -44.566 | 2025-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 3eff432a-1915-36a1-ba6a-327f5d14544b | -8.4467 | -47.692 | 2025-09-17 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 628210a9-ae1a-3d46-bf9e-3bc1e7ce2f32 | -8.9533 | -46.3099 | 2025-09-17 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 452.7 |
| 4e5e3f15-6677-37f6-a294-0deaf6bbc387 | -7.8259 | -46.153 | 2025-09-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bb4647c0-ab75-36af-ae5d-4bb8f9105939 | -12.4259 | -47.8046 | 2025-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1ac097b0-ca9c-3f59-a0bd-31e0bdba9838 | -13.9648 | -44.9445 | 2025-09-17 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| e25bffab-2efd-3f51-a89e-877dfd79163a | -12.729 | -48.0068 | 2025-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 38057127-fd1b-32fa-9102-3ce7aba61384 | -6.8734 | -43.9636 | 2025-09-17 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 21ab5bad-4784-3080-9325-ed5af10ddf7d | -9.1239 | -44.862 | 2025-09-17 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8ad544c1-7757-3560-a642-97879e4d51c8 | -14.208 | -41.8812 | 2025-09-17 13:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 6af50a48-d5d4-3b4d-86d0-4e8e115a29bb | -5.4897 | -39.426 | 2025-09-17 13:00:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 124.7 |
| fbd9a6f6-de97-3c9d-8505-d42446e0ba48 | -3.8042 | -44.1072 | 2025-09-17 13:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 8ac009bf-5540-32cd-b188-4eba76170e18 | -7.5996 | -44.5872 | 2025-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b3f73c8f-9c10-31c0-ba2a-89e24124872e | -12.7482 | -48.0041 | 2025-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 13df6aff-9d84-3401-a914-54e8d9e4b49e | -8.8958 | -47.8683 | 2025-09-17 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| aab04f14-bcf3-3328-bacb-b2e04e28731f | -8.6885 | -46.3823 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ba9385ea-efd4-3fba-aa17-76cac1f44e59 | -7.5807 | -44.589 | 2025-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 190a95eb-64f3-3de1-be78-ba6484764016 | -12.7486 | -47.9818 | 2025-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 178bd05c-4078-3342-8b31-20692c931012 | -10.6925 | -46.4904 | 2025-09-17 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 004bf2ca-a05d-3b10-add6-14d7ce4abd48 | -12.729 | -48.0068 | 2025-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 54e70613-a2f4-3af4-820d-d2c26e5f4f9d | -8.5609 | -47.5712 | 2025-09-17 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9ca33750-e86e-3ce2-a15e-8402dcac29eb | -6.6127 | -45.6066 | 2025-09-17 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d1489dae-f63a-3148-8962-66d0af64e868 | -8.6887 | -46.3599 | 2025-09-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 31be163f-8fcd-3cbd-bc7b-43e408bc67d5 | -11.1108 | -45.3452 | 2025-09-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1596d3f7-c563-3337-99bd-3558fa0a99b3 | -10.6334 | -44.2324 | 2025-09-17 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c4f745b9-04ac-3920-b17e-b60d2b2321cc | -12.0047 | -46.6989 | 2025-09-17 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 268.2 |


[Clique aqui para ver as próximas entradas](README62.md)
