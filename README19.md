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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15f2b4a8-03e8-3c34-a052-5b7dcfc1a961 | -9.07563 | -40.47705 | 2025-08-09 04:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5f39427-2708-3757-a1ce-47121eb3c21e | -4.81591 | -47.3199 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc89b4c6-bbe6-30cf-ac06-e95b704c7237 | -4.81931 | -47.32045 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa540884-82d9-3460-b145-1ca6b61c7872 | -4.47713 | -48.10772 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e999afb-e847-37da-a962-eb5dd4321c6e | -7.30048 | -44.66611 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48446b03-c317-3411-993f-8a8b717b17ff | -5.63 | -57.32949 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46db28b6-51db-3eef-809a-1a8927d13cb9 | -5.82419 | -46.35667 | 2025-08-09 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e98db66c-1e97-314b-8af4-53d676d023ab | -3.81947 | -41.57135 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fa1253d8-84f9-31ba-87d7-d2ca143fab8a | -6.68506 | -43.35308 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f2e18e74-9f93-33bb-a882-24c7ecc64f14 | -7.42294 | -43.97424 | 2025-08-09 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b6483b6-560d-3113-8a15-cd2a2ab25e3d | -6.48414 | -44.41631 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b975fca-58ea-30fc-b467-2ebde2019cf8 | -7.57492 | -44.40464 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3afd829d-19f9-34f2-882a-8d728a7b13f1 | -4.30305 | -48.07684 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31d6761-7dde-3720-a46c-812a66fe79fe | -5.88609 | -57.74887 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5a685b9e-919a-3515-b624-80ba8e13f854 | -5.21863 | -46.07553 | 2025-08-09 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b360f9-6bc8-3e9b-8670-3ef45e6c4789 | -6.60276 | -43.37165 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd901f27-2852-3087-a22b-926a9d061c8f | -6.6005 | -43.38734 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4eed384-498c-335d-9837-80ef9d85d821 | -7.30164 | -44.65818 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8acfddc9-6906-34a9-aed3-bc7603007bc6 | -5.46599 | -43.96515 | 2025-08-09 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1c7cccc-7120-3697-8db2-1094f551609e | -6.60218 | -43.37565 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36f573b7-9b4f-3491-9508-b2e7b422d072 | -6.12203 | -42.95124 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b4812799-bef3-38ad-9151-e43e391fa065 | -6.48814 | -44.41705 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50551690-07d8-3a88-90a4-1ec66ed8d596 | -5.90574 | -57.71055 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1e4b914b-dff9-3c4b-8edf-a39a0cd2d55a | -6.19976 | -55.62041 | 2025-08-09 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58a6b60d-c195-36bf-9ff1-095829345133 | -3.84359 | -47.75034 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1edb8bd5-5573-3b8a-9652-0ef3f2e9e793 | -6.05754 | -43.75137 | 2025-08-09 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ae53283-9935-3992-9a3c-14d81b707d38 | -4.02777 | -48.05922 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039ef61f-0e27-388c-8d78-6e93b62a905e | -4.87292 | -47.76024 | 2025-08-09 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b8cabad-9b3f-3e4c-a919-a4ffe6fd8556 | -6.13406 | -42.96168 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 2c46c676-525e-3485-832f-c75ab8eb309d | -6.05866 | -43.74383 | 2025-08-09 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 345fcfa7-d8bb-3474-a6ac-736fa5b9f67f | -6.20491 | -55.61681 | 2025-08-09 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73bc2195-0e5c-3643-bc9f-9bdd1e870a09 | -4.29523 | -48.06128 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f408d95-bcd1-35b1-8035-69158befc759 | -7.21237 | -41.84684 | 2025-08-09 04:40:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 39bd13db-9e33-3501-aeb5-4b4de41e1c9b | -13.63655 | -49.02072 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 790e293d-a4c1-3640-8f9e-52ffc259fe1f | -11.07673 | -50.46305 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40179dfa-87a1-3467-83d5-bafed673b98f | -7.25326 | -59.99321 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9310e793-4c47-3eae-bb59-181f8af813b3 | -12.48875 | -47.50572 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81224eb4-6487-3d4c-b84b-27aa63cd062a | -13.06568 | -43.83442 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d11ef5b9-eac6-38aa-beaf-e425409f5f87 | -7.08059 | -59.17107 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| efd6d53f-6fdd-3eef-b153-8c5e60131565 | -11.92147 | -44.85512 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37ab8bd3-ffb7-3f08-8698-d22eda418d96 | -13.61109 | -48.98571 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c86c088-f309-3c94-a693-a4b7949baaea | -11.26738 | -50.19806 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d3c5c43-a362-3803-b6af-a7102adc6b7b | -13.06506 | -43.83924 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab91892e-955e-3a19-86dc-7847c41d1c9b | -12.49176 | -47.51054 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eac23ca-6438-30c6-a48c-3e56723e9a78 | -12.71107 | -46.37581 | 2025-08-09 04:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b6b1aea-de24-32c7-84e8-976007f0b84a | -10.44679 | -44.342 | 2025-08-09 04:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6963b3cb-f4b3-3a87-917b-97f8d554dce4 | -7.06823 | -59.17644 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f78de62f-167e-308a-9ae5-f04c006e47c2 | -9.52084 | -45.40551 | 2025-08-09 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85baf46c-058e-3fc3-b942-054e36f79afb | -9.86477 | -44.69612 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c97f2255-ce89-3812-8570-41abe5ec2326 | -9.92706 | -48.33804 | 2025-08-09 04:42:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d91b3e6-4857-353e-af9d-879b568717cf | -7.07863 | -59.18193 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| c69bc6db-e0a7-3882-8c40-7e1e8d25e809 | -13.05298 | -56.84851 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7928dba8-4997-36ec-b31c-d6b2e68185fa | -7.08282 | -59.19029 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a697319f-88d7-3b8b-9612-789d8be2a449 | -8.86478 | -47.27505 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87e58f39-b3aa-3b4e-b9bb-c4dc0855f6ce | -11.73215 | -45.01349 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d818370-202b-3485-80c1-c2e357d2110a | -9.65669 | -43.85095 | 2025-08-09 04:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 11133d00-80fa-371d-8913-3422bbbed276 | -11.74003 | -44.95545 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f20f8f8-07c2-3b44-b2c9-34a730d81e1b | -7.07181 | -59.18814 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| eddc20a0-f3fe-379f-9f59-866bba9a82b0 | -13.62393 | -49.01081 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b82c44b8-beb6-3466-abbc-54d5ddc59b0a | -9.64397 | -48.34043 | 2025-08-09 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44b501e8-3abd-3854-8563-bbce5010c24a | -7.25252 | -59.99729 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 272748bb-0ffa-343d-ace6-b11d8cfd390e | -7.08216 | -59.19397 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cb436fc1-f7da-3074-8e8f-6997f30d5787 | -12.03363 | -47.51707 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90822b09-7a07-3484-8e42-3694169d39c1 | -13.64 | -49.02117 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fe96068-1b9f-3bfb-8d4b-42732a6f14b1 | -7.06333 | -59.17201 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7ade76aa-c0ee-3a49-93bb-6fd8fadd038f | -12.04992 | -47.5066 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0128612-1068-3ea8-9d84-55d4e748499b | -12.03063 | -47.51231 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a35e7e1b-80c6-34ab-a113-e52673235d96 | -9.51406 | -45.425 | 2025-08-09 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3342d917-e557-3043-a275-92c0fdf1831c | -8.87819 | -47.47039 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d555331f-a23e-35ba-b7e5-d6d75b17c41f | -7.08348 | -59.18663 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7b7df445-dd08-39de-9bfd-339d7dd0a43c | -12.71175 | -46.37091 | 2025-08-09 04:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f81fff97-0f35-3526-a52c-fd8fb68356b6 | -8.87349 | -47.47763 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f469bcc7-6d03-35dc-820b-a2dc68c6d655 | -13.63384 | -49.84614 | 2025-08-09 04:42:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccbb6e24-aed8-346e-b42e-a151c00ce47a | -9.20357 | -44.53495 | 2025-08-09 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0191005-fbea-33b8-b85a-493451f75c5b | -8.73071 | -49.74284 | 2025-08-09 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3f21a36-edbf-363b-94de-80a855f66dac | -8.98202 | -45.68736 | 2025-08-09 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 807973b0-9b3e-31c2-a3b4-d4f7480821dc | -7.05814 | -59.20055 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 86f1b7d9-76a2-3b0d-8f51-e299b28b0800 | -7.076 | -59.1965 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1800ad49-9cd3-3c2f-97bd-b189b9444051 | -12.56536 | -47.10774 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62ab7129-e705-3194-9dc3-bd562f3fa7c8 | -11.93812 | -44.54401 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1fe84021-8448-3634-8d06-5ce914ca95c9 | -7.06232 | -59.20897 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bfa9515d-52ba-3c15-9152-ab26bc93263f | -12.41118 | -47.78593 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a13b6a8c-2cb9-399d-9d49-9d5735a89ab8 | -11.74993 | -44.94543 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e4beaa9-1e93-32cd-8231-882f4457f408 | -7.06631 | -59.187 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 057f52b8-a108-3fb2-ae1c-aa5ca5836f4a | -7.07994 | -59.1747 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| cea5dba0-dd16-3d0e-abe9-ec1292fdd992 | -7.08479 | -59.17935 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| a67ba3de-83de-3497-b503-51558db1e825 | -12.58515 | -47.20528 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0291c811-7cea-3b4a-ada7-bba6e40b2b89 | -7.06501 | -59.19418 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 738e8ab3-086c-37b8-9ebe-0eeaf59369b5 | -7.09031 | -59.18038 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| cd3f1677-1b15-39fa-9f03-2176c8710158 | -13.05002 | -43.84699 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 253fc2a7-8ffe-3570-89e6-ba9a36fb521b | -13.77574 | -48.87994 | 2025-08-09 04:42:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3da7645-afe6-3f1a-8fa9-627128f9e6c3 | -9.86011 | -44.69918 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf6b8a92-2ab0-3cd0-818f-c61829500006 | -10.00679 | -48.13085 | 2025-08-09 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01340934-63ec-3931-84a3-33ba5773d83a | -10.17767 | -49.51244 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09ca0523-daeb-3213-8460-3d91ede21b0f | -11.93756 | -44.54815 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac36a13c-8527-385f-a17d-8d2c7571327b | -7.08611 | -59.17204 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b5e6b84d-db7b-3472-aa08-6ed515c65658 | -11.77599 | -47.39653 | 2025-08-09 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67dceefc-85c8-3f96-8685-8d58bb230bbe | -13.55409 | -55.25473 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 33631fda-d166-30fc-9b42-de31ad319cb0 | -10.60616 | -48.36183 | 2025-08-09 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b166d5f9-993c-362d-b516-2bfcabd248bf | -10.83028 | -49.38157 | 2025-08-09 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
