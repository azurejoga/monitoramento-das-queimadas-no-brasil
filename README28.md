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
| e550a93e-37fb-349b-ac3e-7844bfc6c219 | -12.02573 | -47.78337 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8705c9fc-7af5-3947-a702-6e8e0fe6c85f | -9.02125 | -61.22189 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dbed2d5-2ea6-3b62-a1f9-a7fd27f246d8 | -12.0225 | -47.7797 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec99d805-4c88-3c74-a68e-d3caf871a4ba | -9.015 | -59.53726 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9b3639d-a330-30c7-aaf8-391d85395278 | -12.42247 | -50.04709 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1f69f25-9732-3ab2-9333-a6ea5d7a05e8 | -12.49854 | -57.78504 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0ebd273-cf41-33b4-8a8b-4750e109b35c | -11.88231 | -58.71502 | 2025-07-17 05:14:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0403c72e-7ba2-3ba2-872d-2bd283f8986b | -14.65882 | -53.11273 | 2025-07-17 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70219f3b-d5db-3064-8df4-91ee63d04ff8 | -12.41215 | -50.04572 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 379d781e-1721-3926-8385-be9c94f3d729 | -12.99174 | -44.86604 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f0ce05-aff0-368a-9732-f6f4b790923b | -12.49334 | -46.9185 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db97f70-b0ee-3d10-8762-40c36e5de39b | -12.41845 | -50.03714 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e634cd2-e4cb-35df-a757-98116f28e852 | -14.95911 | -56.40115 | 2025-07-17 05:14:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71477fe4-994e-3d2b-bfac-e308c6fb99aa | -12.42285 | -50.044 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5dcbf418-9dc7-34bc-97ef-1701c0eb7f5f | -9.71201 | -61.28982 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7428a5f0-24ca-3251-b40f-434c4805614f | -9.16132 | -59.71188 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c9b2b31-ceec-3d29-9d47-f52d9c92e334 | -7.90154 | -61.52164 | 2025-07-17 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 128a9eac-d8c7-31e6-8e35-19913bd5f6ef | -11.87395 | -55.4507 | 2025-07-17 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a5d08cda-ed02-3627-a2d9-2d7e3e3ceb97 | -11.87442 | -55.44977 | 2025-07-17 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 1a6a8e14-5991-34fa-b74f-52da680e0cdf | -9.01161 | -59.5367 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f2dffb-e8e6-3954-b3ff-69c3a14e8b39 | -12.70327 | -46.80702 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef4f279-8180-35c0-835a-bd88e3442503 | -9.01677 | -61.22454 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 453fa1c7-7f68-3277-b569-593426b0aa7b | -7.48824 | -63.81524 | 2025-07-17 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 428cf66f-53bc-30b9-b3bd-4fbeca6077c7 | -11.52765 | -48.95699 | 2025-07-17 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c4b0cb2-67a9-3d63-afa1-4becb29a12c0 | -8.76507 | -63.8253 | 2025-07-17 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3232ca40-4879-316f-8e43-d9cc0f686132 | -9.1614 | -59.71125 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 801f92ee-23c8-3256-a7b2-615ff9522fa4 | -12.47778 | -46.91558 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf366585-6cd6-3a1c-9a75-1b1e143a064f | -10.67603 | -56.54739 | 2025-07-17 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8da0dd0-f259-376f-bf1d-de9e4d3bccf4 | -10.56514 | -49.13671 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6418a104-59a4-3608-a0b2-1a441251345c | -10.65934 | -49.47484 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e78122b7-9ed6-3724-a01f-3db2dab6c61d | -10.96588 | -46.47358 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 28b49d54-cc70-332c-8a60-fad9a659bb39 | -8.42757 | -64.03497 | 2025-07-17 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e90c32fc-ab73-3887-aa0a-fa76e3dc2b86 | -11.36041 | -48.73193 | 2025-07-17 05:14:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138a2a03-9eaf-3fa4-9b01-237b1ab2f588 | -10.2462 | -59.2719 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcc02f60-a4cb-3eda-b9af-a8b23c5d7c9c | -12.99965 | -44.87948 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13720816-c2bd-3e18-bf29-6ec5954ab647 | -14.32419 | -48.64767 | 2025-07-17 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf11f67b-790e-3542-a7c9-d910a52b8fe5 | -12.42323 | -50.04091 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6531ad58-1eec-30e2-a053-f1a690f46078 | -12.03225 | -47.77957 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a37662f5-90a1-359b-b069-fe4432eab27b | -11.94816 | -48.42188 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8382dd2f-4ca4-3899-b10b-867202b81439 | -11.10907 | -48.86369 | 2025-07-17 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db170d1f-cced-390b-b097-270ad44d5b57 | -9.02113 | -61.22091 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d26038a5-5fbd-3aeb-bb2c-f61202f855e0 | -12.4991 | -57.78145 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6cce3b2-e087-3283-883d-d4a11cb5119f | -10.65853 | -49.47855 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f8a4e48-3dc7-30c6-b8e7-ba82e5d13a13 | -10.97225 | -46.47452 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ac9ade8-a218-30b8-aed0-aa3609671c1e | -12.58338 | -56.98388 | 2025-07-17 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1a5f12d8-a2c9-38bf-bfce-0c231fbc9331 | -11.10861 | -48.8673 | 2025-07-17 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8db217-3f47-3c8b-9644-90f89857d753 | -12.41693 | -50.0495 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0a4dc03-4d44-3b63-a4f6-b612539756eb | -12.50487 | -57.77914 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b5dd9fe-6c09-3fb9-a5fc-5b304dde261c | -11.94688 | -48.42375 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 837373f6-04e2-31fa-b733-937c6415d17d | -12.0263 | -47.77874 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1ed63ee-ffee-3b1a-906c-99d8cf8f6e20 | -12.42361 | -50.03782 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 483f5574-990e-3765-8795-683de98ea635 | -9.16481 | -59.71183 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d68d592-8a8f-31a8-a4b4-cd70b93685bb | -13.00537 | -44.87434 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376113d3-8a4e-3376-8f81-32952f088226 | -12.02845 | -47.78056 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7bdb0d4a-66f0-3b94-ae5e-f3746ac28d87 | -11.11454 | -48.86456 | 2025-07-17 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e5ad17-2158-3442-a89e-7fa9a633d81e | -12.10411 | -48.19622 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0fcb506-c4df-316e-a086-ae67499e4576 | -12.4284 | -50.04158 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eeb66d2c-1691-3272-9fca-2b99fa9e7baa | -10.05009 | -59.10147 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81393177-a0b1-3635-90b3-0b4aebd5c23f | -11.24046 | -49.50436 | 2025-07-17 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d994be2-2779-321f-9751-4064a952e9fa | -11.36088 | -48.72826 | 2025-07-17 05:14:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66081117-8445-34b0-b71d-1fe8f3a78e86 | -12.48701 | -46.9177 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be6aedca-6821-336a-bd6b-c65fd01b0dd1 | -12.10438 | -48.19446 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b78e8f2d-9ff6-3d9f-b302-3da11d2779ad | -9.01692 | -61.22554 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c947f322-855e-3045-81c9-55428489543f | -12.70965 | -46.8079 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fad570b4-9898-33cb-b070-9cfdec2a27be | -12.49966 | -57.77784 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a852b12-bc22-3d58-ad58-c9beb866e700 | -12.37305 | -50.37468 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebec55bc-2e0d-314c-a7c4-e99a624a331a | -10.5647 | -49.14009 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68758ab0-9539-3be1-aaf1-2cdf2ea9cacb | -13.20445 | -56.63565 | 2025-07-17 05:14:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dd5c008-654e-3498-a82b-b071eb6b11b5 | -12.99812 | -44.87419 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97a2146e-43c0-39dc-a12e-9ac6d5492e4b | -12.41769 | -50.04331 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fea8c3e1-4782-3de5-af2f-ae254eb9314b | -11.94769 | -48.42589 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c918e66-cde0-36ad-bf3a-cbbaba5b9d21 | -13.01684 | -45.06204 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ef6091a-1075-35a2-b777-3965e3672052 | -11.94863 | -48.41787 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 262cb4ea-c769-3bba-b590-9b68b3b9c278 | -9.02477 | -61.22153 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d82804c-bc92-34ae-b8ab-52688f4c0236 | -9.02405 | -61.22575 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f18a0aa-df66-33cf-b312-9b9aeca5564d | -9.90013 | -67.01306 | 2025-07-17 05:14:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a72eda3b-2fa4-349c-87c4-5093a91e71ea | -12.40571 | -50.46886 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b197c48c-a852-344b-8d51-2ef344d4caa4 | -12.50711 | -57.78689 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e05c695-9713-3195-ab8e-4534ec7377cb | -13.00041 | -44.87205 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 797bcfe2-e242-3442-ad50-0db5a38dddd2 | -9.01781 | -59.54148 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8fb06b0-6917-39b7-a422-1306861d9874 | -12.99894 | -44.86667 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501571b2-8563-365f-89e7-f988a84c1858 | -12.50376 | -57.78636 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74546ca1-8abb-3bb0-975b-6fa81ac9663b | -12.38087 | -50.38208 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34d17be2-41ec-340c-b4ad-6934bb76e5c5 | -17.15966 | -46.1167 | 2025-07-17 05:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91ff03ff-d887-3336-83c6-b59f4f1912f1 | -10.05287 | -59.10558 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ddda57c-94dc-3340-96f6-a728fd96c498 | -12.50767 | -57.78328 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32531163-2b3b-3998-bb45-d6c56422f5a2 | -9.71563 | -61.29045 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f9a59ae-2e45-3249-9f32-fb4cb2e74ca4 | -10.89888 | -49.21491 | 2025-07-17 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4eff9e23-a2dd-32ae-b463-fe473b62b11c | -12.40422 | -50.48049 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 673f5d1b-ec81-3714-b3f5-6780cbef3d43 | -11.50485 | -48.96108 | 2025-07-17 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3434932-f121-3108-b470-f2916bec3537 | -12.58281 | -56.98764 | 2025-07-17 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 629d3654-ede8-32f4-b63f-9036742c2fc1 | -10.05678 | -59.10257 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb597c24-e4b3-3745-a713-726c9f1c6faf | -9.463 | -63.15006 | 2025-07-17 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81415f82-47ba-39f3-89df-5962af5f501a | -11.23602 | -49.49717 | 2025-07-17 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dbffa8e-7790-339b-97ae-0470f8254f60 | -9.02042 | -61.22514 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7088866-1eb5-3ec1-8846-0e4ac1e1c70d | -10.1097 | -58.22009 | 2025-07-17 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1ef34b1-4454-33f5-b135-31f8b2a35b9d | -8.42755 | -64.03233 | 2025-07-17 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adb29e5e-0e36-302b-ad58-647ca3b7f96e | -11.10682 | -48.88154 | 2025-07-17 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2500ac19-e2ac-3720-a1f6-c187c38d6419 | -12.99396 | -44.86404 | 2025-07-17 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71986fdb-84e7-38e5-b692-2509c8275d46 | -11.11408 | -48.86817 | 2025-07-17 05:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README29.md)
