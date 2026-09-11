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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5777f84-6190-39ce-a962-b9c48facd8a9 | -4.74733 | -45.67439 | 2026-09-11 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e7496b7e-7319-3274-a387-612f232a9e50 | -6.63164 | -55.29632 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3408554d-dbcd-33d4-9825-45420ddf9232 | -4.47407 | -54.89728 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4372404-4159-33d7-90fd-1072e1ae1c10 | -6.33594 | -55.22141 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e490f713-8397-316e-b8e6-c32e972fa64f | 1.28859 | -50.68797 | 2026-09-11 00:26:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 24.4 |
| df5eab70-97b6-30c0-841e-774aeb021e19 | 1.28366 | -50.69952 | 2026-09-11 00:26:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d6381b27-830d-3d9f-95af-794cbcae782b | 1.28623 | -50.68112 | 2026-09-11 00:26:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a65cfb0a-5ef1-353c-b1ae-fe221841aa5b | 2.74251 | -60.2031 | 2026-09-11 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dbde5ef1-0201-324a-b698-e79e4b4368ab | 4.70979 | -60.84532 | 2026-09-11 00:26:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1af873c4-553d-392a-ac33-59eb43ce8a09 | 0.99129 | -51.12983 | 2026-09-11 00:26:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aa7f25df-ab6a-304b-a5aa-77eb825d61d1 | 4.75944 | -60.43388 | 2026-09-11 00:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ace23de0-7988-3b17-8a27-6a7302c12564 | -9.043 | -65.4175 | 2026-09-11 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f6db702c-1903-328b-9a05-2fcfef3637c7 | -9.18 | -68.2009 | 2026-09-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| f2c01abd-ba61-341e-89f6-8c2949a714dd | -19.8023 | -58.0593 | 2026-09-11 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 367e1f01-7c5d-3209-81c8-30391626fc03 | -2.7148 | -57.6274 | 2026-09-11 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7de70d64-1d32-3a73-b365-95c651039646 | -9.1799 | -68.2194 | 2026-09-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 142.3 |
| c6995c04-55c3-3eb9-9a59-cbb476c7ead4 | -14.6026 | -48.8601 | 2026-09-11 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 26c3d393-a504-31b5-82a4-f54fb5b86dea | -9.1985 | -68.2004 | 2026-09-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2ac3bd3e-678f-396a-a409-e0913a670dd0 | -9.1984 | -68.2189 | 2026-09-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 75385f27-7f96-34c2-9790-0fd803b6dcde | -5.2115 | -45.5498 | 2026-09-11 00:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| afb689c1-dc8d-378e-9369-dd127991b04b | -4.2953 | -49.1021 | 2026-09-11 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 4e3be59f-8217-3874-81c3-f063faab422e | -2.7331 | -57.6271 | 2026-09-11 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ba51b52b-4b7d-3ea7-918b-905af695f6f9 | -10.7772 | -45.9372 | 2026-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2ad5993d-420c-3f47-9343-ee8baf8d14ac | -9.1985 | -68.2004 | 2026-09-11 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9f127af6-4d86-36b3-bdb6-a2e9c0acc9d0 | -2.7331 | -57.6271 | 2026-09-11 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6f174c28-835b-322d-b508-62435c9d6261 | -9.043 | -65.4175 | 2026-09-11 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 851fe3ae-f854-3324-9185-3ea069689b2f | -19.8023 | -58.0593 | 2026-09-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 03ff19c7-f400-3234-bb59-01ce43d60288 | -9.1799 | -68.2194 | 2026-09-11 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| abbade7d-db85-3e5a-aa34-9469d91cee02 | -9.18 | -68.2009 | 2026-09-11 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| adbaccd7-c940-3175-91e5-b1a0995e1fa6 | -9.1984 | -68.2189 | 2026-09-11 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c01634b0-d7fe-318d-920b-c169e3c9f3c3 | -4.3587 | -47.7853 | 2026-09-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bb2fe4aa-bee5-3876-986a-61a6f3765b94 | -5.7756 | -45.0826 | 2026-09-11 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a9f30d5d-6e85-3d7c-99b5-b865d365e4af | -19.7822 | -58.062 | 2026-09-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 74e99f33-a77d-33ac-a4cb-79506a504ee4 | -14.6026 | -48.8601 | 2026-09-11 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7a2b11cc-bc6a-39a3-ae9a-f0304003ffd6 | -2.7148 | -57.6274 | 2026-09-11 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1f3961e8-aee0-3353-b53b-12b9ac52bee1 | -9.1799 | -68.2194 | 2026-09-11 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9586a992-fd0b-3d60-8e5c-92de386f2c87 | -10.7772 | -45.9372 | 2026-09-11 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 08891440-4ea4-3c3f-83bc-f144c2f51341 | -10.7963 | -45.9348 | 2026-09-11 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a3c6deaa-2b4b-3536-a8e1-0a38705100a9 | -9.1985 | -68.2004 | 2026-09-11 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1a81b614-54a2-3336-b72d-8c2ff78aa229 | -9.18 | -68.2009 | 2026-09-11 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4a352336-e2dc-3ffe-9f84-4dc938b3a351 | -4.5413 | -54.9633 | 2026-09-11 00:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aa87f946-2977-33f8-94e9-2be489ebbbc5 | -4.3138 | -49.1012 | 2026-09-11 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e973a5a4-9a3f-365b-8b65-e4d5dcca8fd5 | -19.8023 | -58.0593 | 2026-09-11 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| c046f0b9-6fac-3400-a9d7-a60946bb5ffe | -2.7331 | -57.6271 | 2026-09-11 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2e0a9028-c7dd-3a96-95de-1023d28fad91 | -9.0244 | -65.4181 | 2026-09-11 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0597ee56-fc9c-374c-a3c7-8aa5018b5a30 | -14.6026 | -48.8601 | 2026-09-11 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6ad72617-e46d-3593-8c31-1031d80993de | -9.6295 | -40.3392 | 2026-09-11 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 779ee936-5724-37b0-a2c9-061885ba5b71 | -8.6311 | -66.5101 | 2026-09-11 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a7042775-6c74-38f7-b069-3610ad2612e4 | -4.2953 | -49.1021 | 2026-09-11 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4d5d1565-1b97-3c35-917c-cf3e03e6d6d9 | -9.1984 | -68.2189 | 2026-09-11 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 3a839dbf-c9ff-3a65-bcbc-35c9142dfc57 | -4.3587 | -47.7853 | 2026-09-11 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c7e0964d-5aad-3e49-99ba-9521b0c73ebc | -2.7332 | -57.6077 | 2026-09-11 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 78ddbe39-0553-30a2-8775-d1dc0ba727a5 | -9.043 | -65.4175 | 2026-09-11 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a78ae270-059e-3556-b27d-57db0bfd30cf | -9.1984 | -68.2189 | 2026-09-11 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 4eb0f7d2-d912-34d5-96a6-3f8b6f151747 | -13.249 | -61.5983 | 2026-09-11 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e90c5f28-b31e-31d0-af98-9b411795332a | -4.5413 | -54.9633 | 2026-09-11 01:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5446fa5a-6e02-3787-9a60-0f8d6402cf5e | -4.2951 | -49.1234 | 2026-09-11 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 41ae162f-a5b1-37ea-acda-780510bea0d7 | -9.1985 | -68.2004 | 2026-09-11 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 313c751f-112a-3479-a65b-911b94fcb7fa | -9.043 | -65.4175 | 2026-09-11 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c7d32f55-a1ed-3a20-82ec-fd55f25fba75 | -2.7148 | -57.6274 | 2026-09-11 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cdcd7baf-ea4c-3231-9b26-e1a923623132 | -4.2953 | -49.1021 | 2026-09-11 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 450efd01-cbca-3877-9417-301aa371ce90 | -16.208 | -50.4112 | 2026-09-11 01:00:00 | GOES-19 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6e662582-bcbd-33e6-90ac-cd6f3d84f39c | -4.3587 | -47.7853 | 2026-09-11 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 00662195-a665-3c11-9123-aa1b909ad6c4 | -19.8023 | -58.0593 | 2026-09-11 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 9a5a3acb-a571-30c4-ab54-3da9a258796f | -2.7149 | -57.608 | 2026-09-11 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| bbc2c451-31aa-36b1-b4aa-825255fc7cdc | -9.1799 | -68.2194 | 2026-09-11 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 93287e9a-ff7a-3f05-952d-1601ce81f0b2 | -2.7331 | -57.6271 | 2026-09-11 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| cae83591-b810-38c5-aba0-8cd694590a14 | -9.18 | -68.2009 | 2026-09-11 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 080c99f4-38b4-3324-9660-654755046d81 | -13.2488 | -61.6177 | 2026-09-11 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 440a88c4-d8d2-3d93-982d-5d151959e4df | -2.7332 | -57.6077 | 2026-09-11 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c46225cc-836e-39dd-901e-c544c5ec4109 | -16.2084 | -50.3892 | 2026-09-11 01:00:00 | GOES-19 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 756e12f2-9fa9-3b26-a269-46a0e27790b5 | -9.1985 | -68.2004 | 2026-09-11 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 352e7601-09e2-3d30-87e5-3e9a6210be75 | -9.043 | -65.4175 | 2026-09-11 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a0b953c1-f8f5-3d47-922a-d970e4f34d27 | -9.18 | -68.2009 | 2026-09-11 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 0e4fa173-61fd-3066-ab47-7ed851088342 | -2.7148 | -57.6274 | 2026-09-11 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0b0662c1-7fb8-3393-b8c6-f78218a33dac | -9.1799 | -68.2194 | 2026-09-11 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 3387154f-0142-35be-976c-9a8c4ed1de5d | -4.3587 | -47.7853 | 2026-09-11 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| fc1ee54a-8a01-3f93-9deb-b557d9e38691 | -9.1984 | -68.2189 | 2026-09-11 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ead878f8-4549-3caa-a39f-9d9dfa76ca66 | -2.7331 | -57.6271 | 2026-09-11 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 9c20d83c-202f-3a1a-8d1b-401c6840765a | -13.249 | -61.5983 | 2026-09-11 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 272cc4ab-4083-3755-9b5f-86e485c6b03e | -4.2953 | -49.1021 | 2026-09-11 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 2684a8bc-0901-3595-b23d-11b8c53550a3 | -19.8023 | -58.0593 | 2026-09-11 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 8d27de81-8025-30c2-9e2d-77a4e014e62b | -4.3138 | -49.1012 | 2026-09-11 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c8a6fc7b-d05a-3bdc-827d-9ae0930a6e7d | -10.7963 | -45.9348 | 2026-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| af3c8b1c-8473-3f4c-b662-eeb321947c98 | -4.5413 | -54.9633 | 2026-09-11 01:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b0094224-0973-3fd1-a878-c8ce97942af0 | -13.2488 | -61.6177 | 2026-09-11 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 5720a3db-d12b-3d6e-990d-edf08a4cd558 | -10.7772 | -45.9372 | 2026-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5d8075b9-fb73-3414-afc7-826bc5cc9218 | -2.7332 | -57.6077 | 2026-09-11 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a9d4310d-61c3-3c0a-9640-d7ed0f64b1ec | -9.1799 | -68.2194 | 2026-09-11 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b4b42262-c78a-333e-840f-859d1428aa31 | -10.7769 | -45.96 | 2026-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0df30a68-4f30-372f-9366-638d505817c6 | -2.7148 | -57.6274 | 2026-09-11 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1adef33e-d364-3961-9820-5b7df2ed6f64 | -9.1984 | -68.2189 | 2026-09-11 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 12b8608d-4a4d-3eda-a1fb-098b82d32651 | -9.068 | -61.0296 | 2026-09-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a66462ef-3235-3f82-bf37-5806fbf810bb | -4.3772 | -47.7844 | 2026-09-11 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| eefe2256-ed12-3945-94ea-af27d47460a0 | -4.3587 | -47.7853 | 2026-09-11 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8c734975-3775-3491-a9c3-539f81be3338 | -5.2115 | -45.5498 | 2026-09-11 01:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0671b994-2871-36a7-bfe3-0630efb1519e | -10.7772 | -45.9372 | 2026-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| bad8ead2-4acf-3d96-a830-26f481b53d3e | -8.6311 | -66.5101 | 2026-09-11 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 89ca26ab-f547-3fea-b5b9-87e5750203c5 | -2.7331 | -57.6271 | 2026-09-11 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4c9e4824-b0e2-3395-b1aa-6f39b1ba049d | -10.7963 | -45.9348 | 2026-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |


[Clique aqui para ver as próximas entradas](README4.md)
