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
| 865eaa75-0902-3fe5-89ca-ba8b372149be | -7.6235 | -43.62791 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14273866-df84-344a-b247-ea5f453d2cdf | -11.04938 | -44.29192 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9030f8e6-ed12-3d41-a0f4-8d7b2fb95a19 | -10.64492 | -52.1871 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 246959f3-5754-3524-89d1-9b2efdf24368 | -12.04394 | -54.25021 | 2025-10-31 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc592fb6-8f83-362d-8644-efe5f3c4bf4a | -13.68417 | -44.72883 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0eea0be9-4bed-31d3-a525-ca4c0143b3bf | -13.87857 | -47.33797 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28a44de7-aa2d-3041-9d9a-c4d8008ef3bb | -12.13475 | -47.15493 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d839098-e589-38fd-8b9c-3ab100172a6f | -12.66124 | -43.76976 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f86dd3a-1ade-353c-8419-796690621949 | -11.50702 | -43.25465 | 2025-10-31 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de10cf34-71ce-3841-a62f-d564fcdb2225 | -7.95462 | -43.79204 | 2025-10-31 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eceb9841-24ab-3b6d-aa50-1101f0d12a3c | -12.53021 | -43.75875 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45895fc5-02cb-354d-be12-e84796cec471 | -13.74568 | -40.67857 | 2025-10-31 04:08:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cafbb48d-792f-3acf-b551-cd0ecb611159 | -14.65365 | -44.27242 | 2025-10-31 04:08:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b8bc062-43c9-303d-88f9-270d0d4d24ac | -11.72014 | -41.66135 | 2025-10-31 04:08:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 00e56632-92f5-3663-92db-e48c52ed2373 | -13.52 | -47.34594 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baa35dc5-3edf-3779-9861-74dd4b87af8a | -7.39808 | -47.64038 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bdb3c21-43a7-388e-9bf4-cbcb38cf5f72 | -10.50706 | -42.4049 | 2025-10-31 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 93b7637a-ec2f-343d-bc8a-63a7d5f744f1 | -9.8831 | -47.45888 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab95623-f40e-3f49-a081-2192145f7647 | -12.53015 | -47.54566 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 880a38a5-c53f-3116-bb96-88df76a773e1 | -13.81491 | -47.06148 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f43884d5-ee06-3425-9aba-7249a1da4545 | -7.39745 | -47.64412 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77486f12-c687-34b5-9f40-555aeb99d174 | -11.69659 | -46.69715 | 2025-10-31 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 767c55bb-778c-3d01-8cfc-9313b348a09d | -10.47618 | -48.36504 | 2025-10-31 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5ee1330-519f-36c4-8925-a61767ee464a | -9.93128 | -44.90813 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f56bd89f-75a2-3c44-97f4-302a81bf5d5b | -7.64971 | -43.59733 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| b3a31d6c-4624-304e-bac0-5d0f55ad974a | -12.28943 | -48.06848 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bb8f323-b90f-3af7-a75e-1232de427092 | -11.29819 | -44.4864 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16b29695-71fc-347b-85b7-016e4001771e | -10.97165 | -45.47695 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ab06ea-86f6-3e3e-a5e2-3ad23176e4be | -8.04732 | -41.10926 | 2025-10-31 04:08:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c1475cd-1495-3795-a5b0-60774c801ba9 | -8.32472 | -47.9325 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c5625fc-4397-32d8-8df6-2747ab030e67 | -8.18001 | -45.69175 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fb870b4-9d87-3f9e-9462-be9984354c42 | -7.65061 | -43.58997 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4e86d434-f2d3-3dd7-a6d4-76cd7337926d | -12.84455 | -43.4751 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8e375280-9e56-31f9-8eb5-af0c44b574bf | -9.34325 | -46.59638 | 2025-10-31 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d81b2aed-60ec-36b8-922a-56aa8f8be98e | -10.92913 | -44.1656 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfa90fd1-7c1c-34a7-8178-ebd8dc0b0557 | -13.2872 | -47.73407 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fc81daaa-5327-35ce-b9a2-b048e6b45143 | -13.44169 | -47.36589 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59a59052-6b3e-3c73-875d-b591e15db5c3 | -7.91408 | -45.70625 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 905d7702-c090-3779-bfa2-f2e09cc81579 | -11.69454 | -46.7084 | 2025-10-31 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74891da8-bfce-3b45-b4e7-8dcb15a4460e | -8.1664 | -45.496 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19adfecb-19d4-39d9-9967-ee0b117b4015 | -9.73339 | -45.40616 | 2025-10-31 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae0575b-2535-30b6-9609-44d129e2ac1e | -11.03156 | -45.49189 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60187373-f59e-3320-a4e0-880c190a4ff3 | -10.27971 | -44.55413 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b04e60e1-9fb5-3665-a3ae-a16e4b1f8bdc | -10.88743 | -44.31513 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3de2bfe-e0fa-39b4-b303-8dd8f3b15e06 | -12.60199 | -47.52734 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 62accf42-45e7-35fb-a3f7-ed8456034f27 | -11.05216 | -44.29622 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeeb57ec-9df4-3070-99bf-76c742045be4 | -10.6436 | -45.24783 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67d17f08-2f75-3d34-8e12-4f1451cb3c35 | -10.63498 | -43.96597 | 2025-10-31 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8eb8483b-f0b2-3668-aed4-253229bd380d | -13.53552 | -47.4291 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60d5b110-fcab-3b14-a9f9-b2b4ccd0378b | -10.65 | -45.25311 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7da5872-617e-34e5-9413-274c62ccaf15 | -14.38623 | -43.71685 | 2025-10-31 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e11266-d838-32c2-99d2-955ddbf16924 | -13.22555 | -53.87849 | 2025-10-31 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d253fe6-3f04-3c19-b779-19e92b30e764 | -11.30161 | -44.48698 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e751a13-1f64-31fc-a422-d350306265a7 | -8.15901 | -45.47193 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6110cce-007b-39ed-ac5a-5d9de7b76bd5 | -12.53079 | -47.54394 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ed3779e-1179-315a-ae0a-85b8bf21c266 | -14.31271 | -44.57384 | 2025-10-31 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0690dd3-0d2b-31a6-832c-1a07a75dc888 | -11.34308 | -46.03218 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84d73dbe-af26-3328-bc99-ed7fff56fc27 | -13.88237 | -47.33859 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 755c2eb5-d296-3be0-88c9-56f4172df620 | -8.10651 | -45.17908 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e94062c5-640e-3664-8cca-10b9017de4c3 | -7.30808 | -45.66324 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eb22c84-5f25-39c0-aed7-81cac44f0a65 | -13.68478 | -44.72513 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2c02dde0-3221-3055-ba11-6b26c86d598e | -10.53717 | -44.77818 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d70dfeec-1ab1-33b1-9e9c-ecfb1486bf85 | -12.84568 | -43.46802 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aeca7bc3-b753-3cc1-b3ed-b0283ba64c17 | -7.39377 | -47.63985 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fe1ae46-de90-3bbd-a8d8-5cdca60d5b5e | -8.7945 | -42.80912 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 63adcba1-d041-3cd5-a055-c4ef225b9e7d | -10.65354 | -45.25375 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c2ffe3-d3a5-3dbf-b2b7-7cf303cca1ac | -12.88892 | -48.63351 | 2025-10-31 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50e1459c-4c1c-30ca-a40b-e185fc924b4a | -7.66056 | -43.59524 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 89577fbf-e975-3a7e-b96c-5e25fa4ad4fb | -11.80916 | -43.17045 | 2025-10-31 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df8398cf-c968-360f-b271-6af532d9e1ba | -13.37939 | -41.32264 | 2025-10-31 04:08:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4119b77e-7b2c-38d0-bdec-06f21ccfcc87 | -10.95347 | -44.67928 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de4ef13e-798d-30aa-8c40-18f844c40b65 | -11.64074 | -44.04517 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e769c9b-e94e-33b0-a12c-f522435ef8e7 | -15.40571 | -40.86322 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a8d1880-9fea-38f7-a8d2-643abfcae7c2 | -9.91799 | -47.18603 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00c36be6-8beb-3602-a6e2-b707f4a239ca | -10.24266 | -44.56342 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 181fcc54-6536-35e2-9c7d-40e80dd80e47 | -12.75306 | -43.4528 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec7f750-0544-3177-80b7-3b3da5cafe08 | -10.8566 | -44.90623 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8323331d-d5d3-382b-8159-8e0f245153b0 | -12.20415 | -43.10143 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4996964-c7e4-37c9-bbfe-73f2f1003de4 | -11.36275 | -42.25629 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0304cf71-32de-327e-8233-6f54d80c4484 | -11.05104 | -44.01932 | 2025-10-31 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc6d89f6-76e5-32ac-aebc-c111599ab839 | -8.18736 | -45.70066 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b12448e9-62d7-3a93-8865-981891cb3051 | -9.87259 | -44.86968 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 690815c8-6eaa-30a9-890e-797fd303e647 | -7.78079 | -46.40777 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d70afac-a3bb-3773-bfdd-959dc618df93 | -10.67456 | -47.97933 | 2025-10-31 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95d8dac7-cddb-3e9a-92e6-7c568e4affab | -12.30886 | -43.19118 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19044d3e-8f38-3f2d-a7df-9263c9924bca | -10.49364 | -43.32102 | 2025-10-31 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 096559e2-9cc7-30e3-b0d1-d41525739995 | -9.89247 | -47.45308 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de73927c-4df0-3162-a15d-751410a6bd48 | -10.53587 | -44.78598 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e630aab8-a50e-3599-9693-ab13a2cf43b5 | -11.34234 | -46.03657 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce397594-61b1-327b-9585-f19437f6c943 | -7.88176 | -45.69183 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17b7ce13-a5b1-387a-8a57-6f3b5beae010 | -10.88293 | -44.36437 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ffd5430-8aec-390d-a840-299ba2dfa86a | -13.93984 | -44.04148 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96dfcc3a-f6d2-3e08-988c-141874be4ea1 | -12.27572 | -48.05127 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac04f2fd-1d1b-300b-bd0c-cec48c40b116 | -13.23116 | -54.34839 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78c2952a-fabd-31e3-8741-2a77944a059a | -10.92958 | -44.76656 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 990e7373-c98b-395a-8f9c-4bed6a6aeaa5 | -7.3134 | -44.9572 | 2025-10-31 04:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 764c9dee-3f04-39b4-951b-d8759c53972b | -7.3136 | -44.9343 | 2025-10-31 04:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 46f99b16-eab7-3afa-a926-d69d9e53f233 | -5.0399 | -43.6205 | 2025-10-31 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 490d13dc-d0ea-3822-96af-6ce2f93c08f4 | -13.2401 | -54.351 | 2025-10-31 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| fc3beab5-81dc-341c-9abb-18b2f4df0450 | -3.017 | -49.4482 | 2025-10-31 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |


[Clique aqui para ver as próximas entradas](README30.md)
