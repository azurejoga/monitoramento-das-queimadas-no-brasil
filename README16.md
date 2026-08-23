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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fbd3484-6e31-31c4-8438-e72ddb3af49c | -10.05228 | -46.42023 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b37f845-ec74-3fe5-94bc-3311819301ec | -10.70912 | -47.74133 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c019cf1-dda6-308a-b070-f570cbf91d66 | -15.25131 | -52.84784 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fadfc5f5-67a5-3827-a055-9f51b799eae6 | -15.64044 | -55.95677 | 2026-08-23 04:10:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3775f51a-edf7-3099-9faf-75b59ffa7f8f | -14.14831 | -48.06184 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c107d19-190f-3b8d-aa6c-b79d556af424 | -12.56493 | -47.93385 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 867aa116-8e23-30f4-abd4-b7ae77bbcc54 | -15.22263 | -52.7757 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd94b9af-d416-3571-be44-e86b13bed3b0 | -18.03626 | -43.03711 | 2026-08-23 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f6b3b297-48a6-3ef1-86c5-60ae757f30ee | -12.40848 | -42.90216 | 2026-08-23 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 67ad85e0-48f9-34d8-91ba-2efd5a87be4a | -15.20661 | -52.80147 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 857728c2-ef2a-3afa-b234-478d22036880 | -14.56093 | -53.03967 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97e623c6-3b26-33b8-998e-c04a6203a978 | -12.21685 | -43.16987 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4f13d21-00e1-3ac9-aab5-4d8f37e67597 | -10.83876 | -50.97084 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4cfd146-318e-3618-a0b5-e00fd6bfef6d | -15.64293 | -47.65497 | 2026-08-23 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de06b65a-3059-366b-a4a3-4c0ecf0c56f4 | -17.59116 | -44.60965 | 2026-08-23 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f85a2e3b-b83c-38e8-a6e1-1d4fef85a022 | -11.61976 | -50.56232 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da1bbca0-8ecd-339c-b5f1-31a5a46ecec4 | -13.19284 | -51.42699 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 20dd9165-830c-3def-b2da-f8a6b474d5a2 | -16.05034 | -50.43593 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9d02eac3-4b74-3188-98ca-1932ae2c4c28 | -11.0568 | -49.50873 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1659d98-7015-37f1-9156-8198107768e9 | -12.2163 | -43.15173 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4921705-9464-3421-8f49-ad3cc7734cec | -11.20686 | -55.05182 | 2026-08-23 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c57f0d-f489-3712-9de6-8172ad1863d6 | -17.92433 | -44.50288 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4082a3b4-b4dd-3d6e-86c2-090e075dad64 | -14.57569 | -53.02118 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9f5da0f-860d-360f-b3df-9ac983a502c3 | -10.71042 | -47.73877 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1db07a0d-345d-37a4-a653-ad0ced20b7ae | -10.33172 | -45.40482 | 2026-08-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0229a25-2641-3261-97ce-171f5414fd69 | -16.40524 | -51.84078 | 2026-08-23 04:10:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4b11d22-fc82-354c-9e6b-be782b17b9c7 | -13.20395 | -51.43055 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e78e7d9-c43e-39ce-bb10-314df36a2197 | -14.13453 | -48.05113 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15f10d1e-1704-3b36-8969-70655beb34c0 | -12.40463 | -42.90514 | 2026-08-23 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6eb19049-4cf4-3804-8cea-a2a687bb8d55 | -11.85308 | -51.67406 | 2026-08-23 04:10:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2a72f92-bbd3-32ba-8230-1ed53e418645 | -13.1584 | -51.42026 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| aa913060-1e67-3abf-bd83-921e11e07f65 | -12.24193 | -43.12025 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 000e615c-47f4-3fe7-9ec7-6a33e8577736 | -12.24413 | -43.12783 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d419c5fa-b326-3aca-87c9-24df85c32caf | -8.53135 | -54.85419 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16893c20-bf18-38ef-bb18-69eb05172da1 | -13.66032 | -51.85724 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8686d2e8-ed0d-3de8-9b1a-e0158dc539df | -16.57515 | -51.63042 | 2026-08-23 04:10:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7571653c-a3cf-30d6-b192-c951df55ab3f | -14.36736 | -51.83812 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f732d00f-c93f-3064-91e4-f01cf8b70b72 | -16.05554 | -50.43245 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d328a1f3-1c39-331a-a28a-80cc1b2e9c03 | -12.27061 | -43.13208 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 97e7098f-7ace-3374-961b-6065068a6142 | -12.85189 | -48.46736 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 56d8b25c-fa50-3c66-a586-9c8fd941ad08 | -16.05823 | -50.44231 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38b3fbb4-f310-3bd0-b1c1-63076fb61a99 | -12.22016 | -43.1704 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3ab76478-3ccc-3931-9e1c-42ae34d3355e | -14.97116 | -52.67085 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3741428-04da-32af-9699-0ef83f45b74d | -10.99749 | -47.57819 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 698f4454-ecc6-379c-8cfb-b88e6d7b38b4 | -10.84107 | -50.98627 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a98b7e07-96b7-3051-bf7d-c33013c35caf | -12.73447 | -48.39702 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d52c793-8816-3a42-82a2-c8497ea7e01d | -11.33315 | -43.16708 | 2026-08-23 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35f98f80-b330-3806-a3ef-33d1fab61434 | -12.36666 | -46.45121 | 2026-08-23 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5537fe46-d60e-38cc-ac3b-ceed83ff9813 | -12.22979 | -43.17598 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6f77d71-81d9-3fdc-bf3f-2bc0596e880b | -9.94339 | -46.62812 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea0aaba3-c491-3e87-b0e8-660c7235c70a | -12.81528 | -48.41286 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35779b76-42b5-34b7-884d-d90c18975bdf | -9.52732 | -51.64946 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42fc12d3-9c7a-32fc-b3b8-fb5150705b77 | -11.61528 | -50.55927 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| d8293bdb-59ff-3309-b8d1-740d59a56e1b | -14.53324 | -52.02461 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d9c5e85-0102-3081-9c59-e54252c52a9d | -15.76262 | -49.97332 | 2026-08-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66439a6b-a4b6-3505-bc58-39bf11d08899 | -12.2309 | -43.16894 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1ef970f5-6f94-3176-9b64-5e666733cf9a | -12.76776 | -47.10333 | 2026-08-23 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de59e500-88ae-3636-853f-977c7f73e8d7 | -12.5868 | -47.87891 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79060e28-7a92-3169-9537-e38999847984 | -12.59773 | -47.88625 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04431914-957b-348a-846d-219458386a57 | -14.99428 | -52.68988 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e55bc8-884e-353e-baee-719a6e818be8 | -15.04122 | -48.69287 | 2026-08-23 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3df24026-d045-33a8-8bc7-5c7f0834616a | -12.3659 | -46.45561 | 2026-08-23 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f906d613-3348-3f1f-9f4e-82b6d26e93b0 | -12.73654 | -46.46269 | 2026-08-23 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfd4ebc0-373c-33f9-8101-344dbae7d49a | -11.59041 | -46.93731 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 233868eb-d364-3379-b75a-fb49bce98b1d | -12.74266 | -48.39817 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c43a84bd-bb75-369d-8abe-38162f8c2bec | -17.25637 | -44.87632 | 2026-08-23 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aaabae0-6cee-33b2-bfe7-d178b577ae66 | -14.12975 | -48.05297 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 94bd4815-c432-3423-af07-dc3a9f68828f | -17.92934 | -44.4926 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fb4cf87-7bca-3e9e-98c8-10e0ec084ab3 | -10.30995 | -45.3597 | 2026-08-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| edc67a92-6417-3662-9abd-867e806d8607 | -14.30951 | -51.84466 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4edde32-cf88-3414-9f23-57c9f7982fe0 | -13.19573 | -51.44662 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0410c5a-42ba-32ec-9295-7f545718ee9b | -11.61593 | -50.55614 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 432e9f63-0fc3-3b29-a324-a85ceafcbd63 | -15.57165 | -42.59317 | 2026-08-23 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f964ad5-b7be-3b04-a8cf-5aaf77610a34 | -13.88362 | -54.00531 | 2026-08-23 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15fe1cde-9a6a-3029-86c3-dfe206bc1d4b | -13.43846 | -43.85686 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 990bb4d3-84e6-3d67-aca5-e8febcac7774 | -11.43462 | -44.53757 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd153453-d243-3d99-aa87-b38ed56f7ed4 | -16.07083 | -48.44822 | 2026-08-23 04:10:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e879edcf-28a3-3048-a3b2-c5a3b821811b | -13.63509 | -47.76338 | 2026-08-23 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2618e8e6-ad79-3f6f-9efa-2bc6dcaa17bc | -13.16332 | -51.42122 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 3582a44d-544b-3a25-8ab1-1fe15d5ddbe4 | -13.02957 | -42.0008 | 2026-08-23 04:10:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67677cba-0cce-3f19-a993-9240bcf02c8e | -17.92821 | -44.49983 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da8b67c-7e89-3679-8397-ac3caea083f7 | -10.06358 | -46.44819 | 2026-08-23 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5728c9d-3d3b-31c5-8329-55c6f1061f42 | -13.20268 | -51.42891 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcdfc581-e4f4-3c3c-acce-fecb1c5190e5 | -11.43922 | -44.5307 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cab1b69b-bb35-3229-bff7-685e755a4ec7 | -13.43295 | -43.84867 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb302e9-a886-31af-9677-1f5d8a8cb0d1 | -12.22733 | -43.16794 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ec51ca5e-59a1-38aa-8f9e-9fe7b216f9f5 | -13.89008 | -54.00726 | 2026-08-23 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fc480f6-feba-3d19-8458-e8d085d41007 | -10.93744 | -49.60219 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 892db919-e6c0-3914-a06e-446863741ffa | -14.95305 | -52.65381 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4b49e1a-2590-3ba9-b127-174efe43b07b | -11.14792 | -46.1944 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 442a82c3-4ead-3458-9d30-502bd01e73f0 | -17.9199 | -44.37966 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62cfe972-0ea1-3d87-8aac-f5258e0af3d2 | -11.0588 | -49.50717 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a9bf5d7-4691-3ee5-b702-e0612401be90 | -12.29321 | -43.16099 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a7837f80-cdf7-3dd8-9890-f3e130c997cb | -16.0747 | -48.44893 | 2026-08-23 04:10:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b91fb99-ccb6-3857-ba10-af60016a866b | -14.96342 | -52.65569 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f54aeb33-cb7b-331e-bc92-099a1d34b439 | -14.5803 | -53.02581 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80d325c4-ac53-3a71-a86f-d6c4b5497353 | -11.55689 | -46.95095 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d976b897-9771-3a69-9cec-2827d0492bc8 | -14.13367 | -48.05593 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 71591d29-aa58-379c-b008-3acb3edbba39 | -14.96596 | -52.66996 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa7ff9e4-3b3e-30ce-80be-7d3cd5fb09f0 | -14.39214 | -51.78934 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README17.md)
