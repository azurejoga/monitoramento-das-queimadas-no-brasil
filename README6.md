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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 909ac620-e592-3ee3-8946-ed3e263aba36 | -11.84064 | -57.84767 | 2026-05-09 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3066ffb7-8a30-36be-87a3-f897275f1508 | -14.16866 | -54.43306 | 2026-05-09 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aec9db9-292c-3b5d-aea7-b24ea5ce04b8 | -13.36976 | -43.20216 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ccd4204-ca73-3250-b88b-8fd91bf230ab | -13.36044 | -43.12223 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b9087c5-9ab8-3209-8557-e65ca17f37a1 | -11.92474 | -54.10091 | 2026-05-09 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cce303ff-f36b-340f-b389-76edc1c98236 | -11.8229 | -47.32894 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2e18d7d1-1a8c-3b58-9790-d98b0912bafc | -14.0029 | -56.63496 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4abadd4d-eed3-3f6b-9d5a-4c1ea28a5f5c | -12.54653 | -54.60758 | 2026-05-09 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f2c68c-b3b7-3f9a-a503-1c3a04090c1c | -13.36005 | -43.12536 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eec8c62f-9706-37a9-ac75-8e11e805e72b | -10.54468 | -56.33627 | 2026-05-09 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd36fbf6-275c-39a5-8fa0-79f4c4fdd8e2 | -12.54243 | -54.61086 | 2026-05-09 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e549303-b317-3489-b19f-25a656d18db7 | -13.65707 | -47.69257 | 2026-05-09 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 774d7b12-5669-3311-be66-d80cb99448dd | -14.31632 | -57.7334 | 2026-05-09 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80797c51-0d19-34ba-b274-c07d136d8ee3 | -13.18525 | -52.68173 | 2026-05-09 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff93933c-8abd-3731-9c75-2761c5fffb00 | -12.35088 | -50.0339 | 2026-05-09 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb0d8bb5-3313-301d-a8fb-5fc645692658 | -11.82143 | -47.33931 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4aa8e80a-b312-39b5-8b1f-423ec52606b9 | -12.85894 | -43.75463 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25adada0-1560-3515-a75e-9742b09aedf1 | -12.85855 | -43.75773 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fd6f237-bf17-322e-bf74-175dbf157764 | -13.66948 | -52.19468 | 2026-05-09 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a41f6c7-c464-3371-928a-ddef067b3412 | -12.77074 | -46.98534 | 2026-05-09 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0e96ff4-9e61-3b82-bab8-9308e402dd8d | -11.82614 | -47.33471 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2d3629c1-72c6-3903-8e06-9a751b4c4102 | -10.71266 | -56.04347 | 2026-05-09 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e65c3c-972b-3012-8098-2b0fec0f093c | -10.54765 | -56.33558 | 2026-05-09 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6411379-a120-3608-aa51-6a005a9c34b9 | -11.60504 | -54.18747 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac017832-e922-308c-86c9-4b3fb9972428 | -16.41496 | -54.91979 | 2026-05-09 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac959273-dfb8-3dc2-90c5-4c6308d4830d | -16.44849 | -51.7228 | 2026-05-09 04:51:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c7c480-91eb-37fa-b704-9f7bc2e179d4 | -11.29865 | -54.02467 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12fd8dc-0df8-371a-abed-20d888bf7642 | -10.71347 | -56.03882 | 2026-05-09 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 601f8c2b-56ae-3280-ac20-18e3cfcf0cac | -11.29311 | -54.7536 | 2026-05-09 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a82c4c2c-3c97-3d1b-b4d2-473e798ad91e | -14.32123 | -57.72883 | 2026-05-09 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e98124d-2ef2-3402-95d2-fc9fcfa21ab9 | -16.44566 | -51.71851 | 2026-05-09 04:51:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f4d376c-d40d-30f8-a001-c46a6d5cda73 | -13.18469 | -52.68526 | 2026-05-09 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd0941ac-90b5-30d4-84fc-96accc2b5b0c | -11.29803 | -54.02847 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57c11738-9740-3d83-97e6-c4c3c8e89e74 | -11.29118 | -54.02729 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed873266-7495-3730-9529-201bb6a6ef45 | -11.63189 | -54.15306 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfca12d5-7943-3788-adae-3c5fa9d9f75f | -11.06858 | -52.47173 | 2026-05-09 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59665c3f-c9ad-3f1e-970c-46f6e3728db4 | -12.35145 | -50.03002 | 2026-05-09 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 849bbe1f-ea83-3543-bae4-5d147eadf92b | -11.48191 | -54.06202 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7abe0cb-f2b3-3916-905f-d3332c0a84ae | -13.53994 | -49.90303 | 2026-05-09 04:51:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d766a216-866e-373a-96cd-cecc423032e4 | -11.6091 | -54.18427 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c900f98-19ce-3bae-a37c-d6b6fa52fe87 | -17.93944 | -52.95401 | 2026-05-09 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 910b8d48-6f74-3a9e-9a45-4edf9f6b12ae | -12.34799 | -50.02948 | 2026-05-09 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab9e3183-6bab-3fe6-ad94-9855319dae7b | -12.86078 | -43.75856 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a0c90f2-84c1-37f9-9517-76fdf57a007c | -13.36935 | -43.20559 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6dc9dac-8e71-32e7-82fc-ad34c5947797 | -11.5092 | -58.65596 | 2026-05-09 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34710b85-e13c-33bd-8890-2a0b43d35e99 | -11.60973 | -54.18047 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b18ad79-f9f0-35f4-a1d5-28d01bbf3495 | -18.01341 | -51.80375 | 2026-05-09 04:51:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d325f41a-52b6-3413-9836-7cda55888490 | -10.55931 | -56.34373 | 2026-05-09 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 736cce36-44fb-3515-881e-f1839bc4848a | -17.93166 | -52.96016 | 2026-05-09 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b78f123-b603-3028-b463-70559ecb5b2d | -15.22143 | -50.85695 | 2026-05-09 04:51:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256b4dce-7d8e-3336-9502-f4394c7efbce | -13.35741 | -43.12144 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75eec8ac-3a8b-36a9-af25-9a54e8c814c1 | -11.91728 | -54.10351 | 2026-05-09 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 569e1bb5-17f0-37ff-bb30-f9f068fa8aa9 | -11.8254 | -47.33988 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 58be402f-eecf-3eed-bead-bac329e8db0d | -11.9207 | -54.1041 | 2026-05-09 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 147f865f-3508-3700-9d02-39eeb7de76e5 | -12.86115 | -43.75544 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0fef96a-0f1d-3cc7-a6d3-ae10e5a560fe | -11.29176 | -54.76164 | 2026-05-09 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab646db-4ab8-3638-98c6-6c09757eb755 | -16.41622 | -54.91215 | 2026-05-09 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ef510aa-2add-34b8-b29f-d1e636f14090 | -11.7824 | -47.09243 | 2026-05-09 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a6be4a1-e2f2-3564-b4d1-72a7c2a94563 | -10.54855 | -56.33692 | 2026-05-09 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0052d536-16f5-3e2a-97bc-681895e69a69 | -14.00454 | -56.62561 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffcea4b2-8f87-38d1-b14a-e4e74317c11d | -14.00372 | -56.63028 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a78a8d81-6c25-3828-9feb-fac11a78b51c | -11.60567 | -54.18367 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb31928c-e5e0-331c-af95-bf71524e9e33 | -12.99881 | -54.67566 | 2026-05-09 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3195b846-fee3-3515-bce2-6df0e168d2e1 | -12.85815 | -43.76085 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31925831-e1ca-3615-939a-0b8ec8835847 | -11.50478 | -58.65514 | 2026-05-09 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d0db813-d512-34bf-85a4-9f551fbac6e0 | -11.57302 | -56.95065 | 2026-05-09 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a36a93e-ad11-3eb8-b51a-dcc978c727c9 | -12.34741 | -50.03336 | 2026-05-09 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9402dacc-f841-340b-9bc0-c0cb1df890a5 | -14.14117 | -45.38972 | 2026-05-09 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abfb9346-abd1-3824-bdb5-16216b5604c3 | -14.31726 | -57.72808 | 2026-05-09 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975194bc-0a59-3871-9265-5e54c1f51094 | -14.00663 | -56.63569 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8422823a-a5eb-39f2-bf32-29e784df597e | -17.93555 | -52.95708 | 2026-05-09 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 65df98ed-23b0-352d-9551-aea8690f9ef7 | -16.41283 | -54.91156 | 2026-05-09 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 950f4817-239f-3d36-bb04-d788390bfb7e | -11.29528 | -54.76227 | 2026-05-09 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 630476a2-9632-39bf-8388-62b9a9d469b3 | -11.84134 | -57.84378 | 2026-05-09 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f329db35-d88d-3a43-bc0e-438a5ae0fc94 | -13.99835 | -56.63888 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 183c5893-dd89-3922-bfe8-c7f06a06d804 | -12.86367 | -43.75843 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7bb707e-9225-32fa-96e0-beed91570794 | -11.82216 | -47.33414 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5edf6150-5c81-3e75-8d6c-a227722d9cc3 | -11.97799 | -46.78753 | 2026-05-09 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3355683-fb57-34ff-81e6-0a93b873fac2 | -15.41737 | -43.11084 | 2026-05-09 04:51:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe82b37c-c02b-3256-8603-73af10a81bb5 | -11.78289 | -47.08886 | 2026-05-09 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17c1864e-ef55-362a-89a1-0d17953b523e | -10.55242 | -56.33757 | 2026-05-09 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30eefb18-106a-30cf-b3cf-003bd80058af | -11.81819 | -47.33355 | 2026-05-09 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca7f237d-d422-31dd-a26d-750b51c58a44 | -13.37143 | -54.26485 | 2026-05-09 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a1a5513-1c65-30bd-b553-8fc73aa93b2f | -14.90301 | -45.1833 | 2026-05-09 04:51:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 947a8ab0-6dbd-3f90-854e-66aef87ae65a | -15.41779 | -43.1071 | 2026-05-09 04:51:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b8a80e3-20e4-33b9-957f-c0d4e9a5e6aa | -13.36278 | -43.12232 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bea8b17a-eee5-3df0-be43-9abda5f422db | -12.31519 | -45.46727 | 2026-05-09 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| affd21c2-7f79-3378-a989-37dba9b6c805 | -11.29244 | -54.75762 | 2026-05-09 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c99aae3-0fac-3655-a128-df6bddf252c4 | -13.00113 | -54.67461 | 2026-05-09 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d1571d7-2e06-311c-bc6b-e917bc782493 | -12.34452 | -54.75837 | 2026-05-09 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0898d28-aa7b-364f-9a00-400b94cac1f8 | -16.41559 | -54.91597 | 2026-05-09 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db368150-0991-339e-978a-351025ee209d | -14.00745 | -56.63102 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4b3d08d-832f-36c3-b511-88da829e789b | -18.16761 | -51.10685 | 2026-05-09 04:51:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82492d9b-9bd7-37e8-8cdb-88a559a3e431 | -15.22949 | -50.85028 | 2026-05-09 04:51:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08f92532-8e63-3ce6-856f-967e028c8d0c | -16.41961 | -54.91274 | 2026-05-09 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf2c0cf1-7d96-33be-bac5-326afab2d7d0 | -14.31517 | -57.72993 | 2026-05-09 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea83794c-836f-347f-bdda-c06564e92dfc | -13.36242 | -43.12542 | 2026-05-09 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 90d11da5-2c9e-3d4e-a2dc-2d971538f052 | -11.92132 | -54.10033 | 2026-05-09 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e8768c3-5afe-36b5-b397-a7e19fa37330 | -11.29596 | -54.75824 | 2026-05-09 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71da18ca-dbf7-39e5-8c93-73dc7f6e3e5d | -18.48449 | -51.68814 | 2026-05-09 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README7.md)
