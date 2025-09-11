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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e30935a8-3584-36ee-828d-7f76a3de5cf2 | -11.39794 | -43.53134 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcf4923c-8fc4-3df0-90f7-005596239ba5 | -9.14634 | -45.55846 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d8473d9-94ef-3244-93bb-a1915f413016 | -10.02516 | -51.73184 | 2025-09-11 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67add006-7fa7-3bed-8f79-43489104d1ce | -11.35837 | -46.51188 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d96ebca-16ea-315c-90f1-741a965f29e2 | -7.3912 | -47.34925 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4481aea-6d1e-3ac8-b2c4-9f04efaa2554 | -11.71662 | -48.24748 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e5cab0a-6828-32f7-ad67-f14920f02794 | -6.97027 | -44.7846 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48746571-76e7-35a4-92ef-42e66a380063 | -9.06749 | -45.69961 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21b63799-4a27-3973-ad7b-6a7b156743c5 | -12.43177 | -47.80733 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d538adb1-a6ee-3b5e-b3d4-006fddabd31a | -12.53129 | -45.34287 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f2eb989-dd46-35d2-8115-92b9b9c77ec7 | -9.84485 | -47.78135 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87178df1-22bb-3922-abca-d8245cce528f | -6.2538 | -43.4127 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b96c8de6-3aa8-32ce-999f-2b25d823cdca | -7.8778 | -46.02499 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cf521f1-03b8-3067-9830-53889b31c2be | -11.48918 | -43.65927 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d792bb6c-18dd-3606-894d-b623515a3049 | -9.09957 | -46.95279 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f365dea-3926-38d8-9619-fc2e5165b75d | -6.6646 | -44.09721 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d92e0ca8-9a0e-37cf-8b45-37ec0e5c7943 | -9.84379 | -47.7871 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e20f9832-3c52-3440-a454-01f51d6d3c1d | -7.16406 | -48.89036 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820b36a9-055a-36a6-b462-793025a67947 | -7.73336 | -35.13303 | 2025-09-11 03:55:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 61fafc15-f559-355f-a84e-86e53175323c | -6.17167 | -41.07709 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1c1f950d-565c-37e8-b941-e83bdf6c1824 | -7.91285 | -46.85077 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcd0c213-9792-3cdb-9479-8b9908c67e01 | -11.07677 | -51.33356 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2d295d20-fbe9-3639-8560-f694da4733e9 | -6.39536 | -43.51168 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7ada40e-5feb-3479-bd5e-168a680a5640 | -12.01554 | -47.60482 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3fe8cee8-d304-37cc-bf61-5e52bc4cb9be | -12.14317 | -44.85528 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aaa9d97-189b-377f-b604-748ed9a94bb4 | -11.35741 | -46.50805 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 31899d94-bb11-3314-a2b2-c603e7900492 | -9.09806 | -46.95414 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d46cd315-ff0d-30e5-96e1-7bc133e21b50 | -9.02198 | -49.7667 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b755c297-0599-3d8a-a7f3-b389751519af | -9.06685 | -47.08226 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f0e351a-b7fb-329e-b81c-36b43e8827bf | -6.31866 | -42.21157 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 7c27c98c-3355-3c2d-86dc-f39564ce4b72 | -7.39065 | -47.35237 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1b7cb6d-3f45-302c-a1f8-c8168ee59d51 | -8.52662 | -45.68756 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aa71939-b861-3570-86da-8e94eb2158e7 | -5.69682 | -45.32734 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce07eccf-e064-381b-9bb8-e8d30028e827 | -9.83874 | -47.78617 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0046dce-5214-338f-863e-313b3f31c09b | -11.35561 | -46.5016 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b592228e-94c9-3672-bed1-e9ce132bbe35 | -11.10717 | -48.40284 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 292a117e-28ea-3281-a051-6a4237ea54c0 | -13.3172 | -42.46012 | 2025-09-11 03:55:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 865546ea-2c94-3b1b-9a1e-371797992ade | -7.38704 | -44.83553 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89fecc3-6dc9-333c-ab1e-71694d72b443 | -11.36233 | -46.54116 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1b4c90bc-3b5f-3dcc-88a4-69f76e374135 | -10.20174 | -46.83342 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9af6e73-e4f4-3fac-8e00-ae355b19dd1d | -9.01263 | -49.52888 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ca939bc-8a2a-3b01-bc7a-4492f690ed81 | -7.39938 | -47.37711 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e4186a1-a9f0-3d06-a81d-6ff3d881fb0b | -10.01761 | -51.73618 | 2025-09-11 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8058e7f-6691-3b37-b8e2-9854d4984c83 | -13.24932 | -43.7845 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8037087c-d235-30b6-ab5c-7b05d10bdb33 | -6.36723 | -45.16362 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa6c6be7-e68c-30d7-ae9a-41d52e3c0874 | -12.56728 | -44.64382 | 2025-09-11 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc490706-776a-39c5-9227-335837a6f2a8 | -8.16656 | -46.07279 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 790e0a1f-5f7b-35e3-a750-9fc810955352 | -11.78959 | -50.57806 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dbae208-efa7-39e3-bb6b-dea29321e8bc | -7.26386 | -44.60891 | 2025-09-11 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f0a45a8-3311-3f89-b3e7-6c334628877c | -11.96632 | -46.65553 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8b1ff9-f986-3b7b-916a-4b9719d9152d | -9.49724 | -40.86555 | 2025-09-11 03:55:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af719a4e-1289-38fe-a708-f1fc526d3fbd | -9.07609 | -47.0742 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b8a74b5-cbc7-352c-a92e-d80275d2cc02 | -6.3988 | -43.51588 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c91b64d3-e445-3e0c-b0b9-ab8e713cec88 | -8.47361 | -47.28851 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cfd7023-2567-3555-8ed4-c538172150a0 | -8.07952 | -50.17796 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 555d8ae2-19e3-35cb-8123-29a5978af141 | -7.85966 | -48.15586 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78f4e0a2-a832-3992-862c-d70e0c3d9a1b | -10.93986 | -46.81176 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 333b8eaf-6e2d-3b7e-bc12-4a09dbbf218b | -6.31944 | -42.21797 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 068234b0-e89f-3a86-8233-21287982f09b | -11.08411 | -51.33597 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 21ce90dc-2dfd-39f7-ad86-1b1cae0341e6 | -9.67275 | -43.52235 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8da0256d-1780-3ee3-84bb-7aa1d8ee8aa8 | -11.41882 | -43.54431 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2053f652-859c-3854-a767-7e7ff2de723f | -6.31572 | -42.21739 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 51b4d458-1019-3960-98f7-f222c841de40 | -9.77337 | -51.09656 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56c367a-7534-3a19-9054-b5bc95859ed7 | -11.49231 | -43.64079 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72fc6eea-84b2-35f5-9819-02c6f42b4f18 | -11.43356 | -43.57825 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ab626fa-ca12-33f8-9f11-e9f38aba33ba | -5.86065 | -44.22261 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f556c2b6-aa9b-32dd-9257-6981ab379357 | -7.23835 | -44.42612 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e4d3515-c99b-3f79-837c-0aeb3940cb41 | -6.81308 | -44.88771 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6bbd3b1-f53e-32cc-a794-9476c42b03ed | -6.17456 | -41.08155 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b736a57b-d64d-3df5-a202-363101e77adc | -7.39313 | -47.36852 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be891d8a-f325-312e-8ef3-fe178b003138 | -6.63618 | -44.07723 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfe6da22-7292-3598-beaa-85613064d626 | -12.41649 | -44.72389 | 2025-09-11 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6d89565-e2cd-37c5-9722-0a823a4ea959 | -9.70942 | -43.53104 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23d2bc5a-e06a-3428-b692-126f2cef0ff4 | -10.74697 | -48.18038 | 2025-09-11 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16f42b43-252c-3f50-b706-b5016801cf7b | -8.04158 | -48.66077 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 862deab8-b7a6-3596-8683-d0e3145f5630 | -9.00929 | -46.08784 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36e90fa-ef1d-3df1-8397-6917b60a0ecd | -6.98791 | -44.79523 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cbf2d53-90d3-32df-88d5-003d2e46d4c9 | -10.78 | -46.00348 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dfabcf7-4e2a-3718-8f86-2039047c99fc | -12.01879 | -47.585 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfaa1c51-025c-3ce4-9628-5512acd9dd57 | -6.41376 | -44.49634 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff7cd494-d253-3d60-9e7a-400d36f3b37a | -12.13303 | -44.84257 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 691fc8d5-1724-3063-a8ea-9819e57e0baf | -11.50125 | -50.38957 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 450f59b7-a9d0-3ca7-9072-ffec1e60298d | -7.01123 | -42.13578 | 2025-09-11 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae33ce1b-4117-3b82-8db9-f12a53421197 | -6.34449 | -44.08663 | 2025-09-11 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 128702ed-dc13-36b9-bdb5-887813fc8fe3 | -7.85068 | -45.40434 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7ce2dfe-960b-3d9a-a2f9-4eeffa1cb624 | -11.45149 | -43.58601 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30f661f1-f95a-3fe6-b508-5474240b80b5 | -11.35377 | -46.51157 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a38a5641-f708-3c04-a301-00a62274cbd5 | -6.17811 | -43.51116 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f40bb2d-673c-3f2d-9f62-bcac14363f0c | -10.32531 | -48.8102 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1c84760-3b35-3a0a-81ac-c6a5a2d5a27b | -8.49001 | -47.31132 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e3faf54-2388-3f7f-b931-d93b961b033e | -11.47536 | -43.69516 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6252f6b3-f458-30f6-aedc-bf627f09ec42 | -11.40262 | -45.59828 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2e64a35-c6a9-34e3-aa7b-a0f73b21371f | -11.78285 | -50.57546 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5499d32a-e5e5-38dc-9a09-ab01c6c89fe6 | -8.51235 | -45.68994 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8adb489b-f868-3b76-841b-8cf387787086 | -11.48761 | -43.66854 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26dd5590-944d-341e-8006-f50f0dc28fd3 | -6.22256 | -43.50013 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ab4c497-e170-3159-a727-8151263dddea | -11.35948 | -46.53127 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7e3f1635-8ad0-3a8d-b125-4604bba13f1a | -11.02248 | -45.06251 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| edba9c9a-b962-356c-afc0-b2609caed816 | -6.85703 | -47.87252 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| febc289c-3429-3b4d-b691-8f27de81cc4b | -11.34635 | -46.47606 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README29.md)
