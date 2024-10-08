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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1084a1c4-d88e-3dcc-afc6-ee51f3801f58 | -12.7416 | -43.436401 | 2024-10-08 00:05:45 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6c9ba8-0cd6-30f9-8580-fed64a5e97e0 | -12.7434 | -43.445 | 2024-10-08 00:05:45 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af7877fc-c62b-365b-86d8-1adad03d5695 | -12.7318 | -43.438499 | 2024-10-08 00:05:45 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3794342a-3308-3043-840f-3949de57d4ea | -12.7336 | -43.447102 | 2024-10-08 00:05:45 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 538e0e21-c1fc-35a5-8b43-66643e127705 | -12.8713 | -44.604099 | 2024-10-08 00:05:47 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1361c5e7-0b76-3712-80d5-a5e2ee6c395f | -12.5812 | -43.3549 | 2024-10-08 00:05:48 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81c61da4-955c-3f98-b92a-9de047650baa | -12.9988 | -46.193802 | 2024-10-08 00:05:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6417ea8b-d779-31d2-9641-5153a7c92d7c | -8.5364 | -67.1246 | 2024-10-08 00:05:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 40898180-3d2c-30e8-9991-14dd26f50540 | -8.5549 | -67.1242 | 2024-10-08 00:05:55 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 01cefc05-74ad-3607-ae7f-156b12330a75 | -11.8152 | -42.7882 | 2024-10-08 00:05:58 | METOP-B | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 10ba9234-3d89-300c-a7f0-b0c0f4dc9d97 | -9.4087 | -66.5438 | 2024-10-08 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 30342849-5436-3728-a9c2-56320a5140fd | -9.445 | -66.7289 | 2024-10-08 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b1c3e863-8396-399d-9429-03ac526d14c3 | -9.4635 | -66.7283 | 2024-10-08 00:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c0abbb4a-cfb4-3e27-ad5a-0b6237e7f8c3 | -9.572 | -67.4315 | 2024-10-08 00:06:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 398329c0-4393-3ca1-8dcb-c5978a5c64f9 | -10.1143 | -36.186699 | 2024-10-08 00:06:01 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0298d18c-fbf3-371e-999d-73c74d453a2d | -10.1166 | -36.196499 | 2024-10-08 00:06:01 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd8b127c-dafc-38c0-b234-de907443953b | -9.7241 | -66.5716 | 2024-10-08 00:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d0b848e1-35f0-3db2-a521-b8f868943942 | -10.1046 | -36.188999 | 2024-10-08 00:06:02 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f0451f3-61c9-3e9f-b361-48dedaf43b7f | -10.0363 | -36.379299 | 2024-10-08 00:06:03 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| e49e373d-bb54-3d96-8143-ab343393a5f7 | -10.0386 | -36.388901 | 2024-10-08 00:06:03 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| e88a38a6-cfd1-3348-a376-8c320f7f0e79 | -10.1261 | -55.2093 | 2024-10-08 00:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6aacf10f-9e97-33c7-aed7-98d5f48e0734 | -10.1263 | -55.1891 | 2024-10-08 00:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| bfa48381-2d36-3722-bbd1-0e3148a6cf28 | -10.1448 | -55.2078 | 2024-10-08 00:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6ef4f2ad-9c35-365b-a5b1-a177851d3efe | -10.1451 | -55.1876 | 2024-10-08 00:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 9bd6b1f0-5dd6-37b7-b6a4-2be045b55d8e | -11.7772 | -44.499901 | 2024-10-08 00:06:05 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4ef7c56-372a-3212-80c3-8144b3fe610f | -11.7791 | -44.509399 | 2024-10-08 00:06:05 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad7239f9-110f-359a-a930-d2ff42340ce2 | -11.917 | -45.673801 | 2024-10-08 00:06:06 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3979db51-38bf-3c07-968c-750a0bd4fc2f | -11.9193 | -45.685101 | 2024-10-08 00:06:06 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05674306-0c85-3817-97b2-bf9a9638193d | -10.6256 | -55.9154 | 2024-10-08 00:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a265e6d2-0e02-36af-a499-e6eaaf297e92 | -9.8088 | -36.4645 | 2024-10-08 00:06:07 | METOP-B | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c58f56f4-ed5e-354d-8b85-dfebd4e418d7 | -10.8754 | -63.9169 | 2024-10-08 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 20303d60-15d0-393f-a209-98a7ab226701 | -11.0991 | -54.0285 | 2024-10-08 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 1e8ff944-d8d5-356f-8a93-eda4c7695ddc | -11.0994 | -54.008 | 2024-10-08 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 11392e23-be9c-3804-84be-e48787a43d78 | -11.118 | -54.0268 | 2024-10-08 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ceab038c-d0cc-3073-b572-3afabe1b626e | -11.1183 | -54.0062 | 2024-10-08 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 19000939-5e34-3c17-bed9-1cd9a560e025 | -11.5232 | -65.1559 | 2024-10-08 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6c146264-57f3-3183-aba7-c5ad091ddee1 | -11.5233 | -65.137 | 2024-10-08 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 618ee54e-b9cd-3434-b295-465a910be104 | -11.5421 | -65.1362 | 2024-10-08 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9840736c-d83d-3761-862e-125763852d4c | -11.6808 | -64.0121 | 2024-10-08 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 26440ccb-c1cb-36a9-9131-cc04d4eea937 | -12.3616 | -47.0986 | 2024-10-08 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 546e11c8-9203-3b60-b698-3113e05cc9c6 | -12.362 | -47.0761 | 2024-10-08 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 59f80119-d9dd-3656-b1fa-2792081129a8 | -12.1913 | -63.6628 | 2024-10-08 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9a83227d-a769-3cb2-b68d-39dcf95ba3c1 | -12.4729 | -47.307 | 2024-10-08 00:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 73be4a37-83cc-3fdc-8587-952f416331d7 | -12.4414 | -63.018 | 2024-10-08 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b6a74b1c-4716-38ed-9d11-0305379fc302 | -12.4416 | -62.9988 | 2024-10-08 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f6bbc8b1-bba4-34dc-bc89-443cae9035d9 | -12.4603 | -63.0169 | 2024-10-08 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 67ec97e9-5727-3945-855a-2c251b01ab98 | -12.7064 | -62.9645 | 2024-10-08 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b71fb461-d830-34b1-bf42-0297685aec26 | -12.7065 | -62.9453 | 2024-10-08 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 51a3ed5c-71c1-32b6-853a-603e73d9c6c6 | -12.8242 | -62.4573 | 2024-10-08 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 5bafa6f1-4438-3d7b-b933-88acb2b7e302 | -9.2517 | -37.737701 | 2024-10-08 00:06:21 | METOP-B | INHAPI | ALAGOAS | Brasil | 2703304 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ac5f5b22-b03a-3703-8994-592b2e29a7c8 | -13.3978 | -61.9376 | 2024-10-08 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 424d6bf5-ff11-3256-a0ae-ffb8cbf58ecd | -10.4692 | -45.089699 | 2024-10-08 00:06:28 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1c849e4-690b-3b81-883f-e017efcd7428 | -10.4712 | -45.099602 | 2024-10-08 00:06:28 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be612982-5b09-329b-b6d5-c73e6e24262e | -9.9525 | -44.098999 | 2024-10-08 00:06:33 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05eb30e7-3816-3f95-92b6-93581f5182ce | -9.9409 | -44.092602 | 2024-10-08 00:06:33 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61135f67-0142-3045-ab4e-4b4b0b3d48ab | -11.3387 | -50.9678 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e30f3ef-2c2f-3d7e-80ce-3c29b188183a | -11.3435 | -50.993099 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9f026fe-d398-3784-8bcd-18a0cea20907 | -11.3291 | -50.9697 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7dde8220-6eb2-3281-ae83-b80a58a754d0 | -11.3387 | -51.020302 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e505ab45-908b-3c1f-a60c-9d911d4f90cd | -11.3194 | -50.9715 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd2f200c-626b-31da-aee6-3db7d1beb2f5 | -11.3242 | -50.996799 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4f1883d-2955-3b40-96c5-7ae03125b388 | -11.329 | -51.022099 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad70083-7321-3167-9bf0-90a18f712b44 | -11.3097 | -50.9734 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72e56e5e-6fd0-39c2-8812-35be604c6c73 | -11.3145 | -50.9986 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab7b9908-a7f2-3447-9856-09993b3222ba | -11.3193 | -51.023998 | 2024-10-08 00:06:33 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1be9cdb4-60c9-37de-aaa0-bd245236241f | -10.1174 | -45.215599 | 2024-10-08 00:06:34 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b66a6286-9338-343a-91fd-67a7a544e6ef | -11.3 | -50.975201 | 2024-10-08 00:06:34 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d294773b-8eca-33ec-bfd8-18ab42ea726b | -11.3048 | -51.000401 | 2024-10-08 00:06:34 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5941ea31-7eac-35f3-9803-4d0c634659a9 | -11.3096 | -51.025799 | 2024-10-08 00:06:34 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be6f682d-2509-33c0-95bc-eddd8c66e171 | -11.2951 | -51.0023 | 2024-10-08 00:06:34 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a58d27ba-d524-3759-a1c6-f877796e74a0 | -16.0951 | -50.1883 | 2024-10-08 00:06:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e3d173f2-7b55-37a0-9f3c-b4c956f0686c | -9.5252 | -42.973999 | 2024-10-08 00:06:36 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a2d5fa23-37c3-3abe-ac6e-1790a82dffcc | -9.5269 | -42.981602 | 2024-10-08 00:06:36 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 518d05eb-31e7-343e-8efa-d5527f068df6 | -9.5285 | -42.989201 | 2024-10-08 00:06:36 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f19c710-6c9b-3849-94b7-cf6c8a2bd3a2 | -11.2039 | -51.314499 | 2024-10-08 00:06:36 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f00c9ad7-8892-367b-9bf4-eeb8ef716468 | -16.4353 | -57.3393 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 197621ac-8403-33ee-9bc0-a7b527452936 | -16.4356 | -57.3189 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| df70bb45-4073-33dc-940b-5e2102ba506c | -16.5075 | -57.7183 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| bdca402d-ca16-3ce0-a9fe-9542ab58a3f9 | -16.5267 | -57.7365 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 8d0bb588-dfb0-30c1-852c-e32b8587d086 | -16.527 | -57.7161 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| d569c17c-b314-38bf-85af-246daf423372 | -16.5462 | -57.7344 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 9facd768-c127-3418-bfcd-a1a45ce89135 | -16.5466 | -57.714 | 2024-10-08 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| ff359334-5b8b-3a35-8a2a-25b4eab49718 | -9.5431 | -44.054001 | 2024-10-08 00:06:39 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 840afc62-4087-36ac-aba2-ba9bd29bf3e1 | -9.5449 | -44.062401 | 2024-10-08 00:06:39 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c75995b5-9db1-3f96-b937-e124430095bc | -9.5468 | -44.070801 | 2024-10-08 00:06:39 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 944a2755-3af6-3965-8cc4-ee7b9785124f | -9.5333 | -44.056099 | 2024-10-08 00:06:40 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8ef3aa-c574-33ef-b8fd-9fab39a97969 | -9.5351 | -44.064499 | 2024-10-08 00:06:40 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52e825ff-c3d9-3ad4-b9ed-d75cbb41bc49 | -10.5186 | -49.075901 | 2024-10-08 00:06:40 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 247bd96f-4972-3929-9992-e732da97373d | -8.8054 | -41.018501 | 2024-10-08 00:06:41 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b39ef494-a780-3bf9-94ac-de0f8ec09c23 | -8.807 | -41.025398 | 2024-10-08 00:06:41 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8d6686f9-cd86-3b90-a8e4-754fca181b50 | -8.8085 | -41.032299 | 2024-10-08 00:06:41 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0adeca3d-461e-3c86-955e-dd8a7d1f5577 | -16.992 | -56.721 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| f9038299-7397-33b4-845b-b5b1d47f34f5 | -16.9924 | -56.7003 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 85281db1-c4d6-3d5c-a4e3-679e1cf8c935 | -16.9927 | -56.6797 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 9d1f653b-8721-3b94-90a6-04e49ff764d9 | -17.012 | -56.698 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| ac7837ad-5f10-3291-be52-391df21bcc56 | -17.0123 | -56.6773 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 3f8c20cb-9b3c-3e60-99f1-936c7b5ca336 | -17.0127 | -56.6567 | 2024-10-08 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| f5905940-b17c-3752-aa58-4d10c39f288c | -8.8253 | -41.3839 | 2024-10-08 00:06:42 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 39d7e11b-4a30-310d-900f-9137a29eb17f | -8.8268 | -41.3908 | 2024-10-08 00:06:42 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9c903306-f3e7-3909-b958-8663ec5a5132 | -7.3246 | -35.132301 | 2024-10-08 00:06:42 | METOP-B | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README4.md)
