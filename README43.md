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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c6dd653-6c9b-38b9-b4bb-b44793662ac7 | -2.52283 | -44.11896 | 2025-10-08 04:17:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 30dabf0f-95ed-346f-afc0-8aea574cde1f | -12.34801 | -50.29033 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff942946-8788-3cd7-b92d-6fc68ee076a8 | -4.68255 | -45.84759 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56bb6389-0dca-3742-8aec-e42f47d736c4 | -13.261 | -47.15404 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e9d733d-051e-398e-a465-ce901c777b22 | -12.24702 | -47.86166 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2229b0a-ab31-378d-8b6a-067784d0e2fa | -11.84645 | -44.90841 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa8776f3-0a64-38f3-963f-c89006a06c1c | -7.47744 | -43.12791 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 597ebb9f-fca3-3c7b-9865-ba31357e491e | -13.00818 | -46.78754 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 797e051f-ecbc-3219-b9f6-bd016407b8c6 | -13.35298 | -47.55466 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0c8f78b-275b-3654-b515-bafb7245aec1 | -9.13588 | -50.06397 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bba740da-2738-3a69-a706-f51faf3afef8 | -4.00253 | -38.32792 | 2025-10-08 04:17:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e613e031-adac-3569-92b6-2018476fb606 | -12.99155 | -46.78064 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68ca53c1-8444-3ab9-baed-13aa043c3333 | -5.6115 | -45.19673 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c00b4e-1d67-3819-9fd4-fd249c287485 | -12.85658 | -43.81682 | 2025-10-08 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf0a10c9-5a06-3835-94e4-f6dc8c060007 | -5.71505 | -44.66088 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7191cae-ba78-3263-af96-dd7c95e90e16 | -5.60049 | -45.37668 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed18c817-8558-3c71-9d29-d959bf529cc4 | -7.25643 | -44.11205 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| facf2c3b-87b9-3490-9802-7cf342a9b799 | -11.68657 | -50.97161 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9c09160-6f46-3e37-8d51-9484e40c5219 | -7.02725 | -42.8676 | 2025-10-08 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 877ed993-bfe4-3f05-a46f-00b28bf36aab | -11.15831 | -54.86746 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c1958a-247b-3e61-a2e9-a3c2e16c254e | -5.25352 | -46.57661 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ab54dc1-3a87-3b7b-bc0d-d924ec3a3de3 | -11.67846 | -50.96545 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf426199-6539-3078-8d4d-e026e094c755 | -12.2514 | -47.85809 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec36465b-0edd-3f97-b0ca-167111bf4849 | -12.39034 | -51.13782 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c15bdc37-241b-3be1-9414-edb5a17c05ea | -12.3867 | -51.1325 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4141d2b-b5c6-3e11-ada6-685887a4b350 | -7.25977 | -44.11262 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 678e665d-baef-37af-ac52-14e0302c47b0 | -7.77941 | -42.40786 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f04fd6a8-8584-32a2-9388-4680f691fc87 | -4.49734 | -46.35839 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0aaf7fb1-2d38-30ef-b6ca-a7b355e96829 | -4.25773 | -48.54678 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c1cb79-4d1f-3724-83c2-d35a0ad46eed | -3.10805 | -47.79816 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bf6c037-4a04-3d22-89e4-620c6fa6f728 | -5.20698 | -37.62895 | 2025-10-08 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a34da463-5199-3019-b395-5719020a614a | -13.37982 | -47.24321 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 419c45d6-2043-36c0-afe6-f22f2e05d9e4 | -11.18076 | -54.87604 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8141ec14-7f34-3e64-b4f8-9bbee2eead02 | -5.63833 | -38.70826 | 2025-10-08 04:17:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cfcf6216-0daa-3382-b9d5-9c1e00912804 | -7.3573 | -43.86575 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c2e6991-a42f-3dc8-b5c0-6c2225042233 | -2.48108 | -48.36273 | 2025-10-08 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fccacbd-1551-38be-b32e-ccd63607104e | -12.9425 | -46.85165 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee06dd06-bec8-3395-86b5-c6b675d186e7 | -11.13688 | -54.88466 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5cf476e-c6da-35ec-a0f0-b4e9da98b90e | -3.89223 | -41.53529 | 2025-10-08 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 453ad10f-b220-333d-851d-e05d4a9bc89f | -7.01785 | -42.88399 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 7372768c-61d7-353c-8bb0-38595eb58c68 | -11.71595 | -50.94805 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7357de65-1d37-32f5-ae9d-efa5f702baca | -12.64025 | -50.56104 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9557fd8c-2f64-3b8b-9ad4-52823e5eecfb | -3.25966 | -49.12752 | 2025-10-08 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e194f9d-e984-3db8-b6b5-72bf810d8cc1 | -11.15011 | -54.87867 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0e2ccc6-c729-320c-a710-5504e1ede4f4 | -11.98765 | -46.77495 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68abe08c-1d9b-378d-9658-27751ae11822 | -4.29753 | -44.70633 | 2025-10-08 04:17:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a07d7067-5f66-36a1-9abb-50830be38d26 | -4.255 | -48.56307 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafb8a7f-f834-3e1f-b971-3a9fc7831392 | -4.69406 | -45.84529 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d84d2dd9-4eec-3d97-ba0f-1ca115972588 | -2.88194 | -50.7319 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 262bbe72-f4be-3370-a9cd-b1c445eb5b95 | -5.72926 | -43.6136 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70b53d13-58ff-3ee5-80fc-b6edd7f99b1a | -6.01712 | -45.87775 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0183510b-7ce1-33fc-95a3-aa0c67209efa | -4.49808 | -46.35392 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4664c5de-3104-3ec3-8eb2-25554414aaae | -11.18167 | -54.90284 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11866c2b-c251-32f6-9456-59814a004716 | -5.59538 | -44.42875 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae025b2-0141-3c7a-afa2-3acec9567a73 | -5.7755 | -45.74162 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d78a507-af0f-36a5-9056-2618d082f1fd | -5.26204 | -46.47823 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4a8799-444a-3e96-ba14-4ae40b07d7f1 | -4.57456 | -44.98141 | 2025-10-08 04:17:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63b7e3fc-c10d-31a3-8f3b-e0cbd3e808dc | -6.13281 | -44.60331 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9b6aa32-a590-337b-a279-b6fe0be70820 | -4.62366 | -47.41353 | 2025-10-08 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 855f0df0-8d7a-3c38-bbe8-6a9540a9d613 | -4.02215 | -48.96371 | 2025-10-08 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9151901-4b75-31dc-b335-5710e585b78e | -13.36585 | -47.26188 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c3518fd-f506-301d-8d47-83c611ec44bd | -5.77278 | -45.74237 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54e9ff4-2015-3384-a471-36aa431a05a1 | -7.68572 | -42.40456 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7f87f2b4-ec21-376c-b0c4-86541b1b9767 | -11.79316 | -45.04897 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c21f9036-d4c4-3ff2-a404-31d118986c99 | -13.24852 | -47.16394 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0e3adf5-99cb-3cd5-a4b7-584c8f5dfff4 | -11.17586 | -54.90161 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83ef6eea-cd23-3631-b686-6be66f57613b | -9.54565 | -47.77055 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3250540c-bc2b-3cfd-a26c-375cbc9e859f | -12.01708 | -45.19505 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ec55d94-3840-354f-944c-372fb5847534 | -5.13892 | -44.96845 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5a304f6c-a432-372e-89ca-6b7713771a67 | -7.02451 | -42.88505 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2e614103-0f86-39c3-94a6-222d48eae645 | -4.89614 | -41.49672 | 2025-10-08 04:17:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f38f2a58-c4f0-3525-9c21-a4549c8c41d1 | -10.48197 | -49.36495 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f4df608-e8e3-3f7c-9393-4810d2da6fd7 | -3.45138 | -45.59313 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01ef8f6f-4459-3e86-abc7-b8bf3cef4c27 | -3.56726 | -44.46636 | 2025-10-08 04:17:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79943b8e-56aa-3211-b929-4dab0798f771 | -11.49014 | -42.47128 | 2025-10-08 04:17:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71e111d9-f080-3740-8aee-1b16736f01e5 | -3.08629 | -51.24955 | 2025-10-08 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad1f37e-2ce7-35cb-a5c4-fa90df2f27cf | -13.3601 | -47.55581 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6506f8ce-f59e-35c4-8a38-1b7fddc58c7a | -3.455 | -45.59371 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 550ecf3d-00ec-3a11-9563-83bec27a780a | -5.3158 | -43.0851 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bdae7f6-ddd6-3fce-b86c-115e4ecab175 | -6.17301 | -44.68048 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd38e2bd-fd00-3456-93cd-7b7bd67e6188 | -7.79392 | -42.61403 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 57529de0-5d53-3ec3-bc12-3a9dbc75f1a5 | -7.24746 | -44.14669 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4b742fc-3cdc-3119-8c9f-d29efca4a17e | -3.86837 | -42.90979 | 2025-10-08 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0dad9f3-87fb-3797-ab7d-b8014f53af61 | 0.92722 | -51.13947 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dcf20a1-2a8b-3056-a26b-1b81d89c9989 | -11.29723 | -54.89041 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d4946b-d852-3eab-b33f-f231d345aa07 | -13.2827 | -47.1534 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cb4d578-ba29-360d-b168-78eb9fb6df64 | -5.25391 | -44.13637 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 105cf8c8-77b0-33ff-852f-73e236913442 | -11.70043 | -50.99737 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a80f0c-e07f-3dc5-9010-ed8d9c894516 | -11.18329 | -54.89433 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ccc4943-c31a-3f9c-8708-c276dad30882 | -10.4696 | -47.81837 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0caa1d6e-1ee5-3de8-9b0b-c23699da9d2f | -7.15734 | -39.43644 | 2025-10-08 04:17:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d8c84fb-0469-3699-9f22-7152fa5fdbf7 | -7.47356 | -43.13087 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bc2e44a-a936-32c3-b6f1-8347444ddee6 | -7.02228 | -42.87754 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69312db4-c266-3025-b7f8-cc82d161fb7d | -11.74422 | -50.94423 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 67a18cbb-45a8-3b09-933d-c324f7161adf | -7.52457 | -44.08963 | 2025-10-08 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 969747c2-5322-33ca-8987-420438ab23aa | -11.99113 | -46.77555 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6ad96c4-ff02-32bc-aa18-27593e09151a | -11.17493 | -54.89906 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35b85417-3599-3db8-92de-34ffd436733d | -10.85542 | -47.11968 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f278249-c879-3140-bf6b-3ae5516eea74 | -11.50554 | -44.96522 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66f9a39f-1be0-336f-a175-4499cfff6f45 | -3.23646 | -46.79016 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
