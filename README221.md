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

## Dados Diários - Página 221

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9adf34b2-22ef-39ff-bac8-15a91c70ee80 | -6.4394 | -52.6933 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 774fab4c-c258-309e-866f-df4ddfaa7a3e | -2.8346 | -54.1326 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| cddd054f-863e-30e8-b294-a8bf8b834304 | -8.969 | -45.1313 | 2026-10-08 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 318.6 |
| 67567638-9f2c-3bd4-9c5b-96a5cd1c6af5 | -1.494 | -54.5363 | 2026-10-08 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 00a51850-e1d0-323d-9f41-fa0e91d931f9 | -1.3264 | -56.398 | 2026-10-08 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 92e10b6c-8a8e-3914-a029-461557093ef6 | -8.2621 | -54.717 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c667bbce-caba-3daa-88b4-d86df5e0898d | 1.6568 | -55.8045 | 2026-10-08 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 37a374c7-5bf6-3779-82ff-875485fb3777 | -1.7477 | -56.1971 | 2026-10-08 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f0e11133-3b40-3e4a-82f1-0f0134f02c7e | -2.8434 | -57.4696 | 2026-10-08 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| e0b80e87-35a9-34ab-a314-7929c007f128 | -7.2179 | -55.1817 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 89f6abc4-2073-30a4-b67a-40f285461547 | -3.2577 | -54.0217 | 2026-10-08 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 265.2 |
| 0b0f0d5a-fda9-3fd5-889a-e88831e6bc90 | -6.1615 | -52.6676 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 24974a45-e47a-39a7-b20b-710a1f18fa2d | -9.1407 | -64.4024 | 2026-10-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ad726158-9159-3e54-a308-146c342a2b85 | -3.0448 | -57.4657 | 2026-10-08 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d5c2d615-6d45-3697-8f24-7fbbb9dce1eb | -6.1952 | -53.1362 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 16b912c7-701e-314f-8cd9-4da6efea6d89 | -2.9707 | -57.7585 | 2026-10-08 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e6aaa04e-14aa-34e8-9acb-a575db35f701 | -1.1713 | -49.2969 | 2026-10-08 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5b10c8ce-9e18-3491-ab35-dce4193953e1 | 1.6385 | -55.785 | 2026-10-08 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fb9f5147-17b8-3690-836d-62c775890e9e | -7.8878 | -54.9822 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 870a33b7-dcc4-38ef-bfea-5111aec19ef4 | -8.8899 | -45.3907 | 2026-10-08 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 306.4 |
| 19315309-3267-3e98-a118-d528c0c83a35 | -2.4942 | -58.0768 | 2026-10-08 15:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 342b80cf-dd70-3a46-a96e-9432aa667c62 | -3.8973 | -44.1255 | 2026-10-08 15:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 882a5fc4-ba68-3929-b3a8-53c4ab9a6607 | -1.823 | -55.0897 | 2026-10-08 15:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 72ee22b3-0192-3b88-a13c-bf4b4223ed7e | -3.0631 | -57.4847 | 2026-10-08 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 1c70ef30-26bb-3364-be8b-b7e0ee16849c | -9.8253 | -47.4629 | 2026-10-08 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 6d0c3d01-8cca-379c-8bff-8575aec3846a | -6.7366 | -55.1274 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| b29f46a8-9d68-3f76-9ecc-558a3f653a7d | -9.5004 | -66.7831 | 2026-10-08 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 7990d298-4106-3720-b8c0-c6bd622f8d09 | -1.146 | -54.2199 | 2026-10-08 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ef4ac3fc-d77a-3e88-aea4-e533d9a9d968 | -2.4428 | -56.5399 | 2026-10-08 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 21a90595-3140-364c-a805-6ea603a5ac9f | -5.75 | -41.7294 | 2026-10-08 15:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 221.9 |
| 552cfe7a-b797-3ab6-8262-575887a708d5 | -9.8824 | -44.8171 | 2026-10-08 15:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 393238e6-f36a-3f94-8502-915c345905f6 | -3.1633 | -54.7452 | 2026-10-08 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b05a8d92-c820-36f2-ad60-1f2d529073c6 | -9.4819 | -66.7836 | 2026-10-08 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4588e1aa-230f-3cb2-b3d9-ed7d1d5e58f4 | -7.8876 | -55.0023 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 35f370e5-a772-37bd-bf49-7da2c95b8f79 | -1.4752 | -54.7759 | 2026-10-08 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2574415d-e347-346e-8dab-348af327eb1c | -2.7332 | -57.6077 | 2026-10-08 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4078791e-f6ff-3538-917a-20d3666861ab | -2.8433 | -57.4891 | 2026-10-08 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| a52b71fb-779a-31fd-85ed-f59038dcf3ca | 2.7458 | -60.0109 | 2026-10-08 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 20057472-de72-31e3-b611-9df1ba283671 | -2.0947 | -56.6239 | 2026-10-08 15:10:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 2fa39a56-b05d-36dc-af8e-b898644bcfe7 | -9.8015 | -47.8186 | 2026-10-08 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9fb48a49-8cb0-379d-b9a1-e591e7e2d655 | -6.1431 | -52.6481 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 53198dbe-2a66-3d5b-9388-586eb18d2e4f | -2.572 | -56.1842 | 2026-10-08 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6d009517-2862-3f64-9a34-9154d9548c25 | -9.8442 | -47.4608 | 2026-10-08 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 35f3539c-9db8-3d9f-864f-55ec3c6e7a4d | -6.3834 | -52.7374 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a4b00978-9a29-3576-ba64-eeabe14b23f7 | 2.7641 | -60.0106 | 2026-10-08 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 8812c4a1-5811-3212-9edc-d90f99cba20d | -10.4727 | -47.211 | 2026-10-08 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 40ef8ddf-2a93-303d-9858-7a5abcb51cb2 | -11.2295 | -46.2403 | 2026-10-08 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 2c88021a-ff1e-3f42-b70b-54eb57e71d4c | -1.8803 | -53.9701 | 2026-10-08 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4caa4539-f66e-36ae-a9b2-fed3da375062 | -8.5313 | -46.911 | 2026-10-08 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0e083b69-6901-3a9f-b969-9d3dd8faf842 | -6.4021 | -52.7159 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 90c5d481-1d21-30c8-9405-381148048cfc | -8.2247 | -54.7396 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 792a725e-efbb-3706-9d83-40505448c622 | -6.1429 | -47.9432 | 2026-10-08 15:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 11235b88-a5e9-31fc-b7d4-c5eb64e7e42c | -11.6382 | -43.6166 | 2026-10-08 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| e5f29cdc-c331-33e7-b684-ca5b41b0ce27 | -10.9762 | -45.4094 | 2026-10-08 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| db7e8197-cd28-3cf7-bab1-8fed39eddc88 | -9.5003 | -66.8017 | 2026-10-08 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5e69ee79-2d3f-383d-831a-54edc7ed5e09 | 1.6568 | -55.7847 | 2026-10-08 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 614f2c5d-3a08-3c0f-a8ec-4c1412ac764d | -2.2223 | -56.9152 | 2026-10-08 15:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 440ef3f9-9cd1-3a3e-a1ee-20d6191957c0 | -9.1408 | -64.3836 | 2026-10-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4ddf3ba3-326c-3784-afe3-9bfd6a941e93 | -6.267 | -53.4582 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d2f6e9f1-0b03-3f59-864f-26ab9edf0e34 | -2.0447 | -54.3085 | 2026-10-08 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 46596c30-da1d-33a1-aedb-4726ac3ea040 | -2.853 | -54.1322 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e2d07181-dcd8-320f-a3ef-1534878a2fe6 | -2.3863 | -57.2247 | 2026-10-08 15:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2b5d527d-9c1b-360c-8ab7-dd06e3dd6eba | 2.764 | -60.0297 | 2026-10-08 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 984e3afd-0781-391e-b619-c57a3b2ede8e | -5.7321 | -41.6349 | 2026-10-08 15:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 085a7494-3b6c-3003-9f1f-e77f875c2c27 | -6.2162 | -52.7876 | 2026-10-08 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| dc99b20a-919c-3be2-a278-fed17c7e49f4 | -1.6213 | -55.1321 | 2026-10-08 15:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 53aa68dd-0a2d-3e2a-ba56-24b274bdf9e0 | -13.709 | -49.1042 | 2026-10-08 15:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 860d6464-7e2d-3d28-8de6-20055ec8d7d6 | -8.7067 | -62.4184 | 2026-10-08 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 61fd0ab3-9f73-39d1-beed-0be331d3c7c8 | -6.6814 | -55.0903 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3449ae55-d2a1-311d-bd14-7dd2d3f3dcbc | -8.5051 | -54.6202 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9f382b0b-1911-39fc-b913-dd8f7ce0f3dc | -3.0741 | -53.946 | 2026-10-08 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 585aa8b8-a331-39ce-b349-fab26c7c0327 | -5.372 | -44.1751 | 2026-10-08 15:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 390d3941-401a-3cf9-8669-80317afa9b73 | -1.2086 | -49.0412 | 2026-10-08 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 227203d3-9686-37c0-88eb-f42931660bcb | -6.7503 | -50.9543 | 2026-10-08 15:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d33be165-6707-33da-ac43-7e3e31c9fc54 | -2.8713 | -54.1518 | 2026-10-08 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ed2fcb9e-ae28-33a5-a211-1a211c31820b | -7.89 | -54.7206 | 2026-10-08 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b4442fab-fe5e-3b8c-82f8-163b2e641724 | -2.4046 | -57.2244 | 2026-10-08 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 14494dcd-3eab-3470-a8fd-b70813635f8d | -11.2083 | -45.217 | 2026-10-08 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| f9b7d5cc-2321-3c13-8eff-a7c77fddf7c7 | -8.23 | -46.39 | 2026-10-08 15:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bf28c87-a89d-35f4-b59f-3afa09ddb2bc | -13.17 | -54.28 | 2026-10-08 15:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a26a1709-880c-38ef-bcfe-4f762b46740d | -5.37 | -44.17 | 2026-10-08 15:15:00 | MSG-03 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e548b166-06b5-3176-9f0c-778cf73ecb2a | -13.2 | -54.36 | 2026-10-08 15:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 290de891-9f9e-3109-a431-b7e1f91b342b | -5.4 | -44.18 | 2026-10-08 15:15:00 | MSG-03 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3426de7-e7d8-325e-aa3f-1cb63d5db6a9 | -4.1 | -44.09 | 2026-10-08 15:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad903788-4dd2-38a9-be74-25c27b885e95 | -13.17 | -54.35 | 2026-10-08 15:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39cc252a-143a-332d-a9a6-3daf7862befb | -3.9483 | -56.0138 | 2026-10-08 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 63e7e2c4-cc74-3f6c-8efd-ffa2f677d358 | -7.8878 | -54.9822 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 43e71270-0b19-3c67-8f1f-7ad5edff13ce | -11.619 | -43.6196 | 2026-10-08 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 629.8 |
| 9b2391cd-7676-310f-92db-aaf80c4a2ca2 | -1.9535 | -54.0493 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 94dabc81-5d16-396b-b600-42e000631d23 | -11.2146 | -44.8473 | 2026-10-08 15:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7f4cfe6b-e919-3852-9082-a8ea691cbf78 | -3.446 | -58.0586 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4a75894e-0ac2-345f-86b4-a43f0366d171 | -3.2577 | -54.0016 | 2026-10-08 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0ecf99a2-6a89-3286-8edc-ecfd5af06dcf | -5.7315 | -41.7069 | 2026-10-08 15:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 2b301ab8-e245-3b72-b787-1abb83451b22 | -6.1617 | -52.6471 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 315.7 |
| 1521ab72-2a7a-3b5f-a746-e8ab39c5b12e | -1.8803 | -53.9701 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c52c1616-c846-3fe5-aed0-592fc9f2773b | -8.5918 | -67.1418 | 2026-10-08 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d80611e4-a2ed-361b-a8c0-033f9d0c539b | 3.508 | -51.2576 | 2026-10-08 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 64713dfe-6c3a-38b1-9d6d-a4ddb00eb932 | -3.0982 | -58.0273 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 478c8fed-5dbe-3ef1-9178-dd15ad834810 | -13.1641 | -54.3178 | 2026-10-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 24517f89-8092-3493-9610-88b99992bc7e | -2.7697 | -57.6459 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |


[Clique aqui para ver as próximas entradas](README222.md)
