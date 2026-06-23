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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d533c19-5608-3915-9629-19a09aa46046 | -12.48082 | -43.72734 | 2026-06-23 04:06:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8d0b120-c86f-34bb-a7c9-638008548e43 | -10.87911 | -49.54654 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3146c0d5-a97c-3360-a750-5c0c46dc176f | -10.11213 | -47.54736 | 2026-06-23 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b17eb5c1-1591-3b97-b319-e8d99e5ed2f2 | -10.90166 | -54.1372 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c44b895-e4c0-3e48-8e5c-156d4f083297 | -10.56103 | -46.2321 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db96b2f0-6072-3341-8c2e-b087982eaa59 | -12.8495 | -44.36463 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b59f6005-8054-31d3-8088-01b6959449ff | -9.03216 | -44.2543 | 2026-06-23 04:06:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc404646-3c9d-31d5-ac19-a9fdd5a08be1 | -12.86999 | -44.3514 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d44ff832-f29b-3fa3-81e7-54e1708f231b | -11.80776 | -52.52362 | 2026-06-23 04:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 42085d3a-32cb-310e-84b5-76240106d43d | -11.81178 | -47.33652 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9887af75-3a83-3114-bb2e-0ab7fee46f1e | -9.21665 | -45.33052 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4825831e-b811-3655-a26e-95f6b85fcc9e | -10.76842 | -54.11448 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e9f3c3-1b4f-3bb5-bab3-2b8dccb584a8 | -8.97294 | -47.97799 | 2026-06-23 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91bb13f8-22e9-310b-bfa4-1ca63f0dbbd1 | -12.85305 | -44.36525 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bff83897-df58-3483-9133-0e4518ed06bb | -10.77075 | -54.11508 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1696e576-1478-3f77-9d08-38ce2fe4a1d5 | -12.03579 | -47.7995 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9eba6e0-c5a5-39e6-af77-c9f199c88cac | -10.40168 | -49.44677 | 2026-06-23 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 807cdb47-f5e2-3226-9b0e-b9c29361bf8b | -11.05125 | -52.46891 | 2026-06-23 04:06:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59c4c788-078e-36bc-a079-f4e4ab4b6407 | -10.29867 | -46.4604 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7330e4b3-6be1-34da-9870-91d088b1d53c | -14.06834 | -39.49042 | 2026-06-23 04:06:00 | NOAA-20 | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3ff9cb2-2f75-3a5e-af83-00ca2e1f8517 | -12.65579 | -47.67584 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6776ecb-994b-31a7-affe-b7b54f431f5d | -12.06697 | -48.42587 | 2026-06-23 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd732347-329a-3677-bcaf-461bb04b1748 | -12.65934 | -47.68092 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b898c4-07d7-3ef5-b033-ae2f2daadce7 | -12.87145 | -44.36432 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| def0aaa2-324f-3bef-bdc1-dd250ab9deea | -11.89012 | -43.83537 | 2026-06-23 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 487186b8-304e-3cf0-99ed-94f011ca6b03 | -11.91183 | -43.40631 | 2026-06-23 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 399891c4-b374-3d53-bd84-2b10de435538 | -8.86843 | -46.93906 | 2026-06-23 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dae90fb-f2f4-394c-ad39-de9d9ee57fd8 | -12.86437 | -44.36305 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 833e64a1-6de7-3159-a027-17485b4a14e0 | -8.97854 | -47.97377 | 2026-06-23 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84aed3eb-dc86-3253-bdca-356a4f2e11b6 | -11.139 | -47.13205 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ded00be7-e64a-3695-b17e-03d87a0aef0f | -13.16822 | -46.0745 | 2026-06-23 04:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8f6cfa0-0bff-3626-805d-99531e711ea5 | -12.39686 | -40.40971 | 2026-06-23 04:06:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a2536020-b6eb-3c17-ad98-edffddd31bdd | -11.80177 | -52.52237 | 2026-06-23 04:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df308ba7-d76b-3990-b38b-986e1b168861 | -12.86791 | -44.36369 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93aee847-a53f-3a57-9601-1dbfa16d7c91 | -12.87215 | -44.36022 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0d993d4-3e24-3bf7-91bd-3699c12f2fd2 | -11.47569 | -46.68827 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf1da0da-f407-322e-af5c-6f0808e52973 | -7.36156 | -47.01838 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f5de2a2-2c05-381c-bb89-2ce8cb9495bd | -9.82434 | -48.2286 | 2026-06-23 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3602a0c9-931b-33f1-8c27-e0f00a0f6843 | -11.80172 | -47.34323 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b383cfaa-f13e-37bf-a720-4f5a90ead395 | -11.80526 | -47.34816 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2959057-9222-37b2-a126-3a0f5e99aa76 | -9.12428 | -50.93761 | 2026-06-23 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19776c27-84f6-3a73-8f8f-af0b5bb1aac7 | -12.86013 | -44.36652 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8feea2e-6213-34ce-913f-988bbc09d75e | -9.22057 | -45.33122 | 2026-06-23 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2b18620-0427-3631-b398-54b7db72d7b6 | -7.36526 | -47.02377 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b323ec16-e6e0-3934-b731-353a5daa0dea | -12.86576 | -44.35485 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5fc052ef-a412-3682-94b6-d78c767ec885 | -11.05407 | -49.57427 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61fbd5fd-b323-3a51-bf69-e68979aa71af | -10.12442 | -52.11562 | 2026-06-23 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd2cb18-108e-39a5-9543-03d170e625ab | -11.57186 | -47.43685 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6e22ce3-5fdb-367f-9bcb-7e1e25d17186 | -7.36377 | -47.02596 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbd8d3c5-ae98-31c3-ab4a-3d11b92d05e6 | -9.09143 | -47.52499 | 2026-06-23 04:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53d48fa0-84ef-3ebf-b079-58e6c36cbccf | -12.65503 | -47.6801 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83340ae0-767e-3494-aa5f-bfd49dc69357 | -11.29172 | -43.33628 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8c1a62cf-d5ff-3510-93ce-42396b572270 | -10.76528 | -54.1078 | 2026-06-23 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb6cf1c2-28ce-3e55-b614-4d6258b5dfa9 | -10.11659 | -47.54823 | 2026-06-23 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42fc4c63-617b-33e4-b1ab-da1ee0dcdeaa | -11.48124 | -46.681 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3ed2ea3-b49d-356d-af2c-1b6247f376a0 | -10.56296 | -46.2212 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca7db969-6466-38d0-9d1f-8d7f6642ece2 | -9.45739 | -49.83487 | 2026-06-23 04:06:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2258e085-19b0-33ae-92de-e55bae72c35a | -7.725 | -44.56195 | 2026-06-23 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89aa4fa-e651-392b-9fa8-ab8a1e02ab07 | -11.13588 | -47.1333 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cab08e18-a19b-3dac-9e5c-9551e1d04a11 | -13.46243 | -41.7593 | 2026-06-23 04:06:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b011e7aa-3f4a-34d4-b7c1-706236a9ddf7 | -12.85514 | -44.35297 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 24e8404e-7c72-3a53-a609-843086762b98 | -7.35625 | -47.02202 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 948dfb06-ec62-32ee-b4e0-927f4f5f8ca3 | -12.8509 | -44.35643 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2de56ccb-a824-30c7-a1aa-5a3085a0a434 | -11.80685 | -52.52816 | 2026-06-23 04:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45b5a8b1-ef56-3c05-8fd3-13edc0b1cf2c | -11.4778 | -46.67646 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a9b365e-3e74-3107-a722-99216757a5d0 | -12.03137 | -47.79878 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42f97373-7e3e-3847-a3dc-d72d289175fd | -12.36453 | -45.68887 | 2026-06-23 04:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb908fa-74dd-313e-8f59-2e66c2a682dd | -12.50707 | -48.26763 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 09fd17a4-f2e0-356d-94c3-27a8c1dda960 | -8.97385 | -47.9729 | 2026-06-23 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88a23153-236c-354d-a09c-8c051d61fb94 | -12.87076 | -44.36841 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93a2866f-5bc5-3b49-8280-c36e3456b9d8 | -10.96942 | -48.15344 | 2026-06-23 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cc64725-179d-3d5b-8da6-375cda2438bb | -11.58124 | -47.43442 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6458051c-1ba7-39cc-be34-ed00ec7b977e | -12.48427 | -41.7354 | 2026-06-23 04:06:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3ff2e1d6-ebca-3e58-9c9d-1cbd75d0bb6e | -6.93544 | -51.94516 | 2026-06-23 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5b9db58-f364-3fd6-be10-29ce275b7139 | -12.19925 | -47.96844 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05f0008a-dff4-3a5e-b9d8-0f22c131be55 | -12.51999 | -48.29872 | 2026-06-23 04:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ca05357-1735-3ddd-be8a-70c98443e8ce | -11.38593 | -47.81228 | 2026-06-23 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c893b7a0-66ae-35eb-9411-ec14f1884065 | -10.87967 | -49.54354 | 2026-06-23 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb1b4a1e-e269-3dc7-a9e5-ae2af392d069 | -11.76811 | -38.26445 | 2026-06-23 04:06:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4569546-a8f5-373e-b9d6-3afe23900e3a | -12.86507 | -44.35895 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8069d57a-0f5b-3ea0-ad1a-3e1454026ec3 | -11.99098 | -45.14809 | 2026-06-23 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e16193c2-ac7d-348f-916d-1f7ed4ecf5dc | -8.79036 | -44.80658 | 2026-06-23 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21b0c4ff-ceb7-3bc0-ae24-6e6e78f2938f | -8.6151 | -47.79668 | 2026-06-23 04:06:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5648a95-6a62-3901-83c8-0870dffd3804 | -9.77788 | -48.97361 | 2026-06-23 04:06:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aff536c-038e-3621-a30a-8d1fe19b7872 | -11.4764 | -46.68431 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22fb9140-dbb9-36c1-9b4b-1553e234fc2d | -11.81029 | -47.34482 | 2026-06-23 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87d1535d-b41e-3008-80e7-5bbb042a9f33 | -12.65071 | -47.67928 | 2026-06-23 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 137db39b-502c-3f54-9187-59b7bb736103 | -7.13182 | -45.87968 | 2026-06-23 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52c3774d-99e9-3816-9611-c7c6b3156b51 | -6.93186 | -51.94588 | 2026-06-23 04:06:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b7700f-b5dd-394a-bc29-6e097b721330 | -9.74087 | -47.87702 | 2026-06-23 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d6667c3-2b7c-38ac-9e79-33418116e99b | -11.29581 | -43.33303 | 2026-06-23 04:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4d44232e-3660-33d0-8104-787e9bd24faa | -10.56509 | -46.23286 | 2026-06-23 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adc318f4-3b65-30a3-a61d-4a9cdd3ef5e4 | -11.48053 | -46.68499 | 2026-06-23 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94485648-9343-39a5-805e-3a6f88661cc5 | -7.36004 | -47.02053 | 2026-06-23 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f95f799-09a1-3041-8559-de84b7603aaf | -11.57692 | -47.43358 | 2026-06-23 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8797f41e-b6d0-391d-ac99-58ce11bbefda | -12.85868 | -44.35359 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 25e75070-1372-3f15-b042-d5180df7f0d2 | -9.57705 | -49.11414 | 2026-06-23 04:06:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 767b3004-8066-3ceb-b028-87732b93a6cd | -12.73196 | -46.44689 | 2026-06-23 04:06:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 933ec2f5-27a2-38c3-83dd-dce3a13c8ba2 | -12.45001 | -41.75864 | 2026-06-23 04:06:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f637e344-2ead-3056-bae3-4543f4241384 | -12.85589 | -44.36999 | 2026-06-23 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
