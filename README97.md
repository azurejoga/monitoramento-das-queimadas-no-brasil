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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68c414ce-a243-3a9b-8db3-8865c4c1bfa4 | -10.6755 | -50.262 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3bbdf17b-680c-3793-b505-7cae9c543888 | -11.8556 | -50.0006 | 2026-09-18 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| cba4c63f-aabf-3cec-8f3f-2d99df3745de | -10.6723 | -50.4972 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c69bce12-8b33-30cb-a844-ab067aa3a482 | -13.4303 | -51.9036 | 2026-09-18 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 01fb7785-60fd-33f2-8974-a6d4ac7fd613 | -13.2485 | -46.9226 | 2026-09-18 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 296.0 |
| f11542f0-da05-36b4-9860-cf3f28acafc1 | -19.5539 | -47.6346 | 2026-09-18 13:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2d810300-56a4-3407-8ca4-1d3f45e7e5f5 | -11.2975 | -43.3851 | 2026-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 3ff956a5-c457-3a12-902c-9fc13c269932 | -14.8026 | -48.5622 | 2026-09-18 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2e8273b1-51eb-367b-8db8-4bdcf4ee2ca3 | -10.6536 | -50.4778 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 3d42d483-781d-3d9d-8b65-b45fb29e2e2e | -11.2979 | -43.3614 | 2026-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| bb67007b-f647-35b8-8022-ea57b5a5c768 | -8.4503 | -45.8448 | 2026-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| caf3efe7-2d2a-3a95-9bef-044ec839a567 | -7.8027 | -44.9108 | 2026-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| baa680a2-f97e-3956-8066-af2686f04942 | -7.8036 | -44.8422 | 2026-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1cd4054c-dd41-3fbd-8050-c151e5634b27 | -12.0086 | -49.9606 | 2026-09-18 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| af790219-3c75-32de-a548-28b0c563d1ea | -15.6752 | -52.7339 | 2026-09-18 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7eea5ec6-b0e3-3148-be27-d3ec48c82e4b | -10.3116 | -45.3136 | 2026-09-18 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0752b476-8825-3cee-a240-142858ec8e9e | -10.1179 | -45.5662 | 2026-09-18 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| eecf14bd-6360-359f-bf58-8c0b728f744f | -12.998 | -46.9381 | 2026-09-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 28b6355c-74ae-35ea-b81e-d1adb23af930 | -12.1719 | -46.9906 | 2026-09-18 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d457d6a8-c0e7-3d23-8497-d410a8ff8c65 | -7.6762 | -46.0995 | 2026-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 5935003a-8e43-3d03-8373-18f955b207d5 | -11.0636 | -48.3118 | 2026-09-18 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b4ae3f1e-61ac-3dcd-a95d-f987172d0286 | -5.915 | -53.5168 | 2026-09-18 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9fa7ecae-6368-3ca0-a377-e7845729ce5c | -10.3303 | -45.3341 | 2026-09-18 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6633aa30-aad5-397f-ad84-cfb694c91575 | -12.0458 | -50.0208 | 2026-09-18 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ac98053f-ddb8-3799-88ea-70b8c4f708b5 | -11.8556 | -50.0006 | 2026-09-18 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 01b12d4a-154c-30bc-b9ff-d89c61a1a4d2 | -11.064 | -48.2898 | 2026-09-18 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 08773fa2-8c0b-3ad1-af11-7ef56d7a6065 | -7.0448 | -42.0906 | 2026-09-18 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| ec124fa4-2576-3b89-bfe6-d221e22d63cf | -11.4861 | -45.7279 | 2026-09-18 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 12ba9389-6a45-3d0b-ac02-bb081bcdd174 | -12.0267 | -50.0231 | 2026-09-18 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e8734dcd-34db-3045-b0fd-89b3d9717057 | -10.6723 | -50.4972 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| a164eb3a-56bb-3356-bbc8-d42a41c08281 | -10.6533 | -50.4991 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 8673feab-96c9-32c4-9b49-5728658f1e43 | -7.1384 | -42.1529 | 2026-09-18 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| c4038862-7070-377d-bf8f-5416bc97d8e4 | -11.2783 | -43.388 | 2026-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1bd533af-8f83-31df-bd37-eb308ca0be20 | -10.5178 | -46.7366 | 2026-09-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8c3e4c06-28cb-3563-9803-8c618edb51cc | -11.2971 | -43.4088 | 2026-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| abf175ee-1d0b-3c41-aa97-3b6fc7155f44 | -7.0352 | -44.6396 | 2026-09-18 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f7954ed1-fa72-3a59-bf08-d8d4603dd503 | -14.1732 | -45.1875 | 2026-09-18 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 53410acc-a830-35fe-8bd5-90f027b24ab9 | -8.6817 | -45.4359 | 2026-09-18 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.2 |
| f4eb80e4-df3f-3c7b-ad18-452a2ac2a25a | -12.5149 | -47.0991 | 2026-09-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2cef6eff-76ef-3bf4-a633-8d81f74136e7 | -13.4307 | -51.8823 | 2026-09-18 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 39396375-2af4-334f-bd95-dfb8ae06b28e | -11.3442 | -43.9906 | 2026-09-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 22d7766b-d3e8-3bc5-a885-515530f207d0 | -13.6531 | -45.97 | 2026-09-18 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 999e6e77-409b-38bc-8542-664ceac94147 | -7.8033 | -44.8651 | 2026-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 079c91b5-7574-3e1e-a820-1dcd9c048055 | -12.5341 | -47.0964 | 2026-09-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 256be0ce-14e5-39e2-ae8d-52517a79ea1a | -7.7842 | -44.8898 | 2026-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5a47751c-1d08-35fb-93e1-60baaa64f05e | -6.314 | -41.7528 | 2026-09-18 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 26ed922f-ba0e-3aae-af45-f7970fe47016 | -7.1198 | -42.1309 | 2026-09-18 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 127c2861-4f67-3790-b200-a12a2645bab9 | -7.6574 | -46.1013 | 2026-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 39d4b4b5-b692-3f06-a012-24970e0fdcd5 | -10.6189 | -50.2466 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 19e0c9a7-e1b1-3000-ae81-693cd5b4decf | -7.1086 | -43.1027 | 2026-09-18 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| a1c54f4d-112f-390f-94d7-159d38dd31e4 | -7.8038 | -44.8193 | 2026-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a2c6e425-d085-3277-b4a9-ef9d3047f4be | -11.8115 | -46.8158 | 2026-09-18 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 57ca4231-6ee3-3678-ad0f-7bda78cc19e3 | -12.5345 | -47.0738 | 2026-09-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 327d625b-53cc-3edd-9aee-f0a0006cbd1c | -7.1088 | -43.0792 | 2026-09-18 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 17a94595-f955-3d28-938a-38e6a9dfcec6 | -11.3437 | -44.0141 | 2026-09-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 610af18d-a74b-3851-a641-175b5f9b1818 | -10.6755 | -50.262 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| d1803d0f-6d95-3846-bda0-aa3b01763020 | -10.6726 | -50.4758 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 7885bc3a-f18d-3fed-b1e0-cb94a4c78c7a | -7.6765 | -46.0771 | 2026-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 98bd9743-5097-315d-9a79-9698c11cda86 | -10.6944 | -50.26 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| a565d02e-8933-37f9-bef4-e87ca777e978 | -14.1737 | -45.1641 | 2026-09-18 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ece9bb01-d724-34a8-9699-e18de4934b1e | -13.6148 | -46.9334 | 2026-09-18 13:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| de9d0ea3-acf7-37d0-b70e-3f57f4cd523b | -10.1369 | -45.5638 | 2026-09-18 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 59369a68-ade1-3299-b185-eeca3d4b5c53 | -7.1195 | -42.1548 | 2026-09-18 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 2ca32ecf-620c-3219-b5e6-001315bddf1f | -9.8316 | -48.3854 | 2026-09-18 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 3891a0b8-78e0-36ee-b832-eca414ed26c3 | -13.249 | -46.8999 | 2026-09-18 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0f9669b9-cbef-3f02-b14d-e3240676cadf | -12.0672 | -47.5198 | 2026-09-18 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8bbc2a47-b0aa-36ef-b971-5a10176d229a | -12.6235 | -50.8953 | 2026-09-18 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 40a7d217-bb98-36c1-ad21-3164de765e1e | -13.4303 | -51.9036 | 2026-09-18 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 318.8 |
| 2601afc7-6098-32e7-baf4-d704b2b4489a | -11.3446 | -43.9671 | 2026-09-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 44ad0d43-193e-36a3-9dc7-33bed30f52ab | -7.6577 | -46.0788 | 2026-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 1c0d5379-1a29-374c-b649-dfe2a6706b16 | -4.5587 | -42.9523 | 2026-09-18 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c18de118-f953-36a1-9af3-bf70466e4eeb | -13.6341 | -46.9304 | 2026-09-18 13:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 51511d13-7bea-3fa2-a414-964142102f5b | -4.9183 | -47.4295 | 2026-09-18 13:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2690d78f-f765-3e3f-996e-93389d4b638e | -10.6758 | -50.2406 | 2026-09-18 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 279.4 |
| f9a5025a-8905-3d35-92d7-8003eadda30a | -10.3307 | -45.3112 | 2026-09-18 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 0744954e-62e0-3a4d-8fb1-99e9504e118d | -6.3137 | -41.7768 | 2026-09-18 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 592e16af-e8c5-3c4b-b9b8-de449d033911 | -11.3617 | -44.0817 | 2026-09-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 277eb77b-f819-39db-a04a-83293d76aa43 | -9.8505 | -48.3834 | 2026-09-18 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| caa1b8fc-66d4-38fb-b46b-ee3632ed769a | -11.3809 | -44.0788 | 2026-09-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 55f637f8-2592-31bc-ab2c-38b452a6d651 | -11.0048 | -49.7325 | 2026-09-18 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 222b54c8-46e0-3ab7-aa12-d51f01439585 | -12.6427 | -50.893 | 2026-09-18 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| dc6b395c-4798-3c36-841c-84af1556b28b | -9.9505 | -45.336 | 2026-09-18 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fea089af-c26a-3bee-b92f-5a90ae70b785 | -7.0275 | -43.6247 | 2026-09-18 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bf0830ae-87e1-37a0-9d37-07e980ac556a | -13.2485 | -46.9226 | 2026-09-18 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 4b9e2f3f-2795-3534-b8f8-f34fcef0c171 | -11.3433 | -44.0376 | 2026-09-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 38174186-f78e-3993-9c10-8b69c214441b | -10.3303 | -45.3341 | 2026-09-18 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 8f6e2946-f767-35b6-91c7-519ff1a6cb2c | -7.0352 | -44.6396 | 2026-09-18 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e5ebdcf7-61fe-3ada-98d1-bd855095a1b2 | -12.6427 | -50.893 | 2026-09-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 39db77eb-9b6f-3b64-816c-23e0aedff931 | -12.998 | -46.9381 | 2026-09-18 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 009afcd3-9b9a-3986-ac16-aaa1f78fef50 | -7.6765 | -46.0771 | 2026-09-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b6e64b02-890b-3c76-bc19-1f3c90c50b7b | -10.6533 | -50.4991 | 2026-09-18 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7f079a8b-ff07-327d-9823-50db556941e3 | -12.5345 | -47.0738 | 2026-09-18 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1e9962dc-66af-3e45-8565-5c5c7592faa0 | -11.0636 | -48.3118 | 2026-09-18 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4cf8b1f0-cf61-3bdd-bb03-25e1ce973bb0 | -3.7333 | -54.6499 | 2026-09-18 13:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| f671683b-3f2a-334d-8b71-c39a1607bb2a | -12.5341 | -47.0964 | 2026-09-18 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a56ec856-8272-37e1-9772-84c99e7bcbff | -5.6596 | -43.3906 | 2026-09-18 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| f51ba5ed-5f51-3f25-b21a-6d078a9ce446 | -15.6752 | -52.7339 | 2026-09-18 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6e272f4b-a7a3-3115-9d24-2120c7ce8525 | -13.4307 | -51.8823 | 2026-09-18 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 047b7607-8308-3614-994b-21d5baff496a | -12.0481 | -47.5224 | 2026-09-18 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d3641c1b-7269-30c6-85e7-cc57990a9d53 | -7.8038 | -44.8193 | 2026-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |


[Clique aqui para ver as próximas entradas](README98.md)
