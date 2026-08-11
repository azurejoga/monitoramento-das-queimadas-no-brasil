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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b199d9d-3b67-3ce0-9783-e994c9dcfea5 | -4.2634 | -48.2016 | 2026-08-11 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4aa5f470-1179-39b8-9c84-f40c5238bbcf | -10.4237 | -46.6809 | 2026-08-11 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 6659b3a9-ac4a-3c18-a29b-a0d7887d4465 | -14.4734 | -45.6914 | 2026-08-11 03:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 43cbf5ff-ae0f-3dcf-89aa-be388bb02efe | -4.2635 | -48.1799 | 2026-08-11 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 673fed0b-ad76-304e-86b9-e4d5090f5767 | -8.9039 | -60.5769 | 2026-08-11 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 86a61ca1-d6c6-3792-a8ca-6a4b9af5e61a | -14.4544 | -45.6716 | 2026-08-11 03:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ce4b5e72-961e-3d1f-8f45-1c2e00fa6ca1 | -14.4734 | -45.6914 | 2026-08-11 03:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 49f46ab1-c175-37bd-b0b2-12c7b1dcaef5 | -13.5701 | -46.2584 | 2026-08-11 03:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 140.5 |
| a795817f-c231-3cb1-bcfe-de25b23e2c65 | -14.4539 | -45.6948 | 2026-08-11 03:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ddbec80b-9a37-3e95-9489-d548b1a9a2be | -13.5894 | -46.2553 | 2026-08-11 03:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8735c9e2-e2aa-379e-b83a-06a79f168832 | -4.2635 | -48.1799 | 2026-08-11 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 60aba976-341d-3d96-ba2d-bea8f1430457 | -10.4237 | -46.6809 | 2026-08-11 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 35486c6b-2842-3c8c-b19c-21c37d75fdd6 | -13.5696 | -46.2813 | 2026-08-11 03:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 70daf8f7-aa85-3a5d-a539-3dcd3d477e08 | -10.424 | -46.6584 | 2026-08-11 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 6237cbfc-595b-3ef9-90f5-a198e3927021 | -4.2634 | -48.2016 | 2026-08-11 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e7c59ad1-24a4-35ab-83e3-4396496f0a88 | -13.5894 | -46.2553 | 2026-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d558aac9-c225-357c-b176-69130b818b3e | -13.5701 | -46.2584 | 2026-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 40ba02e4-8fdc-3beb-ba74-c0d5c278dcc3 | -14.4734 | -45.6914 | 2026-08-11 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6cd28431-7253-3c73-b9e1-dda6f192f2a8 | -14.4539 | -45.6948 | 2026-08-11 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6ac89b0b-cd13-3fbb-bb69-8b477955627e | -4.2634 | -48.2016 | 2026-08-11 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b53e7af4-995c-3265-8ad6-7b07dbb4de53 | -14.4544 | -45.6716 | 2026-08-11 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 960f3d84-3013-3e13-a72b-5cea008ebeb2 | -4.2635 | -48.1799 | 2026-08-11 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 93b5ea41-a338-34f2-8636-97a3f79cceda | -13.5696 | -46.2813 | 2026-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 165.3 |
| ceb312c9-08ba-367e-aaf9-b593f1ce70ef | -10.4237 | -46.6809 | 2026-08-11 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 23f70113-24e3-3255-a46b-0b9583719d97 | -10.424 | -46.6584 | 2026-08-11 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 18bdfabb-731b-395f-9bd7-08f0423b50e3 | -12.4703 | -45.3308 | 2026-08-11 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a9d9f08e-2c4d-393c-a969-a4ece3ca37f8 | -13.589 | -46.2782 | 2026-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e3d9794e-528c-3533-b33f-2918fd339f54 | -5.26139 | -36.69264 | 2026-08-11 03:28:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b47ed734-9b8a-3485-aa32-733dc6de74c1 | -5.25739 | -36.69315 | 2026-08-11 03:28:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9dc707fa-7699-34a6-81dd-231b4cf70556 | -4.978 | -37.23761 | 2026-08-11 03:28:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a3e356d-bae2-3724-b14f-34d38f7176b1 | -4.97853 | -37.23457 | 2026-08-11 03:28:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f660a3ed-6475-3a87-be3a-c4101a60d6d3 | -5.25645 | -36.69182 | 2026-08-11 03:28:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| be5403ab-3174-344e-b2bb-5b3266decbfd | -10.424 | -46.6584 | 2026-08-11 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 18172fe2-af0d-35e6-b083-fd7e8ac05855 | -13.5696 | -46.2813 | 2026-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9a6ad2ee-f8cf-3acb-8ed7-6a2ddbd25988 | -14.4539 | -45.6948 | 2026-08-11 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 08e27cf8-2d80-3fbe-9e56-e85954bc7154 | -13.5701 | -46.2584 | 2026-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3d3d8c0e-09db-3c38-b9c8-4c8d3477e1f0 | -14.4734 | -45.6914 | 2026-08-11 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c0e84c6a-016f-391c-9281-2e9dacbb2a40 | -10.4237 | -46.6809 | 2026-08-11 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 9dd6eb66-87ea-3ad9-b5d4-5d860210ca95 | -4.2635 | -48.1799 | 2026-08-11 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ada743ca-04e3-3da2-92a9-d037fb2f2ab4 | -8.9039 | -60.5769 | 2026-08-11 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1514109d-5060-3ac0-9f81-781799c94370 | -4.2634 | -48.2016 | 2026-08-11 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2477cbaa-48e7-32e2-9642-ce48a1303287 | -14.28386 | -45.30653 | 2026-08-11 03:30:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a29e74be-f1c4-34f3-8d0b-14fb0bbef8f7 | -11.4676 | -44.57387 | 2026-08-11 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| feb210e2-a1ac-366f-a4a0-a86a208a115c | -14.99271 | -39.52769 | 2026-08-11 03:30:00 | NPP-375D | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d8a9792-5a96-3238-b208-b7ad189beb0c | -14.27789 | -45.30888 | 2026-08-11 03:30:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe934aa0-5e67-3fc8-acfe-44ae014b8b1d | -14.27673 | -45.30477 | 2026-08-11 03:30:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e04da2e4-b4fb-3193-8d75-a6eb5af74b54 | -14.99126 | -39.52644 | 2026-08-11 03:30:00 | NPP-375D | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0fa40dd2-075f-328e-bcaa-5db5b0054174 | -11.4636 | -44.56382 | 2026-08-11 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ad54d15-4e93-3c4a-bcd9-e3113e6c63d0 | -11.46199 | -44.57122 | 2026-08-11 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52f2cb3e-af7d-3699-b7c1-ff5bd310c406 | -11.4692 | -44.5728 | 2026-08-11 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3546a41b-07b4-3f59-a3f0-15d5d978adb1 | -14.27958 | -45.30156 | 2026-08-11 03:30:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c64f28a-ae1f-3637-bfa4-5abfc1c887a9 | -11.46196 | -44.56483 | 2026-08-11 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57f2fc75-bf18-3bd2-863f-26fc40dc5c85 | -18.00413 | -44.36699 | 2026-08-11 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c82034e-849f-3ff9-b695-a871f9ba45b3 | -15.43718 | -41.38041 | 2026-08-11 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bf029db-5e7e-3c3e-8d9c-cf6bd92650fa | -18.32868 | -43.77927 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82f620a7-0859-3539-b070-1d9f232a761e | -15.52127 | -42.67033 | 2026-08-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 73c7bd73-39d4-3842-8366-b55bd034c388 | -18.32261 | -43.77766 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1dac0e46-8c9a-3a36-b405-e384f1d02dd6 | -18.02238 | -44.4341 | 2026-08-11 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4dcad62-1f42-3b84-a154-8f2987f01ea3 | -19.8358 | -42.7649 | 2026-08-11 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9b2c80b-eefa-31ed-8c5e-591b48872409 | -22.18454 | -43.24335 | 2026-08-11 03:32:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f047c9e1-2c25-375c-814c-1c36d9848f95 | -18.42377 | -45.49928 | 2026-08-11 03:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b957b83-ff3c-3dbb-98c4-6223a893a2c1 | -19.83488 | -42.76899 | 2026-08-11 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9fce59f8-a773-38a4-91c8-32d01d2fd9a9 | -18.32288 | -43.78061 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5b01cd78-8656-395f-b511-434f0a3b3c03 | -18.33002 | -43.77738 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9040e48f-58c9-3550-9051-7a31fecd95be | -15.52281 | -42.66845 | 2026-08-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 65d401da-8420-3408-a2cd-362a3aa1b1a9 | -16.66334 | -43.63969 | 2026-08-11 03:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 61f5d699-bda5-384c-962e-472e1ed12fe2 | -15.52234 | -42.66528 | 2026-08-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a3fb1f1e-283c-3633-aa49-46ef3915f5ab | -22.18547 | -43.23925 | 2026-08-11 03:32:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f594488d-7e83-3dcf-b6c0-5c85ff2fd98a | -15.43633 | -41.38457 | 2026-08-11 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 063bc067-7209-3498-b4fb-7e354ef9fcd4 | -16.65831 | -43.63271 | 2026-08-11 03:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a9d59224-01aa-3736-8544-499e4f19e663 | -18.00304 | -44.37175 | 2026-08-11 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a6f4512-9ed4-3eb1-9b2e-3e5cf9c231f9 | -19.84153 | -42.76563 | 2026-08-11 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a51805ab-de90-34e4-992f-ab7b538f85e3 | -18.32148 | -43.78259 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 37cd695d-97d6-3e3d-989a-1925e38d11af | -17.99666 | -44.3703 | 2026-08-11 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f703c90a-26af-35b5-a06b-544ea11dbb42 | -15.52387 | -42.66359 | 2026-08-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c1621121-d863-3132-a728-dd8b77969612 | -16.66449 | -43.63449 | 2026-08-11 03:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5ea21a76-91b9-3a1e-9ddb-50bd798c3999 | -17.89503 | -44.45892 | 2026-08-11 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2e17486-5791-3210-872e-0f51a60916ab | -19.8394 | -42.76241 | 2026-08-11 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5f6f7c9-7fd6-302d-a0dc-333284a8c918 | -17.89362 | -44.4651 | 2026-08-11 03:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f8d2c1-431b-36de-95b8-6043bbc3f7d7 | -18.32892 | -43.78235 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| befb5def-ccdb-3f1c-bd17-069dcd94aff3 | -18.32397 | -43.77566 | 2026-08-11 03:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9ef5404f-3954-36a1-aaae-29408299f5e6 | -17.99555 | -44.37514 | 2026-08-11 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d429dfd-7d48-34e8-b1eb-9412db69f0aa | -18.00198 | -44.37638 | 2026-08-11 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c1da5db-c0c3-3c37-9fc0-3eff8d67bb5a | -16.65715 | -43.63795 | 2026-08-11 03:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 930ffee2-61bf-3025-9de8-e86412ade458 | -19.83846 | -42.76674 | 2026-08-11 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0676e33b-0300-3bf4-850f-b5f9defa6934 | -18.42521 | -45.49313 | 2026-08-11 03:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c42d758-1e8e-3101-bc19-e763d40624ab | -22.56712 | -47.23115 | 2026-08-11 03:34:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba9876b2-8040-360c-ba28-1d10ae47e636 | -13.5696 | -46.2813 | 2026-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f778242e-0177-34bc-8c1e-5ac434036f5d | -9.3906 | -47.4878 | 2026-08-11 03:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b7f70af9-72e4-38c2-af05-2dc6360583f7 | -12.4703 | -45.3308 | 2026-08-11 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1eba33cb-4be0-3512-afe2-9ae5f2ccf964 | -14.4544 | -45.6716 | 2026-08-11 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a5fd933c-e2e5-30e5-9031-555adf3f5a66 | -12.49 | -45.3047 | 2026-08-11 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d8654d35-e3f8-3c82-90e3-8d4de30c7b50 | -14.1249 | -45.6368 | 2026-08-11 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c12d4913-2291-3062-bb97-be681be13a5c | -4.2634 | -48.2016 | 2026-08-11 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c4c32f7b-1861-3573-b9cb-c4a9e1a42657 | -14.4539 | -45.6948 | 2026-08-11 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3155089d-8f53-3008-b7b2-8a20e5a389b5 | -10.4237 | -46.6809 | 2026-08-11 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 88c8c25e-5242-38ec-a31f-1158ce29472a | -14.4734 | -45.6914 | 2026-08-11 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a9f7d78d-64d2-3e6a-a201-ae7187fbbb7b | -9.3714 | -47.5119 | 2026-08-11 03:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 578a8bea-980f-3895-b5fe-98b5341ad47b | -12.4905 | -45.2816 | 2026-08-11 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a3a8c4ba-8c26-3b43-b131-d252ca258f2b | -13.5701 | -46.2584 | 2026-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |


[Clique aqui para ver as próximas entradas](README5.md)
