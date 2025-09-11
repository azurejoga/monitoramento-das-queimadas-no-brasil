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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed2e111-9a7b-3564-9d53-22a03dc7be00 | -8.1649 | -46.0983 | 2025-09-11 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 83ede533-6c34-38f0-9e99-07e3d1764e93 | -6.4364 | -44.4847 | 2025-09-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 9152c33a-baf8-3cc0-ad29-bbecaadecbb8 | -11.7211 | -46.5127 | 2025-09-11 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 476.4 |
| fde61c52-de7e-3f0d-877d-40908b1e4bee | -6.2228 | -43.3226 | 2025-09-11 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ec899fa2-8824-33e2-9c76-d48128320adf | -13.241 | -51.7571 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 232de599-e56a-3342-ac08-5d0f68cc6be6 | -11.3718 | -43.5157 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| bde8c5ba-f150-3031-842d-f47aa3d57643 | -12.9976 | -48.0131 | 2025-09-11 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e6bffe18-b282-3c27-a33b-2fbf1457b431 | -6.3226 | -53.4553 | 2025-09-11 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a3c3eefc-b55e-3183-8695-74c12fc68979 | -11.779 | -46.4821 | 2025-09-11 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 2a77d861-32ad-3311-95f0-e731218fcc2d | -8.8755 | -49.5613 | 2025-09-11 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 1535cd60-1d57-3ed5-a086-bb3921661fa9 | -11.429 | -43.5307 | 2025-09-11 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9745b4d0-92c5-363f-99df-8b4cc970f991 | -19.2611 | -48.0221 | 2025-09-11 13:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9cba5602-d435-3122-ae99-b1c5e19a2b03 | -10.7369 | -46.0785 | 2025-09-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 970dc3e7-dd6d-3d8f-af8e-0db96397f7b8 | -7.852 | -45.5199 | 2025-09-11 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 27a70785-8f3b-3f5c-905d-0fafe29f935e | -7.5592 | -48.2505 | 2025-09-11 13:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ed8aaf25-7313-3e4d-ab62-bcab657e35d0 | -9.0753 | -47.078 | 2025-09-11 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 95213058-8eb4-399e-9e5b-75169e75fea1 | -6.4364 | -44.4847 | 2025-09-11 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| fd936352-e029-38f3-b170-ba78c670fc43 | -10.3885 | -50.5264 | 2025-09-11 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 2f16b258-2c9d-373d-833e-3f7d7d51c518 | -6.8525 | -47.8707 | 2025-09-11 13:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4b7d06b1-766c-38c8-baab-21d070f78062 | -9.0759 | -47.0335 | 2025-09-11 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 02660010-b9d3-320e-88a2-1f56abaa0408 | -9.9398 | -46.064 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| d4207d9c-8b2c-3a9f-9029-91cea8182f6f | -10.184 | -46.2153 | 2025-09-11 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 223.2 |
| a9e7bea6-d214-39c7-a23d-5be248413a39 | -9.9026 | -50.17 | 2025-09-11 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a0504cf1-f5d6-30e8-a19c-aa68a809a821 | -6.0784 | -44.6961 | 2025-09-11 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d45e7960-6cfa-3624-84e7-c4bac18cf92a | -9.9004 | -51.8811 | 2025-09-11 13:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 948c9c52-9423-3a79-8127-cc7c8f3027a5 | -3.9564 | -40.7207 | 2025-09-11 13:40:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 95da931d-7727-312f-be9e-e7a47eb62ef3 | -10.6606 | -48.6218 | 2025-09-11 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 15f7eba9-1854-3739-aac1-9838a850b619 | -11.7112 | -48.2757 | 2025-09-11 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 401.9 |
| c4c95c35-d6d1-39f5-8044-7ae9e5139e1a | -6.1894 | -41.0641 | 2025-09-11 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 045a43b7-fd35-3e40-af6a-5e6ce9cd45f3 | -11.7211 | -46.5127 | 2025-09-11 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 209.0 |
| ab135a70-d8d3-3f8c-b33e-f9c9a923f03d | -15.6732 | -47.0389 | 2025-09-11 13:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 91b62138-c1f8-3caf-9f15-659ebc5b769f | -11.0997 | -48.4392 | 2025-09-11 13:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 41ae734f-15a4-3d5a-8752-86dd75fc31ac | -12.9292 | -54.7538 | 2025-09-11 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 7521550f-ee9e-3090-bb53-964bd3a653af | -15.8014 | -52.2258 | 2025-09-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 90928657-ef6e-3053-9d71-d5c9fc3cb126 | -10.5671 | -47.2442 | 2025-09-11 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| f167ead4-fc84-38e8-8e1e-3cbd12029f99 | -10.6796 | -48.6196 | 2025-09-11 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| db8de4f5-9953-3f31-8df0-ba477ea6aab7 | -6.2228 | -43.3226 | 2025-09-11 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 70f2d69b-2cc5-3dd7-94f1-85994bc02b50 | -11.1 | -48.4172 | 2025-09-11 13:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f8d24c21-69ad-36a8-96cc-1ae3668c0300 | -15.749 | -48.0459 | 2025-09-11 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 56e8b0be-9b65-3815-93bb-f69df362a5ef | -15.801 | -52.2472 | 2025-09-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5a3dd1f5-68bd-3e73-be1c-a71eb4cf24fe | -15.1016 | -50.1468 | 2025-09-11 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 197.2 |
| ed203bb4-2f54-3674-ab26-5bc25a018871 | -15.8006 | -52.2687 | 2025-09-11 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 40a6ec30-91dd-301f-bc26-fb1354ff4063 | -9.0567 | -47.0577 | 2025-09-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e2ad7b33-3da2-3224-b13d-cc4c94994a11 | -11.391 | -43.5128 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d7e48608-2695-366c-b896-7fc02516d448 | -9.0262 | -49.5261 | 2025-09-11 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e4e0553d-b1f4-3015-8b07-837df337d1e8 | -9.7445 | -47.8468 | 2025-09-11 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 20227686-80b8-361a-9cf0-8548d6956841 | -8.994 | -46.0808 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| dd6c62d1-f64c-3382-93c0-068e9d48d851 | -11.3397 | -46.4967 | 2025-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| fba83f44-6f98-3441-9b73-8226149fc955 | -9.0939 | -47.0983 | 2025-09-11 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2bf4d9b4-1516-3e83-a092-1f41466c4424 | -17.3749 | -52.9341 | 2025-09-11 13:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6d3295de-05d0-39f5-87bd-aeb2c0480e6c | -7.559 | -48.2723 | 2025-09-11 13:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0eccf894-65d3-32a1-ab43-ce7f5225810a | -6.1705 | -41.0658 | 2025-09-11 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| cb05c60d-5bb9-36ee-8c35-8bd4547b6ad2 | -8.9365 | -46.1545 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c2789cae-9206-3505-b3c2-ee2c5bc28d6e | -11.4281 | -43.578 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 268716b2-240a-39ce-8d07-4baee59e5e22 | -9.9762 | -50.3121 | 2025-09-11 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 870301fd-e762-3677-a06e-a83cbf54ce92 | -11.779 | -46.4821 | 2025-09-11 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 922c3818-fe75-3f7d-94ea-f9ed0cb0058d | -13.2798 | -51.7312 | 2025-09-11 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c20cdc7d-ad17-391e-b582-4f74974a3320 | -11.4097 | -43.5336 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 293ec53d-e3bd-369f-8615-9ffdbddc4ba4 | -9.0265 | -49.5046 | 2025-09-11 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 456cb87f-6919-3f84-9ed8-2da2dc4de615 | -9.4611 | -46.4566 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 040900e9-8f8b-3545-8965-ff684f83150a | -22.9617 | -49.7387 | 2025-09-11 13:40:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.5 |
| f5546ea1-7fe1-3c45-bfa4-bf61b6fcc0b3 | -5.9193 | -45.7492 | 2025-09-11 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 65987d18-f4de-37c6-9985-85b5b20133f9 | -15.7681 | -48.065 | 2025-09-11 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 063d90de-5739-3443-b61d-4596595f8d70 | -7.852 | -45.5199 | 2025-09-11 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ba35660d-8e43-3926-892f-705a0013b525 | -10.6603 | -48.6436 | 2025-09-11 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8c65c247-43ea-3ab1-ae5b-3426aa04e574 | -10.8594 | -45.5622 | 2025-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f7368012-3b9e-3fbd-bb7b-6917187bf6df | -9.7634 | -47.8447 | 2025-09-11 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 58c37bb1-bd68-3ea9-b54d-f9b350d434f6 | -9.0579 | -46.9688 | 2025-09-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f2cab8fc-a8c7-3481-a4af-f42d71525480 | -4.553 | -43.7439 | 2025-09-11 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3fd77d81-ab0b-3b9b-a0b0-34a1b34466aa | -9.4804 | -46.4321 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3722424a-2714-3bdf-bfdf-81fbc4d2d2e0 | -10.203 | -46.213 | 2025-09-11 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 9efb4ede-33f2-3e47-8414-1dddc66fea5e | -19.2611 | -48.0221 | 2025-09-11 13:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ac5fae8a-67f9-315a-ae90-e82a64273546 | -14.1492 | -45.4009 | 2025-09-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| fefc2796-7cb5-319a-b58f-17ba82c8b4b2 | -10.1844 | -46.1927 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 7f756e63-e313-31d2-bf1b-6663ebb4677e | -14.4464 | -53.2544 | 2025-09-11 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 2cea17c9-bb8b-3c1c-ac2a-96cbd3ca61bd | -11.7115 | -48.2536 | 2025-09-11 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 245355d0-7bad-39f9-a4ae-acc22670f52e | -22.9828 | -49.7336 | 2025-09-11 13:40:00 | GOES-19 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.0 |
| 036bf942-ea48-3e42-abc6-40c22b68573a | -15.1211 | -50.1438 | 2025-09-11 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e1e75786-9a31-3d2f-a07e-22f29805de62 | -9.4797 | -46.477 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 9f1e7c9c-333e-311b-9e08-efcafe4fdfa1 | -10.6793 | -48.6415 | 2025-09-11 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| fc83e171-6b91-389b-a78f-92c2fded94a5 | -11.4845 | -43.6402 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 35ea7d67-8747-33d0-b7ea-1dbd4367af74 | -11.3588 | -46.4941 | 2025-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| d8af46ab-252a-303f-b0b9-2b5a56d4d531 | -10.7366 | -46.1011 | 2025-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 933344a7-ac1d-3e4a-bded-c28a6990b386 | -9.7011 | -46.877 | 2025-09-11 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f71c68b0-7027-3635-aa0f-38371757bf5b | -8.8755 | -49.5613 | 2025-09-11 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| ee09992c-e47f-3dba-9ade-8f2ebf385f84 | -8.1649 | -46.0983 | 2025-09-11 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ec332754-4ddb-384b-987b-77aa0418e615 | -15.1021 | -50.1249 | 2025-09-11 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b811f54e-21ce-3f55-9ab8-51197ebe6f0c | -6.2226 | -43.3459 | 2025-09-11 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3db01ed1-f0fb-3739-aa73-11dce8f6168e | -8.5667 | -45.5842 | 2025-09-11 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 3cd86afd-3eea-3ffe-bf79-ab27b2a22924 | -14.2927 | -45.0495 | 2025-09-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 88c8832e-1224-3c83-8b0f-55140124bce7 | -6.8187 | -45.6123 | 2025-09-11 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e60ed32d-b24d-356c-bf27-a4afeadfc944 | -13.2602 | -51.7548 | 2025-09-11 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 0cfc3a0d-f04b-30d3-93f9-c56db65cec1f | -11.7786 | -46.5047 | 2025-09-11 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 306.0 |
| bd5e745c-1d8a-32b3-9c9c-cf004f013e29 | -14.4461 | -53.2755 | 2025-09-11 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8a2a1687-6464-34d7-ab53-2e181d3bcd4b | -7.8708 | -45.5181 | 2025-09-11 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 22c142f3-4523-39c2-af28-b8220cb92c28 | -11.4093 | -43.5573 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| a20675cc-5e26-31d9-9ab8-00539fe50e8e | -11.3718 | -43.5157 | 2025-09-11 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 38dfc68a-23ee-3224-9816-b48e7a101dc7 | -9.0129 | -46.0788 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0d18e603-a08b-320f-9272-672dc4f17b2d | -9.1514 | -47.0257 | 2025-09-11 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 511e2850-30f2-3875-9fd9-1a9623da932e | -9.4801 | -46.4545 | 2025-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 433.1 |


[Clique aqui para ver as próximas entradas](README143.md)
