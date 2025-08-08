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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422d7682-4d05-3004-a430-def56ca9f3cd | -6.1906 | -42.51126 | 2025-08-08 12:32:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.5 |
| 4a8e45bd-f037-37a8-bfea-a76b47bd11e8 | -7.25927 | -44.66177 | 2025-08-08 12:32:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 846f3eba-cb00-39f8-b15b-2a1a2e685892 | -7.57176 | -44.402 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3a0e2acb-3233-3b14-897c-2e9598783897 | -6.53997 | -43.21427 | 2025-08-08 12:32:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 97de0876-f946-3298-87a5-0d9beea3fb15 | -7.89334 | -45.3369 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 43e455d4-8fe9-3e84-80bb-eb766bf39733 | -7.90242 | -45.35279 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 64a45202-1961-3a4e-857b-a50e273691ca | -6.12795 | -42.96437 | 2025-08-08 12:32:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| fe9ed998-8291-3750-8f98-ccac9d5802b9 | -7.89141 | -45.35124 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2cdb5abd-3873-3504-b549-ac9e9279d662 | -6.53824 | -43.22773 | 2025-08-08 12:32:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 5dc69c8c-9cb3-37d0-9882-8e92b3135b2e | -7.26023 | -44.67151 | 2025-08-08 12:32:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 47b1c27c-efe2-3c74-9f3f-c1d365cc57b3 | -6.77501 | -43.81999 | 2025-08-08 12:32:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| aa1ae129-7f20-3634-9211-9bde48a1fa3e | -6.54094 | -43.20766 | 2025-08-08 12:32:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 159460fd-55e5-37b4-898e-d544c87013ab | -5.07521 | -48.31329 | 2025-08-08 12:32:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1faa342c-9426-37f8-8af5-51c5567e4f22 | -6.74071 | -44.77713 | 2025-08-08 12:32:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c27f0b57-c0e3-383a-811b-18ff8fdc8c6f | -3.47552 | -48.98462 | 2025-08-08 12:32:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8730449f-5b62-3199-98e0-537bc783d928 | -3.54669 | -43.1949 | 2025-08-08 12:32:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 11a9adb0-345b-3cda-bfc1-a684ea952cb0 | -6.27365 | -45.27547 | 2025-08-08 12:32:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8ab475df-da22-344c-9227-0e756440bb1a | -3.36541 | -42.993 | 2025-08-08 12:32:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6a4d1741-45b3-3a6e-affc-573f31cff83e | -7.91539 | -45.34 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 45ea8d9c-89e6-35c6-96ab-9b23b5ec0119 | -8.84906 | -49.85411 | 2025-08-08 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77c7d9ce-8e65-3ec3-891b-2c8475b5cdab | -12.09871 | -44.72644 | 2025-08-08 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 340eedb3-952c-3309-b044-b2e5acb0a6e4 | -11.56061 | -47.45164 | 2025-08-08 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 783ad35a-9eae-3c06-9d8f-efffc79edb40 | -10.43381 | -44.34825 | 2025-08-08 12:34:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 19dbd56d-e0ff-3b7a-a075-f2f71ea767ee | -16.62214 | -50.43027 | 2025-08-08 12:34:00 | TERRA_M-T | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b38d0779-54d6-3e1c-a10f-ec3f436c3a25 | -14.7761 | -47.99504 | 2025-08-08 12:34:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 216ae71f-d2c1-3817-aef0-a9344ca601a0 | -11.09473 | -50.48128 | 2025-08-08 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 71537045-aaa4-3d69-86b4-5e9d9fbc73d2 | -16.62083 | -50.43988 | 2025-08-08 12:34:00 | TERRA_M-T | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e1eabaab-f3b6-3b53-a09d-8c6aee566eb6 | -12.57114 | -47.13496 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 9822a110-6aa5-301f-8534-03a20076ea26 | -11.06833 | -50.46191 | 2025-08-08 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7238249b-628b-3696-9392-f6d1290ea20c | -10.64802 | -45.22507 | 2025-08-08 12:34:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f1ec4a78-2add-3045-8269-87907ebadcb4 | -8.91376 | -60.56736 | 2025-08-08 12:34:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9b0b98e8-1c68-31d6-ae29-c060ad9222a0 | -16.01673 | -43.37191 | 2025-08-08 12:34:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 043cdb40-5589-3971-acc3-80626c25b8ba | -13.71365 | -51.94564 | 2025-08-08 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8117366d-7489-3efd-bfdd-a5f6a4b0913e | -14.7846 | -48.00838 | 2025-08-08 12:34:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2f69fac3-d8cf-3508-8ab3-736912ed9a0b | -18.59504 | -51.80708 | 2025-08-08 12:34:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eb731ad2-d0d6-3b5e-ade3-75d3dfc1c1ef | -11.01142 | -50.54479 | 2025-08-08 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4b7ba63-0fa7-3313-b28f-75f7a2e38cb3 | -12.55042 | -47.13221 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 787216a7-4b1b-32c5-8220-deba40435578 | -10.62648 | -44.77064 | 2025-08-08 12:34:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| da715e47-ea04-382c-a4f5-a11925f5b1d5 | -18.84341 | -47.03541 | 2025-08-08 12:34:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e6204e3f-aa7d-3af9-89a9-a6a1dadf61ad | -12.09636 | -44.72038 | 2025-08-08 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b25a1beb-83fb-3517-be18-98a3358abacb | -12.52474 | -47.11021 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a16559a7-fe84-3cfd-ba58-17ad0d7f0b57 | -11.73652 | -47.51114 | 2025-08-08 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5a0dc861-b1ae-3258-b4b5-f552ba6044c9 | -11.77925 | -47.4992 | 2025-08-08 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2edeae61-cc3b-33d4-8a72-dd5df5ea3060 | -12.56074 | -47.13391 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| ea88e65a-0e2d-3d0c-82f3-41ef7a061b5b | -12.53511 | -47.11156 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d2a08682-82ce-37f5-8717-afe8589c928c | -12.67588 | -48.19494 | 2025-08-08 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f63538f-f605-3e35-814b-3df3afdf84a6 | -12.57342 | -47.19892 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2f7b51b7-8d28-33a7-9451-b92d26fcb0bc | -11.92197 | -44.85254 | 2025-08-08 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| c0c31834-049b-3e1a-91df-1b69bdd3c7fe | -18.85297 | -47.05326 | 2025-08-08 12:34:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 0317fcfb-182b-3bfc-a74b-355ef5228e77 | -10.59853 | -52.78052 | 2025-08-08 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 609a1f1a-18f5-3a91-91af-a43a99e00b35 | -11.7808 | -47.48722 | 2025-08-08 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f8a6cd6b-2ae1-3c37-9f42-918c188efeb9 | -11.80161 | -43.8157 | 2025-08-08 12:34:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| b07dfbc2-72f1-35f5-b8e4-b253e251bef8 | -16.32838 | -47.71459 | 2025-08-08 12:34:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2a58a927-a0cf-38da-b17b-2da75a5dbf22 | -17.05878 | -49.28913 | 2025-08-08 12:34:00 | TERRA_M-T | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 74cee6f9-e139-3efb-aaad-e54f71124662 | -10.63341 | -44.75926 | 2025-08-08 12:34:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| f1654fc7-8c2d-3023-96ab-ddcca65cffa9 | -12.23161 | -46.75072 | 2025-08-08 12:34:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9a3ce654-2e7e-37f1-ab13-6cec4a544bd1 | -16.33468 | -43.51462 | 2025-08-08 12:34:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ee00420b-626b-3f67-8ccb-134ad9fa45fe | -18.84151 | -47.05174 | 2025-08-08 12:34:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 59c15c0e-d106-3712-a38d-1523247dc398 | -12.58698 | -47.17528 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 15701fec-240d-3cb3-b794-b8cc15c6b296 | -10.86038 | -44.80183 | 2025-08-08 12:34:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0707fb4d-c9fa-355d-b812-382e8153966b | -12.57504 | -47.18642 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6be50e0e-a789-3f39-8d87-012158323aff | -12.56953 | -47.1475 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 2d18333a-b2c9-335a-86dd-98d66d1aca64 | -10.62872 | -44.75309 | 2025-08-08 12:34:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5e559d9f-9186-3097-be04-beea5b4b3baa | -12.98832 | -47.46016 | 2025-08-08 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 57fddd9e-475b-34e0-98ad-31f6e19a4677 | -11.91321 | -44.85719 | 2025-08-08 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0efa643a-2b77-36ce-90b6-93ca833de3b8 | -10.59699 | -52.79069 | 2025-08-08 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 49085cd6-adbb-3a46-ac31-06c3250f0306 | -10.67838 | -50.54477 | 2025-08-08 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 92028133-9edd-3cbe-bc46-9063912f9369 | -16.26185 | -54.45617 | 2025-08-08 12:34:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f9443b76-2473-3543-b573-251ba8c2775f | -11.06704 | -50.47083 | 2025-08-08 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 1fb3f3f6-48b9-3524-b0fa-e9dbba18b950 | -12.58536 | -47.18779 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bedae618-e7ef-34b1-b4dc-b1bf94c6dbd7 | -13.00395 | -47.49927 | 2025-08-08 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30caa03b-f8f0-3ee9-b0ce-d1e8fb7b367c | -12.49352 | -47.49855 | 2025-08-08 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5e2fc579-4e50-3933-b726-492329d12d28 | -18.85488 | -47.03697 | 2025-08-08 12:34:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| f60f212a-a4e9-33b9-916e-231a74692739 | -12.52639 | -47.09757 | 2025-08-08 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d402b010-f7e1-3b2d-885f-a2b529df5f69 | -17.75794 | -45.58691 | 2025-08-08 12:34:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 43c57705-a035-36ec-831f-4706b64a5c56 | -11.77146 | -46.29747 | 2025-08-08 12:34:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 02e37339-5ef5-39e2-8486-b65e141f534d | -16.01761 | -43.37886 | 2025-08-08 12:34:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c85cff9a-04b3-3275-9bc5-fa0225ec4d2f | -10.64594 | -45.24134 | 2025-08-08 12:34:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 946a01f9-8ea7-349d-b5ba-f9431ff3b3e6 | -16.32126 | -47.72124 | 2025-08-08 12:34:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8bc5f75a-b5e1-3c80-ba10-40da4ed051b7 | -16.01371 | -43.39937 | 2025-08-08 12:34:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 140a720f-f006-3a57-a659-8446913c3322 | -16.33598 | -43.52143 | 2025-08-08 12:34:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4d0061e5-671b-3dcb-a94e-0cf444998bb5 | -13.71231 | -51.9548 | 2025-08-08 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2786d357-cdee-3b02-93ae-b59df84b1820 | -12.09404 | -44.73911 | 2025-08-08 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2138a2f9-a4bb-39a0-b8b5-ece27ee59fef | -12.49319 | -47.50479 | 2025-08-08 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| eca1ce86-406c-3d54-aa78-dd58fcdb820b | -10.99568 | -45.9101 | 2025-08-08 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 049c837e-a990-3e3a-9eb4-0f2660952143 | -16.62123 | -53.13212 | 2025-08-08 12:34:00 | TERRA_M-T | ARAGUAINHA | MATO GROSSO | Brasil | 5101209 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0ddc30b1-29c6-3078-9ad4-78ff3f47ff5e | -11.7692 | -47.49837 | 2025-08-08 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 094a40e4-d5e6-315d-a755-8997b23aad86 | -20.81081 | -44.52086 | 2025-08-08 12:36:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 93f6985e-847d-3040-9304-f3986b2fc87f | -21.6322 | -46.43786 | 2025-08-08 12:36:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 8bd229ec-a7ba-30b1-bbf6-5886e96c9462 | -21.4375 | -45.10752 | 2025-08-08 12:36:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 5051b95c-c74d-3c04-977e-8bd4165e799d | -20.82521 | -44.52218 | 2025-08-08 12:36:00 | TERRA_M-T | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| ae9f9b6c-f1c0-363a-bf16-bbbf53e1c20b | -21.44323 | -45.12676 | 2025-08-08 12:36:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 7888c92e-9ccc-3bb4-8b2d-d0412b850c58 | -7.8915 | -45.3575 | 2025-08-08 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 26ff3596-b0b8-3c86-a73d-b6d6c79e5388 | -12.5337 | -47.1189 | 2025-08-08 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 77db6cd8-3821-39aa-ae06-400daf964bdf | -12.5341 | -47.0964 | 2025-08-08 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 12ebe7f0-2218-33dc-a0e0-2741cbbedd01 | -7.0614 | -59.1972 | 2025-08-08 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 296.1 |
| 8696caf2-7794-36a2-b09a-61fa79a05106 | -7.8918 | -45.3348 | 2025-08-08 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| f1d806e2-6c9d-34ca-82a5-847969923065 | -12.5718 | -47.1359 | 2025-08-08 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| c3aebe3a-f73a-3f6d-b437-d8cc454d5fe6 | -7.2603 | -44.665 | 2025-08-08 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 62e56769-5b65-38b4-add3-1e7a674538e9 | -12.5526 | -47.1387 | 2025-08-08 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |


[Clique aqui para ver as próximas entradas](README29.md)
