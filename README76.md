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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f03577b-1463-3470-aeb6-168c84b72d37 | -7.082 | -42.1346 | 2026-09-15 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 151ee49c-8d71-39cd-bcd3-fd8a92d83c51 | -10.792 | -46.2071 | 2026-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 69037751-1fce-36ac-b80d-f64d1f3bdcc1 | -9.1337 | -65.844 | 2026-09-15 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a6df2962-231b-344a-a0d3-69b83cfa79d4 | -9.5915 | -46.5989 | 2026-09-15 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 57ba8a40-9534-302d-a53b-b4a489d0d8a1 | -15.539 | -53.8502 | 2026-09-15 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1e1311b8-3c63-3114-a16b-fa273f991fd2 | -10.6962 | -47.4953 | 2026-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d0159d1c-bf39-3163-9979-4d088a210397 | -2.9209 | -50.4208 | 2026-09-15 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ef1f221c-4202-33c6-b0be-38c809e1b789 | -18.1709 | -51.7685 | 2026-09-15 13:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b806b387-931d-37d3-bb16-17602fd7ca3e | -5.144 | -55.9345 | 2026-09-15 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 1adaa43b-c47f-3305-aa6a-2d140103b3e0 | -11.2113 | -54.1208 | 2026-09-15 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8885d30d-b10b-3493-999e-5908b9bbc921 | -8.5468 | -50.4423 | 2026-09-15 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 299.8 |
| 7e2a7b8d-1169-33d1-99eb-9840d41924a9 | -2.6602 | -57.5119 | 2026-09-15 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9cf99e98-b017-3f7b-b8e5-0126200a6e35 | -8.638 | -44.4567 | 2026-09-15 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 56f8f327-3306-3d42-904f-b0379127fa79 | -9.3763 | -50.1139 | 2026-09-15 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 27856915-6ac2-3166-93c8-e641ef09cc5e | -13.7002 | -51.8274 | 2026-09-15 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b37e4123-485d-381e-9ba1-ddfb277ad73e | -7.0164 | -44.6413 | 2026-09-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 2392d202-fd5a-308b-837f-4ec8285cf0b4 | -7.0823 | -42.1107 | 2026-09-15 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| 56170c57-343a-3839-89d6-9276d3617275 | -2.6601 | -57.5507 | 2026-09-15 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7c5150b0-e647-3dd1-a94b-8c67a9b3db3f | -11.5045 | -45.771 | 2026-09-15 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a088bd17-9888-39e7-b882-27775d166595 | -9.3572 | -50.137 | 2026-09-15 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cee4dda5-6c39-3a83-b263-2e3b830584e1 | -10.3116 | -45.3136 | 2026-09-15 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8cf3efd6-7350-3c3f-aec3-0b43e0fee55e | -2.884 | -50.4219 | 2026-09-15 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a8a2258e-17d4-3afd-bf0e-3e8082e27e32 | -9.3572 | -50.137 | 2026-09-15 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 8d1abfd9-f00a-3c9c-bb7a-947d3c1cbbe1 | -9.4234 | -47.8588 | 2026-09-15 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 413c343c-7bd7-36d1-aaf5-bf4350885db8 | -10.3113 | -45.3366 | 2026-09-15 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 468.0 |
| 0c5a7c52-1449-3c31-844a-0b0a9bd43bf6 | -6.8405 | -43.5254 | 2026-09-15 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 93be20ae-b14c-3c30-85cd-dfd430f53084 | -11.0434 | -49.6851 | 2026-09-15 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b79e3147-97d6-3871-9331-a2f4f188f8f7 | -2.9025 | -50.4004 | 2026-09-15 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f1c7e59e-a6e1-3087-aa8a-9c5cd718f58a | -2.9025 | -50.4214 | 2026-09-15 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 5cc4e497-e3ee-34b4-b56f-fe09aac7d76b | -7.0164 | -44.6413 | 2026-09-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 5f715590-6aff-303d-8f6e-fa3ce9f7b04b | -11.9033 | -43.8112 | 2026-09-15 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c0eaa5cf-cce5-365f-8cae-a7e2d35cd537 | -13.3062 | -51.2808 | 2026-09-15 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0ac639e1-6e40-31cd-a1cd-6fd0d7948ccd | -10.9875 | -48.3209 | 2026-09-15 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| e6c8ce7a-7b93-3e11-852a-5cb29d31f5c1 | -13.7726 | -48.7866 | 2026-09-15 13:40:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a15efb9c-e42c-3479-a443-99a26e3e1665 | -10.6829 | -54.1475 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7677d295-babc-3d85-a356-9d4e073d14a7 | -2.9209 | -50.4208 | 2026-09-15 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 63d20cfa-94de-3dbb-9acc-b04c2b18723f | -7.082 | -42.1346 | 2026-09-15 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 693f5d27-9d31-381f-b407-0fd85370c139 | -8.8137 | -46.905 | 2026-09-15 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 80aba522-fd07-3ca5-a192-ed787650c4e1 | -7.0166 | -44.6184 | 2026-09-15 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f6d54e70-f207-3ee3-9177-4a2f5fce791f | -8.638 | -44.4567 | 2026-09-15 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 233b68fa-d9fc-389e-9bb8-b55d8d245d9d | -10.312 | -45.2907 | 2026-09-15 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ef6224bc-6793-3a03-9bbc-f95f56a51183 | -13.287 | -51.2832 | 2026-09-15 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3232b7fa-7d10-3cc6-9f1e-b34bcb74bdc8 | -18.1714 | -51.7466 | 2026-09-15 13:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 4b94ada7-4217-39cb-afd5-8279c28f89db | -11.5045 | -45.771 | 2026-09-15 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e4f0cadc-f0fa-3775-acc3-32c745c5787a | -8.5656 | -50.4407 | 2026-09-15 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 9dd20642-10ee-3d90-8fc3-3e7799b939ab | -9.7358 | -47.0958 | 2026-09-15 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3798342f-80a2-3def-81da-e46e09b85d7e | -11.2302 | -54.119 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 45f9d76e-fd31-3431-a578-4eb8930a718e | -18.1709 | -51.7685 | 2026-09-15 13:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 80db8b78-a3f5-3ec7-aa8d-10181ee00ae0 | -9.238 | -46.1894 | 2026-09-15 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7a8b4150-3d05-357f-ab35-558256e6f76b | -8.5468 | -50.4423 | 2026-09-15 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 54544db5-7a0d-364f-b8b6-e59a24fa0b1d | -9.494 | -45.459 | 2026-09-15 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a7b917c0-7153-3507-9df5-d764549bf236 | -11.8154 | -46.5899 | 2026-09-15 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| ac7e7959-dbe1-3375-ba80-c3808c2edc37 | -11.2304 | -54.0985 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 9f2eedf1-5863-3d07-a60d-e91661392d56 | -9.3577 | -50.0943 | 2026-09-15 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 58a7e334-a22c-3ad3-8732-a3db90ce9162 | -10.5788 | -47.7306 | 2026-09-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a10ee66b-2598-3c1f-8a99-0739b6810bd3 | -13.7722 | -48.8087 | 2026-09-15 13:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 07fc1acb-168d-3676-a2bb-301851b210e8 | -9.3575 | -50.1156 | 2026-09-15 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 3fb39938-973a-3121-a1a0-9d6f91ecde1e | -2.921 | -50.3999 | 2026-09-15 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6a629503-17ec-3edf-8e57-2fdc3bbf36b0 | -13.7006 | -51.8061 | 2026-09-15 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9b2d63db-f93e-309c-8101-776451368946 | -11.2113 | -54.1208 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 177.5 |
| d621e47c-0c83-30e4-91e5-1df98f00a51f | -9.3569 | -50.1583 | 2026-09-15 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e789eb22-0197-3855-8c41-c06adec47600 | -10.792 | -46.2071 | 2026-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 0945643f-c399-37f9-bc97-2d1007a473d0 | -2.7768 | -49.4553 | 2026-09-15 13:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 945523d7-fab5-3ba7-862e-3061289859a7 | -4.5229 | -54.9639 | 2026-09-15 13:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7a5fdca7-c3f1-38ae-9676-b8513897d8c8 | -9.475 | -45.4612 | 2026-09-15 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 82f102ce-2a15-33ce-ba0c-944ee71e39b3 | -10.5785 | -47.7528 | 2026-09-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1ab66350-f696-35fe-83ea-66ba4d5e6bf7 | -10.3116 | -45.3136 | 2026-09-15 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 58fa2cd4-746d-3326-b46c-36f6826af6d0 | -10.2922 | -45.339 | 2026-09-15 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 0b716f6c-9578-344f-a036-a73f0104c1e5 | -10.3109 | -45.3595 | 2026-09-15 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 293bcea0-4067-3688-866b-10fa52fc79b2 | -5.144 | -55.9345 | 2026-09-15 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 99a89280-3663-342c-bdd7-6e4f93954b8d | -15.539 | -53.8502 | 2026-09-15 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 6447421e-80e0-36d5-b03c-b00fbb395d51 | -10.6641 | -54.1491 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 017edafc-83c0-31fb-ad4f-7923d99ef9cf | -13.2232 | -51.6744 | 2026-09-15 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e2841e6e-2850-3eda-886d-83bb14c9f001 | -9.5915 | -46.5989 | 2026-09-15 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 3ebd0e76-8ecb-3db4-bfa5-5da8a241db12 | -3.8372 | -51.8875 | 2026-09-15 13:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 10584424-553b-32b1-9d83-607c686eedb7 | -7.0823 | -42.1107 | 2026-09-15 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 5a2856de-4e18-392f-85c9-b19fe4d7c488 | -5.1256 | -55.9352 | 2026-09-15 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| eb33df57-f99e-3d5d-b40b-bcdc0d21ce65 | -10.8665 | -46.3105 | 2026-09-15 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 8111cce5-e8c5-3c6d-a3d9-ed8c9557ee4a | -5.1255 | -55.955 | 2026-09-15 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 662087af-b758-35d0-8b31-189a6b53a70c | -13.7002 | -51.8274 | 2026-09-15 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b9f288a8-4d1f-36f1-b97c-2d25ba40c407 | -10.9685 | -48.3232 | 2026-09-15 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4cf0ffe3-15f8-38c6-a021-7c6f520acdca | -10.6827 | -54.1679 | 2026-09-15 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| faf7d9e3-2a39-388e-bc8c-860953db0160 | -9.7687 | -46.1067 | 2026-09-15 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 609cde70-9f32-30a6-aa3e-057231a2f037 | -11.5041 | -45.7939 | 2026-09-15 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| aa9fe317-a723-366b-b7d0-d90584559bc3 | -13.2867 | -51.3046 | 2026-09-15 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 0a43f702-8a5e-3890-a172-76d2a6d14ba3 | -10.312 | -45.2907 | 2026-09-15 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e59ed1c0-7beb-3837-beb6-1be62d8a879c | -6.8405 | -43.5254 | 2026-09-15 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9a1b1473-30c0-3ece-9921-c5d876f6dedb | -5.1256 | -55.9352 | 2026-09-15 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 6afaa6be-2eb3-3480-b36f-c201ba40f3ab | -14.6779 | -48.0016 | 2026-09-15 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 297448d3-a881-37ae-87bb-1d9862ca3611 | -8.5656 | -50.4407 | 2026-09-15 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 64f6c092-0ec5-3b84-9c35-60bece15b08e | -13.287 | -51.2832 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| e85166c6-1656-3a1e-b740-a5849aa33009 | -9.1337 | -65.844 | 2026-09-15 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c7ff1712-6a92-30b5-9fff-4de8e1ef1d90 | -7.1711 | -44.2367 | 2026-09-15 13:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 502.3 |
| 1259188c-1663-33fc-85c8-31f36f291b81 | -2.7149 | -57.608 | 2026-09-15 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 012aa637-3cc9-3065-8143-544b1f222e8e | -11.8154 | -46.5899 | 2026-09-15 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e08826c8-5873-39cc-89ac-e5e8f5857cbc | -11.2302 | -54.119 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| f9161b14-afbe-3825-839d-2e7921346f50 | -13.2867 | -51.3046 | 2026-09-15 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| fb3b4e6a-9200-37ea-bffe-a6fc57799128 | -10.2922 | -45.339 | 2026-09-15 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 280f67a6-953d-33f9-aa9b-2bdca0747342 | -10.6829 | -54.1475 | 2026-09-15 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 019d6725-b817-3244-b1f4-d712d4353bb1 | -9.5915 | -46.5989 | 2026-09-15 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |


[Clique aqui para ver as próximas entradas](README77.md)
