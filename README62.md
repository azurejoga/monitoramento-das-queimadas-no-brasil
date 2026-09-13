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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae1db10-7261-329a-8d39-c62a5572fd45 | -6.8567 | -47.4328 | 2026-09-13 13:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a6e4826e-09a1-3957-a44a-9509cb620077 | -11.0429 | -47.1856 | 2026-09-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d682abc7-cefd-3efd-972d-95829a990deb | -8.832 | -46.9476 | 2026-09-13 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| f01a960c-f86e-3fb8-8470-e674930f6bb9 | -2.6602 | -57.5119 | 2026-09-13 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 29067696-44b5-33bb-8eed-c185829252bd | -7.0166 | -44.6184 | 2026-09-13 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a4bbc046-c6a4-33e8-8113-261102f9dc1f | -11.8189 | -46.386 | 2026-09-13 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 1fa9c829-9977-3aa8-94de-4cc4d3537659 | -8.9272 | -45.4321 | 2026-09-13 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 85755331-a873-341e-89cb-6012ce842a1e | -6.6767 | -58.7105 | 2026-09-13 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3f143b7e-88cc-3ddb-bea0-6468789a0b23 | -7.0164 | -44.6413 | 2026-09-13 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 3a07fb08-36b5-38fb-a6a3-c606b039224d | -11.838 | -46.3834 | 2026-09-13 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 83439c2b-00a6-3ef8-bf11-0b0197fdf889 | -5.1255 | -55.955 | 2026-09-13 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 292ad059-4dd4-305e-8f46-2059e02ad55a | -13.299 | -51.7288 | 2026-09-13 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f3025644-bcda-3d12-b184-e4069e372028 | -6.6758 | -58.8654 | 2026-09-13 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 160.8 |
| bb933a88-b5c2-3f38-8585-7c91cf985147 | -13.3055 | -51.3235 | 2026-09-13 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 0c3b0409-cb55-385e-9a6b-66ea8cdc9f44 | -11.3532 | -46.8324 | 2026-09-13 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 556.0 |
| f08b8d72-01fe-3757-9de8-548ff33cbf40 | -10.7535 | -46.2347 | 2026-09-13 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5e68bb4a-bd5a-316e-9440-bc6319ed54e7 | -11.5793 | -47.0043 | 2026-09-13 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| a26612e9-5326-337b-a9b6-8196a133d42f | -7.5394 | -44.9133 | 2026-09-13 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2a3cb31b-7ef2-3d01-b857-9168aac87e55 | -14.0823 | -41.4134 | 2026-09-13 13:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 267.7 |
| 26a9315d-ab7f-30e6-a843-45d74ab536b4 | -2.6785 | -57.5115 | 2026-09-13 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ec8d264b-3327-380c-ade0-2d92f05f9482 | -11.5796 | -46.9819 | 2026-09-13 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| adb4e995-e9d4-3a0e-9b49-773d4e34c73d | -13.4507 | -48.48 | 2026-09-13 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 263e1c8e-928f-349f-8193-dd213b009912 | -7.0352 | -44.6396 | 2026-09-13 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 18a266c8-1be1-3f40-a178-7ec47443a928 | -6.6021 | -58.849 | 2026-09-13 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 69e566f3-9709-3f19-b8e3-cd9b04c57ebe | -11.3025 | -44.184 | 2026-09-13 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 6d8c6358-1747-3e86-932a-0af70a3dde58 | -9.3951 | -50.1121 | 2026-09-13 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| e9514f67-3f2c-3a40-adc5-43a812f367fb | -13.4503 | -48.5022 | 2026-09-13 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 67a18619-a581-3df6-abd1-fe9becb85e97 | -13.4507 | -48.48 | 2026-09-13 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 932291d3-8769-3900-a19a-a2e68df5481c | -9.8992 | -47.5874 | 2026-09-13 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 02a19d05-9b25-3d77-99e5-7ce89dd61127 | -9.376 | -50.1352 | 2026-09-13 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 35346f5e-cd3b-35f1-bc56-3070563b0584 | -10.2926 | -45.3161 | 2026-09-13 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| b249343d-6ccb-323b-9770-ff33b92b7381 | -9.7548 | -47.0937 | 2026-09-13 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f8fc43bf-d398-351b-82ff-675b8c6e24ba | -7.0352 | -44.6396 | 2026-09-13 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| b72cc936-fca2-398e-975c-aae382c99deb | -11.354 | -46.7874 | 2026-09-13 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 057b867e-49ca-3537-a422-064d017015e1 | -10.6829 | -54.1475 | 2026-09-13 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 281.3 |
| 9303c8d4-2911-3746-948a-d13cd8078a71 | -11.5793 | -47.0043 | 2026-09-13 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 90e9178a-e74f-3bf4-a984-94bb997a49cc | -10.2929 | -45.2932 | 2026-09-13 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 1c5e6173-72c3-34fc-9a73-910f584d2373 | -8.6005 | -44.4378 | 2026-09-13 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4147741f-1263-3d12-a526-a988ea95a367 | -7.0166 | -44.6184 | 2026-09-13 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9f0552ed-4b62-3fe8-9198-725f3cf5f3e5 | -5.1255 | -55.955 | 2026-09-13 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 1850ac25-a6bd-3c4e-bedd-123875cb5a25 | -6.6757 | -58.8847 | 2026-09-13 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 9fdb13bc-5f58-36e6-acb0-7176bd33ae71 | -6.6767 | -58.7105 | 2026-09-13 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 1d00adb1-48a3-36de-a775-f54eadf5405a | -6.2831 | -59.9394 | 2026-09-13 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f37013cc-28be-341a-a297-83d038b1c3c9 | -9.5129 | -45.4568 | 2026-09-13 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 775111b7-90dd-3ba8-80b6-5f1bec449e11 | -7.0164 | -44.6413 | 2026-09-13 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| b665972e-b786-3980-a36c-a6d27e987df8 | -9.3763 | -50.1139 | 2026-09-13 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| efdff578-1494-3870-9be1-73fef8e7335d | -10.6417 | -46.0906 | 2026-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 2219bfca-9844-3b22-831a-b10a294a4b16 | -6.6021 | -58.849 | 2026-09-13 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 89ce6879-3a39-30b3-b0fc-968d033b3e55 | -11.3532 | -46.8324 | 2026-09-13 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| e02c9803-e730-3107-a6a8-50ba4f233667 | -7.2072 | -46.0963 | 2026-09-13 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 63448240-ebf1-3a54-a42d-d49432e3ad41 | -11.838 | -46.3834 | 2026-09-13 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3a2abeee-62ab-34bf-b736-b658983b45a7 | -6.6758 | -58.8654 | 2026-09-13 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 8328058b-8669-36e3-af23-ce21bbad7e28 | -4.1223 | -54.0158 | 2026-09-13 13:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 7086274b-5f8f-3072-b8da-e640e7b0c47d | -6.5159 | -42.2363 | 2026-09-13 13:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| e3ca301a-5a34-356f-a9de-2239be545cb5 | -2.6785 | -57.531 | 2026-09-13 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| c10842a9-cfe2-3844-921e-0b6558bf56df | -11.8189 | -46.386 | 2026-09-13 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 7119f86b-0811-302d-a977-92b834f19c84 | -2.6784 | -57.5504 | 2026-09-13 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 203.2 |
| d15bcb08-ebd1-39f7-806b-68202a535b68 | -9.3948 | -50.1334 | 2026-09-13 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9f5f05f7-8c79-3644-8d97-fc88657e31b4 | -3.3809 | -50.7623 | 2026-09-13 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 35383a28-f213-38be-aa6a-e325a28b9794 | -11.351 | -48.1668 | 2026-09-13 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fcab5f2f-0d2e-30ef-ae8f-488d4cb4e382 | -9.6752 | -46.0273 | 2026-09-13 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0e242a57-b703-38ac-8d07-09d673e3b0e1 | -11.3021 | -44.2074 | 2026-09-13 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| ba5b2613-40e1-39a6-9b88-666c3d9bb790 | -5.1254 | -55.9748 | 2026-09-13 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7652a72b-bf56-3fe3-b0c1-31d9c009dbd2 | -10.6413 | -46.1133 | 2026-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| b6ed0eab-39cb-327f-897a-8d333223111a | -10.2922 | -45.339 | 2026-09-13 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c244d011-8097-3444-95d0-417ef4902a63 | -11.2833 | -44.1868 | 2026-09-13 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 761d0376-b3d6-31f5-be50-23d8f251ae20 | -11.5796 | -46.9819 | 2026-09-13 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| ea653657-eddd-376e-9d0a-cdacd7ca923f | -10.7018 | -54.1458 | 2026-09-13 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 46af78fa-3562-35e7-abf3-319278010fdf | -6.8567 | -47.4328 | 2026-09-13 13:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f545c32e-698f-3268-9552-927dbbd3eb33 | -13.3055 | -51.3235 | 2026-09-13 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ac88850a-76fa-39eb-a5d3-c4d320023ffe | -8.9272 | -45.4321 | 2026-09-13 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2394b524-a89a-3fc2-8df0-9382b605d3fb | -2.6785 | -57.5115 | 2026-09-13 13:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e6652514-417e-3031-a3bd-6b43b16a163b | -6.6337 | -45.3792 | 2026-09-13 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cb4bbc31-712c-3ad4-b7b5-6101e59cdf8a | -15.5595 | -53.7845 | 2026-09-13 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 791a1400-5a76-39b5-9031-13dc054756a1 | -6.6758 | -58.8654 | 2026-09-13 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 74f430cd-bd79-3132-b18e-a8446a4dc3c1 | -8.6005 | -44.4378 | 2026-09-13 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4b9d8d0e-b3b4-3844-abd8-e420934f536d | -13.972 | -54.0627 | 2026-09-13 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bccb6a83-03a5-35e9-8dde-bad63aadeaa8 | -9.3951 | -50.1121 | 2026-09-13 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d81533c8-0965-3598-95b5-2795910beb3f | -3.3809 | -50.7623 | 2026-09-13 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 6b73043b-ee65-3fc4-9956-3366144b901a | -11.5793 | -47.0043 | 2026-09-13 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 855d92cd-cfd6-38fb-a9ce-5f9680ea0277 | -6.2832 | -59.9202 | 2026-09-13 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 42bd7953-5a58-30d9-9d77-424a2dbeeafa | -10.2926 | -45.3161 | 2026-09-13 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 560e805c-df9f-376c-9cac-fa313e7445d0 | -4.1223 | -54.0158 | 2026-09-13 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 120fd23c-7488-30ba-a268-dd538d48e44b | -11.5796 | -46.9819 | 2026-09-13 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4d57ed56-bc59-3a8e-888a-30eaf76b286e | -11.838 | -46.3834 | 2026-09-13 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d9dbd868-0056-30c1-8282-7d585764f617 | -10.6827 | -54.1679 | 2026-09-13 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 328.6 |
| 15deff84-2850-3d93-93eb-17d120f4cbac | -9.3204 | -44.355 | 2026-09-13 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f9c4d449-6a8b-35d4-b621-c5869d5e9624 | -8.5415 | -54.7187 | 2026-09-13 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| bae63639-ec67-36b3-8f36-af3f17d45e67 | -11.3025 | -44.184 | 2026-09-13 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 49b4cd19-50b4-3188-ba83-2791569317d7 | -10.7018 | -54.1458 | 2026-09-13 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 5cae24f0-f6f1-3334-9f33-d6b2c7b47a7d | -11.8189 | -46.386 | 2026-09-13 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c84f0c98-0236-3bca-af18-2ddf04c4d394 | -7.7634 | -46.6944 | 2026-09-13 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2defe87e-d4f9-3680-a5b7-f2dd58194b2b | -6.602 | -58.8684 | 2026-09-13 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3e543ce7-e205-3f71-89b4-b60dc7c483e2 | -9.3948 | -50.1334 | 2026-09-13 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b25f8508-dfcb-3ecd-901a-d9dd55f0c02f | -7.5394 | -44.9133 | 2026-09-13 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 55c5706d-541d-3bd3-8594-67c5340bf47f | -5.1255 | -55.955 | 2026-09-13 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cd9ca14b-13f2-378f-a967-a9843fe40a8b | -6.5837 | -58.8498 | 2026-09-13 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| de15755d-51b9-300f-9a66-cf615ae61c2b | -8.4292 | -46.0271 | 2026-09-13 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| aa200028-d6ce-337e-b054-98fe210c05fe | -13.4503 | -48.5022 | 2026-09-13 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 830a37cf-ea5d-3fcd-b16a-1a30a3975311 | -6.8755 | -47.4313 | 2026-09-13 13:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |


[Clique aqui para ver as próximas entradas](README63.md)
