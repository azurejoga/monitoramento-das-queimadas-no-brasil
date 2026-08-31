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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 218708be-4289-3314-9188-3202b9ce1091 | -11.32286 | -45.19354 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 95db60b2-5d6f-3c2a-b545-f5f4fe9bde9f | -10.45563 | -46.75564 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f4765c1b-7b47-3c49-acc8-ecfd68e86dd2 | -10.46758 | -46.54575 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e46f2002-83e6-3577-992b-d6efc2f9b0d3 | -13.84856 | -54.09565 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f6d4d2e2-f558-36c0-9af2-6d2f78814985 | -11.17097 | -45.58969 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 689377c7-2712-348f-b12d-6867251da14e | -11.25195 | -45.10295 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7c265ba3-7f6d-3b63-94c9-8bdfe9b79294 | -10.74368 | -54.03393 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d2bdb6c3-e4f2-31c8-afb0-4f310ddce696 | -14.44748 | -49.00859 | 2026-08-31 16:30:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b53ad41-cd24-3e79-925f-f57a2dbd9f0f | -8.74805 | -46.46877 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d53db5df-afe6-3182-a730-9979da1c7585 | -8.7245 | -45.38158 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ca386084-ac7d-339a-8d86-18f13a9edef3 | -11.6485 | -46.75274 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6706eea4-46fd-35ed-9ef0-39bdd92e884d | -9.30242 | -40.5674 | 2026-08-31 16:30:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 9a128bf9-caec-335f-9568-5afcb5033aa0 | -9.20116 | -47.99415 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f96188f7-10d8-3c6c-ba73-d4831773dda0 | -11.32289 | -45.16672 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 365.5 |
| bd4cb9e4-1ff7-3116-843e-eb120ec0ebfb | -12.09572 | -47.18081 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 975008f6-0994-312b-a374-58af2e6b1343 | -12.92153 | -45.84903 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d63835f2-81d0-303e-a8c7-a7a23582ac71 | -8.42091 | -44.98499 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c0d2b63c-fe23-3fdc-9bb9-88560e0a49ff | -11.7163 | -47.63631 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 313f7899-cf55-3c2c-85be-1e92516682ca | -11.21497 | -45.10826 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 61849bb1-8ab9-3139-b198-5aa000caad39 | -14.57762 | -53.58582 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 49c537c8-7b68-326e-b908-0f9f90d48a44 | -9.41224 | -45.66066 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 98c97e8f-04d6-3f0e-a15d-a586b6e0cd74 | -11.71687 | -47.64056 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c4f43d6b-9837-397b-b8e7-7ed91f8905c8 | -9.59602 | -47.59629 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 42206a8a-ad78-344e-a33d-f1ae6b9a3a3f | -12.09982 | -47.14767 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6397d4d5-e975-3e6b-8e26-46e736c1ba77 | -11.2012 | -46.09583 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1c0615f0-f7af-3bc6-aafd-854a433e35b9 | -10.98831 | -49.68971 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5e268502-ecb6-3b01-96e6-840a9cc695b3 | -13.54829 | -48.24112 | 2026-08-31 16:30:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 03e9bdae-2823-33bb-ba35-efb763cea58c | -14.64383 | -53.57311 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 537e6547-9b2f-3e69-9350-48364a16cc0d | -10.98963 | -48.38383 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e0907b59-59a0-3392-8245-19e4677428be | -9.98047 | -53.92694 | 2026-08-31 16:30:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 32130f10-0ded-3d74-8824-9df7cc0169c7 | -10.95972 | -48.40946 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d53b0de2-4835-326a-900d-07b88b9dd65d | -10.34981 | -48.22633 | 2026-08-31 16:30:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d5606b4-6589-3f53-be82-2e859417c247 | -8.86031 | -47.08101 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ce5f7ef-bd24-3afc-baee-f26bb1e6f26a | -8.76666 | -46.46082 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c113d8c6-9113-3c92-8d2f-8b94a355634f | -11.91296 | -45.04462 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 501a3ee3-cf10-3cd5-99c9-34b259a8ac6a | -10.73434 | -47.96526 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ff6560f-b097-3868-9788-8b3f15e51123 | -10.85384 | -45.33084 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 517f1737-38a5-3eea-8a3c-b70dd382ef1c | -14.21702 | -48.63934 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fb748f98-686b-3641-887b-a7397c7e725b | -9.6029 | -47.6154 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b118285-4945-31e3-8a7e-4a83da0eac14 | -11.93386 | -45.08599 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 79eed75a-5c19-348b-b8ca-cbc0b85f8606 | -11.16825 | -45.04354 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 74e792ac-a57d-3af1-9736-a6280de5b62d | -9.66504 | -47.94563 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| caf97075-1d2d-3138-921e-ef8c8e496f1a | -13.19979 | -44.07195 | 2026-08-31 16:30:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5fd1c5b6-131a-31e2-a361-3748f11c0e36 | -11.34209 | -45.22235 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c66c823-1ed1-3a6c-8879-8ab2cd9575f1 | -11.54233 | -45.47638 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f4e02b34-cfe5-3139-8526-564fb22f6c81 | -12.09189 | -47.15282 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3a8e6c4-44ab-3087-ace7-736daeffb0c4 | -12.07346 | -47.20823 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f7349999-0faf-31fe-9cc4-e32d55a94031 | -9.58763 | -47.62924 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 98c0ccad-4421-3648-b6bf-7a49e59b9dbf | -10.33179 | -49.95268 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dbbc3376-7ee7-3f14-a76d-03c6338f039b | -11.26105 | -45.06133 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f3c9a869-36bf-30d3-8192-74551dc29e11 | -10.82209 | -50.6808 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.8 |
| e5910eea-43aa-3892-bfd4-3c66de7d394f | -10.12375 | -50.30132 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3353edc2-71d8-34a0-bdbe-0ac39c25ebf5 | -12.10466 | -47.278 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 55a67efa-bee3-3951-932a-df6196d456a7 | -9.78321 | -46.60984 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b456edd-2369-3872-a698-15541521f548 | -10.3271 | -49.95535 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| db4b13d7-2cb0-375e-a06c-89b60e2c0a22 | -10.15212 | -45.69758 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8d4ec170-ea11-3afd-bbb5-38fd22f16a8d | -10.4511 | -46.75262 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 33cc484e-df8a-3ef6-89f1-139e86b89d88 | -8.76071 | -46.44698 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 659eb731-b6c9-3f22-994d-bbd7afb06103 | -10.56206 | -46.16656 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1d8f338d-041a-3789-b99b-5f8175c0ab48 | -11.79852 | -44.8841 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 708b124d-2c0b-3312-9d02-04de58869aca | -13.27355 | -51.60075 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3fcea81e-2a26-321d-8f8d-62bf30fca01d | -11.63041 | -50.18091 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d03651fe-b9f7-3341-af56-efd3dcb4f6cf | -14.79644 | -48.26802 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2d81a074-1629-3756-abc6-ebdb51ef4e64 | -10.82719 | -50.63695 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 55a737cd-8a36-3997-9161-6ca9757d103c | -11.24642 | -45.11709 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 15c3d444-a5a6-3e35-8d88-dfc83d37a31b | -11.37191 | -45.21819 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4f35ed53-06b1-37bd-be6b-120cbcd5b003 | -10.84343 | -48.33929 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| caf79893-f39b-316a-940b-e0866a7d4779 | -10.54814 | -43.92201 | 2026-08-31 16:30:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b28e126-b199-3fda-b82a-ebda5f1d8d4f | -11.24949 | -45.35355 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db233421-ffc1-31a0-bf04-fce07b5a3a02 | -8.39604 | -44.98901 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d650e1af-e600-3546-8212-5ea31ad2f47f | -10.83613 | -45.99221 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 142425e2-74b3-3891-8f65-7840b9be6ad2 | -9.6013 | -47.60359 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8fade7ed-b838-38ad-a10f-3544146e2d22 | -14.4168 | -53.09895 | 2026-08-31 16:30:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cdbf664b-0115-3bfd-adf7-7b5351e58d97 | -10.79976 | -50.71709 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5fb019a3-c04f-3e32-873c-247dca762a2c | -10.5712 | -50.3861 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3748c0e9-c631-38b7-ac77-37bbc853f525 | -10.0832 | -46.62352 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d27c97c-6951-33ba-bf8a-2e2f77d407a2 | -10.34368 | -49.96492 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d48c6ab8-b7f0-3573-b92f-6138dfadfbf1 | -10.83432 | -46.00743 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1ca071f7-be8b-366e-9961-ec4c036bf1c0 | -14.5643 | -53.58763 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1c3507e1-4fa0-3d9b-a473-f696f21e68a7 | -9.44392 | -45.6632 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7a83f282-ddd5-362b-900d-91d7e7cd8437 | -11.35518 | -45.23425 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 75fa0ba5-7884-309e-a619-6e2e110d9c9f | -14.44836 | -52.51164 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 22a94880-d300-33f4-86c7-1418056a6e78 | -15.28124 | -53.87753 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 75a90da3-4b8a-3763-95ff-be2a8c8a506c | -11.32225 | -45.1892 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5bcdca8e-fb37-3562-a51d-143a9c9795a0 | -8.66252 | -39.6588 | 2026-08-31 16:30:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 838b9b7a-d6c0-3487-85c3-a07bed828e92 | -8.93431 | -45.03437 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7520a868-56e9-39ef-ae13-d3eed29257b6 | -13.26786 | -51.60067 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 65da5d4c-a8f5-3385-93b9-3364367e6759 | -15.50594 | -55.13935 | 2026-08-31 16:30:00 | NPP-375 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5e9d550d-82a3-3a33-afe0-95e14376cfb3 | -11.24804 | -51.25561 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b20f072a-49d5-3273-82e6-5b1490bd5763 | -10.56562 | -50.38366 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 6a204a76-6a74-38f1-9bce-3d775ba4f849 | -10.33211 | -49.95472 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c0bd15de-d613-3a74-9d7a-b2c9884c52a1 | -11.24002 | -51.24497 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 998f9bfa-23dc-3ac7-a23c-6bc2f53de07b | -13.54767 | -48.23618 | 2026-08-31 16:30:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| dc371cca-3d91-32f4-8df2-30f3d772550c | -9.7839 | -46.61483 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 19ee840e-7b10-3faa-abce-9ea1dfe53b90 | -11.58101 | -47.72147 | 2026-08-31 16:30:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7d2277f9-7b9f-3150-9042-9c2328dc551a | -15.27562 | -53.89069 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ad677c3f-cb56-3766-b7d2-5a5efe3cb2cf | -14.64678 | -53.57336 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a171136a-f08d-3248-91e0-cb5ee13b32a2 | -8.92008 | -44.17143 | 2026-08-31 16:30:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 52bdb8d8-f63b-37c8-922c-eaffe9da2ced | -10.82148 | -50.63436 | 2026-08-31 16:30:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 5beeb7cd-cfc8-352f-968e-d2bac59a19ef | -11.49199 | -50.34237 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README126.md)
