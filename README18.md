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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3265a907-7112-3231-901b-09d6e68cea6d | -9.7727 | -64.248299 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24d2a027-e3e4-324b-a015-51b08d80caf0 | -9.7172 | -64.903099 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa0a5eeb-89f8-3350-9228-9248ebade043 | -9.0945 | -65.738998 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 807fd680-2465-384e-b251-9278e09a264f | -8.1822 | -61.373001 | 2025-08-29 02:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 509c0644-0780-3cdf-824a-f0208349cf25 | -10.2779 | -64.4944 | 2025-08-29 02:11:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 185633be-ad7c-3159-88a8-28d4b7d9519d | -9.097 | -65.749199 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a47bf82-f22c-3e51-9040-fdb8c2989522 | -9.1167 | -65.787598 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceed308e-cb48-3f81-af3e-a5469dd26020 | -9.7758 | -64.260696 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f03c6831-b6b6-3176-8de4-1dde1fed8f39 | -9.1483 | -65.790703 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa77f452-d3fa-387e-a860-d6649e219468 | -9.4602 | -60.5835 | 2025-08-29 02:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c932775-0dee-31cb-894a-e19c7373d9b7 | -10.37 | -57.829498 | 2025-08-29 02:11:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce86158-ba83-3000-8978-584e247ceb2e | -9.0922 | -65.772003 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9a8b961-e153-3311-a116-c28b002f89f2 | -9.2182 | -60.880199 | 2025-08-29 02:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa53ea4-4eb8-3f50-8cb5-6702fe51c22c | -8.1352 | -61.229301 | 2025-08-29 02:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8d72a76-aeba-3637-8a51-a84503f65eaa | -12.4288 | -63.911098 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0cc9aa4-ec83-3044-a9d0-926d7c105724 | -12.4191 | -63.913601 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba82f7b4-e60c-38c6-8110-1b822a0988a9 | -8.9409 | -65.958199 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca5f2a9-973a-3fe4-8af4-079f8cebd0e2 | -6.9827 | -59.345699 | 2025-08-29 02:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2b4c3bd-c683-3b16-bf15-fa74e10e1017 | -9.1459 | -65.780502 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f93529a9-48c5-36af-9148-587540afd7e0 | -12.4317 | -63.923 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2b22c11-bd23-35f8-a039-e54193d49e31 | -9.1313 | -65.805496 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 743481f2-ae27-3898-9578-c60ace915f79 | -9.7824 | -64.245903 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6011d7-edb0-31fc-bced-581715b8387b | -10.8574 | -60.803101 | 2025-08-29 02:11:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed56314e-a791-3a00-b11a-9e1cf83398f3 | -6.9731 | -59.348202 | 2025-08-29 02:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0db94fd-d4e9-389a-8224-c3f9fa567c46 | -9.1606 | -65.798401 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2a879b0-7a91-38f2-a76c-14513d059dbc | -8.1298 | -61.208099 | 2025-08-29 02:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6581a18-2ec7-3432-a65e-55b7c23e1e65 | -9.2086 | -60.882702 | 2025-08-29 02:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 749a3ef5-c6ef-3aa0-b470-84e572952beb | -9.203 | -60.861198 | 2025-08-29 02:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0517a3b5-5545-3eb0-ac7c-530d7ffbbc0d | -9.1093 | -65.800201 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59a2abc0-e6f0-3790-932d-796209f65e88 | -9.1362 | -65.782898 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b536493-7ff4-3609-872e-0dea627c33a0 | -9.1069 | -65.790001 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a61e93a-e483-3dab-ba84-1ac859a41dad | -10.3605 | -57.8321 | 2025-08-29 02:11:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 234fd6e6-7875-37dd-bcfd-5fb736a93dda | -8.1726 | -61.3755 | 2025-08-29 02:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7c8618c-fe62-36b4-8017-bfddad12961b | -10.0966 | -68.961998 | 2025-08-29 02:11:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3d339ec8-d5fb-352a-acd7-55458e5dcb1c | -9.1142 | -65.777496 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14933b8c-bb0c-3b34-b30f-4328ba267d78 | -12.4094 | -63.9161 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb0a7d2-d988-31fd-a89f-e546e906a175 | -9.4544 | -60.561199 | 2025-08-29 02:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b25ecff2-93d7-3417-b89a-782d3d63ae39 | -8.4295 | -70.1464 | 2025-08-29 02:11:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c2954918-dd19-3027-b4a1-e303146989bf | -9.7691 | -64.275497 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9b59b8c-5963-3674-bd93-540103445a40 | -9.4448 | -60.563801 | 2025-08-29 02:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6192cc1-f85a-3ffb-8a0f-a328667dae70 | -9.7599 | -64.238297 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4307aa22-2535-3996-86c6-2bcfd8ac7d3e | -9.7696 | -64.235901 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6597e273-7a5f-3d8a-ba56-452cb09aa74e | -9.7563 | -64.265602 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63b2dcca-fe3b-3713-aba9-f09dd00943ab | -9.0971 | -65.792297 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd113fd-d855-311f-8b53-021f9f294510 | -9.1213 | -65.2966 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b08a75d-487e-3d73-a03d-eec69466ed52 | -8.6389 | -69.576698 | 2025-08-29 02:11:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7a27806c-4de2-3140-bc7f-a1814b161193 | -12.425 | -63.937401 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da48b846-ed25-3585-9dc2-d4e9e78d02cf | -12.4347 | -63.934898 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aacfce60-d6bb-3022-b38b-4a4031dd25ea | -9.4506 | -60.585999 | 2025-08-29 02:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6d9f20-204d-3de5-9e12-afbdd68d959f | -12.422 | -63.925499 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47fc6e84-95ae-3040-933a-b32cb35e249d | -12.4123 | -63.928001 | 2025-08-29 02:11:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b31d4c69-39d8-3c92-a8e8-2c18ebf386c7 | -9.1581 | -65.7883 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a932b74-9825-3e9a-a42b-c0cf031b4ff9 | -8.5557 | -70.066498 | 2025-08-29 02:11:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ed215182-098d-370b-853b-1172fdeea2a8 | -9.1216 | -65.807899 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccbbd8a3-3d20-3b8b-864e-982b8703820f | -8.5275 | -70.754799 | 2025-08-29 02:11:00 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9438704c-147e-3df4-8ecb-ceb6f0450662 | -9.4389 | -60.541401 | 2025-08-29 02:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73cda2be-7f60-34c3-a826-51b206cbee76 | -9.7199 | -64.914299 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 380be69f-86ba-37cb-83f3-0e20798ec79c | -9.1703 | -65.796097 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 790daa11-0740-3e85-9c05-70b38d50aeb7 | -9.0946 | -65.782204 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce14365b-202b-3e0c-acf3-35c4e7c0f1e2 | -9.794 | -67.844101 | 2025-08-29 02:11:00 | METOP-C | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2a16f649-0592-31f1-a052-47aad7c19e63 | -8.6862 | -69.424301 | 2025-08-29 02:11:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fa393864-f4a9-3189-86bf-113a4a530154 | -9.1728 | -65.806198 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a613f7f2-e56d-367b-9385-c1f8cd23a999 | -9.0995 | -65.759499 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 443b5804-eb3e-35d0-b052-37c2758f372c | -9.1191 | -65.797798 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc39f14d-8736-316e-8df1-874076f39def | -9.1117 | -65.767303 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58909430-4279-300a-8f30-e3fa14d6427e | -8.8856 | -69.438103 | 2025-08-29 02:11:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fc1b42e0-856d-386e-992d-49df669ddb59 | -10.853 | -60.826 | 2025-08-29 02:11:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c39c140b-f56e-3af5-afff-8e2bdfe3338f | -9.763 | -64.250702 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5a7060-659b-37b1-9480-3a0d477499ed | -10.8477 | -60.805698 | 2025-08-29 02:11:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a66fb3e-ab93-3cee-8473-85d16d059bc6 | -9.124 | -65.8181 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9fc393c-17d5-3806-8616-47c7bb8fd9e5 | -8.5259 | -70.747902 | 2025-08-29 02:11:00 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 22def13c-1046-3f17-bdc0-54664422a8e3 | -9.7661 | -64.2631 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9bca12-a2e2-3ee0-b92c-024475062eb5 | -9.7533 | -64.253197 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0789cc3f-a3b5-305b-96b8-24336592ab83 | -9.5386 | -65.695602 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ffd8e795-0099-3ef1-993b-948c550fb888 | -9.5264 | -65.687897 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 08686035-9a28-3bba-a50b-5fce04693e71 | -9.1508 | -65.800797 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c912deb-b0da-3c26-808a-483971ee359e | -9.1044 | -65.7798 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec7b0af-a2f1-3283-b9cb-37f903bd4eac | -8.6896 | -62.4776 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a62ded9a-14da-3190-80b9-41d7810d57a0 | -9.1288 | -65.795403 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a46f6b79-6e8b-379f-a1a5-357bab820c4d | -8.163 | -61.377899 | 2025-08-29 02:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44a53d1b-40f7-348a-8238-4ab4736e2eff | -9.0996 | -65.802498 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70f66fd1-de0e-33b2-96df-6da2529f62a0 | -6.9635 | -59.3507 | 2025-08-29 02:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a93b1de3-8a46-37df-b412-b1a28192e10b | -5.6081 | -45.0038 | 2025-08-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 210.7 |
| b651946a-59f2-37f1-9fb4-b1ec330e528b | -10.4551 | -57.9378 | 2025-08-29 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7f7d822a-2bbb-3306-bddc-24f718b774fc | -9.4432 | -60.5692 | 2025-08-29 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ddcc63a9-c01e-3a8f-b638-bc7d6d081ef6 | -5.627 | -44.9797 | 2025-08-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 050ff0e8-3050-3ab0-9969-409fc4fa93d3 | -9.134 | -65.7694 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 95e8be97-bf2c-3587-9e86-3397fcf47db6 | -6.5358 | -43.9237 | 2025-08-29 02:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7a68ca52-250a-3323-84ce-04d712331335 | -9.1525 | -65.7874 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7a51d7fa-0e23-3e3b-9d17-8856ae905f6d | -6.9684 | -59.3169 | 2025-08-29 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 67e2f1e1-a1af-3327-bff2-ebc477b0d5de | -12.0976 | -44.717 | 2025-08-29 02:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a6781838-d8c5-3051-b63c-17758b8dbc1b | -10.3624 | -57.8258 | 2025-08-29 02:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f68e5222-be86-33b1-b004-b62caca53f65 | -10.3812 | -57.8245 | 2025-08-29 02:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f8b5d73e-e5cd-39f0-aba0-08a32340e058 | -13.0151 | -56.9184 | 2025-08-29 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 737ddab2-97e4-3fc9-98c8-ab939d39115c | -6.9683 | -59.3362 | 2025-08-29 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 70db973a-96f8-304e-b07b-cec88eb25d8d | -9.4263 | -47.6384 | 2025-08-29 02:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 45da533d-3f5a-3724-b629-b4b4a4a108d9 | -12.9961 | -56.9201 | 2025-08-29 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fcacd62d-050d-392e-8b10-1988373d66c2 | -10.8293 | -47.4791 | 2025-08-29 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| a1595a07-ae24-3d98-b0f6-2bc4b807b1da | -10.8608 | -60.7998 | 2025-08-29 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8808f670-51f1-311a-9af8-489eae68fde3 | -5.6083 | -44.9811 | 2025-08-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |


[Clique aqui para ver as próximas entradas](README19.md)
