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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe4f862-aae7-346f-8ad7-8d800b81146f | -7.0673 | -44.34271 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abe2d536-bcd7-3dae-955d-0498e24eba0d | -6.21418 | -43.91205 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c10131-92b0-33f4-b207-bad29681fbe4 | -6.59205 | -44.31915 | 2025-09-17 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52076ac9-0274-3b7a-a620-e6f10152f7d0 | -2.2602 | -47.84722 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81a89e76-0bbe-3f95-8f44-adea973f6af2 | -8.13616 | -43.64645 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54a4d111-66c0-349d-b607-91464ec35ed9 | -5.61293 | -42.89677 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fe8859d2-8bc0-37d9-bfcf-9de338711ce9 | -6.42359 | -43.30651 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca5d043f-5943-3e23-a076-092b92bcf7d7 | -4.99489 | -44.87529 | 2025-09-17 04:10:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15057745-3175-370e-842f-49f94adb06d1 | -6.29312 | -42.3836 | 2025-09-17 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c880304f-4fb6-3af1-b8dc-7d08260ed444 | -2.83185 | -48.65546 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 04181a8a-0668-37d1-b623-3599467df8e4 | -7.40025 | -44.6055 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09e3d76b-674e-34f8-8631-4a63673d71e5 | -7.66283 | -45.1417 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b39bcc-731b-396a-b263-d0d4184864fc | -6.35255 | -43.16346 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54e0c5bb-83e1-3bbc-965a-dcfce8e255b1 | -5.62784 | -44.83288 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| da08a658-ced6-3d90-b32f-4f6aa8e59230 | -6.35313 | -43.15979 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9dea6389-b510-3e88-b1fc-3f3a2f2f48d9 | -9.12331 | -44.88298 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 962e2cd5-f48f-3b03-ad74-888509f487ee | -9.09142 | -44.94366 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba087747-39df-39cd-a383-78909d05ce4d | -7.03228 | -44.16303 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9192bf6e-cab9-3c61-a981-5bcea1fb52f2 | -6.40957 | -43.34988 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e611ad3-7ccb-3d70-8dfc-6d30d8832061 | -7.59084 | -44.58459 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d549d3ed-fc05-3e66-98ed-f60d0fa6480a | -8.06673 | -45.45734 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89cdf833-5d9c-324c-a330-b5eaa45bf2c6 | -6.87495 | -45.19099 | 2025-09-17 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42ab11e1-ec73-3376-a108-9f2801c8bed2 | -9.54821 | -46.30507 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ace0b4f-4fba-33e1-9866-4a7e02d64e5c | -6.22639 | -42.02458 | 2025-09-17 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71d8f822-e981-319e-be0a-4846a8d0138e | -8.95916 | -46.2725 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb8b56aa-ca29-376d-9a1a-2fb514623510 | -7.26138 | -46.59782 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89cb240a-3c7f-3eb7-950b-02d6128f0df1 | -6.9601 | -44.53695 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e86ecbe-786b-3812-bb32-1fa88687857c | -3.23626 | -46.79603 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aa8a955-7dd5-3771-b2f4-bd3c8a27908c | -6.62799 | -45.59001 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fec886e-ac5f-3237-b6e9-837839980b76 | -5.60005 | -44.11327 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60a62a6d-33f6-3a35-b1f8-6e26968e5c2b | -7.87667 | -48.15466 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75d95020-51d0-3208-8cf7-f64de71c7fd7 | -8.149 | -46.75644 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28f88838-937c-3cb7-a628-be58839f21cc | -7.27188 | -46.58445 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 811dfa8f-02bf-356d-a8cd-e8ffb8871973 | -7.01599 | -41.45769 | 2025-09-17 04:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db9cee05-82b3-3817-9155-83d08c32ac74 | -6.70732 | -43.30203 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 453d55fb-a7f4-32e8-a887-bace1d0e35d2 | -3.8478 | -40.35502 | 2025-09-17 04:10:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b64d93d-101d-305a-af17-6aee233e63b6 | -6.4021 | -43.35253 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae693798-cefb-33ac-97e7-aa86b603ab36 | -5.09334 | -45.10139 | 2025-09-17 04:10:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6b1a57c-c75a-3b08-91f9-2e0fd5808100 | -6.33336 | -43.32696 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7dee36c-72dd-34a1-82ad-e4eabe0e87d0 | -6.3429 | -43.15816 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97e93003-e6a5-3cb5-b776-1c07d0edd63d | -3.23693 | -46.79196 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f274e43e-1fde-3a9a-9361-bf41bb37f2cc | -10.15787 | -45.2952 | 2025-09-17 04:10:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01ef71a3-249b-3a48-94e0-4848edd822e0 | -6.51805 | -45.75565 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 885c6142-15f4-39bd-803e-27d2f19cef49 | -7.00384 | -45.72119 | 2025-09-17 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74c03360-2a79-36e7-9834-cddb4ffbcca9 | -7.32666 | -43.9705 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0f9cb1b-47fe-3222-b62e-17795cffb836 | -8.90099 | -47.87844 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40e7b50d-a6c7-3a31-917e-1b765ec4718c | -7.60595 | -47.46821 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece59389-273a-3b45-82ab-4c5298bf9fb3 | -9.549 | -46.30044 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 203ee691-a095-346c-9a84-ec5e2dfd8c6e | -9.55085 | -46.29887 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bb6c4b4-e225-306f-88fe-185dfee2564c | -8.47378 | -44.72705 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4eb2fbf-2e94-3fb8-9583-4b05a9345b62 | -7.69421 | -44.48079 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ddc1625-635e-3a41-80d3-e87ab6672ce2 | -8.13855 | -43.63157 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2790863-4f09-3cdd-b5bd-dab70cc62332 | -9.09959 | -40.09978 | 2025-09-17 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 54eea3f1-84c1-3209-bbc3-bb023bfef9fb | -5.77241 | -45.90087 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650a8ecd-8a3e-3060-b68f-8b547cd9074f | -3.80032 | -47.57715 | 2025-09-17 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01a4a712-7565-328c-8513-4bf7848c2023 | -6.16691 | -44.52524 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b5fb95-aecf-3698-a8ad-302c7aa5298a | -9.07201 | -50.31326 | 2025-09-17 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16422192-f338-37e6-b793-ac588f653e3f | -7.26702 | -46.58881 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 50dd8a84-b10e-3426-8f04-4a9fd468ad01 | -7.61571 | -47.46178 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a654735c-e493-3a7c-aca8-2b1fc1cc0430 | -7.48054 | -47.39037 | 2025-09-17 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0d4a602-48bc-3fa9-92af-23914dbb9d5a | -5.76848 | -45.90024 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b56989b8-80a2-31bf-9d3b-0d9e777f8242 | -7.07547 | -44.55947 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e19d3831-4fb8-3389-bfcc-6c61b0cede43 | -5.61575 | -42.90093 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3dce03e8-7985-396a-a155-746428f33750 | -9.24261 | -45.64849 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d9450b-0e7f-3c06-a5cd-09d37d4113aa | -6.42172 | -44.01214 | 2025-09-17 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d83741-6777-3ead-bd5a-01b592e9c4ea | -5.60361 | -44.11384 | 2025-09-17 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b4ff77c-6dd6-3671-8cca-8b093e31488a | -9.09564 | -44.94025 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 236ce300-0b4d-3c0a-8886-ecb8eb033bcb | -5.47401 | -45.34928 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9dbf38e-79ec-3d46-b6c3-32cb1810e66c | -6.48032 | -46.00331 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85d3bc9f-dca3-3a44-ae68-1c22920fd750 | -6.96716 | -45.5443 | 2025-09-17 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4614054d-64f4-3be8-aef9-24ee369e185d | -6.97866 | -44.53592 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2227141-1178-3ad0-9b81-f3ad80536aea | -8.90453 | -47.88325 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fecca391-758c-3d11-a099-6e603d5b290c | -5.61517 | -42.90456 | 2025-09-17 04:10:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d6591ff1-d064-37df-a841-3323b6399b43 | -6.21355 | -43.91597 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90abf336-0275-345e-9c13-40dd2e97c42b | -8.16408 | -46.76454 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2487a675-5e60-368b-83f3-d23e03a3de30 | -6.04122 | -43.14466 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5af9612f-5e11-32c4-8739-8e17c2a974f5 | -7.06376 | -44.34208 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8599cd27-8212-3619-a58a-e2862a936464 | -9.74313 | -47.86037 | 2025-09-17 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f6dbee0-82e6-3e16-8339-5547789e9d31 | -5.34721 | -44.81887 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d178428-e904-3457-b1d6-5f7e19717b36 | -3.21795 | -47.12807 | 2025-09-17 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbc056f1-90c8-3ab2-b614-a6a0e8b1ea83 | -6.86956 | -38.4353 | 2025-09-17 04:10:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 29785471-3aa2-36a3-9007-06c2484f0ddf | -6.40819 | -42.66441 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4a888d80-e4c0-36df-96fe-81068e56b1ba | -7.82447 | -46.15631 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f7b5f29a-5830-365e-a4f6-698911987a0e | -5.63225 | -44.82909 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a3bd05a-672a-3ec2-aae2-5e8f12f4b2a7 | -9.06802 | -44.95222 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b4681c-6a45-33eb-be40-50e85b00c95b | -5.66661 | -45.04488 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4850bf16-d4d6-3a6e-8859-e03b70771674 | -8.91922 | -44.4757 | 2025-09-17 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1beca583-658d-3fcc-a47a-3aeb99c56571 | -5.91903 | -45.91238 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d510f7e4-24fe-3f13-80eb-dc75597062fb | -6.98059 | -44.45686 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e253843e-10e5-3a80-bb96-6250528e80c5 | -5.5233 | -42.18924 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0928980d-1295-31f2-bf24-e02551904482 | -6.451 | -43.31086 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a36f8ce1-01ab-325d-9e58-c742bafe0894 | -6.34395 | -42.95641 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0bfe86f-7408-3569-81bb-d27d7b14ee41 | -6.61049 | -45.57757 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af89138d-0757-388e-a409-fc88c90948ec | -9.04603 | -44.88634 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79e63eb2-4561-3d2d-9043-b4d128c00bba | -6.21291 | -43.9199 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc9cbb53-36fa-32a7-8140-0f8657d342f8 | -9.05025 | -44.88294 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e33bfce-91e5-39a3-af37-896fa1c1d99a | -6.03899 | -43.13668 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b30c34a2-f3d4-3d98-a6e8-8a96e63f02f5 | -9.06874 | -47.02281 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 795cdee9-6ae4-3752-bbba-e249a62fd1a7 | -6.70792 | -43.29835 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60b8f782-2e4f-370c-9dea-44d367bea4e0 | -6.5259 | -41.81853 | 2025-09-17 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
