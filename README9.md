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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23ceed91-0042-3519-a0dc-d6c008bb460a | -2.926 | -51.473301 | 2026-08-30 00:32:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9956c356-1924-3f9b-9fee-3ed67f5d736c | -4.1608 | -60.675499 | 2026-08-30 00:32:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6af1f63-253d-36d2-a9d7-58ed8424171f | -11.2409 | -53.98 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa6fdd28-30d4-3b92-b6d5-808646354600 | -14.4001 | -52.545601 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9d00ee1-899a-3445-9d6d-4c870ecb0e0d | -9.1942 | -51.5313 | 2026-08-30 00:32:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59e2b333-b5f3-3b57-8a25-dc49be8c3a8b | -2.9123 | -54.103298 | 2026-08-30 00:32:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08dc9ca0-b105-3a89-b1b8-bd9a40c27870 | -7.5166 | -55.3251 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e1c5f4-5ca5-3213-ae28-d33f0dce4ba3 | -6.7906 | -55.6684 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab0bc9e9-460d-31d9-b185-0131d2dd830b | -4.9581 | -55.853401 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efb850b3-a516-3510-ba17-846d78dbedb9 | -10.7546 | -44.866299 | 2026-08-30 00:32:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3725b5-9197-37f6-8bd0-15de782c685f | -11.3066 | -54.0505 | 2026-08-30 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d4310411-acea-3e99-a150-64e4de15655c | -5.8894 | -57.7708 | 2026-08-30 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 7eaf60d5-7e54-3a65-9873-754ee445b957 | -3.6215 | -60.566 | 2026-08-30 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 33dd207a-31e9-3388-b783-1829a0d3415a | -10.8062 | -45.3178 | 2026-08-30 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a2c97d69-e5fd-3f88-88b6-262357988641 | -10.9405 | -43.0117 | 2026-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9434ed10-d803-3035-a150-2d64a483a3c4 | -6.9363 | -55.6958 | 2026-08-30 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| d53d0cbf-a0eb-3121-af3f-6d6562167f91 | -3.7715 | -59.3419 | 2026-08-30 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b6613a4c-ca48-3a7f-80b1-16dcb96d4256 | -6.9361 | -55.7157 | 2026-08-30 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 0837f4d2-03b2-353f-b0fa-9fe559223a8f | -11.8389 | -51.1152 | 2026-08-30 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3b7c24d6-32e2-30b7-86de-59321bc860b6 | -9.0615 | -65.4169 | 2026-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 45c1fddf-b060-3571-8b7b-c0ead58547c6 | -5.4875 | -57.1611 | 2026-08-30 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d51bd364-ccba-3ac2-97e3-509c6e33fa55 | -7.5477 | -61.3247 | 2026-08-30 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3b2d311d-16d6-3225-b30f-8dd7e4aff797 | -9.043 | -65.4175 | 2026-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 552a3bed-2155-38fb-9523-bdf3d5c1ae07 | -3.7532 | -59.3423 | 2026-08-30 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8d067a39-43f3-32aa-985e-040dd44f2723 | -10.7752 | -44.8852 | 2026-08-30 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3b056606-2443-356b-851b-f751fc5ad560 | -11.3068 | -54.0299 | 2026-08-30 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 2f24417f-db17-3e91-ab73-e61d25fe0c64 | -4.9604 | -55.8424 | 2026-08-30 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fa61c55c-6e30-3860-bfb2-e688e9e7a279 | -3.6398 | -60.5656 | 2026-08-30 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fe4c7423-4ab6-398a-9226-da39742d7745 | -10.7407 | -54.0401 | 2026-08-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| aaed0018-011e-347b-b32f-8105f658ee5c | -7.3117 | -60.6089 | 2026-08-30 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 71cfb163-7761-31f7-be66-1cc0011269eb | -5.4876 | -57.1416 | 2026-08-30 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f6b627b3-71d2-3706-96fd-e949d3b25a60 | -16.1428 | -43.0347 | 2026-08-30 00:40:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 612e318e-3515-35a8-bdf1-158f3e0f7e78 | -4.1516 | -60.6878 | 2026-08-30 00:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5d020bb1-5f7f-3958-a43b-781e79a96813 | -10.9401 | -43.0355 | 2026-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 34ad52aa-e347-3804-a2ae-f5c9bb137fa5 | -10.9593 | -43.0326 | 2026-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4d7cb7b7-5f0b-3780-bd7a-bc68dbaafd61 | -6.9546 | -55.7147 | 2026-08-30 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 54d1a3a6-d9a6-38d2-9d89-a33873e20580 | -3.6216 | -60.547 | 2026-08-30 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 19379e66-498a-337f-a1c1-2a70dd4542d4 | -9.9281 | -60.5242 | 2026-08-30 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5c2b0372-6e11-34cb-a400-57b6e0e4f382 | -7.5661 | -61.3239 | 2026-08-30 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 93cea77e-74bc-3bb1-a01b-82561cd696c7 | -7.5662 | -61.3049 | 2026-08-30 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6a3e6d03-3c82-3269-84d1-79362bd4904d | -5.871 | -57.7715 | 2026-08-30 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7a5a1924-1b21-3769-a531-092c0e6bef84 | -9.8927 | -60.2752 | 2026-08-30 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1b8492c0-cf6a-3ca0-ab0d-8109e08b6548 | -11.2879 | -54.0317 | 2026-08-30 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b0c09920-36c8-3f30-b7ce-db47056f7d58 | -7.2932 | -60.6096 | 2026-08-30 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 6586d6f2-20df-3f81-a36a-80e72936c159 | -23.15006 | -48.67174 | 2026-08-30 00:41:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 953e0625-8c9c-3180-93d2-a96acddfa430 | -24.80128 | -53.21926 | 2026-08-30 00:41:00 | TERRA_M-M | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 35ce1c10-914c-3538-96f7-765d5266f8f8 | -22.01541 | -56.03211 | 2026-08-30 00:41:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e9d2f0a6-cad0-3335-bfd1-42a9daac4e50 | -19.08302 | -57.39281 | 2026-08-30 00:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 61a34b67-f2e3-30da-9282-a1c979de0c27 | -14.39854 | -52.58191 | 2026-08-30 00:43:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 327a2de8-4379-3cf2-9253-f0ad7a7700d3 | -14.40032 | -52.57497 | 2026-08-30 00:43:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 65a1eea9-1bf6-3fa4-99d5-cce400d3225e | -14.39541 | -52.56248 | 2026-08-30 00:43:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| db5430d8-05a4-3814-bc0b-3d66989a48fb | -16.3448 | -50.98457 | 2026-08-30 00:43:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 19053f2e-4404-3236-abf9-63cfb00a2488 | -21.01557 | -57.83924 | 2026-08-30 00:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 5fbc3d9d-69d0-35d9-bb5f-21ef40ba6de2 | -21.01429 | -57.82979 | 2026-08-30 00:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 5d6edb2b-543a-37b2-ba21-62a4ca5ae0f8 | -16.35189 | -50.97647 | 2026-08-30 00:43:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 8f5ff692-0725-3a1e-ba14-4fa2bbd67263 | -14.42503 | -52.56995 | 2026-08-30 00:43:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f1f2956e-ccc2-3aef-93d7-d930293e9af7 | -14.43739 | -52.56744 | 2026-08-30 00:43:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 79f90f93-19b4-33d0-90d2-e5f86fd78fe7 | -15.64714 | -56.4039 | 2026-08-30 00:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4ae28eee-901f-3e7a-b018-d6d1fba51d69 | -15.12407 | -53.59394 | 2026-08-30 00:43:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 017a6553-46b9-3a96-8e90-210fa5632348 | -19.08432 | -57.40213 | 2026-08-30 00:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 6d16fcda-33d0-336c-addd-f3f2313c29d9 | -19.09315 | -57.40073 | 2026-08-30 00:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| b54762e3-9310-3975-a35e-e20f6aa749a9 | -16.35622 | -51.00085 | 2026-08-30 00:43:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ecac9879-f065-377c-987f-1c3466c20702 | -15.12152 | -53.57842 | 2026-08-30 00:43:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7a8f7655-c718-3356-a6cd-bd9394ec5077 | -14.25523 | -54.67532 | 2026-08-30 00:43:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c53d12ee-56e2-31b1-b878-ddc90d65d80c | -15.22224 | -57.6653 | 2026-08-30 00:43:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 20e8c5d8-6acd-3589-a540-2b583f73cff0 | -15.64561 | -56.39368 | 2026-08-30 00:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e0d5e969-1ddf-30f9-8c56-4666cf80b92a | -14.25316 | -54.66188 | 2026-08-30 00:43:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 375d0ba2-13fa-349d-9b5b-a97fb195f290 | -19.09055 | -57.38209 | 2026-08-30 00:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 073dcf7d-29e6-3431-b6ee-c8610484e36c | -11.18936 | -55.1049 | 2026-08-30 00:45:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a98949ec-550b-33e3-aeb7-b31b7f4582b0 | -11.29653 | -54.04374 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 187.2 |
| d6e1debb-6960-36e3-b358-e12051969f49 | -10.354 | -49.97523 | 2026-08-30 00:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| eabfbd65-def9-3c8e-81b7-5567eabe8343 | -10.75354 | -54.03343 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 126f5d40-9071-368f-993d-de8e76ce57de | -11.49823 | -60.47053 | 2026-08-30 00:45:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b21dc82c-d206-3bfd-b05a-6c2b998647b1 | -13.83227 | -54.09805 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fc641021-4245-36ea-932d-bc8c7664b36e | -10.73832 | -54.06003 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1d947c2d-fc69-3535-8faa-cc372c2e7eb9 | -11.29387 | -54.02734 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| dccd3553-7326-31c1-8276-afd855987c14 | -14.28448 | -57.04765 | 2026-08-30 00:45:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f2df2c4a-8173-3f66-a1b2-44e19768f3c5 | -10.76274 | -50.70005 | 2026-08-30 00:45:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 56af31f8-2bdb-3e02-861e-9396bb7982fa | -11.28955 | -54.05146 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 028e7e5e-3591-3fc8-8966-b4295f5a7d5a | -11.18467 | -55.09693 | 2026-08-30 00:45:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7109eed4-2586-3b7b-b877-b66e796f4a39 | -11.00015 | -50.54854 | 2026-08-30 00:45:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 367306a4-c998-3630-b552-4433a5182f58 | -13.86168 | -54.13937 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f9d78883-5bb7-3c8d-b90d-a1ffa5ca81de | -13.85693 | -54.10938 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| bc431435-adc8-35e8-be1e-bc364e6549e6 | -11.29872 | -54.03299 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 86d7c0c5-71a5-3a6e-a042-d4045e500673 | -11.03567 | -57.21794 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| caf68d59-00fe-3d7c-979b-a9e8ddde4ec0 | -13.85058 | -54.14122 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d2250dca-c927-308b-8977-5f2cfb3232e9 | -11.24648 | -54.00727 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 41c40952-1acf-3570-8ce1-fe0f2529688d | -13.84821 | -54.12631 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 918.5 |
| 59349219-ecad-30d5-b6bf-7f80a814cea2 | -11.59748 | -58.51283 | 2026-08-30 00:45:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5675d673-c6e5-3f9f-b090-db26ac5c4bd8 | -13.84582 | -54.11135 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1572.2 |
| d9f556da-06a1-3cdf-b3ae-933758cdee40 | -10.75015 | -54.05806 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 1daba7bb-01ff-300c-a957-b2fe15d36436 | -11.62641 | -54.58995 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6c80e9e3-2a60-392f-b0f8-62c9b0ad7b0d | -10.74752 | -54.04097 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 5ee69e27-3058-3576-a6db-b43c9a161ab8 | -13.8347 | -54.11321 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 362.4 |
| 73453aeb-38e3-33a5-86a3-6a33d1b5b3c8 | -11.03863 | -57.23849 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 306d586e-b957-38b6-b874-05724391fd6b | -13.85294 | -54.15606 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 32e43b04-ee9b-31f4-869e-1256603f879a | -10.99484 | -50.5169 | 2026-08-30 00:45:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5d4cc6b7-8ccb-356d-9145-07fc8e4ab298 | -11.0401 | -57.24873 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c793861d-6af6-3b1e-be42-56bac54f5075 | -11.03072 | -57.25021 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 86140203-ec30-3610-aba0-f08a71fac133 | -12.56141 | -55.74021 | 2026-08-30 00:45:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |


[Clique aqui para ver as próximas entradas](README10.md)
