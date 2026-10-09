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

## Dados Diários - Página 235

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 729037ef-c7fe-30ab-b42b-92ab844ff64b | -9.0147 | -45.9434 | 2026-10-09 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 28aaa8a2-8ef0-33b1-b2fb-c70180a51af2 | -11.8499 | -43.5835 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| d4fed267-4f08-33d3-a2ef-8c884c47424e | -11.2259 | -45.3064 | 2026-10-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 691ec691-9b31-3afd-9f21-7d663bfe0674 | -12.2346 | -57.1071 | 2026-10-09 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| f9028709-552f-34e5-9d5d-5085f071df35 | -9.0359 | -44.3885 | 2026-10-09 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| aca840b6-2a4f-31f3-a15b-0ec44ef12932 | -11.6562 | -43.6846 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| dda99b18-499d-315c-a047-177c01efa142 | -10.4901 | -47.3201 | 2026-10-09 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 5900e278-5e6d-36de-9b53-34e50e8b6cb0 | -8.9687 | -45.1542 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 294bb26b-7fd7-322d-b5e6-57fde69779b5 | -12.2343 | -57.1271 | 2026-10-09 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e587bec2-2d84-397d-8d72-59190bff7c07 | -12.0058 | -43.464 | 2026-10-09 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 474.5 |
| 18490e6f-b017-39c5-8277-659e0f5488e9 | -8.9775 | -45.9023 | 2026-10-09 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 82c8d925-0b3b-3b5c-9189-0945718bcb32 | -11.5797 | -43.6728 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c81be78a-ef54-37c8-9fe4-71d72184618c | -11.6557 | -43.7083 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e4ae768e-ce53-35a8-811a-7d3b479eb8ed | -11.8302 | -43.6103 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6f5b6de1-328a-3852-97ff-936d832d9477 | -9.1012 | -45.1393 | 2026-10-09 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 64d87bf9-3ec5-321f-bc4f-eded1d347eed | -8.9693 | -45.1084 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 55497e26-09f7-36ad-bc69-8fc6a2c1a8e2 | -8.9491 | -45.202 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 80aac0d0-3d54-3c25-93d4-e57c4fe13f89 | -11.2263 | -45.2834 | 2026-10-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 2cef28b2-aff5-34d3-b0ec-125054c051d6 | -11.8307 | -43.5866 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.4 |
| c82976ab-16c8-3d28-82f6-34ac268cb355 | -12.0063 | -43.4402 | 2026-10-09 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| be082768-ef36-3e83-bb83-c6956afd0995 | -11.5985 | -43.6935 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 44991285-0d7a-34df-b415-fc0961342bf7 | -16.1136 | -43.4052 | 2026-10-09 12:30:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8451653f-07e4-338f-955f-def3bd1b6aff | -9.1297 | -45.8179 | 2026-10-09 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2e95c710-4424-3325-b766-3aae9e98c3e6 | -10.917 | -45.5317 | 2026-10-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 300.1 |
| e6835da0-67aa-30ad-829e-233089258aaf | -8.9684 | -45.177 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 90b5188a-c257-3037-b1a5-3bfa02c77fd2 | -12.2348 | -57.0871 | 2026-10-09 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 1a2fc1b1-b332-3bba-88c4-4ee5e6332f7a | -8.9113 | -45.2062 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b0adfc5a-4615-34cd-bc6a-5632784b133a | -10.8598 | -45.5394 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 221cedd1-06ab-3bc3-b247-b1718be4ee60 | -11.2068 | -45.3091 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e1417080-820c-3a89-9361-88b7895f4738 | -9.2973 | -47.4092 | 2026-10-09 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9b92de79-5b48-3018-8a71-18bcd89a5611 | -9.8439 | -47.483 | 2026-10-09 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 677c6b20-dba8-3c12-82b7-9cc1c4f41605 | -11.2259 | -45.3064 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.8 |
| a1e875e6-72ea-3d4f-88dc-a4cf55bda7d3 | -18.3335 | -42.3598 | 2026-10-09 12:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| fd3b34fc-aa58-3f6a-abbb-f24c22b22782 | -9.297 | -47.4313 | 2026-10-09 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d2403908-2442-3d34-b86b-409af35f7cf5 | -12.2343 | -57.1271 | 2026-10-09 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 33ea67e4-cff6-3ec2-8b72-e65fe5d51808 | -8.9494 | -45.1791 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 163.1 |
| a3c4cf56-af8e-36a5-80a5-22f91b29623f | -9.2781 | -47.4333 | 2026-10-09 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 5e1b3549-6be7-370f-a82c-54898254aebc | -11.5801 | -43.6492 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 20c86277-08af-38b1-864c-d46fa2d6100f | -11.6562 | -43.6846 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 62782c5d-e881-33de-96c7-3b3989c2c758 | -11.5985 | -43.6935 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ccfd33a4-ecc2-3547-833a-63d51593f9e5 | -11.8302 | -43.6103 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| eae672c3-26fe-3f77-95f2-ea8c91587137 | -9.3101 | -46.4509 | 2026-10-09 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| a82da8df-1c60-311c-9b12-2f24f2dd15da | -8.969 | -45.1313 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 226.4 |
| a2ec53ba-6c7c-3961-84cf-b09b83043eac | -10.8789 | -45.5368 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 882c6b97-25f1-3175-a6e7-75fcd96d0218 | -10.4901 | -47.3201 | 2026-10-09 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 86e6e3b7-d5f1-332a-ae12-42c929ba2d6f | -11.0562 | -44.0561 | 2026-10-09 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2960e27d-a150-3e59-a249-79e0055012aa | -8.911 | -45.229 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| ad1d86ed-5dfd-3dfb-b2b8-29146d018389 | -11.3371 | -46.6547 | 2026-10-09 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 954b01c2-12a1-324b-95a8-b06b4ec62493 | -11.1051 | -45.689 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 0f860da3-94b3-3394-9871-4c45916486e1 | -9.1297 | -45.8179 | 2026-10-09 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| d1e13512-bff5-3ce5-9fcf-02a70a224049 | -8.9302 | -45.2041 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| a7968698-5d57-3a84-9f6c-74ff8b5a544b | -11.1242 | -45.6865 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.8 |
| ff9fb6b0-8e9d-3092-965a-3c8068c50204 | -11.2263 | -45.2834 | 2026-10-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 270f82dd-c720-378c-8811-de30f87e01f8 | -9.1012 | -45.1393 | 2026-10-09 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fff3ec5a-340d-3cce-9f23-6f274ef9308f | -8.9964 | -45.9002 | 2026-10-09 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 2336515e-2b6b-3039-9af3-986b2317c135 | -11.8499 | -43.5835 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| f53270eb-de3c-322e-9976-018a1d08c57a | -16.1136 | -43.4052 | 2026-10-09 12:40:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 02734482-ac02-353c-86d1-6fe6b171fd59 | -11.8307 | -43.5866 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 1bd5c0d9-dc01-374f-9017-f716b583e9cb | -8.9687 | -45.1542 | 2026-10-09 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| fc9c3e60-879d-35b7-9a98-edb9126dd5ad | -13.1824 | -54.3778 | 2026-10-09 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 5dcf34c4-1656-3edb-9b6b-932be223b305 | -12.2346 | -57.1071 | 2026-10-09 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| acf9e447-e07a-36cc-9320-d9042a0b3b74 | -11.5989 | -43.6699 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| ff703cee-8a0b-3a30-b713-671df6e8d36a | -11.4131 | -46.6671 | 2026-10-09 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| ce457849-8f61-3c29-9019-3477f61e182a | -11.4128 | -46.6897 | 2026-10-09 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 30e39167-f576-3022-965a-e34c554b5874 | -13.1639 | -54.3385 | 2026-10-09 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| dfd9f5f7-6fa1-3309-a102-097ed224d753 | -11.6557 | -43.7083 | 2026-10-09 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 14e59d50-80e4-3958-b88f-c74a9cfcd754 | -13.1827 | -54.3571 | 2026-10-09 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 34c6ad90-9a2e-3bc6-be9a-b3556b27d434 | -11.7674 | -44.9522 | 2026-10-09 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8d82a86c-f80b-3d80-a7a7-264eedc48b46 | -13.1636 | -54.3591 | 2026-10-09 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| b320ffdd-f9b6-3c40-9745-e676155b16c6 | -8.9775 | -45.9023 | 2026-10-09 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 875e874b-565b-3677-ac73-f93b5252864c | -10.9174 | -45.5088 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 11d7cd2a-a0ff-3554-bede-29254d1e120f | -11.5998 | -43.6226 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| b25c04ca-f894-364d-89cc-8356a357c023 | -11.7674 | -44.9522 | 2026-10-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4792df73-08ba-3182-aabe-102b069c43ed | -12.0058 | -43.464 | 2026-10-09 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 807.9 |
| 610b7cb6-5d6c-395a-97cb-4714c08382b9 | -12.2346 | -57.1071 | 2026-10-09 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| da2f1733-d8c6-3373-804e-05148a1b152a | -11.6194 | -43.5959 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| a4efd067-3022-394c-a847-09b711e5612f | -8.9494 | -45.1791 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ac360e17-89ce-362d-90db-3ca8e1fbdb4f | -12.2343 | -57.1271 | 2026-10-09 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2c1cfcec-d80f-3ef5-862d-3806549e650b | -11.5985 | -43.6935 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 8604de81-2ed5-33bc-bf56-4ec8ff028bc2 | -11.8302 | -43.6103 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b1f24188-7ac8-37dc-9f36-6dd9eaf9d75a | -9.3101 | -46.4509 | 2026-10-09 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| b9ef836f-7fec-3bb9-b0b0-dbca5ef8b316 | -11.8499 | -43.5835 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 21089320-924d-3b34-82b2-27dfe89779ae | -11.0562 | -44.0561 | 2026-10-09 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| e914d855-b91d-3ffd-846f-2e9ace8e3863 | -11.0745 | -44.1003 | 2026-10-09 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 115090dd-1ef4-3343-b7ea-6950ac439a8d | -11.2263 | -45.2834 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| ed0b0c77-3dfe-31d5-aeb6-09691f6abf3e | -12.0054 | -43.4878 | 2026-10-09 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 276.3 |
| 391d34a8-e3e8-3963-bb39-dc35caf53d9c | -8.9693 | -45.1084 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 930b495a-72d1-3d5c-9493-6258801a5692 | -8.9687 | -45.1542 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 579ccbcf-cf85-3c0b-bd1a-64adf4b2dd10 | -10.5281 | -47.3156 | 2026-10-09 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| eca2c58b-0820-310f-a570-9f8c645e14c8 | -8.969 | -45.1313 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 83bc1361-559b-31c5-aa3b-ef4dc7f53b7d | -10.8789 | -45.5368 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| ab6989b8-6de7-30fb-ab07-1d3c1a8c5c8c | -12.0063 | -43.4402 | 2026-10-09 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 374.5 |
| 414ee903-4477-30d1-b7ef-1ca0c80b37cf | -12.2348 | -57.0871 | 2026-10-09 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 50dd1de1-7e7f-3580-9c7d-66eb83fa52e4 | -11.8307 | -43.5866 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 6260f5cd-796d-35d0-88b8-520c000bd41e | -18.3335 | -42.3598 | 2026-10-09 12:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| 1f1ec330-3c68-3c8e-a105-5adc245a5652 | -10.3161 | -46.2668 | 2026-10-09 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 3db3e5a8-9255-30fc-9221-614d41599bf3 | -9.1297 | -45.8179 | 2026-10-09 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| a40a59fe-22c0-3883-9564-f47cff582980 | -11.5801 | -43.6492 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 941aa192-4efb-3470-bc0e-4e9dcd74f952 | -11.5993 | -43.6462 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 0853e9e7-33be-3930-89e6-c84d92f2d468 | -11.6562 | -43.6846 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 268.4 |


[Clique aqui para ver as próximas entradas](README236.md)
