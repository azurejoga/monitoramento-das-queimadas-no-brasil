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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 433faa85-c621-3298-b3f6-0900a24d0e0c | -11.15149 | -45.0471 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90695d4c-9fe9-3f99-a74a-0094b9db1fdc | -6.95026 | -56.5173 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 199e452b-94af-3c00-9785-ad4a8eef0da9 | -9.0662 | -60.48521 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bc472e8-db25-326f-882b-aa39dd4aabee | -10.398 | -48.23374 | 2026-09-01 05:16:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a940a4db-af33-3142-8e36-2c32f8906763 | -6.02123 | -57.66928 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66ea912d-8456-3ce7-b71b-410da55699ba | -8.62622 | -54.85581 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 523e23f8-4a41-31ef-8d7a-8cde471ec495 | -4.77357 | -41.79926 | 2026-09-01 05:16:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ef5907c7-0b42-3047-8912-f8c316c7c87c | -6.88686 | -59.41022 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 960f4cae-39b4-3e1f-8807-5368834180e0 | -8.93268 | -62.36004 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a67a3c5c-582e-3bff-ba40-5842329abe1d | -5.24971 | -55.90763 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1a3a542-02e8-37cc-8971-ae35d02a8ea6 | -6.12637 | -57.69395 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 198c2069-a445-3669-9404-1c141f621983 | -8.27378 | -54.92456 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6dfe1f69-57ed-3910-85e4-4982d80e86f3 | -9.46868 | -57.02279 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f8bd8d9-e3d9-365e-b744-19eec8b7561b | -6.94796 | -55.63352 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 411e4908-52c2-30c3-887f-1db338c718cb | -4.96428 | -55.85197 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1a2f5e6-a8d2-395d-95e9-5f3444116680 | -5.24362 | -55.90312 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55256910-391d-389e-9a5d-fb887bb128d8 | -10.82886 | -50.71175 | 2026-09-01 05:16:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39e3d226-6871-301b-9b77-613ca2235fb0 | -3.61433 | -59.07496 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 854fbf49-98a8-37bb-877b-b89778fea3bb | -10.15827 | -45.7465 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 736ef334-14c1-3b32-8c3d-442a911290dd | -4.92657 | -55.76796 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4f81dd1-4c98-3fe4-9c52-48843c0e9e97 | -8.1332 | -45.57711 | 2026-09-01 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 463a9caa-a852-330f-9456-ce159c865b6f | -10.74502 | -47.98611 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a9f6b74-527e-308d-b0ae-6c73f838883d | -6.1207 | -57.68542 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fa2673a-198f-3463-aeb7-e5e9cf7d5244 | -10.75584 | -47.98503 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb80f261-d1a6-3a86-aed1-0ade0ef26c12 | -10.16184 | -45.76694 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1dfaff6-1aa7-339d-8336-00d75caa68c6 | -5.24639 | -55.90711 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e4d23a4-b9ab-3c81-9337-7c57c1fc110e | -6.5138 | -55.23661 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 807807dc-073c-3aa2-8870-7e642bc0559a | -8.79773 | -62.50939 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8183888-9e82-3880-8d4f-921a7ded93b1 | -8.78918 | -62.48237 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e18ff0d-2f8c-37e2-b8da-b3cd4ceda297 | -8.20845 | -54.94418 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85b8d5f5-245f-3049-a5bf-db9f8d5b6162 | -6.15331 | -57.78169 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abacb5b6-76cf-353f-a1fe-bddf407113cf | -7.34012 | -60.59017 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7a40614-b425-3332-b47f-8b303cc35ef9 | -7.29024 | -60.57632 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4ca0fb7a-a5a8-37ee-91a7-d2c949319e5c | -6.78434 | -55.63999 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d6495f4-353e-3207-959a-9c2d8deb4de3 | -6.93134 | -55.63089 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53472fd5-6a1a-321d-945b-008504718502 | -7.86844 | -63.75219 | 2026-09-01 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b15b215-2288-34b2-b9a2-ed28cef36291 | -5.98244 | -53.61469 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c2398e-7113-3769-b69f-cbeb86c47503 | -6.93411 | -55.63489 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5abcf34-bc97-3ead-a05b-39637fbb6b5f | -11.31173 | -45.1958 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62102578-0229-3afb-9cdd-be8cafde3fe0 | -6.35136 | -44.09498 | 2026-09-01 05:16:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1150ee9b-87c8-3a04-9881-f9a08de90d3e | -9.48416 | -57.02577 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2138c9f-676b-3a40-82f3-ca691977a54d | -7.34492 | -55.19705 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0ae3fe-9556-3abb-9097-b5604b00e67c | -6.72246 | -50.46359 | 2026-09-01 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f31e68a-45b6-374d-b6b9-9ef4919fec7c | -7.28282 | -49.8331 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6e23252-e01f-352f-9e84-1e0254df341c | -6.56775 | -58.56069 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89c30eb6-4997-3c48-ae50-e6267b3377ae | -7.28846 | -49.82518 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06d87790-d647-3da3-b06b-d5205d232c11 | -7.57374 | -60.46388 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bba5b402-6b23-3baf-a481-a8d3e3989b04 | -7.04606 | -51.33828 | 2026-09-01 05:16:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14eaf9de-6982-3c0b-a870-92f5c094506f | -5.4805 | -57.14755 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c49a4733-4360-3089-8bfb-de2de65bdc08 | -11.51682 | -46.92889 | 2026-09-01 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a21065a2-11c9-3b54-ace2-c9bacdbe3928 | -7.05598 | -52.7197 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3376e292-a5fd-31ec-baa0-a7a8f9638d82 | -8.04214 | -61.73282 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b853519-fa8e-393a-bbf5-ef82fdfc42fb | -5.89619 | -57.75681 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78a18c86-ba24-3ff7-ac7a-7a84864fca27 | -7.5709 | -61.37023 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b15e3a9-7de9-3462-95a8-85ffd7fa2ece | -7.63096 | -55.2887 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bdc0ac0-55f0-33ad-bd49-8e303e7fa87b | -8.69162 | -62.93794 | 2026-09-01 05:16:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b017321-345c-314f-9496-c389d9dcdaf4 | -5.73581 | -43.28178 | 2026-09-01 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b02e9f15-fc66-3ad7-a299-a679ce8fe90d | -4.15721 | -60.72805 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77ec0bcf-4276-34d2-b339-524559a9a29e | -6.92801 | -55.63036 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9e1c52-c9a2-374a-b946-04e214ae6aa0 | -8.12461 | -54.9642 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8334f484-47be-3cce-841e-48edcc5b13ff | -3.55484 | -59.03752 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e387d58-3240-35b5-b281-16dd767c3ae3 | -10.78563 | -50.50498 | 2026-09-01 05:16:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9863ec98-e6cb-33c4-827a-d10a25184a8e | -4.38325 | -55.16096 | 2026-09-01 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b41c74f-8a52-300b-9f97-94f4b109c4e6 | -9.18204 | -59.45941 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbbdbfb3-c2f0-366e-ac0c-c5a0fe90e010 | -5.80514 | -43.64495 | 2026-09-01 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ac32dc5-33f4-35be-a115-ab151653a79c | -3.36702 | -52.12183 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0efeb396-2b09-3c15-8d2b-f8c280c38424 | -6.18239 | -57.73287 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fe6de75-f7ad-3bcd-942d-36fed7e9ab98 | -4.79857 | -55.97873 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b94935db-d858-3706-9b48-5595bcddaa96 | -6.25558 | -55.41373 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cb01d7c-f9d7-3a75-a34d-4f85c886995e | -8.61661 | -54.85056 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b565be0-38ad-3fec-8f2b-554a9e968fb9 | -5.87758 | -57.78462 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d111b3-d544-31a0-8d0a-75364622565f | -9.17683 | -59.6319 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c49e8a27-f49b-3bc4-b312-6d16de5ad07f | -6.01837 | -57.66867 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84abec20-966d-33e2-9f93-35f257608f03 | -7.68394 | -55.34404 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 074ef736-1f67-3f3a-9656-bc56e4a4d9bc | -7.56987 | -60.46326 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53f943bd-68bb-39b9-bff1-377da27990ae | -7.62316 | -55.29471 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 415ddab9-1d6d-316b-8aed-47cbeb6eea3a | -8.49991 | -55.31195 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ed05ba-710e-398f-b9df-f62ef175223e | -8.90144 | -60.58433 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90d8ce9f-e265-3a3b-937a-7a94955567bc | -7.03621 | -59.22758 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfa6496f-8820-3178-8a52-687d7a7710cb | -11.25097 | -45.14301 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8d26b66-5452-3f4e-8873-9512a0859c46 | -8.6234 | -54.85162 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5b19eef-9294-3950-a5e8-1272c42c15c1 | -8.27435 | -54.92089 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ecde170-f460-357b-96e0-e0d7985dc720 | -6.81134 | -59.56788 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4feee7cf-72a7-3c79-9b96-30ff40dd84ea | -6.75895 | -56.33703 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc7f6c63-0890-3390-b049-c37474e91f3b | -3.50983 | -56.31643 | 2026-09-01 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df9bd14-555b-393b-badb-ba19d39d375b | -10.32863 | -49.95251 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fea0035-f170-3642-990e-53a78c6993e2 | -8.77407 | -46.45223 | 2026-09-01 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c776974-21be-3f01-ab03-e93c05780e90 | -6.1553 | -57.40408 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbbc2537-8a8e-37ca-a3a4-8128471f59ad | -7.57629 | -61.3334 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f01f498-76fb-3956-a552-cc2e68bc13a4 | -8.26928 | -54.93126 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e8a05a95-b448-3998-ad4c-16b7a7ec45a7 | -8.50327 | -55.31248 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2dbd92-09c6-325b-850a-f5c7b5785031 | -8.94306 | -63.29996 | 2026-09-01 05:16:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 53e0dec8-1fb5-3d2b-8e58-90a8547f4466 | -7.34882 | -55.19406 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb718f5b-647e-3a8d-b02b-5558feeff455 | -5.95581 | -57.68533 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 106d643e-483f-318b-a982-01a5a1bffe29 | -8.50382 | -55.30893 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5219ac24-b3f7-322c-a9dd-a6853846a89e | -6.37226 | -51.7581 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32bd8db4-4d97-356f-b7b0-ad18824d4c61 | -7.48347 | -61.38884 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 121c8e44-f4e0-327d-88ac-7d10cd779694 | -7.5721 | -60.47366 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| be65248f-64fb-32fb-a4de-909b6321b421 | -7.34487 | -60.58578 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 06441868-954a-3ba8-8a8b-2eda9731394a | -6.26778 | -55.4228 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
