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
| 0ad4eae7-d427-3ad2-9603-3d614eab3fec | -6.8389 | -56.3949 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 848e695d-9117-3b28-bc42-78a2091f8744 | -13.9541 | -58.1162 | 2026-08-09 02:20:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6e9b2ded-633f-3112-a6bc-0f2db92cd8a4 | -6.8203 | -56.4155 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1366da88-2afa-318d-9a90-269ddbbd040f | -18.6332 | -49.8517 | 2026-08-09 02:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| 4c2c4e16-f406-3281-8001-b7cfeb16dbd9 | -6.8387 | -56.4344 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| dde54b91-053b-3099-9459-1e14f5424c2f | -13.9541 | -58.1162 | 2026-08-09 02:30:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f774afeb-6422-338b-8a30-6b528bfe892c | -18.6533 | -49.8478 | 2026-08-09 02:30:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 4f9b6511-bac7-38cb-bd3e-70e4b6bbd869 | -6.8202 | -56.4353 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| da4dca1e-5de3-3bf0-99b9-11d84398c367 | -6.8387 | -56.4344 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ec966dd1-7d33-3e9d-92ca-e1a6dd765692 | -6.8388 | -56.4146 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 01e9ab6f-34dd-3699-8a7b-e31fd10c3ae8 | -6.8389 | -56.3949 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c214ccee-2a64-3d54-af9c-a686ec0965fb | -6.8203 | -56.4155 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 99e91034-6460-3975-8c1d-574c0f59f1db | -6.8574 | -56.394 | 2026-08-09 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 752cbf2e-8908-331c-8125-6e1b6190fc01 | -19.0926 | -48.3106 | 2026-08-09 02:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 541b8502-2a35-34fa-a1b4-88efc2487ef0 | -19.1128 | -48.3063 | 2026-08-09 02:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ae34cc94-8925-3b29-b25b-765e2a985f37 | -13.935 | -58.1179 | 2026-08-09 02:30:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f1f16d3b-27ad-3b5f-aba2-8c377f2a866f | -13.9541 | -58.1162 | 2026-08-09 02:40:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a36cb538-8caa-3849-9961-8a5141f354e2 | -6.8388 | -56.4146 | 2026-08-09 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 286633eb-22e1-38fc-8de5-34726b766403 | -6.8202 | -56.4353 | 2026-08-09 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8607514f-0c33-3e65-869b-934964635b5a | -9.4582 | -40.3143 | 2026-08-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 1180fe82-0398-3053-aa68-2f26d8be1151 | -6.8203 | -56.4155 | 2026-08-09 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2c49ccf0-b855-3b09-8a5e-c13bb7fb4493 | -9.4773 | -40.3116 | 2026-08-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 954785e0-dc6a-3ba6-8854-622962db8492 | -6.8387 | -56.4344 | 2026-08-09 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2292ba1d-3819-3a90-822a-027f1d307670 | -9.4773 | -40.3116 | 2026-08-09 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 542964a9-090b-3715-804d-3f3095d4e47b | -19.0926 | -48.3106 | 2026-08-09 02:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e8409333-d5a2-3db7-b6ed-b7a8c2e7d506 | -6.8388 | -56.4146 | 2026-08-09 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 6f5d7971-ee4b-3602-8cda-26005afaebdb | -6.1476 | -57.7215 | 2026-08-09 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7904bd8c-e92f-3fa9-96cb-0b12a10fee46 | -19.1128 | -48.3063 | 2026-08-09 02:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a33125f3-57fb-3de2-84f9-a7fd399bf790 | -19.0932 | -48.2876 | 2026-08-09 02:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 80a63fb8-6241-31aa-bf95-338b9c389a95 | -13.9541 | -58.1162 | 2026-08-09 02:50:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d016157b-a250-37ef-a349-73378aad9059 | -6.8202 | -56.4353 | 2026-08-09 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dfb05c47-72d0-3b8e-be8c-70841711d8b2 | -6.8387 | -56.4344 | 2026-08-09 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 21d5eb94-2668-396e-b1c7-8f9f8d25d030 | -7.5924 | -45.2044 | 2026-08-09 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 287acd7c-6f14-35b6-822f-ddfd99527aa8 | -18.6332 | -49.8517 | 2026-08-09 03:00:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 343d4135-be2b-3560-a3a4-6873e34d85ef | -6.8388 | -56.4146 | 2026-08-09 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| b41d61ea-ad4e-36eb-9dff-920b9f21a8d5 | -6.8202 | -56.4353 | 2026-08-09 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 92ed539a-4423-3cff-ae33-7db73e80d092 | -18.6533 | -49.8478 | 2026-08-09 03:00:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.5 |
| 68bcd9b3-a1d2-3fb6-9738-f080a256077e | -6.8387 | -56.4344 | 2026-08-09 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 21d5243b-07e0-3e94-a548-3f70f64a23fb | -9.4582 | -40.3143 | 2026-08-09 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 8211589a-1058-3407-929d-2b10a0b86708 | -6.8387 | -56.4344 | 2026-08-09 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e09ee39f-a280-30ab-85e9-f08ab2bdcfa7 | -6.8388 | -56.4146 | 2026-08-09 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 18a94fd6-5229-3d90-8981-2abed675458c | -6.8202 | -56.4353 | 2026-08-09 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 37414de0-f589-35fd-99e6-3ce16cc5c57d | -9.4582 | -40.3143 | 2026-08-09 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 3a71f51d-8a0a-34ae-9840-4b7c7b58ae1a | -9.4773 | -40.3116 | 2026-08-09 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| a11b89f6-1f2a-3146-af5e-f8a62897c5bb | -6.8202 | -56.4353 | 2026-08-09 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 72139239-c3b7-325e-893f-9a3e6a5c060e | -6.8387 | -56.4344 | 2026-08-09 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 39d9a9c1-e5ed-348e-80c9-c3f8792d974d | -6.8388 | -56.4146 | 2026-08-09 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 13802878-25ac-377f-913a-a7e66089f8c6 | -9.4769 | -40.3365 | 2026-08-09 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 9c063ada-47f8-3e71-8d16-442ba3d5249e | -6.8387 | -56.4344 | 2026-08-09 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d144697b-7670-3241-86c6-b26938cc2a0c | -4.2798 | -48.5672 | 2026-08-09 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 81679f2b-c233-3b3b-956e-089153a37428 | -9.4582 | -40.3143 | 2026-08-09 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 55811b2a-eb32-38cf-8cce-4d04d631f01f | -9.4773 | -40.3116 | 2026-08-09 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 173.4 |
| 1fcf52df-de73-3040-ac60-fa0406df6b4d | -6.8388 | -56.4146 | 2026-08-09 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b11c8d68-bf5c-3e4c-90cd-0df8851b2fda | -7.57179 | -44.39127 | 2026-08-09 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 617f3f4e-b510-342e-934a-0873655d1892 | -7.58977 | -45.21421 | 2026-08-09 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f8e00ed9-d80a-384c-ba5f-d4448aee9179 | -6.98411 | -42.91126 | 2026-08-09 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 89e5ab69-1890-3ac4-be1d-26854fcc7a94 | -6.98673 | -41.47823 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 775a39f6-6ec3-3d3b-adca-5bf3faab5e24 | -7.58657 | -45.21274 | 2026-08-09 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 96e7ede5-cfed-358c-8ba4-b8e022544cdf | -6.97826 | -42.91009 | 2026-08-09 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 291177d3-b68e-3cd3-b6e8-fd634bc2febf | -6.93239 | -42.43732 | 2026-08-09 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8978fe1-2c90-3863-b39e-eb44a16decad | -6.87386 | -44.92583 | 2026-08-09 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 335854d5-1b31-3acf-a64f-4458f156259d | -6.97228 | -41.49707 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5124a63a-ce2a-3d62-b698-6d17c44b18c0 | -6.92819 | -42.42813 | 2026-08-09 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 297830a7-c3b6-3460-a960-d26671df2da5 | -6.88041 | -44.92752 | 2026-08-09 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 01cc73de-b19e-3814-8285-4285b18e7508 | -6.98135 | -41.47748 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b795b96b-f68c-34ad-959c-46b446d659ed | -6.96147 | -41.50925 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b158b03-a953-312a-a71c-f3cf8f66949b | -6.96447 | -41.50969 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77991d86-1ba7-3a82-a8db-557fb0300bf0 | -6.96205 | -41.50591 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ec00aa8-229b-3694-837c-799cca527915 | -6.03235 | -35.51045 | 2026-08-09 03:30:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b402794-022d-33c0-aebd-8b2de386b97d | -7.57277 | -44.38598 | 2026-08-09 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceacd5da-8a7c-34e7-93fc-cebeda2c04c0 | -6.87652 | -44.9276 | 2026-08-09 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aeffc862-fdb5-352a-8e7f-952f15c93ec9 | -4.90466 | -43.47218 | 2026-08-09 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0f8b5fc-ffdb-3b63-9f58-0fb7daf8cc34 | -6.92746 | -42.43211 | 2026-08-09 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6c7160dc-e6cb-3aff-99e0-becf30ff9925 | -6.03262 | -35.51207 | 2026-08-09 03:30:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1797f3e-4508-3cae-ab6e-e59dd12b1fe9 | -3.12153 | -40.10818 | 2026-08-09 03:30:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0b56025e-7f08-35a5-9e49-f6cbbece6c7e | -6.96508 | -41.50631 | 2026-08-09 03:30:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da1390bc-bf2d-385b-b9de-793f73bfe489 | -7.58308 | -45.21306 | 2026-08-09 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5cf6338c-512c-32a6-8fd5-1ea1411c249d | -7.28904 | -38.93643 | 2026-08-09 03:30:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b9fb863c-34e2-3ebe-bc42-aa3134395b0e | -7.57985 | -45.2117 | 2026-08-09 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc254d0-d94a-3d8d-80d7-24b2c44fea04 | -6.9849 | -42.90691 | 2026-08-09 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e769860-5b98-3e6e-81e3-5568bd9dbb02 | -14.10545 | -39.72714 | 2026-08-09 03:32:00 | NOAA-21 | IPIAÚ | BAHIA | Brasil | 2913903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ddd22473-aa1f-3d2f-8ea6-784d681281c6 | -12.11954 | -47.22654 | 2026-08-09 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0951fce4-e946-3df8-9b2b-6c530de99deb | -10.88989 | -37.0789 | 2026-08-09 03:32:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14d44453-b93d-3866-bb71-959f3df77a2a | -14.90955 | -48.23973 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 47411e0c-068f-3075-902f-471eaa7e4081 | -9.4654 | -40.32174 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d7a03c5e-bbb6-3721-bc95-4d56251cbf16 | -10.49014 | -46.62455 | 2026-08-09 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4337b82c-2a84-37b6-a3ca-74997484cca2 | -9.46663 | -40.31884 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 936e75db-976a-3262-89fa-c1f44cf7c3dc | -14.90477 | -48.23865 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8dae889-6b93-369e-98c5-acaad027e282 | -13.53089 | -44.03662 | 2026-08-09 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1305fc31-575b-3fbb-9305-6ddd81599ad8 | -10.49069 | -46.62395 | 2026-08-09 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4d1e3153-774b-3ca6-81e3-3da00797bda0 | -11.03872 | -44.2781 | 2026-08-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd0338fe-638d-3260-b539-912fd1ad8fd3 | -14.91109 | -48.23296 | 2026-08-09 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4354a7fe-2bdd-373e-93dd-ed779212252a | -9.46951 | -40.32996 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.8 |
| b308784e-f7dd-3577-a429-829b76e72875 | -9.46718 | -40.31151 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.3 |
| dabf7407-0d63-3a5e-910a-daaa07f51299 | -9.46755 | -40.31375 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 854597f0-6c4d-3fbe-8498-9354caa7effc | -9.46629 | -40.31662 | 2026-08-09 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 5ed8a2ce-8b3e-3f97-ad01-dc6b37998b45 | -10.90726 | -45.12471 | 2026-08-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a064137-5873-3011-ae90-b9c0f5d79ed8 | -15.40682 | -41.8013 | 2026-08-09 03:32:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7188b522-2ac6-3a9b-ad74-672e6e3a4009 | -15.87716 | -43.33228 | 2026-08-09 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b3d0e2-caa7-32dd-97b6-37d8d4249a7f | -10.48924 | -46.63113 | 2026-08-09 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README6.md)
