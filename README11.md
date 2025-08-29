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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40d1fc5b-8abd-3a0f-894c-85aa2d73e4db | -9.2219 | -60.85842 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7b1ed341-5c27-3b8b-93a3-918623ed9b73 | -12.04525 | -50.64346 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 94b7fd04-0d8d-343e-9174-e385a30a89ed | -5.70596 | -45.95564 | 2025-08-29 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c94a4bef-7a78-3b0b-986e-a7ddfcd0f000 | -14.11964 | -53.96156 | 2025-08-29 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 34126254-82a2-3d7c-9deb-31c7eb149347 | -8.18106 | -61.37042 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 769c24c8-f07a-33bc-a49c-82eabf5beb3f | -13.40619 | -46.95805 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7715ffec-1d71-3f68-af5c-6df92d1e2a94 | -13.67222 | -46.91449 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f4d88995-38e3-3d95-abb8-84e4162d10ca | -5.6925 | -45.95772 | 2025-08-29 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 15b38ff2-50aa-3eee-9abd-2139ecac2126 | -10.37404 | -57.81927 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ceff04c7-4800-3b39-864c-257ac84a6b32 | -10.85343 | -60.814 | 2025-08-29 00:50:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 74c4a766-ad1b-36e9-83f0-92520d7595e0 | -11.57729 | -49.52203 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d17b562a-c6c7-35cc-844d-de3203782ae7 | -5.62105 | -45.02232 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 296d9edb-8018-331d-a694-608830f786ed | -11.42823 | -55.17887 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9732126a-f341-3da2-b287-783e4af44a18 | -12.90374 | -48.13207 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 7f6097d5-f395-3cfa-bde3-effe7a6cb080 | -9.45897 | -60.55314 | 2025-08-29 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 0a279ff6-03eb-3b7d-ab59-dfd1f56af1c8 | -12.03367 | -50.62636 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 00d1a019-05ff-363d-aa5d-fa9fe579047e | -7.63941 | -46.55987 | 2025-08-29 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3e274166-995a-3263-9a11-bcd52fbbf9cb | -16.24041 | -49.87351 | 2025-08-29 00:50:00 | TERRA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86dfca39-4cf5-3e77-a4f3-7b3c4808ceb2 | -10.38446 | -57.8418 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| cc7eef90-8681-36b0-9d9f-26c40c79cad9 | -11.31491 | -43.56034 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 3bcfd049-11b4-3c93-a696-508ec3ac8bc0 | -15.95743 | -51.41755 | 2025-08-29 00:50:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 272999c0-cf6c-3107-808b-2b069aaf13a0 | -11.15304 | -54.30546 | 2025-08-29 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b648e484-611c-3787-82e1-4988aef992a0 | -6.7016 | -49.47294 | 2025-08-29 00:50:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 483fbaf3-3e03-3574-b38a-af80c062d719 | -9.46147 | -60.57657 | 2025-08-29 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 1c360fc4-1db8-3c1e-930a-04b8fc9ce30c | -11.15439 | -54.31591 | 2025-08-29 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52fa6ac1-47ef-3e3c-b43e-d0838837e787 | -9.20926 | -60.86619 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 9d966fb6-b90b-30c7-9603-66531cc5b23c | -10.46258 | -57.93517 | 2025-08-29 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f09d51ae-cc1a-3cac-91a4-6f96d5feabc8 | -15.06368 | -48.3879 | 2025-08-29 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d92dd736-2792-3ef1-944a-021e45d25644 | -9.31544 | -56.91173 | 2025-08-29 00:50:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1ea5df43-6022-3cb0-8923-38ed708f4f1d | -9.44094 | -47.63635 | 2025-08-29 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4bb38760-3b2e-3d94-a2a5-86d6514364a9 | -11.42692 | -55.17259 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 64304bc1-e7a1-3b5d-aa30-e39aa540709b | -10.97315 | -46.8863 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b9caae07-80a7-3a2b-b844-158119b1b858 | -9.68882 | -47.06995 | 2025-08-29 00:50:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f03bafa-a636-3e03-a197-c3a60ee79a75 | -13.59854 | -46.868 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 46958486-cc76-3b8f-a3fa-c093d7bcd659 | -13.57237 | -46.86477 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 28934382-4e1c-3a9b-b93e-d589049f70af | -7.72255 | -50.27797 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 75c39167-5583-3787-a341-7ffc84447ba2 | -10.37613 | -57.83705 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| cf7fefff-48ab-3999-9cd7-ed76746fb9a7 | -7.7334 | -50.28645 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d52aef37-a22b-335a-b3d6-14f4116345be | -14.31793 | -51.94683 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f642728d-d912-3388-ad37-dc2cb278f1b8 | -10.86041 | -47.49804 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0dd4e527-2247-3e80-a935-7f5e4f7afe18 | -12.91549 | -48.14206 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9113fa3f-46d1-3d4f-9e27-a568ba40c44a | -12.03499 | -50.63559 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 25cfc5b0-b9d8-37f8-836c-86b9d4329bb9 | -10.37222 | -57.84301 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bda09205-da22-3ce5-a6af-8bc142e86053 | -13.19852 | -45.30839 | 2025-08-29 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 10a41a9d-d21d-3b3c-a119-2a18b69698de | -7.74133 | -50.27491 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ecd18d87-b4bb-374f-969a-0d1db4f962dc | -13.90321 | -43.87463 | 2025-08-29 00:50:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c5d1a9de-74e3-39ba-920b-38a435ae2b4f | -13.44082 | -46.96733 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 47d306dc-259d-3776-915a-5a89c35bf7e8 | -12.10062 | -44.72316 | 2025-08-29 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7deda153-b0e5-373f-9b72-c8ac4f7ecce2 | -9.49135 | -45.39841 | 2025-08-29 00:50:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9b0fbebf-880d-3c09-81f7-f873b21c3db9 | -12.04656 | -50.65268 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3733504b-340c-364a-9780-ee167980bba0 | -14.36712 | -52.10965 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2aebc436-254e-347e-a658-990c8697d3eb | -8.13094 | -61.21981 | 2025-08-29 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 1b47b5ff-1a17-32da-a190-fdf3c6bc2796 | -13.55083 | -46.9402 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2af6b582-b080-3405-b3df-ecc6cc2e4bdc | -7.39598 | -45.92922 | 2025-08-29 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 177d2004-8421-3e63-aadd-3ee6a51a6e81 | -13.35758 | -54.39164 | 2025-08-29 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a2160ee1-d3c4-345e-8038-1383443a7624 | -11.34948 | -43.57586 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f049ad0d-79f6-3c63-b170-10de8144f755 | -15.04536 | -48.13401 | 2025-08-29 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ae2f661c-0402-30b3-9d3e-e52743f1a835 | -14.24613 | -48.05977 | 2025-08-29 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 09f64367-404a-3936-8594-0f2a835d0d6a | -5.69794 | -45.9635 | 2025-08-29 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| fb88aa45-778c-3ae7-b1d4-1d5f56573c79 | -7.04688 | -44.3886 | 2025-08-29 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3409d1f5-3297-3344-aea6-af0a9d8a65c7 | -13.66576 | -46.87241 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fee8c631-c97b-3507-8a3b-a718bb815934 | -10.01965 | -51.11426 | 2025-08-29 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e645b4d7-ebd4-325c-a555-b9fee4adac4a | -13.41467 | -47.01104 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 381f6f28-ef41-3179-b556-99f99797730c | -10.98533 | -46.89345 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7bd19667-8d14-3b63-bd95-ae88c3ed33b4 | -13.51885 | -46.94759 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3fc4352-0d8f-3d05-b52f-9ce314a93432 | -10.94577 | -46.85968 | 2025-08-29 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b28c6c44-96fe-3913-883a-030318411579 | -11.34462 | -43.54815 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| eed1721c-897b-31e4-abb6-caacc2781141 | -11.5761 | -44.64691 | 2025-08-29 00:50:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9cd13156-0a88-34c2-bc5e-61e7f3b6158b | -10.38836 | -57.83579 | 2025-08-29 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 67f453da-1bcc-37a6-b273-f54cc7da9f03 | -13.18319 | -45.29198 | 2025-08-29 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ed7229f2-75e6-3416-a542-ea327be69211 | -8.17971 | -61.39596 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 819a2039-6e47-31f2-89cd-54b22bfd85c8 | -9.47829 | -45.40086 | 2025-08-29 00:50:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 23eb6d05-f799-3e32-8d23-71f48f1abf32 | -7.0424 | -44.36058 | 2025-08-29 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 704d4fd4-5334-3b91-9b69-591fcb2cbce4 | -10.9755 | -46.90155 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a7424e12-d781-37e3-8f19-fcd153078eb7 | -13.80983 | -52.76093 | 2025-08-29 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fba2026d-c95b-3eb9-ae79-412f8cd5f68f | -9.15517 | -60.93318 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ef6a3d8c-00d8-3725-a20e-b573449dbc87 | -6.54207 | -43.92284 | 2025-08-29 00:50:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 300.2 |
| 5624b280-3a96-3d59-a274-24a1aba6bf42 | -11.38116 | -54.34781 | 2025-08-29 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ae5ae71-839d-36f1-b865-a8203307278d | -11.34415 | -43.55505 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| f7f2f00d-b46b-37ae-a6a7-505e545abb8c | -8.20999 | -49.56309 | 2025-08-29 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d6eca231-d3c8-36d9-b7a4-70665a57bdbb | -11.577 | -46.26377 | 2025-08-29 00:50:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3b5f17c5-54fb-3f5c-90a4-2b537187d254 | -14.3256 | -51.93629 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c325f4f7-0276-3d8e-9eed-b50a4689baaf | -11.23036 | -55.06758 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f30d0a16-e5c8-384e-8686-8da661efc0b0 | -10.84885 | -60.80789 | 2025-08-29 00:50:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c9398f56-aefb-34f5-a9ea-70da17a8214b | -13.02432 | -56.91087 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 32e5946e-5890-3da0-be83-670a269ad839 | -10.86445 | -60.80623 | 2025-08-29 00:50:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| fefa124d-dfcf-3a65-b0c0-98574b4561e0 | -13.03316 | -56.92137 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a9b901d0-4682-33d3-afd1-09e6451de8b9 | -9.16812 | -60.78151 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c1ff0e72-3af7-3742-a1e6-83d79c75e0dc | -11.23068 | -55.07391 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4e90ae8e-93c1-304d-b537-70028a2b9857 | -7.56909 | -47.50583 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8e5d90df-2486-3c8f-8775-8dfc60cd4217 | -9.16614 | -60.77552 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8b14b414-648f-3d07-a900-f4b700ddfd2a | -10.49618 | -51.61323 | 2025-08-29 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 66e6df48-1c18-33ea-9e93-97713d2d39ed | -3.2401 | -52.59459 | 2025-08-29 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3bb7169c-f8ec-385a-9e31-7dd5fc4896db | -1.74552 | -54.5126 | 2025-08-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57e81068-f7dd-3d09-b031-aa6f6cc5bf5c | -5.17379 | -46.07688 | 2025-08-29 00:52:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 7631dd79-d758-38a8-bb17-b108cec0d2da | -2.98159 | -48.60659 | 2025-08-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f5be1279-4892-305f-be1b-1d5398dd27e7 | -4.07277 | -47.95258 | 2025-08-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2b5114a7-1756-3be0-9221-bf83e311cd98 | -5.17581 | -46.05956 | 2025-08-29 00:52:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| abbe8769-3845-3c59-813c-e964b6685843 | -3.41502 | -49.0514 | 2025-08-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 14fc5daa-0a02-3953-be7d-31267d6fad9f | -5.18726 | -46.07491 | 2025-08-29 00:52:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |


[Clique aqui para ver as próximas entradas](README12.md)
