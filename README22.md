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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e52db337-55ff-3cef-85ac-5cceb31ee0ac | -6.89668 | -45.25126 | 2025-07-30 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 528e02e3-acd4-3e2b-902c-9e67df2f1488 | -6.89613 | -45.25478 | 2025-07-30 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b08d53a-60d2-3cdd-baf0-52dc985325f2 | -9.85167 | -44.70459 | 2025-07-30 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54eb1838-065d-3351-91e7-a2651e395983 | -4.59986 | -43.31056 | 2025-07-30 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d618a5d3-4e5d-3b53-872f-6da40b32b91b | -6.17017 | -44.77757 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09f9318-5a96-366c-98c4-4e788e6e0800 | -6.50481 | -56.21719 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f76b8bd-5563-3238-ad6f-a2f7b659de34 | -10.47357 | -46.69632 | 2025-07-30 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce7a53ad-fb37-3f49-8f8f-b7a097cce220 | -3.83602 | -48.96227 | 2025-07-30 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34d49edd-f72b-3973-bd9d-575676ab27d3 | -8.33201 | -54.75187 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89522269-1dff-3f80-b7dd-fb7f513bb595 | -6.69766 | -42.04782 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d75c729f-e2b2-326b-9cc3-53094b47aec9 | -7.10451 | -44.38175 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5fb831e-b550-35a4-93be-3269dcb4c51a | -6.53466 | -56.19384 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db4fe8cc-f357-3c54-8a39-962b6f342fc5 | -6.39438 | -44.74965 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4d69b0c-317b-3184-9fc3-1489b6306f44 | -7.77167 | -45.86732 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74d751b4-d844-33ed-9bcf-6a04c2af49b2 | -6.39889 | -44.74298 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ad157d6-0c73-33e8-9996-12ad4252e887 | -9.23648 | -50.04263 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c347a22-e23f-3f4d-9bc5-98b3e46b7372 | -5.98893 | -45.52011 | 2025-07-30 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41caac63-8680-3d41-8faf-0ebc97e062b5 | -5.2443 | -45.21843 | 2025-07-30 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aa77fa4-52be-32b3-97d3-78f9a78673ef | -7.13076 | -44.34285 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1287bd07-aa48-3580-a9ef-712cb7ee083d | -6.2394 | -44.08446 | 2025-07-30 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c313cd30-d1d9-38c0-89f3-16163cfdc329 | -9.59469 | -46.32269 | 2025-07-30 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 812efb51-d9fa-3a90-8d8d-32d8ba898b34 | -6.6157 | -59.98338 | 2025-07-30 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ba08438-aac8-33e4-a5e9-a33cfcba0d97 | -8.30396 | -55.10844 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38c453dd-4624-343b-b04f-83fb127efca9 | -4.84979 | -42.99375 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aadcda46-7c1f-38dc-91ca-c696ff968d07 | -3.9701 | -50.87591 | 2025-07-30 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb1fb08-ea10-377a-b8f1-c5a33f518cad | -7.3353 | -44.69394 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a7b4aa9-12d0-3239-82e7-97d253fabf7a | -6.52571 | -56.19752 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7df924c4-8659-35b7-9478-8a8823439c40 | -5.83144 | -44.03897 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d8bb79f-5f24-368d-a2b4-58384c452b52 | -7.86553 | -47.87348 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7b3f99e-66c5-3ef3-9497-e3790ed27dac | -6.90743 | -44.73052 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 545be6b8-fd9e-3fa4-8900-634cc31b2fc7 | -5.76284 | -43.96762 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f2451f3-4623-30f6-a95a-7451dc80cad7 | -6.40636 | -47.66682 | 2025-07-30 04:27:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 67b07719-4b6f-3903-97d5-4901d028b8ef | -8.03685 | -46.91231 | 2025-07-30 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2729297a-a8c0-3de9-b2c2-6a7319520643 | -7.00494 | -42.37207 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aa2fc18-d68b-388f-b225-a95322ac54b9 | -7.38392 | -48.17003 | 2025-07-30 04:27:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2348de4e-c118-3138-8a8b-df1f6db88928 | -6.62025 | -59.98081 | 2025-07-30 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 120b6013-6024-3b8f-a33b-d0e27b523e58 | -5.76594 | -43.90234 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0a7a66b-4976-3538-9043-ffba8ebfada9 | -5.82424 | -46.35007 | 2025-07-30 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 313eea33-b89d-3c46-a372-adf2fe5c13b8 | -6.60475 | -44.78856 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59fcd427-7bbb-3f13-ac4d-27d41737f205 | -5.67398 | -43.68165 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d83250a1-b0c5-3a91-a12e-2d0f81db2511 | -8.88654 | -47.33913 | 2025-07-30 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fb9c603-0d96-3f55-8aa8-640b83e4ac75 | -7.14224 | -44.3601 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f136daa-c31a-3cdf-8daa-5c483975ecc9 | -3.50955 | -43.25377 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d5ad01e-928e-3781-8ce0-a8a758417723 | -6.71353 | -44.35793 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7f6ab6b-3709-3000-8d10-4e532a1adefc | -6.57172 | -56.18146 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f419a0ac-44b3-36cb-9b3c-fa453334bfb8 | -6.50548 | -56.21339 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6aacb2db-9823-372d-9b65-e545cf683095 | -7.92599 | -43.11262 | 2025-07-30 04:27:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9949d657-565e-3a26-b728-1be9158f1860 | -6.95711 | -56.38044 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc9a299e-f803-3f52-9847-d48be10c2716 | -3.8859 | -41.03533 | 2025-07-30 04:27:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ef908b0-10b5-314c-a538-c8cd040600c2 | -8.94793 | -46.73669 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70b8d3ea-7e02-3dec-98f6-ebbdc0fc9ca4 | -6.50615 | -56.20963 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33831c59-a3ad-3688-8d23-8d0721bcbff0 | -5.68445 | -43.68328 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547c62d4-58dc-3322-aa5c-bf8e339993fc | -5.67747 | -43.68219 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44774b70-2277-33ec-8ee7-9d029b09eec8 | -3.51303 | -43.2543 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd09ad48-91ce-3b8e-8c44-0d0a5cdb3313 | -8.23919 | -44.91676 | 2025-07-30 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d74223f8-d261-3565-bb55-4c6e6fafea31 | -4.6506 | -43.12116 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c218faa8-df90-3e94-b359-a381e5f70b41 | -8.62765 | -45.88601 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c8d87ff-5a6e-360c-ac70-264f584b3d4f | -3.27348 | -49.14222 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c69b19d-8ce2-3b13-a473-8761792ab2d6 | -8.67469 | -51.21358 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19bf2f8-bc05-363c-855e-69dc2560d4e0 | -7.35091 | -43.76687 | 2025-07-30 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a9e907-16f0-3208-bb57-fb567fe76dae | -6.55353 | -56.18584 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc609d1b-1450-3916-9832-8061d87867a3 | -5.82369 | -46.35354 | 2025-07-30 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9235d24e-8230-3b2e-91da-8b534f4959e7 | -3.58568 | -47.51823 | 2025-07-30 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 321710a8-b3e6-3cd4-8dd1-f3acabb5bb20 | -6.3922 | -53.32267 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83dd528b-ae5b-3826-ab54-8e82e67e6e38 | -2.80914 | -49.00747 | 2025-07-30 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a20a9ecc-a466-37fd-b8aa-c7d401b29dd0 | -10.61988 | -45.24742 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72f102a3-b04a-368e-b0f8-b5fbee2914aa | -6.49423 | -56.21133 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e9cbaa1-3eff-3374-ab4a-ee20a07e7c1c | -5.85189 | -44.22131 | 2025-07-30 04:27:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7be6101-560b-3640-a118-10aede40da16 | -8.01856 | -47.68103 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 352c7aa1-7fc0-3bb4-8fad-ebd6c2b3c2ee | -6.51941 | -56.20034 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66cff791-bd85-3371-9160-be22955cee8b | -7.59893 | -44.83841 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecbd9590-de82-302d-90f6-26ba53a3ad05 | -10.00258 | -48.12539 | 2025-07-30 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3721b18c-bb05-3912-b28d-5c5006e07441 | -7.08647 | -44.49768 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce6e62c3-713f-3af9-92ef-4fb47f2bbea5 | -8.62152 | -45.8814 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f48e1f1-c328-3b34-a68a-2839c00d3f64 | -7.308 | -44.68977 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07b9e3ad-5986-35fb-94cb-b58985a2b8ae | -8.67859 | -51.21425 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46452246-8481-386b-ba42-05acdabb5efa | -6.53115 | -56.21295 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07a154ff-fa90-3f96-9bfb-4024db0546cc | -8.52048 | -43.31603 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4aea03c4-e977-3972-9e8c-8ad57b3cdec4 | -5.76232 | -43.94825 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d96c378-b059-3ff2-a3ba-fe9d932765db | -7.86216 | -47.87293 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a28f7c9-ed38-354f-9279-9eced3e0f297 | -7.21987 | -43.10344 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ec153acc-bc73-367c-9fdd-5f83fc7c9c73 | -8.6477 | -47.91751 | 2025-07-30 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b73115f8-cb6c-3d7a-850d-02b62693a2ce | -6.50547 | -43.19809 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 103395c0-b4b6-3c80-ba11-8599ae1db602 | -9.22871 | -50.04856 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a197d9-1786-322f-9d9f-14719c97cb73 | -7.73321 | -51.09386 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3fbb3d1-0260-328b-9241-0b7603a5d73c | -8.32581 | -54.75576 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55f58e36-8acc-3099-985d-b7ccb0e930c3 | -10.40636 | -47.25332 | 2025-07-30 04:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 757f8fe3-d474-35bb-8315-ee0c1cf58b4f | -4.03137 | -48.06046 | 2025-07-30 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c952f83-cc76-3862-9182-102d6ff7bdb2 | -9.62917 | -48.54934 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14b366ff-666c-3e7c-b40a-a5f6a4d8c1a0 | -5.23847 | -46.77832 | 2025-07-30 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 499a5071-20c0-3462-a75a-2094b00eb48a | -7.05365 | -44.96003 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 327a2a5b-b3f2-3e2a-a635-d4e6d99888b9 | -4.65475 | -43.11774 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97101bfc-d47b-3b9f-96bd-d80fc6dcd63a | -10.00651 | -48.12238 | 2025-07-30 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31a340f1-5c4a-3db2-8b7c-abc860fa5002 | -9.15948 | -49.85101 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61bc2135-aa53-362c-8ec7-38c51a1e4440 | -7.60827 | -45.04845 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c93125b9-f248-3140-be39-c531caf528a4 | -4.37612 | -49.03733 | 2025-07-30 04:27:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c96e8520-8f7c-3da9-b462-fed1d0caa59a | -3.58417 | -52.54576 | 2025-07-30 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aec659e0-4c4c-3c26-aec8-5b37d1b984b2 | -7.78395 | -44.99744 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ef4b125-4290-3e56-9f49-35095bc724b3 | -6.49695 | -56.19606 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54eced74-0975-3b6d-8094-4a5b4352d2ba | -7.10439 | -44.37724 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
