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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5d40901-2935-3477-9b66-4eb3ce1ae764 | -6.28574 | -59.92946 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fc5e5ae-fda6-3d56-98d4-5da701b87316 | -7.87064 | -54.72632 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7910d38-fd32-343e-a940-6b6679d567cf | -8.81823 | -61.40666 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 453e61ad-383f-31b2-b54a-b5b818c37fe9 | -13.46884 | -48.52206 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b01a9b8-103d-35aa-a300-20caadc1c674 | -8.81692 | -61.4113 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dac5f317-99ae-3abe-abd1-cffe0a4313ed | -9.71703 | -54.36482 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08583527-0716-3dcd-aeb2-17f3050dc0e3 | -9.36601 | -50.0922 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaee81ff-2766-35cf-b73d-424a82739ea2 | -13.45948 | -48.48781 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9761fee6-b1e5-3003-8004-26b351d2e2b8 | -7.86046 | -54.69001 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00bdabbf-8429-3b60-86ba-76acd69174bc | -8.12273 | -54.80685 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd9cf51e-eba5-38dd-a86d-a2406baf148e | -11.71767 | -46.7327 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aca733db-8c28-35b7-bdb6-a0de8d164ce5 | -7.08161 | -49.94468 | 2026-09-13 04:51:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b08546b9-196a-3e5f-99db-79a0375180a3 | -6.37607 | -58.28899 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3236bcfa-b086-351a-92dc-30e8bcf115e6 | -10.52167 | -47.90066 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31a33e90-1280-3a5d-9996-593144d495ea | -13.78684 | -48.79957 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2405067e-b54c-3697-9414-cf60f4c9ff2c | -9.87808 | -47.58372 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c19db75-0063-3a29-89dd-f3ce2cd79935 | -6.38072 | -58.29309 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04f2f456-8219-3ed9-834f-047da2ae79d3 | -7.96135 | -43.99374 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8debbac5-fe3d-3745-8217-6be48bea6d31 | -8.83142 | -46.91095 | 2026-09-13 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69ac166d-aa31-39a9-b66f-edae899429d8 | -8.04486 | -54.84672 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7147df28-8fce-3258-af18-24a8b7067436 | -10.96474 | -58.96155 | 2026-09-13 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ed7167-1368-3c50-a4c0-2b5c028e618a | -6.59749 | -58.84635 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8cfeea92-e690-3c33-a8fd-1a4e8a2f68ef | -10.57306 | -51.36812 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a7c638f-38ed-34b2-976c-84740edc43b0 | -8.4721 | -48.94166 | 2026-09-13 04:51:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59935ade-7893-35b8-a8c9-3b9274b82065 | -11.19455 | -42.78049 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e9c4989b-2159-3b64-a6f6-d6f32775832e | -11.98467 | -48.64796 | 2026-09-13 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 345e3cfb-5722-3b6c-ab88-1ec917f5e666 | -10.93847 | -47.90376 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c98cb91-f1f1-3818-8e46-3e564ad6badd | -9.69539 | -43.3971 | 2026-09-13 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95a30268-948b-3a26-8a35-54ef6de60627 | -13.45244 | -48.51102 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad7c8a3-d148-30f0-8805-a7e7d5ef74bc | -9.58564 | -55.15699 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36ccdf36-5e00-3691-8ec0-7d95e8e6e68e | -9.6974 | -54.34195 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 120adb16-823c-3ddc-bae5-dbeef8f969c2 | -10.53227 | -51.36503 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41a8e4ab-b21f-3b1d-a322-9b22fb94cc61 | -6.18653 | -57.7182 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62f84a5-7ca6-39fd-8892-df5e7a9dfd46 | -7.54111 | -44.89869 | 2026-09-13 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e9a62b-2f3f-3169-8440-0400a2d4d6c1 | -13.34608 | -51.77442 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0857ad48-354e-362f-b090-b83ff8f62557 | -11.96103 | -49.77734 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e86f809f-5b35-304d-9757-2cf8dbb7e0d0 | -10.28981 | -55.06515 | 2026-09-13 04:51:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdfe4889-a890-3deb-aa01-2de4d97a94a7 | -8.05337 | -54.84914 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6641dadc-9235-3685-be25-f205dfa2386e | -6.59307 | -58.87054 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15d22665-c3fa-3089-9e9b-811f3e142b63 | -8.81394 | -46.90408 | 2026-09-13 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 716d24a1-140d-3337-8d79-fbae5624c80e | -10.62527 | -46.10675 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d09c7bb-c50d-3178-91c4-1c6554a927aa | -8.31691 | -49.68842 | 2026-09-13 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00f3435a-b383-3fc4-bc57-b6ce58c00957 | -7.34008 | -55.21543 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca3958e1-c192-376f-ab66-d550d0caa47a | -6.81302 | -58.99643 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 703cbcd2-1a79-38bf-9ae0-b33bec0829bb | -10.09656 | -48.86148 | 2026-09-13 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 309bdc04-abf5-30cb-a901-cf0aeca6ca92 | -9.39596 | -50.13323 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b7a37ef-5f55-3187-94c5-6e50322eaa82 | -5.97261 | -57.76985 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9279d250-81a9-3778-81cd-ea08f554f407 | -10.49264 | -48.09364 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 792e1e96-a924-30ec-b639-fd7f135bd540 | -7.8729 | -54.71325 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1985cf9e-b18a-3c59-b7af-f20ef23cfa8a | -6.67133 | -58.71347 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1700857a-58e5-3c97-9a17-8ff9aa7db6a6 | -9.58503 | -55.16056 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b382b9-1224-384e-a9bd-a52cc21d9698 | -9.71236 | -48.11193 | 2026-09-13 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b4b6d83-2f20-3402-9b73-a37907ec3682 | -6.19157 | -57.71908 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d9ceb7-1fc4-36c1-a39b-07a5ec9ff9f9 | -13.45655 | -48.48324 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec12dfa0-6e6f-3333-9da2-fcd219e0e644 | -10.93729 | -47.91166 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77f186e7-a688-3e40-bfac-9af27e6ebf01 | -13.60711 | -47.8838 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fab12fd-8810-32e2-8212-dd4df7f99d4a | -10.5481 | -51.33086 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1072815-1483-3aa7-b1f0-9e88341a3d1d | -7.62937 | -45.98295 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47d5e6aa-2f99-3ac9-b296-1d46cd686dac | -9.59548 | -55.14776 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4434e10e-afc6-3304-935f-a945c2c49d07 | -7.86601 | -54.7292 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 710b4529-11ea-3787-827c-a40a796153be | -6.37604 | -58.2884 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70a0a97d-2e33-3cfa-bea1-1578b48f7e3a | -10.54338 | -51.3815 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dd679cb-feb8-3439-a017-6988fc514213 | -8.04888 | -54.84744 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbee2a67-f126-33eb-a771-170de281ac6b | -6.72236 | -50.47224 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16f04245-d5f3-351d-9692-ce9df751e295 | -6.68131 | -58.87586 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 012e2250-092d-3b1c-8b23-57bd1c53e5a6 | -8.05213 | -54.8562 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa4e8c9d-6eae-392d-8d09-e9ee0c12592f | -13.62232 | -47.88139 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 215e080d-ff9a-3a50-b8e4-dffa804f5112 | -7.96192 | -43.98977 | 2026-09-13 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89460773-6822-3570-bc63-e5a111d20f0a | -6.7695 | -59.42661 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c282571-3fba-3ffa-9756-5235cc98b194 | -6.59546 | -58.84995 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32f852ba-1ce1-389e-ba16-c16ab29bd36c | -10.9679 | -48.3557 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 277f4429-7bc7-35ac-8f37-8a9687c11bc4 | -9.70942 | -54.36342 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3a8606e-d762-3e5c-af7c-47915ca4c40b | -6.11331 | -57.67122 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| feb5f1e3-7dc0-3184-8d8e-f514d727ab70 | -5.96753 | -57.76902 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6aab20df-e3d4-329b-acde-8a2c0f8b20cb | -11.1994 | -42.78128 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a0ccd68a-60ad-31fe-914f-1a660d8d07ad | -11.18614 | -42.79122 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 50653945-84c3-328a-b429-e2ca8278b987 | -11.56878 | -46.9873 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e39c663b-1004-36ae-b3a3-3867778d15fb | -6.29863 | -59.95744 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0934a9-6e16-3529-accf-693f93f249e2 | -10.08473 | -46.8415 | 2026-09-13 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff83041-4195-3f3b-97d5-2c05f615c9d9 | -11.81881 | -46.40211 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24f5c926-a10e-3855-b752-6d528a440a49 | -7.872 | -54.71133 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34da752-3e76-3b0a-ae12-848ee036d509 | -10.96441 | -48.35528 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c873aeb-b27a-3a0f-8567-94de90488f63 | -13.34594 | -51.79645 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a57efbe-0e6b-377a-859f-f7897c5d378f | -8.28947 | -39.9692 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bdb4c4e5-bed8-3384-a611-3f51c11ab9d3 | -8.8672 | -62.52422 | 2026-09-13 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6c36cc2-662e-318c-ae46-64f52408d886 | -7.86669 | -54.70155 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 742712ba-5434-34e7-9b25-2df3a4c1b34a | -5.9782 | -57.76777 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64271ec7-e770-34fe-95f5-744b777569b4 | -10.30156 | -45.29292 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6f4d98c-25fa-36fd-a851-d09cde5f99d9 | -12.67213 | -54.66386 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9f1daa5-02fb-36ee-b77a-85d5e3bcb017 | -6.06849 | -57.86795 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8eb6eb2d-2d91-33d1-8060-483008f124ac | -6.73773 | -55.64183 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d77a81fa-8fbd-3601-aa8f-096a4ac45c44 | -6.08488 | -57.86437 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 793313b9-be5e-3576-aa8f-ab5f07ecc651 | -6.59686 | -58.84979 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a4f0e6b-ed42-3ef7-af3e-fb5565160b8b | -10.45754 | -48.64797 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bf5c0fb-314b-3516-bda5-2bf8ca8cc831 | -6.59273 | -58.8419 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dee955f-60ee-3e65-9e09-86c9ff6e8382 | -11.48586 | -49.80866 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ff2c99a-331a-3436-a92f-58e8b98df38a | -6.72128 | -50.46878 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1a39e8e-d9ee-3396-9971-95393e68729b | -10.94491 | -47.90901 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d280601f-33b3-3f39-b50b-552ff489355e | -7.85956 | -54.69517 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc85713-ac16-3680-948f-7b55674d1ba1 | -13.02282 | -48.64252 | 2026-09-13 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
