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
| 9218dcff-baf9-333c-b637-e626aab1c962 | -11.7786 | -47.6474 | 2026-08-28 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8a6f8717-c2c8-3e25-a416-3c8a89e47fc8 | -10.7839 | -50.6346 | 2026-08-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f12e990b-a3aa-36f1-8f43-842c32e8148e | -8.0548 | -45.8616 | 2026-08-28 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3cd71bf7-8fb4-330b-8ce3-1f713c0b4bdb | -10.4981 | -64.5005 | 2026-08-28 15:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| eb499a8a-fcc7-39e9-b3e2-3f725b5572f7 | -11.843 | -47.2152 | 2026-08-28 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 5278d916-6b7b-35f0-b24b-17bd8e1356ae | -6.2298 | -53.4805 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9dd40d78-95a6-3eff-8052-030c353fb560 | -6.857 | -59.4371 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4ac2ad82-c8b3-3fa3-8131-32a1b246b2f7 | -9.4329 | -51.6926 | 2026-08-28 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 146563f0-1d32-3acf-9b39-333794f637f9 | -10.5593 | -50.4663 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4fec6832-490b-354f-bb91-fa689635f889 | -11.2302 | -45.0528 | 2026-08-28 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f4548cc7-7349-3a3e-bc8b-06f172c5f249 | -10.4693 | -46.1802 | 2026-08-28 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 581a7c73-d9a2-370f-82c2-e7504643b754 | -10.7407 | -54.0401 | 2026-08-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d828fa76-4fb4-39af-b2d3-2da8e9978b28 | -11.6603 | -46.7239 | 2026-08-28 15:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 49d42fcd-d3cc-366a-a800-7545e5d7fd2e | -6.9521 | -58.9506 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8cf4a549-b502-33b9-8114-010faf98fd51 | -14.3182 | -51.7046 | 2026-08-28 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 319.7 |
| 8f6620ab-4112-3031-a98f-13904b60ea07 | -9.9708 | -53.9419 | 2026-08-28 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| 8a2eb165-72c9-3ba9-9ea8-44a7af1b5631 | -15.4788 | -53.9628 | 2026-08-28 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 170.7 |
| f6af0a2f-5981-319d-abf2-5341f9eb1c0e | -10.7649 | -50.6366 | 2026-08-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| cf4ac247-3645-3f97-801f-b7c79959906e | -11.006 | -49.6461 | 2026-08-28 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| db67b6ee-690d-3a34-b272-1233a96514e3 | -14.2102 | -45.274 | 2026-08-28 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| b86f09f4-40ec-35a0-a0e3-42bedc93e336 | -8.8184 | -49.6308 | 2026-08-28 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b17083c0-25e8-3cec-8706-817b4c30955d | -6.8755 | -59.4364 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 812aa00d-8dd8-384a-acf8-b671de08becf | -6.8569 | -59.4564 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| bd2a9fc6-1c53-3579-99a7-761f1fc56a1d | -13.5075 | -51.8728 | 2026-08-28 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| cb8f9e25-01ae-3d55-8a0f-c3f9caa99a7d | -10.9187 | -46.6192 | 2026-08-28 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 417.9 |
| e8df9f35-227b-361e-bf83-b3ec63efed10 | -6.8018 | -59.4201 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| edf7aaab-1bbb-394a-9596-63e62de1cc1e | -13.2294 | -51.2904 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 2ca375ce-08f4-3d01-8eb1-a3547d130f92 | -14.4842 | -52.1512 | 2026-08-28 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 269.4 |
| fa15f710-6775-3d31-8fa9-72b98c5e5d09 | -10.5779 | -50.4857 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b767c17e-26c3-3ad1-89d4-080af3a7feab | -12.1507 | -50.6313 | 2026-08-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5a99cc3b-9789-3169-bf55-3ecb2ef60f3f | -11.8239 | -47.2178 | 2026-08-28 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 2d3b6b84-ebd7-30b8-ad48-42203b2b861b | -14.3179 | -51.726 | 2026-08-28 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 66d46972-2bfb-3392-897c-eecdbab23259 | -13.4324 | -51.776 | 2026-08-28 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c8526fec-9781-361d-be92-f51e475b0f38 | -10.7975 | -54.0146 | 2026-08-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b4fc9a0f-a3fa-3e7c-815d-754077f822d8 | -8.0742 | -45.8147 | 2026-08-28 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 9cefe40b-bef0-351a-b399-dc0fe0966cd7 | -13.3985 | -51.5037 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 6b93ea0a-1c1e-3ac5-b390-da54494eaa58 | -10.3526 | -50.3809 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 206818cd-c413-3060-83ce-7615a7d404d2 | -10.937 | -50.5118 | 2026-08-28 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 61adb97b-0f40-3608-ad21-d21e1cdb6fa7 | -8.5968 | -54.7957 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d25a1251-064a-3a2f-832f-734a2d2dbce4 | -11.7354 | -54.5431 | 2026-08-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| dd267edd-c460-3759-85b9-79b180b68ca0 | -14.2097 | -45.2973 | 2026-08-28 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 0cac2ee7-ddcf-3127-9c5c-e32100cb5403 | -7.3479 | -55.1544 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fa24480b-c332-3319-ac27-5cb20dd82f63 | -12.2281 | -50.5578 | 2026-08-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 68dafc02-7b81-3a5c-a590-24dad7f8f7f7 | -11.7165 | -54.5449 | 2026-08-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d1997456-38cc-3098-949d-9dde2c1fb02a | -10.3202 | -49.9782 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2a606cf7-9dfe-34b6-920b-1863bec12a30 | -14.4838 | -52.1725 | 2026-08-28 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bea75a65-192b-347b-af73-250f59bc8af7 | -5.4764 | -45.1035 | 2026-08-28 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4792329b-5e6b-387b-ac5e-7acfaa87abd5 | -13.4191 | -51.4159 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 30f21adc-5c00-36ac-aecb-1cb36e4d2b50 | -10.8996 | -46.6216 | 2026-08-28 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| f2175eab-0ff6-3af1-9c90-241d798a96ec | -13.2102 | -51.2928 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| b1ef7978-17c0-3eff-be84-9a41ed6e0011 | -8.948 | -62.3894 | 2026-08-28 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 1757ae8e-c890-3cad-9962-b032dd773a75 | -6.8017 | -59.4394 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a7a62ef8-edbc-315f-afbe-e64f621e4f83 | -6.8019 | -59.4008 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 70ee8215-0704-3e89-b59b-bfa24caa4349 | -11.7167 | -54.5244 | 2026-08-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8fb680bf-2111-3a6f-8eb2-45af7b48785d | -6.769 | -58.7066 | 2026-08-28 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| c92864f0-ef20-3aee-a3b2-2a66f081a9bf | -13.3789 | -51.5275 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7e68be00-88e2-331f-bf4e-04443026b823 | -6.6167 | -45.1994 | 2026-08-28 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 24f658da-b76d-3795-a8bb-26053c7e6b51 | -10.5601 | -50.4022 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| feedad64-26d8-3ff9-80f8-13ecec20fa74 | -13.5268 | -51.8704 | 2026-08-28 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 77508943-7f1d-3ceb-be23-c7f41ec9c6d4 | -11.8243 | -47.1954 | 2026-08-28 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 220d4c45-8f24-374a-8658-0b617ce0ac90 | -12.2086 | -50.5815 | 2026-08-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| fd45cd1d-6c7b-3ea0-9cb8-c8ca4eb3d945 | -10.3895 | -61.231 | 2026-08-28 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 5af71532-f46c-3064-a960-3c5bb9ecf3a8 | -10.7598 | -54.0179 | 2026-08-28 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5560d7f8-d8bf-3cf2-9eae-7f382ac1c8de | -11.2109 | -51.2476 | 2026-08-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 28cf2e4b-e3f6-36a2-ab00-915e9150cd52 | -8.5969 | -54.7755 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| cd6d4d95-3330-31a5-9bd7-5f5b49878d66 | -10.9589 | -50.2958 | 2026-08-28 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 179817b8-05d1-3085-8d34-1ca4363cf25a | -6.7513 | -55.6853 | 2026-08-28 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 05bcd591-c616-3af7-b730-f96ccdf5ab5c | -6.6397 | -53.173 | 2026-08-28 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7015b9c1-0bd3-3005-933d-e85cd6c022e6 | -6.6396 | -53.1934 | 2026-08-28 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e830fd80-e0fd-33f6-97e7-720a2259b70a | -9.7028 | -48.1366 | 2026-08-28 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 307.1 |
| baacbd43-01ae-3248-8cac-80b7c0b0a4f9 | -11.2497 | -45.027 | 2026-08-28 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e23f5f7b-17b6-3adb-9878-5dabc40e0604 | -6.7698 | -55.6844 | 2026-08-28 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| fb19a430-dfd9-3af9-b27c-540aaec968ef | -10.8992 | -46.6442 | 2026-08-28 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 179473e9-4819-3dbe-9e3b-e21cb3a86853 | -14.4444 | -53.3806 | 2026-08-28 15:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a18d2eea-ba68-3bd5-bebc-e2a797d05abb | -14.6024 | -53.1508 | 2026-08-28 15:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 6bf4da35-5191-3e07-8c2d-e5eb87f2f9db | -11.7357 | -54.5227 | 2026-08-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ee27a85a-7ad0-370a-b668-47d22acdc4f2 | -7.3478 | -55.1744 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 589fdb82-ff29-3459-aee4-51802f01f6bc | -16.1641 | -58.5851 | 2026-08-28 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| d9f104a1-e61f-33ed-9965-9aaa6b3cfa93 | -6.2676 | -53.3768 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b2af01e0-fc11-3dda-9a62-814aa565f327 | -7.3665 | -55.1534 | 2026-08-28 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 00af9f78-8c96-3ce7-ab94-2a009c9e1233 | -16.1638 | -58.6053 | 2026-08-28 15:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| fd9cda20-4756-3dc8-b4e3-e61904ac010b | -15.4594 | -53.9653 | 2026-08-28 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a59d6ca5-0caf-35bb-9863-bd78963d4897 | -14.9161 | -40.9358 | 2026-08-28 15:00:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.0 |
| d77dbbf8-ee4c-3509-b9c0-700748ed1c8b | -13.4194 | -51.3945 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 4b7f4f56-fd38-367b-bc15-eccee33aff59 | -10.3391 | -49.9762 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0c5bacd2-681e-36c7-baf4-22a9e0dab319 | -12.0733 | -47.1614 | 2026-08-28 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| afa436cc-944b-38f4-beee-9eb22107d588 | -6.7832 | -59.4401 | 2026-08-28 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b4b0792a-9ff4-3360-a56f-09090374bef9 | -13.3988 | -51.4824 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 16101b86-dad6-37ce-bb53-27c9cc61a321 | -10.498 | -64.5193 | 2026-08-28 15:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8716672b-e21c-351d-b276-9fd9ed1b2f08 | -9.1525 | -49.9639 | 2026-08-28 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3a08e1a6-3d1b-3379-bac4-4009d63ae697 | -9.4758 | -48.1822 | 2026-08-28 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| a86b558c-54a8-3025-b6cb-e94704520db0 | -10.5598 | -50.4236 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1024ba92-a9e8-3bc9-b7e0-f2c687dc1320 | -8.8372 | -49.6291 | 2026-08-28 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0e425492-f79b-3786-b2ec-214a222ab7da | -13.4132 | -51.7784 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4f85bbc7-1e82-3143-8762-7199c4941e85 | -14.8817 | -52.6293 | 2026-08-28 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fa1cc4e4-556e-3cd3-9902-0c4802f6bf70 | -9.08971 | -35.31077 | 2026-08-28 15:09:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 83d9214b-c681-351c-abdc-2312b847e1c5 | -6.91818 | -38.48607 | 2026-08-28 15:09:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 15.3 |
| e580b810-ba83-34bc-9435-856439acd416 | -9.0956 | -35.31017 | 2026-08-28 15:09:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9e8c082f-3216-344a-a0fd-303f59970995 | -6.91832 | -38.48993 | 2026-08-28 15:09:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5f8de69c-ea9c-3ff5-b16d-7bc293d77419 | -8.9478 | -62.4084 | 2026-08-28 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 153.1 |


[Clique aqui para ver as próximas entradas](README82.md)
