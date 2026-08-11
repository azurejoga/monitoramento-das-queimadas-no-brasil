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
| 378038e3-99c7-3b19-ab49-62558ae1ac2d | -9.47685 | -60.53814 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee6bc634-5b70-3597-ab66-4f8ab3af23cc | -13.56559 | -46.27766 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 1df40646-1f81-3934-862b-05489f999290 | -10.41504 | -46.68718 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70569ecf-cd75-3c5c-b189-69a30ade3a71 | -11.95885 | -46.34134 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec8f207e-6e2d-3445-a166-036e73f2c3fc | -10.11309 | -46.20425 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72cf5055-ced2-3c69-a75d-e6116978cbea | -13.0795 | -43.06183 | 2026-08-11 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d3ef431-11f4-3cbd-8b66-f1245f391dfd | -9.47452 | -60.51656 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ae07493-cce1-321c-8c03-858c6548b915 | -13.60859 | -46.32126 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81b26f67-2083-368e-a27e-4335a3017cc8 | -12.45893 | -45.33923 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ea4bc5a-2781-3272-a807-5bbb0612fa29 | -6.71411 | -58.94043 | 2026-08-11 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c7ccd4-ee1d-36d8-a9f3-7b2f13ebf39d | -8.9024 | -60.58094 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e80a64fa-ab32-36d9-a80e-17c8ad3db828 | -7.5933 | -42.76226 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e6a883b-4f12-3c66-8b79-5fb8f21de867 | -10.88642 | -50.36984 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24ac5859-4c7a-3e94-b759-5da224e68bd2 | -8.305 | -46.39117 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f261e2ad-3f45-350c-8c70-97bad10291db | -11.64474 | -51.65322 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 718428dd-5e09-3c78-9f18-d41532b0b578 | -11.02566 | -45.652 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855b971b-8a40-30ee-b6f4-44ed1bf6d8a7 | -12.23942 | -47.30228 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce6e5207-a8d8-34ad-a524-c1ce15c11363 | -12.49116 | -45.30135 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec57d591-30d9-3d53-a784-96f500f596da | -10.86799 | -50.24771 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9377a1c-d8c9-3d1f-a009-d904df5288f7 | -11.96239 | -46.34201 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a88073cc-fedd-3133-a1a0-11dcf03ee3b0 | -8.23639 | -46.24266 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2325939-d756-302e-b82b-77049c948621 | -8.90335 | -60.57584 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2649bd08-9494-3710-ad80-0078a423faec | -13.64903 | -46.24485 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcc95a8f-535a-39d6-9023-3d94a489214a | -7.39196 | -42.86728 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67da3af5-9d3a-391c-9c58-cfebef5e3f54 | -11.98657 | -45.80304 | 2026-08-11 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d4aab4e-fa2f-329f-a9bd-4bb914755260 | -9.3884 | -47.44721 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbe8050c-7716-3b4d-9af0-0a9604ca3b2b | -10.43166 | -46.67023 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 395995bb-f341-3761-83d7-a4e6b0dd23ff | -10.9382 | -57.11298 | 2026-08-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6189a6cd-49c2-362a-a5d4-cf3d3c10e19b | -7.59898 | -42.782 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0a8f7681-3057-3dc1-890d-6d7bf97f607c | -8.94152 | -60.5253 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b2959d0-ab69-3597-8ef9-78d92cffe6f6 | -8.29873 | -46.38628 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb8f9209-3428-3949-a228-ff0e279b07cd | -13.57645 | -46.27931 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4deb73d7-c841-3bcd-99a8-f7671d6f2aef | -7.62169 | -45.95043 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebc7307e-ac84-3d9d-ad05-9da2e1fbe8a8 | -13.57452 | -46.31816 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb0f21cc-3ac9-35ff-86df-1820dd196495 | -7.64174 | -44.38354 | 2026-08-11 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 858c4758-789b-3109-b365-8e4545159bb9 | -11.46232 | -44.55904 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cf8cbb6-e2d6-3e65-815b-3989af2489e8 | -8.30214 | -46.38689 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b440572-9ce2-39a2-a742-18b80a53f91d | -12.47968 | -45.3282 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 778254fb-f797-3fd7-a27d-f75fa1f64d5d | -11.49303 | -54.60827 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8a5156-3d97-3801-a682-ac6ed89f0faa | -8.2404 | -46.23943 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 342c868b-69b4-34ac-9977-5ece6370fcb8 | -8.4989 | -45.40983 | 2026-08-11 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e6a7505-29ea-3b52-96c0-49f874e4a140 | -10.58259 | -44.77761 | 2026-08-11 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5566e87b-075a-3277-919c-e8905e8c023c | -11.2397 | -54.87855 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7fbfc9d-707a-3c38-9348-99749bec5270 | -7.38839 | -42.86297 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 529ce2fa-24bf-3e2a-a8f1-51989bf8a592 | -9.3961 | -45.49941 | 2026-08-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c2e9c36-1746-3b8d-bde8-2b1d04bb6ab0 | -10.4951 | -50.29862 | 2026-08-11 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6b14468-1d11-3cae-a449-15c583a71553 | -7.39092 | -42.87467 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa22d512-9611-3873-a9b4-bfb1adfa50d5 | -13.65146 | -46.25381 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bfd03088-5f5a-334a-ac6c-878c9df061ce | -9.46826 | -60.51537 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9fb850-fd99-3822-bd29-ff42bb2db054 | -13.56674 | -46.29528 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4cfb0402-7e4b-369b-b2c0-daccec69f770 | -8.89411 | -60.5901 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 52b81518-72ef-3657-bc21-14fc39d1a435 | -11.48042 | -46.61806 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dacf26e2-395d-355c-a328-7a77eedf4184 | -11.95671 | -46.33453 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56d36047-5d92-3249-8522-fda38e1272fe | -10.11079 | -46.19566 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ed13f6-117e-345b-8dc6-205ec84b7e42 | -8.54769 | -45.34378 | 2026-08-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3ea8558-847b-364f-be10-59b5083d99c5 | -11.02138 | -45.65595 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 081a5bc4-0e2c-3bfb-ab2a-0ccae954e42c | -10.7364 | -50.4535 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 809e403d-5f6c-37a0-a3cd-880f59d43ced | -6.52409 | -45.67344 | 2026-08-11 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a59ae1b5-b41d-3386-805a-5e82210e5c69 | -11.49065 | -54.60814 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e55fd7-7f24-3149-a3ad-69eb3eafcd77 | -13.59594 | -46.24707 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2085c50-ea0d-329c-8f80-4bc72f5f8acf | -11.22619 | -54.85609 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a24bd782-f1d5-392d-9164-53d2166c89da | -10.43336 | -46.65881 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b40992f1-783c-3aaa-8b9e-d311d621078b | -11.96833 | -46.35113 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 800986a2-8d1c-3d59-bf6c-71eea3edfa28 | -12.48034 | -45.32356 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 089ab078-ff34-32d4-8f13-9b04e2f10398 | -10.07227 | -60.5004 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac7b879a-4249-301c-ba1d-aa570b5497b4 | -10.50429 | -46.60275 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e264ff7b-b99e-3749-879a-1722a151dc1c | -8.66544 | -54.95592 | 2026-08-11 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8eb4dd33-0cc0-35e7-a70f-f47d79f3d585 | -8.56084 | -45.35417 | 2026-08-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87ad9928-3731-3b84-ad9e-30a7aec2a38a | -12.50069 | -45.28841 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8266972c-db58-3a42-924a-73c1e3a024bd | -8.89241 | -60.57546 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b091fa50-33ee-3c71-9fab-b20fad156c31 | -8.23926 | -46.24696 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1fa6a5b-4d15-37a4-a582-bb95a9f4e903 | -11.9713 | -46.35566 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 702e52c6-9ba4-3dee-a7e7-7af902e60df2 | -13.48588 | -43.07343 | 2026-08-11 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7aa5331-9ccc-37f4-966f-6adf9bd6c62a | -6.31033 | -51.12756 | 2026-08-11 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45466473-062b-3408-849d-ccf933260f2c | -9.46958 | -60.54206 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4367ce34-897a-38c0-87d7-243dba121779 | -11.46553 | -44.56458 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab25b683-31ee-3ee2-a21b-958d5fcc59c2 | -8.89341 | -60.57032 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43ffa3b9-88ca-39f4-9243-8c45cc9b6f1c | -10.72675 | -47.9142 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06b6fd41-1f84-353a-b3a8-62550682953b | -13.57044 | -46.26967 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fee5b6db-2ef4-3b28-9b56-9215fe4347e8 | -8.95362 | -60.56496 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 25e101ac-e578-3b99-86d5-7909217778ae | -12.45647 | -45.32935 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e7b879-6398-3e40-96f2-25343b254dd2 | -13.51578 | -44.13713 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e309fc87-59dd-3c76-a785-0f8a01c63f45 | -6.83996 | -56.42625 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52b3544e-e313-3f31-a2e4-dd75daee49fc | -13.4357 | -48.27658 | 2026-08-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c609ffbb-0ab7-3c1c-85c6-fd31b7f8f352 | -8.89799 | -60.56939 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4c87626-6641-3143-8ee9-532986b8709f | -10.93713 | -57.10951 | 2026-08-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d632323-e6d9-3db8-ae84-d637e97c8fe5 | -7.38793 | -45.11641 | 2026-08-11 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f051eac0-96f7-3439-bbb9-0828495bb44c | -11.24892 | -54.82713 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b286ecd4-032c-3907-bde0-4426b772f561 | -6.84308 | -56.40875 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c4a175-8c7b-3387-8d64-b16fbd309c5f | -11.32259 | -45.22593 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 969b7ef8-e117-3d20-b28d-20b57174fa84 | -8.89974 | -60.57159 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20235fb8-0cf8-3b77-95ae-69e720becdac | -10.87135 | -50.24826 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577b8a71-5cce-3175-b64a-abaff9f1b010 | -6.84657 | -56.41833 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9e973c6-2a20-35f3-8c1c-553e430f8052 | -13.57098 | -46.29158 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b64f0fb-aba2-3121-8eb2-f9d113792c79 | -13.5837 | -46.28035 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12874161-7609-37c9-8bfc-da51b7b5032c | -9.39399 | -47.45543 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d26c53f-1d35-35d5-8eae-fbf6103c23b0 | -11.95643 | -46.333 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f0fc1748-03a9-3054-b238-e8ffdd4a788f | -10.87471 | -50.24881 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f5351ee-8195-3aa8-b93f-2ecccb908671 | -10.23647 | -45.86033 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12ef948a-c0d4-3794-a09f-a9f0ff90d60b | -6.46487 | -47.84259 | 2026-08-11 04:34:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
