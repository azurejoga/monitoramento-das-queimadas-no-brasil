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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86a7647-ce43-3152-bf04-2ce611f65301 | -10.27422 | -50.41552 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76dc691a-0d0e-30f7-8b1e-a67b0db67b2a | -12.76537 | -48.43353 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bbec8bc-9f8f-303e-9354-e55f3bbdfca2 | -11.33535 | -45.9226 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b22939-471d-3ce8-8278-eaf0df62701a | -17.97897 | -44.43964 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f974bcc5-8605-39cb-a8d0-5da4c9d0d7a5 | -10.28005 | -50.44673 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1da2f317-f72a-3925-9df4-d58e9abf9f7a | -11.24292 | -54.0178 | 2026-08-18 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c46d9a21-c236-343c-bb74-9e282aba0716 | -14.17205 | -52.93216 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| feabf84e-a24a-37a2-a41a-daec82359ac1 | -11.12992 | -46.48956 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf33a618-a814-3de2-bb25-6caf2348a7a3 | -14.17814 | -52.93592 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0ec55fee-9408-32de-98c6-af7fb7af2441 | -14.03233 | -53.67672 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2250ede-49dd-3067-8d6d-9aa5c36c94f3 | -14.03095 | -53.68447 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24e9b93a-6fc8-39e7-91e8-ef02c4ebe689 | -16.69324 | -49.33661 | 2026-08-18 04:40:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ef7eea0-2357-3951-875b-d655f38d3c9c | -13.79009 | -53.84495 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c49e9e43-0adb-316d-9566-75153e21fde0 | -12.46055 | -54.19069 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 742625be-d17c-3291-83fb-e263f06677be | -11.13327 | -46.49012 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa747dc-d1b9-3eaa-9dc5-5491a069e231 | -15.23086 | -57.64949 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 575fd6b2-48cf-3053-a160-0b0659ebb929 | -11.12313 | -47.2717 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 15234818-6f99-3a94-8c19-efcb4208c4e5 | -10.56215 | -51.97293 | 2026-08-18 04:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e6d645e-c369-3dc7-bcc0-2b81b3b89200 | -14.17682 | -52.8985 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b54f378b-d8b3-3376-a8d8-187bd43768b1 | -14.33335 | -51.95598 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73ca60d9-396a-3f43-9e4c-9f74ba63e6fe | -12.46336 | -54.20008 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4b82f2d-ad06-358e-99d3-14073c914971 | -14.35511 | -51.92596 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05dee0c-011b-3676-82cb-4e40466e814e | -14.18079 | -52.92855 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab049f6b-392a-3440-9086-0303b8d1e8ff | -16.39074 | -43.7033 | 2026-08-18 04:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c8f4cff-df79-35f4-8caa-075093706ce4 | -13.56833 | -51.70099 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3058d39-70c8-3766-8c5f-0cc1988417fc | -13.43845 | -43.84083 | 2026-08-18 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 463f4291-1ba4-363e-8ca1-ebb8034dbe02 | -12.05173 | -46.45704 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceaa1c4c-b23f-3b1c-ab7d-69393ed6093b | -11.12258 | -47.2752 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 196ddf02-96ab-361a-8522-e53ac97f0720 | -14.86442 | -49.98247 | 2026-08-18 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e33f4fd7-93cd-3f68-8cd5-24e756f37985 | -14.16901 | -52.89691 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ab2bed0b-a32d-3f87-b19a-d7d32e9a1b96 | -14.18111 | -52.94194 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed082b2c-987a-330d-8e05-ef134514f7d1 | -14.4199 | -51.88257 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad672cd-5963-3c73-83c2-89aeebeaecc7 | -14.81862 | -46.63107 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 71e8f2bd-dcaf-352f-8298-fe3d5006eae5 | -17.9445 | -44.42888 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0267028-a435-367a-97f6-132cf7eee59c | -13.56409 | -51.76949 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a460093-2013-3fce-8df5-01c91ea6892e | -9.42254 | -60.42524 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e95726-7b80-3a3c-9ef0-6d97518d98bd | -11.13254 | -47.27683 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82b2ab24-a6db-329b-9d90-32b99060a8bf | -11.38779 | -46.39797 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 414f6b03-ed08-323f-b35b-6279880e94e7 | -14.16961 | -52.89979 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26844fcb-02ed-33dc-95ce-f525a3f54ac0 | -14.03303 | -53.6728 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93674ffc-7e4e-3494-accb-59386f4a4fb4 | -11.20332 | -54.81375 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63b9cc1d-db23-35c8-b1a1-1e87828676d5 | -16.24213 | -57.65755 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b8e08cb-2590-30bf-b0eb-f65991a52f4f | -12.46651 | -54.18294 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae663b0c-61f0-346d-b9e8-1df557fc4c29 | -13.59056 | -44.81359 | 2026-08-18 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff93458b-7579-3762-b170-3c0cae1c8cd3 | -14.17514 | -52.93008 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d889eff3-65b5-3906-9957-3d65f6cb710a | -17.45653 | -47.85655 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23f326b7-7075-39be-9f6f-edb0a550cd0a | -13.64746 | -46.24113 | 2026-08-18 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68f0bdc0-261b-3f69-abc2-5d8c5001cb95 | -13.41394 | -54.38219 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f16a6209-5dbc-3fa4-86e9-74ab7bb34b50 | -11.52111 | -46.63584 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a72f8b05-5b45-3bcd-869e-dcc69b6a81fb | -15.22497 | -57.6516 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d0d334-e4d6-3242-98cc-5b0f5fd75540 | -11.38835 | -46.39432 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf32b79-41df-3e1d-b49a-6257eba83d4d | -13.93408 | -53.93518 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1e4c7ba-1723-3f4a-aa33-04893a4eb9de | -12.26429 | -51.54059 | 2026-08-18 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d04d398-0fa5-3091-825e-bb1d0c43a671 | -12.94632 | -56.64585 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 274d2bbe-ebe3-32eb-b0cc-75edc88dcfb3 | -15.26075 | -56.50182 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b89b24f-389a-3cc8-8bbe-b8744c03ec32 | -9.15951 | -59.67371 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32f1390-653c-32bb-bd89-87deb5d400f6 | -14.83561 | -46.63422 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87da7f24-d804-33c0-ab58-c6f43c66c197 | -14.43388 | -51.88976 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c04cdb68-f5a3-3e92-a09d-e6ca9a3bb10f | -12.52417 | -47.89275 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5039083-cb38-37da-a41b-b23d0581a101 | -15.22677 | -57.64709 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2fefe2-c455-3e2b-a123-a701453d1076 | -12.26507 | -51.53613 | 2026-08-18 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3539c46-0d52-30d8-b0aa-d4d9b67fc8bb | -10.27423 | -50.41226 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2dec935-e191-3646-af14-be55faef72dc | -11.45523 | -46.57404 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56137342-ef2b-3183-9fe9-d94644decf65 | -11.11998 | -46.49936 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c32c96bd-82b8-3e2c-8368-e042f44aa247 | -14.17398 | -52.91415 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0f35cfbd-bc12-382c-aaa8-a957d7ee6208 | -14.44097 | -51.82664 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c46e96e2-b5a1-34c3-a8a0-222dc9a61edb | -11.11381 | -46.49484 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 029247c3-b97e-3609-a0de-25878e9c12f2 | -12.7022 | -48.51495 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83d31049-d6a5-3aa1-8e3c-b04b2365da94 | -14.171 | -52.90821 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9df8005f-c1da-378e-8408-ba82ec350bb6 | -17.97966 | -44.43454 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e37985d-4957-3d24-89f1-c10ccb3ace05 | -10.27353 | -50.41646 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 731032e6-68c9-3666-a67d-f015d1613b93 | -10.27062 | -50.41164 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e325ff5-6a11-39ea-bdcf-d3dfe8435adc | -12.46493 | -54.1915 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92303cde-d020-3a81-90f9-ee78f0c3fc1f | -13.25519 | -51.65403 | 2026-08-18 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86b37b45-dc5f-3e27-9970-84b171ece63c | -15.0841 | -48.69207 | 2026-08-18 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acdd18ad-3e89-3602-8ff2-8154f6f54796 | -16.24141 | -57.66114 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c336abbb-af29-3d00-9072-a8eec2b002ec | -13.01823 | -56.58711 | 2026-08-18 04:40:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bed43aa-1155-3e93-822b-90ded06ee190 | -14.81351 | -46.6418 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f55d6dc6-abd1-33c1-8bd5-014397cf2d1f | -12.22682 | -47.03226 | 2026-08-18 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7490ff2b-c9fa-3c1e-967f-7e91035beb29 | -11.12267 | -46.49208 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b345dd35-5ab3-39e4-a7c9-b1f99a7aeb1e | -12.46572 | -54.18723 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65d50fa9-2d3a-3c5c-868b-7bdfc7922b07 | -14.80954 | -46.64499 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5fe8714d-a566-386b-9fc0-bbf64c1be3b2 | -14.0407 | -53.6863 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d94ca1-34d2-3ea1-b5f6-c6f5920cfe44 | -11.36481 | -46.39076 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a1d4375-5865-3878-a40a-21bc30a976b8 | -14.36273 | -51.8735 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dd228e8-72b7-361e-8a78-b765248e3360 | -12.71345 | -48.48752 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9153cc0d-c946-313a-8381-70cc3f0ca99d | -13.40395 | -57.05006 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ed1a26-9b11-359e-9a4b-17ae2a80843d | -11.85738 | -50.18245 | 2026-08-18 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3678e15-b61a-395f-8ccb-b1c75febab41 | -17.98747 | -44.43583 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac4ce567-a9c1-372d-8428-353c145f814f | -10.77065 | -50.37186 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e16a54d0-2591-330f-b943-84e16a5e98fa | -14.45784 | -51.83886 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0561582c-272b-3db9-abb0-72bcbf4e7769 | -14.17382 | -52.92205 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6d96f25-a731-391e-b446-4ca2268c4390 | -14.179 | -52.93883 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b02e8b4-df7b-3517-bb82-208bb568bf29 | -14.63363 | -47.2726 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05065657-d42d-3a03-9287-77084ba3801b | -14.26842 | -51.9117 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eab86ad5-cfbe-3751-86bd-0a4c716912bb | -12.52529 | -47.8857 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffb276e-cc1f-30ce-8667-b604784d0ac8 | -13.55725 | -51.69897 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cbc7fac-6c31-385c-bdc4-954233d7da9f | -13.463 | -51.7948 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0640f95f-2ab3-3396-ae20-8c3457bc0c1c | -13.56541 | -51.69585 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9d5c758-4114-3ff6-a0bf-611e4e4cca6c | -16.23319 | -57.64896 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
