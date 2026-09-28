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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9667699-e852-3925-8200-c5a8676fcc89 | -7.19645 | -44.17585 | 2026-09-28 17:09:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b87f995-872b-3584-b7f4-cc2bdef9d5d4 | -13.51134 | -61.13743 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| da551503-c0a7-32ef-b108-b5ba9754060c | -11.0791 | -46.08622 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 388320ba-ab90-355b-a77e-f10e97ad3a39 | -9.78652 | -45.81665 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1e7d837b-3f71-3b20-ba8c-0589b5592848 | -12.14749 | -61.16595 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 890fd32c-414a-3da0-927d-02f4f7ddd178 | -10.70219 | -48.75319 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc933d23-8717-3779-97dc-d49238d77309 | -8.09763 | -44.00901 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dcf70928-6592-3ba2-8033-e639a9536353 | -7.42011 | -55.63844 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98a1c912-c4ac-3d87-9617-63e170c8e315 | -12.15591 | -50.3851 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3a969018-9654-3a59-84ac-0b199a34b39a | -9.52611 | -46.37521 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6da4825-7969-315c-83c8-044a21bf0665 | -6.33607 | -55.32448 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d2568316-171f-3b26-9f7a-be5b8ac958d0 | -9.11212 | -49.90244 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 4e5fbe33-cc0d-30d4-ba3c-30d5c54d3ccd | -6.65191 | -55.10115 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c05afa3-f5e8-33b8-80c2-c83e5bc6c6f5 | -10.63476 | -50.58508 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 102631b9-4401-36ef-85e7-7c7afb0251a7 | -6.30815 | -43.60715 | 2026-09-28 17:09:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0f869831-d8bd-39f6-9467-1fca70fbaf3e | -10.55226 | -57.43716 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3042c29c-2c87-300c-b543-cf34b4c5a460 | -10.50459 | -64.0732 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 62185069-7911-36f5-9059-ffe7212c2583 | -11.38214 | -47.39635 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f43410ec-0ea3-3b0d-af20-51aeb783a841 | -10.82154 | -57.22212 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d0316c2a-c26a-3fb3-ae24-270255305b39 | -6.15324 | -51.57263 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| afc7c7f3-ad9f-3990-b047-a306a88b69b7 | -7.68724 | -54.75864 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7f61ae95-943a-33ea-abdb-efe62e6a49fc | -6.1116 | -53.48983 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 39ab917b-c19b-36d7-96eb-2178ff109290 | -10.93942 | -43.87844 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 02ffb20b-cca2-3418-b2d1-036534654467 | -8.1775 | -44.43456 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e28cd551-cfec-33fd-bdc3-16a78d0f6f23 | -9.72977 | -53.87069 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9286abb-3a1a-3fd5-967c-f9378876ca32 | -7.3817 | -44.76468 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5e975e8a-442d-366a-bd05-1f608c8a8389 | -11.64877 | -50.68097 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 411b564d-baca-3edb-a0b8-5b93bdaf05e8 | -11.86074 | -47.08725 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5d46f08b-2927-3174-a597-45f94c62d5f5 | -6.13793 | -52.72768 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 68cd9d41-48e1-3263-ba49-a69d39dfbd20 | -9.86924 | -43.6204 | 2026-09-28 17:09:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| cc5f5eb4-c081-3d16-a6c7-550b02b5c7a2 | -11.06501 | -52.46775 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 32aa2cc4-652f-3ddf-ad86-9272b992e3ce | -10.25575 | -44.59856 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 202c05e2-a8db-35e2-9ba4-22debdb9b665 | -9.73474 | -53.8808 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| beafe1d3-a820-32bc-b9f9-d8b70ac145f0 | -9.96256 | -51.45306 | 2026-09-28 17:09:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8ef66e15-84e8-3f9c-9718-1e1c227f0950 | -7.76571 | -54.78117 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ec7da10c-5ade-3889-9da4-2ee458fa6a13 | -7.4945 | -63.81268 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e57d5b70-388e-365c-9110-e6c125202c1b | -9.40038 | -46.39115 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b0fc2fd9-cc7f-3dd1-b62f-96bcb128837b | -10.81944 | -57.23382 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| aff4e601-8224-38ce-b48b-b587caf8db20 | -5.79702 | -46.08898 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cc03df0d-d9e8-348b-9755-297a7f533f22 | -8.93475 | -47.42572 | 2026-09-28 17:09:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c47b875e-bd25-380c-b962-c902656a1f2e | -6.1671 | -52.91062 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8df2b0db-b745-3eec-89e6-38ac8cdf2964 | -7.50718 | -55.02567 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 36ebd49d-ab73-35e9-a87b-a6bd595488cf | -5.79765 | -46.09256 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d4d5fc4-c5b2-3564-b584-fd1924e478ad | -7.27297 | -46.92955 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5d047858-274c-3213-8427-ec7cb8e14a2e | -11.73584 | -54.5165 | 2026-09-28 17:09:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0c40f743-3812-3971-b097-357fab4506e3 | -11.06624 | -48.89546 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c6e26e6a-7d63-352f-bd0d-f37c569d54df | -6.16359 | -52.91117 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 66933541-3008-357e-89b5-575ecedcd7ff | -11.53769 | -47.39759 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 56262513-596c-3b4c-8f27-13fe2e18ddd4 | -9.43906 | -46.54897 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c389a435-f5fc-3580-9e3a-e28df06264d2 | -6.52751 | -55.37939 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e336fc0c-b999-3c80-a938-31f78b5ad46f | -7.90272 | -54.767 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 1cff5154-1300-33c0-a945-de45eabdfd30 | -6.13024 | -53.0483 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e563e4cc-28de-30f1-936f-ba32737b90d7 | -10.20078 | -50.00765 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7c105bbc-ec18-34d6-bb50-c386fab98937 | -9.3281 | -46.56714 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ad2c086-5e54-391d-a84b-e52f1ea26088 | -12.06649 | -48.54811 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 29618bfe-c522-3256-884f-cb858d916052 | -6.1563 | -52.8881 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 53ef22fa-a419-30cf-8bcf-39a069af387a | -8.63048 | -49.47673 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82f94cc8-21b5-397b-b72e-35fe2528b1a6 | -8.24221 | -45.46282 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5add3c7a-d5ef-31d7-aa66-aa18adbc10a5 | -10.10298 | -43.95992 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e1a348f1-2426-3363-99cf-3279275b9be4 | -10.45717 | -47.47961 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7770e511-0a8d-3bd7-98d4-2da0694ffdc1 | -11.08622 | -48.88796 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b2730145-0ef8-39a1-862e-e8036a37a073 | -8.21543 | -56.09019 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b1c2930f-997f-385f-b5bf-40fcc2083f3e | -9.32823 | -46.56463 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7630680e-6615-34a5-81ce-060731716fc5 | -8.60197 | -54.64775 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f845c0ad-b1d3-3768-b68e-359dcb7a2471 | -10.75716 | -48.77159 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 37934918-ffc0-378b-9691-4a338cfe8ad9 | -6.23603 | -53.30041 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 91056300-5b79-3788-915c-88fce60fc70e | -7.43003 | -55.63693 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| df467682-c3c4-3a4b-a7aa-0d8b5a2137f2 | -8.99973 | -51.25639 | 2026-09-28 17:09:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d675c81d-a8fa-30ef-817f-120baf6c44e8 | -11.56495 | -47.38575 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e97837d-8d38-3382-b661-956c639a5cc8 | -7.69439 | -54.76109 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 351a7ad6-9406-3889-8b51-51da9ab4b666 | -10.266 | -44.622 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 52a377c8-7123-3b97-bdd9-d090d2d4c040 | -6.68975 | -45.64448 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4c51cc9e-a83d-3514-ad18-739295d0b1c4 | -11.07417 | -46.08746 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac75c715-42af-3e9a-be9a-54f59b9bf209 | -10.21389 | -49.98993 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 965a8d75-7653-3629-92ee-6d91ff893a91 | -10.8651 | -48.51281 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a31769fe-1554-377a-9e89-910ff69ee81b | -8.2377 | -45.40565 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f262bb08-6fac-36eb-b57b-b511a326d0b9 | -10.90571 | -44.66131 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 008f0204-8afd-3609-bc20-2a620ba66b9b | -6.01064 | -53.90005 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0be39b45-5bf3-32c2-997a-dc1739ad93d0 | -6.2223 | -46.63657 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 22819686-9b97-375d-95b7-90ac7fa73924 | -9.27979 | -51.73487 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d52a47b-b427-3c5b-90a9-990507d90750 | -6.17215 | -52.82884 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c563bbc6-d6c7-3837-bf00-51f480c8358b | -9.03265 | -45.98714 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76958e6b-a42d-3cb4-8a61-53aa6c77823e | -6.17746 | -53.28238 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a8654b55-231c-3f66-8837-69e7674640c2 | -9.64576 | -45.54841 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34176404-bed4-3218-8b51-4f1324efb4a2 | -9.48469 | -66.78423 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| caa74dff-23c6-3b6e-931f-fb424dc81f2f | -9.43293 | -46.54782 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bd3a6c8a-e87d-3428-b3a6-7a2aea953630 | -11.07037 | -48.89473 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7dc208a6-4a56-3544-a226-60a295bf6121 | -9.07493 | -46.5049 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 416af0c8-d762-3927-9fba-b83aac59955f | -9.31766 | -46.56609 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9af15e5-3b7f-38f9-886f-52f0e5cf6698 | -12.79756 | -54.01369 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| d47dfdae-a8b5-3ce5-a895-3e01272b077c | -7.75963 | -54.78566 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af217269-4d67-319e-94de-40a28d3afa9f | -6.01007 | -53.89642 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 51f2fe54-be30-3d82-9a58-eace9e5e85f6 | -9.49719 | -46.35505 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 14c89c44-7d9a-3844-82d2-81cf4c62681d | -12.6688 | -54.6447 | 2026-09-28 17:09:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4b2ba5b6-3e9f-380b-8254-5746f1d3efc0 | -6.16094 | -52.82657 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f03c95eb-1751-39ae-84bc-4ebcdde31683 | -7.26291 | -43.36888 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 93566b9a-2ee7-36f8-8496-c278520d6ae8 | -6.38133 | -55.13362 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7821a106-948b-368d-9bc5-0c9022ac881d | -11.17255 | -44.80257 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03069dad-8836-3c07-9ce8-9faafaa94156 | -9.51615 | -54.64764 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fc7bb5d-8df9-3da7-8106-9c7262e0d642 | -11.42085 | -44.96689 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README148.md)
