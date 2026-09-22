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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 809875f0-ab31-31aa-9f7b-111a090c9b22 | -2.89935 | -60.05109 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e98f48a-b1d4-3d84-bc1a-a507e763872a | -3.54374 | -60.57969 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf349cb2-7f94-3333-aeb1-f968e765f70d | -6.05227 | -57.82367 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d3a4d4-8941-3454-b756-b680ab050ed6 | -8.60202 | -54.60704 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4020e956-5737-3f48-a6cc-e030489b9b82 | -3.70168 | -60.63467 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bc2bcb-d826-3cf2-97f2-96f8d173f4d1 | -3.28572 | -57.86262 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bc295d0-cc9b-37c5-9f78-7b841cf8054d | -3.06295 | -61.0601 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9e480d-bf72-3c21-abcc-a7f96860ce9c | -3.05756 | -61.27243 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ce14286-eb10-3ea4-92ff-c061314a534f | -3.05687 | -54.40959 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85bb30f7-299f-31fa-9d55-c787eb3c4b6b | -4.41161 | -55.24194 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e6130c9-6860-30ac-90fc-3b3a772f4ef5 | -4.50632 | -59.55735 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1560ecbd-5df5-30f7-bf6c-58d6dd5a19ff | -6.64423 | -59.9211 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3edb6c37-0c20-3319-aae5-d6bce6e490f3 | -3.07258 | -61.2671 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60405c69-7d66-3501-b1b6-0624c5435273 | -7.69268 | -61.53718 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 134d6ef5-bb39-36e2-a65c-6ff4b83f6148 | -3.77661 | -61.7622 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fefff86e-f8b2-3753-9942-237d0ef9383a | -3.30277 | -57.86138 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05cee4b8-e95d-34ea-8c5c-bd6ec186aab3 | -6.33437 | -59.95237 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 448117c7-df43-3f6c-9eac-a06ca360893e | -7.60381 | -55.36009 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dcac1e2-29d6-330d-b160-68425fd7cfa2 | -6.80062 | -58.79141 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec7ce954-7043-330f-a8bb-089a2106c5d7 | -6.35951 | -58.28577 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e89f6d6a-4ac4-3b7a-a984-76bcc45e6281 | -6.6277 | -59.93053 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9c5ceb6e-6101-3bce-ac65-1ad4921e9b93 | -3.07674 | -61.06215 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 435ed145-7688-3363-9df1-78161c84fea6 | -4.08654 | -62.08571 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d5bdac7-9eff-3491-b3d3-30c3b107823c | -3.45836 | -59.53049 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa6311d-b26b-37dd-a576-c727cc61628e | -4.0899 | -62.08623 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea903936-5654-3854-830d-a159623def2c | -6.38286 | -55.28242 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6593500-226c-3407-bfdc-a96bd8bbe414 | -8.61676 | -54.62427 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50293b8c-5e48-3834-b2f0-72e83b41ec25 | -3.05833 | -54.39971 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddfaf14d-142e-31c4-820c-720dc91c5f57 | -8.60152 | -54.61081 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2227df3-0818-36d0-afc1-23f0b7b8ae7e | -6.83639 | -55.5331 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151fc7e2-b17b-38fc-8e96-667a143f90f0 | -3.00586 | -59.37136 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0c210a7-1edc-396d-b0a1-091b5b5339bc | -5.98202 | -57.77713 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab4ec47-646a-32bd-bf2a-26ca50ca49a0 | -6.69696 | -59.95726 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a74ed2-9113-3eb7-b0ef-804467363123 | -4.22579 | -63.07752 | 2026-09-22 05:42:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2513210-d641-321d-87f5-0636dfa59d69 | -3.48133 | -59.57928 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3c7d47e-30bb-3b45-a755-56707e320dca | -3.52993 | -58.6615 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 011e7e7a-0cb8-33b3-a0c6-cacc013473e8 | -6.45176 | -59.96791 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7f50ba5-4775-3db1-8c01-f6c867ef4644 | -3.05131 | -61.26769 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da0820e-d671-3dc0-ab4a-0d12236707a2 | -7.32364 | -55.59833 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6c21a37-6ebe-3df6-a679-ca630ee0723c | -6.62769 | -59.92811 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 03518f69-3062-3cc1-bc3d-ca6ead3041a2 | -3.46953 | -59.5322 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c7ac70f-bec3-3fe9-83ea-fd2b1144a981 | -6.30866 | -59.94371 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa486ad4-6d1f-3c56-9cd0-5ffe5c0d9721 | -3.34372 | -59.86617 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d54e6ced-67bf-343b-a06b-26813dd4aa7a | -6.7622 | -59.11449 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0952254-a533-34a1-a7a5-ba46224f9a16 | -2.86683 | -57.80083 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 42dbad3f-4aa5-324d-be5f-ee5a049cc047 | -3.68543 | -60.5765 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb4bdcce-053c-3a40-a263-beaa0f03d8ca | -4.34773 | -55.6514 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b0192b-a801-3106-8eee-d80379318304 | -4.96678 | -55.82884 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb1f8ebc-e4ce-3a1a-88ca-38b2415f85c7 | -2.604 | -59.76292 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa9e30d1-0214-3b75-9805-fc2707c63367 | -3.39612 | -59.52827 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d424e00a-2099-3168-9e17-bcc051523e6b | -2.99845 | -60.80261 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 332be9da-379f-3328-bb6c-4997d26487e2 | -3.40053 | -59.5244 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 404654db-4bc7-30ee-8698-a304fd34b5c2 | -3.29095 | -57.85585 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d452c8d8-7fa2-3275-959a-2f7b13ccb2b7 | -4.95778 | -55.82225 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9681e81-6d0a-3a05-8c51-a16fe89c8855 | -3.10565 | -60.71994 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4bfc2f-fd0d-3a1f-a283-6ed7183e82c4 | -3.06516 | -61.2924 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549edc2e-78a0-329a-86b2-22f45e7fc60a | -3.06972 | -61.28555 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56175a2c-1fff-3c8d-b3a3-6e5ba6507e5c | -2.93377 | -57.80346 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0202d9f7-a40d-3ade-b590-929317f175d0 | -2.53218 | -59.55297 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b68175e3-8855-36fe-b811-71db2dda21a4 | -6.09611 | -57.68567 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d559006-b2a7-3eba-93f0-0a1e5a265c70 | -3.19054 | -60.43196 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a2971c5-81ea-39f9-ad01-b03d2aa600ae | -3.38356 | -61.29502 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a00a126-9bc9-3990-a893-baa9a4696532 | -4.41663 | -55.24266 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a3e948e-d3fc-39d7-ac1b-c07bd58ed556 | -6.10447 | -57.62312 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a917b80b-1ae5-3e51-8fe1-eae21b619fcc | -3.07018 | -54.39176 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e60668e-2c67-30d9-9f7f-ec69e3f58f22 | -3.21153 | -53.95941 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df14f8fd-cf0b-31c7-bc42-f1ee336f589c | -4.41079 | -55.24766 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae6a81b-bfa9-3266-b72a-7e757104263e | -3.06289 | -61.28448 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ebe4bac-498e-39ce-a884-55f8cdd8f501 | -8.82738 | -50.4927 | 2026-09-22 05:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a796ca3-4efb-3bb9-9611-f11d2492e3ee | -3.06175 | -61.26921 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c90808a-85cd-3d14-af72-d246e2d72ad6 | -6.74165 | -59.07594 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| babe6adb-5290-31a1-b9f3-1a19c5c1ffd4 | -6.62532 | -59.92076 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec53dc44-aa3b-3e65-9351-c7762eca16ec | -3.3657 | -61.3415 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18372b59-b3b6-34c3-829b-d5dee8664674 | -6.4624 | -59.97415 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7aacfa3d-6652-31e6-88bf-602f9b723ff0 | -6.64491 | -59.91647 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef8e044d-5a73-3cc1-b3bf-125ad5630a5c | -3.45754 | -58.32076 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9837c150-fdaf-3d15-acd0-03b9d4e2c529 | -5.86955 | -53.65044 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b42c1440-86ad-3c41-a0d9-b2e5b69bceb4 | -5.66894 | -60.23226 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514406de-4368-3a13-8070-7cd40bac00a9 | -4.26003 | -60.0091 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7056956c-af3b-3f23-83dc-f5070e619626 | -7.24578 | -55.6132 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec20e748-901b-3e80-be44-bcaffdc0dd39 | -3.76364 | -59.47738 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a51064ee-0b42-3ca9-8688-e65a83c2a1e2 | -6.45655 | -59.98742 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bdbf2e7-3ba8-3ced-8340-5ffda8563eef | -3.07319 | -61.08462 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17be8b48-d9a3-390c-b105-1b49333f73ff | -6.91947 | -59.62747 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61676bb1-88e7-3473-8058-99dbcddc27c6 | -3.54178 | -58.68876 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0433f0f4-e2e3-38ce-85f2-516260ebaedd | -3.50801 | -59.57882 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e658bfae-4788-30eb-a979-ce6256ca69ad | -5.85019 | -52.03183 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1275113-1117-311e-a833-d0a9dd84c3ec | -7.24116 | -55.60907 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92a317f0-51fb-33e2-a85f-d721ff9ff40e | -4.47848 | -55.48755 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e812f1e9-520d-37af-b66d-88d742bbe751 | -6.73563 | -55.09569 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2326b1b-c1ac-31dd-9dbb-2a25c29ac18e | -7.23694 | -55.60211 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f19aa465-ea84-3bfa-8aca-dd7b4c0cfa90 | -8.26273 | -55.26759 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8153b5b3-0ea1-3b68-88f1-e8ba511167aa | -6.06534 | -57.87027 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2431113-ada0-31e3-9a05-870e85397013 | -7.60853 | -55.35957 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21c7c76-9fc4-3ec6-bc1a-addf960bb427 | -2.65337 | -59.68702 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ff7b671-66a3-3e6b-a988-feeb357a3ae1 | -6.19501 | -57.77963 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a195c062-0181-34ea-a133-f89a2803101d | -3.71782 | -60.57632 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9192eba-947d-3845-a52d-212a497a7379 | -3.69021 | -60.56911 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18012344-72b3-35d6-bd58-5e357b03a810 | -6.37881 | -60.01509 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d607edc-6476-3b3b-bfc2-9cd3664c1128 | -6.61774 | -59.91963 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |


[Clique aqui para ver as próximas entradas](README112.md)
