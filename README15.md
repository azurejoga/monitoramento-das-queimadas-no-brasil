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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7925321e-6ef9-35fc-8aa7-8eccd5a743f3 | -11.31358 | -46.30093 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c074a17f-3561-3d1c-921d-0bc9c3cb5da5 | -11.14604 | -46.50119 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733e46dd-f2a2-35c7-9a6f-046d275bac7f | -7.38515 | -55.48371 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c6100a5f-f303-30c3-a94f-5be33a20912c | -11.6157 | -47.79585 | 2026-08-17 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e172e5ea-1588-3665-af15-539d6b61abc3 | -6.86289 | -56.41603 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bd56d6f-d042-3b68-82de-b6b3aa25efa1 | -11.39705 | -46.39785 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae7e4621-abf7-3429-b1a9-10e8d0d89455 | -8.37323 | -46.37566 | 2026-08-17 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cc9b10f-6e74-36a4-8164-f52c824af94b | -12.22976 | -47.04359 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 117348ca-02e1-3748-b5d1-9b40d0e81530 | -11.70107 | -54.61245 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49fa7a7b-7827-302e-8a61-e6cff1b497a7 | -7.90686 | -48.52724 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e28c0c-7010-3a4b-8ed7-fa8ebce859f7 | -12.66876 | -48.5083 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 46168484-a6b9-32ca-8618-7d951d4d73e7 | -7.38447 | -55.48484 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e2cd21b-edc6-3bf7-a210-b10dbdb3c58d | -11.40091 | -46.41647 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b3506cf-a7f8-33ba-8e37-4426c69c2fc6 | -12.6831 | -48.44311 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 905169d0-596f-3826-99bb-19a0c3b5521f | -15.15734 | -48.61442 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d54624-156c-397f-8d96-9c227fa8ce9c | -11.40974 | -46.40356 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b64b96b-38fc-3621-9d2c-afcebf36de07 | -11.14154 | -46.52951 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8b91dc-e4af-367a-80d7-bc1dbed98ca2 | -12.66528 | -48.50779 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 18814c32-f168-325a-b92c-84f41e5a2876 | -13.5194 | -46.28498 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e15563fc-8cc9-3826-9d40-dfc6e46ee610 | -11.22775 | -54.01611 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fa2232e-4009-334f-b81c-d1dfe1b23c4e | -8.67258 | -54.76334 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25ac22cb-319c-38ca-9b5b-3a45dcf060a6 | -8.73478 | -45.31038 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f66dec70-31b0-345c-ab4e-01268f1fafac | -10.46948 | -46.30484 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d94bc9d3-ae1e-36ee-98ee-99208ee5dd87 | -10.50796 | -50.01913 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| ccaf0489-bf4b-3a0f-81d7-9889b58648cd | -14.48651 | -51.97935 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 553682df-e9d5-3eb2-85b5-f87e8dea8826 | -13.51937 | -46.24157 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c346e5c8-61d4-30f0-90f8-06418d54011d | -6.82935 | -56.45963 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1ac5342-2c36-35ce-b6c3-7a40b0626820 | -11.78943 | -51.78814 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac32d22e-113d-3233-b944-e0cc5ea3b635 | -8.03494 | -55.1416 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c508a35d-683d-31d6-be4f-1b1c5fd156a8 | -8.09591 | -46.90345 | 2026-08-17 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a51647-db16-3bc3-accb-794844a2644f | -11.99785 | -46.42735 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1db102a6-4093-38f1-ab02-eac454ed82b8 | -11.71912 | -54.6002 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bcaf340-e3fd-3b8e-b101-dd1e9a0c7070 | -8.64318 | -54.71109 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab2a03f0-c2ec-319d-a568-821bd4c76a21 | -14.30745 | -47.20054 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ef6aede-d91d-3a55-a31a-610b894aec36 | -9.60054 | -46.03484 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91b837b6-2be8-313a-9319-a7181dc186e9 | -13.52326 | -46.30372 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdcd931e-0b2c-3a37-8074-d82e080fa2d8 | -14.09327 | -53.60776 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fab53f73-a7ad-39bf-891a-3fc9a5047c4f | -8.51647 | -54.90324 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c543df7-b8f2-3b70-a60d-70ff40dcc97d | -14.05828 | -53.69412 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94240d62-9000-344c-96a9-5c2e60d0c6e8 | -11.22425 | -54.0172 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 965d7231-9a18-3106-88ee-71c902139bf3 | -7.37981 | -55.51235 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ad42e85-d39a-32bc-843f-54a3c21d310d | -7.53351 | -55.58741 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 733c5f61-534b-308f-aa92-2ebc7caca0cd | -15.08983 | -47.02691 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490d1c08-c356-31e0-a772-ed1d4909d236 | -12.66743 | -48.51627 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 48fa0088-b5a7-38cb-9b24-8ee12ac909b2 | -13.51113 | -46.29451 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e27252b6-6d52-39d7-854e-030603b20fe4 | -8.58425 | -54.68499 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e0ac8882-2e52-3e40-8600-9c603889d556 | -12.26521 | -45.91193 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e12828ff-15bd-3c44-8200-433e5bcff5ff | -11.50462 | -46.59951 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3bc89bd-a90e-382c-920e-94739b8d8a79 | -11.28875 | -45.80844 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cada3d02-0b83-3b35-aa07-d8a954bc85bb | -10.51341 | -50.01019 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47d8667f-5e31-39c8-84ab-c59876b09889 | -12.54955 | -47.86583 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da950d6b-09af-37bb-bbeb-2373bd1e0c66 | -11.11689 | -47.25577 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76fb2477-6fa5-3fd7-9c82-60ca97f8a24b | -11.70049 | -54.61549 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f385793-4278-340a-8007-c3f5d0bfa90e | -15.12939 | -50.05181 | 2026-08-17 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7d33616-760d-3b5a-afae-93850cf89031 | -11.80874 | -44.80978 | 2026-08-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 75d631af-2d7e-3f53-b729-201f133f3f03 | -10.50494 | -50.01366 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4fc07f0-9f1f-3c19-adb8-cf23b87676e0 | -11.72921 | -54.60228 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede24f21-4005-37a2-b1df-86eecbe86dd7 | -11.98225 | -46.46043 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3f3fac6-ba7c-3ddc-a2a9-a43f14e37963 | -11.23367 | -54.01147 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d09bdca-0d3a-3996-8e1f-1718f5e736e5 | -8.02719 | -55.15229 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dcd23b8-053b-30eb-bc1f-6c7e0fcd3b9e | -11.53688 | -46.22224 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9e4c5ad-097f-3b61-8197-c85668960f76 | -11.24533 | -50.70951 | 2026-08-17 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e531e6-a20f-379a-8796-bbeb918c8895 | -11.90845 | -47.35295 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5c8f9b-6e51-31fb-8fe5-102036adacf0 | -9.86991 | -45.77045 | 2026-08-17 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd264817-09c3-30ab-a6fd-7e496ba7ceae | -11.45206 | -46.58747 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb1e0fdb-e933-3b4d-a2bf-daa2a5bebd97 | -11.99448 | -46.47018 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b2af845-05b8-3bc1-a020-135217794c50 | -9.70185 | -47.66307 | 2026-08-17 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e131ead-ed23-3d2a-9c09-4f3b42bd66ba | -11.81804 | -51.77305 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47b28d1a-40e6-35d0-b38f-3005dbbcafdc | -12.67781 | -48.51812 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 598282d0-ee53-3c4a-85ee-e71491093d53 | -12.04696 | -46.48214 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b471232-3ee4-344f-b85d-687fa27f25c9 | -13.26156 | -51.65892 | 2026-08-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa181b6a-85e9-3b88-a8b0-c3ce44bb01db | -7.36561 | -55.49017 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a9b02a9-d8e7-3e1f-9bba-d6d492410687 | -14.87155 | -46.66213 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8742ac2a-6a44-3230-b56f-e90f19a23960 | -6.12324 | -57.73562 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 305c072c-abb3-3513-ae9d-976aef7f88fb | -10.49926 | -50.40525 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27891992-6954-3033-92d6-4192af3d416e | -11.72698 | -54.61418 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c6e763b-ef54-3abf-9bc9-d0fba334187d | -14.44185 | -51.97106 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d370469e-e188-3e4a-b7e3-bbb811892275 | -11.22183 | -54.02076 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b01c40c3-b041-355d-8ab2-332b45643f52 | -14.47585 | -45.67916 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6feb4e79-2c7d-3e23-bc23-d7216a9cf3fe | -6.86993 | -56.41236 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faeb84bf-d51a-3b84-955d-77d32efab3c1 | -8.0673 | -48.53378 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a7129a23-a265-3a06-bd6d-7c4f418ca4cd | -14.48973 | -45.67769 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8e13ae3-3e59-3a96-a653-276124007021 | -11.09967 | -47.29799 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173fb462-3556-330f-b034-d7265edb0cb9 | -8.02937 | -55.1405 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f282d94f-c763-396d-bfb2-8e69ba38dfb0 | -6.83025 | -56.45472 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62bdc136-3961-3282-b592-e2ee4b32741f | -9.45922 | -50.31265 | 2026-08-17 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21762bb0-4b38-3114-a1f7-6a5ce96fd7ae | -11.33069 | -46.21368 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 459439f6-ca93-35ae-9342-0c2de80ffa21 | -11.44764 | -46.59393 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0687dbbc-a412-3f0a-86e1-450705960535 | -11.46866 | -46.59015 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 59992f1b-4ba0-3590-87ae-6c7a952bf6dc | -10.46837 | -46.31188 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5096f9b-e5b3-36f1-bb74-80711f1b2db3 | -12.02042 | -46.49964 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfaf29bd-ce18-304b-8037-0cddf5b812ed | -13.53482 | -46.273 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8287e9c8-e6f6-391c-b8fa-9395ac16da9c | -14.92408 | -46.60866 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9205e93a-6817-397b-bbcd-a74a14f9cdac | -13.51554 | -46.28798 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ef09f115-1e54-3929-adbb-b644e0e74dab | -12.69768 | -48.50551 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f971b87f-c3c4-3e94-8d88-31df4358dc1a | -7.38209 | -55.50013 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0366aca-374d-3bff-98f5-f1f0cf0c431c | -9.98236 | -53.93845 | 2026-08-17 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb0766b1-64a2-3409-bde6-c367c9bb61ff | -14.87486 | -46.66267 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42f7c3d1-665d-3fd8-a2b2-d69cb406c519 | -11.98953 | -46.45854 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55863ccf-2d08-3e3f-beac-59b0345302b0 | -11.97784 | -46.44526 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
