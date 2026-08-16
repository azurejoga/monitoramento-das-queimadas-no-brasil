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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a4aeeea-272c-3c51-a684-f4f9f913c2a3 | -11.21654 | -54.82247 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e04c9814-889f-3df9-9ab2-270680a1222f | -8.61172 | -54.6804 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b3929e6-863b-37f8-b8f3-bc358599a503 | -9.37146 | -57.35703 | 2026-08-16 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f245532e-3490-3798-8c89-972bc4a116ad | -9.47085 | -60.50829 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b7f4856-4d8b-3ee3-8f9c-a40a0c3a7081 | -12.45522 | -46.65062 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87ba29e8-5009-345f-92e6-1e0577b43a4c | -7.42273 | -60.0128 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff2d5606-21fa-3461-b4d8-a4c8e870cce1 | -6.62884 | -59.07648 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fdbcb57d-daec-3141-96d9-f3a2a7b39e61 | -11.22873 | -54.82414 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ecf2100-4757-334d-ab18-087957f7dd92 | -6.42986 | -60.07616 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e561baa6-c3d1-3814-b626-7eae9312be0f | -6.24907 | -55.62037 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 131525c2-10e9-386a-859d-709d5443a8be | -6.6336 | -56.39929 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d8919ae-aa65-39c8-9241-66f502cfa9bf | -6.11821 | -57.71837 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a639e07-1dca-31d7-bb41-ee8f332aac09 | -9.35532 | -62.36546 | 2026-08-16 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 869580f6-b7e0-3032-888d-30fa7b098019 | -6.84923 | -58.9626 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01172b3c-21b2-347e-802a-323aa7c4263f | -6.85029 | -56.42006 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a408d12-9351-38a5-b050-81bafcea3f73 | -12.03436 | -46.43807 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0400b568-9622-303a-8809-111fe144fc68 | -8.65112 | -54.72013 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883e0491-c9fe-3ece-8941-e5af33084dac | -6.60777 | -58.97944 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0385a2fc-bd7e-3e46-9704-076b897ab387 | -8.97227 | -60.50395 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b0ca5330-3829-3fc3-957a-2346cf9140ce | -6.09376 | -57.72261 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b792611-1294-3ab3-ba53-67cc840ada94 | -11.50753 | -54.61755 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af0fe28c-cece-3870-b76d-554342a8ad01 | -5.23136 | -49.33321 | 2026-08-16 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 814378da-95b0-327f-a8b6-4abd0ff8dc89 | -8.64638 | -54.7048 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a07f3da4-7f8d-3818-8b6e-656348bf072f | -6.85417 | -56.43848 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 005435d0-82fd-39ba-b81f-7a46fe79dc09 | -12.0156 | -46.44385 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| cc067911-4ac7-339a-b350-9dae81482737 | -8.65682 | -54.72856 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56d38124-319d-3a6d-8af9-3891bbfa3424 | -9.13077 | -66.97592 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8ab0ab5-fb5b-38a3-ba0e-e9d35848dd99 | -11.90471 | -45.97406 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed630143-6075-300f-8bb4-32ed2eccb599 | -10.27024 | -48.29728 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 312abb8c-79fc-3ef7-b016-60162689b6c0 | -8.26586 | -57.34538 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a71c100a-74bf-38e4-82f2-94dd28dcd109 | -6.85438 | -58.97609 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b96dfb4-47c0-3c99-8863-9e1d06ea050e | -8.96302 | -60.53574 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d004e9b-cb00-32df-89ab-d195dcff4e47 | -6.25544 | -47.69584 | 2026-08-16 05:16:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec690887-5e10-3cfb-bdef-c9f4f05a781f | -7.34631 | -59.59285 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 136e06be-f1b2-3c5b-aa9c-0f5fb04a3eef | -9.14555 | -59.64566 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9889eef3-7b12-3e07-80b9-ce784ba48313 | -6.11207 | -57.71799 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77ce5d0b-27e1-332d-a172-a26cb207d3f1 | -7.39495 | -59.99439 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9879c6bd-3b32-3ad0-904d-f2ae74b54c04 | -9.47272 | -51.6197 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 940697d6-7c88-369a-8900-f9a543313df7 | -11.33731 | -46.2099 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 205f27c1-eb03-3aff-a9dd-0b23ef9b78fa | -8.96615 | -60.51718 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d45b738-7aae-3220-8f0d-f104a53289e4 | -6.62523 | -59.07589 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a0c3e12b-4ea5-3275-99db-a71c182b9690 | -6.6221 | -59.04972 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1873d6a-5f4a-3ae3-83a6-fbfa01d70704 | -11.70634 | -49.07609 | 2026-08-16 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b89b2d2-33f3-3436-932f-c48f36cde739 | -9.14195 | -59.64507 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6904131-e994-3da1-83d1-6b3acbc92bb9 | -8.54847 | -54.59543 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ae8e80c-31ad-3a7d-a1e2-d4b5321921c6 | -8.95372 | -60.56768 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b141bf3-2ea0-36e4-9f2f-3a54d0d71651 | -11.50459 | -54.63729 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e057d33b-55a4-33c6-9e8c-55542ce0a951 | -6.39505 | -45.69389 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05710c68-0af3-3594-92d5-fcd727e9d147 | -11.88779 | -50.62254 | 2026-08-16 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8f7763a-b068-3276-8a32-f4c5fdd1dd74 | -6.63245 | -59.07709 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4612f675-0c72-38df-b024-2be1a80fa490 | -8.61114 | -54.70678 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7f38a59-d6ef-3a25-b3a6-4f6180cf4f33 | -6.59817 | -56.36512 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a777fa78-ce51-3ae3-8647-5bba1181b20a | -6.88249 | -59.01739 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53903ac-05c9-3196-9506-6de741889628 | -6.308 | -43.6117 | 2026-08-16 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffd724aa-bc15-34cf-90ff-d7eaa2c94b48 | -6.11943 | -57.71095 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c427bcca-916b-3faf-83a8-b4ae8ca60517 | -11.50809 | -54.63782 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9b2921c-673a-309e-85c7-d06fbdfe90f9 | -6.81319 | -56.46049 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d468f5c-f94b-3d84-aa81-7014c3a45b66 | -11.50927 | -54.62992 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c909873-591a-3847-9e22-4603cec4d184 | -8.9608 | -60.52579 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 73be672d-9029-3ddc-9d0a-6ba3af89762e | -7.09851 | -55.45154 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3763ceb9-8436-3f46-83ef-59600d9d9e5f | -8.65738 | -54.72488 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54298f08-0e05-3e38-9bcb-2c3923015c02 | -6.78537 | -55.84791 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceeba629-db57-37a4-8b83-06609faa9be7 | -8.79897 | -45.7879 | 2026-08-16 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a155d087-89e4-3bba-b121-ef4f28f2e202 | -6.81263 | -56.46397 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee501a6-c4e0-37f9-a82b-0d18b8615373 | -11.70669 | -49.07702 | 2026-08-16 05:16:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c301c4d-5944-39e1-8df3-7a25c2306c5e | -6.85729 | -58.98077 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0ecaf5e-fc1d-3537-8d9e-ea4392cfaa5a | -8.95436 | -60.58704 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3cd97ca-7796-392b-87e1-a849262ac600 | -11.32458 | -46.21518 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57b45bce-f2d3-32cf-9c43-cae90801fc98 | -6.96456 | -59.30698 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d0e1ed3-7712-3467-9d3c-d1e2207cd42e | -11.89385 | -45.96189 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 692318f9-6c96-3919-ab9c-419e6f5aff6b | -6.81984 | -56.44014 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ebfeb70-29e1-30f5-8787-01984e6415be | -7.34118 | -59.60092 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6e081ec-039a-39bb-bd97-f3fb40fb3ff1 | -6.83313 | -56.44226 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c73500e9-2554-3163-a474-ba3f88f82a2a | -11.08209 | -47.25256 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29a40782-a76a-380d-a3f2-228c65b11a1a | -8.97149 | -60.50858 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc45ff98-134d-3dbb-ba7b-3bc233396145 | -8.59807 | -54.70095 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5024ffa-e0a2-3c73-a50b-c36f4f7e15e8 | -6.71523 | -58.9413 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e8beb81-bbd4-3f26-b17f-b50e89eda431 | -9.48184 | -51.64223 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae34cda-08f2-3047-88d6-fcfad8fe8aee | -7.3375 | -59.60032 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 969dcdb6-2881-3a93-974d-c7f7589fc98e | -6.8358 | -58.97722 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0831d064-a618-38cc-8108-3bedb3b20979 | -7.36948 | -46.81199 | 2026-08-16 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4c08c4d-57b1-3e7f-8e8a-a146a0194b38 | -9.29605 | -56.80883 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8825e5e-c4f1-33ef-bee2-31315102da22 | -8.65625 | -54.73225 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbf1ea38-2cbc-3b74-bc5c-e69fe26a4e10 | -12.44656 | -46.65553 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbcf8c6b-4ab5-37c5-a1b8-f3529155b77c | -6.86191 | -56.41122 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01d06d4d-58c7-3c59-9ca7-35fb06dcce0f | -6.79288 | -55.69267 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e43c294-4b94-3721-91aa-13a4a9a2b29f | -7.40693 | -60.01495 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3579bb57-0e7d-3948-9cb0-271ced2f30eb | -6.11601 | -57.7104 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6393f2e-4cd9-344a-95cb-1ef1cf46497f | -6.53806 | -55.18073 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f18670b-5c03-3f04-9c0b-6619036ab8ae | -8.5422 | -54.59064 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34854be9-9df2-334a-a249-092f132c0dba | -6.6237 | -58.99478 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dab337f-1d64-39f6-9242-b6b41a0e62d4 | -6.81762 | -56.45406 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 905e314a-6ac0-3a25-9d6b-ff1183061fd6 | -8.65854 | -54.74015 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b507a2d-f329-33b8-90a1-39dee9043575 | -6.837 | -56.43932 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d7ae2bf-de95-37b4-9e60-385cdbabc757 | -9.14542 | -68.20633 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 492d2df5-2e56-377a-a4af-390036a4feb7 | -6.62748 | -59.08483 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2847af1e-e537-3048-a4a2-386be8e42373 | -9.48482 | -51.65005 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d87c1b29-349c-3923-9dd3-34f2befd0e2b | -6.24576 | -55.61985 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35a2a122-9a6c-3b7a-9846-e1b95ee7e94f | -6.9719 | -56.46058 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48b48be8-53fa-3c49-a8d4-92babe8ac474 | -8.98207 | -60.51511 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README34.md)
