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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ae06aa-eed5-30b7-bc18-1d2657a3f05d | -9.47534 | -57.02386 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab619059-34f2-35e9-b79b-9f0992d5e6b6 | -10.7865 | -50.50279 | 2026-09-01 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b546754-c240-38ce-ba1c-53a6b61ac271 | -9.36993 | -60.31518 | 2026-09-01 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dae425e-0368-3798-9279-9dbb427824b7 | -8.94945 | -60.60228 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdd1f352-5192-355a-813f-d63f8947ec13 | -4.79967 | -55.97181 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de961d37-01cf-3789-88ce-0dc0c75706f6 | -5.95763 | -57.67416 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2093d5-7d5e-31a9-92ca-fc9b024c96ff | -6.12189 | -57.67801 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 462658b1-a6d9-39a9-a691-61bb462f50aa | -9.47257 | -57.01981 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4e3c3c-8c1d-3a93-a2d6-fa5bad4bc9df | -7.20099 | -60.67693 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45557d5f-dbf0-3ca6-ba6c-4f7c351e2a81 | -6.20975 | -53.58985 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0489c0f3-6efd-31f6-bfa9-34137fd43f07 | -10.03039 | -44.68771 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f762f3d-a974-34ca-93be-2f001c015d3d | -9.47201 | -57.02332 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94b4480-80eb-37f2-9401-8770971dc542 | -7.5613 | -60.46693 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbd487c0-5132-307f-a094-a47b2420abc7 | -6.62198 | -58.38387 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa130900-6056-3181-a22c-4220da1a446b | -5.94087 | -57.69053 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ce00dbe-fe88-3233-ac13-7549ba84e184 | -5.24861 | -55.91456 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64e57922-2148-315f-b457-3476b7783d4d | -5.95642 | -57.6816 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b1c218e-6648-323b-89c3-b57eba6da2fb | -9.47811 | -57.02792 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79386e0b-b680-3228-9cad-3d61af42f3bf | -6.8179 | -59.43866 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b5cce23-a933-33a6-a67b-3c1b51a54236 | -11.5173 | -46.92504 | 2026-09-01 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 977f8a2a-019a-3e29-affe-1e4aaeba351c | -7.56599 | -60.46269 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5bd6a318-c988-3be4-a3be-1ea76fa67ca6 | -8.26288 | -62.75954 | 2026-09-01 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5aec1b38-3009-3f03-90a0-655e54b57225 | -6.77536 | -59.42898 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1f1af7-befa-383a-b237-ca53f1639884 | -3.61129 | -59.06983 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4fad931-6313-39a8-bc01-6b30ba2e9ecc | -7.34403 | -60.59081 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a494756c-7923-32a7-8210-2b4a2ea0b4e9 | -8.62008 | -54.69337 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4810b2c-bcd3-31d1-a6e7-83755c3507cd | -7.62004 | -57.61522 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053d08de-dace-3450-8aa8-49380d801de9 | -5.89173 | -52.15373 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2cfd58f8-b5f4-3a72-a32c-ab0bca6fdd14 | -6.13801 | -55.6406 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cacab79-6161-309b-872a-3f8dab4121ad | -6.94353 | -55.63995 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bf0233f-1688-35c7-93b5-b5684fb0bd4a | -6.94693 | -56.51678 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d15ab02-7d17-3c35-874a-b1b9550d02c2 | -7.40088 | -49.63068 | 2026-09-01 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d75f49f-27c5-36ab-bc4f-78f48f96c28c | -7.28738 | -52.54023 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c5819e3-e80a-3346-bab6-afe277ca6181 | -4.06762 | -50.97088 | 2026-09-01 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a844cd40-cb21-376d-9bce-4ef39f0cdf63 | -9.16829 | -59.3647 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa66847f-eb42-3438-8b1c-a1ee5f7010ad | -8.48875 | -44.74532 | 2026-09-01 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b42697-7632-3349-a65a-1a2ee4d99622 | -3.12004 | -61.23325 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 583cb4c9-f5c5-3d50-a4bf-919305e1a3e6 | -10.69316 | -46.26119 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77e80e27-14bc-3735-a716-81e7fd1391dc | -8.4198 | -45.00098 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2475e149-19a6-3c34-bd02-6de4a63a0507 | -5.5803 | -60.23656 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87d77ea7-5fc1-3248-a96a-adbc594922eb | -9.79521 | -55.30669 | 2026-09-01 05:16:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67cb6cdb-ef46-3038-8cab-a5a000fc9d23 | -8.69358 | -54.69317 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c97931b7-4b08-3cca-bc6e-e83f2a7b56e1 | -7.02194 | -59.64875 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e04d589a-8cc2-3292-989e-2cf5c0e34de8 | -7.41112 | -48.00023 | 2026-09-01 05:16:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 09951308-3531-3d4a-928c-0979baad807b | -4.85277 | -55.831 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e950c5c-b6b0-390c-856f-7eef7863582f | -6.74428 | -55.4654 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c72116f-8354-3543-9483-82c826eef193 | -9.15309 | -60.94114 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bff71cbb-6e5a-30e7-95cb-74303538a619 | -10.99553 | -48.39268 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ada5707e-c4c2-31b4-b3d5-6d2dab34863a | -3.63131 | -60.56738 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aa05b29-ba44-396a-847b-fd2f15144daa | -6.67468 | -58.74552 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e25c9f9-f8b6-32c1-ab95-b636ad5a2cc1 | -6.0907 | -57.71869 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173592ee-f0a8-3c4a-8be0-9a76cc0fded4 | -5.87819 | -57.78087 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55cd7d89-23aa-309e-ac5e-386462158e34 | -7.56518 | -60.46753 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba422da1-5797-33e4-9f98-db0c343531b7 | -6.82276 | -58.87236 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f0cf6cc-0a0c-37a9-a23d-3e9e0268f362 | -7.91367 | -61.33199 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2a91fd-c541-3f4f-9cf7-712c99c2f1c5 | -5.25303 | -55.90816 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fa201d5-4f88-39e7-87f5-e40de255a359 | -5.48389 | -57.1481 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b3fe999-7f90-363b-8c12-aa3d7048fa82 | -8.50773 | -55.3059 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d18ce07-7234-3620-89a6-5582afafb025 | -10.23729 | -54.34777 | 2026-09-01 05:16:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99a31f7f-2973-3e9c-80c7-6c9ab0f5e594 | -6.36237 | -55.99973 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9ed8882-c805-3023-82d4-af907369f159 | -11.47784 | -45.08064 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fa0c640-9d12-3350-9226-63e56a1fdf83 | -6.80496 | -59.4561 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abbaf8d-b336-3b24-8ce1-0d29016bb6a4 | -7.36273 | -60.59911 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f48c82-e4a0-3f87-96d0-516a58690e3a | -7.35606 | -55.19159 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f15d21fb-0b86-3cc4-8e29-6d929c21dade | -7.6304 | -55.29223 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 951d53bc-e176-3bf4-ba0a-742554ef4e73 | -6.24404 | -55.48671 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4cf75a6-e75b-34e9-997c-036406b09ee2 | -6.6561 | -59.42805 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c2a3887-905d-3f3f-aad1-978b8d915f5d | -8.92841 | -62.3593 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9865ad0-17da-37a6-b1a1-65671453c493 | -6.82543 | -59.57476 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01c1b059-5e09-36a1-aa6e-cecf8f1b97a0 | -3.79378 | -59.347 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ef94acf-a6ff-31b8-89e1-723faf29aa87 | -7.35551 | -55.19512 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94297456-ed43-396e-8072-9740b4875c7d | -8.23717 | -54.93744 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a81b5465-70fd-3de4-94ab-0b41539a3604 | -3.6214 | -60.5506 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09780a70-a82d-355e-a445-0f7256c68b24 | -7.57697 | -61.33381 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 512ed70b-ad96-35ed-90c9-72d104cad9bb | -10.02397 | -44.68685 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e700800-58fd-37bc-9dd3-ecc8a510dc2b | -6.15589 | -57.40041 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a635f539-cf6a-3e04-9dbd-9c0bc82e192f | -7.58319 | -61.34206 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37c3f80c-5f08-3f57-bef1-5ba378130b0b | -10.75021 | -47.98727 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a84b7b75-75f1-382d-976c-a958963eb3aa | -7.62427 | -55.28764 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eadec987-5326-3e4d-af62-7c104061c511 | -3.11637 | -61.22838 | 2026-09-01 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24049084-e046-39c5-be0a-41a2e71268cd | -4.96815 | -55.84904 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f869f7b3-96b7-3c10-8653-814bc0890034 | -5.25081 | -55.90071 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30be6390-4fcd-3492-a145-0d38b7cd9dc0 | -6.94408 | -55.63647 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6117790a-7f6b-3b6e-bcd1-1a277a63d275 | -3.25942 | -58.24072 | 2026-09-01 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a9f2718-faa1-39dc-8037-a5fbc7b110dc | -6.4199 | -55.52892 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1670ae8e-52b5-3059-9b8f-3fa684724e6d | -6.25226 | -55.4132 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31741ba5-bac3-33ab-8679-65e2a662ecf7 | -7.58452 | -60.47067 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b6e0c540-d00a-3d2b-b3e8-ddd727c0669c | -4.15493 | -60.7162 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc937e89-9450-3b37-a4f8-b7ea73d32d95 | -7.56049 | -60.47178 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 537971f2-a092-3bb1-943a-e60aff31be70 | -11.31444 | -45.17316 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 359430ae-c90a-3fe8-b591-9fb90105e615 | -5.48786 | -57.14503 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0b15dc0-608a-382b-a4ea-fdb4fc0f09bd | -6.13605 | -57.8443 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ced93ac-a66f-3adc-868d-a677f322b997 | -6.77554 | -55.67424 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 100940a6-19e2-3f20-9fa8-71f4aad28e51 | -7.45801 | -59.92998 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 826ed32e-1319-3e34-b1dd-fd92413f42e2 | -8.58999 | -54.77531 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d6a87b7-d7ae-3296-b29c-28a208ef11d6 | -8.26985 | -54.9276 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 84da0a24-1a52-3c2c-9b5b-f354cbee8f8e | -7.35431 | -60.57735 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3f184d9c-aa7c-35e8-9245-3b0607658f2b | -4.95819 | -55.84745 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e19c9db-36dd-357a-ad64-15315c5b7444 | -7.2775 | -48.12309 | 2026-09-01 05:16:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fab70d6-05c4-3804-ad6d-35d1a6a51392 | -6.52313 | -55.23421 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README62.md)
