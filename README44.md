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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45d1626f-b272-3d9d-b0d3-fcd57481dd7f | -14.13179 | -53.69492 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b17f75bd-ba73-340c-8989-0cd6fa3af60d | -14.3829 | -51.88943 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 661e9283-f1a0-3c77-b6b9-5e2942473039 | -16.336 | -55.38627 | 2026-08-16 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ebe28a55-5717-36df-bd40-7622cab020d4 | -11.58617 | -54.69294 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beae003e-cd11-387d-aade-5ce028b0228f | -13.26713 | -51.67696 | 2026-08-16 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 004321a7-b487-3235-b1b9-457d1bab5ca8 | -13.75731 | -53.4363 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c53bc2fe-3ba1-383b-951d-9c421e46214a | -14.3326 | -51.97642 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b284c11-0708-3f2c-abdc-5cc843a4c3c8 | -12.67141 | -48.45949 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 491ca03f-8710-33f6-88ae-a5b75f37f2e9 | -13.75482 | -53.42628 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 819be8d1-cf3c-30c7-9315-3baaf5b24b0a | -12.57216 | -47.85126 | 2026-08-16 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41ecfbdc-c7b4-3826-83ed-325d8c7ccc73 | -14.38871 | -51.9108 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f5252fd9-c33a-300d-9bb6-37d183150949 | -14.08627 | -53.61382 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52981121-46e4-3236-90c7-d07150fe008d | -14.74363 | -49.24647 | 2026-08-16 05:18:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23be141a-4ab8-3a50-9899-a6ab6081e944 | -14.41068 | -51.84378 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9563221-7ee5-36b6-b2ad-8d55bc1e59d5 | -14.46733 | -51.9981 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f69dfe1e-d328-3082-a98f-dd846b475551 | -13.69914 | -51.87508 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4d7542d-83bb-3387-a30b-3cff284ca460 | -12.70709 | -48.47208 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 755aa18b-1ad2-309b-ac10-a4c2b00d270f | -13.53516 | -46.24937 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9aa250ed-65eb-332a-8ffb-9a07ad93d996 | -14.31044 | -51.95438 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c85da755-a5b0-347c-9719-ea445812954a | -15.16521 | -50.06687 | 2026-08-16 05:18:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0163643c-5f2b-309d-bfae-70f9b22aab9a | -15.54378 | -47.38605 | 2026-08-16 05:18:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530e206f-a3b7-396e-a485-2a1f4772d671 | -13.91085 | -53.94893 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2918746-92cb-3bf8-98a5-0dfbb2c14616 | -13.48701 | -48.22923 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6aa5fb0-2496-3334-9af5-47c2a12af6ec | -12.72351 | -48.46851 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c15ccc5f-ac30-334f-81db-784450e53796 | -11.57626 | -54.68735 | 2026-08-16 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f30172e-cdbf-3250-8a46-3b3bc3297f5f | -12.70524 | -48.48678 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73f2ef37-d3d9-3341-99c2-ad1e66076280 | -15.0679 | -47.02671 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1198295-7797-3a5d-b5cd-86f5c3010ff5 | -14.41461 | -51.94316 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5519b35-1b13-3bcd-a094-dd0eb2a08bda | -13.54748 | -46.25002 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ead2296e-1c5e-3bf0-9b57-80e1278fb7d1 | -15.117 | -48.18024 | 2026-08-16 05:18:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6250431-2740-3293-8210-635132453823 | -14.48811 | -45.68642 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6940409-1f81-3f94-a744-623c5a4cfc65 | -12.05784 | -58.0408 | 2026-08-16 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 780251df-4c2b-3587-be55-eae260c46a01 | -14.32561 | -53.30672 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ca22f7a-ee95-3915-8fc3-ee402747a9c1 | -12.70152 | -48.47405 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fdffa23b-8597-322b-9532-1bebe715b9a3 | -13.42069 | -57.04639 | 2026-08-16 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73b49cd6-b5b9-3d63-9bef-adad723af092 | -16.33659 | -55.38211 | 2026-08-16 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50ffabde-9173-30fe-ae52-250b418fcfe8 | -14.90681 | -46.62617 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0838e3d0-47bf-3baa-86ea-c2def4786bdc | -14.48869 | -45.68106 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef635444-a05a-3eee-9d48-d17d064fabd3 | -11.32628 | -61.26673 | 2026-08-16 05:18:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f8659ed-3aef-3b6a-9aec-009757d5e604 | -12.70039 | -48.48309 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6932bc64-450c-34eb-9bcd-df30387daccd | -14.44237 | -53.29609 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2292d13f-2158-33f1-acae-3c64d0818a16 | -12.72868 | -48.46969 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e8a6584-e437-35ad-bf4e-4ae45133f7f6 | -14.22596 | -51.81664 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ecf7073-4615-3c80-9755-b1044cd23317 | -12.71268 | -48.46993 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e803aa4-c4d4-3896-a033-8f2a46e4b2fe | -14.4857 | -54.02187 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d77f2afc-8ea0-3f24-9162-03b46fb9ecb6 | -18.59089 | -47.13339 | 2026-08-16 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bff72234-93e8-30a7-8ee1-c69e19724825 | -14.06778 | -53.68861 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 194f650d-db86-32e4-9d25-912ba22f511e | -18.59106 | -47.13228 | 2026-08-16 05:18:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc7359fd-36dd-3bb0-b602-7141e2269929 | -12.39421 | -55.76605 | 2026-08-16 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93fd2cb6-16d6-3e77-aa10-9fa898061fef | -14.40153 | -51.87968 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7675fd6-752f-3274-b1af-a761e5f646e3 | -16.89742 | -54.17164 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 740dd734-dd36-3c2e-bd83-28a30913716f | -14.22732 | -53.03828 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 051ce417-5de2-37c2-9f3a-1190f87829c3 | -16.2124 | -57.64059 | 2026-08-16 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f9bfe605-2262-3cb2-8680-a084a882dfbe | -12.71791 | -48.47066 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7759467f-1c6b-32f4-b276-0b87bb480034 | -16.8936 | -54.17108 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76eaaa49-69c5-3e97-a3b3-10e427386640 | -14.38769 | -51.886 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0c95b9a-3e04-3dba-b923-48291109ff3c | -14.32881 | -51.97744 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3472af9-48a2-3a97-92ec-aae6a452f959 | -13.65412 | -46.2426 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f15c008b-571c-348d-b9ed-3987266688cb | -13.4973 | -48.23433 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78df35d5-d9fa-3878-9ed7-e7d888f83355 | -12.67819 | -48.44773 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c75d2d0-cc5a-39f1-a52d-f4534a8eda69 | -12.71228 | -48.47311 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca5553bc-29bd-31ff-9e75-d3937cca69d5 | -15.06831 | -47.02294 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5e8c9361-cedf-3264-ba2d-b8b97459d499 | -14.90021 | -46.63034 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d19e427-55d0-3629-8425-04ef55f358d4 | -14.4183 | -51.94776 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a24539e-5cd1-3c9a-88c6-6e90340bf478 | -14.75764 | -56.36316 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ca0b68-91fc-34c7-9301-62b6176efe5b | -14.90621 | -46.63167 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17ebe821-9a9f-3a29-ae54-fb089516ccb1 | -14.28985 | -51.94733 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2353c2d5-8394-34ff-b87a-142cf85aac7a | -13.65366 | -46.24671 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a04d3c4-78b8-33c3-9f99-9f8f07a24394 | -12.67776 | -48.45125 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5d7d884-3664-3c12-a7c2-2137352e05fc | -13.49238 | -48.2299 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c80c42b-5ca0-3d37-ad1a-5921ba743df2 | -13.79798 | -53.82757 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7664ecf-ef23-3876-ae6d-1b9fa2ed7875 | -15.05699 | -47.01647 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eff51544-c44d-3b75-9cc5-672d8d4ab644 | -14.38344 | -51.88538 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 488e8fe3-a2e9-34dd-bd25-d16624028973 | -14.33135 | -53.12325 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07c56660-c3cf-3bcb-95dd-7265fd19c020 | -12.67735 | -48.45456 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a558d0c-c065-3f39-a0e9-13f3e231bcb2 | -14.07068 | -53.72214 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14039b7f-289b-3345-ab08-a10a2a286ee7 | -14.07155 | -53.68924 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bcb0b6b-552b-3e7f-bcd4-d1f6d9014982 | -12.56672 | -47.85055 | 2026-08-16 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 165b624a-432e-33e0-b4e3-fd0c408e77bb | -15.22911 | -57.6559 | 2026-08-16 05:18:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 270c66ea-7ed3-3147-95c8-b09617f51667 | -16.33242 | -55.38589 | 2026-08-16 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7a62158-7991-344e-87d9-80e92c0c08ac | -14.77837 | -56.95192 | 2026-08-16 05:18:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eeda5c8-2d00-3282-9082-1239a0dd72dc | -13.49821 | -48.22696 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdbbd705-de8d-30f2-8435-64e4dc442d2c | -12.68221 | -48.45828 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b06756f-9785-3c1a-aeee-1d903c77c111 | -13.69834 | -51.87766 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89d02742-de53-3720-8845-0b6d35a42340 | -16.92501 | -54.14142 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89e47a47-3f06-3352-bb0c-931f6c2d5ca3 | -15.15366 | -48.67169 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55e560f1-60a7-3fd5-bd63-0a6f3b1c1270 | -14.48171 | -45.68566 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e34129c7-d8d2-3c71-9f20-bf06b2bb3975 | -13.70687 | -46.27014 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36db3b93-e8fb-34fb-8b0b-e1ef37e2bf7c | -12.71045 | -48.48763 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b227ebb-0ac9-363f-9bb7-4d903172407e | -12.70671 | -48.47514 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| add82386-feb1-3390-99e5-2d7f71b6d7e2 | -13.50806 | -48.23562 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c68197-35c1-3773-bcc5-2b418fe968a0 | -14.22169 | -51.81602 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd559a90-be7f-3cce-ba96-e7b3507e0d5b | -14.48115 | -45.69098 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 736a78c7-5fbe-3cd9-83db-78f2c921c48f | -15.70527 | -47.62687 | 2026-08-16 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9285d34-43ce-3089-9452-e220d96c2a6e | -14.41494 | -51.84439 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 418cc897-b040-3452-a693-80ed7c4644e5 | -14.44626 | -53.29665 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d057ad3e-af6f-3f4e-9ec3-dab6cfe26884 | -15.22967 | -57.65231 | 2026-08-16 05:18:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6834588-2c47-3820-a1fb-0ab31922731d | -13.43953 | -43.8572 | 2026-08-16 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51cf8bac-0509-3f51-b03b-29eccbf30729 | -13.50221 | -48.23877 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1625155-aa75-390b-96e4-e348dcfd6a03 | -12.67216 | -48.4534 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README45.md)
