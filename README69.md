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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8dbdeba-4355-31c6-9438-2e35f10e9b5b | -4.4246 | -43.4038 | 2025-11-16 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| e188faea-9b65-3672-b26c-a924a480e075 | -6.7013 | -40.7962 | 2025-11-16 13:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 58fbe711-c10b-3144-a8e3-430c1cc037f1 | -9.7246 | -43.9566 | 2025-11-16 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 318.2 |
| 01931437-2264-3949-8e87-7b320208cdbd | -4.019 | -48.8147 | 2025-11-16 13:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 364795ba-ad76-3f0f-af26-05d32f9c0651 | -3.2304 | -43.3486 | 2025-11-16 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 2cd919bc-da81-31f8-ae62-9a77fff74d51 | -8.0573 | -45.6583 | 2025-11-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 28e734d6-1118-336d-a759-8e2a1d23bbf0 | -9.7432 | -43.9775 | 2025-11-16 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f580fc35-a31d-3304-9eba-b15696f47395 | -4.4059 | -43.4049 | 2025-11-16 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 8ece6468-6522-376d-a3e6-2a15b09305b4 | -6.2391 | -41.7115 | 2025-11-16 13:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| a317a090-f4fc-36f2-a0ff-fc739b00b77a | -3.5568 | -41.7314 | 2025-11-16 13:30:00 | GOES-19 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 2378e4e1-f664-376f-9f4d-33e0bd7cadc6 | -9.7242 | -43.98 | 2025-11-16 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 0808eb33-92ed-3174-9b29-ded710cf3aed | -6.2389 | -41.7355 | 2025-11-16 13:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 44615ae5-4598-31cc-88f0-60a20afd6770 | -4.4246 | -43.4038 | 2025-11-16 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 0e83cd2f-d132-346d-9812-67b62e45b42b | -5.0083 | -45.2922 | 2025-11-16 13:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 49ce69f6-3d5d-3ba1-bfd8-9ffbea29ee53 | -8.6814 | -45.4587 | 2025-11-16 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 55b874df-fb44-3167-b66a-998ccda8a877 | -7.1931 | -39.2058 | 2025-11-16 13:30:00 | GOES-19 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 65.4 |
| c1bf60b2-b750-388b-9600-5cd0397eb7fb | -2.5238 | -47.8115 | 2025-11-16 13:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 805a003b-fdd6-3feb-971f-64913913bb2d | -6.6824 | -40.7981 | 2025-11-16 13:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| ff143d17-98a0-35fa-b93e-3645a493e5dd | -2.4201 | -45.7015 | 2025-11-16 13:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3300e828-547d-3840-8099-1a4daa6a93c5 | -8.6811 | -45.4814 | 2025-11-16 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 96733bef-306a-3353-a944-fd18ac4bab5d | -3.2117 | -43.3494 | 2025-11-16 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| f059fe1d-1de8-35dd-b640-7effd44c4f41 | -9.7436 | -43.9542 | 2025-11-16 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 8a2ba50a-cd53-3f97-8ef2-8d34555a38a8 | -4.019 | -48.8147 | 2025-11-16 13:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f1220f4f-c990-37a9-8f1a-105c4deda740 | -3.2117 | -43.3494 | 2025-11-16 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 6f1c35a7-f019-3dbd-9a60-cbc60b6fff9b | -3.8436 | -40.7759 | 2025-11-16 13:40:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 103.0 |
| f72642eb-9d56-3175-9446-9b92139751d8 | -6.7339 | -42.9498 | 2025-11-16 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 1ca15612-1ab2-392e-97fc-07332d8e6746 | -4.4246 | -43.4038 | 2025-11-16 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| c7e77d59-f276-383a-a419-c2ca0b51b9f6 | -9.9969 | -44.7797 | 2025-11-16 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| d0ead060-ee82-3b2f-9a3b-b34c1d582618 | -8.6814 | -45.4587 | 2025-11-16 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 227.8 |
| e915cd66-ec22-3d53-96e1-94b4204bdad6 | -3.1559 | -43.3285 | 2025-11-16 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ab868692-d08b-31b6-ac9e-dec042603a81 | -10.0159 | -44.7773 | 2025-11-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ffa6bb0e-f7eb-3a71-a0cb-f61642742bc7 | -6.2389 | -41.7355 | 2025-11-16 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 8e10d6bb-5d7f-3a01-ad25-3a133456789e | -6.3705 | -41.7477 | 2025-11-16 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 8aeafcb1-9ba2-3e68-abef-65664651c81a | -10.1722 | -44.5032 | 2025-11-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 35d3bd11-644b-3965-a7ad-cc662e52d17c | -9.0327 | -46.0091 | 2025-11-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| fe727442-e9c4-3a68-b73a-7f46209d7fa2 | -10.1718 | -44.5264 | 2025-11-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 90acef10-1ff2-3a78-9de0-3193479cf076 | -10.1245 | -43.9046 | 2025-11-16 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 427.3 |
| 65d7fdf4-1e54-3544-b869-fd9b75964bb0 | -9.9377 | -44.9252 | 2025-11-16 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 9ebd37eb-02d8-3359-b775-427b185b9969 | -9.7436 | -43.9542 | 2025-11-16 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| fe39abaf-0581-325a-b2cf-052c934c3a46 | -6.2391 | -41.7115 | 2025-11-16 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 204.0 |
| 3e6a0a99-b839-3f7f-9157-6731f8f16e4c | -9.7432 | -43.9775 | 2025-11-16 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 17cc1d7e-b84b-3638-b414-00c9ad78a44e | -9.7242 | -43.98 | 2025-11-16 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| aac412ef-4e7e-3338-989d-ae0b8901f4b5 | -3.2304 | -43.3486 | 2025-11-16 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d8e89cda-92b0-38e4-8581-d96435f80a2f | -4.4059 | -43.4049 | 2025-11-16 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 8df91022-87f1-3e6b-a879-e7d3fbe42449 | -2.5238 | -47.8115 | 2025-11-16 13:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3332bf18-5831-37b4-9b60-0e61efc0fcf7 | -6.258 | -41.7098 | 2025-11-16 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| eb512bcf-5ecd-3121-ba28-b6e2c6050e29 | -10.1912 | -44.5007 | 2025-11-16 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 8c380571-9cdf-3d34-a50a-9232bf3dd887 | -8.6811 | -45.4814 | 2025-11-16 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 5d09f866-645d-39df-ac08-fe00ef95d6b8 | -9.7246 | -43.9566 | 2025-11-16 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 302.8 |
| df3f1060-b575-3000-a4bd-3a34b303384f | -9.9972 | -44.7566 | 2025-11-16 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1c63be22-9169-3f4c-ac8a-7c9430f02f6b | -8.6808 | -45.5041 | 2025-11-16 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 2977be70-3b81-3d4b-b510-71439207670c | -2.4201 | -45.7015 | 2025-11-16 13:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f73db837-a4d5-3385-9711-58a51a74f4f5 | -9.9187 | -44.9276 | 2025-11-16 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a13425eb-d3cb-3206-921a-f08f92fc1324 | -10.1055 | -43.9072 | 2025-11-16 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8e34ba34-8281-34f3-9e87-8df91198c7fd | -6.2389 | -41.7355 | 2025-11-16 13:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 29dcc855-87a0-3595-995f-980510944260 | -9.9187 | -44.9276 | 2025-11-16 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 357ad0f1-ff6a-3944-a561-20b633890318 | -3.6088 | -42.4176 | 2025-11-16 13:50:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| f4c94801-3d5c-37a0-b119-53888b3d08c6 | -4.019 | -48.8147 | 2025-11-16 13:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 45227815-c97e-3dc7-950d-1732c3627e9f | -9.7532 | -47.2049 | 2025-11-16 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b470fdf6-3dec-393a-9d42-fdbeed81834d | -10.0159 | -44.7773 | 2025-11-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5ff90fe7-4692-3ef4-bc36-ee07f0202f19 | -6.7013 | -40.7962 | 2025-11-16 13:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| c614e625-b4c1-3e72-a1b8-283a31715d05 | -10.1055 | -43.9072 | 2025-11-16 13:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| adbd920a-69d0-3287-b1bf-53f5fc86c932 | -8.6641 | -43.9211 | 2025-11-16 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4ad79b54-df48-3239-a358-3b6817862e0d | -4.4059 | -43.4049 | 2025-11-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 1f4b33e0-7410-3a83-9a03-6826482ec7c0 | -6.258 | -41.7098 | 2025-11-16 13:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 20882f4b-2063-30d7-8198-9bfa95df0031 | -9.9972 | -44.7566 | 2025-11-16 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 0383c436-0e45-3342-9fd1-12f5ff002d42 | -8.6814 | -45.4587 | 2025-11-16 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 51bf61a7-98ac-3656-8533-f255c5f6f7c2 | -4.4246 | -43.4038 | 2025-11-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b562e88f-1d7a-3a20-b712-822c4f8555bf | -10.1912 | -44.5007 | 2025-11-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d500cb45-6776-39ee-9aa0-8e1148da4614 | -9.9969 | -44.7797 | 2025-11-16 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 42538b21-d02c-3e39-a57d-2634c7ec21dc | -9.7246 | -43.9566 | 2025-11-16 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 234.3 |
| 061bc9e3-f03b-3af8-8c74-0ed68d0fc440 | -10.1722 | -44.5032 | 2025-11-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 34fa06e3-b61e-3d0d-9d95-6f90908c855a | -9.7242 | -43.98 | 2025-11-16 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 80b83d93-54b8-3bf7-8f5e-dad7d1102599 | -9.9377 | -44.9252 | 2025-11-16 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 17ca416f-23ea-382a-8935-4a58c668d36e | -3.2116 | -43.3726 | 2025-11-16 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2ad6e14f-444d-3268-acef-eebad280baf7 | -4.4061 | -43.3816 | 2025-11-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0f87591d-2026-368c-bbc5-b082ba40188c | -9.7432 | -43.9775 | 2025-11-16 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3aa0db72-fd95-3152-a13b-8fbeecf51981 | -3.8436 | -40.7759 | 2025-11-16 13:50:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 141.0 |
| 61eff0be-845a-354e-8a8c-4114ba8da38e | -8.6811 | -45.4814 | 2025-11-16 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 201.5 |
| e335674a-e9ff-35e9-9f63-ef8afcc79aa2 | -3.2117 | -43.3494 | 2025-11-16 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5b8d18e9-3d2e-3c79-806c-09241fad6190 | -3.4647 | -41.4726 | 2025-11-16 13:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| e1de3661-274b-37fb-a3d1-82e35cd3479e | -2.5238 | -47.8115 | 2025-11-16 13:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 757f48e7-8547-37b6-9cbb-d759177f604b | -6.7339 | -42.9498 | 2025-11-16 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 9e86b490-9527-3c58-976c-ce8a14f9e855 | -8.3067 | -43.798 | 2025-11-16 13:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 46c9e79c-1e28-36be-9d93-6a2e7fb49404 | -6.3705 | -41.7477 | 2025-11-16 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 222.9 |
| b2a852b8-7ea8-3069-be1d-6f537debf329 | -6.2391 | -41.7115 | 2025-11-16 13:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 167.0 |
| 627ed86c-bc81-348f-a755-943b2d4d84bc | -10.1718 | -44.5264 | 2025-11-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 217.9 |
| a0b79b7d-1c3e-37f6-a934-c03b0d6138f4 | -8.6808 | -45.5041 | 2025-11-16 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 2b5c071b-61d0-3da9-af6b-5c5a624ce09b | -10.1245 | -43.9046 | 2025-11-16 13:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 654920c5-bed3-3daf-94b1-e147925a579e | -9.157 | -45.2015 | 2025-11-16 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 75cf3c99-f6ee-30ce-8b13-693b54dcacda | -3.2304 | -43.3486 | 2025-11-16 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 5ead4133-329f-37f2-80f2-e48e1fd7baad | -2.4201 | -45.7015 | 2025-11-16 13:50:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b4450641-3c42-3759-bfc2-18bc8470ce44 | -9.7436 | -43.9542 | 2025-11-16 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 2ac67a7d-d6f1-3117-96a7-e1a2f9c25b48 | -3.2304 | -43.3486 | 2025-11-16 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6689611c-83ae-3d30-908a-0de6df63335d | -10.1722 | -44.5032 | 2025-11-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 29482484-e62b-3e72-8d92-2a58c9c5d4fd | -9.8542 | -44.1729 | 2025-11-16 14:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e0b1904c-6e94-349c-a54d-3db77d021d51 | -9.7432 | -43.9775 | 2025-11-16 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 303eb8e4-8af2-3ec6-b43b-d80b8f79519b | -9.2139 | -45.195 | 2025-11-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 38747173-a4a0-3707-981e-51f7c23ea747 | -9.9377 | -44.9252 | 2025-11-16 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4d490654-d623-3bc7-a320-f14390764df8 | -8.5415 | -46.0832 | 2025-11-16 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |


[Clique aqui para ver as próximas entradas](README70.md)
