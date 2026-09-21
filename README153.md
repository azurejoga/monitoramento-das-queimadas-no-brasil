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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db2c9ca7-c617-32c0-bd09-f406afc761ba | -10.24912 | -49.99646 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1e24449d-de75-3443-963f-42e4ecf17957 | -11.68095 | -43.44257 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 154ee494-00f7-333c-ab5f-3adf31b594b5 | -12.06023 | -50.06201 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 14d2ff48-7510-32a3-9a09-71d9ffb929f3 | -9.01135 | -44.34846 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a4b15695-2d99-31aa-b6e2-592e1992a2bd | -11.3562 | -43.15418 | 2026-09-21 16:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| eeed3c96-8c35-3abc-8d02-2885031e3766 | -10.73381 | -50.7932 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| cbf2d1e6-d76f-30b9-ae35-baed6b321a63 | -11.65157 | -47.77065 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b6dac6c4-517d-3379-972a-63017e241ad7 | -12.44672 | -47.05381 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 90d685c5-925a-367e-85c3-5f860adfe857 | -11.10404 | -48.30599 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 35a78293-a5d4-3985-a61f-ed8395df69df | -9.54218 | -46.52566 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4c2b5006-e7d4-3fc0-8625-585612849f08 | -10.6203 | -50.59829 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3e325d74-0aae-3a53-b28e-3d03a8cab334 | -9.75401 | -46.05996 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 868e08e9-881c-346d-834f-e5b6910e827f | -8.70173 | -45.44278 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8337a424-318c-3c8b-9979-6a92ae05f222 | -10.69217 | -50.67981 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b257bb75-6a99-3863-b949-a239b5bb90eb | -10.84266 | -50.15798 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 7824c336-0d38-3c7f-9464-48a7709ea429 | -11.14725 | -42.8176 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d7a71b12-7913-392b-a490-a4e3e1917627 | -9.86991 | -48.47253 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7ac70d94-f056-33b2-84dd-f3a782558436 | -10.38967 | -48.89624 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cfc6a756-7436-3df2-92d7-7fcd19bf6354 | -12.44532 | -47.0416 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ec92eb8-e559-3ac6-a597-f5e3588b460e | -11.37563 | -44.23136 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dcb80b4d-e82f-3e7c-9b70-81df99780807 | -12.82347 | -44.22257 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1f8aa151-df27-3c29-a622-8d57f1000170 | -10.99266 | -46.51447 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf344af3-51fb-3924-890b-c95522bc4ec1 | -11.43677 | -45.35478 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 79723e36-c89f-3dfb-b627-708976b28fdd | -11.08429 | -49.74341 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| a79901f0-6845-30eb-b87d-a7f79a88da05 | -11.64251 | -50.21656 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1328da1f-1fca-30fb-a807-dc6a911d2232 | -14.06191 | -42.16559 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9788e68a-4e90-3671-b88c-16ece9c98753 | -12.54767 | -50.03128 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 392554da-16e6-3c91-a5df-afbaf6783753 | -11.64929 | -50.21497 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 893fead2-b329-3af0-9a07-af1d1c2e24ab | -11.67865 | -43.42467 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 45a99907-fe29-37a0-a047-3bcc8459c3cd | -8.24433 | -37.40154 | 2026-09-21 16:01:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 67781ace-efbe-3efb-a9a0-43db430e1620 | -9.61154 | -43.938 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 834882c4-76de-388c-8b48-e855f58eb3fa | -12.05472 | -50.07556 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 4ae53a12-6de0-3477-9287-ce10643742e5 | -10.72223 | -50.70787 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 49927b52-a3ba-389f-a27c-29b3be239cc8 | -9.95975 | -45.73486 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a824026d-195b-3a26-b37a-259de439a952 | -10.38518 | -48.91192 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| eec6e44f-6ae2-3caf-9c20-574c1afc6cd0 | -13.55096 | -44.89065 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9533e11-b68c-379d-b410-67b53b92cec5 | -12.42142 | -47.0363 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ec827d30-1ce4-3130-a2ae-9d8aaed10467 | -14.12278 | -45.55225 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9900fc94-08e1-31e0-b418-7afbb5738569 | -10.98154 | -48.22243 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c412131c-d43a-3aa1-b3eb-8c9abe9d8ca6 | -8.78093 | -44.26988 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 49447046-fac7-374f-8fce-3d777f6206e4 | -10.20684 | -44.15655 | 2026-09-21 16:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b67ad3d8-94d8-327f-af93-58d964acbc3d | -13.90179 | -45.48767 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6f142d0f-1114-3101-9848-f33c8676f33f | -11.603 | -46.96951 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 00285348-7eb8-3f42-8ae7-396eba354bcf | -11.81032 | -49.84495 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 42c0b86c-8aa2-3059-802a-73eb252851e0 | -9.74436 | -46.06682 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64f52188-840f-331b-966e-681152857363 | -8.49637 | -37.0265 | 2026-09-21 16:01:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 84046dd6-3b4a-303c-96a9-38ab45d3fb7e | -10.82073 | -50.14767 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3f0815e0-7bf5-3810-9ea0-3f3ba7ab4fb8 | -14.10389 | -44.83559 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7a333e26-a9cc-3b54-b65a-4fd25ff4b1c8 | -9.9111 | -45.82661 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf6120ec-eb5b-372a-864d-6c33ad40915a | -9.5338 | -47.94695 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2c44ad7e-9304-3a62-8b8b-d624040ad0aa | -10.94792 | -50.58085 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 549e2526-36e9-3334-9a39-cea0086c559d | -10.80779 | -50.15545 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d4abdd1a-ccf6-35a5-82b8-536359b15d06 | -10.19707 | -44.15321 | 2026-09-21 16:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5140f2e6-c86b-306d-aa59-b05456d5d243 | -10.07706 | -50.27195 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9cd4960a-98a1-31ec-acd6-9fd52bafe8e9 | -9.44901 | -45.41361 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a3758bdc-746d-325f-8c74-136450bf01c8 | -10.69525 | -50.76923 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8bd911f1-f635-3e8d-aa37-9d8a3bceba7f | -9.01913 | -44.9962 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9cd0d949-7243-3b9d-b1c8-ac961f630e4d | -13.90258 | -45.49434 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b4560fe5-021b-3013-b8f1-6f89cfd2de41 | -8.68544 | -45.31775 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 296a186c-9243-3689-ba51-b4c984a7caee | -9.31223 | -46.61217 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b0b7081-50e7-3301-9694-202246c5822c | -9.39331 | -48.32392 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8b23b7f3-371b-37e3-a9e5-f8276828963e | -10.55706 | -46.55019 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 933eb94e-dba5-3750-b91a-0191bfd92a79 | -13.22958 | -46.9344 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 087b252e-fc84-35c1-8853-14ba1bfb432b | -7.39944 | -34.94518 | 2026-09-21 16:01:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 3c73f4d6-877e-3074-8249-9bb2ffce47f4 | -10.38457 | -48.9069 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| dbb23333-0a60-3746-af21-52144d0dd4d1 | -12.38026 | -46.9977 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e005c4cb-076b-3aab-a251-836259ff0f28 | -10.37885 | -48.91245 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 34a46ebe-7393-3b19-92a9-674323e95efc | -8.76314 | -45.87074 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2e67df16-e300-3e95-a962-f51ae45cc132 | -11.96378 | -46.51546 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 58429609-68c8-30a2-9135-9352c1c6fa37 | -10.8351 | -50.15243 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 91d0c040-49a2-31dd-bf66-760dc8c2ad68 | -9.4238 | -35.96956 | 2026-09-21 16:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 0400b038-446f-3bae-a5b6-ff4601823320 | -10.40634 | -50.3362 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 301c41b1-94d9-39f1-98aa-9a6001d8b329 | -10.72416 | -50.791 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 85298298-32c3-3fa4-888b-7c724f5329ac | -10.9487 | -50.58756 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| f5b5a4dc-ebff-332f-9d91-dadda19433f0 | -11.6742 | -43.42526 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 50f70279-098f-33f0-8b39-cfd75e21b0ef | -10.08488 | -46.16998 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e46e08b2-0969-3071-a96e-83fe1d8adb49 | -9.96563 | -45.74035 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3e144cb0-a51f-3c77-acff-020b0ddbf06a | -11.07316 | -49.74201 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3719a3e8-5db6-359f-b824-cb9e8a210757 | -10.75364 | -46.33213 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fd15ad52-94e1-3b48-adf6-055d4f593874 | -9.95273 | -45.68033 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cd27f5c-d79c-3e2b-b36f-12bb30992c53 | -11.65359 | -43.432 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fcc59bb-3323-3140-a194-b0ff50b46a5f | -14.86503 | -49.21027 | 2026-09-21 16:01:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 31e3ec44-f28b-3f27-9c3a-9fa1a142818f | -9.96524 | -45.7373 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 83ed0e1f-8813-334c-bf2d-1655036e68ff | -8.46037 | -45.86333 | 2026-09-21 16:01:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 10e4eb6f-53a0-3eea-aab3-65c30dd078c1 | -11.94064 | -46.50902 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c2248695-0b2c-33da-87ef-a0ed659d92d2 | -9.90348 | -48.44405 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 78c0b5ff-36bf-3d8b-97cd-0b3721824e9a | -10.25185 | -49.99153 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 308cbce6-ffb7-3772-9e45-4be3942c4295 | -12.43587 | -47.07321 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ac80ab1c-81a5-306f-af57-3e4d09fe30ad | -10.75166 | -46.3336 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6f7285df-ae51-3f4f-8fcd-f74f86a8e395 | -12.42877 | -45.05209 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eeb4cbdd-212a-3675-9f2b-4fb4565a1eb1 | -12.40317 | -47.04369 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d7b1b509-2d8e-3ec6-8dcf-cede0ff7cda4 | -10.35621 | -50.20773 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 27199328-45eb-3790-ac23-ecca1f1745ee | -13.28474 | -40.39148 | 2026-09-21 16:01:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3d1af67f-483d-3c2c-b5f9-1eb6204b8a69 | -10.56059 | -46.56281 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ca8c18a2-6d03-354e-a3c0-5a0566c2a331 | -9.01662 | -48.15801 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b610b1dd-a1f5-39cb-87dd-5c4b84ba31d5 | -11.43771 | -45.40292 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a6b364a-ceef-33e3-84b4-38ecff113dd7 | -9.84703 | -46.40043 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e48992d3-8a89-33fc-8029-b96901460536 | -13.03229 | -50.60175 | 2026-09-21 16:01:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 261913ab-7105-3185-84d7-4a92e79e7b8f | -11.67822 | -43.45661 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 3691ba32-32b3-3a32-9d8e-d4aca232e831 | -9.21701 | -44.62062 | 2026-09-21 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README154.md)
