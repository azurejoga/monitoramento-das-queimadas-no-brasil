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

## Dados Diários - Página 401

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e99b41-7680-3b6d-990d-b449693f5fd2 | -3.5726 | -58.5581 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 6230be8a-e521-3f6e-8a07-2dc4c6e480dc | -8.282 | -45.749 | 2026-10-08 19:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 4e335b10-2fd9-34c1-b854-7a2c6e23b3bb | -7.0281 | -45.3008 | 2026-10-08 19:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1151f7ff-fb73-3e48-9909-45a3ab3d8d5f | -8.9311 | -45.1355 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 250.6 |
| 337869cf-8c6e-30e0-b0a9-9533fe246a58 | -14.4345 | -43.9157 | 2026-10-08 19:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 220e4156-afb2-3137-86f2-500f60130d6f | -2.8896 | -54.1715 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 36df79b7-1ff3-3ec2-884b-9289d4cde91d | -3.8911 | -42.1187 | 2026-10-08 19:00:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 9d953a2d-efb6-3c90-9e43-5a7c85140c38 | -8.9497 | -45.1563 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 85bad847-309a-33f2-b798-e24310338fa3 | -11.6382 | -43.6166 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| bc7dc0f1-2952-3334-82fa-54bcd9e893fe | -13.3671 | -43.8742 | 2026-10-08 19:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 229.4 |
| acbe6a5b-f72b-3048-ab94-040d5f08eaa1 | -6.1615 | -47.9419 | 2026-10-08 19:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 3c1e4ff3-8333-3c32-b937-658829ee81bd | -6.1371 | -53.5056 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| df6653f7-50db-35df-8f2a-ddccbd6f7b4f | -11.1145 | -44.0009 | 2026-10-08 19:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 7aeed635-6112-3cc0-aace-60ec73dd1f6d | -13.885 | -44.1365 | 2026-10-08 19:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 329.3 |
| 77973e82-4941-3621-89a7-0eead4223418 | -8.9964 | -45.9002 | 2026-10-08 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 2cb193c0-216b-3c0b-bc2e-4a93d245eb48 | -15.9788 | -44.8676 | 2026-10-08 19:00:00 | GOES-19 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| e5baa441-41f7-37b5-8710-e5827fc2a769 | -4.1192 | -44.4119 | 2026-10-08 19:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 610546ed-2f4e-3d4e-bd03-14c2a774a6b5 | -2.9449 | -54.1099 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e941764a-36a4-3f8d-8a85-b27212b977b8 | -3.1114 | -53.7839 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c3232927-bbf5-394d-9634-3bf0d7ae72b1 | -2.9271 | -53.9295 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4e1c89a4-5f65-3196-bdff-d3f094fea14e | -2.9632 | -54.1296 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0db27339-09c1-393e-a64d-2bb764336eac | -2.5675 | -58.037 | 2026-10-08 19:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| ef229701-6269-3abe-9d67-f99e05b4d433 | 1.7671 | -55.5661 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 4251f6fd-6e87-3a83-bd41-a7c083d275c7 | -9.3394 | -65.4638 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 4c155b70-437a-31ca-ad54-f8daf9495b00 | -5.6136 | -44.3647 | 2026-10-08 19:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| f8cd6c16-c312-3965-af19-4af3eea4fbf3 | -3.2085 | -57.87 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0724471c-9d6a-3da5-b807-7fa62f80fe5c | -7.0892 | -52.6753 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 262.7 |
| f3ad8dc1-060b-313b-8a08-9f83b9ca5622 | -8.1985 | -46.431 | 2026-10-08 19:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6fe8b46d-994a-3811-8608-9769a7bad6c2 | -8.6107 | -67.0301 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 6cf8667e-73a9-3f34-ac79-e54a3e2588a4 | -2.7428 | -54.1347 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 48dfc3e0-123e-3d99-b0c4-02054a38d9e3 | -3.3452 | -50.4917 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a8f4fa7d-c82a-3e2c-92d7-c5e0a225654a | -6.4568 | -55.4609 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 816b413b-48cb-37d7-8ffd-cd89cc37db02 | -5.3953 | -45.897 | 2026-10-08 19:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b2890195-72de-3b93-b993-fe2e7a00b03e | -2.0834 | -46.5765 | 2026-10-08 19:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 2d782c0e-c962-3aa6-a72f-a91e91f92a9e | 2.0047 | -55.8786 | 2026-10-08 19:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 52d7868e-7d92-3a15-8df8-2a0f2161a474 | -5.9266 | -51.8358 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| b4f0bc88-672b-3078-8304-b052f71f42be | -8.0338 | -49.3985 | 2026-10-08 19:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6b4089fc-4cd2-3c33-8c5e-7b212a94fdad | -5.9267 | -51.8151 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 2217ee20-8a57-3447-9102-ff6362ad37ca | -6.0076 | -53.4919 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| c45e65e2-4ad9-3007-a425-973713911c7f | -16.3213 | -44.5598 | 2026-10-08 19:00:00 | GOES-19 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 13b988b8-f563-36b1-8693-4d66f33a34fb | -6.3283 | -55.3276 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| f269af38-04d4-3c19-a9c0-6c5bd250ae83 | -3.2634 | -57.8689 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 31def358-38db-3fe5-b64d-fcde2f088ef4 | -6.3133 | -54.8084 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| d1191ff9-0497-373a-97cb-cfc3392db1e4 | -7.7025 | -45.4436 | 2026-10-08 19:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 34300af3-d55e-3dc6-9c38-5c8170021631 | -6.1746 | -53.4427 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 762bc1a1-c336-3c5f-a9da-ae944827bd4d | -3.3452 | -50.4707 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 46ff9b37-9406-3d95-9bf4-fb0c4bf6d94e | -7.2185 | -55.1016 | 2026-10-08 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 3bfbf00f-e550-3ea3-83f1-5db5650cd4ed | -2.9979 | -54.7692 | 2026-10-08 19:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 10b6a9f3-918d-3820-aab4-42ff63dd4dfc | -2.7429 | -54.0945 | 2026-10-08 19:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 645755a3-c19b-35b3-9ff2-8f57bf65dd94 | -4.7404 | -55.6522 | 2026-10-08 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 9ecd8a0d-f3a9-327b-9b4d-495aa2cdc457 | -11.7335 | -43.649 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 8142d95c-39e5-3e8c-bcd4-ff1fc3052b8d | -3.1697 | -58.6437 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| f67143bf-2d91-389b-8ac1-c9b2e69dc1ff | -3.188 | -58.6241 | 2026-10-08 19:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| fae9c1d4-2612-3e94-af3f-e5c03f442945 | -9.5003 | -66.8017 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 324bfc7e-b0da-31c8-82d9-5e4f79ddf2c3 | 1.6937 | -55.6263 | 2026-10-08 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 9e3588e7-db88-359e-b925-09f8d791be0d | -2.572 | -56.1842 | 2026-10-08 19:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 239.3 |
| 50220df5-6955-36f8-864c-4dbc062bc39b | -9.3395 | -65.4451 | 2026-10-08 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| fd2afed3-deac-3626-a2ff-293edd8fe916 | -3.4312 | -56.9307 | 2026-10-08 19:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c92497f4-ec39-3277-8cf6-f7dffe26d06a | -5.3718 | -44.1981 | 2026-10-08 19:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 3ff1d920-49a1-3a55-9675-de76b43e7b39 | 3.5448 | -51.2772 | 2026-10-08 19:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 30091aa2-e80b-3c5b-a3cd-11a1026aaa3a | -3.1787 | -50.5807 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 214.5 |
| 20e01f34-1045-37d6-bd2e-3a0cfb4b7438 | -5.3951 | -45.9194 | 2026-10-08 19:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7333a0b1-048e-38cd-bae4-0001d0cc74fd | -11.6387 | -43.5929 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 422.6 |
| ad38fc50-203d-31c0-aca3-07c3df95b4c5 | -6.4764 | -55.3004 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| c4e0ea00-f264-3f90-be8a-826a86fb74bc | -2.853 | -54.1322 | 2026-10-08 19:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 40274d28-e95a-3aed-b7f7-1d9dbfbf83db | -5.4266 | -46.6516 | 2026-10-08 19:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 073cdb21-dd11-3061-a2d3-0681e23ac989 | -6.2355 | -52.6841 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| af5f90f7-3806-312c-969b-69325b5817ee | -8.2176 | -46.4068 | 2026-10-08 19:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9644a38c-168d-3e2d-83e4-80b5ba5e967d | -5.3763 | -45.943 | 2026-10-08 19:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d20544b2-5836-353f-a2eb-5de42c463cde | -3.8413 | -44.1283 | 2026-10-08 19:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 47b025e4-d9c3-3603-be29-28f06dfc750a | -3.7057 | -57.0998 | 2026-10-08 19:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e16f6754-8b50-3aee-b2c1-aa97fd747baf | -14.4339 | -43.9396 | 2026-10-08 19:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 6b11cfe2-b476-3de8-8ae7-460c1c35053d | -3.1951 | -42.9538 | 2026-10-08 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c836f431-f76f-31e8-9fd4-dc487f5ad63f | -3.3912 | -58.0017 | 2026-10-08 19:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 82961809-a55b-3765-99e7-63a04d5c75f0 | -6.0386 | -51.7261 | 2026-10-08 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| a81f3e12-4231-31f0-90ca-209bba0441fc | -7.6397 | -44.3764 | 2026-10-08 19:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 701398c6-0aae-37b3-b568-af28f922f820 | -8.5368 | -67.0135 | 2026-10-08 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| a81e0ad6-55fd-3a1d-9381-3a8f0d6211f2 | -3.2577 | -54.0217 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 210.5 |
| 4d4ba692-510b-37fd-9658-930f6effa044 | -3.2268 | -57.8696 | 2026-10-08 19:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 158c1362-a789-3603-be91-d23432fbc8d4 | -5.8801 | -45.9537 | 2026-10-08 19:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6bdfb26e-ffde-338e-96b6-637217fcaa02 | -6.4949 | -55.2995 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 446.3 |
| 1e8bcdb3-f115-32e5-9f1e-0cd765d0a436 | -3.1787 | -50.5597 | 2026-10-08 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ec66354b-8d03-322b-a298-6cf92354ea57 | -8.9501 | -45.1334 | 2026-10-08 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 10af2ccf-e653-3e7f-bb47-46a01f259677 | -14.4585 | -41.2104 | 2026-10-08 19:00:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 3d9b4408-003f-3e58-ab60-73b0e5c97ffc | 3.7276 | -51.6437 | 2026-10-08 19:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 632771d0-dac6-39e7-9436-ab108a0fee41 | -11.7738 | -43.5482 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 950b5d4a-be1b-3ad7-bf51-2a9e6e446141 | -11.755 | -43.5275 | 2026-10-08 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| ab6c09ba-3bf4-3639-8a8d-0c509cb55a03 | -3.93 | -56.0143 | 2026-10-08 19:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 183.6 |
| 1bf0db75-8aea-3bad-a1cf-870877b6dd38 | -7.8722 | -45.4047 | 2026-10-08 19:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| da503704-0352-3b39-9789-bdad920b50b1 | -11.7756 | -45.5725 | 2026-10-08 19:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| edb214dd-4133-3917-93ce-3f51f4b528d3 | -6.8319 | -39.3213 | 2026-10-08 19:00:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 66bfb9e7-4b52-3af2-b35e-3c7c639732f3 | -3.2577 | -54.0016 | 2026-10-08 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7348c872-f6c3-37ac-a2a7-349da7f2ed3f | -3.9121 | -55.8964 | 2026-10-08 19:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ea565e20-9eee-34dd-9c01-beb5041205f1 | -8.9772 | -45.9249 | 2026-10-08 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 9c8bccaf-fbe5-3212-9ffa-2cc0e71fe444 | -3.1114 | -53.8041 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e66d6873-561d-378a-8dd7-fa68f7a01019 | -14.0873 | -43.7671 | 2026-10-08 19:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| faa910d9-cb89-339e-a1d0-ae0fe2a7d9de | -6.0386 | -51.7261 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2c247907-b63b-30a6-847e-e542c4e9fdb8 | -3.67 | -56.8074 | 2026-10-08 19:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bbf6e6ba-38bd-3cd9-984c-05d8ed1cf1d1 | -11.6387 | -43.5929 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 346.8 |
| 32211c10-26b4-3cd2-b059-ca83dc20fb72 | -2.8896 | -54.1715 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |


[Clique aqui para ver as próximas entradas](README402.md)
