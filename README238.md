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

## Dados Diários - Página 238

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f74feb-d9e4-39f1-9716-290c26cb3063 | -13.1249 | -46.3291 | 2026-10-09 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 87c39476-ca6f-3175-b1ee-caa10dd59a64 | -11.8499 | -43.5835 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 3bdc0346-ed78-303b-80c1-ed201c5fe73d | -11.0566 | -44.0327 | 2026-10-09 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 2eab9488-2f2a-373b-a06a-12dbcfcf9021 | -11.598 | -43.7172 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ebc0edf8-4622-3b32-9f96-848a0513674c | -9.3101 | -46.4509 | 2026-10-09 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| ee210b83-8e32-3567-9810-7bb7265aed27 | -9.0829 | -45.0957 | 2026-10-09 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 6209b938-328e-3b6b-a240-8b854bc35c19 | -8.9775 | -45.9023 | 2026-10-09 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| dbcfdee7-76e3-3ce9-a17a-6e2d36318958 | -11.2259 | -45.3064 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 7e7d7b22-b886-3688-b829-65e7d8f556c1 | -11.8307 | -43.5866 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.5 |
| 17d29ab7-913e-367d-baa0-b82dde3abf08 | -12.8105 | -44.6505 | 2026-10-09 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 248.1 |
| 219b62a4-01dd-344b-bd74-db8715fea12a | -10.9174 | -45.5088 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 8699f474-bfac-32a4-9123-94e6ada5e3ad | -11.8302 | -43.6103 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 47cf4ef9-6f22-3d0e-a2c3-0b7e54728309 | -8.0766 | -45.6112 | 2026-10-09 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0e921687-8e4f-332b-b4ab-444eff6737bd | 4.4435 | -60.9846 | 2026-10-09 13:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a657e56b-6f9e-376b-9d39-be20724dd761 | -11.6566 | -43.661 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 90d83b1c-3781-367f-a6ee-fdde16032404 | -8.5315 | -46.8887 | 2026-10-09 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| fcdac37f-cbd4-315b-a031-d799865c43fd | -11.245 | -45.3037 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 429.3 |
| d422c91a-96b4-376a-8888-b98f6946a347 | -5.5 | -43.02 | 2026-10-09 13:15:00 | MSG-03 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45c3826f-c734-3d16-8d99-fb39d81db4ec | -5.5 | -43.07 | 2026-10-09 13:15:00 | MSG-03 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c40ad8c-ce5b-39fe-b958-01860438a5af | -5.53 | -43.07 | 2026-10-09 13:15:00 | MSG-03 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2aebb874-8785-314e-9a34-a6d70ebe77a5 | -10.9533 | -50.7018 | 2026-10-09 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7624159c-99f4-3f87-88bf-9133ac7dd5bf | -9.2973 | -47.4092 | 2026-10-09 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 983a4cdc-dd0d-32cb-908d-467014ac5afc | -11.2475 | -46.3058 | 2026-10-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| d1407ebf-07b8-3254-9449-9d9814281ce7 | -8.5313 | -46.911 | 2026-10-09 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| fd6cba35-760c-3142-9a90-b574b95f6798 | -10.8413 | -47.9423 | 2026-10-09 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 58b6e271-0edd-3c5b-bcd8-74cc8f321cf0 | -11.2259 | -45.3064 | 2026-10-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 43927691-20c0-36d0-87ec-c188e997f62c | -16.6321 | -47.203 | 2026-10-09 13:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 187.4 |
| c6798d91-aa0d-3ce9-824a-150ece91e1f2 | -10.9953 | -45.4068 | 2026-10-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 9fc97151-f0d0-3248-9fb9-71b628d3ae29 | -15.3838 | -41.878 | 2026-10-09 13:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| b2b5aaa5-525d-3ef4-9126-9c5caa5ece33 | -8.3011 | -45.7245 | 2026-10-09 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| aa77da2d-5e77-3f89-8cb1-9c10b38aa40e | -11.8302 | -43.6103 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8cbcf669-1645-3fba-a1c7-5203bc5ffa3c | -10.8127 | -47.3256 | 2026-10-09 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3613f1f0-e8ab-3529-8df3-6811c8b7db21 | -11.8783 | -47.3892 | 2026-10-09 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1077b504-f5fe-30ed-8656-7ab566dbba58 | -9.1015 | -45.1164 | 2026-10-09 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 64c57290-5d67-36ba-bbfd-d248458bdac8 | -12.1917 | -44.8186 | 2026-10-09 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 50a772b1-7959-37b5-b10c-7a51abd5b919 | -8.2063 | -45.7791 | 2026-10-09 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 181bcfc6-981b-3a93-95ed-1d50b2988a3d | -11.5801 | -43.6492 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 234d9076-4f50-3236-9673-a4ebe2ea1eae | -8.0766 | -45.6112 | 2026-10-09 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c4190abb-f9f6-34c8-8cd8-1dbe3db3e8c8 | -11.6562 | -43.6846 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 456.0 |
| 35b26bbc-df1e-3a62-8379-b5ba47c1d1ee | -10.5281 | -47.3156 | 2026-10-09 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2d7fcf07-30f4-39df-b28f-4ef0ed9d5880 | -15.3832 | -41.9029 | 2026-10-09 13:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.2 |
| 171a7646-4f9b-3f1b-b2f6-cb73dff7ab68 | -15.2535 | -42.3741 | 2026-10-09 13:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| 5d06e6a7-5490-3188-830d-efa3ef805d0d | -10.4334 | -47.3046 | 2026-10-09 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 00c252a7-f57a-3ca7-8265-5721daefa4e0 | -11.245 | -45.3037 | 2026-10-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 34795e6f-d667-3129-bd05-9c943aef6dcc | -8.9964 | -45.9002 | 2026-10-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.4 |
| f05805aa-ff56-33ff-8d6e-ee6320080ef1 | -10.7479 | -46.5959 | 2026-10-09 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| eeaf6b76-42c8-340e-a4d3-98e8c2312082 | -10.4901 | -47.3201 | 2026-10-09 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| e8c020fa-3e3c-319f-8c13-31c8600c1809 | -12.0054 | -43.4878 | 2026-10-09 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 0c3faa3a-ecb2-3c3d-a6e3-595bb2f9e8e5 | -9.1012 | -45.1393 | 2026-10-09 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 043db373-4d9d-3ce7-a9fb-6035e8cd5704 | -18.3335 | -42.3598 | 2026-10-09 13:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| df16a5a5-4d13-369d-a395-782f939aa12a | -11.5998 | -43.6226 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9dcb1348-72ab-3fe8-bfbc-e72633eb4f3c | -8.3234 | -45.4506 | 2026-10-09 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 90d1913e-0c6e-3512-9c80-e88901adafa5 | -12.1537 | -44.8013 | 2026-10-09 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 2a997a3f-edee-36b8-b3c8-8006f91112ec | -9.9798 | -45.9236 | 2026-10-09 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 330.2 |
| a8818757-69b2-34e8-9e6f-1c49d6743ed4 | -10.9536 | -50.6805 | 2026-10-09 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ce6d5313-3d50-3960-b13b-90494edc592c | -11.2068 | -45.3091 | 2026-10-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b8afe9f0-dfc1-318b-875a-8346345bd11f | -15.2541 | -42.3495 | 2026-10-09 13:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| 2609e3ee-7ab4-3d40-9e8a-5bab07d9f727 | -9.9208 | -44.7893 | 2026-10-09 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| b7e3d7ce-c5a7-3540-a872-9b316f43aea6 | -8.0764 | -45.6339 | 2026-10-09 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 895521d4-1b3b-320c-ac54-f98b24ebd158 | -9.9801 | -45.9009 | 2026-10-09 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 15494b37-ac9a-3ab2-9c86-57f0e4b52e1f | -12.211 | -44.8156 | 2026-10-09 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 45e338b4-d7e8-3703-a240-cbd1f0fe8fc0 | -11.9865 | -43.4671 | 2026-10-09 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1698.2 |
| abd91ece-ec34-3ba5-b2c5-28a6b6c2c19a | -12.0063 | -43.4402 | 2026-10-09 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 267.7 |
| cfffc0b4-1cf0-31e4-be41-1da384a55889 | -9.9991 | -45.8986 | 2026-10-09 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| e6d798bb-5193-3d10-a513-234935851029 | -12.0058 | -43.464 | 2026-10-09 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 477.7 |
| fc6415f9-f1cd-3f2a-965f-95375fd7f10c | -8.9775 | -45.9023 | 2026-10-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 282c0e40-fe31-36c0-a140-024223f6efc5 | -8.969 | -45.1313 | 2026-10-09 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 0fa3f552-e05c-3c83-9c09-869adaa7fd4e | -11.5985 | -43.6935 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 09de3c67-f725-363a-a086-c76e41b6a328 | -10.7475 | -46.6184 | 2026-10-09 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 69b36933-200b-3568-8b9c-961456ac0f57 | -11.6566 | -43.661 | 2026-10-09 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f4e39096-a2e1-34a7-8fd4-33396b11a7bf | -12.1729 | -44.7983 | 2026-10-09 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 37ba959c-7e52-36c2-8b41-2d9f05be558f | -12.2149 | -44.6057 | 2026-10-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 699a8a72-b78a-3253-b416-ca42c19309f0 | -11.5998 | -43.6226 | 2026-10-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| aef9e5e2-f132-3ba0-93b3-a9f301f39929 | -10.4901 | -47.3201 | 2026-10-09 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| dad2db84-50d8-36dc-9f24-bae38c8e62aa | -9.9991 | -45.8986 | 2026-10-09 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f73bb61e-fcb4-33c3-9d1d-24242bdeacb0 | -12.1733 | -44.775 | 2026-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| a5dd7ef3-cef0-313c-94ed-cd65c1a6baaf | 4.4435 | -60.9846 | 2026-10-09 13:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 16cc1372-edbd-3943-8eb2-5b1f6f304779 | -9.1015 | -45.1164 | 2026-10-09 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 91d3d883-8811-3199-b8a3-5ba9c2ce7a05 | -10.917 | -45.5317 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 211.9 |
| a2281706-b3fd-3ca1-ab9f-ee13b0e16ec3 | -15.2541 | -42.3495 | 2026-10-09 13:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| d6bc80e8-3083-361b-888f-74b0b6678db2 | -12.1729 | -44.7983 | 2026-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 37b17ad0-e9af-3689-8970-05ddeb993bd1 | -8.5315 | -46.8887 | 2026-10-09 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 62e4bd39-ace0-39e5-973a-da36b9651d9d | -9.9798 | -45.9236 | 2026-10-09 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 35f0cb06-a5a8-3d9d-88d0-d3a3a8550d87 | -8.5313 | -46.911 | 2026-10-09 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d67c787a-21b6-3597-ac86-ca990b483c17 | -18.3335 | -42.3598 | 2026-10-09 13:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.3 |
| 35e0e7f5-334d-34b6-80c9-7304ff8cf9a6 | -12.1541 | -44.778 | 2026-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 21c37af3-cf40-36cc-a78f-9c77321fdbda | -10.9174 | -45.5088 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| f5a77c10-ca1b-342d-837b-b133e80d42c0 | -8.9775 | -45.9023 | 2026-10-09 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 360ac70d-e264-3c18-957d-e2bfd1947420 | -8.3234 | -45.4506 | 2026-10-09 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fa56e67a-3be1-3bfc-bac9-c797d1aaf235 | -11.8783 | -47.3892 | 2026-10-09 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| df23f1c5-8f14-3cd9-ad9c-dcd85f4f7543 | -9.183 | -43.3688 | 2026-10-09 13:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| 78caddc2-bb53-3379-9a5d-a3740430e34b | -12.1725 | -44.8216 | 2026-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1c2cc9c0-51ed-3c12-b08f-f57562890563 | -11.6562 | -43.6846 | 2026-10-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 404.5 |
| e5d776a9-26e5-37d3-b97c-f8fec2f48bff | -12.0054 | -43.4878 | 2026-10-09 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 3fe104e4-1109-381e-b176-eaec52cf075e | -15.3838 | -41.878 | 2026-10-09 13:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.0 |
| 9beebb5d-4f2c-30bf-b713-7d7e1e5ba149 | -11.2259 | -45.3064 | 2026-10-09 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e6ea5993-3c3a-37ba-bb1f-d0ba96007920 | -10.4334 | -47.3046 | 2026-10-09 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 4fa24445-8ee5-3125-936f-bb4f22746e6f | -8.0764 | -45.6339 | 2026-10-09 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 6f582685-1c1c-3be2-8a74-55cecb113822 | -11.3371 | -46.6547 | 2026-10-09 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ceb368b9-45dd-3255-aa4d-91162982e525 | -11.9865 | -43.4671 | 2026-10-09 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1696.2 |


[Clique aqui para ver as próximas entradas](README239.md)
