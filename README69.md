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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a618f20a-763d-3676-8f9e-975b81f50dde | -12.44096 | -50.84007 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 936cefd7-8031-3b7c-a6f9-cf353298c1a8 | -11.52584 | -46.86814 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2f9e28c-4d3e-3477-bff9-0081fae54452 | -9.49596 | -56.7533 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82bf8e94-2eab-3603-83b1-ca5b7e058117 | -12.95815 | -48.61514 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82aa8eb3-3a7e-3224-94a2-b8ad3329d810 | -9.46048 | -56.7048 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac222e70-0350-38ef-8a5e-0d7096aefdc0 | -8.65312 | -66.59694 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fe4c5a1-acb1-31bf-ab18-2cad5a40eff4 | -9.10468 | -60.96 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e05572c-5205-3ac0-9159-266bb2c6fb7c | -12.51317 | -56.90242 | 2026-09-17 05:18:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea39d75f-635f-3c0b-a019-ba3780dcfec5 | -8.88341 | -62.38953 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcb3ad4f-3462-3f25-9555-aba0b169c0f5 | -12.37605 | -48.46252 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a82cea8c-4278-38a2-8662-45da9e646581 | -15.49747 | -53.80342 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 261e0bdf-90c5-3dd4-9674-5a446da5083a | -14.84227 | -59.54367 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 592b30cb-a653-334a-a861-5aef61011a49 | -12.1244 | -57.17997 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 697ebcac-c101-3f3d-a33d-0c52c79d121f | -9.17179 | -58.30313 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2507526-0c20-3dc9-a58b-ac99cc16d040 | -10.83694 | -46.16212 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c366c91-6779-3e42-bf23-a2754a95674a | -10.83316 | -46.14448 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61f57f6e-c974-3953-b7db-98145fc247f6 | -10.3904 | -58.30711 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f08e77-e42d-3c13-add0-989c308f6c1b | -10.82832 | -46.13519 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c8d22a-22b3-37ee-8e02-b4a9b53f8bb7 | -14.15145 | -47.37803 | 2026-09-17 05:18:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c72ed44-d19f-3dfe-a271-010e436a9ef8 | -12.13715 | -57.18569 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6ea503-709f-303c-aa31-94391515feb2 | -15.46426 | -52.88287 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62826e7e-6ea4-3387-ba93-ec673cba3f03 | -11.53619 | -46.8781 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e28b1ca-68d7-3eb7-9a78-fe5f645f6af5 | -9.09817 | -60.97422 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9375898-69e3-39bd-9d4f-2eef837aea5c | -9.05848 | -65.91512 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8cf56f6-5bf5-3ef8-a86f-97fc9f843bb8 | -9.28604 | -60.62939 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35df19ab-bc61-3336-a198-a68f8ac3a8b2 | -11.52536 | -46.87215 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b2c4505-8107-38c1-8eaf-5ce2e2703a84 | -12.43854 | -50.79099 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6707ac1d-3cb6-3f1c-9f1e-5597f1f50d64 | -9.10635 | -65.93475 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a52f2b52-52c5-3924-9528-7089b658160a | -12.4527 | -50.81961 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f92eaad-4d86-3248-adc8-379942e3ddb3 | -8.75163 | -66.57541 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b0167f3c-e3ae-33ba-8485-10f0d09e4b46 | -11.07975 | -60.70546 | 2026-09-17 05:18:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c72a6a23-95c6-332a-aa11-659f27d49286 | -12.45207 | -50.75721 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb3fed3a-ccfa-392f-b46e-c006d952f038 | -11.80929 | -58.17705 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 83316596-4e8c-3422-b124-25776c2eb3c7 | -13.43043 | -43.81682 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6982373d-12ab-30ad-8512-30868b07c203 | -15.49053 | -53.79747 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48089095-d4a0-3d34-b0ce-ed453be23f9d | -15.48673 | -53.79691 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ed24e49-d519-3592-9c50-e90fea7b8991 | -12.42149 | -48.48425 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f084dea9-a6bd-3f0b-be32-c74be7a623d6 | -9.10209 | -60.9749 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea2d717d-8726-38fc-925e-ad6053a07c2b | -12.11826 | -57.19708 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1944610-f3f8-3cbe-9a8a-3f625a338e8a | -15.64122 | -52.73483 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40d45796-8bb1-3017-814f-177601edfb3c | -12.4486 | -50.84998 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ab8f890-a683-3099-8162-3e904eca67ec | -10.63303 | -48.7075 | 2026-09-17 05:18:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90d1fc9c-b868-3077-918e-2b6b590d57c0 | -14.8233 | -59.55198 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f765cef-609e-3903-9464-a7c86e2fe69d | -11.89101 | -43.81723 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4a1a5c6-186e-3a2d-8305-3e9c8b1713d7 | -9.10295 | -60.96994 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 033808a9-e196-3e53-9064-b3576dd78b6a | -9.09687 | -60.95862 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b62afaa8-f328-3742-ac6c-51bed4f2e984 | -11.33746 | -46.77105 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d6016e-1aca-3257-aeb7-9df7a3daf57f | -12.1094 | -57.18838 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9b2cd1c-0932-3b95-b9ea-08c6dd07fe67 | -10.8273 | -46.14334 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9000cc15-e4e9-304c-bf67-c7ba972e15f2 | -12.30064 | -47.42478 | 2026-09-17 05:18:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c75f516-c52e-3cbc-91b9-869c2b7718cf | -10.59374 | -59.42071 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c525d04-d067-3c38-963d-7e05ae9a1ff4 | -12.44595 | -50.83636 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5110e2a-87a9-3e48-a318-0eee7601b8a8 | -12.78434 | -51.24384 | 2026-09-17 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19efbf0a-7ed1-3121-bbd1-f1653e78fc43 | -12.42854 | -50.79846 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5bef174-e028-3aa2-b0a5-8f7e4d4d0751 | -11.49934 | -54.46663 | 2026-09-17 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11c198c6-2f99-3d66-84d1-a713d66a2246 | -12.44478 | -50.84502 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 710d9d2d-4b45-3d34-9622-6ad6ade28641 | -10.76769 | -46.20726 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19d75d3f-fb25-3378-9f66-3852d12f9646 | -11.49524 | -54.47004 | 2026-09-17 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67cbf148-1c4f-3200-a06b-ff12b512aac2 | -12.14381 | -57.18678 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 383dfd6c-e0ef-3cc9-9f88-cfa5ae9f9b4b | -12.45916 | -50.77162 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c686b9c3-6cbe-3c84-975e-dc496059c3f4 | -11.58087 | -46.89057 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61c6f7ac-adb4-3db7-9cdd-ebca6011cd40 | -9.49319 | -56.74927 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4ffdb2-c95d-317f-a81f-c5eb8c99f764 | -8.76966 | -61.39758 | 2026-09-17 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a779945-7fcc-3f27-a912-5a105a3ccc7a | -12.31263 | -47.95723 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 099dc0ac-9f21-3e7b-beac-196c961cd4fa | -11.98185 | -52.46889 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 263a70ce-97e3-3e5a-b670-f3a7a79c5ee6 | -10.28081 | -60.5383 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9fc3114-6495-398e-911e-121d9131bc99 | -11.16813 | -42.79178 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 845ebb7c-cf6d-3490-b2be-b08fc1b09e3f | -14.96201 | -47.53385 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a029af6-6426-3718-b88c-6dc5609c1f88 | -11.81266 | -58.17762 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a0471204-c39f-3f67-bfac-de7a18ff5d1b | -9.09742 | -60.95671 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 752562fa-73c2-3a46-8613-1b5e6f9913fe | -9.49152 | -56.75977 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88eb867-fadf-3d1b-ad1b-56272eb439df | -12.12107 | -57.17943 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b049a3-4437-31ce-b784-6cc088a67905 | -11.16799 | -42.78665 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56659671-f67c-381d-a649-7e1ca38743a4 | -11.98649 | -52.46443 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd9ea77-2354-3e1c-bd46-1589faf097d5 | -9.89059 | -57.79486 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb02da7-bff6-31df-80bc-b4b56c8de439 | -14.13115 | -44.01424 | 2026-09-17 05:18:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 569f3c47-ff44-347e-b8ba-11adc3e828d7 | -12.42507 | -50.82457 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90d422d3-ff2e-3384-9a59-886760eb2e85 | -12.43713 | -50.83511 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 46771cc5-8f2d-33b6-98f2-003e37a86b84 | -9.62458 | -61.81889 | 2026-09-17 05:18:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9545abda-4d63-3152-8f3a-e4e496fe6eb1 | -14.18276 | -45.14019 | 2026-09-17 05:18:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4f798ed-eab2-3a08-8154-636851e6c2c3 | -10.78451 | -46.1986 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56611777-2e5c-3c9c-ad21-068a15b47c1b | -11.53467 | -46.87785 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f764895c-664c-399f-883a-54adbf5fb466 | -11.58843 | -46.87628 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4e54613-7eb6-3603-8036-9339c96c4f3a | -9.28523 | -60.63413 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48fbb31d-698b-38f1-99d5-42be1c5dcfcc | -12.37014 | -48.46756 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3984e528-05f0-3654-a880-d3485185142c | -12.70916 | -48.26808 | 2026-09-17 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f3483f-20e2-37d9-a0f8-f886b2209b0f | -12.44738 | -50.79223 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfb90d62-fc93-3ce7-9829-37451621d6fd | -13.43658 | -43.80963 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9357318e-5d0d-3cd2-b48c-28bb14c28545 | -10.82625 | -46.15168 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 1e6efaa6-762d-3f8e-adef-879601d8317f | -12.44154 | -50.83574 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b942224d-027d-3442-b1e0-5b2bd5a67a2d | -8.75948 | -66.5647 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8d65db-b7c4-30e8-94c7-6b1ab7bc0133 | -9.69516 | -58.17803 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f76406a-60de-3b66-adeb-a281b178ed79 | -12.4247 | -50.79347 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fe469a6-2554-3f98-a50a-d0246d60c7ea | -8.11016 | -64.12032 | 2026-09-17 05:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efca672f-f7d0-35f1-8aa9-4aee7acd8302 | -11.3237 | -46.77914 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff9f165b-74f4-3bca-b42b-196cfd167a54 | -10.81638 | -50.83549 | 2026-09-17 05:18:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f47276-6b60-3bff-8af8-48adbc5d9315 | -13.3874 | -57.02164 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f84a317-dfb2-3aa1-9332-1f59695ec405 | -13.38684 | -57.02521 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e2449af-af22-3109-9ac8-a4cc65d2c2a8 | -13.58197 | -45.47094 | 2026-09-17 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc14451e-2a4e-3652-a2d8-6aa41c9fb96d | -12.46035 | -50.82954 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README70.md)
