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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba588fda-5d65-3a30-a429-10532c4a44e2 | -6.55852 | -56.55248 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a30407f-674d-398a-8dca-f496ad994f53 | -12.73569 | -46.47227 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e29c1eac-37c0-3c68-9b6f-49137ab2051d | -7.04799 | -56.62065 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9557661-2299-3f84-a7ca-2660ac9a2c7a | -10.79212 | -50.93276 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 60ff4e1a-3553-346f-863e-2a8ec2675218 | -7.49367 | -55.35856 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4080d728-7a18-3bc9-851e-01bf7b776352 | -6.99766 | -59.25656 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c4988f01-4593-3773-a1c0-6a2e57b6fec1 | -9.97114 | -48.3274 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0589ba6-4a29-3adf-bcde-94918e12a283 | -6.72762 | -59.44756 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ddce891-550b-3750-996c-f1fbd53eee1f | -10.58 | -50.40603 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 975243d5-4cb6-3fa9-b796-7f56a219b289 | -6.55798 | -56.556 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088e0be4-f7c1-3123-a3e6-46e8aef6b628 | -6.43469 | -54.96737 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72148cdc-c8a3-3105-b852-fb66849a8993 | -7.01916 | -59.25251 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84eb6520-39ef-3c36-9dc2-91f38af26148 | -9.9764 | -48.33091 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad5af55e-7e46-3cdd-846d-d3b80cb776be | -6.63882 | -58.48101 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee3cab5-4bb9-3f75-96c3-c0bc84ec251a | -6.95875 | -59.07919 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74f3eed1-3559-3a3e-9241-b58570e667e0 | -6.12736 | -57.81735 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2184c99d-9352-33ea-9be1-41220a7b1be3 | -6.84812 | -59.46264 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fa3c67e-32de-33a9-944e-08e4ca57315a | -6.11849 | -59.92437 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea605fb-339d-30f9-908b-91449e5bcb20 | -7.00444 | -59.25764 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd54747-6f98-3ff7-aa08-b5132162dac2 | -6.35706 | -54.7626 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94da970-70f5-3a86-8956-f84b0b742726 | -8.57011 | -55.28016 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b6659e-9efa-324f-bf0f-15c744f17bee | -6.81881 | -59.60327 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 738a4f94-94a1-3136-b16e-fb5fa92e4441 | -8.81269 | -62.33441 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dec0edeb-b810-3caf-88fe-fe52684a22b3 | -6.82884 | -59.66993 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c03ee90-699f-36cb-af65-10ec6b766c5c | -8.12121 | -47.48 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204b4278-00af-381d-8c74-91ee14102a67 | -9.05611 | -50.80573 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d138d62b-5b51-393c-871e-7bb0c4b60a47 | -9.39303 | -60.58577 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53d42e84-331a-3411-b5ec-9cd055a04ea4 | -6.80568 | -59.59734 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07c01c5e-d8ef-3dee-bb66-6ef9dca8970a | -10.36881 | -45.05984 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 02a1108c-dcda-3c29-8403-9d887dba053f | -6.81255 | -59.59842 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b3e022-b93a-32cb-a2eb-26dc3c57dd70 | -6.7742 | -59.44331 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90f70cf9-e977-392a-911b-8dd6ad6dada4 | -8.21903 | -54.98797 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab53a8cc-629b-3c8f-b84a-9f0728c08b07 | -12.75239 | -46.44167 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2abf2570-49b9-3df2-9afb-597a2ab44f27 | -10.58157 | -50.40825 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2176e1ab-877e-3036-aa9a-e2bf0274816b | -6.68871 | -58.72416 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb111a06-7e08-3d14-9011-0e8efc0d18d7 | -7.49899 | -55.35838 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5dd0010-b2ce-395c-8d0e-485f0dc999d4 | -6.14901 | -59.92057 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae975f46-02f2-31e5-9e59-b6276ad92ebb | -6.35999 | -54.76708 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d46d0b-c55a-37fc-bfc9-eca44a2250ea | -6.36353 | -54.7676 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d111928-6d5d-32dd-a86f-66a642d70cc2 | -6.62233 | -53.19085 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c838c54-c511-39bc-9ce8-56b44a5339b5 | -8.085 | -47.53231 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d67a42-46a3-37c1-95bb-cb2390124610 | -6.14266 | -59.91555 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea6f8e84-b7c1-39c4-b1de-ceb36b206e52 | -6.4411 | -54.97233 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8a4e2f1-9a59-3f5d-bd52-6d5ecc3f8bfe | -6.99941 | -59.24568 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a2ebd90e-4b90-308d-b94b-8c5424841120 | -9.97163 | -48.32365 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de2bed7e-84c1-3509-ab21-e9f44109fbb5 | -7.01297 | -59.24778 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0aa6d7f-01f1-300d-a760-ea484340fb37 | -6.53926 | -58.31434 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94584c0a-8516-3f4c-9d4e-11533097400f | -10.37506 | -45.06583 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c02f6e59-25ed-3659-a227-fb644aed388d | -7.54758 | -61.37117 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9aa7c596-f38c-3e52-b9a5-7cd235fd6cf9 | -6.22284 | -55.92448 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c6f49fc-4edf-31d1-a870-a7d2c87b845f | -8.17208 | -46.69774 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19cc0334-50cd-3d56-97dc-a9c9d4afb2be | -6.12261 | -59.92102 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91db2a26-3d04-3865-affd-4f8aa98873b6 | -6.63326 | -58.49456 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a52e93c-20a0-3c01-bd46-24c6495ea801 | -8.51655 | -55.3494 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e914f8-bf39-3b87-b19b-9678b8245eaf | -8.55675 | -54.71814 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de22f2f1-c46a-31bb-826e-285a11d65d13 | -6.77361 | -59.44701 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f594e6b3-5389-3791-bf00-d66cfe35781e | -9.05674 | -50.80103 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 01eb7124-e0d8-3212-b69d-c77e463c979c | -6.64049 | -58.49209 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| daf995fd-ae9b-3b54-b95c-95ac8637ba01 | -6.83249 | -52.50144 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e4a480-e7cd-3ff6-a4ad-b42fb492b7b8 | -6.40871 | -60.06141 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 958ad466-d096-3cbe-a5c0-0f62795db93a | -7.5424 | -61.35669 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90d6f88a-d185-3144-a3ba-928c54fd6a1d | -12.88499 | -48.4995 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57919f51-cf91-3534-9f8f-6fe2c37af2b7 | -6.60994 | -58.38295 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e99f0bae-ae8a-3cc0-8b5b-1c7fe3952ac7 | -9.38253 | -45.42383 | 2026-08-25 05:12:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 491d76a2-d5a1-3fce-82dd-adf06d5748c6 | -6.35172 | -54.77401 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160f3e42-0394-3291-9a16-b39796b5d4a3 | -6.44169 | -54.96842 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56fe0d1-4ce9-3a99-aecb-7f06a2029c37 | -6.96207 | -52.80835 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e65770dc-e195-3c8e-a2eb-7e3c5f317c55 | -8.62147 | -54.73872 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 534f4bc8-9901-3d72-8bf7-d327a6af7cf1 | -7.01356 | -59.24414 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13969ea0-b9a0-39e4-8297-71c271a34fdd | -6.25331 | -55.42142 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 352ed54f-aa5a-3549-b5bb-d3407f661b99 | -10.90837 | -50.24528 | 2026-08-25 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d2d401d-028b-3041-8cf3-428a72204c16 | -8.82036 | -62.33569 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 59a20009-2669-306b-8f3a-19d39c1acb9c | -8.54537 | -55.30086 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a284826-8c5d-336b-ab52-c4709e94f99e | -7.05132 | -56.62119 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54ae5f50-16ec-3dc8-a444-5b46d80b1b10 | -8.15677 | -52.01925 | 2026-08-25 05:12:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11ef6c0b-2a1d-37e4-8758-efe1545d6d77 | -8.21544 | -54.98761 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a627a95f-b8aa-31c6-8dd9-f9f110a72bc8 | -7.20867 | -60.61506 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e2268a9-341b-3914-ba99-b0b11cfde278 | -10.91482 | -51.07248 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f934e2f-bf19-3597-9a02-276f566d78c6 | -8.55099 | -63.18413 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f75a279d-585c-36ca-b73a-898149abab43 | -6.22338 | -55.92085 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b25bb668-8a96-379c-9560-0a6333200ba8 | -6.86851 | -59.44655 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c71c63-82a2-368d-95a9-21012173e94b | -6.63882 | -58.50265 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 60c68b3d-4aab-3dfc-85eb-ed0f2ba4760f | -9.06543 | -60.43795 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 208e68a4-452e-32fe-9758-fd76dd56b699 | -6.8661 | -56.41157 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ebc07d0-e851-36fb-986e-596adade213b | -6.25846 | -55.41068 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcd307b5-8345-327c-9b3d-e7e567209fef | -7.22087 | -60.6243 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b58471a1-04fc-3abe-b364-d19763dcc159 | -7.53577 | -61.35106 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08dc2a3c-4c82-3a34-8993-a7aa8d9b1a28 | -8.80825 | -62.31406 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85d9f53b-f79f-3f97-9411-fa87b8960f14 | -7.51486 | -55.584 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7a06eac-071e-3623-8790-7a910deddf7d | -6.63493 | -58.50565 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b679d18-4ba7-3749-93d1-4d7ae9347d56 | -5.94386 | -57.73184 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c2439ea-458a-3387-98ca-4a71b1af1959 | -6.79906 | -59.81689 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b646826c-7cd5-3127-9933-6013ae8686cf | -6.81257 | -59.687 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac32730a-78ac-3e4c-ad48-871bcb63b0cc | -6.97339 | -59.07409 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 700f3e68-a789-3210-b8eb-58b29045b3de | -8.61982 | -47.15303 | 2026-08-25 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de1ec7ad-a811-38be-9ba4-c30c82533ccb | -6.22229 | -55.9281 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1d2ca54-3997-38f6-b8b8-4d3948741693 | -8.81652 | -62.33504 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74bc5e90-5443-3310-a027-cc5c9eaa0c9f | -6.437 | -54.97572 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25b20710-af5d-3a14-8b57-ba0ac5029a86 | -7.60782 | -61.18918 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a03b2aa-f31d-35c3-aac5-5294d535b4eb | -8.17145 | -46.70246 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README56.md)
