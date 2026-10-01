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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fbdb9f2-0bfa-3466-b9fc-790135d22727 | -12.26334 | -53.99311 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e52d5c-2532-3713-809e-3fde4c3ee4d3 | -10.35478 | -55.44585 | 2026-10-01 05:55:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c05ce5ed-d11b-3408-a969-50887c9cbd37 | -9.30542 | -57.7101 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acb54050-a92d-3703-ad1f-56ee8b909a43 | -3.59467 | -61.71856 | 2026-10-01 05:55:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 430f428c-88a6-3348-9900-f73cf91ac549 | -3.59529 | -61.7145 | 2026-10-01 05:55:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aff7bf97-d70f-3a3e-84f8-5e1142c0a9fe | -3.48646 | -59.52795 | 2026-10-01 05:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ab9e70-f039-3efe-bc53-fc1630e5e013 | -10.07335 | -63.08103 | 2026-10-01 05:55:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dab8fd65-9b4b-3d42-84dd-8a540ced1796 | -4.30806 | -50.73001 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4d11b3e-e1fa-3030-a002-1fe79a7a0e76 | -4.30123 | -50.77642 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| f92562f7-adfa-3d64-b6a9-827f3fb9036a | -9.00324 | -65.6981 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c84db88-684d-3069-9a6a-8c8ec5c34d3f | -4.391 | -54.82733 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81dce818-992a-3ffb-bc00-104977942e9f | -4.26809 | -50.74866 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 797a829b-3545-3731-a380-20283326a26f | -4.28466 | -50.73668 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e15d5cf-486e-35af-b7a9-570168dec332 | -3.80343 | -59.3036 | 2026-10-01 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619541ad-5b9f-3cf0-bf8a-40a7b47cf99d | -3.22032 | -54.31442 | 2026-10-01 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb4ca5f-6997-301e-a519-82deecd314c5 | -4.25458 | -50.73917 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8cd8a542-5b04-3f14-93d7-d74698908260 | -3.14201 | -53.7407 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 614f8b38-348e-39a6-ba62-b405b84830fb | -9.96287 | -59.2566 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf623acc-d70c-37f3-95a0-e1e8f8a96349 | -4.06876 | -51.10183 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35608674-bdcc-39eb-8f03-04f47f049b72 | -4.27635 | -50.74287 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ffd9d376-7e37-33b6-8b8c-f3826709dbdd | -4.28566 | -50.78153 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| aa02d616-2f32-359b-a102-f1439ca1e38d | -3.03154 | -53.86914 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8290aae-0d3f-3760-b8fd-89c1d0c4f237 | -4.26395 | -50.77777 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 75744c20-825d-3b4f-9e03-bebc6b754d3b | -4.26887 | -59.89023 | 2026-10-01 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1da241ba-9d56-3880-a372-546ee2717e5c | -9.66323 | -65.00411 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58ef3d62-0eb8-37d4-8778-6bd65da2422d | -9.54573 | -56.16252 | 2026-10-01 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3ffec8-3a97-3f96-a058-419442c182b7 | -13.6583 | -53.934 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 862aced2-8db4-3230-a5ce-2f4239796b7b | -11.26319 | -54.81908 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 446a8f67-dc7e-3f3d-9cc5-9e8e4841f34f | -2.87944 | -54.87553 | 2026-10-01 05:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4438359-d3a2-35ef-9f3e-841aab2cbb6d | -4.27535 | -50.74988 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1535e7d8-3fec-3b74-a230-e7f26ddc3aa5 | -9.00657 | -65.69863 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b2807de-7a49-3572-ab4f-f098449299bc | -9.70142 | -58.13043 | 2026-10-01 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b00f69d-e467-3911-96bf-d16be857c608 | -10.51613 | -57.77215 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 868230cb-cdd7-3005-b3f4-66197f72b410 | -10.41245 | -53.7755 | 2026-10-01 05:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d74d7d-f092-36d5-bdb7-b77552c21f1c | -4.2535 | -50.74683 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 09e67435-719a-3b62-afcc-373e9ec0ef13 | -4.28464 | -50.78865 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 5e2064d5-89cb-378b-b279-5d18bcd8bbc8 | -3.01383 | -53.88649 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dfcae06-a84f-3733-a850-891cbd2254fa | -12.71117 | -54.06884 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 104cb61f-b501-3466-8764-37eafd546bc9 | -4.29504 | -50.76785 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 94799766-79f0-35a7-9a0f-36bf0797f4eb | -13.65156 | -53.93303 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ebd5b523-0b55-3071-b98a-43fabcf60c7c | -4.38712 | -54.82548 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d1e3d45-7c47-302c-bffb-e16c57302684 | -4.28669 | -50.77433 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 39a48409-e9ab-340f-b291-10588ef66cf9 | -13.66613 | -53.94658 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5c9ba0ad-98bb-36f0-920f-ca13057184ce | -4.29996 | -50.78879 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| acea2b0b-4f06-3af4-805e-8a5859d9eeb5 | -10.54077 | -57.78168 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa0621d2-8352-30d5-9589-15dc6ae6e216 | -3.16062 | -54.08401 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ad6f59-bc49-3bed-8649-903aeee34c12 | -4.27018 | -50.78613 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3a395e2b-da58-39d6-be9c-4589b25a596d | -4.26829 | -59.88971 | 2026-10-01 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c814ca-dbae-39fb-b2ef-e150e770c811 | -4.24527 | -50.75257 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 729f695d-baf0-3843-8d06-f177009e8bb3 | -10.50518 | -57.7766 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6a22af-d200-305f-becc-855823141382 | -4.26289 | -50.78527 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a6c675cf-817d-364a-a960-d9aa854117a5 | -13.65088 | -53.93921 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 525ef65c-98c3-3bc1-ab35-6242c4f573bb | -4.30017 | -50.78378 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 9b3ef618-e9d8-3594-a101-7fafa1aa800a | -3.16395 | -54.10172 | 2026-10-01 05:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d55566eb-ff61-338c-a2d8-65f61e2275f4 | -9.00269 | -65.7016 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0f3bc02-ddac-3a39-a219-52f055fe1d6e | -3.16646 | -54.08501 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6b3fbd6-b820-3798-bc46-8f98f8683316 | -3.01975 | -53.88735 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a81a052-e3ce-342d-8f23-f4c8f20ac110 | -4.30231 | -50.76893 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f0d01faf-c650-3336-a445-ed375be19a3c | -4.30542 | -50.74738 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 944cb15b-3c26-30ef-b4b2-544c1ac4853c | -9.02037 | -60.55213 | 2026-10-01 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8133aaf4-0900-3f11-b071-55c717e01230 | -3.59857 | -54.55568 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c561d61-84dc-32ba-9d50-eb330ec46396 | -9.54062 | -56.15797 | 2026-10-01 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b71812a-3004-31b9-8780-1bd647e582c2 | -3.02828 | -53.8712 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75012400-1cb4-35f2-ad5a-9ad6d3e9ecfa | -4.29088 | -50.74511 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 55325459-93ec-3d0c-a718-111a62c87233 | -11.16549 | -54.11721 | 2026-10-01 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9adada-0a37-33f7-8e65-6b7255da8483 | -3.68412 | -60.53872 | 2026-10-01 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00044275-2ac2-36b2-8b62-ce7880900c29 | -4.27011 | -50.73451 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de656e8e-5792-3c8d-a4be-9f321f2f21e1 | -12.70453 | -54.06802 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb4652a-8ec0-376b-8c56-44235fad7a37 | -4.29273 | -50.78753 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0c613f7c-a3c4-360a-bf3a-85014f5de1f2 | -4.25873 | -50.75227 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8a1ef894-c85c-3bbc-8404-0a4b8b92fd5d | -4.24536 | -50.74224 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc60a3c0-ce9a-3692-b3f8-915aa375e788 | -4.25974 | -50.75525 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| b2086588-c7ce-35db-aa88-20a3b701b3eb | -3.70721 | -59.68385 | 2026-10-01 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cf5de7c-e181-3c23-b2a9-1ff02cfc29c2 | -4.25151 | -50.76096 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 131eaa07-0499-3f04-8e1f-371b2867f090 | -4.29672 | -54.79776 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39c33491-4ccc-3307-8628-7f337de39630 | -4.26701 | -50.75625 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d3a4c306-226b-3958-8305-4aaeddbc27f7 | -4.26095 | -50.73731 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 32bed749-cb29-3f72-88ad-c1948c109c27 | -4.27941 | -50.77342 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c8ee9b6c-b9a7-34e5-a782-b8e7abf28c4f | -9.71253 | -65.06312 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79e6d46a-75bb-3881-ad60-916e0bbe041e | -2.87838 | -54.87433 | 2026-10-01 05:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be4f44cc-ae80-33bb-b561-ad1ed15c7f96 | -13.65996 | -53.94 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ff1c4f9d-91b1-3e63-b97b-2e27d3136ef4 | -3.6834 | -60.54339 | 2026-10-01 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e402c9a4-e296-3ef7-a0eb-0292b6268ce2 | -3.68722 | -60.54397 | 2026-10-01 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee93f480-3e01-3727-b646-e3770242d68b | -11.25845 | -59.19752 | 2026-10-01 05:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68f5d1c3-7d4a-3939-82e3-29fb2d73b35f | -13.64646 | -53.93805 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 628896d8-a30a-3a91-8856-5fd0d694b185 | -4.28157 | -50.75832 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d7263fc6-03d6-307f-815b-e9560ea0e4e4 | -4.06255 | -51.09431 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82805ab9-a18d-3f13-880d-ac7c2764ff2d | -9.66943 | -65.0307 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 592e1fb7-c30c-34a8-b191-4a0d4858dbbb | -12.70784 | -54.0687 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58cd739b-8c61-396f-a8e8-6044dc1ad798 | -3.01448 | -53.88222 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 440e9273-34f0-3365-b655-16df2f004993 | -10.53686 | -57.77213 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85f744f6-1661-3057-8da4-4684d948697d | -4.29773 | -50.75108 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ece6af5-8b8a-36ea-803b-9813d89d51ba | -10.56268 | -57.77288 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f15cc156-ae4a-3b5d-9605-4d3f237a0391 | -4.24736 | -50.73771 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6f3305a-9e17-3a26-a639-b8e162668a8e | -3.22608 | -54.31538 | 2026-10-01 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9428c93-ec34-3fdb-ba2b-93437c2b74ca | -4.25368 | -50.73615 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f949e389-8d5c-38e2-b5c1-1ad24785bb89 | -4.29577 | -50.76538 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 8d172d1c-9d5f-3872-bf75-11f8a49eff49 | -3.16521 | -54.09332 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd891f75-fe5d-3c62-81b3-2989c0603611 | -9.0245 | -60.55268 | 2026-10-01 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f9ded17-cb58-3888-93f5-a74342e930bf | -3.6522 | -60.61947 | 2026-10-01 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README91.md)
