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

## Dados Diários - Página 223

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9d3e831-c84e-35f2-9aaf-8948ea4e4157 | -4.7404 | -55.6522 | 2026-10-08 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a0e8da39-7435-3e29-a619-3543830b6b20 | -3.1879 | -58.6433 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 335.5 |
| f9507fb5-be28-3c7f-a9d8-ba601c3004c4 | -2.4806 | -56.0875 | 2026-10-08 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 960ad44b-0f7f-3551-b0bc-07d4efc68b39 | -13.7086 | -49.1263 | 2026-10-08 15:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a6671d58-b98b-3b36-83cc-9406c5f585a9 | -2.4804 | -56.1466 | 2026-10-08 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 333833db-3bca-355a-aaf6-d18e754c3535 | -1.146 | -54.2199 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e7c98264-9968-376e-84a7-ed55cc0a2e66 | -12.1545 | -44.7547 | 2026-10-08 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| ce5ce6d5-2f22-3eb4-8637-b34d88ebe1db | -3.0448 | -57.4657 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d1bbbc58-41ba-323a-bb58-c795f1c7931b | -3.095 | -59.1832 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| cbc3f092-5fa5-36cd-9125-47214aeb029e | -2.8897 | -54.1514 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 70ccc3ba-22b6-366d-9b8b-cf43431b9cfb | -3.8338 | -57.1746 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 59334e59-f8e1-3efa-9ce4-ce1e4a6ceedb | -2.1544 | -54.4668 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1aa6738c-3ebe-3b61-9c65-934d7cbdd544 | -5.372 | -44.1751 | 2026-10-08 15:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 427.2 |
| 59a77fb8-ad28-3f07-abdd-073db7802839 | 1.6385 | -55.785 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ad09b5b3-5f27-36db-b603-8c8f637ab3e1 | -3.0447 | -57.4851 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 28b9e75f-dbb3-303f-a673-41ed2c3b3619 | -3.1133 | -59.1828 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a05b6f64-1ebc-312a-a5d1-7dd57b92b2ce | -3.3175 | -58.1582 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f1756178-54e9-332b-a579-f55f2dd26fed | -9.4819 | -66.7836 | 2026-10-08 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| efb4b06f-4e13-3117-a3e3-41f431f44cff | 1.6568 | -55.8045 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| c62f588b-a334-3513-aae3-aaade3121605 | -1.6213 | -55.1321 | 2026-10-08 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 276fefc7-e6ac-399c-96ff-49212e3d1988 | -5.8599 | -53.4586 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 26e28927-828e-3704-b31b-57a3e0fa8340 | -1.2086 | -49.0412 | 2026-10-08 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e684c734-afe2-39f1-b283-81e97a388c62 | -7.9046 | -63.7129 | 2026-10-08 15:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a9edeca2-62c0-37e7-898b-473a9d606ab0 | -3.1697 | -58.6244 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 93cc30f0-6bfe-3085-8d16-07e1ceca59e4 | 2.0047 | -55.8786 | 2026-10-08 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b32f2956-b3fd-3ad9-8ad4-ed03471da178 | -3.426 | -58.5999 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ef3a44f0-ccde-3451-8096-75f70b1e01e6 | -9.1408 | -64.3836 | 2026-10-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 16020c1f-01c9-3c3c-934a-5ddd4a444946 | -12.4644 | -62.5173 | 2026-10-08 15:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f299ef0b-509d-3293-ac5e-f8b4b40c4e9c | -6.1952 | -53.1362 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4ddf42c5-4f5e-343d-8e59-b006ce7bc4db | 2.764 | -60.0297 | 2026-10-08 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 866ea632-1f69-326d-a8e1-59d14abd665b | -1.4569 | -54.7562 | 2026-10-08 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 48dddb15-289d-3773-8059-99fd1731a55d | -6.1971 | -52.8705 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| f32d94c6-5c6a-39b5-ad85-f42be712d234 | -3.3723 | -58.1957 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7c1cfafd-fd9e-3ddd-ba62-0646e6fe0964 | -3.0992 | -57.6589 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 24b0a8bd-91aa-306b-b843-590935d24aa3 | -11.2295 | -46.2403 | 2026-10-08 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| d3d7e268-d6c7-3caa-931e-57579a400125 | -7.8878 | -54.9822 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3937e94f-39a7-3977-b846-ca03aa55b4db | -8.9501 | -45.1334 | 2026-10-08 15:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 474.0 |
| a1b264ed-129f-3cb5-9fc4-cc8df804bc44 | -2.2223 | -56.9152 | 2026-10-08 15:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 6017d08b-96e4-36ce-a983-9172dda38cf1 | 2.7458 | -60.0109 | 2026-10-08 15:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 9e762fef-37e5-3561-8edd-2da4fc7c4333 | -1.2265 | -49.381 | 2026-10-08 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 00c2fe1f-43e1-3b9a-92aa-9010ec572327 | -3.0631 | -57.4847 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| b2c2f32f-fa36-3ff5-861b-f01ea5a7842e | -3.3319 | -59.5043 | 2026-10-08 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a665a753-1387-3459-85a3-bdd46ce9245d | 2.7641 | -60.0106 | 2026-10-08 15:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 84bba53d-e120-3fe7-bb97-bf0f65032f1f | -3.3323 | -59.3703 | 2026-10-08 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d08e51c0-a911-38fa-8870-753cc7c82a00 | -9.5313 | -46.8513 | 2026-10-08 15:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c3f3eca3-bcae-3451-8d53-f36862aaf998 | -8.6292 | -67.0111 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 98d20916-0d37-3ae2-beec-2e0864d079f2 | -3.1901 | -57.8704 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a9d2f0f8-a33b-319a-bb3f-4c4469653440 | -6.1971 | -52.8705 | 2026-10-08 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 2675ef58-35be-383e-84bb-abbf8c926c0c | -2.4046 | -57.2244 | 2026-10-08 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b42b5a8c-8283-3010-82f8-0ac245c96941 | -5.2729 | -55.9494 | 2026-10-08 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c1222114-73e4-364b-87dc-55b916d715eb | -2.204 | -56.9155 | 2026-10-08 15:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 2ad8eda3-fb0d-3e29-a2b7-7b3aa9312b60 | -12.1948 | -44.6554 | 2026-10-08 15:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| aed4bb7d-ca5b-3a4f-bf2f-8225a26d741a | -3.426 | -58.5999 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7ae755db-c5db-31b3-a0a1-16763e7c4915 | -9.8253 | -47.4629 | 2026-10-08 15:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| edc11343-7b6a-3c5b-ace2-06e2ac20884e | -3.1114 | -53.7839 | 2026-10-08 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0bb43db5-4aa8-3781-a32e-7ed895377e9a | -3.4094 | -58.0207 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 496429ac-0018-3015-a573-ba559647bba2 | -2.0947 | -56.6239 | 2026-10-08 15:30:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| eaf638cb-c3c5-3c6c-bf03-5b454e917aa8 | -2.2222 | -56.9348 | 2026-10-08 15:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| dbb16824-7b73-3340-900e-3949194a1f8c | -3.0007 | -53.9075 | 2026-10-08 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 38eda1a6-1ffe-350b-bba7-1694e4b6fa79 | -3.3173 | -58.2162 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 84370d4a-b113-35d4-9b74-11f67a268cbc | -3.0008 | -53.8874 | 2026-10-08 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bc280f99-0f3f-30fa-95bc-b6302c783ebe | -6.1226 | -55.7154 | 2026-10-08 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4cc6610c-38d8-3d5a-ac79-eb2d795ad64b | -3.0799 | -58.0083 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 93ac81e3-00ee-3cf4-8497-c30021d430c7 | -3.2085 | -57.87 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| d393cc8a-16b2-39d3-aa5f-4ec4d50c7029 | -3.4095 | -58.0013 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f20a3a7c-ceff-30d1-99ad-ee8785f7a9ee | -2.4428 | -56.5399 | 2026-10-08 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| cf48eb2f-60ec-3fc4-b930-0135081c98a0 | -2.4805 | -56.1072 | 2026-10-08 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b821f0dd-2ec3-3847-b841-d1fa7db24a0b | -3.188 | -58.6241 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 170.8 |
| d17ed837-2490-3bba-8a47-0affea7ffd86 | -2.8346 | -54.1326 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| bf6b3314-802c-3860-b6f6-098204b2f022 | -6.2159 | -52.8285 | 2026-10-08 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| b9084c82-2e67-31ab-97d1-0865e97b9aa6 | -12.1922 | -44.7953 | 2026-10-08 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| d03a373a-4691-3da5-827b-58c195ff9e9f | -3.0447 | -57.4851 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 87861047-c1ed-3f45-a76c-6b346e5779e9 | -3.3172 | -58.2355 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 09003c8d-f5d5-3ac7-908a-6fa0f5ff37a2 | -13.1833 | -54.3158 | 2026-10-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 599015c4-5af8-30ba-9189-2a4cc637d961 | -8.7067 | -62.4184 | 2026-10-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 570d4ea5-4721-3eee-a3ee-74f12f7412d5 | -11.6374 | -43.664 | 2026-10-08 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 8796699b-5470-3dc1-8d02-c98e23265d4c | -6.6901 | -45.3519 | 2026-10-08 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 1c1cb720-e054-37e4-b371-042fdf357444 | -3.5176 | -58.5786 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 165bcf4b-88a2-3979-a4a3-bca4ef4c50bc | -3.6448 | -58.8839 | 2026-10-08 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 35190a7d-1ceb-3e10-a1f8-2886c7f84070 | -3.8973 | -44.1255 | 2026-10-08 15:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7243ac1a-e6ec-3a2c-8a45-4d9b51dd8d4a | -9.1407 | -64.4024 | 2026-10-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b74e6c53-e047-35ac-86a5-7f6ce30be625 | -5.75 | -41.7294 | 2026-10-08 15:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 206.5 |
| 78cd941c-76ea-3bf5-b03c-85825d1cc742 | 1.7672 | -55.5463 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ce123f23-322a-3d08-83b1-cc3e8cb38a3d | -3.2084 | -57.8894 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 80c37794-550d-3dc0-9a23-0ffde978d487 | -2.853 | -54.1322 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| c1b37ea1-31da-3d7d-b84a-40e51913f1fa | -6.8574 | -59.36 | 2026-10-08 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 68c08052-a90f-3d80-a5ec-92b9f7a461cd | -4.7768 | -55.75 | 2026-10-08 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| abcea5dd-c44c-3a52-8e97-e5aefae156e1 | 1.6202 | -55.7852 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f6f5d26e-f479-36d6-ab41-f581407e7fde | -2.7613 | -54.0941 | 2026-10-08 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 191.2 |
| bdb77626-fdab-3917-a334-caed4bab86c3 | -9.077 | -66.0881 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 40842798-b7e8-3516-a2c7-cb6a42e79b08 | -6.4905 | -55.9563 | 2026-10-08 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b2d982a8-61ca-3047-b946-5783499edf5f | -3.1879 | -58.6626 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 131.9 |
| f488f110-784b-3ca8-996b-3eeed846a31b | -2.7981 | -54.0732 | 2026-10-08 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c64b8b4c-faf3-3288-b227-b1d104947965 | -3.0798 | -58.0276 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 68e2daed-9d99-3ef3-b112-236e21358874 | -7.218 | -55.1617 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d7c609fd-2951-3278-aef2-68bf278e77a0 | -3.4096 | -57.982 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 938b3e88-e9e0-302f-a641-d0ebba5b4785 | -1.2086 | -49.0412 | 2026-10-08 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5fde9103-b1ed-36dd-bddd-760a9b1f4884 | -2.7541 | -56.6126 | 2026-10-08 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 05f2582d-df18-32df-bee0-9898abd89801 | -2.572 | -56.1646 | 2026-10-08 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d48b7e6f-ef53-3786-9df7-0828d1799a1a | 1.1691 | -50.7481 | 2026-10-08 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |


[Clique aqui para ver as próximas entradas](README224.md)
