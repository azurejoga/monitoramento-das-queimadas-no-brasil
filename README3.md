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
| 6b5e39d6-6566-391e-a9da-cddf290d0239 | -4.00408 | -43.75973 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b18258e2-c915-328e-b7c4-3aaf3b61f867 | -6.0113 | -42.34918 | 2024-12-18 00:22:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e2e1c7c7-8a76-3f28-bfb0-76bb3f803310 | -5.2966 | -44.94047 | 2024-12-18 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c487f17c-0be6-3c1e-a310-f14d19c03d58 | -5.50994 | -44.32633 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed3d3e8f-0d5a-32ed-943f-09196eebab2c | -4.87585 | -41.38759 | 2024-12-18 00:22:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c026de01-465b-37c8-9f36-7ebea09ac9da | -4.30742 | -43.89012 | 2024-12-18 00:22:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 82efb6f5-741a-38f4-a5b9-55d56acfee38 | -4.44373 | -38.06638 | 2024-12-18 00:22:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 24731029-16e8-3fb9-9d8e-ec1cfb818a89 | -6.44504 | -40.62155 | 2024-12-18 00:22:00 | TERRA_M-M | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 92910e4b-a5cc-3323-ad69-1992f74744e7 | -3.07629 | -40.04885 | 2024-12-18 00:22:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 08631350-f208-3d51-bc1a-d87e47182271 | -3.87794 | -47.0328 | 2024-12-18 00:22:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| abece81d-08a8-311a-86b1-2c9e27b314c6 | -4.13521 | -46.80639 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5bed823b-f8ed-375a-a273-7a015d717b22 | -6.76321 | -40.13336 | 2024-12-18 00:22:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 7af254f2-0aba-3437-9446-863710c4c0df | -10.252 | -36.37769 | 2024-12-18 00:22:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2ab2675b-95d6-32a7-8e80-86cc46d0d73d | -4.92162 | -41.32706 | 2024-12-18 00:22:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d788b63f-2e63-3851-98be-5ae5de7c3c3b | -5.92007 | -48.06256 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d2614dc3-6f29-3550-885b-8bc23a428764 | -4.11243 | -46.72479 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1b9674d7-6403-3acc-a313-c1d25f3de483 | -6.43618 | -40.62282 | 2024-12-18 00:22:00 | TERRA_M-M | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 92e8d5d3-387b-33a1-bfce-a82fe62007d2 | -7.70595 | -35.10114 | 2024-12-18 00:22:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| f8685195-58ac-3bb0-85ee-3a9ba94fcc75 | -4.11723 | -43.56128 | 2024-12-18 00:22:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d211576d-5d0e-3da0-8627-9e4ede58f2c0 | -6.06417 | -44.04435 | 2024-12-18 00:22:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6e6367d8-ba6a-3bc2-aa62-832bf2537712 | -5.34 | -41.21942 | 2024-12-18 00:22:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d3e6f9f5-7499-3bf6-b53a-bc00097b5a2e | -5.86204 | -39.16982 | 2024-12-18 00:22:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 23.9 |
| e30171cb-c77a-3082-b492-e02f874ef9e8 | -4.10277 | -46.74321 | 2024-12-18 00:22:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 8bca3db5-3742-3c33-a9f8-9a6484e855da | -5.70822 | -41.41389 | 2024-12-18 00:22:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b5784b86-ab71-33ed-b346-cdf642fa29b9 | -6.39481 | -35.06516 | 2024-12-18 00:22:00 | TERRA_M-M | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 29f0686e-df87-3b71-b40d-6ef770b9c0f2 | -7.70858 | -35.11781 | 2024-12-18 00:22:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 26485ba8-2a36-361a-8695-3b681178d8c7 | -9.48891 | -35.89286 | 2024-12-18 00:22:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 31cbc925-67e6-3b49-9b8e-157484821921 | -3.9066 | -46.665001 | 2024-12-18 00:23:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44fae719-cb9c-39d2-9bcf-f78f20268586 | -9.2995 | -40.237301 | 2024-12-18 00:23:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f1d15d4-1c50-3917-aaa8-978d9503d0c5 | -11.8681 | -43.830601 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 048982c3-87d7-3e33-910a-f1d97c0a8161 | -11.8638 | -43.812401 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 800d8572-4c64-3d9a-8b6a-eba7aa9a2342 | -5.3362 | -44.297699 | 2024-12-18 00:23:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b41c446-de47-3d9d-80a9-1c4151f72920 | -5.3338 | -44.287399 | 2024-12-18 00:23:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 376aa143-5340-37dd-922a-05a23de092dc | -10.5058 | -49.111401 | 2024-12-18 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa114cf8-1308-3097-b699-23e56f826cc7 | -11.8584 | -43.833 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b089d345-837a-3660-9666-a08ef99d8ce5 | -4.6671 | -44.518101 | 2024-12-18 00:23:00 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10f4dc39-936a-30d0-9a73-d3537e5c5d7f | -4.0071 | -46.924198 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f37f0fc9-7788-3a16-869d-e9817754d885 | -5.9254 | -48.061001 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5313d8c-110d-3c07-8d4a-38ad5cc4654f | -4.959 | -43.698799 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b469d32-92da-3f73-912b-bec80e7a811c | -4.8001 | -44.030399 | 2024-12-18 00:23:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aeccab8a-8174-3df4-b36c-38b20d91b344 | -3.8663 | -47.029301 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d54aa63-7e8d-3b0e-898d-5974f8472ee2 | -5.9405 | -39.658699 | 2024-12-18 00:23:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 70979f0c-0a1f-3ba6-ba11-cef5426e69d2 | -4.6768 | -44.5158 | 2024-12-18 00:23:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9ed946-8efc-32e2-b7f8-d8d0e502f782 | -5.3436 | -44.285099 | 2024-12-18 00:23:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bc08899-d3da-3114-8c02-2a02a85102e9 | -10.3615 | -47.765999 | 2024-12-18 00:23:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fec319d1-2954-3e1f-ba0a-644dd117f86e | -20.7799 | -49.827801 | 2024-12-18 00:23:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f039f3c7-431b-3845-9c6c-6a7af40da15d | -11.866 | -43.821499 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 304874eb-f09d-3eac-94d0-3f67580a869c | -4.0319 | -47.032501 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f2921a4-8dea-3256-baf7-8fa3975c2816 | -3.8744 | -47.019402 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 167ec457-d234-36a3-be00-30f58f67a156 | -6.9738 | -43.553902 | 2024-12-18 00:23:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ddb92dc4-a38c-3bdd-a5fe-00f474a5e9de | -6.0587 | -44.040901 | 2024-12-18 00:23:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31130a23-1e5b-3d13-be6c-7da7564bfd0b | -4.9714 | -43.708 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31e13b7e-1fbf-32f2-9333-f37ca5f66f97 | -5.927 | -48.068001 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bdc7581-b8f9-343d-a894-f052d92d7a47 | -3.0189 | -45.222599 | 2024-12-18 00:23:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb0a4561-6c70-342c-beed-32e679015b71 | -20.781799 | -49.837502 | 2024-12-18 00:23:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2800715-443b-3549-a2a3-f3e46e96ec54 | -5.9368 | -48.0658 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 866ede15-77a9-3e40-bbb4-710d20b029f3 | -20.7384 | -54.384899 | 2024-12-18 00:23:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c0500418-005d-3f51-bda6-0348b3a88b3f | -6.1886 | -44.418701 | 2024-12-18 00:23:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e64eb2d-94c6-3e68-9e84-e0a2bf5be0d8 | -3.0383 | -53.879002 | 2024-12-18 00:23:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f121393-18b2-3db2-82a5-2ba3d46bbc3f | -4.9519 | -43.712502 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4fd6f7-8258-3295-aec9-d2d24b1e5808 | -9.2954 | -40.2206 | 2024-12-18 00:23:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 799f59f2-1ea4-3685-aa30-680047930dd7 | -2.139 | -46.456402 | 2024-12-18 00:23:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265b9d27-9d41-360e-b5f4-59ce439aaadc | -11.2324 | -49.001701 | 2024-12-18 00:23:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65c9cf80-1560-353e-8cf5-170e339bdd9c | -3.0212 | -45.2323 | 2024-12-18 00:23:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51fa50f7-c8fb-315f-9556-6ac8835b95c6 | -20.741501 | -54.4035 | 2024-12-18 00:23:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d91351d0-fb10-3d9b-bf9b-f62f01c9bb3c | -5.9239 | -48.054001 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7608a77-371a-3bf4-8dc4-8448b6d0ca17 | -7.1924 | -44.919998 | 2024-12-18 00:23:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2abf44-8232-391c-a774-a0a8e33b82e3 | -3.8779 | -47.034901 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59ba4167-d5da-384d-8846-4a1bee0c226e | -9.2857 | -40.223099 | 2024-12-18 00:23:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ec63efa4-b090-3c7e-945c-a63e4eefc131 | -22.3015 | -49.697899 | 2024-12-18 00:23:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f82b4649-de1f-3893-8dfe-e8a5bdd5d33b | -21.069401 | -48.749599 | 2024-12-18 00:23:00 | METOP-B | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fd64413-7663-3698-8158-6d48fa94fe90 | -5.9418 | -43.763302 | 2024-12-18 00:23:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c64b783f-08d9-31d5-9564-822b1dc06830 | -4.9563 | -43.687401 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c46b57fb-0291-3d94-b35c-06cceca20dbf | -3.8646 | -47.021599 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2fe54c9-aadf-3de5-83ad-084462a7fb34 | -10.5074 | -49.1185 | 2024-12-18 00:23:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3764ec28-6211-3f8a-9b91-fa46d69a0230 | -4.9644 | -43.7216 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cc77a2d-4d20-3b06-bee5-235ad1f147b8 | -4.0123 | -47.0369 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5836227d-cde9-34e9-b7e2-4c53fd6a802c | -21.3571 | -48.604099 | 2024-12-18 00:23:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e4bd30e-6095-3f79-92e4-835015ef1e89 | -6.0489 | -44.043201 | 2024-12-18 00:23:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1f5f2b9-c883-38e6-ac64-3c1b13141406 | -5.346 | -44.295399 | 2024-12-18 00:23:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8d7da32-e2ae-35dc-b764-cead1798a395 | -4.967 | -43.732899 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76e01a43-f230-3df5-ae37-e2f80b6c14eb | -4.9492 | -43.701099 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84c2a3fe-588a-3a43-9115-ae538a54b640 | -19.069799 | -52.8368 | 2024-12-18 00:23:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d26349db-e2fd-33e4-af35-254d71a95225 | -22.299601 | -49.687801 | 2024-12-18 00:23:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c6e6b56-086f-3f1e-a4a2-fe570c1c854b | -5.9456 | -39.679501 | 2024-12-18 00:23:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c750e90b-f97f-362c-9183-9a1f03f38bf9 | -4.9331 | -45.0863 | 2024-12-18 00:23:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a26dac5-db58-3957-842e-cb51b2157536 | -11.8563 | -43.823898 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f74345b8-0899-3e37-9855-ac25d766227f | -9.2912 | -40.2038 | 2024-12-18 00:23:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 38431b07-129b-3064-b3b5-61c5c33b7488 | -5.9337 | -48.0518 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4d233b-78e8-311d-a561-4505b142ac4a | -19.060101 | -52.838799 | 2024-12-18 00:23:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f7711e06-bf2e-361c-bc02-9b6454470a7b | -3.0234 | -45.242001 | 2024-12-18 00:23:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3e2902-987a-3555-9875-bdd8dd3b182d | -4.9687 | -43.696602 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3c1139b-ce6f-3cd1-90c3-6e7cdc193cd3 | -4.9661 | -43.685101 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5bc5204-169b-34be-9979-2aaeb04b0ee1 | -4.0382 | -47.0149 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2d7a3fb-86f8-3d21-892a-2b7a8cff6ba1 | -3.0662 | -40.038601 | 2024-12-18 00:23:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0fa12189-e47c-3419-b597-49c1465f9873 | -6.9666 | -43.567101 | 2024-12-18 00:23:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57942630-3d2b-3e5d-845e-eaf7597194c7 | -11.8541 | -43.8148 | 2024-12-18 00:23:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 571242ec-76b0-3b4b-a850-d84d52675524 | -5.9352 | -48.0588 | 2024-12-18 00:23:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7406d9e7-38b5-3c4f-ae10-edee0c415102 | -2.1409 | -46.464901 | 2024-12-18 00:23:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0793f9f3-b1af-37f6-a03e-fba8094cef74 | -4.9617 | -43.710201 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
