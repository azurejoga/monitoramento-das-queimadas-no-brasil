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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2984c687-7867-35a9-837a-dffa442b15e7 | -9.4837 | -57.8241 | 2025-06-21 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a590229d-8bc8-3475-b8e4-96723772e459 | -13.2343 | -49.8475 | 2025-06-21 01:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d76a7fea-ee26-35c5-887f-62b7e72979d3 | -13.2346 | -49.8258 | 2025-06-21 01:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 71319b9e-96f1-3beb-b565-c33d7108c140 | -9.4648 | -57.8449 | 2025-06-21 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8b12a5eb-7ed4-390c-b01f-27d52fa3915f | -11.798 | -57.243 | 2025-06-21 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| ac3ea53e-67ed-3436-ba0c-d7f48c342a46 | -4.5243 | -48.016 | 2025-06-21 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 88aadb06-ba2e-31e0-8acb-dcc2d0def200 | -11.8663 | -54.6739 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 9a0697c5-34db-3a39-bbfc-852133d36735 | -13.24377 | -49.83659 | 2025-06-21 01:20:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 2629c1bd-9497-3e4f-9600-73375a778ec6 | -13.22969 | -49.83926 | 2025-06-21 01:20:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 21367989-5438-3593-af8c-4ebf4cec6b52 | -13.04059 | -53.71558 | 2025-06-21 01:20:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 00042568-3d18-3b80-909e-50f94ba014e8 | -14.86525 | -59.79495 | 2025-06-21 01:20:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dda0078b-d2b8-3bdb-832e-070819996f1e | -12.52719 | -57.20713 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 533f9ec3-4b0f-360a-ade9-72d24b85a4fc | -12.29176 | -50.10386 | 2025-06-21 01:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| a7084f6b-5da9-387e-80f9-cd21b9e660d3 | -13.14333 | -56.81015 | 2025-06-21 01:20:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 356165a8-ab0b-3768-96e4-87bde7b86780 | -13.05104 | -53.71374 | 2025-06-21 01:20:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3dabe349-b675-3589-999a-b5d1d5126179 | -13.29326 | -57.08949 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07f53dde-25a9-380f-a9fc-9fc3e9bc5888 | -13.10256 | -52.29512 | 2025-06-21 01:20:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6c78f6e1-907c-3aef-9451-87f0f5953ecc | -13.24816 | -49.86197 | 2025-06-21 01:20:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3a7d031d-5db8-3d5d-b75b-350141abf147 | -12.57918 | -56.98842 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b991eba-0490-3362-812d-b378f7dbc883 | -12.89211 | -56.98809 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4226376f-a9ae-3456-93dd-cc93cf6db6ee | -12.9749 | -54.6814 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fe1f2647-5250-3aba-b0af-8d3fa11b32ae | -12.97406 | -54.68726 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 56a895a4-7578-3f61-b921-3899e9a8f713 | -16.30016 | -53.83472 | 2025-06-21 01:20:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 58ed92f1-234d-3a37-9b4f-ff0c2ab945f1 | -12.51832 | -57.20846 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9666e95a-18a2-3ca7-860f-da9bbe0baf71 | -12.42781 | -54.86958 | 2025-06-21 01:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6f8a504d-b571-3267-85d9-eeaa9f8f442e | -9.47309 | -57.83881 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 016a38d1-0484-3d08-b081-7f68025a7561 | -11.87416 | -54.66068 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 96f69ba6-9bf3-3712-95a4-33888b8b58af | -11.87775 | -54.68403 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| fd15866c-d8de-397b-bc65-b89009bcdeec | -9.48069 | -57.82851 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5aec6636-8da3-3946-96de-a4451e29d89a | -10.86738 | -53.76348 | 2025-06-21 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| efe4c566-4e57-36d5-8fe4-c4f3ad838c76 | -12.5782 | -58.38012 | 2025-06-21 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2ebc0f50-3a74-3895-8da3-ef4a5c18b2f4 | -11.79375 | -57.23563 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 8dd62263-50f0-3f2b-9bcd-c1975517bcac | -12.51124 | -58.35289 | 2025-06-21 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f56cd311-1db5-3fd2-ac81-eeb5ee0e5581 | -11.86598 | -54.67397 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4b94399d-0d0b-319b-a5ab-782ee091a1ed | -10.88986 | -56.46344 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 78938f7e-cd58-3b7f-9479-fb1717bd89a6 | -12.03083 | -57.09478 | 2025-06-21 01:20:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9c48ba12-4d88-3d01-9bc9-0000335ba5a2 | -11.52576 | -56.97625 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 19486c3c-857e-3068-bd9f-b833bc580847 | -9.25423 | -57.53198 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 82b2b452-02fd-39ce-aec2-88242b67f2bb | -9.47182 | -57.82982 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d3759804-31a4-3396-9b88-7f23e0c2498d | -11.13587 | -53.92519 | 2025-06-21 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 77a6010e-d60e-341e-81d5-3c7e1f7263ae | -10.89125 | -56.47312 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 232d2b2a-3ef6-3551-bde5-1c3d83383c24 | -11.57291 | -54.56351 | 2025-06-21 01:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ee450bce-a2b6-302f-98e1-be2e383c15aa | -9.25293 | -57.52285 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 82c54594-b635-3273-89ef-2b5fd8cb899f | -11.78486 | -57.23696 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b29e437b-28b5-36ac-a582-b03cd75da5e7 | -10.52373 | -53.61946 | 2025-06-21 01:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 15470624-9391-3141-b96c-4e5c7a4b24a6 | -12.51248 | -58.36195 | 2025-06-21 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5b2dbee4-b42c-33aa-aa3e-4829ccd91bae | -11.86778 | -54.68563 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 59698651-e10d-3859-ad4c-202e74bb5095 | -11.88594 | -54.67075 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| dbfe149c-9291-3414-83a1-e5079cad1c0d | -11.93836 | -58.74696 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 34faca23-d442-38f4-8c2e-f6f9ac4255e1 | -11.94726 | -58.74568 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d392d041-d6b9-3693-9c66-83470337d439 | -9.48195 | -57.8375 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 947b1631-1a5c-3b2b-a9c8-c32b9e6b7af3 | -10.30401 | -57.13451 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a11867b-4326-3692-810e-ddbcbe5acf0f | -11.78615 | -57.24604 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 46435b37-06b9-3f29-858d-90393a8be00b | -11.94084 | -58.76522 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7eb8ef47-6ba0-3630-b60a-d590424f6695 | -10.14776 | -48.98838 | 2025-06-21 01:20:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2780b8ef-1fc2-38c5-9094-6300a39d2dfc | -9.47942 | -57.81953 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 42c54dac-973c-3001-847e-4f15461a2df3 | -11.52707 | -56.98549 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3bcca8ca-3b23-3594-82c6-1c725186b29e | -11.88772 | -54.68242 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 10b1ab0e-5dc8-3ece-9501-41a3800e949e | -11.57302 | -54.56943 | 2025-06-21 01:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5d74cf42-25da-393f-b37c-8ce67ca55ecc | -10.52599 | -53.63387 | 2025-06-21 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f87615bc-d459-3ed2-a6fd-7e7f11a135ad | -11.91873 | -54.81928 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dbedfaab-a3f7-31a3-af90-431b2c327cb2 | -11.53471 | -56.97491 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ced516bf-7e39-3d87-a93f-8d86a3f30c7f | -12.51 | -58.34383 | 2025-06-21 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7aa5b36a-a6e9-30c3-8ce5-de783d181baf | -11.61834 | -58.29544 | 2025-06-21 01:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 63a891e0-0efd-390c-8fbe-912eb5c80569 | -11.86677 | -54.67984 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| a8d766e1-9289-3e0a-bba7-2e285eddbf70 | -10.88846 | -56.45374 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 612c32c4-a0ed-3367-837f-2f0434c49562 | -11.87596 | -54.67236 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 675.7 |
| 02c65772-f67e-3611-92dc-cefb3c0ab0d9 | -11.9485 | -58.75479 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0986bafd-10b1-3cd0-a272-d8069732ba8c | -9.47436 | -57.84779 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9b520202-5355-39c1-b872-9db0d1449762 | -11.95864 | -58.76267 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f86683ec-6dab-3fde-a61e-29e3a2d565ab | -11.78744 | -57.25512 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 795cc1fa-ecdb-30b9-8576-1116ad29fad9 | -11.9396 | -58.75609 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b5e3c564-9dca-3162-b591-f5a8526257a5 | -9.47055 | -57.82083 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a9ed33fb-7707-3858-8f23-2ada3056e09a | -10.02996 | -54.31849 | 2025-06-21 01:20:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 726f6ba6-07f7-335c-96aa-d96d0fa23232 | -11.86504 | -54.66814 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2b4a3c8d-20db-3313-9fa1-9125ac3eb157 | -11.79503 | -57.24472 | 2025-06-21 01:20:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| df5913ed-9fae-30cc-b438-59e0cea6bd95 | -10.29503 | -57.13585 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5fb98783-dbd7-39bf-8de3-b2a3caf8bf5a | -10.03192 | -54.33151 | 2025-06-21 01:20:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| abddd52a-dd25-3322-9d0f-c3df9a36507f | -11.94974 | -58.76392 | 2025-06-21 01:20:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9abdd244-0acc-35fd-9823-86ad60937e6e | -9.46336 | -57.84654 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dd6e9773-3a3d-3f4e-9463-a6d3cc5df873 | -9.26187 | -57.52156 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| adcd2d76-cdb8-34ac-b180-deb757e3f708 | -12.28677 | -57.27085 | 2025-06-21 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5040306b-6751-377a-84dc-7426608ad607 | -11.88415 | -54.65908 | 2025-06-21 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4cd1574f-4453-38f1-b957-6680ae03f2af | -9.4621 | -57.83755 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a17eeebe-f5d3-3a19-b970-67dbe0ac496c | -9.26317 | -57.53071 | 2025-06-21 01:20:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| fe8f5fad-8d42-3b82-b734-9ac853c0f6ac | -9.01992 | -61.22705 | 2025-06-21 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f037912e-b27d-30b5-b36e-1dfdb00c2ab7 | -9.02131 | -61.23771 | 2025-06-21 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6ce18536-6870-33a5-8c26-ba181e02dde0 | -9.02954 | -61.22574 | 2025-06-21 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 477d93f0-1920-3d88-95cf-86f79793a0be | -9.02815 | -61.21512 | 2025-06-21 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2a646959-f897-3681-9387-62265a6b5782 | -9.4835 | -57.8438 | 2025-06-21 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 46f4ced4-ff0c-3e59-9c36-93705774842b | -9.4837 | -57.8241 | 2025-06-21 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 48b69c8e-0264-3f4a-9c84-1d52b70d7b3b | -11.8853 | -54.6722 | 2025-06-21 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 301.2 |
| f378ecfb-9407-3dfc-8d89-338bb222760e | -13.2343 | -49.8475 | 2025-06-21 01:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 082cdbb3-6c5d-3410-8ca0-d50fea963e0c | -11.8666 | -54.6535 | 2025-06-21 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a289e038-7b5e-3e10-b3d9-3dfe17f46542 | -4.543 | -47.9934 | 2025-06-21 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| f1933811-2925-3476-958a-c548f95bb925 | -11.8855 | -54.6517 | 2025-06-21 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 79b6d03a-259b-3b25-9d37-2f0cf0785602 | -13.2346 | -49.8258 | 2025-06-21 01:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d7b3f95d-a92d-38bc-acb0-295efdbe908c | -9.4648 | -57.8449 | 2025-06-21 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0a0d5cb9-e94d-34a0-a600-a3cdffb9706e | -11.866 | -54.6944 | 2025-06-21 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c4f36987-0fe4-3e81-8a76-3e1773a16c8d | -11.798 | -57.243 | 2025-06-21 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 139.7 |


[Clique aqui para ver as próximas entradas](README5.md)
