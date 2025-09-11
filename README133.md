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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d34565d6-37b6-36af-9ed6-ddd17e29d2fb | -9.05057 | -46.97604 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 2a042173-edda-3b44-9859-cf1029b95bc9 | -7.84358 | -45.40005 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1fa4ebf7-7372-3f9a-9f2e-f6b35b7c7e57 | -6.44326 | -44.49536 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 56b44d18-8d65-3526-9f14-c46d8bf577a8 | -6.17484 | -41.08516 | 2025-09-11 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 27f9147e-6367-3618-a596-8e82493dd19c | -6.40698 | -42.60195 | 2025-09-11 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 7402a199-c7fc-3f3c-be77-02ccc6bb9718 | -8.33906 | -44.90448 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 063640d5-46dd-3ca2-a24b-30c9afe6ceb8 | -8.73232 | -47.08868 | 2025-09-11 11:57:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a326d2d2-b3d4-3b08-a890-4f8144600dc3 | -8.38703 | -47.99314 | 2025-09-11 11:57:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0b6a1b28-a4fd-37e2-8f60-5a68d020d54f | -6.36016 | -43.04822 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5cf6ad08-94ec-31eb-8e44-11128f1ef502 | -9.15878 | -45.56688 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ab1cedfc-d395-338a-b2e5-a90d7c8438c3 | -11.72405 | -48.26154 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d0883ab7-09e3-3fae-9446-24fbb343792a | -10.19515 | -46.22237 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c0b053bd-8b1f-30ab-bd79-778e24423028 | -10.43521 | -50.56172 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 585e947c-967e-32fe-8d08-8dd45c66df57 | -8.92666 | -44.60153 | 2025-09-11 11:57:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 11bb68b3-d387-3a47-94dd-e872719415b3 | -8.50795 | -45.66825 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9c337343-4ea4-3cbd-9980-95e8b8aa42e7 | -6.21202 | -43.4935 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 62a0b36b-4e31-3dbc-81f5-76be3c0cc390 | -7.39548 | -44.37336 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 816a502b-a890-307c-a7a2-89d70235957f | -8.76484 | -47.11006 | 2025-09-11 11:57:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| cba8980a-4ffd-3368-946a-6018d16e4ecc | -6.17534 | -42.67043 | 2025-09-11 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fe8ca784-c07f-3abe-96e4-ab0c09db88a8 | -7.17479 | -44.13396 | 2025-09-11 11:57:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0f256e1a-3d9b-3996-a7b2-06399d8c3c33 | -9.69026 | -46.79442 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fcae7b20-d59f-3bd6-9483-e4bd7e5500da | -6.61528 | -43.9535 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f1cd924a-6354-3a9c-9d0e-67361fc42ad0 | -8.17619 | -46.09085 | 2025-09-11 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3ebd9fb6-ed5e-3e1a-9338-e085be63eeda | -11.42416 | -43.55125 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3b08c59e-4e65-3a2b-b017-f17219e4e0eb | -11.36342 | -46.55738 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 620914cf-5c67-370a-b2da-d7960fc2df74 | -8.74266 | -45.2178 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9647d771-4545-3d1e-acde-b9491f8a0d4e | -5.12641 | -42.89897 | 2025-09-11 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a478270a-a55b-3978-81e7-3940681acbe6 | -8.04327 | -44.49171 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 92543c6c-8905-3171-84f1-6767570f2355 | -9.04258 | -45.7883 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| bdbbcc50-77e9-3168-b395-c7a69e9d20e3 | -9.06506 | -45.71293 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| be33bc16-8e16-3964-87ae-f9fe19da28c9 | -9.09177 | -47.0724 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab52cb1a-9676-3b24-9c20-2d983f900037 | -5.53352 | -44.34693 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b83d512f-fcb6-3d92-b5ce-bdfa887a389a | -12.0675 | -44.37331 | 2025-09-11 11:57:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 559ef4c5-79b3-372d-b6ca-5a78c58e6aa7 | -9.84273 | -47.78061 | 2025-09-11 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| b184b971-2c31-36e8-8d1b-258ca67544f8 | -11.78243 | -46.4809 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 8919ac63-7d99-3ba5-9afb-732bd0c646f0 | -6.22468 | -43.34212 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e7a964e6-fb8b-377b-8e0e-f484923848db | -10.67591 | -48.63728 | 2025-09-11 11:57:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d4d1091e-4ab1-36f3-857f-c035850dbf27 | -11.3995 | -45.59874 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e5460a2c-e65a-398b-b6ac-6f93b9ada19d | -9.76386 | -47.85291 | 2025-09-11 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4333151a-3683-36cc-8030-ac059bd9fd79 | -5.63454 | -42.58432 | 2025-09-11 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1c91f6f3-b794-323e-9c4c-d7ea36a97dcd | -12.47064 | -43.21208 | 2025-09-11 11:57:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7baf90d4-fb56-33e0-a0cf-1c8cc5f9d0b2 | -9.00569 | -46.09342 | 2025-09-11 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8d6fbced-bb91-33d7-9f0f-114c14c6fd4e | -10.15483 | -46.16885 | 2025-09-11 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d654d759-8167-34f3-aa57-352283ee32da | -6.70114 | -45.31536 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c0f3a77c-d64e-311f-969e-bb8f3a82d810 | -9.81295 | -46.81985 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5e3bb44a-43c8-39d2-81db-8fd96ca2c121 | -7.03777 | -42.13494 | 2025-09-11 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b87d70fd-039b-325d-b50c-d35685501e17 | -11.46676 | -43.69811 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 7c713b4f-8eb0-3df5-a61d-a8ca86dad2da | -11.38245 | -43.52 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b2d17e84-2007-3118-add7-3de6f17a367a | -11.50918 | -50.37823 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| bb76d0c8-0b9c-385d-bb08-1714a5c53050 | -7.73831 | -43.90656 | 2025-09-11 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 641e6d20-4b5a-3d1e-94d7-bd6117e35219 | -7.51449 | -44.73037 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a7c22299-a9fb-3f02-b66f-5dc67bf051de | -6.66405 | -38.18959 | 2025-09-11 11:57:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 715fe575-7114-3dc2-971c-68f28c8652fe | -7.42412 | -45.87747 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 228d1042-fec8-3346-9ed6-14efc6f0f15a | -11.17099 | -45.28733 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| f5f4cf6f-86ad-328e-b523-24dbe3e4838d | -11.82187 | -46.74022 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 62d6ff05-feff-3630-9939-51f3c065551b | -7.39713 | -44.36256 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| df4be89c-d5ce-36f0-b352-4bfd48e27ef7 | -8.72972 | -47.10482 | 2025-09-11 11:57:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1df6e927-e3d1-321b-a3e0-82b4ca337fd9 | -9.04056 | -45.8012 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ce99e20e-fbf9-3ceb-a27f-0aeb6cbd147d | -7.26523 | -44.61565 | 2025-09-11 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 56f3797b-6ea3-349c-a3ef-26ae28673cd9 | -8.74087 | -45.22974 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 94e9899a-df73-32f7-bead-64363066ec4c | -9.05307 | -46.96035 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bce46431-d1fd-36af-8112-5382d4506f5a | -6.31625 | -43.41237 | 2025-09-11 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f374432e-428f-3200-9b1a-f113a29ff155 | -7.86129 | -44.87766 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e6abf612-9afd-3043-81dc-accd0a27c247 | -11.64003 | -41.7379 | 2025-09-11 11:57:00 | TERRA_M-M | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a3048f75-ed8d-363f-b188-1a42f0a251aa | -9.13912 | -46.99891 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 49ff5a3c-9a49-362a-b1c5-73382df153a2 | -11.70628 | -46.51577 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| fc29e29e-596f-3878-94c7-60147edf8941 | -6.43495 | -44.4826 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1f5eb0d3-beb6-38fb-9b2a-be774b993ec0 | -9.8788 | -46.47558 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7c4970e5-48a1-31b8-95dd-1333dcc07947 | -8.52696 | -45.68436 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0b5cff43-8ca0-367d-aa48-f94d2ca7c489 | -8.75314 | -47.10827 | 2025-09-11 11:57:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 23cb947e-df01-3eeb-bf0a-7e783a93148a | -9.10078 | -47.09022 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 311ea710-3978-3b22-bfd3-b7c90f108d0c | -9.7214 | -43.52605 | 2025-09-11 11:57:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b578ac4d-ad20-327c-a1e0-59ed5928a699 | -13.11584 | -40.58332 | 2025-09-11 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 66a4795c-3d93-39ee-99b1-a601a05cfec9 | -11.76972 | -46.49253 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c0d8b0c7-8abb-3bb2-8e99-b4abc8944b3b | -7.23593 | -44.47289 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 328cb42d-834c-39e4-ac06-132e1c6c50e5 | -11.38311 | -45.57274 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d330c86e-4de1-315d-ab89-f73af8de5469 | -7.86451 | -45.51452 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 62e3a428-935e-31c6-9e07-dd0446bba0ba | -12.4615 | -42.6415 | 2025-09-11 11:57:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b426d321-1e8f-3de9-b901-2531203f1dc8 | -7.85403 | -45.40137 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| a98c76c3-2a4d-3104-bef7-68a543353596 | -6.6165 | -43.87858 | 2025-09-11 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aa310973-23d4-3d88-8076-2c610e247b84 | -11.50459 | -50.40448 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1c83abc3-aa58-30c7-9a46-bcf5cebc8182 | -7.0859 | -45.20449 | 2025-09-11 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0504bbee-3897-3ca5-8de8-a85f459be5f0 | -6.32124 | -43.44369 | 2025-09-11 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 94a63566-f9a1-3dbb-81eb-5b2c25811e01 | -10.19725 | -46.20898 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 7cb41309-8079-32a9-8f36-5e471cd0d6d3 | -9.8153 | -46.80515 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 3f456eb9-32ff-31a6-9067-3de258594a9c | -7.39398 | -44.36706 | 2025-09-11 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 301240c8-af52-3aab-80e4-18a72b83d10b | -11.70837 | -46.50264 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2226e2e2-3258-3443-aa29-d7d43f8677d7 | -12.51168 | -41.89689 | 2025-09-11 11:57:00 | TERRA_M-M | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 78f1e705-f8c8-38f9-8cb6-de6fb20d2484 | -13.00846 | -40.08035 | 2025-09-11 11:57:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a8df61c8-00cf-320a-aad6-46f1c130b1f9 | -7.47264 | -41.93006 | 2025-09-11 11:57:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4e490517-72fc-3205-8a6e-6446a9a7e6d4 | -5.76559 | -42.76314 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4d4e61c6-a164-3514-bec9-6a65531eb84c | -11.17273 | -45.27599 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4fddc821-1fd9-32fd-a59e-f04f9d5408fe | -9.06115 | -47.05865 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| bb5975e4-5965-3d32-8637-078dc62760aa | -11.40124 | -45.58749 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6f70e6bf-239e-3037-97c3-1b03bd048367 | -6.48439 | -44.49642 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ad85ccf5-c6fd-37d0-ab5e-2adfe87f1c22 | -9.82176 | -46.83678 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2b400a72-0ba1-3f90-a2f1-9b33f3fb5a7e | -12.5955 | -42.53884 | 2025-09-11 11:57:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| de946a83-a84b-353d-844a-3358c30cc6be | -10.20031 | -46.84708 | 2025-09-11 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 348ffcbd-d75c-35ff-ada1-f39e1696b113 | -9.10024 | -45.69253 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d0f2e743-842f-3be6-9f7d-f9339873ee31 | -6.54309 | -44.78555 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |


[Clique aqui para ver as próximas entradas](README134.md)
