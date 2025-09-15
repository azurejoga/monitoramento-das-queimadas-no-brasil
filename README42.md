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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 506ec511-5ea3-30e9-825d-61a5680cb9c9 | -7.63892 | -49.73842 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7307e2f4-bc3f-3cf1-825a-ee4d768912ec | -9.10231 | -50.5359 | 2025-09-15 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65af7ef0-7a61-3f99-bb9c-2bb3db97f92f | -8.10415 | -50.16193 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d55a273-a122-3da4-8b35-afcab015d1f0 | -8.95688 | -46.22108 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6197e7b0-cdc5-3ea6-accf-b845d14df1af | -3.79449 | -52.17691 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcbfdafa-e8f3-37d6-95de-c3dcf7714c78 | -5.11592 | -46.133 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6365175a-8859-3cb1-b86f-3f8004f8a5ea | -8.96632 | -45.76671 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 766a6c23-0eae-3de6-9e91-b69eccebbe6a | -6.35263 | -43.16008 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 033fadf7-2066-3bb7-9f6d-3c8b85fa5e04 | -6.1789 | -41.18577 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8ad4400-289a-3c0a-b526-83601bd05f43 | -6.94074 | -44.40026 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f315967-01c9-3660-a499-4f944aa03ba1 | -6.41647 | -42.60738 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afadfab7-3d01-3989-ad6d-de0ab7859452 | -7.88565 | -43.58884 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 94f55e05-f0ec-3654-b6cb-30a66466caf0 | -10.78454 | -45.98039 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c94bb9e3-6587-30d6-ae36-fd1a56e1743b | -8.96866 | -46.04935 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3e1c27b-219c-3cb6-b7ff-936613917866 | -5.2046 | -44.31746 | 2025-09-15 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed00bebe-ce70-31b7-b8f3-541f44387942 | -6.77392 | -44.72463 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d25b0760-509f-3f5d-a867-1b726cd99da4 | -7.05349 | -44.13938 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af9aaa92-87c3-3404-b005-8396d85cc0e5 | -7.86615 | -43.58592 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c954519-e096-3f70-a46e-62d1f09960d7 | -5.47344 | -44.68777 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6fc9dd0a-b421-365a-91f5-d24b2bd32fe0 | -8.92031 | -45.47254 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 9fdc1258-c1e5-3e5a-afe5-4605133d5502 | -8.99209 | -45.76097 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7af45258-9ec3-3ff5-8507-3bfe3199fb0a | -4.24825 | -54.92227 | 2025-09-15 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3415f816-1bc2-3810-9533-153da7c68238 | -10.93259 | -45.49303 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e986ab94-a34e-3a63-b4a8-f217769de01d | -8.64609 | -46.3693 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c0466ab-6e85-35ca-aa9b-64e5872bd49c | -7.68874 | -44.67745 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 577b6b75-9898-3a8a-85d3-518d2acb0c42 | -7.38762 | -49.9889 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72716b99-cf9f-3a4c-8022-7681a11e28fb | -3.65205 | -54.05296 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57fa6c78-1fa7-3c64-aac8-41bf982e2017 | -7.44127 | -45.84414 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86f5268c-c9a0-3e30-a212-bcd6eefa0a8b | -6.41161 | -46.93256 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e974b87f-94ac-3428-b952-4292c956b3b7 | -10.89381 | -45.44326 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de655773-64e8-3e14-a353-ae14594c457c | -7.79673 | -46.15131 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d55b791b-d5a9-3e14-a29e-67e8aa03cb60 | -7.8917 | -43.56679 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1db4a19c-19db-36df-ba6c-f7ea6d9249ea | -8.42888 | -45.73235 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19ff57c1-0a89-3f6c-b3cd-31a064ad5c28 | -10.73356 | -44.76688 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 320dc636-8bda-3eaa-90d6-ee9cfa58d013 | -8.96573 | -45.77073 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0d3e1cb-7f28-32a9-8208-ba317f3a1c27 | -5.57674 | -51.97451 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e83c028-ee65-3ef7-9c65-ee9e38644215 | -9.13016 | -46.9473 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d8e4a6e-673e-36fc-bbfc-400fe98634a6 | -10.91367 | -45.56313 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 912bb7ef-a33a-3b2b-8dcc-67ee2bce8004 | -7.40168 | -49.98742 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 831b07ed-2dab-34d7-8bc6-2fbef1be48eb | -5.48155 | -44.69328 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc5c3a72-0038-387a-93df-94d449c18fdb | -6.81126 | -46.93433 | 2025-09-15 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df7e5e64-1fcc-3e09-931e-7771c704ee1b | -7.69764 | -44.67959 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36f54ba7-ed9d-3ca7-9d14-d3a77d5d3b03 | -8.94363 | -46.045 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69ce113-262d-30b9-a05c-5a37ef995d58 | -7.40223 | -49.98382 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 842215d7-0457-35f0-a821-845f6afd8166 | -7.84461 | -43.85899 | 2025-09-15 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46a149c4-6c80-3915-98e9-0e28c0de817e | -8.95996 | -45.81026 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60560e7f-5859-3ef7-9662-35e844516386 | -8.96095 | -45.7971 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8678b518-a687-3365-ad3b-5676ab7baf80 | -7.68914 | -48.86374 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f6d7509-53e0-3268-aa66-5ae9660558c8 | -9.55265 | -48.04606 | 2025-09-15 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b9f900f-6f25-3665-99f4-96dc910bc703 | -4.41324 | -47.60979 | 2025-09-15 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f71d28d-da25-35ca-88fc-730a9389a798 | -3.64691 | -54.06115 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c16e78a-e5a3-3eee-a75a-a1b40092257b | -5.12061 | -46.12862 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73ef2676-eb7d-3fec-92b9-b4df4c980a45 | -8.11845 | -43.66743 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c53f8aee-9a2a-37b5-a174-509a8be77cae | -10.75209 | -44.69942 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 617c33fa-c49b-3943-9bd3-c415d1e2c51c | -6.97459 | -44.54969 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 53dcd5fd-ba00-38c5-bb9c-43b7dadf1b32 | -7.30446 | -43.93169 | 2025-09-15 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c905fb7-a3f5-34b7-8c88-5b6bb4ea8328 | -5.67324 | -43.49202 | 2025-09-15 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f3b6567-34b9-3bdb-bef2-365fb6efa1d4 | -6.17581 | -41.19571 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e117197-ba54-3f5e-a4df-87ea93aafe49 | -7.97046 | -45.64025 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f01fe4b6-57f6-3c0a-b3d5-2a7bc9a2e70b | -7.35616 | -44.29374 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08fce8d2-a333-3988-b91e-c79cabee6b1a | -3.88031 | -52.29601 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94f9e628-4cd7-399f-ae2f-87b9bc04ccad | -7.35262 | -44.29504 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f73b8ed-211b-3151-9506-05045b35b2e2 | -10.13903 | -46.15361 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 439c4c96-ee49-3bcf-81cf-b2de82899e0c | -6.99324 | -45.61918 | 2025-09-15 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e49cb84b-40ec-378d-bd4a-270e4d539b69 | -9.17255 | -45.5834 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6f1b250-faa7-371e-8651-69e2c8c1b7dd | -7.22134 | -49.59654 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82d3946e-2e3b-3e9e-b326-b83e59a045a1 | -7.73153 | -45.30562 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2352c129-e560-350d-aa03-a8b4f932dbf3 | -6.18294 | -41.18523 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7313c2bd-2c38-33b8-8c7c-927b411e34fa | -8.97899 | -45.82348 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 79a7f41e-93d9-3c0b-912a-64a6f82b9cff | -8.77688 | -46.06641 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2004dfe-d9f8-3226-9c6b-e5cec90b53ec | -3.64901 | -54.04809 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d65da941-69a8-3083-8545-210c2a1f0c92 | -10.88933 | -45.44256 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2523caf-2219-31e5-8dc0-20d6edcc201a | -3.85586 | -51.33358 | 2025-09-15 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b2382d4-e06a-3c79-904f-f9d2a06af2dd | -7.97777 | -45.64954 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f583a76-6d1e-3e24-ad79-b55c2a131a7a | -6.16312 | -41.17622 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f2fdec5-01c8-321b-a57a-3fdecaa2452a | -8.23548 | -45.88664 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd05bc80-6423-3690-af65-5d5de84f0bf8 | -8.34866 | -44.72552 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba987456-105b-3d5d-b162-be9df37f4012 | -3.73141 | -55.94412 | 2025-09-15 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2777bac-ba16-3df4-92e6-21714f6b4319 | -8.99436 | -49.79192 | 2025-09-15 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c3b238-ff9b-33a3-ab2a-20049b076e00 | -8.1881 | -46.76656 | 2025-09-15 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bab7431-aaf8-3104-afb6-1ab68d090ec8 | -7.69896 | -44.67046 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9cd02d68-a1c3-3747-ae56-f763b6f32d04 | -8.96167 | -45.79856 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f9d3ab6-031b-3eea-b5ed-b8d06de3bba6 | -8.44244 | -55.62029 | 2025-09-15 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 375eba23-10da-3fbf-9207-041315cc5d95 | -5.15099 | -46.00928 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b857020-a15d-3ed0-ba9c-9b6ec8d7d4b1 | -8.89969 | -45.48893 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1925df-32f4-3cdb-b22f-490ed7416b71 | -5.92981 | -43.22987 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d62f4d4-7511-3e70-a312-86f075685b66 | -6.34696 | -43.16475 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30f8c8fb-e29f-382e-9e17-d7836218533b | -7.89347 | -43.56795 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3672ab93-fd31-3f99-b5bb-3612dcb22913 | -8.62164 | -45.74404 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be5ad25e-0761-3548-86f8-70685b3d76cd | -7.05189 | -44.14099 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a417762-3dba-3b4b-8165-6d5b6a8c0ca0 | -7.44072 | -45.84786 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 680297b8-ddfb-3f40-b554-af3d79af349e | -10.4015 | -48.61261 | 2025-09-15 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09d68397-bb66-3c42-a2fa-8e6c3f9f4ff7 | -7.98513 | -44.85229 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97fdbbc2-64a1-3e0d-8439-8e4266c17d77 | -7.73586 | -45.30622 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1451ee4d-abaf-33a7-afa2-ee3479974842 | -8.92838 | -54.44259 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c12d51a-b654-32c5-86b4-e87ed9ac68d1 | -9.09068 | -44.81437 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3190b8c-1500-33d5-a7da-98df37e58d3c | -7.88223 | -43.57737 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| cf49a433-d75b-3aee-8a35-12267ed02dc7 | -8.89965 | -46.16392 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a9c5677-2c83-362f-873b-ff1ba65db12a | -7.8876 | -43.56068 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0cae6b2b-295d-3431-bc1a-15d2963b71d7 | -6.44867 | -44.5232 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README43.md)
