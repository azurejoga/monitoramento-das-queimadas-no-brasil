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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26c9a25e-380f-3580-8447-39bf60b0dc74 | -10.88713 | -54.13641 | 2025-11-16 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7808e97-4cab-3a2f-8c6b-d21e525ee9f8 | -10.92969 | -48.69787 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4c1e512-94be-3919-99a2-737917c1b89c | -12.00858 | -49.28383 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a348aed3-5368-3e18-af4d-10a339dc874f | -6.87987 | -51.80939 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ebedd8-eed8-340c-a6c0-daa41bbd5e08 | -11.71049 | -48.39785 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd7db1bf-57d2-3b74-b003-33f370bd0e96 | -9.06198 | -44.7461 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cdf8367c-c611-3e4d-a2c1-ecf969adf776 | -7.01606 | -45.16457 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ae25fc1-474b-3012-a6e6-0d9f4129cabc | -6.13907 | -48.0448 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fca3fd33-9f0b-3171-9861-92256d48ea8c | -10.0007 | -44.77589 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3b37954-6513-35ee-8283-2cbd3392755d | -11.16576 | -47.46051 | 2025-11-16 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b643386f-f77b-3dcc-a63a-a03c444226da | -6.32769 | -46.33198 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84029d95-8a76-3750-90bd-7b0140ae6198 | -6.87929 | -51.81324 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddebd200-9004-3f8b-a468-1531f6a7e39e | -7.22772 | -47.98515 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cbc3832-e285-3fb6-977f-519b31153d98 | -8.57371 | -46.04821 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487c6177-48aa-30ea-844b-c77a6b04e573 | -9.72353 | -48.89952 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3d3f5f4-a869-3ee5-932e-1b64d1961b6e | -11.05294 | -45.16112 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3925acee-53fe-3c23-a9be-5dabd52233c6 | -10.54644 | -47.9393 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b1c6dfd-30c4-3ee7-adb7-4d408e76f2f1 | -6.36007 | -46.16056 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca6336cd-a990-35ef-8bcc-519808bd1fda | -9.64737 | -48.8833 | 2025-11-16 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a95f888-ad37-3206-95b9-5be0de7f32a7 | -5.71614 | -46.46347 | 2025-11-16 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0aa7f7a-ec4c-3d27-9a1f-bf7d862323e8 | -7.37348 | -43.32076 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f9d01e3-c26c-3c2f-9c44-af9f98623dec | -7.21898 | -47.98374 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dca38a6-1984-3917-8cc2-d7676d85eed8 | -11.66108 | -49.61751 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03795438-b10f-3118-b540-28a650aebfb3 | -9.57374 | -46.62667 | 2025-11-16 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d067f7a-204b-3df1-a176-a610615e7844 | -10.13251 | -49.15417 | 2025-11-16 04:57:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09123ce3-813b-3953-8269-327d662fdd7c | -12.38039 | -48.10218 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c54df26-ed25-3c8e-bdec-449b80f3006a | -11.05951 | -45.15418 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c00b31e4-1e29-3ecc-8818-cd0c469ba0de | -12.39638 | -48.08945 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8ed18ff7-824c-360f-9877-58a55f5def03 | -7.36746 | -43.31999 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b1d125-fe04-381c-bf03-f60257e40213 | -8.8678 | -50.19276 | 2025-11-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81083c10-c4dd-33b8-bc9e-fbc76905ca8a | -8.0663 | -43.10091 | 2025-11-16 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6e8ebbec-f0e1-3844-bffa-3f16d330e6ed | -7.29805 | -45.10453 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1f78b4b-cb32-3aa5-a090-826baec774e1 | -10.62145 | -44.58868 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e59a68e-0a37-3160-99a0-06f485301af6 | -12.05771 | -48.21341 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f438141-4d74-32f0-98b4-897d4bdd8209 | -12.20107 | -49.61343 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7cd61383-37dd-38ec-a3dd-fc212249e4af | -11.15822 | -49.44403 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9c7de5b-f73e-30b1-992f-9f229d691750 | -12.20188 | -49.54452 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b78fa164-527f-38f1-a6da-f291b164dc9a | -11.70988 | -48.86959 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8481743c-635f-3c90-b393-637c282baedf | -10.81082 | -47.98745 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8785f4b-e6f7-30c6-83a6-b96746d18b39 | -10.93963 | -48.69096 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3bfc7a7-ac0e-3265-9ed7-dcdf986c130d | -11.6649 | -48.46275 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb3c643a-e235-3e63-8bf9-14ff20f0e89b | -5.74528 | -49.46197 | 2025-11-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f58083d-f37d-3c12-a638-b671fb4394ff | -11.05386 | -45.1538 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f83df7d8-93d8-3cc1-acbb-a6aadde2870c | -8.58305 | -48.74627 | 2025-11-16 04:57:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f51499-65e3-3dbb-af11-9a787677e94d | -12.20981 | -49.54968 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee628db1-7d34-3245-b477-b0c385080251 | -12.8662 | -46.45937 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11fc42a7-beb5-33a4-a32e-9fdae5b6ea0f | -9.74433 | -43.95353 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e5817abb-98d8-3a8d-abf8-54592b33f7ed | -11.8451 | -47.60315 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b61a12df-73e3-31b8-8a38-5e3218e45780 | -11.90941 | -46.20082 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 572bc286-2eba-34f0-8a71-8e5b69a39d26 | -11.71046 | -48.86523 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5cf568e-a353-31f8-9ccd-cd9e935018c4 | -11.41172 | -43.32375 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8721c23-d67a-3e47-9ea6-88dac4ee57fc | -11.7187 | -48.87074 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa3237a9-9632-3244-ba95-5720080b7263 | -9.15444 | -48.05548 | 2025-11-16 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 942d3d9e-2ae2-3fed-b0a6-62c2bb339e0e | -6.1476 | -48.04642 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f1c1b03-3b75-34c4-9405-b587c20f67f1 | -7.71492 | -47.2911 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0daad570-84a5-3c2b-9512-a8e5df4c83d5 | -6.67764 | -42.03896 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b40c5a03-51f8-3817-ae26-169938653fc5 | -11.15877 | -49.44012 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7d56cd0-2339-3fbc-b0d5-af9b64882aab | -11.16711 | -49.44755 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 465c5ba4-8548-3420-96b8-07723a56d7ed | -6.21047 | -44.64751 | 2025-11-16 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eef68fbb-da40-3288-aee2-8c0127ee3652 | -9.844 | -44.18248 | 2025-11-16 04:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6800ea96-38ea-3d56-817f-cab5295a2dcb | -10.31565 | -51.92096 | 2025-11-16 04:57:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72b6d558-6e6f-33b5-a01c-7d03f67dca7b | -7.4431 | -45.22237 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0bfedef-8109-3758-9cd7-e25145f24e7f | -7.02137 | -45.1653 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dea98eb-b6fd-307f-be1d-8e73b7cf2dcb | -12.06696 | -48.21479 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b7c052c-9c0d-3ab1-9cf9-430ce88f5a94 | -12.00166 | -49.27014 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 693d32f8-0f74-39c2-b823-92b2ad972487 | -7.22397 | -47.98013 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa43d787-88da-3eae-857b-24bd21e6c588 | -10.54844 | -47.92411 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f64e4bf-dbbc-35b0-bcb4-1cdc0d0a307a | -6.70247 | -40.79837 | 2025-11-16 04:57:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| eb49078a-12cb-304c-b0c6-b6f09ad8191e | -12.06026 | -46.97448 | 2025-11-16 04:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6f4aa27-0c25-3f7d-8494-24ca164052d1 | -5.12396 | -55.97029 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16913bcc-b5e3-3b64-aeaf-751201dab94b | -10.6932 | -48.58805 | 2025-11-16 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 839c6c94-edc8-373c-b9dd-6fb3bb557425 | -13.55914 | -44.27455 | 2025-11-16 04:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c86dda3f-ef6d-368c-ac1f-85c4c1a36144 | -12.77471 | -43.71403 | 2025-11-16 04:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 644ba6e9-0022-3e87-ab42-8501f40d45e1 | -13.553 | -44.27386 | 2025-11-16 04:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d957bd94-06db-387b-b5e8-7f9dd21f7239 | -12.40507 | -48.096 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2416a305-7568-37ce-a3c9-1ba4729fba89 | -11.96609 | -44.95178 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c14db5f-83e3-39fd-b2f2-591f289aebaf | -11.84992 | -47.60376 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 353b19e3-87bb-3029-9b61-c9ac058c24b8 | -11.03913 | -49.5341 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d41cd06-212a-3153-bc3a-1cb828ab387e | -11.16188 | -49.44854 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ed2fbe4-75dd-35e4-ad30-f1163853a0d6 | -7.34643 | -43.33968 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54b81e1d-f9d3-3766-bd8e-2c6b0c874baf | -7.35302 | -43.33618 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18518f6e-2183-3ad4-8318-42931fc79dfb | -9.83811 | -44.18177 | 2025-11-16 04:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26082280-5a40-378e-8285-7f39914f0536 | -6.03208 | -48.18594 | 2025-11-16 04:57:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5eba09c-b1c6-3a56-a2f2-f040e9035aba | -6.81691 | -48.78891 | 2025-11-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04afe5bd-a990-3e5c-ac80-dbd2e11c3daf | -11.96106 | -44.95549 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b98cd158-9596-3bf4-b1ab-0d8e8f3cf9be | -9.57775 | -49.10497 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7590588-f4f0-31b5-8040-bce3319ac671 | -9.66022 | -43.89834 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ab123d8b-8be7-32e0-ba19-9f7a021b883b | -12.69597 | -46.79365 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 159105ff-9de5-3089-9bec-365a6450af9f | -10.6225 | -44.58247 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bb3f727-9a18-394f-869e-4d25249d6a02 | -11.15922 | -49.44241 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f05d931-a06c-345d-9408-55495bcd455e | -7.44699 | -45.22501 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f6c6eaf-b601-3865-b1e1-641756da2c7e | -8.57329 | -46.05132 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33593e81-7c95-312b-8cc4-6e22e47df94d | -6.13419 | -48.04816 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9fb6701b-9298-359d-a37e-26021a64ad1c | -9.74108 | -43.95822 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7bf4902-559a-34c8-8169-a1ae62d3cb58 | -10.70608 | -44.52631 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e7fd3fe-3b19-37da-a5fe-85020f9e7624 | -12.20951 | -49.61457 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f9fe240-313a-32df-9424-07ecd8e30b48 | -10.6594 | -49.37216 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7defcf8-a2f7-358e-8b98-a3d1ecdc4b9b | -9.72263 | -43.96054 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5814176b-77d3-397e-acfd-250a3ecdd42a | -11.16243 | -49.44463 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e928e0d5-f916-3e51-85ec-98e838e1ce44 | -9.64848 | -46.02517 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README57.md)
