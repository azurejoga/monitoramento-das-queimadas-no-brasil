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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e9ad887-3646-33b4-ab5c-1aaf38864272 | -7.23842 | -44.16766 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df2902ad-76ae-3874-b8e0-5d87f8ee2e7f | -3.21962 | -50.55634 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab753cf0-b3c8-3dc4-a311-51331d9c02d3 | -3.24263 | -54.02708 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60d11335-c638-339d-832c-e1d3162a4ec5 | -3.25842 | -50.39333 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6a58c1-ea69-3df2-ae40-de896410b5b8 | -6.64908 | -55.33693 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 064f36e7-cac0-3cf5-aab4-735983e7390b | -3.40583 | -54.1847 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2e863bf6-f01c-3ef6-82b8-aab1d7c2a924 | -7.06378 | -40.96053 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f589a35c-fe33-32d1-a0a7-bbd12628d179 | -5.89504 | -43.27364 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca5e7853-1395-38c1-a2ff-e782b35abc1c | -6.41683 | -51.95543 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd830999-72f0-32c3-88aa-2125c1d6d81f | -4.41067 | -49.78236 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39df40f4-a9bb-3851-8d08-8cfb37b6db6b | -3.2038 | -50.55022 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dcb7e9f-9ab8-3301-a00d-4f17f67d4e53 | -3.00956 | -51.00399 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6c46efd-41cd-367d-b3cf-91ee809d6eb7 | -8.36163 | -48.13998 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18600c57-9347-3175-bdf7-07e3f7ced771 | -7.07462 | -41.59552 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 26d3be56-23a1-3666-88b5-e69aaafd081f | -5.59547 | -47.27568 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd83ce57-d1b8-3981-a0c7-48514fcc4f58 | -4.63742 | -50.95974 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ad2f422-bfd1-3d18-96dc-8b016078b3b9 | -9.30617 | -47.40515 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 727141e6-0cee-3f99-8300-fd80397bcc72 | -6.70261 | -47.38576 | 2026-10-10 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c3b4630-3158-361d-8e03-e7b221b3a962 | -5.95205 | -45.38075 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab0c8cda-03e2-3dc6-93ee-d2cda3f64ae3 | -5.62505 | -43.64771 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab1ce867-0ac7-3683-bcd0-944beb368614 | -2.00098 | -47.95515 | 2026-10-10 04:08:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 808a6b18-29c0-3c37-9ef9-af867a36399a | -4.39783 | -49.77588 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5597095e-8e20-381d-8ff4-7d4c8c4f5cc2 | -9.01258 | -44.36736 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c78d87a5-c507-3753-930e-6096467ab24e | -6.91302 | -45.87335 | 2026-10-10 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d2b2f8e-fe08-3780-a3f6-02040ee92d67 | -6.45136 | -55.2897 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41d3505c-d386-3b17-938d-d89404fe3285 | -6.82984 | -39.56428 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f889b73-d5c0-366a-8071-73cc0c07a6f1 | -3.26246 | -54.69346 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37fc3825-571f-37a6-836f-33f60aced09e | -7.71394 | -43.96479 | 2026-10-10 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f46e9ef-4ddf-3502-8b82-6bc50ff67d78 | -3.56837 | -54.68544 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 612c442d-2fe3-3bf5-a4a7-76494729a46b | -3.10285 | -53.78587 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f728c0de-13a1-3422-829b-b3a1c59e2a3a | -5.11656 | -46.22829 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c9dfe7c-e7a2-3db5-9227-9ac4b23a1953 | -5.45598 | -44.78154 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76990609-d49b-3bd8-a5dd-42b954e2f67f | -4.89124 | -49.05156 | 2026-10-10 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6eb6cbd5-eeaf-3078-b8b8-e78fdbca7e86 | -6.43938 | -55.04541 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 847da2ee-f460-3997-bb79-e92ebf1c6ea8 | -9.46638 | -44.60322 | 2026-10-10 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1f6643b-6de1-3b45-840e-2cf129674cbe | -9.26926 | -47.42786 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 546dd7c4-a2aa-3161-bb70-621eb4135825 | -5.24914 | -42.2336 | 2026-10-10 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 092c5bc9-1397-3f15-8768-e2bbfcb46009 | -2.72954 | -54.15257 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 800e72e0-aac1-3787-a8bd-a5f97e5cb25f | -7.29152 | -44.01306 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2e9442-15c6-369d-bceb-2c04ced1217f | -6.01222 | -40.96452 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 840a066c-ee2e-339e-bbd3-6f25fa54441e | -6.44444 | -55.28819 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f46d80b4-82b3-3f96-8bc7-ee4a7b2198ae | -3.4682 | -50.59356 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6346d1d-96db-3f82-91c9-9dcb2b688d2d | -6.21145 | -45.42873 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91f77f07-618d-30cf-b6ce-f1bece066de7 | -3.23448 | -50.18803 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebd36b1f-61f2-30f3-9277-d623a75fc650 | -4.40443 | -49.76763 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 69adcda8-6f8f-3cb7-aabc-45114603a0ce | -5.95711 | -40.92399 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d3e3492-e235-35b9-af03-9716c14ad60c | -3.24952 | -50.41311 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3afc140e-363b-3d3a-8aea-c303e618528f | -8.79918 | -47.57981 | 2026-10-10 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0849d865-72bc-3bec-8b1a-f4c9b2aa533e | -6.06872 | -44.66492 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69398fc8-4062-3a18-afa3-0b04891c69e7 | -6.46554 | -55.51644 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24a878cd-d827-361d-b3d6-1e8fbe23b03d | -9.21532 | -45.65119 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e94c0f9-efc0-3c62-8696-b293e88f6892 | -6.41918 | -51.95472 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 035bc0dd-3aaa-30d4-86ef-3cda041840a3 | -6.99874 | -47.71735 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2fe01fb2-1c2f-304e-b550-0f2f636bce9d | -6.498 | -44.36558 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6736010e-8e48-33be-bfd9-333f5c254740 | -3.24148 | -54.03354 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 500a47b7-dbae-3f75-867d-251089e1200d | -8.21283 | -45.79005 | 2026-10-10 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b9a1650-756e-312f-ad7f-ebb8d9810dbf | -5.55698 | -43.96461 | 2026-10-10 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65bfe645-367e-35ba-8dc8-5590717c4749 | -7.05767 | -40.95596 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02ed46a6-9322-3f55-bee6-e033af474c57 | -2.74657 | -48.42872 | 2026-10-10 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b645ea-73cb-3461-82d4-4b2198fe1144 | -7.97172 | -46.88471 | 2026-10-10 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af92c293-51ac-3e91-942c-a471d65cef1b | -7.28809 | -44.01252 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53fe76ef-3e0f-39f3-8b1d-301886529d3e | -6.41075 | -43.74333 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7432ab8-1746-3e7f-b7a6-d54634e55ca8 | -2.19528 | -46.83626 | 2026-10-10 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05a15674-83cc-3d5a-bb62-a85240aa1105 | -1.73977 | -52.24149 | 2026-10-10 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a6905a9-613c-3292-b827-9c9c42f4abe3 | -4.26292 | -43.95516 | 2026-10-10 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15a30ca2-b81f-373a-8cc4-ec94b3fab3fe | -6.50151 | -44.3661 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65c948a9-47ee-3363-889f-c4bbe4fb3b31 | -3.57814 | -54.70153 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a77374fa-a7ef-3842-9c2c-419eb8e31540 | -4.43244 | -47.53605 | 2026-10-10 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| c0cfe2c3-b0aa-3045-a2d9-ff6c871dc266 | -5.11297 | -46.21951 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bd332f1-3afc-372a-bced-48fd5b33175e | -3.43748 | -54.53564 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5653ea8f-d49f-3f5d-a948-d09836c5df0c | -3.39146 | -44.03033 | 2026-10-10 04:08:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76e64618-f0eb-3f93-b8b5-c3964ee5dc8d | -6.46616 | -55.05738 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 473bbc66-8048-3ec2-bd27-50a08dc33b0f | -9.46576 | -44.607 | 2026-10-10 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eff3774-fa66-37d6-a750-ba43e80c71c4 | -5.62103 | -43.65092 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7927e6a-8304-35c3-90e1-252f6f877416 | -7.06971 | -41.6054 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 126d272b-8771-38ab-be60-8520ed4ae6e1 | -3.11818 | -54.16273 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cad95fe5-077e-3726-b3d6-9fab7634d2ac | -8.77142 | -49.6051 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69b78464-d1f1-319c-aba7-eedf45521c87 | -8.89728 | -51.71258 | 2026-10-10 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c37b840c-7eee-362a-bc5e-e33f9a7b3ae4 | -7.53921 | -45.31561 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b1779b1f-bc6c-3f4c-9a08-ce5666555884 | -9.02872 | -44.35467 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0170a7dd-25c8-374c-961f-589c063ba006 | -3.96047 | -51.89336 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e8d07e7-8cb6-302b-8db8-390a6c0c6f2e | -6.7759 | -48.66927 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1685e922-a988-3a9a-b002-16122cd408c5 | -3.21731 | -49.44744 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644c1fe3-f81a-30d7-9742-00af5e357ba4 | -7.16613 | -41.98803 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e98a2f2-9f03-3386-8476-4ba9f317a01b | -5.7068 | -53.4833 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 27e4802b-fbfe-39cc-961d-acbbc9f9adf0 | -3.24774 | -50.42356 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e3f3e02-9724-38d0-8b5a-64dd7701cb67 | -3.11647 | -54.1763 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 927cdf02-a10f-3849-b6a2-ea3e8595d60b | -5.45661 | -44.7852 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3770240c-9593-3a05-999f-21aef5969c9f | -7.53196 | -45.31441 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3e4ca22f-7978-3007-a0be-34c6db978a06 | -7.4964 | -55.00363 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 93589632-6b96-333c-b60a-5aec5bbbb80f | -2.39988 | -51.30058 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ab4e6ce-cdce-3f49-bf01-5ee6b0fd3159 | -5.29255 | -45.07801 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999ead6c-f65e-356e-b15f-d559ccf79a40 | -3.21535 | -50.5484 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81c2b894-f969-3f5a-9db8-f24cc79a837d | -2.40335 | -45.57768 | 2026-10-10 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3cbd8af-bd5a-3864-9493-e6d59facfffe | -9.26988 | -47.42429 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f9e91ab-7105-3690-b031-17d1a3e6bfcd | -3.03639 | -53.8924 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32cb604b-4992-3767-894d-0cd82408a9ad | -7.92623 | -54.72435 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d98c56e-b706-3df5-a81a-0e84f93d6d8c | -3.98477 | -54.45226 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e827d4ee-1af5-3c60-b381-eec0fda1c992 | -9.29198 | -47.39194 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd862895-1af9-3376-a96b-6356ac11bb27 | -4.40344 | -49.77364 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README39.md)
