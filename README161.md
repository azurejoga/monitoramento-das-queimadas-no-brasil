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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe2c50dd-5b6b-3354-802c-369d364f90c8 | -11.245 | -45.3037 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| c24cbf0f-7fe3-31c2-9830-19c4b3589393 | -8.1856 | -44.4132 | 2026-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 250c1aa8-8f71-3544-b169-382fd3b4e825 | -12.214 | -44.6524 | 2026-10-10 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 62f7dee9-f802-3f97-b094-c698c5997ac5 | -12.7072 | -43.0611 | 2026-10-10 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 157.5 |
| e481a9b1-c6b8-3e65-9fea-a725b1a419c4 | -8.0581 | -45.5904 | 2026-10-10 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| fc2fcb2f-0112-3c1d-bc37-41273b8d5530 | -11.2083 | -45.217 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 7342238e-10c5-355d-a99c-1b30c8000eb2 | -12.2302 | -44.8126 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cd54444c-bace-34b2-9b24-044d9f4331a8 | -4.4977 | -43.6315 | 2026-10-10 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 54d6b1ee-e98a-3ab2-913c-1d713b3306a5 | -11.0374 | -44.0355 | 2026-10-10 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| ae4aadfe-2e36-3e81-b2b5-c5fb72dfb7ce | -11.0144 | -45.4042 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 91fb1221-76d7-3bae-b19c-9aaa30ce0646 | -10.8401 | -50.6712 | 2026-10-10 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| bdaeaa11-9ffd-3347-bfa3-c7757607a638 | -11.1873 | -45.3347 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1d14a1d2-361c-38db-93a7-e707d16796b5 | -9.1009 | -45.1622 | 2026-10-10 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4055081f-b47e-3c95-a15a-06324fa489ff | -11.8692 | -43.5805 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 308ab00e-d518-35ca-a4a3-6f9f3403c6d0 | -11.3823 | -54.0434 | 2026-10-10 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4cdab69b-47a0-34a7-9e87-c1b64c409016 | -11.1197 | -45.9602 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| a0758a60-b77c-3853-9bf9-c43f32593611 | -12.6873 | -43.0884 | 2026-10-10 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 290.0 |
| 021f1dc5-5199-3a0c-8d57-202ff6fff392 | -12.8513 | -50.9957 | 2026-10-10 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2e3e037e-0b86-3b5d-8bff-c1558dcd7bd0 | -1.5123 | -54.5361 | 2026-10-10 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 24616755-acf5-31c4-9376-f07d3deea62a | -18.3125 | -42.3901 | 2026-10-10 14:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 55cf6449-5162-3826-b742-38e16407e28d | -15.1088 | -46.9343 | 2026-10-10 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 191bac29-9dde-3f97-86b0-c815aa07f287 | -1.6226 | -54.3948 | 2026-10-10 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0aa6a48f-0991-33c7-904e-415fb4f56bdb | -1.8986 | -53.9899 | 2026-10-10 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| dd44d715-6f1d-3183-8d40-541a41ac0275 | -11.8503 | -43.5598 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 1bf59c56-69ed-35dc-8b6f-3a6bd11452b5 | -12.1917 | -44.8186 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 737.7 |
| 6a4f9ca3-6ba3-377a-a759-f55e8568529e | -5.7654 | -42.0866 | 2026-10-10 14:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| d670a516-8572-32b0-ac83-cd46c0f990be | 3.8754 | -61.3187 | 2026-10-10 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 581cf53a-c4f8-33c0-aa38-59be3af6685b | 1.6754 | -55.6266 | 2026-10-10 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 772b885f-ac23-3022-8666-160d4fb09357 | -12.8321 | -50.9981 | 2026-10-10 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4a1704c9-0dd1-3799-9b84-fb94941df31a | -9.9384 | -44.8791 | 2026-10-10 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 184.0 |
| f65f3531-3a4f-3765-a996-3ba6d20371b1 | -8.7623 | -49.6144 | 2026-10-10 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 238f5012-da95-3a4f-ada2-71daf85522f4 | -17.4581 | -45.0511 | 2026-10-10 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 2a2225c4-0be0-3cba-8a02-f0dd939d6662 | -11.0937 | -44.0975 | 2026-10-10 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1040.2 |
| 07fdfd84-1455-31e3-8e2f-7ae993aa6302 | -11.8508 | -43.5361 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| c535045b-4630-30fe-b219-8bf1d6c64b5b | -11.87 | -43.533 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.0 |
| b6f2c09d-c12e-31ab-9f45-7da4bf889b6c | 2.727 | -60.2586 | 2026-10-10 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 107.7 |
| b5dd933e-1cb2-39f3-af27-c6f3a11f5401 | -3.2204 | -49.4205 | 2026-10-10 14:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f13907a9-4bcd-375a-9286-c3dac54e4394 | -1.3264 | -56.398 | 2026-10-10 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 372fae6d-e758-3f05-8156-d592368c7adc | -7.4883 | -42.8532 | 2026-10-10 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| b2528662-65ea-35bd-ba26-cb843cca374b | -8.9311 | -45.1355 | 2026-10-10 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.9 |
| c7a75c91-064e-3030-b586-ba616731ee8e | -11.0379 | -44.012 | 2026-10-10 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 224441dc-5618-3182-aa29-c42d035d3659 | -11.8495 | -43.6072 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 58e16394-e6a2-31e3-a729-c188c34fd43f | -10.4147 | -47.2846 | 2026-10-10 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2f30609e-2e90-3594-997a-0aad125f7651 | -0.8768 | -48.7033 | 2026-10-10 14:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 45afa2cc-fa9b-3f08-91a4-3cc865adbcd0 | -12.1913 | -44.8419 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| cf980436-4aac-3bc3-82d6-32ef6e16d812 | -5.7317 | -41.6829 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| e03d694c-ecf5-3a1c-aa35-12363201969c | -11.8687 | -43.6042 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 9a1a1f26-e68b-3691-b9cd-7070c8de9e1a | -11.3447 | -54.0264 | 2026-10-10 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ec4fc5a5-634a-357e-8d41-5f9909da4fa3 | -5.7124 | -41.7325 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 9a36c96c-ee07-34b0-9ead-d599690f70ef | -1.2175 | -55.6512 | 2026-10-10 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7ee4942a-e693-3f30-b1bd-f06afbeaab25 | -2.8491 | -49.8763 | 2026-10-10 14:30:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b9ccdcc3-33f2-3f8e-a7af-66b0dbb01a86 | -10.2488 | -49.6636 | 2026-10-10 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 798e3c15-ecd7-347b-8e69-92afcc86091b | 4.279 | -60.9126 | 2026-10-10 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5f1be6f6-c5a4-3da7-85e5-112e1cf6069c | -12.0265 | -43.3895 | 2026-10-10 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 921294a9-4b34-36d7-9e0d-39d62e4d0afd | -12.4837 | -51.2959 | 2026-10-10 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 7ebd589d-9101-3f6f-b99c-fab02c1f8c6e | -1.3447 | -56.3979 | 2026-10-10 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f75d64c7-28b2-30d3-bedc-c6c1bc35c6af | -13.1641 | -54.3178 | 2026-10-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 56f10033-a2b3-3ec9-a235-b4f340c3f592 | -4.4977 | -43.6315 | 2026-10-10 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a7c59fae-3188-3da5-a81a-d5fd618f965b | -11.8692 | -43.5805 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 06a3c656-13fa-389d-ba17-3d1a9d232b50 | -12.0063 | -43.4402 | 2026-10-10 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 6186550d-be98-3871-9b32-58e87383e6d3 | -2.7428 | -54.1146 | 2026-10-10 14:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a8675cad-c629-3a4a-8824-c6ec3e776ed9 | -5.7319 | -41.6589 | 2026-10-10 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 8b720de3-23ca-3d2d-b683-d2d6f03ca6d5 | -11.6194 | -43.5959 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| c8819bb7-bd1b-358a-bf97-f10a656fc864 | -11.5998 | -43.6226 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| a08ca905-dc0b-34c3-b092-94780f9539b5 | -3.2203 | -49.4417 | 2026-10-10 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1bc8a469-7dd4-3ab1-8189-76c7cfa68816 | -11.2068 | -45.3091 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 1712166a-beb7-3fee-8360-6b2dd492ea73 | -1.2175 | -55.6512 | 2026-10-10 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5d0f5766-5bb0-3807-a33b-0aff5c7f8aba | -11.0332 | -45.4246 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| e39836fa-06cc-3256-9b79-d80152e8f371 | -11.7764 | -45.5265 | 2026-10-10 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 6b876437-6092-3bce-9c46-8038af227531 | -11.2079 | -45.24 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 37a51e65-a811-34d5-9720-21c52b746e93 | -2.849 | -49.8974 | 2026-10-10 14:40:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b2c167a0-1d0c-325a-8f01-20d2a2eed1a6 | -11.1197 | -45.9602 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 379.8 |
| 74361c50-51b5-31cf-9489-fd82586c24f9 | -1.2907 | -55.7295 | 2026-10-10 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f0739062-fa0c-3e68-bc94-75ac09e0f887 | -11.0328 | -45.4475 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 348ebc9b-4c55-34c8-98dd-4bcedb3beef7 | -9.9208 | -44.7893 | 2026-10-10 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 52ac44e3-44ec-37b0-8d63-94ff69309bbf | -11.8696 | -43.5568 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 44c95c5e-b96d-3297-b464-250891dbd663 | 1.3162 | -50.8505 | 2026-10-10 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f395d917-b988-3a53-b0c3-58c84ba663b9 | -2.4048 | -50.3085 | 2026-10-10 14:40:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3264d35d-a6b2-3e2a-993d-6fe359422326 | -8.9311 | -45.1355 | 2026-10-10 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 93b24fcf-5c8e-3b3f-9910-35b866e8a679 | -12.811 | -44.627 | 2026-10-10 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 76b50766-72a3-3c54-a572-4fc55c6f6fa7 | -11.0183 | -44.0382 | 2026-10-10 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 231.7 |
| ec058bfa-22c7-32e7-b32b-fb6898945e4b | -12.7072 | -43.0611 | 2026-10-10 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 146.2 |
| 6bc7731a-560b-33f7-9b3d-870b573a762c | -12.0457 | -43.3864 | 2026-10-10 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| db557bce-bf62-309c-96cc-f6dbfc8a7bc4 | -10.2488 | -49.6636 | 2026-10-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ee034ee6-87c6-35b5-9917-0443a49defe5 | -3.2532 | -50.4108 | 2026-10-10 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| cc50f8c3-f06b-33eb-8d5a-e9c48ccaeeea | -12.1861 | -48.4124 | 2026-10-10 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 69321302-b7fb-3f4b-a78c-f0e8948b5b95 | -17.4575 | -45.075 | 2026-10-10 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 239.0 |
| e2855cd4-46f3-3e8e-965c-db831dc0bffd | -17.4581 | -45.0511 | 2026-10-10 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 69ec11ef-3a86-38e0-be01-2c9e1f033ad1 | -1.2723 | -55.7494 | 2026-10-10 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f1656719-4880-327b-ad3a-ed77d33edea0 | -11.8508 | -43.5361 | 2026-10-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 14ba2012-28c6-3937-9497-28b7ddc76961 | -11.3865 | -50.8891 | 2026-10-10 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d5201e70-7bf3-305a-9e0c-94ce6cafb386 | -10.5281 | -47.3156 | 2026-10-10 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 87c26d38-56df-3f53-9249-551f5d56b0b8 | -11.1873 | -45.3347 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 9a26d920-713c-3398-a298-27c28787dd53 | -11.0187 | -44.0148 | 2026-10-10 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f335a211-f9b8-3c12-b9cb-5f5f1f17a762 | -1.3447 | -56.4175 | 2026-10-10 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| fe2b4bf6-b65d-3e5b-9d0c-bf11fee2db41 | -10.9796 | -45.2026 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 07356521-93fb-3f7f-95b6-02c51c16704c | 3.9309 | -61.0906 | 2026-10-10 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 51502c77-e203-3eda-8f63-aae14963c2f3 | -8.7623 | -49.6144 | 2026-10-10 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 119e8821-da6b-3b53-a35f-1e9b0e43b123 | -11.245 | -45.3037 | 2026-10-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5af1a466-a0ce-3a39-bd16-1726b0e182ff | -1.6395 | -55.1914 | 2026-10-10 14:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |


[Clique aqui para ver as próximas entradas](README162.md)
