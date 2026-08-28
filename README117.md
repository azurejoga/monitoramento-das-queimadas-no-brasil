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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe68cbf5-f59e-3bdd-8ba0-4cb534dac348 | -8.59688 | -54.78561 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c27310c1-2307-3496-b156-845d8ec22cff | -6.41635 | -51.70225 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73dd712c-3f93-3f5d-b252-b52af68f55b7 | -7.2731 | -49.85894 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1ba9e067-ecbe-3289-826e-52ac780a0849 | -6.03202 | -57.8176 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8486292e-4254-3eac-abcb-b1fe1030c3dd | -6.53944 | -55.24268 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 935aa2f3-5647-3a84-9f49-1221804751de | -8.79931 | -49.99076 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f3435339-1176-3499-aa91-76228d81ea7d | -8.11415 | -51.66143 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f31087c0-5878-374d-afdc-1a89dfecc6e5 | -2.71619 | -47.04517 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 937d74dd-cd5e-3db5-b397-0eaee7ed8cd2 | -9.00542 | -65.45056 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 487d1540-c4c9-3529-908a-042eae17ce34 | -7.47857 | -61.4146 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f8b1c87e-3c5f-3be2-ae57-cdf3322ba15b | -6.43438 | -45.29724 | 2026-08-28 17:28:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12c624fa-8c51-306b-9427-762bd4e0a290 | -8.59243 | -54.82426 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6e03575a-e1c2-3329-a117-5c6d3a516398 | -7.25865 | -45.85775 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77cf348e-11d7-3824-bc50-147e2a602fe8 | -7.04845 | -55.68459 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6d3440de-1526-380f-8fe6-7024b3e7663f | -8.81896 | -68.99362 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8d0f54f7-281a-32f4-a756-6a2422b5ccbf | -6.83182 | -55.61634 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 62e22a47-9611-3a62-b38a-e6c40c2e4a44 | -9.20899 | -51.547 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9dc589e8-1038-38a4-9ed0-f961f2a09f5a | -6.77282 | -52.89903 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c989e869-d215-3efe-a728-0f3dcf443909 | -3.73573 | -57.23231 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b453bece-26d3-31c7-897a-45288c39fe1c | -5.77328 | -57.56061 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f747244-f99d-382e-ba22-b3b78df67fc2 | -9.7068 | -48.13087 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cca371ab-f0c8-317a-9895-b998a622d906 | -8.63192 | -66.5354 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 63a2fcce-597e-334c-bd99-9e092cefffa6 | -9.22432 | -59.7767 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| dcee6082-3362-3e45-92ae-981effb023b1 | -4.3295 | -54.90439 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| bfdddce9-3dc0-3b33-9105-5086cc8695c0 | -9.93026 | -60.44129 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e92c302c-3f7a-3069-97fd-920330211beb | -4.45234 | -55.39187 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0fdecab4-b239-33c8-bfbc-c6ad4c80cc91 | -6.82676 | -55.60608 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e0ef9dd7-9965-385e-86b4-8aa502ee2ef6 | -9.97436 | -53.94088 | 2026-08-28 17:28:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9139a2e1-cd45-3da5-b1f1-d1c921975ad0 | -6.32571 | -54.74168 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 588c1f7d-67b9-3caa-b6c3-41d9f67ee181 | -4.29831 | -59.46914 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3e756e31-52cc-3910-8450-a6aac21d2b9d | -8.98236 | -65.44012 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4c6bc734-62dc-3f3c-bb48-22a2761acbfc | -6.41272 | -51.68047 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6b84643-8cc1-39cd-8da1-9c27339f6c35 | -5.76941 | -57.55764 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d093250f-2871-3735-9436-95141c5e11b8 | -6.31875 | -54.74278 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 05160df7-8df6-3ad4-b2f7-76ffd257fd12 | -9.66584 | -55.08236 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54f77b63-18b5-389d-ab1d-6f79d8e2bfb2 | -5.77047 | -57.5646 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3fd6fb22-2974-342a-b6df-72126eac9843 | -7.35343 | -55.15827 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a111b00c-dc2a-3df7-9cb7-32551bd712b3 | -8.4599 | -70.41923 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d04e5f29-6a05-3848-9cd4-cf4042916011 | -9.91866 | -60.44289 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 772ad9ef-9547-32c3-937d-14635ca454f7 | -8.47012 | -47.66175 | 2026-08-28 17:28:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c1d2cb59-e892-3f5d-9b1b-df33038c35fc | -8.54804 | -55.30076 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f065a20-b385-323e-b5e3-2c204243b0ee | -6.75005 | -58.71993 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 819a69ed-39cf-37cc-a39a-51e8882ec13c | -7.05695 | -51.65678 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9bd5a97d-b887-3480-aa42-ff5c51a4af1f | -6.24546 | -45.96307 | 2026-08-28 17:28:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5906e236-7fb7-313e-8f94-7c9e86117efc | -9.20625 | -65.79634 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b4e4d23-5189-3f62-813f-2eb4585ec479 | -6.89964 | -43.6492 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b91aee08-b438-34b4-809c-acc0f020d581 | -8.59462 | -54.79357 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 5b9aec66-75b2-38a2-899a-5dee42bf5a3f | -9.86976 | -60.26011 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5ffd5671-a1df-3c2b-941f-e3390c127092 | -8.6027 | -54.71574 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d67ee824-058b-3b37-a50f-adda25a0858f | -5.93972 | -57.72754 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a38dc84-d88b-3589-99a3-4b09b8038f6f | -6.98998 | -60.65912 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9e946cf-7554-3a5d-93ea-e62f40d0405d | -6.54227 | -55.23846 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 9d8ccede-83dd-3fb6-bf6d-c2717bc4e595 | -7.35911 | -55.17229 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 774c588c-82da-39be-9fb4-e087ec4f7f08 | -8.95882 | -62.38066 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| b56f140b-e534-3590-a79d-0889544cc00a | -10.75547 | -54.02531 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 4c1891fb-0eed-3df4-8ba9-d77850ae548c | -5.76661 | -57.56162 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c50c3f9c-0b1d-3945-baf6-97761da56f1f | -6.95289 | -59.48969 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9d36c020-3304-3539-9cc0-637c40bfd645 | -4.47479 | -55.39992 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e5afb208-f1dd-3ec2-a71f-6615cfed2a0e | -9.69932 | -65.10225 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 153eec75-e68c-3fab-be40-d66013341965 | -10.76021 | -53.97385 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 47f3fd20-0f97-338f-a20f-2de0788202cb | -8.98812 | -65.4427 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e87b59f8-d63b-3f8b-a0a8-dd329951a3a9 | -8.68455 | -62.84592 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 77996121-3e98-3345-b3c7-b35a04e122c5 | -6.16898 | -57.79192 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac4ce646-7005-34c0-9187-6674dfa7bcfc | -6.8438 | -59.94516 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e4500ff9-8295-3073-948a-4d0b27b47a55 | -9.18475 | -59.63282 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 584e7a92-3aa0-3dd3-bc70-044ff7c59030 | -5.99507 | -57.68698 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0a3726b-dfcb-3aac-bfea-4b4774339fb7 | -6.70126 | -59.46153 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57f875a1-9359-32eb-9518-948f91222d09 | -4.92928 | -55.76674 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 15f2aa57-79ec-3f1d-9cfd-04d34dbed310 | -4.89212 | -56.26851 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3103ae5-9a25-317f-a007-95a6c93d8453 | -7.54892 | -57.72947 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9f0cbe70-726e-3aa7-9193-08d65eac06ef | -7.45983 | -61.39654 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5ca6ff1f-6489-3ff4-a04a-020d131735fd | -5.80979 | -57.62981 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb3c7321-2c4f-3e95-a880-a01f016ecf1b | -3.91298 | -56.0086 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8bf6a74-74ff-3d38-b678-b539b54265f3 | -8.23397 | -54.96534 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 74c178bd-411d-3d6a-aabd-4d2d1a48690b | -6.10694 | -54.49389 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e7a56de7-7276-33c3-a27d-37fcac1f4ef1 | -8.13851 | -64.00123 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f1a0fa7-3f8f-3649-949a-a93f372c0fc0 | -4.36096 | -55.12619 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c65c412f-d6c1-3051-a3d3-f5d5cb02da51 | -6.83126 | -55.61275 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| beb5dcad-809b-3426-a4bb-108abe89d8a1 | -3.03223 | -43.84556 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56cffcc2-5318-35b5-b749-2a2b66c9680e | -8.04307 | -45.86267 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 68f81025-fb11-37f5-9d1b-6337c80d2054 | -6.01339 | -57.85278 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3929fe89-1ab0-32ef-97b0-b8e8f8497b8f | -7.35401 | -55.16195 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9611715-3013-3392-8efb-0319dd99708f | -9.6989 | -65.09902 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 59e70c2c-a1ed-3437-97a6-962f3a751578 | -6.9446 | -58.94772 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f503cfca-8a3b-3cb6-ab03-5b2c2ba134ac | -8.96421 | -48.16667 | 2026-08-28 17:28:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0baf10ce-e553-3669-b2fc-e4a2bd307e1d | -7.01252 | -59.57488 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b7acf76c-2e58-36c6-92e2-c138b0d891df | -6.76684 | -63.06218 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 003a7723-cdbe-39a5-bdf7-b74561d222f1 | -5.99183 | -61.46624 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5aa4000b-9154-3c4c-968b-4f4d317c073a | -7.55228 | -57.72896 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 17fbcaf7-e613-3842-8702-48731e9950ac | -8.03341 | -48.01501 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73693d81-ae74-3ef2-8584-e3a56c3adb3a | -8.5948 | -55.28187 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a2ab513-d236-34b9-b67f-5e1d07909fb3 | -7.84132 | -62.31403 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1485dec2-f18d-306d-99a2-f5d2c88a2b54 | -8.23006 | -49.94737 | 2026-08-28 17:28:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d99a4ca0-4132-3fb8-b677-5de5c83957dc | -9.24301 | -57.07954 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ec749c6-d40c-3507-a791-0b556225f805 | -8.82713 | -49.59876 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ed985591-8d57-3180-8afc-f775071e36b1 | -6.17717 | -57.66513 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fddb8f4-7b06-386e-a833-8867c2e83b53 | -6.74662 | -58.72044 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c5d1e79d-8fc8-31e1-b546-38a26dc5d039 | -7.03162 | -55.68721 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17d40d5e-3ccd-3f9d-b813-9f712015bfa1 | -7.50182 | -55.28426 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c9ea331f-216f-332c-bf54-f309330a6d0c | -8.82121 | -49.61884 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README118.md)
