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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7765ecc-4129-3d41-a42a-3355669e3ce2 | -11.43702 | -45.13278 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c3fc8377-5227-3bc9-a35b-c9e6047381df | -12.73059 | -46.39607 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcfe7b3b-1297-3f61-9466-3ff24644bf09 | -11.72834 | -47.52249 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c99469f2-8e0f-3f56-8f42-588562e4080e | -11.02854 | -45.06725 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6661a436-21b7-3f96-8d7e-e5edf8af3215 | -8.52421 | -47.4433 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3be6bc54-981c-331e-af7d-f554e91edf0d | -8.51399 | -44.74967 | 2025-08-06 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1141482f-ab63-380a-906e-0b8af025fb39 | -15.1219 | -47.42997 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a2e5ca6-2ac9-3905-a121-9ca56c23713c | -11.90244 | -44.97061 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adff131c-5d56-3c22-8e7b-64c698accc8d | -8.23823 | -45.06422 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e67eb3ec-7579-32e6-8b8f-4562689ae284 | -11.73227 | -47.52869 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 74bdb83f-e5de-3065-9cbb-1020a665b5d0 | -10.43138 | -44.37674 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9cab706-123c-3d76-960c-8bf3204242d1 | -11.76612 | -44.96178 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9941927-c37c-3849-835b-657e8eb1a9e1 | -12.04231 | -44.01732 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49e74343-471a-3fd1-a57f-6e87cfc15982 | -8.53879 | -47.48447 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6920e70b-1b22-3143-a5c8-3c0304cce2a2 | -11.83991 | -43.72693 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 13f1c084-2053-3d47-8f55-1fd0ac3608e6 | -10.48215 | -44.37381 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feac5ae5-9198-3566-a643-1d7338d76d7d | -10.44429 | -44.37479 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdb54e3f-ee43-34fe-993b-a3ec2214678d | -10.45936 | -44.33603 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e05b60b2-172a-3974-8b77-464eefe711a6 | -11.43651 | -45.13689 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e89f90f3-a22e-3471-8c63-6e93ca685332 | -9.54923 | -40.32615 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ce15452-8c3e-3c28-b89f-da455eb17e5f | -11.78769 | -45.00947 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95e856c7-6759-3fdc-a193-dfe14ddf60a0 | -9.07686 | -45.05672 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3ec71ce-c363-30af-9440-d9e7dc6daa30 | -14.78862 | -42.4377 | 2025-08-06 03:57:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e54067f-58da-31f0-a9ab-363ebd3e15c7 | -12.99785 | -44.8966 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19b6ffde-3ded-331b-b8ee-1e0ff2718883 | -8.8501 | -47.46573 | 2025-08-06 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 904a95fc-55d4-3393-bf75-9cb53b7ffac0 | -8.51663 | -43.31549 | 2025-08-06 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 859d64a9-5436-3698-940e-0eba23d39dbd | -9.64848 | -43.84764 | 2025-08-06 03:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29b093ed-1a8c-3cd7-8442-b2363b201be0 | -8.83717 | -47.62162 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f283e82-727f-3d44-8653-4526448f8926 | -10.47091 | -44.34175 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c051e107-e878-3e11-a923-8664a705b19f | -12.07697 | -45.80433 | 2025-08-06 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78177111-8a68-371d-8afd-1a4bc038391d | -12.03758 | -44.02154 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6163f36-c8e1-3ecc-92de-3fa82cd9f4d7 | -12.29209 | -42.65481 | 2025-08-06 03:57:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71c7ac2e-4a61-3081-8d4a-920a59571eaf | -11.78908 | -45.00854 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b8f70a-f7a2-3c29-a85e-26a1ebb11f73 | -8.84953 | -47.46882 | 2025-08-06 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a1e857d-bfc7-314f-b1ee-96dceec6d823 | -11.64715 | -50.15491 | 2025-08-06 03:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad732a5c-3d36-35dc-9dda-8103dabf63a5 | -13.2967 | -43.85278 | 2025-08-06 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae1266a8-28cd-31ee-825a-8ed538202d7c | -12.65541 | -48.11782 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bb17a5b-4765-39b8-b6f2-ad0d4173a01c | -12.71955 | -48.08056 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a153d19-e528-3720-9662-70bdedba9895 | -11.43141 | -45.14013 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c35c5dd0-d251-3783-a6ca-faf87ef21601 | -11.43723 | -45.13294 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c285950b-abf6-31f0-807b-6b3679032f9b | -8.53013 | -47.46999 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85696ab1-0602-3894-8f02-a426691869ee | -11.74764 | -44.99411 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76ee6cd3-0b1e-3e18-b10f-159fea343504 | -11.73327 | -47.52329 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02612669-58d9-3e1e-8959-8352f9cd2431 | -9.07255 | -45.05977 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3727a3ce-f4a9-3987-baea-4f126b798f4f | -10.43676 | -44.36989 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 192c3dd1-eb94-3f92-ad9b-457fae5c47d7 | -9.50798 | -46.73023 | 2025-08-06 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b99508c0-9782-36a9-a4d2-a00b8d5ad6dd | -15.12078 | -47.43208 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b40763f-fce4-31ed-aba8-be37b86b03db | -8.98736 | -45.69102 | 2025-08-06 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a9e2aad-c053-3b5a-9bd3-8b989d811645 | -11.72338 | -47.52191 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99e9875-80c7-381f-86af-0032298a2016 | -11.43579 | -45.1409 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 18483e17-a3e2-32d8-a57d-dd094ad5abe4 | -9.07834 | -45.05241 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ba1ebc7-dcce-37b3-88e7-9a50bd1cb29f | -9.70241 | -48.87241 | 2025-08-06 03:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 541bf624-ff98-35ef-88cf-b60c14805466 | -9.07251 | -45.05595 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eaa6d5d0-b653-3d3e-b4b9-787234528c87 | -11.90174 | -44.9747 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4001ccfe-b6ee-30b7-babb-f3f1ed899638 | -9.4652 | -46.30754 | 2025-08-06 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb74e3a5-a550-3647-a4f8-bb781f84445e | -11.43505 | -45.14495 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 166b6364-72d9-394d-a0c8-e803ac8fe678 | -12.67052 | -44.91103 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5683632b-36f4-3720-b709-c6057163193e | -10.4781 | -44.37297 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02bd522e-0014-3a07-9001-0714cc8f3931 | -11.83609 | -43.72625 | 2025-08-06 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cde16f30-2ea8-308b-989b-783c6fa5d280 | -11.90463 | -44.97022 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8131008b-3296-3884-b0ee-8461a9d54f3a | -11.44054 | -45.13749 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| def8580e-7d23-3454-a885-8b4c674f33d3 | -12.02354 | -44.82474 | 2025-08-06 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a84aac9-9b49-3c45-b036-65027ebac1c0 | -8.98652 | -45.69571 | 2025-08-06 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0a5bc8b-5b3b-36d1-abdb-349273d14981 | -9.6213 | -40.59223 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7620268b-0f4d-37d0-a9c5-0898ddbcd0b0 | -11.762 | -44.96095 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b2050d1-0650-39ca-9acb-77199ccf6f24 | -9.69688 | -48.87126 | 2025-08-06 03:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ece8d80-bf47-343f-83fb-e70d75fb47f9 | -8.51357 | -43.30985 | 2025-08-06 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cc939625-edbb-3f6a-8312-f02b9139dd6b | -10.1217 | -51.67577 | 2025-08-06 03:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff15fc61-909f-3d61-95e0-ff6637857091 | -11.8969 | -44.97805 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9c86ba9-e209-3188-9ae6-c2dfc7bb062b | -8.53825 | -47.48438 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db775fd0-1c21-3bd3-88d9-003fcfd9e3c2 | -15.12171 | -47.42728 | 2025-08-06 03:57:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c8c3a583-278d-3f50-835f-67f8b6ab94b0 | -12.66156 | -48.11283 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4fe8b72-221b-3b1a-81e8-8e610f95fa82 | -11.4279 | -45.13538 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc765b7f-4b82-382e-bd5d-bafb78567e34 | -11.32641 | -47.305 | 2025-08-06 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23f48a0-da4d-3db3-b94b-b5cea6b1772d | -11.76262 | -47.53585 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ffe6ecd-2b8d-361a-bb07-1955153a0864 | -11.44 | -45.14159 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a3c6b138-7218-3b63-8f23-50bca40a40d8 | -11.43564 | -45.14076 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d16ec846-0454-3fad-9b98-8b21aa836aaf | -8.84295 | -47.61935 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3f22b1b-53cd-30d2-b5a4-7f0b9153651a | -11.76549 | -44.96536 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 843f80a3-bd5b-36c7-a173-beff9c0b52bc | -12.55024 | -44.73985 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836cb794-64a8-32ae-8012-767e24bbfe30 | -10.48248 | -44.34737 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b73c2f4-c406-342a-9d48-4d7eeed244b2 | -12.71452 | -48.07977 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dafd045a-370a-3a65-8230-6ce1d1ea574b | -9.07319 | -45.05198 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4df8398-c712-38fc-aeb5-99b7437ed15b | -11.43351 | -45.12807 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8a0bef9-67ea-36b7-a0ec-f1acf7f37a38 | -8.25512 | -45.07166 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4eafe0c-7ca0-325a-a6a7-e826f1c67139 | -9.07755 | -45.05268 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05213e27-1c4d-3ea2-b466-90d061c5ffc8 | -10.48309 | -44.34378 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3587002-da2a-3e45-ab60-e77a1d3d7997 | -11.49476 | -50.2889 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6098af7-80fb-31de-8aee-b346019936cd | -12.99701 | -44.89948 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a413b8d0-ea37-3ce4-9734-107e5c14271b | -11.73886 | -47.54803 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5234e4b0-e313-32e8-aaf5-23869ece4897 | -13.76361 | -42.57876 | 2025-08-06 03:57:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 103ccf32-902c-3ceb-bde6-25a6fc3e4956 | -12.9741 | -44.88766 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b82fd5dd-7111-3785-a9fd-12caca3cd8ac | -11.90808 | -44.95115 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13b878c4-6b9a-3687-8679-0bb7bae5f0d4 | -11.76898 | -44.96979 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55a7caaa-915e-3ad6-a497-87fa31d45763 | -11.74424 | -45.0134 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be85e813-81aa-3e1c-a4c9-fcd9ba325ed7 | -9.6287 | -40.58967 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47a1c300-bc35-3e5e-8953-cc12730821a3 | -9.51279 | -46.73125 | 2025-08-06 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8c2657c-dfc5-39e4-a18e-2a4cd620a7d1 | -11.43493 | -45.14482 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6122577d-98d6-3077-a857-9d70fc4a19ac | -9.07763 | -45.05642 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 992cc9e7-00aa-35dc-9505-ceccd2e03dae | -10.47904 | -44.34308 | 2025-08-06 03:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
