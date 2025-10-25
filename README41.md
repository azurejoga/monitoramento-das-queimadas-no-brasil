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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cb103b0-b884-3c69-b250-9f8192b7e8cf | -9.32186 | -46.96782 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 20d5bd5c-ea7b-35e7-af70-c04888fa5df1 | -6.90194 | -45.17141 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 044e1ad3-e7b4-3f77-a4d0-34b463f4c33a | -12.2242 | -43.31144 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776042b9-028b-32f6-8e78-e0c652d48f23 | -12.11998 | -46.71672 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89b8befe-c49c-329d-a291-1f437278bdef | -6.79294 | -46.46434 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ed88e07-90f2-39a5-8113-31ae242c8fe0 | -7.15966 | -46.08655 | 2025-10-25 04:19:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bed053c-935c-397c-9cf6-313e5790bfb5 | -6.71169 | -44.63338 | 2025-10-25 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee167271-3509-3b40-b0d6-20c5d1bba003 | -12.71634 | -46.91737 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d95564f3-d8c6-3822-8e92-9a27f92ded7a | -10.63912 | -45.23553 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d947128-af32-322f-8d3c-10b387fe6d69 | -7.69384 | -42.24049 | 2025-10-25 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68298453-5482-34ac-8e94-955704e53234 | -10.62488 | -42.3117 | 2025-10-25 04:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3051ac94-ea6a-3e1d-a988-44cc25720160 | -6.79574 | -51.10985 | 2025-10-25 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efcf164a-30da-33ec-8c3b-5679c8426374 | -12.83628 | -47.24427 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d00fbe-3f72-35a5-b84d-cb3587ca04c7 | -10.71558 | -44.74724 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca043a0a-ad8a-3511-ad21-16f87d37e141 | -7.84848 | -40.90403 | 2025-10-25 04:19:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 501f822e-dfb8-3ec9-a26d-460252b3ab79 | -7.79336 | -45.39937 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b481e11e-562f-3c5a-b641-91ed48d86752 | -13.545 | -47.5674 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4b6ee40-4135-32b8-9a62-f1fed8478981 | -10.56376 | -47.99507 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f17aac-7554-3210-ba3c-ca1c77d11501 | -6.10783 | -48.10958 | 2025-10-25 04:19:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec9f152d-3efa-3740-96f5-4f646a2d50dd | -10.73563 | -45.13969 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23bbba0d-0539-3f96-b69a-4f9b62d2d650 | -13.62749 | -47.61211 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de190b5-6a84-3ef3-bc6e-a247e463c15e | -6.96847 | -43.495 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7a5c22a-0ce7-3c46-8afd-9927f879e741 | -8.55106 | -50.04205 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b42082-e973-3efa-9472-82ad244e4e8a | -10.92477 | -50.11216 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34de93fe-012c-3868-95a5-bef8fb89aca3 | -6.23922 | -46.39635 | 2025-10-25 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd5616a2-6e7b-308a-bea5-da0c79e23996 | -10.74872 | -47.9012 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0a893da-da33-3afd-9260-76d56b277233 | -10.41719 | -44.50419 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68c0dd5a-64e4-3d05-8616-96bcc1f5a05f | -12.11779 | -46.70905 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dc71090-0412-36ed-94ec-cf79a1860d24 | -9.44344 | -56.6458 | 2025-10-25 04:19:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1d2b719-4eae-30b3-8689-718c26482f30 | -7.45872 | -41.91027 | 2025-10-25 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fee68587-c0a2-35f0-a653-0aa76ae01e11 | -11.36095 | -54.32546 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5403a69-4939-37a1-b964-63384e3fe70b | -8.15702 | -47.76881 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9287f31d-c55e-32a2-ae56-d942754659fc | -13.41305 | -47.9612 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e96d1ed-7506-3d2c-b2f2-f886a5c0d2aa | -12.21865 | -46.50271 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44a4575c-60cf-3ad3-b602-21d0dc331637 | -11.05521 | -48.33176 | 2025-10-25 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be01891c-a743-3f40-9f3d-cea72806cadd | -1.29799 | -49.34956 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0719e7-59cd-376d-8488-ede789d45179 | -9.15215 | -45.82948 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 877ec9b7-ffaf-346f-aa76-7d2bd96b9bf2 | -11.98552 | -43.3138 | 2025-10-25 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec47a0b-4da6-3849-9434-d62c9aef4867 | -11.54407 | -48.81477 | 2025-10-25 04:19:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2c29faa-8a8d-31fb-97ee-8eb5a15d12fd | -7.22988 | -46.03553 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a23d55d2-6587-3a5e-827f-7f9f6f311b47 | -11.57011 | -51.47143 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf86791-162b-3a23-a0c3-eb37b5fb04b9 | -7.27503 | -50.00747 | 2025-10-25 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402f7e69-45fb-3511-a913-60a716e177ba | -6.95787 | -43.49698 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9a85b5-4e31-316a-89b1-3c43656cc2c4 | -10.64243 | -45.23607 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 414181cc-3fc2-3859-9b97-bdf90c51f980 | -8.54647 | -50.04488 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 806f74e8-c383-3d49-a9f0-a1e5007738b3 | -6.28889 | -47.06594 | 2025-10-25 04:19:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cbd718b-c0b5-33ef-8807-8fe6ef0532b0 | -13.06713 | -43.84293 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41c319a0-01ae-3be2-90b4-a4c1742aabd4 | -12.30606 | -45.52146 | 2025-10-25 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f921d0b-b426-33a0-a98a-3460476f3652 | -12.12444 | -46.71016 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 43b3a293-38e1-3398-aa3b-540e59b53c13 | -14.15448 | -44.31495 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e14b380a-9314-3c6c-b425-331a576e5fb8 | -6.59405 | -44.3251 | 2025-10-25 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f11356cb-995f-3435-9fb4-deb99292002e | -10.9305 | -50.40652 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9efd1a15-dcd2-3ad1-a2f9-52e52859b657 | -6.55175 | -46.63206 | 2025-10-25 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33a50273-8292-3f7b-9898-945051a779cd | -10.39908 | -45.31492 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea7f564-872c-32ec-871d-8ad8ff074a8f | -12.83677 | -48.63476 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 30845fe2-49e6-3889-b166-ea0bf07d5d04 | -5.81405 | -50.19732 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a7414f-d843-30a7-bef2-77c0bb0bf19c | -6.78749 | -45.42071 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2b135f4-12cc-3bb3-8299-a68da7210ca2 | -12.80809 | -48.67617 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfedf6d9-1445-37fe-9fb4-aa0575316194 | -1.33191 | -49.11515 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eff8d074-d746-3567-bf4d-e99974c8aeb4 | -13.33002 | -47.93132 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83485499-a27b-37bd-8ee4-b36292bd6b38 | -10.35316 | -49.00121 | 2025-10-25 04:19:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69843e07-7630-3e8e-9254-8f30d9741a18 | -9.87134 | -44.89027 | 2025-10-25 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2752086a-abcd-3af9-981d-40b9deb4c1e8 | -7.47997 | -46.87932 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31e1b05b-810a-36ca-bfab-751bb31d4407 | -6.80546 | -42.39683 | 2025-10-25 04:19:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 89209e20-d5c9-34f6-bb55-b6f17511f134 | -12.07545 | -46.39966 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e47d2e3-1306-37d9-b8b2-21556643310c | -10.41446 | -44.73903 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de89136-71d0-3da7-9345-d009b87a2cd2 | -13.63086 | -47.6126 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5ee1495-3c91-3aa1-a53f-c7626758b65c | -12.2992 | -47.45477 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afd04fe-1f74-366a-9f2c-7b6565ca3d95 | -12.1272 | -46.71427 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c2e9394c-d8e1-34e2-ac76-2fc2cc825bb7 | -1.2993 | -49.3415 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b47583fe-d7c9-3b17-aac7-1748cc95d028 | -6.96346 | -43.50512 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13b4982e-32eb-368d-b9f5-d318dc418bca | -9.99733 | -47.0852 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc0d1a6-f59b-3f0e-a60e-92f65f7d234e | -2.89582 | -41.78887 | 2025-10-25 04:19:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d424dfcf-4fa7-3d68-9ced-6ff27e84cf39 | -12.94941 | -48.50587 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c22cdfd-fa4f-3ca1-bcb6-0ef9d27748c6 | -6.99016 | -42.78935 | 2025-10-25 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab67a65c-37cb-3ba9-847d-3066951e9814 | -11.99777 | -47.15405 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fdf2b8b-3db7-30f2-bcf8-40162fcfaf2a | -12.91224 | -47.74 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88c647d6-25af-3cb2-8dce-b112c47dd9bd | -13.28573 | -47.49496 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 908d621a-c3b1-3b64-b9d6-0dff4e4f4802 | -13.04416 | -47.20495 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5804bebf-74f6-3cd9-86ba-57c432597629 | -7.69032 | -42.23999 | 2025-10-25 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a9025c2-ecbe-30a5-a434-e772338eef14 | -9.59212 | -46.87909 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08346384-58bf-3338-8076-d567491dab9b | -7.7758 | -42.91857 | 2025-10-25 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b412b95d-b71a-33eb-a538-8e7d91294975 | -8.20984 | -46.9219 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b129ba96-0b64-3acd-a8fd-85c3167c7a6a | -10.61895 | -48.0743 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0394a73b-54ba-3874-880e-d88fbe7d97a3 | -12.08201 | -46.42252 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84d2e311-5992-386e-b5a9-f85a095861f2 | -9.19518 | -46.34388 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84b53c31-7b52-3785-9702-49bc37453aea | -13.321 | -47.96498 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2f340b2-7013-3827-8059-b6370d2ea74b | -9.62016 | -46.9062 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83cc470e-76e9-36d4-a551-93e13b5857fa | -9.17602 | -46.37744 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1503eda6-d5f0-397d-a51d-7c65b592099e | -9.17892 | -45.70454 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8ebb3d7-a9da-32af-a878-5228f761ca8f | -12.77945 | -47.56919 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a41e986f-657a-38b5-9fe9-d6dc3f2b42db | -12.05776 | -46.40397 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6369a61-30fc-3ce7-8bd1-4e52926e8e43 | -12.25988 | -47.44071 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55716c08-11ea-31d6-9a03-6506450877e7 | -9.25187 | -45.58743 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f4a81d9-1963-3a49-9ef0-736cd5921d58 | -10.14031 | -52.13569 | 2025-10-25 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72611b51-f2a4-3980-ac99-c179d4626074 | -13.01725 | -47.22272 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ebef2c7-d7c9-33e1-9f90-ad34361a11c6 | -12.68365 | -47.91348 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17a4bab3-e5c9-36e2-97a9-8834512be709 | -9.99858 | -47.59428 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaeeb3ee-d40f-30e5-b67c-a930265df797 | -11.84931 | -49.85671 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c08d6472-7cdf-3666-9460-78dc47dc2d9b | -13.39948 | -47.95867 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README42.md)
