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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b76bd556-e638-3ed7-84f4-4c069f6d06ec | -7.1429 | -41.7692 | 2025-11-16 14:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 614c1ff9-3116-3110-bc2a-ecddf062a283 | -9.7532 | -47.2049 | 2025-11-16 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 0884b04c-4cdd-3655-9a43-ffeb076e63c6 | -9.9969 | -44.7797 | 2025-11-16 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| baacc841-4db6-32c8-8820-f53abfda91b4 | -8.6814 | -45.4587 | 2025-11-16 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 364ff996-5a63-3279-9431-5213c51014de | -4.4059 | -43.4049 | 2025-11-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| e95e9910-35e0-3dd4-a29c-5efacaec476a | -9.9972 | -44.7566 | 2025-11-16 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 143cf425-d0b9-3ad8-9311-e951571f8299 | -8.6808 | -45.5041 | 2025-11-16 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 216.5 |
| a38e30cb-cdda-35bf-8655-c7af28f6ec95 | -3.2302 | -43.3718 | 2025-11-16 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ab2aaf18-9218-3784-bd1a-e36b6c531344 | -8.5383 | -44.8582 | 2025-11-16 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 00a38c68-3fe3-36a8-8ce9-05e13fa35bba | -3.8436 | -40.7759 | 2025-11-16 14:00:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 271ffdfc-f835-3e90-b471-7d23512341c3 | -2.5238 | -47.8115 | 2025-11-16 14:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ad40ecdc-83c5-388c-beeb-86806e12bb34 | -6.3705 | -41.7477 | 2025-11-16 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 157.7 |
| a51423ce-beac-309f-8ec9-eabc40c80747 | -9.7242 | -43.98 | 2025-11-16 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| c13fa20f-8453-37c6-b9f0-0c55585fa79e | -8.6811 | -45.4814 | 2025-11-16 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 275.7 |
| fb6feaad-88ce-3360-a310-34e1d2391beb | -9.7246 | -43.9566 | 2025-11-16 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 288.4 |
| 1190a099-6107-3082-a45a-e4f1164ae9c6 | -11.4136 | -43.32 | 2025-11-16 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c8095ef9-4440-373f-b22c-4650de0bd90b | -10.1055 | -43.9072 | 2025-11-16 14:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 71d3292e-4c29-3e8e-b6a0-694872cc14a8 | -4.019 | -48.8147 | 2025-11-16 14:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b8588a59-3494-38d5-9df0-b9ebae89a7b4 | -6.2391 | -41.7115 | 2025-11-16 14:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 2fe79a31-8f3a-31e4-aac7-5ce39987e548 | -3.6088 | -42.4176 | 2025-11-16 14:00:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| afc03a81-ce72-38ab-aa52-ef2a254b38c2 | -10.1245 | -43.9046 | 2025-11-16 14:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 426.4 |
| 04a7e51f-ee26-34d3-8122-63419a7a2c66 | -6.7339 | -42.9498 | 2025-11-16 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 23a64070-d972-37b9-b292-f0e408662751 | -9.7436 | -43.9542 | 2025-11-16 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 218750c2-866c-3dfb-81a5-cdc1bd417431 | -8.6623 | -45.4834 | 2025-11-16 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| f8824658-aaef-3337-bd40-06b03c6ed720 | -10.1718 | -44.5264 | 2025-11-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d86ee093-f542-38ff-9535-051526b835e6 | -1.9886 | -47.3465 | 2025-11-16 14:00:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8cf39478-e70b-3330-8930-d11453ce225e | -8.1092 | -46.0363 | 2025-11-16 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 9ab45d4a-ec27-35b1-b9d0-7455180f871a | -1.3191 | -49.1462 | 2025-11-16 14:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| efb69899-fd41-3502-bba9-fc793648c157 | -8.6623 | -45.4834 | 2025-11-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 66df49e2-427d-3318-a537-eaeeaae1f6ba | -4.0884 | -43.3996 | 2025-11-16 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| fe0c8a50-c4e0-3c54-8fc2-6584c57cd13b | -3.8436 | -40.7759 | 2025-11-16 14:10:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 140.0 |
| b5b2c76c-0dd5-3b82-b66d-a3ace0572762 | -8.5415 | -46.0832 | 2025-11-16 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c6226312-747d-3ef1-a0e6-eb40fd7f97f6 | -3.2439 | -40.8074 | 2025-11-16 14:10:00 | GOES-19 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 118.4 |
| b982142d-8646-3530-99e1-a857c8552e2a | -4.1528 | -42.1514 | 2025-11-16 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 6b572129-ed4d-39e5-9824-30ea1978f707 | -2.5238 | -47.8115 | 2025-11-16 14:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| feb67ed4-9ba6-364e-8d79-63af3d3d7487 | -8.6808 | -45.5041 | 2025-11-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 3931a0c9-cda8-3aa2-997a-d3cc43f900f9 | -9.7242 | -43.98 | 2025-11-16 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 7fd8b724-3169-3540-8c1c-032c9c324724 | -9.6373 | -46.0317 | 2025-11-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c4d03409-ffad-3635-ae10-922b41db86b1 | -9.7532 | -47.2049 | 2025-11-16 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 1828fb91-713b-3dc0-965e-65af4158ec4d | -11.9179 | -46.1907 | 2025-11-16 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 539d6366-08e4-353b-b7b4-57da4fdb2716 | -9.9969 | -44.7797 | 2025-11-16 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 39004dde-e0d8-3a2c-968a-8769f027f49b | -10.1722 | -44.5032 | 2025-11-16 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 198.2 |
| d0d744c3-c12e-32d5-bbd3-c339915c343b | -8.7546 | -45.6323 | 2025-11-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 821fe58a-1d03-3d87-a241-2c99cbdc6792 | -9.8542 | -44.1729 | 2025-11-16 14:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c7fa5fa7-8638-37b1-9ffe-5b1990ee41cb | -9.6562 | -46.0295 | 2025-11-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 1d9770b2-c110-38a6-83cc-560bd4554fa0 | -6.5411 | -43.4122 | 2025-11-16 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 62.2 |
| b7aa8b2f-56ce-3e31-ad15-54d6f5e3d13d | -9.7432 | -43.9775 | 2025-11-16 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d6117acb-87e1-3560-a393-ad9d32538f7a | -8.6811 | -45.4814 | 2025-11-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 251.0 |
| 6e7ac1d9-ee12-314f-b985-690d829b39a8 | -3.8437 | -40.7515 | 2025-11-16 14:10:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 553a6bde-aac2-3c4e-93ac-615f15f74cfe | -8.6814 | -45.4587 | 2025-11-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e3923860-eb8b-33c0-b12e-902e36070300 | -9.9972 | -44.7566 | 2025-11-16 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 59745051-0429-3d05-a97a-e2bd6208c781 | -3.2117 | -43.3494 | 2025-11-16 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 27a20db3-2fad-37a0-8dcb-324c94baee87 | 1.6202 | -55.8049 | 2025-11-16 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3ba5d9a4-163d-36c2-bebb-1e2b9bf75f40 | -10.1234 | -49.159 | 2025-11-16 14:10:00 | GOES-19 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1c1f84e3-5630-3cc8-8db4-ee660d3a1191 | -6.2763 | -41.7562 | 2025-11-16 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 379dc369-5b4a-3432-a9ab-06b18e583f97 | -9.861 | -47.6137 | 2025-11-16 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9ecca880-d093-3d7a-9d3e-7a339cf600f5 | -10.1055 | -43.9072 | 2025-11-16 14:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| a8e7f3ae-2b07-31ed-8759-2c11ba310f27 | -9.7436 | -43.9542 | 2025-11-16 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 24606aa2-f965-33dc-bf6e-0394f3c96665 | -2.5053 | -47.812 | 2025-11-16 14:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 26a5394b-78d6-3363-932a-908d97a2bd8c | -9.0327 | -46.0091 | 2025-11-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 1f1f52ec-42d3-3cfc-9ff5-566af369b8ff | -8.1092 | -46.0363 | 2025-11-16 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 68988618-d1b7-3c78-abcf-816908dce516 | -6.7339 | -42.9498 | 2025-11-16 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 74d569f0-2783-3616-b38d-b7960ea6c301 | -6.258 | -41.7098 | 2025-11-16 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 17fb5817-be3a-3f3a-aeb6-bb360e98083e | -3.2304 | -43.3486 | 2025-11-16 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| b456f787-431e-3c81-a676-c4d2a20b335a | -3.317 | -41.1187 | 2025-11-16 14:10:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 92.5 |
| b165fd04-837a-33f6-95ce-b7dd77f3dc19 | -12.8722 | -46.459 | 2025-11-16 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| d50dc1a6-cfdd-3fae-9598-b83a3f824000 | -9.8542 | -44.1729 | 2025-11-16 14:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 169.7 |
| d47eaf35-3a26-3641-ac2a-07b33229319b | -9.7436 | -43.9542 | 2025-11-16 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 09908c92-1b48-3a6b-b5b1-3264cd77d744 | -2.4201 | -45.7015 | 2025-11-16 14:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ebf8a065-204e-3b6c-a65c-1ba2e89505b2 | -8.1092 | -46.0363 | 2025-11-16 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 45e2f249-b506-3f7a-b693-06746211dd07 | -3.8437 | -40.7515 | 2025-11-16 14:20:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 289cfefe-0e30-3600-b95f-9749b3b86174 | -10.8768 | -44.501 | 2025-11-16 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 224373c7-b06f-384d-8a7d-479d283bb224 | -4.8119 | -41.6803 | 2025-11-16 14:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 14a4b76f-0404-3220-aa71-594c2b2e9ce8 | -11.7208 | -48.8669 | 2025-11-16 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 0faab93f-fb7a-3d4f-a469-291ff6ba8550 | -10.1245 | -43.9046 | 2025-11-16 14:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 1d53000f-25e8-3a84-b4fc-8445ea8c567c | -8.6814 | -45.4587 | 2025-11-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 9fc1f3d4-ac4a-3925-ac1b-ec82be6064b5 | -2.5053 | -47.812 | 2025-11-16 14:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ff9ca486-154a-3294-b15d-c80b8eec3e0b | -9.8305 | -47.0852 | 2025-11-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3cefa555-dc5a-3aa6-ba7f-5fb227578151 | -9.157 | -48.0615 | 2025-11-16 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 41ecd0c2-60eb-3ac1-8853-d7a692559ec3 | -12.8534 | -46.4392 | 2025-11-16 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 84899b42-e787-3cf9-832d-c13fb3ca0fec | -2.4201 | -45.7238 | 2025-11-16 14:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4dcd6902-abf3-3c39-9ded-21ced33e7ff5 | -11.7021 | -48.8474 | 2025-11-16 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 30c7006e-5921-3ea6-aab1-e622ef7b2952 | -9.7242 | -43.98 | 2025-11-16 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 7b545a73-96bd-38dd-bb10-5e232682c615 | -9.6562 | -46.0295 | 2025-11-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5a431318-ffa9-3395-b0d0-4671e76f1bea | -8.6623 | -45.4834 | 2025-11-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 3136e404-541f-39be-86e2-76e5da654397 | -12.4109 | -47.5616 | 2025-11-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1da724a6-2520-3158-8f2b-3b961c079163 | -10.1725 | -44.48 | 2025-11-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ae0a12b7-34f1-3333-8f9f-2b5a0b06214c | -10.1718 | -44.5264 | 2025-11-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 330.6 |
| d59fd371-46bd-3909-9026-648973b1bcba | -6.7339 | -42.9498 | 2025-11-16 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 970d581d-0d19-3cbd-ba02-4587e5b909c7 | -10.1234 | -49.159 | 2025-11-16 14:20:00 | GOES-19 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 963a6c74-4b0b-343b-a9c1-1872ab95f3d8 | -10.1055 | -43.9072 | 2025-11-16 14:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 918bf7d3-afd4-3571-92c8-fd9527099033 | -3.3909 | -44.72 | 2025-11-16 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ba26cfa3-0a53-3420-9ece-b85aa44fac70 | -4.1528 | -42.1514 | 2025-11-16 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 428b65b1-9d38-3c06-856b-0946303cfcf2 | -12.8727 | -46.4363 | 2025-11-16 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 028ce2c2-8aad-3fc7-a75b-01a02357c808 | -12.3921 | -47.5419 | 2025-11-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 75d481d7-e21e-37c2-b235-7151ddcd7805 | -11.7017 | -48.8692 | 2025-11-16 14:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 49234831-7db6-3a11-af72-d7922fecb192 | -10.1912 | -44.5007 | 2025-11-16 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4429b4a7-f0d3-3cbd-8029-56fde38daaa8 | -8.6811 | -45.4814 | 2025-11-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 0e938bdb-59f1-38a3-8c89-fb3734be337a | -11.4136 | -43.32 | 2025-11-16 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c9e24c58-289f-3e23-8c17-e9cefb8b4364 | -3.9895 | -44.2813 | 2025-11-16 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |


[Clique aqui para ver as próximas entradas](README71.md)
