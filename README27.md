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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c5787b-99ab-35f1-8e00-4078563fce87 | -4.8276 | -47.31794 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 153625ad-91f2-32e1-8783-d8c41cfd5acc | -6.28703 | -43.8433 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21306c14-1987-320e-b972-3ce0d3e86018 | -5.0589 | -45.4681 | 2025-08-26 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6faeb631-37c9-3234-ba91-7cf08aaab436 | -9.17008 | -40.60515 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85924c0a-bd2c-3fac-85aa-cda1d157d77f | -12.37942 | -46.55369 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7b6883d-fa21-34ee-bc0e-25ee8d723433 | -6.56606 | -44.21841 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 10579b7c-f304-39f4-b473-17a21d202fc0 | -5.06356 | -45.46896 | 2025-08-26 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4bab7a5-4173-3d25-a16b-fc4597dd61cf | -6.80819 | -44.99556 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74133f6e-9c61-3bd9-abdf-4dfb8d640cc7 | -8.90507 | -45.7226 | 2025-08-26 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0563a987-2c08-3923-88bc-74677ac7a91e | -6.29981 | -43.77085 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 915a9070-d5ee-30d1-b8df-6b11c612a192 | -6.80181 | -44.33881 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 621c17d5-6983-32ce-b6e0-38362fef23e4 | -6.56254 | -44.21381 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1ecea20a-2161-328a-9c96-e5351a63e0b8 | -7.59159 | -46.23177 | 2025-08-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14c94e83-a23c-3f94-be29-738d2b660a4e | -6.04288 | -44.22754 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46ada3da-d406-36ba-beb7-1cc0f77f5fc6 | -7.66514 | -42.68155 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8b78c6b-f026-3226-b592-b4e014091fe1 | -7.67034 | -42.67318 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 100bda81-577d-3e27-be9a-1485afe660e5 | -6.03867 | -44.22676 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f49c85d3-87ee-303a-900c-c397a9ade92f | -6.18964 | -44.15482 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a1dc16d9-6924-3468-89f7-cf6908ad3299 | -6.89862 | -44.43492 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5574cb82-5612-38f1-90bb-c1c8f8024dd9 | -7.33001 | -46.09869 | 2025-08-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30d256db-d61e-314e-8d05-982b275ea493 | -11.14711 | -44.75948 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 38f23c0f-ac1d-3112-b3f5-ec31fbe6654e | -8.24708 | -45.09546 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b26a71a-aa28-36c1-ad5a-b69f8f6ab2a2 | -5.79131 | -43.88663 | 2025-08-26 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fa6421e-d027-36a5-8f8b-d502ee5c923a | -11.63062 | -44.86551 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0bdb9f9-dead-3b3e-9e01-8765e1d5f1f3 | -12.09885 | -45.84501 | 2025-08-26 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57bfc0d0-a04c-32e0-a1c2-46ed231d1244 | -8.37544 | -48.02768 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbbe75e-26ed-3319-b966-f314eb0eef4d | -11.30131 | -43.2914 | 2025-08-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b48203-a7cb-3fe4-9ebc-8219344a6a57 | -10.60713 | -44.78051 | 2025-08-26 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a23abced-b9dc-325a-af29-238319781250 | -6.29513 | -43.7738 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 803a6576-a4a9-31b2-b480-878ca317b48a | -7.30415 | -44.52921 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f48b5b-49d0-3458-b353-56013891b8c0 | -11.14926 | -44.77085 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 12f5c6bc-4f2e-3ae1-8c89-599ae616258a | -6.78792 | -44.34415 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd5e131b-298c-3584-b72f-8b6c2b636a1c | -10.50064 | -46.87802 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6485671d-1fde-3360-ad8f-9fc3b00e033f | -11.50619 | -52.13844 | 2025-08-26 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9032ebad-8904-3620-8780-cb0e96bacf57 | -8.1289 | -47.29189 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76e071b5-7596-3eb0-9ef9-2003a7df60bf | -8.073 | -49.67004 | 2025-08-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de6a1cf-fb74-33d5-b879-6298508cdc34 | -7.57818 | -47.49229 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44028ca5-2358-3e88-a2ab-048549d17d55 | -8.9029 | -45.72513 | 2025-08-26 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1fa00de-ed6a-3390-921c-b19142c1900a | -12.41705 | -46.81403 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 04ef103e-4143-3c8c-a6ff-130f7e1ea898 | -9.16786 | -40.59739 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2228d067-6ab4-3712-a3e0-aec1f216124b | -8.30831 | -47.23959 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 156650cd-d5df-3c90-bc35-9912b2c72730 | -10.75665 | -47.07508 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 244ce5c0-7c67-3555-9e55-09f9303e3722 | -6.80451 | -44.9906 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0e8af51-2259-31c4-a3d5-fcc5bf3c7a97 | -8.37601 | -48.02446 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3282f94-7d98-3b57-b6de-1301a9a6f2e7 | -11.15447 | -44.69446 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d89e03-94fa-305b-a829-c79af55afb4c | -7.24561 | -43.66397 | 2025-08-26 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66a1f594-1207-3422-afe6-7ccb6bc5b829 | -11.20932 | -41.596 | 2025-08-26 03:55:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5dcd42f8-061e-346e-9988-f2f406a3cee0 | -5.81235 | -42.30257 | 2025-08-26 03:55:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 559db19d-b92c-3cd3-979f-89cb15063c1c | -8.07379 | -49.66586 | 2025-08-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a00ebd49-3f74-3e24-b170-a21417586bb7 | -12.41396 | -46.48972 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89e1e84b-2965-38e1-a9ef-c344b7f54d60 | -8.31327 | -47.24067 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b13f90f4-319a-3fa4-a657-f712ae6935c4 | -11.03083 | -49.14465 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 541ca9b5-d60b-34ef-bf43-6705f0652df1 | -11.15351 | -44.79394 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34fa226e-d65c-3b3e-b85a-ba259d196250 | -9.32436 | -40.21438 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 55e8e39b-41bc-3b82-a4ac-707baf7eb655 | -9.57758 | -48.63542 | 2025-08-26 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 685a93bd-7435-30a2-80f1-5d07aecff334 | -6.80892 | -44.99128 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a08df59e-2323-3e1b-aaa2-6274d68a944f | -8.16493 | -45.05602 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93956afd-94ba-300e-ab02-263bcf7e6544 | -11.62897 | -46.39042 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5f27887-9635-3a8d-829a-6c33a87aff50 | -6.90338 | -44.40672 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 046e8a6c-1ea8-3c5f-b6d8-c706a39f2ad9 | -6.52407 | -44.43808 | 2025-08-26 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 238f7eea-50dd-33d2-930b-1a9a14e785b8 | -10.38367 | -43.46934 | 2025-08-26 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 144380d0-687f-32de-b98e-e2a1a2d6409e | -8.24779 | -45.09125 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41ea1e78-52f6-303c-b2a8-47229ec0f862 | -11.06307 | -44.59468 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fca5ff34-9516-35b4-a04c-ae88eb65bd78 | -10.78293 | -46.38478 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b0e872d-d167-3098-8d95-c3001fe88764 | -7.46563 | -45.01239 | 2025-08-26 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fde7e7e7-9813-3146-9e1d-1c8cd73de3e9 | -7.21853 | -44.41885 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4e477b6-63e1-3b21-80d0-3f9c3d3e544c | -6.28765 | -43.83963 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1afb88d6-3076-3678-ba6e-2e5a4b5b1495 | -7.74982 | -43.92278 | 2025-08-26 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 887a809f-4417-3259-99ab-c4658d5aff7f | -11.1533 | -44.77155 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0f982956-a518-32d1-b47c-c58079ee1b66 | -7.57105 | -47.47261 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b099d6d8-271b-3063-b9a8-69ca551e8667 | -8.30839 | -47.2407 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7dad7c0-78d5-3c39-ab07-6e5d2bc93f85 | -6.19877 | -44.15181 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36170f33-cd20-3f75-868f-bb2783da4e8e | -11.15982 | -44.75809 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9156dd4e-2108-3153-9776-caa700c9a5cb | -12.41231 | -46.4988 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b549a3a-eb56-3649-9a31-0d668de3b046 | -6.19388 | -44.15525 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3993f732-a2f2-3908-b660-5a159bd3389a | -11.14818 | -44.80053 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| babe1f16-1521-38c3-bd04-14e63bd79f8c | -7.85152 | -46.74092 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be45dba3-8419-3d0c-9442-94064eef6924 | -11.62916 | -46.41452 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ec8dbe8-7236-3b7c-963c-cb68c245bcdc | -11.15857 | -44.7652 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 62a08b2a-a8d7-3d5e-a2a6-b6b51d35e4b8 | -6.69957 | -48.38144 | 2025-08-26 03:55:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 00dafeda-efbf-38ff-b998-d408816bbe6f | -10.76329 | -47.06553 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfb5744b-92b0-3039-aba1-622bbc65a3cf | -11.92323 | -46.74469 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04c7a94e-56c9-3a84-9d23-dc203fe433b4 | -8.32648 | -50.5711 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 36e1c539-0adb-3551-acdf-23e02b9912ce | -7.09646 | -44.62766 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9979f076-845c-3f9f-8fa1-3157eabd426c | -8.70729 | -47.86586 | 2025-08-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c851f766-a5d4-30ae-868b-f96c58e2e694 | -11.64271 | -44.86762 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d8695c-9853-330d-8edc-d82959aea1f9 | -5.87184 | -42.41358 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3460b2b7-d3b7-3e14-9e2f-5e2077e2d87a | -9.74654 | -37.91659 | 2025-08-26 03:55:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc938f1b-d83f-3981-8bb8-eb58c4df2d75 | -11.64702 | -46.1926 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0fbfa79-98b5-385e-ab58-5dabe4c05cb0 | -11.52893 | -50.45105 | 2025-08-26 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e95a2569-0561-3646-a9ae-2ead5332b073 | -10.75762 | -47.06982 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 98d073a6-2e81-338e-a6e8-4f57e3233952 | -7.53488 | -44.92905 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28d900e-0557-345b-9f3e-bd8e9e9b3c27 | -11.15011 | -44.78958 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b040a01-042c-388d-96b6-0970ebd37b86 | -9.4013 | -48.24685 | 2025-08-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08db0f14-acfa-3f73-9e71-943472fae567 | -11.15286 | -44.7976 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b0d4fc4-6772-3355-ba6d-a6e96f524708 | -9.16728 | -40.601 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d2b33660-5665-3089-bdf8-3b33fc272b2f | -12.41792 | -46.80936 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| dd26054e-844a-3e19-a9c4-5eb1afae8b72 | -7.89606 | -41.90696 | 2025-08-26 03:55:00 | NOAA-21 | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c40792d-7764-337c-afd6-d3c5a4a692c2 | -6.98774 | -44.13326 | 2025-08-26 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3adc2fc3-4bb4-3ecf-b5a4-f8d922ebccea | -6.32169 | -37.75933 | 2025-08-26 03:55:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
