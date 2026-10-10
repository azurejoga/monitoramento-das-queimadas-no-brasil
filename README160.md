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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67fe0bac-750e-3e2e-8510-7634b68153cc | -11.8499 | -43.5835 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 4b3b5ac9-1021-394d-8f67-0ed62d8a2f6c | -12.5028 | -51.2937 | 2026-10-10 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 977fde92-44b7-3130-9ed4-778c598f0c7e | -12.211 | -44.8156 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1212.0 |
| e96526ad-fe4b-3925-9644-bd3c53ab38df | -11.0379 | -44.012 | 2026-10-10 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 285.8 |
| 04845eb5-3efd-3703-b277-4a3068e48ebc | -11.47 | -43.3824 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 8b63d943-03e8-3557-a043-ba6e028b3a7b | -11.0144 | -45.4042 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 333.0 |
| e20f8736-28b3-322e-ad8b-80f795bbd038 | -10.9957 | -45.3839 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| eb2da3f9-6779-3a15-b765-8ebd366ef9e6 | -11.8495 | -43.6072 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 03e2e2d8-d871-30b9-af0e-3df1032b5d40 | -6.4956 | -38.9535 | 2026-10-10 14:20:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 89dda17c-76a2-3e1b-9e73-04ba333533c6 | -12.1861 | -48.4124 | 2026-10-10 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0bb85201-af4b-3e91-98e1-b76d4353d106 | -10.4914 | -47.231 | 2026-10-10 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3e649324-fd7b-3fd2-9048-3f65976f44a7 | -8.7075 | -44.9086 | 2026-10-10 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 471cf0ff-c55a-36e3-b47d-159bf02347cb | -17.4775 | -45.0705 | 2026-10-10 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d50d4630-2759-38c0-9a63-24790ac3e7f1 | -13.1641 | -54.3178 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 72bd32cc-09ea-3557-ab18-52f133a805c2 | -11.6194 | -43.5959 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| bdeeed64-6f69-3ef4-a229-d12f373403bb | -11.057 | -44.0092 | 2026-10-10 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| f13c0476-01e9-350b-aaa9-da6ed4329ffc | -7.1825 | -52.6283 | 2026-10-10 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d9217c33-4c79-337e-a670-7e72115fa1e8 | -10.9197 | -45.3712 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| fba8a29a-b4f6-314c-83c4-90ac81cb27bf | -10.2491 | -49.642 | 2026-10-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| f43e2093-0376-3183-918f-bfe1bb16502a | -12.2127 | -44.7224 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 92b14063-255f-36b3-bb79-d2d77b94cef6 | -10.4147 | -47.2846 | 2026-10-10 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| d5d33a90-f9a1-3fc6-91ff-e6a070718ef5 | -7.4886 | -42.8295 | 2026-10-10 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 33131344-9536-35e7-9c1a-59fbd65d4f5a | -9.9398 | -44.7869 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 291.0 |
| 1e3429e9-d736-3b1a-8dbb-3e010d2862d5 | -13.183 | -54.3365 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| caf6abc9-936f-3549-9d1c-47d2b3ab6731 | -1.4301 | -49.0382 | 2026-10-10 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 230f58c7-6615-3e20-82c0-7de40689b79e | -4.4977 | -43.6315 | 2026-10-10 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 543c635c-7f0e-39ef-aab7-da5816017068 | -12.1913 | -44.8419 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 391dbf5c-b86c-3b4e-b4b9-d0742512cb22 | -4.4976 | -43.6547 | 2026-10-10 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| acce5bbe-6acf-34cb-b70e-ff5c0cb4acfa | -11.1873 | -45.3347 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e09211ef-9829-372e-82a6-1da0dda306c5 | -12.8321 | -50.9981 | 2026-10-10 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| dd65ed08-a24a-3aef-b4cc-03812da16124 | -11.6002 | -43.5989 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 15890218-e5d7-3ea8-b15f-072f3e476c1b | -10.2488 | -49.6636 | 2026-10-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8a2776e3-1196-36c8-8022-267c57fa540a | -7.4703 | -42.7842 | 2026-10-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 4277d485-f819-3b39-970d-c31419bf9925 | -11.0183 | -44.0382 | 2026-10-10 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 195f621a-d157-386d-add9-edcfd99840c0 | -1.2455 | -49.0194 | 2026-10-10 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 97adbe14-dc71-36bb-baf1-562ae2387cc4 | -12.2106 | -44.8389 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 266009a9-9ad4-3922-9adc-e27b067cdb9e | -8.9275 | -45.4094 | 2026-10-10 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 24ce844a-d2c1-3d06-8765-34ffe809c969 | -9.1012 | -45.1393 | 2026-10-10 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e3fcfb3c-97bc-3ea6-8122-050676acda0a | -10.8909 | -44.8001 | 2026-10-10 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| df137974-82e1-3b2f-85e7-ed64f3d77225 | -12.2119 | -44.769 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 1dc3a14f-8c67-3b48-a4c4-ed7f743fc15a | -12.1926 | -44.772 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 949cec75-7d1b-3f8f-be23-1f0ef0acfad5 | -12.1922 | -44.7953 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 0af3cecd-d58a-3973-ba2a-c9fc889fea9c | -10.9384 | -45.3916 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 93baf7eb-0d5d-397d-b7c7-be54172a0c0e | -1.4486 | -48.9953 | 2026-10-10 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0d0a9aa6-42d0-338b-b85b-35b9f5281cd4 | -11.0335 | -45.4016 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| cd5d5165-ca72-3294-9bcb-465178380d91 | -12.1917 | -44.8186 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 377.6 |
| d7720705-226d-3508-badb-39e522ead35d | -7.4883 | -42.8532 | 2026-10-10 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 03715374-e147-3522-863f-d8ede13150fd | -15.6892 | -43.8327 | 2026-10-10 14:20:00 | GOES-19 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 53f9bf4d-7143-386f-8991-315867d1e20e | -17.4575 | -45.075 | 2026-10-10 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 4aef20e1-b328-3107-a014-4a832b58502b | -8.0769 | -45.5886 | 2026-10-10 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5eedf35f-8979-3440-b07b-613e96356b35 | -10.2486 | -49.6851 | 2026-10-10 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3e3ff764-50f0-3818-b9b6-b53ba41e1eb2 | -3.106 | -50.2896 | 2026-10-10 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b6e1f80e-657c-398c-a459-68627b6c58ce | -13.1641 | -54.3178 | 2026-10-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a4e17cd5-dae1-3910-b474-6d04f942879d | 1.7305 | -55.5666 | 2026-10-10 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e5ffa94c-9a61-30f0-8b94-9aa43cbcb29f | -1.3447 | -56.3979 | 2026-10-10 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 99c49bd3-aaec-3cce-b4ce-175e2566457c | -12.1861 | -48.4124 | 2026-10-10 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b2d67cab-6b05-3159-a7a7-c0db952b8be8 | -7.4703 | -42.7842 | 2026-10-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 3914a750-204a-3f41-a4e0-3cc4d047b7c8 | -11.2259 | -45.3064 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 5b4d0acf-1ec2-3210-af2d-774be449acf6 | -11.0183 | -44.0382 | 2026-10-10 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 901074b1-e133-369d-b422-e683593a53f3 | -15.6892 | -43.8327 | 2026-10-10 14:30:00 | GOES-19 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 0a59bcda-2a66-3756-b77d-02a36a7dd73d | -12.1922 | -44.7953 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 301.6 |
| f2908228-e188-3dc4-8912-ae19efe5ca51 | -12.2136 | -44.6758 | 2026-10-10 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 7d82268f-9af1-395b-9441-ba9eaa345dd5 | -12.0063 | -43.4402 | 2026-10-10 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 317.9 |
| 048d8fe0-553b-3e31-880a-27cb5aa8ec8a | -13.1639 | -54.3385 | 2026-10-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 7f7bb576-da1a-32e4-b9e5-2e39b60e97dd | -5.942 | -41.3282 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| df75ff02-e1a8-311d-8adf-aa407b237fa8 | -5.7321 | -41.6349 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| d540b449-6a33-3ef3-956e-585b713bf9e6 | -11.7772 | -45.4806 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 59da45a2-bf2b-3afd-844b-a39fc51c08a7 | -9.1525 | -49.9639 | 2026-10-10 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9e8384a3-ec4f-3068-966c-3c41614cf10d | -13.1833 | -54.3158 | 2026-10-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a7b07ce6-a341-35c9-b41f-4d59086e1e01 | -12.8303 | -44.6239 | 2026-10-10 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| daed7929-5ac0-31d1-890a-e59d1631e3b5 | -9.9381 | -44.9022 | 2026-10-10 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a143f9ac-19fa-3e27-856a-24c40ee9bc95 | -1.2723 | -55.7494 | 2026-10-10 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1bbf8569-386d-3504-8bf6-37c822b495fb | -12.1926 | -44.772 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 0e4333d2-7464-3f2a-995f-7ce4bb23ef6f | -11.8696 | -43.5568 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 96445e16-7f51-3bfd-bc40-bdba590a10d1 | -11.3633 | -54.0452 | 2026-10-10 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| afa5b8bf-37dd-350f-90c7-9e5bc76c6838 | 3.9309 | -61.0906 | 2026-10-10 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 678b66b9-c93f-3a5a-970c-4ea35f91faa8 | -12.2127 | -44.7224 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| cf3b3812-f13a-30c5-a68b-f9803647defa | -1.6409 | -54.4146 | 2026-10-10 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 444.8 |
| 253e52c9-219f-3bf7-9d76-da2fa7aad652 | -12.2329 | -44.6728 | 2026-10-10 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 2f6f7f76-c848-3246-8dec-c86a51d7e9ab | -9.9398 | -44.7869 | 2026-10-10 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| eebc2ea1-ed36-30bd-aaf5-8b3d1632a8c3 | -12.211 | -44.8156 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 836.9 |
| 74f1abc1-a39d-3f27-909d-ba787d857b8f | -4.2965 | -43.0149 | 2026-10-10 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ac9568d2-cc30-3824-a425-10cfa709486c | -5.7509 | -41.6333 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| c525e57f-5aa8-31a9-b031-8accb1da12d4 | -11.7768 | -45.5035 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| baac2ea9-af34-34eb-8682-77bd27966ecc | -10.9388 | -45.3687 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 3021320a-015c-30d6-a1a2-87c5323786f5 | -10.8909 | -44.8001 | 2026-10-10 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 0555c5e6-cacb-3482-8ecc-be8568a7eda0 | -12.4646 | -51.2982 | 2026-10-10 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 87e5feb0-ec1c-384f-9de1-492e5ef96678 | -11.1876 | -45.3117 | 2026-10-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| b860bf61-220e-34d7-937f-1311a2a6dde0 | -11.987 | -43.4433 | 2026-10-10 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 1974f7ce-a4f1-3fd9-97aa-c7ee74f9ff8f | -0.8768 | -48.7246 | 2026-10-10 14:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 065bf93a-3413-3194-bd8c-5fc57326e1f9 | -13.183 | -54.3365 | 2026-10-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| d10b9e3e-17d0-316c-b0b8-1966a498da9e | -3.1059 | -50.3105 | 2026-10-10 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e0185f22-9413-31a9-aba4-14a5babadebf | -11.057 | -44.0092 | 2026-10-10 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 04172d3c-768d-3fc2-b7d4-b92347ee273b | -5.7319 | -41.6589 | 2026-10-10 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| cd5998b4-9069-3168-be51-c59595d0e1ea | -12.2106 | -44.8389 | 2026-10-10 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 6479f3db-e67d-39e1-9c1d-ebe2113eba0e | -11.7742 | -43.5245 | 2026-10-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 4d5ee341-9259-3c7a-87dc-e26b7feb843b | -9.9208 | -44.7893 | 2026-10-10 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| b1d70555-da2f-35cc-bb5e-877a4eb04e33 | 1.7304 | -55.5863 | 2026-10-10 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3acc3267-be90-300d-8e9c-b2d9a669bc5f | -13.2018 | -54.3551 | 2026-10-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4702c777-2e5a-36e5-8aa5-f8546df0287c | -12.0256 | -43.4371 | 2026-10-10 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |


[Clique aqui para ver as próximas entradas](README161.md)
