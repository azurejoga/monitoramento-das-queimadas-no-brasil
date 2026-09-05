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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d759261f-4ff8-3ebd-85cd-93c17cffeb20 | -3.4435 | -43.269699 | 2026-09-05 00:08:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5d01f3-7c16-34db-80bf-665cd9ee4002 | -13.3169 | -44.040501 | 2026-09-05 00:08:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0935c5-2b42-3037-92df-379712fe3b9d | -2.8213 | -46.7024 | 2026-09-05 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7679171f-349c-3093-bead-bc98c9517fb3 | -7.6728 | -46.067902 | 2026-09-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c91ce13e-3bec-349c-9116-2dfc68564e50 | -10.9404 | -45.348 | 2026-09-05 00:08:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bcad153-98c5-3918-a999-21ef29ce1f54 | -4.2859 | -54.7658 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed2fa17-f661-3124-9e78-caec36bc3ae6 | -3.5836 | -51.466202 | 2026-09-05 00:08:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05ba0ea3-cc37-361f-83d7-d230b1038ec7 | -13.4376 | -43.809898 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2af6d876-12d3-3d30-8d45-90f8fa3eec63 | -21.5802 | -48.650101 | 2026-09-05 00:08:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2a2b95a-11fc-327d-a286-d1dfdf9085ea | -11.8023 | -44.798 | 2026-09-05 00:08:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fae445a-87e8-35d9-8370-cd4a9971ff3f | -11.812 | -44.795601 | 2026-09-05 00:08:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62df9d32-e72a-3628-b8b8-83ef01fcce91 | -2.4575 | -47.587299 | 2026-09-05 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76558e06-0851-3c59-9897-9a66f0ac3be1 | -19.260799 | -46.858299 | 2026-09-05 00:08:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9dbe112-4b36-3e49-8072-9f8db25501d3 | -4.1281 | -49.449402 | 2026-09-05 00:08:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81139aa7-c3b4-39fc-afef-a467cb122b0a | -17.209299 | -53.8386 | 2026-09-05 00:08:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7077e032-e5e4-3478-bc55-137b17544430 | -3.1273 | -60.592899 | 2026-09-05 00:08:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87c36955-2ec8-30e6-9877-4b36968f679f | -5.8604 | -52.037701 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e63448e-6195-3163-b3f0-86dabad5d82b | -17.5716 | -44.962898 | 2026-09-05 00:08:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 80a3e1da-e292-345d-8542-89b6f993a6cf | -10.7716 | -44.456001 | 2026-09-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fa02dc0-1bd2-3232-8cf7-c3a73e502e42 | -4.1627 | -49.6931 | 2026-09-05 00:08:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d55fcc92-3f62-307d-8db3-a5b9adf74d3c | -7.1229 | -42.2332 | 2026-09-05 00:08:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9048f14c-a893-3917-8575-4f3fd400c849 | -4.1045 | -50.439602 | 2026-09-05 00:08:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ce88ba-8896-3750-a5c3-a9bdd51af2f3 | -5.8489 | -52.032101 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae37f83-7b0c-343e-bc9f-ca6b21998db2 | -9.6143 | -48.562801 | 2026-09-05 00:08:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ca10058-e5a8-308d-9823-e861f439a015 | -7.7004 | -44.340599 | 2026-09-05 00:08:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0dde6713-bd4c-3d7a-899b-ae5e682f5021 | -4.1642 | -49.700001 | 2026-09-05 00:08:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344d6e81-eedb-391f-9ccc-79c2efee4151 | -19.806101 | -49.586399 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1824d7b3-4eae-368e-a388-82f5b4f7a696 | -5.7686 | -45.065498 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f201b9d0-bea0-38cb-9e5e-79af9cb742ea | -17.0875 | -56.806099 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39818b25-97ee-349d-96ff-92f9aa812922 | -17.103001 | -56.780102 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 432aad68-4f9f-30bf-94fe-7cc0acf259b9 | -20.3395 | -47.5867 | 2026-09-05 00:08:00 | METOP-B | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8dbada-39c6-3e66-b268-b53ef179c047 | -19.8097 | -49.604099 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ecdf07d-d0b9-3968-b052-2837a9daf534 | -1.8352 | -47.929798 | 2026-09-05 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7508a82a-17a1-3048-8ba1-764ce465d9f1 | -5.2106 | -44.312099 | 2026-09-05 00:08:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89d71843-195d-3b54-ae74-33cf960b0246 | -13.3245 | -44.029202 | 2026-09-05 00:08:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ede3aaf2-e9bb-31e6-996b-5d34ae5fa3a6 | -18.229401 | -47.653801 | 2026-09-05 00:08:00 | METOP-B | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3357195-0288-3c1f-aea4-9c45afaecfb4 | -6.2707 | -43.268799 | 2026-09-05 00:08:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4d6cf48-3280-318c-b75d-d99decfd98e9 | -4.3644 | -47.770901 | 2026-09-05 00:08:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44285571-64a0-3b14-b9e5-6274080498a9 | -20.2416 | -51.201599 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3a88c851-c74b-3be2-b952-57a88d1d29e4 | -20.7591 | -45.0527 | 2026-09-05 00:08:00 | METOP-B | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a0e0c1e-64e2-3adc-b67a-c7b00f1add3d | -3.5689 | -59.368099 | 2026-09-05 00:08:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c579947c-5c98-3cb9-8b7d-06d99a825b0b | -17.518101 | -50.041401 | 2026-09-05 00:08:00 | METOP-B | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcbb81d8-af9d-39b2-b0cf-786f71e0ab36 | -4.2836 | -54.755299 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87e8940-206c-3d28-919b-7bc66c0efb40 | -4.3627 | -47.7635 | 2026-09-05 00:08:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7a5aa7-2fc5-33bf-9b7d-d17327974471 | -4.3661 | -47.7784 | 2026-09-05 00:08:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904c5ad4-9ed1-3618-b8b6-fbe1eaa52efd | -1.8335 | -47.922199 | 2026-09-05 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0574b5f2-a6ca-3a5d-8a44-e788032ea145 | -12.9273 | -42.427799 | 2026-09-05 00:08:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5a0babf1-f4fd-3659-9a90-b88d365fd2f9 | -5.6142 | -45.242298 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41d5b80e-8f43-3ae2-bb8d-fae1eca28e34 | -3.7926 | -55.8745 | 2026-09-05 00:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a45ffde-d9cc-38e0-8609-e669047728d9 | -1.1877 | -53.808701 | 2026-09-05 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1fe69e3-35a3-3d4e-b0dc-a5a640d46c5d | -19.7484 | -46.6884 | 2026-09-05 00:08:00 | METOP-B | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0db272d-36e7-3b90-b29e-9e1f12384370 | -2.8058 | -48.6632 | 2026-09-05 00:08:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd3ada35-26d5-3bfa-b22f-ca630a0dffe9 | -6.3535 | -46.114601 | 2026-09-05 00:08:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0551c3d3-7975-3a04-a726-e5f0201a1167 | -19.8326 | -42.696098 | 2026-09-05 00:08:00 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07137159-40ba-3277-97ac-9695d8e45548 | -3.1329 | -60.618198 | 2026-09-05 00:08:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcccdab4-c651-3d00-aa87-3b862b7db1d3 | -13.4321 | -43.830601 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1486179a-41f8-33ab-a112-a5cffdc95e07 | -17.519699 | -40.258099 | 2026-09-05 00:08:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d9121ea-d3e1-38b3-ab7b-75c60d612a33 | -17.296301 | -43.342701 | 2026-09-05 00:08:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc20017-ddba-354f-92fc-dbd6d82ef333 | -5.4928 | -45.119701 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 486bfd3b-9243-36c5-9c7b-6bd008914879 | -3.6913 | -51.9935 | 2026-09-05 00:08:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce039b8b-a315-3122-b68e-a2a1d9af864c | -4.2738 | -54.7575 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8a32d2-da0d-3358-bad8-4710cfda7c0b | -5.8523 | -52.047699 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb84205-1bed-3970-bcc3-c7c98ffc340b | -6.3515 | -46.1063 | 2026-09-05 00:08:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ca78d6b-b3ac-3f7a-9b89-313ca51c23d4 | -2.7783 | -47.773998 | 2026-09-05 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a211cb-ed21-35ab-80b8-4faf13137bcc | -1.1798 | -53.819401 | 2026-09-05 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569750e9-edb9-3459-9ef2-dd1da01f516e | -21.578501 | -48.641602 | 2026-09-05 00:08:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 34fdd27b-8824-3262-a096-f63e9eae1355 | -12.9175 | -42.430302 | 2026-09-05 00:08:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d48145ff-a6eb-3ffe-a9bf-aa6b7972078e | -5.7708 | -45.075199 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8b9494e-0503-33c5-8b61-8d14bf7af8b0 | -4.6682 | -55.6231 | 2026-09-05 00:08:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4246ea2-2b78-3910-b932-1bac84aebe19 | -2.7685 | -47.776199 | 2026-09-05 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2346e5-f24a-3914-98e2-06402c263175 | -15.0815 | -52.534401 | 2026-09-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53e335e8-5b40-37c7-b250-f7022c309f55 | -3.2257 | -48.6064 | 2026-09-05 00:08:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eca1ee8-0346-3e98-9a6e-c268e55e93d8 | -19.250999 | -46.8606 | 2026-09-05 00:08:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 12ecc41d-d578-3440-8ed2-5b92e6fa6460 | 0.1796 | -51.447399 | 2026-09-05 00:08:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 09d55241-d4a4-3f06-8d9a-d27dc14f199d | -4.6779 | -55.620998 | 2026-09-05 00:08:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4322b01-a206-3146-9152-62415bb3bff4 | -6.5542 | -44.768902 | 2026-09-05 00:08:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 470325e1-0e88-31e2-bf2d-1dcf6edcd9fb | -17.5163 | -50.032799 | 2026-09-05 00:08:00 | METOP-B | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9e3be9-2372-31b7-805d-052e1d80d8a9 | -20.9865 | -45.803902 | 2026-09-05 00:08:00 | METOP-B | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5e49d269-1844-39f5-9731-86c70fdd2150 | -17.0933 | -56.781799 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a546131b-9001-3871-8475-2abff08d44cf | 2.3756 | -50.759102 | 2026-09-05 00:08:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef3680e-e3d7-35a3-b626-b264b456ad7a | -17.0972 | -56.804401 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7332a21-ec1a-377f-bd0a-ce85eff8a58e | -19.8195 | -49.602001 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93e2f768-e428-3234-a108-9f6b815e2b9e | -18.122601 | -51.755699 | 2026-09-05 00:08:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3e1f6bd-8e59-3ab3-a60e-a65824c51838 | -5.9732 | -43.6189 | 2026-09-05 00:08:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e13576e3-2b06-3358-91fa-552be195fae8 | -13.4118 | -41.876499 | 2026-09-05 00:08:00 | METOP-B | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e96546fb-65de-3344-bc84-43484ff050e5 | -3.2274 | -50.569199 | 2026-09-05 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2b9d2e4-6c75-33af-9669-5256a5405fda | -17.506599 | -40.247799 | 2026-09-05 00:08:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d81350db-5198-3ea0-831c-98a7220c1d6c | -3.6237 | -54.598202 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf93638b-0a91-34c7-92ac-6cf4665171fe | -11.5348 | -44.889599 | 2026-09-05 00:08:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6027313a-6bdf-392e-9fc1-2f0ac655aa31 | -4.1529 | -49.695301 | 2026-09-05 00:08:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f99aff7d-9163-3a59-b974-9226e6088d98 | -20.243601 | -51.212502 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c97be21-1e11-3369-97bb-8afc2ef040ff | -17.51 | -40.260799 | 2026-09-05 00:08:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbf98020-5747-3317-b37e-3952e28596e2 | -17.0991 | -56.757702 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5623b473-b799-31e9-a8d3-50497b1010ac | -5.9163 | -47.886799 | 2026-09-05 00:08:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb7e4e5b-0900-3e2b-8da6-2e6cfe310700 | -13.5568 | -44.093399 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf14f6c-f662-3e9e-9713-c83e94482615 | -15.0696 | -52.525398 | 2026-09-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03f75e99-a5fe-3510-8ce2-4dccccf35d28 | -15.0793 | -52.523399 | 2026-09-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45e72fa7-96eb-3610-828f-896e5f275b84 | -5.4906 | -45.1101 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1475532c-5c25-3b44-89ca-0427c1f35a45 | 2.3725 | -50.7728 | 2026-09-05 00:08:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f6a9d4b7-8ffe-34aa-bfaa-1d91a58e8c86 | -9.12 | -44.281601 | 2026-09-05 00:08:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
