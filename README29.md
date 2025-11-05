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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9d16987-6b12-38db-a46f-88d291de3b0b | -3.53837 | -55.42025 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e71bfef2-f2c0-3a6c-989d-36a289339e59 | -3.89802 | -51.24389 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617321e1-bcae-3783-a9df-79836207d948 | -2.26792 | -47.85304 | 2025-11-05 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2f627e7-782e-3121-a5c4-00432c078eb8 | -4.2494 | -48.56079 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e78e5f63-f917-39b6-8b36-cdc6893b5f58 | -3.49214 | -43.62009 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbff41bc-b037-3a05-954b-16179ebb8794 | -3.23089 | -43.43425 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6040e75-98d3-3ab1-9e49-d2b30d9414a7 | -4.15325 | -46.79351 | 2025-11-05 05:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbeeff5a-a3de-3089-9c54-847322616061 | -5.24506 | -45.73964 | 2025-11-05 05:01:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb4133db-c0fe-3490-ace8-1b1a904813d0 | -2.9616 | -48.5961 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15cc593e-3a72-33ce-ba29-918c0d496c54 | -4.29605 | -43.78785 | 2025-11-05 05:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 893fa309-fda8-39b4-87fd-b9f5f6717d57 | -3.40886 | -50.84041 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7722582-62bb-3d50-bb6c-85513bacccdf | -2.73263 | -47.38541 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 082803a1-4dfc-3f0a-931c-8a40d2a86dc3 | -2.65514 | -48.50663 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5a18c049-93d3-3bdf-a2ee-c1e682ce29a7 | -2.88919 | -51.01438 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d9f7b4-1897-3c04-b812-d6ecfbdc133c | -4.4586 | -43.2223 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ea58b7e8-4359-37d0-9b55-1348c4f66517 | -4.48158 | -45.98352 | 2025-11-05 05:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e9d4a1e-0cd0-3bed-93a0-c8f8d8942b42 | -2.9294 | -51.31012 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81efd1d0-d6eb-3d12-b5f6-f3414c218b3b | -3.24122 | -52.92135 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c1fe759-1c59-32d3-8a4f-e1f5d0c7819e | -3.81698 | -51.28841 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0e233618-c1c9-3805-85fc-d33145b75758 | -2.42372 | -49.30242 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60df4c41-c78a-36e3-8547-7a34f8e63536 | -4.17722 | -55.59894 | 2025-11-05 05:01:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a744ba-70cb-308e-8ca4-98bf2ad53e0f | -1.28903 | -49.14843 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 438baaf5-533c-3574-9215-2cf33d7e61b3 | -3.41554 | -44.4426 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1ddc75d-a2af-3aa6-98d5-ec71bb26a35d | -1.27264 | -49.14588 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d46310d-4357-3243-bc30-b8d0168cfbe3 | -3.84549 | -49.90746 | 2025-11-05 05:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0aa8a27-2bf0-3e92-8ccd-9c8b09ac3a92 | -4.45429 | -43.22094 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f608b5ee-6e16-343f-8e4f-a2a05d66c262 | -3.78997 | -51.31601 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ea05c4b-61e4-3059-8b1a-86071fbaf38e | -3.22945 | -43.4441 | 2025-11-05 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 430a25f4-fc50-3c43-b296-e48651775a74 | -2.63766 | -48.5039 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88f29389-6f24-3ded-97a3-39dfd2834151 | -2.73188 | -47.39041 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e65386b-752b-3d73-a65c-cbdba88fd730 | -4.28689 | -47.17638 | 2025-11-05 05:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5dbfddc-a83f-330b-b17f-d746376008a5 | -2.83507 | -49.41972 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99bc9ea6-576d-3e10-8577-0c045daa322e | -2.38223 | -53.97808 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f2b79e8-8834-3035-9677-85365afb73a5 | -3.31265 | -53.83712 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 336f4f0d-a423-3815-948b-50d569e33c69 | -2.27696 | -55.972 | 2025-11-05 05:01:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0cc6357-e651-3c84-bfa1-1f37545969ec | -3.16906 | -49.2343 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a7b578-f44a-3169-a09f-fe0639faf7c8 | -2.82016 | -54.35733 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad403b90-d6ec-30f6-81ca-8692ae669d72 | -2.82037 | -45.14866 | 2025-11-05 05:01:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7166a2ab-0049-3050-b0cd-d824b644eeca | -5.45659 | -45.40469 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 100646c6-2933-3a81-bca2-41de05ec5acb | -2.89137 | -54.85743 | 2025-11-05 05:01:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dcb5a57-6230-3664-8c2a-62ca8ee423cc | -3.85965 | -49.36779 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c11a7da-7548-38c2-a3be-aa4e333a8ba8 | -4.46634 | -43.22824 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f63bc880-31da-3fc3-8863-133b93fddba9 | -2.96597 | -48.59676 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e699ed58-7f0d-3b7c-ba5f-0469a5d0d220 | -4.66166 | -44.52689 | 2025-11-05 05:01:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abd0f7e0-bd18-31bd-b846-516e6ce5951c | -5.03991 | -43.62349 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 03499d49-1d65-3bb1-800a-d043c34a7959 | -2.63934 | -54.57521 | 2025-11-05 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2101229-0f34-3600-9570-cfac7d651082 | -3.10791 | -51.0297 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a51ac3e-3d80-3f04-8eaa-b11e2dd16ee8 | -3.31434 | -53.84816 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863843aa-2c6b-3ef1-8b69-2d6e30341173 | -3.50432 | -54.37615 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336599ab-7b86-3913-9626-e58153771b77 | -4.30169 | -43.78949 | 2025-11-05 05:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eeac4737-9c48-3dad-a4aa-582fce984a36 | -2.98348 | -51.3474 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3550c75d-f40f-3898-b9aa-abdca22c030a | -5.03807 | -43.61768 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a1d37a7c-82a5-3af0-b6cd-d5b981bb1e15 | -3.70564 | -45.89172 | 2025-11-05 05:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 46e2fc7b-6bac-3580-8715-f6adcb1164c6 | -4.10033 | -47.2853 | 2025-11-05 05:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e4bad8be-dc69-3117-bcaa-8d70edf77748 | -3.22489 | -44.40625 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d9ce121-18b5-398b-9c87-8ac229abaf28 | -3.27209 | -53.26648 | 2025-11-05 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9534da1-c510-35a9-97ae-edaaf60c6a66 | -3.22551 | -44.40209 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee78481-e469-3120-95ec-5d7e558c50ae | -3.31489 | -53.84465 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae9dd01e-091e-3af8-a8f6-62923edbd2b8 | -3.36815 | -44.24414 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b87b381e-3d03-3962-8120-d29b2f04f1aa | -5.03673 | -43.62771 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| cdb38bac-0931-30c0-86cb-0a810c1c2267 | -5.45148 | -45.40018 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 833d70e5-5263-3f59-8b67-d33fe180ea1a | -1.30075 | -49.154 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f986c05e-0d67-3b4d-864e-06e3b0e3ef9e | -3.82214 | -52.3597 | 2025-11-05 05:01:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9080ed1f-93f9-39e1-8ffe-b6c87405ea03 | -5.06272 | -45.47424 | 2025-11-05 05:01:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959d0009-e5b1-37c4-9f69-57369ceb403f | -3.96365 | -43.78623 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 480f8f18-2e9f-3723-8f73-8f4bdb61587e | -4.55226 | -46.75989 | 2025-11-05 05:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0525d26e-d9a7-3353-8cef-ed3fd0ca9de3 | -5.45714 | -45.40089 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 295db26b-2f52-328b-b2cd-d8504c614770 | -5.0392 | -43.62851 | 2025-11-05 05:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4ca0fac2-8c86-36f6-a7d9-7c4931958685 | -3.31712 | -53.85218 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fb0de8-19b4-3474-a5f2-5eb4261b20e7 | -4.11095 | -48.02241 | 2025-11-05 05:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 26520342-1b2f-3a79-9a0c-fdd955987de9 | 3.1438 | -60.72198 | 2025-11-05 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4425ddd-89cb-3298-a7f1-a65bed9cccaf | -3.50261 | -51.55449 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c059e5f-f9c5-3e85-a14c-15ba45df64d4 | -3.92741 | -53.84211 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318b926d-6cc7-376c-b143-1ac5b2e18afa | -4.46562 | -43.23353 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1ef49bbb-590b-3d36-ba06-ae01e1672fb0 | -4.58766 | -43.33681 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 987df06f-741a-38c1-b453-bce8fe3b0eff | -4.21782 | -48.35223 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67e275cd-5a1b-32dc-95ac-8aa4831277dc | -3.77496 | -53.42061 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c09f39d-9504-39ba-8f5a-1f3d6bd7a398 | -4.18052 | -55.59946 | 2025-11-05 05:01:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c4b82d-bd52-3337-a1cd-d1fb4fa9d863 | -2.87977 | -49.59501 | 2025-11-05 05:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90c7a305-232b-3c48-b787-72661da179a0 | -3.11095 | -51.03475 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2a0b58-7743-3a93-9ce5-255f9fbdbdd0 | -5.45093 | -45.404 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7e8a360-9a09-3bd9-a46b-817e7701d442 | -3.31379 | -53.85166 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fefdd46a-42ec-3bef-9a11-cc6b68800f94 | -3.69631 | -49.56548 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 957f6f09-856e-3d85-8cc1-1ddee322dc12 | -2.83096 | -49.41906 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a905334-f5bd-329d-b6c3-9b564cff7e49 | -5.45981 | -45.40639 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9d5a283d-eb16-3336-b2e9-6ce8dd13d72d | -2.48601 | -55.72702 | 2025-11-05 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d753f411-1f71-35e4-99c1-c706653f5f42 | -4.41022 | -48.94304 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d694efe8-febf-3902-aea6-c763c9b018cf | -3.0218 | -51.09394 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96803036-cfe8-375c-997d-0cd3239da143 | -3.06865 | -47.77927 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 357b0cc2-a31c-3d49-a10a-207892cb3ec6 | -2.48268 | -55.7265 | 2025-11-05 05:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d01f1bf-2df1-3784-8ac4-333fe28e115e | -5.47456 | -43.57919 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4b5b9a1c-c4b1-3ffc-9978-c1da0bb03c3e | -3.91059 | -54.71543 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c55279-33d8-30bb-bbd3-a476e4094088 | -3.90775 | -54.69033 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eae4c5e9-09da-3fee-960b-6c39f0102a4b | -3.50486 | -54.3727 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa68d4f-d3ab-3961-800d-f303a2ee5278 | -5.45518 | -45.39814 | 2025-11-05 05:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 92c4e39c-2a03-3893-bf55-b3de6e7742c9 | -3.54958 | -54.71863 | 2025-11-05 05:01:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be770f5c-74d7-32e9-8f43-f41cb0bb1a25 | -4.71871 | -49.77038 | 2025-11-05 05:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edfff0b9-15d5-3ad9-aa3d-1af71c5d4bea | -5.46754 | -43.58337 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7534690f-62b7-3158-8b8a-db54c90191bb | -2.68774 | -48.46835 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac9e0185-1555-3c91-98fc-7d33d928a5b3 | 0.25883 | -50.95758 | 2025-11-05 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README30.md)
