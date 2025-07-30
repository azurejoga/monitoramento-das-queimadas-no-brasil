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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61151c5d-3d24-3d4f-b654-95a2bbc8f18a | -8.35928 | -47.34582 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab187c09-cecf-3d01-a64e-14c529acdd18 | -8.33291 | -54.75661 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff62d6c-26ce-3bbe-9f7e-82f88898da33 | -6.53109 | -56.21027 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66eb948c-7009-334f-9bda-eadfb1c61319 | -6.5653 | -56.18515 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05ddbdbb-1621-39f9-b807-7fbbbf502128 | -12.47064 | -47.27499 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fe9e2b8-33ab-370d-b273-89eca20b4dee | -9.87126 | -44.69321 | 2025-07-30 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98eb093d-5050-3693-99e0-3a4180dfa63c | -10.62723 | -45.24224 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 56b3459a-3ec1-3837-8fc0-43600eafa85b | -9.2056 | -59.67193 | 2025-07-30 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53b0108e-0c70-38bd-a5c6-24a5198b1604 | -8.62308 | -45.89077 | 2025-07-30 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19bb8137-6057-3de1-8b27-91447855ab57 | -8.5209 | -43.31565 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 158e4a0e-4ebd-3797-8376-f754c625dd74 | -14.74007 | -46.29892 | 2025-07-30 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c972e8de-25c5-39e0-94b2-51ad6efa309d | -9.22701 | -50.04611 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af031e25-53d4-3132-a8bf-c950922a6693 | -6.49741 | -56.21034 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3a950f-063b-395c-9a5f-c24a7b023b01 | -12.54665 | -44.7332 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba712e87-f8c2-3490-8208-d0632ea3b4cd | -11.32785 | -48.92084 | 2025-07-30 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7271e988-f403-3961-b8df-4857d12f3ae5 | -11.46754 | -45.11723 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b5779373-31bc-3d2c-9e7a-28edbc862ce5 | -9.55932 | -40.3272 | 2025-07-30 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 092919d3-6308-3dd7-abfd-a2bf2be23653 | -13.07188 | -47.38187 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 001a15e2-fdb4-394a-ac36-a9d38ae17bf7 | -12.47455 | -47.28033 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1301cff6-67b0-3610-a121-391db86c813a | -6.6188 | -59.98474 | 2025-07-30 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f902a474-d6a9-3369-a303-e4b4028380b4 | -10.61748 | -45.23786 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8409863a-dc9e-375c-8e9f-42980db941a2 | -11.34777 | -51.25155 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6265db90-97cf-3d3d-b8ab-9e8a7e8fc676 | -7.65906 | -46.51791 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caaa32a1-01f9-3d65-8646-e1b6ca5b4083 | -6.49586 | -56.19683 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1413f83-832b-3e5c-b100-2b3be72f30c8 | -8.95726 | -46.73317 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86660da1-cbf9-379d-9f94-56bbe5669cea | -10.40884 | -47.25294 | 2025-07-30 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d96212ba-c3f8-3497-a1f7-922e164da256 | -6.53084 | -56.18941 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cda02fc9-c503-3cc7-a03b-c6c4242b8339 | -9.26026 | -50.22714 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e98e1368-1491-3386-a815-bfa376bb9415 | -6.52214 | -56.19682 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 363d1eb7-a53f-3e45-bf49-fd873a28af88 | -14.76396 | -47.54192 | 2025-07-30 04:51:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1490e570-e59d-348f-8732-c248419836bb | -7.65969 | -46.51352 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8796daa1-31b6-37df-bb71-51f37e2e20ef | -7.74402 | -51.09612 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01c80d7d-49fc-3721-80d7-a89a11d87c34 | -11.98595 | -46.69281 | 2025-07-30 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b99e8d32-6221-3fcd-8f53-110718d0c9e6 | -7.73374 | -51.09457 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 129ef5f4-d294-3f72-b582-fb2a4f2e7497 | -7.77104 | -45.86624 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a04e3899-aef4-338d-9ec7-8bd537f33ec6 | -8.67816 | -51.21547 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 876561dd-ed28-305f-8d01-e3a1605bfebd | -14.50258 | -46.53609 | 2025-07-30 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e529a1a9-b83b-3378-adcd-804295ab3c28 | -9.15864 | -49.85082 | 2025-07-30 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebee5bfb-86ee-35c4-a6a0-8da0760c3de5 | -6.53397 | -56.19307 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2916573e-5390-39d0-a7f2-59011b5d2930 | -11.47314 | -45.11455 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e14f8561-5522-3f63-a334-f885f3e3dbff | -14.46322 | -47.88522 | 2025-07-30 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7908891-d36b-3ea2-9cea-8fc883616b68 | -8.31425 | -55.10931 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fec1d92c-58ba-3066-bcaa-376abf3686ae | -6.558 | -56.18393 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2cdf5e6-59e0-39d3-b5fe-40c11bcb9f7d | -6.54634 | -56.18637 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4815f4-3c2e-36e5-af5e-830be5d66d86 | -11.32036 | -48.91618 | 2025-07-30 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3b4a3de6-42ad-3c19-ad49-09cf092c5ba1 | -11.33722 | -51.24995 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d20fb4ae-d0ab-344e-9a8e-4a7da63b0814 | -9.02109 | -47.9765 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dfe9215-c425-321a-9737-0aa7e04fb6ec | -10.04053 | -59.3582 | 2025-07-30 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8296960-da07-32ca-9a6d-e4389ff4c293 | -10.62294 | -45.2356 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be5f6623-9246-35e7-b460-46d073c0e2a9 | -12.82029 | -45.44388 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b55850c-26e7-3a47-80a9-1583e8dee6fc | -9.22556 | -48.6007 | 2025-07-30 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433c489e-aaff-3a27-8195-995425ee0d24 | -6.48946 | -56.00819 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38ccb2e9-b562-3b51-a075-d420c6d88ffc | -9.45335 | -63.21138 | 2025-07-30 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb71713-9154-3eaf-9fb3-53db7610b763 | -11.91934 | -44.5467 | 2025-07-30 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b6a946-e4d6-3f4e-993b-77c7a32801f8 | -8.01783 | -47.68024 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 588ae372-4d0e-3ae3-a3d3-8b71584b767d | -12.47125 | -47.2703 | 2025-07-30 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d4f80f8-6987-3cc7-b542-381850c6171e | -10.49901 | -53.57722 | 2025-07-30 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76d72caa-5aae-3108-9d23-f5d4f0b2ca4e | -12.80998 | -45.44244 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04b20314-5d62-32f9-970c-af1a853fe35b | -6.50769 | -56.21647 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a707591a-4876-322f-8b51-5033238ee155 | -13.08169 | -47.3093 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e97fcb6b-99cb-375e-9990-0932da39fd6f | -7.85265 | -46.73305 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45fcbed3-c25b-3562-9cf5-cbf438c3f699 | -10.7091 | -48.85819 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce611c7-ecc3-37c4-b2da-ac9a2d8ae770 | -8.96044 | -46.74278 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06977b82-7d29-39b7-9629-0bde120ce631 | -7.86547 | -47.87275 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9710ce8b-1825-3ba4-83d1-f7e90518e5ec | -8.01728 | -47.68402 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0aa4c1b-e99e-3235-838d-a379e014aace | -11.31986 | -48.91972 | 2025-07-30 04:51:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40c72bd9-b953-3375-b59a-4ddb9389996d | -8.34026 | -54.75409 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6f57d3b-d850-3bc3-bccc-a74505952e4c | -8.52039 | -43.31945 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 68bfb761-5ec2-3167-a843-0d1f94f87836 | -6.52744 | -56.20964 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6538f996-d3ac-319e-860b-ff1f1758fdba | -10.62216 | -45.24154 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0659dc05-3afa-3651-bfdb-e52a6feb6fc8 | -6.50473 | -56.21156 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27e4d7e9-6cf1-3156-9cd6-a502314e37d8 | -9.18143 | -48.84601 | 2025-07-30 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e57d4531-22bf-3096-86e8-e0f1873f0de3 | -6.55729 | -56.18821 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d2e27b3-71d0-3d68-89f8-0ef3a25d9ccb | -9.56003 | -40.32756 | 2025-07-30 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 143b376d-cec7-3e44-afa5-d908d2893e80 | -11.46195 | -45.11978 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1066e532-27e2-3f24-87f0-de97774a1e2d | -8.62377 | -45.88587 | 2025-07-30 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4eb96463-4497-3484-9246-25645d5e0821 | -8.95448 | -46.73983 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bafae9a6-bf21-3376-8c94-cbb29a2f71a4 | -9.55318 | -40.32671 | 2025-07-30 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| c0e8e6ea-e013-3ace-befb-10c0e666b25b | -6.51936 | -56.21398 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dde037a-2301-3669-9245-cee193759e13 | -17.48931 | -46.73457 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e69afd87-dea3-305f-93c5-a00661730a47 | -18.1342 | -53.83154 | 2025-07-30 04:53:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a6e91ac-2a8f-3471-b695-a0d8f4de8f01 | -14.5082 | -58.80037 | 2025-07-30 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bf8c4f0-1b2f-3bb6-93e1-6e1d1a1c616c | -17.97859 | -45.60446 | 2025-07-30 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e07e3047-0a74-324d-b26c-7f0e592b6da3 | -17.48861 | -46.74068 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d968571-ebb2-3d2e-b4a2-9bb98e8430e8 | -16.88796 | -49.07344 | 2025-07-30 04:53:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a90918e-c90e-38a6-b265-bd1252089b21 | -17.48358 | -46.73998 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d618ad6a-6fe0-35e4-99ee-2d4114c2f522 | -16.66528 | -49.33054 | 2025-07-30 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeabd783-e081-3eea-86d1-dd9c7b8b5966 | -18.58614 | -55.9443 | 2025-07-30 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e49ccb2c-2955-3087-9d8e-18edc45c5b61 | -18.45013 | -54.66177 | 2025-07-30 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0b146a6-0708-3c7e-bd48-147383261d2d | -18.77941 | -47.62153 | 2025-07-30 04:53:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc4eaeda-6010-3fab-8055-cb8abd3db2ee | -14.41179 | -59.34345 | 2025-07-30 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7248b2f7-eed5-347d-b90b-ddc144084271 | -15.7705 | -49.95643 | 2025-07-30 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9592057c-3a11-39ec-b769-7794afdedecb | -16.63702 | -49.35101 | 2025-07-30 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f31aa881-6198-35e1-9981-08da4f2f1741 | -17.48427 | -46.73389 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a2c9441-660d-3062-afd7-32daf82dccfa | -17.62248 | -53.86033 | 2025-07-30 04:53:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 144de4d7-8540-3cc2-bdbc-73fa5ef6a5da | -18.58282 | -55.94372 | 2025-07-30 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| cceddf8a-5857-3db4-9f90-4a7010c1981e | -15.76653 | -49.9558 | 2025-07-30 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 48b1c25c-a8f6-3180-87de-875f9d48f0a2 | -20.29375 | -54.07463 | 2025-07-30 04:53:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98b646a1-1e45-3858-9d94-4753efbbb75c | -19.10376 | -44.40833 | 2025-07-30 04:53:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb70b171-3583-3720-be0a-f2f8ee083bbd | -19.01758 | -54.65681 | 2025-07-30 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
