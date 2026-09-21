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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d149a228-2e2f-318e-a117-9fdb4e57b2bf | -8.49672 | -47.98002 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9088a0e1-46b2-3e19-90ed-39f9fd6f6326 | -5.22709 | -48.06261 | 2026-09-21 16:03:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3e945d23-e19f-3c11-b768-c4c4cc095c55 | -7.55382 | -44.94744 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e4376c18-b61a-3268-adc4-aee646c20681 | -6.56436 | -45.56321 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 54f5a334-a0db-36ce-b8bb-3f89f5506e99 | -8.20382 | -47.17737 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3c8dd2f5-379c-3459-b882-91008821e0cc | -5.55474 | -45.68963 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 15874823-bd98-346b-9071-36dd5c5871b0 | -7.5484 | -48.68314 | 2026-09-21 16:03:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 102a0667-2bc3-3f5b-bbcb-853b8cde6b57 | -7.4088 | -44.78485 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 02b990a8-061c-3fa0-b67e-2ae85aadf00e | -6.47827 | -42.76549 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bace1ee9-3e1a-3e03-94f6-1f2999c51333 | -7.33744 | -44.47482 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2d86138f-75ff-37e2-80f2-8a3ec21f1bf2 | -6.60136 | -35.74871 | 2026-09-21 16:03:00 | NOAA-21 | CACIMBA DE DENTRO | PARAÍBA | Brasil | 2503506 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 083ea807-0612-33d0-8a9c-bf84f2d18573 | -2.6745 | -49.02261 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b5bdba45-efe3-30e3-acdb-e14439aba00b | -3.33919 | -42.53532 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5afcbe32-bc7b-3312-afd8-2fd2d4d9e0e2 | -8.43865 | -45.81766 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c8c24ec9-bfff-3bd6-977e-6ad97554b495 | -3.4186 | -43.27022 | 2026-09-21 16:03:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2117d5db-7a56-303a-bfa3-102c11b27e8f | -3.43721 | -42.85786 | 2026-09-21 16:03:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| baee6961-95ff-3ad5-b6a2-a5a7f756361c | -6.49605 | -43.89677 | 2026-09-21 16:03:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1280dc3c-7c55-36c7-98db-8f74ab6b75bf | -8.44927 | -48.45314 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2171e7a3-d959-3da8-b5ce-37aabbe0b6a1 | -5.7457 | -43.70374 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| eaa2a69f-1388-3529-bfa1-f7b098f4fe30 | -4.39872 | -43.05597 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b464f7e1-27ea-319d-bc56-b6018cfb3a34 | -6.57295 | -45.55339 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4f14d84e-bdfd-3eaf-b419-79e67efd553d | -5.14773 | -42.8293 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 847d5a61-2da4-3dcd-b7f1-c3e94ccbd01c | -6.73916 | -46.6284 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3eb4b98d-ebfa-390b-b011-5d02cd8fc068 | -6.86542 | -43.69825 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 294b9632-2ce9-32a5-811d-bdae952c1c20 | -8.41552 | -45.8724 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5ad62af4-13b9-3883-96a3-5501c3fb6114 | -6.73576 | -44.28572 | 2026-09-21 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 808d3af4-daee-3a68-86db-85bba54dc63d | -4.39729 | -43.04615 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 93f6ebcb-eb13-3b95-adfa-24e260c7cdd1 | -5.75776 | -42.44765 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a53ef74f-308d-38c0-be2b-1edc24d659b8 | -6.94237 | -43.09211 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9233106-7a8c-3f67-ae11-1e19786c8f9f | -6.84568 | -43.77277 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce17559a-7c8e-33b3-aa30-2243c4c189e3 | -7.78265 | -44.8145 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 362b1298-fe0c-350a-ae79-4db778af79fa | -5.44035 | -45.74435 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5ccbc211-4086-3959-9e96-2dbc787657ff | -3.38389 | -42.96392 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 90b91d6b-7db8-3324-b946-237396633d70 | -7.03084 | -42.10044 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| fa6e2d23-b4a3-32ef-b919-fb8314bff28d | -7.73521 | -49.38552 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 75a7cfa3-e723-3b45-8c62-cba64ed0f50c | -7.61612 | -46.12344 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 64c634e6-4c7c-307f-8bb8-cdc70b68c428 | -5.65737 | -43.4138 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6e991453-f9eb-31e2-9704-5ed4309ba54e | -7.43415 | -44.76334 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 97d02125-03bc-3d13-b358-2435b6609f77 | -6.30364 | -44.88863 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 96cc3a49-67f9-3455-a94b-a7e4e3939742 | -7.57443 | -45.44108 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c1563744-663d-3665-962a-38dd7a7c1aee | -6.56033 | -45.56919 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1f06d1ff-1589-3ccc-9946-2e2cfdc2da7c | -6.85866 | -44.57807 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 0a23d00d-b7d6-3a94-8ae0-7cc5e3dc0282 | -3.34923 | -42.76139 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7f24dd9b-685c-3894-aea3-29cda165a455 | -3.41532 | -42.26413 | 2026-09-21 16:03:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6936486-ecce-3be9-867b-f644730eb8c0 | -6.26181 | -41.65436 | 2026-09-21 16:03:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 2146fb48-8d3a-3715-a9ea-c66dc27c8dbd | -2.78199 | -51.35033 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 52b85b7b-4cc5-3840-9aa8-fb779fb06951 | -7.73702 | -43.88609 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 78ec1ad1-a8bf-3ca3-b7f7-c9f35dcf068f | -7.73983 | -43.90678 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5ec0232b-29f8-3073-ba3e-23a3bde948e6 | -5.6425 | -43.36808 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7913f194-372c-3924-a8f7-330ff70e05f6 | -5.80792 | -43.85878 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 05f4300c-8a81-34a2-ad22-74177478b8cc | -3.70706 | -38.70525 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 94bf763a-8248-321b-b1f5-77d944cdd9f3 | -8.08175 | -44.36747 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 15a6f176-0f4d-3237-b22b-c8e670d58b9d | -6.56305 | -44.90242 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7a57e7be-7bd4-3fa8-9e90-5e51e35c9823 | -7.74136 | -43.88554 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76298c20-1745-3abe-b9bc-972219a49bac | -3.43949 | -39.24711 | 2026-09-21 16:03:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 67c13e3e-08f8-3458-a565-f71fbb81c965 | -3.24724 | -42.80556 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 699b76fc-3cf0-3815-84d2-531caf5ae14d | -6.8373 | -43.49696 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5d48d9ee-81b4-30a5-ad58-eb5d72ff7f54 | -3.37917 | -50.40062 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 9213ce85-82e9-30ee-9616-28f85628dae5 | -6.44965 | -45.16063 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4528f485-2ec1-3ed8-92d2-0f18f0f1e264 | -6.67477 | -50.9394 | 2026-09-21 16:03:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e67fe3f7-4dd9-381f-aef7-f0d3f178c99a | -3.33127 | -42.77111 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 381.4 |
| 5f70e2ec-4076-3e5a-9ba6-0fd5065db322 | -8.7853 | -48.74883 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b614dd7d-99f9-3ec5-8c20-7a1023ca1280 | -5.61611 | -43.38659 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| baa74c71-7412-35ad-8d20-9ac5b94bf46b | -7.05497 | -43.66342 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 837fc7df-6ebe-3063-84f4-f6cc09116e90 | -3.24654 | -42.80094 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| accf2d50-fc87-3317-a26c-c33535dec68a | -4.60501 | -45.0475 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be125aeb-2db8-3de3-9eec-60866928700a | -1.70796 | -49.79291 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b2a9dac4-2972-3cc4-9a3d-3f2e9947ab12 | -3.84517 | -41.70056 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3f557280-f5a6-32ac-9f7f-31d75b1ed2ff | -3.60641 | -40.16657 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 61e4d162-9e4a-3f4a-ae66-07672830db85 | -5.74625 | -43.70749 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 77d18760-c76f-3588-96e4-59bb606af7a3 | -6.46976 | -48.42617 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 70475678-6f39-3744-a31b-993699a0a79f | -6.92345 | -38.73254 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ef4970c8-cea9-3f0b-b691-82e641e68fe2 | -7.03219 | -43.68718 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54f7753d-b4d4-3ad0-8141-2453c3cabc80 | -6.90565 | -42.92297 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 947bb106-7460-397d-865d-72f378f76731 | -6.85219 | -45.52266 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 35a5b8bb-16b5-3afc-9b00-c3d64df397a4 | -6.18065 | -43.34945 | 2026-09-21 16:03:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c7708c3d-546e-35e3-85fb-3c09a393cf8d | -7.72384 | -43.90008 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d0786304-4249-347c-8d69-ec56291afa5c | -5.57796 | -46.69096 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 022ce503-fc14-3841-a6de-6f7c1238eca5 | -4.1734 | -40.15013 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 96528ef0-6582-362d-a2b1-5545d24e9f2d | -5.58961 | -45.54771 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 31049524-65f9-3913-9afd-02c37bb11bf8 | -8.79147 | -48.74847 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 66e91e2d-2d52-3af1-817c-6cd9a24b8914 | -6.81817 | -43.73199 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| af57bd0a-d21a-39c6-9afb-f57ea4eb7b1a | -6.93342 | -38.73105 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 71b95e95-db0b-3d42-a4af-8c0a4a960e00 | -8.41396 | -45.86098 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8c89574a-e71a-3d29-a9a6-7a6a4d7bd662 | -1.44745 | -49.75434 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1879a338-5479-3fe1-80b2-bcd88eea2058 | -3.36649 | -50.76085 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fccb4ec1-b80a-35dc-a8bf-03bc5d86932f | -8.41633 | -46.87217 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c30bed9-8ded-382c-bfc6-c87b7914630c | -6.6688 | -47.7811 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3436ac23-25b2-34af-8d45-26b8b93955bc | -6.25506 | -41.65974 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| ecd50156-4895-31e6-ba25-5af0b4dd7168 | -5.67988 | -43.42557 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2e8318d9-7e2f-32f1-8309-312634f4847a | -2.78037 | -51.3518 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0d8e5991-8ee1-3696-97b3-9ef54e20950b | -1.19367 | -46.65894 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ac57859a-0e75-3993-98d6-e824107c96ce | -3.66699 | -38.90809 | 2026-09-21 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a39c10a-66ec-3f12-b1ef-7828cb0d8f66 | -7.51415 | -46.23068 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6346abfb-a87b-35c6-83f8-2b8ab7216845 | -5.37156 | -43.18733 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 779665e2-aa15-3ea5-a85f-688c2f10fd39 | -5.83315 | -43.85512 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 0f316552-aa81-3d28-a2dc-f1cae18967ff | -3.56898 | -43.4673 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c32835e3-402b-3a38-af9f-a13e7b094c06 | -6.84404 | -38.56683 | 2026-09-21 16:03:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cbba90d2-f29f-3b10-942b-695cae8926e7 | -7.41215 | -44.80859 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6f3bd863-f442-3e32-bf31-5caef2ad2dbb | -7.16659 | -37.71097 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |


[Clique aqui para ver as próximas entradas](README168.md)
