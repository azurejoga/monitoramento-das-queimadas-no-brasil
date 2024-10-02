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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3e13316-01bc-32bd-9d95-f91e42a4981c | -9.19852 | -58.20621 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ec58eb-5877-31f5-81c2-efa335ee2b51 | -9.19797 | -58.20971 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90e631e-c7bc-3c0c-be3d-eb5bb288bf84 | -9.1963 | -58.19868 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e8ec7a5-c99e-3dab-a3bf-fe7b37ca09b8 | -9.19575 | -58.20218 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e05a681d-3a58-3051-a945-94d6c4462a55 | -9.1952 | -58.20568 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f317a179-9447-3464-9b56-6e28fe85fe5f | -9.19243 | -58.20165 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220dc364-c9de-3743-bd58-6c58d695a8c5 | -9.19186 | -58.18362 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3011113b-7032-3b5f-996b-6cb17c01682f | -9.18909 | -58.1796 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23aa2a6c-209c-3eab-a926-0d8b575ea67d | -9.18854 | -58.18309 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0b320e3-3c48-3977-8b9e-13baeda32070 | -10.72225 | -58.5158 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63677837-f7ae-3c66-9e29-f2ab11d732d4 | -10.72114 | -58.52283 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b010c2-7490-3d49-b924-c2919da4d9ec | -10.72058 | -58.52633 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a177efb9-e1eb-3057-ae1a-55004496d2ff | -10.71892 | -58.51526 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e862f65-3aba-3980-85e0-822edc114b06 | -10.71837 | -58.51878 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f2817f-1ff7-37e2-a609-e0e6a0059fbe | -10.71781 | -58.52229 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fecb473e-0853-312d-9a47-1372894a33c4 | -10.71725 | -58.52581 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc4b8ba0-e90f-3e24-9090-3b4e2a4e9eb5 | -10.7167 | -58.52932 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 867d3236-974d-35f1-bdda-bdf954531934 | -10.71581 | -58.51791 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fa92591-c802-3a16-bdd8-0c8471c477a4 | -10.7147 | -58.52494 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e760a4b8-8328-3f0e-b717-bd6def5399e9 | -10.71415 | -58.52846 | 2024-10-02 05:10:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3075d059-2dda-36cd-870a-87285162f505 | -10.33385 | -58.47132 | 2024-10-02 05:10:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 975237c5-ea10-32f2-be6f-03a5ad656f2e | -9.96702 | -59.60469 | 2024-10-02 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb44cb57-92f8-3853-b1aa-aa9ef6618082 | -9.71265 | -58.44317 | 2024-10-02 05:10:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c5916e-3533-3a06-afc9-06920dc0de4d | -9.70932 | -58.44263 | 2024-10-02 05:10:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7398cf2d-a7fb-34ae-86e1-d7a46ab0b8f2 | -9.70876 | -58.44614 | 2024-10-02 05:10:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 314c5260-ce3d-3397-8822-3b7747bbdd99 | -9.56971 | -59.10247 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f15243d0-58d9-3e46-9950-70daa082c34f | -9.56635 | -59.10192 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba956cf-2357-351d-922c-25553af0a7b2 | -3.17369 | -58.96585 | 2024-10-02 05:10:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a0554ef-f0c0-3d15-98f3-4857b65ead34 | -3.1733 | -58.96657 | 2024-10-02 05:10:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5fb4820-176b-37e8-9513-8b9021189260 | -6.98608 | -59.93639 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa2b093-c6e2-3bf0-91b6-00b19941ecdc | -6.95625 | -60.14305 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9896470-1047-3e78-86a3-d7b5dbdd6475 | -6.95335 | -60.13845 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ff46de-d41e-3198-8d5f-6a2fc5cd3740 | -6.92176 | -59.99845 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f335f58-47c1-3151-be71-435bc5b33f8b | -6.91824 | -59.99786 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcfb3314-a9df-32f5-8873-c1db6176fcf9 | -6.83027 | -59.78786 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a799f8-4d88-3653-b5f1-2c76908e3ce6 | -6.82937 | -59.78861 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a077f901-169d-39d2-bfff-a037ca44a90f | -6.71893 | -59.12412 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b3fea61-076f-3c1e-835d-0d29ff18aec0 | -6.71834 | -59.12781 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc220fb-68a5-34f3-aee1-f6d05aebe176 | -6.71775 | -59.1315 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f740584-8352-38f3-a7c8-f5a1209c219a | -6.71551 | -59.12355 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091ae367-c980-3232-8ad5-e6a5fb994862 | -6.71492 | -59.12725 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86c26424-8c9e-3a79-b2a3-791201267add | -6.71433 | -59.13093 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b98167f7-5500-3620-b4e6-27d1c704c99a | -6.71151 | -59.12668 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 285c627d-03c6-3999-9dcd-e3c94cffba77 | -6.71092 | -59.13037 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 427b16a0-aff1-3c66-bfd2-07c134fa1445 | -6.7075 | -59.12981 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b4a1ae6-e5ee-3d88-a595-6585fe5fde2c | -9.85063 | -60.73854 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ddf637e-d97d-3c48-9022-32efbb6df3b0 | -9.84997 | -60.74252 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f74e9ae-0c93-3e4b-9ee1-846316ea5a64 | -9.84931 | -60.74651 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c71481a-909f-37e1-8635-cf35603b3169 | -9.84643 | -60.74192 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c64fef-1182-36f7-a98a-c58bf893d99d | -9.84577 | -60.74593 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a239ef60-0270-371b-9c60-8713205fda28 | -9.84398 | -60.77858 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77c69b22-765b-3f81-8845-b67612c342a0 | -9.39542 | -61.04769 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d65aaba-fbb3-32c5-95f2-27905a2cd65a | -9.39473 | -61.05186 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 272adc78-5dff-33ab-bbfc-cca213824086 | -9.39181 | -61.04709 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00492818-45a0-3f82-81a6-4317643cc782 | -9.39112 | -61.05125 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f22af85f-204d-3244-b8c9-0dc961a1b41a | -9.93216 | -59.92902 | 2024-10-02 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7cdbf88-3610-3bc8-bb2d-e9ad08f01489 | -9.92873 | -59.92846 | 2024-10-02 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ec28686-d0fc-33a0-b832-a1d5c4c3f546 | -9.92551 | -59.9049 | 2024-10-02 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 675b89d4-5e19-33b4-9a30-605a08dfeb94 | -10.19239 | -61.30916 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 653d1a18-af27-39e7-9512-1c2b6b780675 | -10.19168 | -61.3134 | 2024-10-02 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94042c41-a331-3cf9-b494-a0d1538a2a9a | -3.18616 | -60.54834 | 2024-10-02 05:10:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52adcc58-5a06-3b3d-a274-bcd0f2cb3c26 | -7.836 | -61.33486 | 2024-10-02 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e69ae38-0868-3f60-b95c-893692b26129 | -9.27762 | -62.16696 | 2024-10-02 05:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6121faf-3ca6-36ec-9b9f-c58f2e511b4c | -9.17754 | -61.89408 | 2024-10-02 05:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e639770-95a4-38f8-87ff-b23c9fc2ffef | -9.14301 | -61.26437 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478d4ad6-2a10-3c74-bbce-7053b77f097c | -9.1379 | -62.41953 | 2024-10-02 05:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efe2d89c-b68d-3097-ba73-d9eefac5f479 | -9.09373 | -61.13527 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea60e760-d484-340b-b518-ef24b762b11f | -9.09009 | -61.13467 | 2024-10-02 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8350bc2b-57c9-3b4f-bf7a-778e6ad2f1e5 | -9.0814 | -62.35225 | 2024-10-02 05:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9036c4ad-b0a1-3bdc-9077-3a1117e7a08d | -8.95003 | -62.39345 | 2024-10-02 05:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66ccb6ba-9ad8-3de2-a375-1c74004b8c24 | -8.67298 | -62.51204 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b815fe66-4a4b-3fda-97d5-7ba6c7e473fd | -8.58457 | -62.42168 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fec401b-1ec7-399a-8750-34286165ee0d | -8.58064 | -62.42098 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 767b58f1-4187-3732-8200-fa1d199208d8 | -8.56238 | -62.48008 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecd2c2ec-f941-3870-a2bf-11f89b7a269d | -8.56151 | -62.48514 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c071c2aa-be66-3001-986d-f7cd1124713e | -8.55919 | -62.48281 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67d3fa2b-e370-3ada-a612-37585f59530e | -8.55843 | -62.4794 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb39c7b0-5f89-3be7-a6a9-5dc8d9c9da75 | -8.55756 | -62.48445 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f47b63-950d-38c6-be91-8a922e3ce41b | -9.5128 | -62.45547 | 2024-10-02 05:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa4dd797-c6bd-39a7-9c52-6e8df3acf52e | -8.47741 | -62.70307 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca0a002-d9dd-3b01-a109-c591dc212baa | -2.88498 | -61.87498 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cde17eea-8a73-3595-b6a8-1bd65620ba70 | -3.03342 | -61.6734 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c05ae1-2d7b-386f-954f-fc1c1826e5f8 | -3.03284 | -61.67701 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8520bb2a-553d-3365-b13a-791dc2804e41 | -2.88438 | -61.87868 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62c2e9d1-38eb-3e9c-b0b1-ff5a13b57d5e | -2.88379 | -61.8824 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 260856b6-21bb-3f88-a998-3defbf9e228b | -2.88024 | -61.87804 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8823a6b-b7b3-30ec-b0e9-a6560b64b04a | -2.87964 | -61.88178 | 2024-10-02 05:10:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f13f94ae-03d7-3454-97e2-8d622fd33a2b | -8.7808 | -62.82836 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 645e4976-bcf1-3dca-ad72-068775706247 | -8.78021 | -62.83189 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0000bf5e-a3bb-3433-b777-b96b42573688 | -8.69964 | -62.81432 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef0bced-2c9c-3c7b-aa38-7e043f26b4ea | -8.69905 | -62.81785 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e72056e-bd0d-3421-b8f9-c9951b7301ce | -8.69562 | -62.81362 | 2024-10-02 05:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 123ba9c1-333e-3820-adb7-ae048ddcc6b3 | -8.48944 | -62.70512 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 911fb075-3fc7-358a-9fb1-ef923c7cf076 | -8.48543 | -62.70444 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce002da2-3a91-34ca-b1ec-86afbc7c2c5d | -8.48484 | -62.70792 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30b6c246-4ac3-3234-99a5-17a17235841a | -8.48142 | -62.70375 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974dbc5f-7db3-300f-828a-67167a275a4e | -8.48083 | -62.70723 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e500564a-1dd0-3f2d-bb29-907431488fde | -8.48024 | -62.71073 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2291c005-d72b-3732-8049-3d889c89ca71 | -8.47623 | -62.71004 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 372be232-77a7-3f28-aa22-6366c7afac29 | -8.47564 | -62.71353 | 2024-10-02 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README134.md)
