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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796631fd-3054-381a-97c0-a9a1b336304b | -7.09929 | -44.92939 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44c362c5-2032-3d69-bba6-dcd781c53961 | -7.24429 | -45.39045 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d31512-a8b1-3094-9115-3d3fc5666b1a | -7.38108 | -43.4472 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38907615-39bb-35af-a9f7-c7cefc0d6e43 | -7.08578 | -44.92064 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1dd695a-0ff0-30d4-84a5-c164dca007bb | -7.78045 | -44.60623 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c622f0a0-7d21-32c6-91b2-6f72b6726d4d | -7.24481 | -45.38751 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d5b57da-522f-3c3c-a366-98dfcca609f6 | -8.8901 | -47.34652 | 2025-07-28 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b8a0460-e4c7-37ef-ab91-b84453ea77ed | -7.9129 | -43.10575 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a76a175-b8f3-352b-a7c4-26a28f7b863b | -8.73988 | -46.68633 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c416e5b8-8725-3aca-b787-f4b26ecc70e3 | -7.21049 | -44.16762 | 2025-07-28 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11000bb6-7e0c-3571-bad2-12222a39fad8 | -6.95579 | -42.68516 | 2025-07-28 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 357b9055-e86e-3116-9da3-b7d8597f386f | -7.34122 | -44.70167 | 2025-07-28 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c2cc373-8db4-34c3-a09a-8056a4e7d83e | -7.41894 | -44.70833 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1fe224e-c4c8-3517-8cd8-92456ce7ee02 | -4.0457 | -42.52807 | 2025-07-28 03:47:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1d83fcc-f0f0-33d1-9c24-5ce2cf3a86cb | -7.69375 | -46.05107 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa63a63-894a-3005-a92b-fb60a9c94cd5 | -4.22297 | -41.14671 | 2025-07-28 03:47:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 98372e3e-13eb-3538-b553-98825c27343b | -6.25378 | -44.96163 | 2025-07-28 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ec7736f-d80b-3e6f-888f-438262bbd7bf | -7.66313 | -44.80258 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fcf77ab-1c75-376a-aa9a-136ffca18340 | -6.25781 | -44.96782 | 2025-07-28 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18ef6d09-0e48-33dd-9d8a-2fd5af43108b | -7.10691 | -44.88624 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c49e3a1-6282-3cce-8e0f-bb33d9d2d6ee | -8.31043 | -42.2147 | 2025-07-28 03:47:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ca73ecb-c013-3468-b5bd-2e376ce097b7 | -6.92205 | -44.25352 | 2025-07-28 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feda6127-adfa-3a52-827b-0dd5ecb3b1e3 | -6.98811 | -47.08075 | 2025-07-28 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f6f4710-1610-3d71-b86b-5c1041252fb6 | -7.29247 | -43.07445 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3aaa0b9a-c095-35ae-bfc4-8e0c3e670874 | -7.28532 | -43.07385 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39883ea6-79cc-3fb6-803a-5599ac857e15 | -7.34888 | -44.71406 | 2025-07-28 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 310401d1-caf7-325d-bf56-9f55c9399950 | -6.16337 | -44.77248 | 2025-07-28 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 224f7018-40b4-3867-b3a5-e5a1f165aeb4 | -7.39507 | -44.67505 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de0c37ea-214a-3fa9-8155-d5b3902f0a81 | -6.63269 | -43.03561 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de1d0ff-be53-3433-bf74-2796a85711da | -6.3941 | -43.38091 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8e3327e-72b2-32bf-8fc2-06fb767c8872 | -7.3763 | -44.47639 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 508439db-4f5a-3815-9628-219f22d9d29a | -7.92037 | -43.10937 | 2025-07-28 03:47:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ffd4dc4-34be-33b0-8023-381e7b737c5b | -7.08111 | -44.90282 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a08addd-ba19-344e-8440-bc8bad16026f | -7.38015 | -44.48203 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d052e14-651e-3cc9-83e7-e6a5de25a5e3 | -7.78151 | -44.60805 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd9c9695-1d88-3c9a-bac4-2dc0daa1c6ca | -7.07531 | -44.90746 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c5c1ed2-0e17-3790-ba09-1529517bfed0 | -7.53716 | -44.4254 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c45859-770d-3cd0-9aa7-5e8bf6ab180b | -7.65831 | -44.80197 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5b2659a-7b9c-39e6-a028-d40033c49935 | -7.08228 | -44.92547 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dbf6c157-feac-386e-9ed1-cf09285c432e | -2.95456 | -41.35909 | 2025-07-28 03:47:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 89c1104a-8737-33b8-ada0-72cdfb88bd0c | -7.07678 | -43.87479 | 2025-07-28 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7813d395-c435-3dad-80df-b8fd87364ab1 | -6.70314 | -43.07693 | 2025-07-28 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b86bd6c4-020b-31f4-b033-857c694be138 | -6.38792 | -43.68786 | 2025-07-28 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bba702d1-0a38-3c2a-81fd-bb31647b5173 | -7.02445 | -42.10929 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 213b96b1-a9b5-3dc8-b7ed-107ddabc77b9 | -7.37815 | -43.43797 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92cf05d9-7986-32fd-bfa5-5dd42aa4d99b | -7.14587 | -48.2089 | 2025-07-28 03:47:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171df8f5-d890-33a3-875c-7100d5ad551d | -9.12233 | -45.86324 | 2025-07-28 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea073f95-cbdf-3c28-a2d0-0975044fa647 | -6.92378 | -44.24346 | 2025-07-28 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abbb1e78-2825-34a7-93b6-326df5a6eed5 | -7.07513 | -44.92409 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e723867f-ad6c-3872-8dc1-f685ed8b1d2a | -7.29535 | -43.08324 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03dd55ac-8572-3524-b979-3e7dd4984573 | -7.34985 | -44.7365 | 2025-07-28 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29901d61-13c9-339f-aefe-9c7f06512a9c | -7.0832 | -44.92005 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4918cacc-8ce6-3c46-930a-3196eb03c73f | -9.23036 | -40.32057 | 2025-07-28 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c88e1d91-2cc3-3e1b-b533-07ccb5b8c1c9 | -7.38102 | -44.47711 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ebb2b0d-4eaf-3db5-a926-97e4b5e0f2f7 | -7.69488 | -46.04473 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b68d33fb-fb6e-38e9-9f26-24c756ba85b0 | -4.40142 | -37.79353 | 2025-07-28 03:47:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fcaa21eb-557c-3321-b676-089abd9388e0 | -7.23875 | -45.39251 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88236d3d-6828-317d-b9b2-27dc7ae50423 | -7.69026 | -46.04057 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d2797b2-f90c-3a18-a5d2-072f84bf2312 | -7.29178 | -43.07844 | 2025-07-28 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d4b3c4a-2aea-3bfd-bf19-fd841461a95f | -7.08482 | -44.92604 | 2025-07-28 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34196f72-e43e-32ff-aab3-8029f387b42b | -7.52741 | -42.41668 | 2025-07-28 03:47:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be0514d1-e72f-35fb-85af-e8e77678df54 | -7.34507 | -44.70776 | 2025-07-28 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18eeb337-9cc9-3dc8-8e68-a8642d5a0874 | -9.12727 | -45.86454 | 2025-07-28 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c7b4727-13fc-392b-bee8-1bc49bf4aab7 | -7.29947 | -43.42284 | 2025-07-28 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53141fb2-d637-309d-b581-9f76a250e9dc | -7.23824 | -45.39539 | 2025-07-28 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97d10898-d031-3159-8cb4-8987f4c64043 | -8.0353 | -46.90253 | 2025-07-28 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8abfe56c-c9ea-33c1-981c-1e956ce1f058 | -7.53133 | -44.40369 | 2025-07-28 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c0fa906-797a-3e21-811c-e8c45190090b | -7.69319 | -46.05425 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3d0654-0d2e-3abf-9da6-49bc19fbbcd2 | -6.38524 | -43.37933 | 2025-07-28 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0e84f2e-742f-304e-b44a-b1366d49025f | -7.00225 | -42.36205 | 2025-07-28 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51b062ec-e721-3d0b-8af2-89fe5acb5c69 | -7.68969 | -46.04375 | 2025-07-28 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 492965d9-9b0e-385a-8716-6140463b1ed6 | -10.54067 | -49.49441 | 2025-07-28 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a8f45de-a1d8-3857-b38c-f8a1908ba70e | -5.78516 | -43.60476 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2eb67a1-4b7c-3e7c-98f3-18745626a1a9 | -13.10683 | -47.37594 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cd41a05-c208-394b-b748-5b1ee97b745d | -4.16109 | -46.82127 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| e6df290b-e75d-31be-a614-d1112805260b | -5.1068 | -43.78453 | 2025-07-28 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c041510-1038-3c10-ae65-6b373b4600bb | -12.68471 | -47.03765 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d821ff-11d4-3c47-9228-2496605312c2 | -5.96431 | -45.06038 | 2025-07-28 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c6ad7e-b8a8-3dad-ac00-31868f314dee | -6.41349 | -41.14257 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dec2c6e-cf89-318b-80a0-6f35f31cd29e | -6.37125 | -41.79236 | 2025-07-28 03:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c0c666b-b5af-3e52-883f-76d3cbf5acf2 | -10.51552 | -42.55435 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b32d9844-de0a-338f-ba30-739f73da104a | -17.36244 | -42.64475 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 837e7fee-b8c1-3599-8c0c-dfa49f7464fe | -5.72875 | -43.8505 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39b622fd-e06f-3db9-84bb-07e3d06a1feb | -5.75114 | -43.96978 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 485df011-b1a5-37f3-8426-6d888b4731c8 | -17.35349 | -42.64438 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6896aa91-0336-3ecb-a952-9c8a7fd1b940 | -14.49684 | -48.64827 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 228346b0-33e7-3ebb-99ef-9a86f6a74101 | -14.51088 | -48.66304 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c36412e5-93a9-3c31-9582-81cbd98e19ca | -17.35855 | -42.6365 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78202fc1-09fd-384b-8385-d5a835f5fa21 | -10.83895 | -46.68049 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75f9b2bd-84d7-306d-b7d2-60ec0e1d366e | -12.74546 | -44.72873 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d17ed20-24b9-3c5b-8c87-2e612f9799ea | -10.5185 | -42.55663 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ebebf3dc-d70f-32ea-9353-38dbbc310e6f | -17.35993 | -42.65006 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cdd0177-ead2-3f24-b8ad-e9b8e0f5d578 | -6.14368 | -44.34585 | 2025-07-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a1697a-463b-3767-85be-f3bfc3076738 | -13.108 | -47.37647 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dfbddcb-a121-3762-b362-a669ec2d4e7f | -4.16107 | -46.82284 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| fcd37741-31fb-3fc4-bfae-1b2e3cf7e5d8 | -10.51945 | -42.55501 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 148f6493-ccd0-3db5-8979-c2a4b54e5c5f | -13.12813 | -47.35582 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e709b0e-8415-35ef-a611-69622e68a282 | -6.24424 | -44.06696 | 2025-07-28 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cdedba3-8210-37fb-80ff-d645df41d25c | -10.52031 | -42.54994 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b2bfa975-793b-3a42-b75f-e885288121f3 | -5.7477 | -43.98978 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
