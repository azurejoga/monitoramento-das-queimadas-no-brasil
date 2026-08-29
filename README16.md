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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c5b4f0-380e-3ce2-9aa0-684de9e61a7e | -6.7639 | -55.652 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccd14be-1951-326d-a1c6-3cfdc2d41b95 | -6.7404 | -55.462799 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7febf97b-4034-3ecc-8712-8cf39154a218 | -6.9176 | -59.483299 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5638f1a-01a0-3a7c-95ae-6d2702014fec | -14.9501 | -56.306999 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4b75c22-6b62-3fdd-b34c-1cc369439d43 | 3.2887 | -60.608601 | 2026-08-29 01:16:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8a806952-72d0-3436-97ce-630a1e742f9f | -6.1692 | -57.771 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c89524-7025-3e3d-b734-457c0d36b18d | 2.413 | -60.8741 | 2026-08-29 01:16:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fd58f6d9-8f18-3e80-ae2b-2ab704ba6849 | -14.1924 | -52.853298 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc44640b-2e26-3158-9fd4-8d5bb10ca3ea | -8.2428 | -54.9575 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f984c229-fc69-39bb-a46b-29d5ac614f06 | -8.532 | -55.266899 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6811136f-6696-343a-b10e-474b47f6e74d | -6.5777 | -56.540798 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8b6f4d-e7c7-3db4-94d6-c7e046526128 | -11.2305 | -54.004501 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0037d7-e878-39c2-804d-824df35b8534 | -20.9412 | -57.5811 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e42083c-993b-3821-81ee-a35b9b64cac2 | -9.8717 | -60.2896 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad5cb150-3046-39b4-beb1-a938762321af | -9.258 | -57.072601 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8db4f818-5127-3dd8-9aeb-597532b3533c | -7.302 | -49.532799 | 2026-08-29 01:16:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0d4573-0a79-374c-8222-b61468198ccb | -10.4776 | -64.470596 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb07c3a0-2066-39e2-b8f7-e9fa1e3b33c9 | -6.9502 | -58.941101 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb278877-c38a-32af-8c55-41233cce40dc | -9.6107 | -55.111401 | 2026-08-29 01:16:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd8876f-eda4-33ae-8f93-4559aa6e28be | -11.0324 | -57.2145 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1ee8582-5ecb-376a-85ea-285c9d64241a | -18.999399 | -47.442001 | 2026-08-29 01:16:00 | METOP-C | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdde843c-7e2b-3082-bf42-08e788cc1d91 | -6.5794 | -56.548 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a783dc-913e-3b04-b526-f8ddfc911cd1 | -7.6098 | -61.352402 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55c9254c-cd62-3781-bb3c-0dd5ee125c78 | -7.3063 | -49.550201 | 2026-08-29 01:16:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbfcb90-aec7-3881-a3f0-bd9bae5d6d96 | -5.9855 | -57.689602 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44688b1c-93fd-3620-bb8c-7d73682c459a | -6.7611 | -63.052299 | 2026-08-29 01:16:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9b0b9e-6d21-3d19-8683-1e1d0188fb82 | -10.4838 | -64.500603 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 703a971d-c8f7-3a9e-ae93-8305d77086f5 | -8.6021 | -54.7728 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74f138a8-43cc-333a-885d-8f7092784d28 | -11.0406 | -57.205399 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 601b40c1-a170-33b6-b97e-bbea5ceae683 | -8.6244 | -54.691502 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f673aa2b-0c27-3b0e-a417-8aa38bdba7d1 | -9.309 | -56.798599 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16707325-9337-3a44-93d1-7492d020fc8f | -8.5961 | -54.7911 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa5df8e-7c69-3927-a2bc-ffcace3b7a82 | -14.9321 | -56.3186 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c53a07e1-4191-3ea3-9677-520222e6c755 | -6.6461 | -53.182598 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a75b16-3679-3c61-8065-a7ce4f44d53e | -6.7563 | -58.721298 | 2026-08-29 01:16:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a5b2182-ddc9-3491-b5f5-4f64ca3fd8bd | -9.4314 | -51.682301 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ffad90-57f3-3ca3-b20d-f67a8cf12aa8 | -11.2676 | -54.030102 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b2546ef-6bca-30dc-9f72-e895a71431d7 | -8.9774 | -50.801998 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be8266d7-e7fa-3723-950b-2f62b9ac668c | -4.2825 | -48.193501 | 2026-08-29 01:16:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a92a2a95-bb0b-37ef-b5ef-3bd7d5672ae3 | -10.5658 | -59.6115 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dce1e456-ff61-32f9-a8d3-c986acc11c2c | -6.1193 | -57.688301 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4cda52b-e6dc-3e64-acec-c71e0bc1d17e | -5.8984 | -57.759602 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56061499-6a8f-3ead-9087-391ed7a2d7c7 | 0.1511 | -60.392399 | 2026-08-29 01:16:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 979cdfcf-2680-368b-99d7-b6ded3be8767 | -6.7579 | -58.728199 | 2026-08-29 01:16:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6abfe21b-5feb-3835-8160-a1b87fc38b40 | -6.1209 | -57.695202 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c91d6a-8c88-335b-a2b3-8a4ab952a5ac | -11.2792 | -54.035999 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 386e1df1-f608-3e6e-8946-257021b775a5 | -11.2637 | -54.013802 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 108456af-bce1-3a62-8bd4-4ac2a462661d | -9.2792 | -57.075001 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31e46159-53ff-39be-81b6-b100968fcaae | -6.2669 | -55.423801 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e9428b-2e8c-3123-9b56-845a6ddf1e19 | -11.1828 | -51.283401 | 2026-08-29 01:16:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d257e285-d471-3e53-af84-dd11644648f6 | -10.7535 | -54.040901 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c30b1817-a315-3a11-960b-2cc68ee27dee | -6.8181 | -59.452702 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a90968b3-c6fe-3ca8-b438-5a2f68293c5f | -6.7805 | -59.423401 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6cbdea1-b0a0-3a94-9649-6c521bae53ad | -6.2553 | -55.418301 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be844476-803d-3032-be38-b2cc3601eba2 | -4.5474 | -54.908199 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6cc2366-e258-3032-b6ff-2b2059a14485 | -5.8855 | -57.7481 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 752ee8b7-9fdd-3f42-9b18-4fea6c11d7ed | -14.9063 | -52.637699 | 2026-08-29 01:16:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b1b64e5-9d55-3b78-88a2-2e6016308b89 | -2.7438 | -58.170502 | 2026-08-29 01:16:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95026888-db7e-35ed-9989-c10c7da3f8e4 | -14.1765 | -52.8298 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d516759-0e63-32b2-9b93-9ca40a2065fd | -14.9352 | -56.332699 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7e8f097-1e0d-3a0b-b780-3c70c414502f | -4.0631 | -56.284599 | 2026-08-29 01:16:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b39fffe5-19ab-3461-8727-c78adde31b9c | -20.9377 | -57.564201 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b7cc0e7-5acd-362b-b446-f48aa9361c94 | -7.3421 | -55.167099 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a5e49c-6b44-3db7-a6bc-b388152003fc | -7.2721 | -45.833401 | 2026-08-29 01:16:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60deda9a-d324-359b-b898-65f2e0664959 | -9.4153 | -51.5746 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7767f2f7-206b-3196-9ecc-cc2188222aa9 | -9.1518 | -49.9687 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e4656c-4df8-3921-87b2-f51671ba0d1a | -10.4807 | -64.485603 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67829c3f-832b-3870-aa07-a7ff195ead9c | -6.9419 | -58.950298 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36003cb9-44d5-3fc7-ab28-797486003dbc | -11.0355 | -57.228401 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce276581-38b3-3999-a233-2525e853dd15 | -19.23 | -57.670898 | 2026-08-29 01:16:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7b6be84-a8bb-372a-a367-cfd5c73deb14 | -14.1569 | -52.834599 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8daa575a-b367-32ac-bcbc-664e0319b338 | -10.393 | -61.232899 | 2026-08-29 01:16:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1de88a16-3955-3fc4-89c6-b7aeb55b4739 | -10.507 | -59.624401 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26618dc3-d554-30fd-85ec-13ae320a43d5 | -20.939501 | -57.572701 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf2d765a-e968-3f11-83d2-4b83b109e871 | -6.7558 | -55.6618 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fee9807-f3f0-3133-a55d-200cd7e041a7 | -14.9093 | -56.308998 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcc17a1e-6019-3933-a52f-45647bbcece5 | -11.2177 | -51.299198 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95a7f1e5-d87e-3c38-952d-d7db24952c92 | -10.7515 | -54.0327 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34cefccf-4159-376a-8f4a-3a118e3e2820 | -9.2217 | -59.760201 | 2026-08-29 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10d2b54d-4ca8-386b-a84b-49bee21e0b1e | -7.2899 | -45.862202 | 2026-08-29 01:16:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22d82f6a-9a3b-3839-b29b-fe1abf8ea99e | -20.954399 | -57.595798 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 19cf0141-1c5d-3c77-aee7-06fca8bd10de | -4.3666 | -47.748299 | 2026-08-29 01:16:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80fac84d-a6fe-33a3-9e5c-3570e39b5c1b | -4.1635 | -60.695999 | 2026-08-29 01:16:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c113e148-9ad5-30fb-8b28-d9228788c3b8 | -3.9374 | -59.333401 | 2026-08-29 01:16:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d246b1d9-f664-31e2-b32e-3454bdb24504 | -6.9305 | -58.945499 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e398c9e1-99f0-3832-8042-40ce898f3272 | -6.9694 | -55.692699 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 000358cf-fc3c-323f-9704-7a6917f7800a | -10.4905 | -64.483597 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f617a3b4-ce52-3a09-ae9d-930d96724f96 | -14.2678 | -57.036999 | 2026-08-29 01:16:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90895e27-2137-3e7a-89d4-5d847d20b75a | -5.8968 | -57.7528 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24837a62-7a45-3635-84be-dfe81f9ad795 | -8.5965 | -54.748798 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac2ee649-8e8c-318e-9c25-18fdb34eacc8 | -7.5962 | -61.3372 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8db7e41e-20a2-3e24-9408-6d2089596400 | -5.8788 | -57.764099 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8ab094-dba6-353b-9ef7-53f47c8fa5f8 | -8.598 | -54.799099 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fad71f61-aafe-3bdb-b090-e348ea51971e | -7.3538 | -55.172699 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dc01fe9-900f-3b14-ad68-8999173360d7 | -8.5302 | -55.347599 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c1f2e5-5cc6-3be8-875d-6149e662822c | -10.474 | -64.502602 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf791171-c8c2-3779-8237-b7a3ea19f7b3 | -6.1558 | -57.802799 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c53dfc-3375-3444-a4db-5c0c88b3c5d1 | -9.1823 | -56.966099 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f64e3f-d0d1-3ec5-ba31-1758702a5566 | -6.5427 | -55.235199 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a20a44b-dc47-3dd2-a655-67bc115728bd | -14.9336 | -56.3256 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
