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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1f149d4-d64a-3578-95bf-bc10edc625c7 | -5.04208 | -49.76672 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d5e7282-3fab-323f-b606-f2b67985e8f9 | -10.29974 | -46.61944 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1214014-9156-35ff-b96a-5228b3d99df3 | -9.1398 | -45.82994 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b84f8347-90dc-3d20-8120-c01407288546 | -6.13911 | -47.92783 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8f59e2bb-1db6-3e0e-87fe-368779afe625 | -6.85309 | -41.74541 | 2026-10-08 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 839f48f4-a9b6-37bf-8365-13d2c45180a5 | -9.03305 | -44.37051 | 2026-10-08 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 939d104a-efaa-3ec7-9577-2a0f05f8e6e4 | -3.35335 | -50.47904 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93d34710-3e4a-34ee-8777-dbd1baa90275 | -6.62783 | -43.73209 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a74ce87c-b352-35a6-99f9-bf258501405b | -3.8617 | -50.4211 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 39e4e5a7-eed3-3be5-ab83-1a1d044c0e04 | -3.19391 | -50.5657 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d7d15b8-f315-32fd-ac15-11df852bf985 | -7.47211 | -42.84548 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ada7ac0b-3a6f-3ba8-b0d4-ccf4e389971a | -3.18051 | -50.56333 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 411e2143-59aa-3666-853a-c05d27dff686 | -6.13375 | -47.93397 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcf041bc-5200-3b7c-af5b-88229ed85afd | -5.72902 | -41.76957 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b474ffa9-8962-3455-bb89-45c248d06a6e | -5.24168 | -50.91265 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af3c4aef-55ae-3131-b148-0814ae5829f8 | -5.97786 | -41.37519 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7765670f-f585-3efd-bae0-e1d1ef6ed34a | -11.61654 | -43.64219 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 320291d4-6f6a-3ae9-95e1-9f78e6f97f72 | -5.75559 | -41.62987 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f8b68f65-fea2-36e3-8bbf-1acc870e5db8 | -10.44124 | -47.27566 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 812da34c-4787-3baf-9a5f-8004383415c4 | -9.89923 | -44.79988 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f78224d-d073-3062-980f-efad5a52d304 | -3.16692 | -50.46433 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 292110d2-431b-3fbd-9a47-bbd35e0df544 | -3.47795 | -50.0925 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00d92daa-f2d2-3ec7-93bf-6a1ea229a5c1 | -9.79651 | -47.81632 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178735fc-458e-3a1e-a143-54daf9462d15 | -6.67336 | -43.48207 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa3d0f59-c3cc-3190-9d73-cdb9e7132b98 | -5.52078 | -50.02484 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b0a849-ef94-3543-abe8-caca7b52097d | -6.83839 | -42.2929 | 2026-10-08 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4ae3a0c-eac0-3fbd-a3ca-c82d334a7544 | -9.80157 | -47.81726 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 953eea8d-09f9-3cba-adae-221bbffff3c7 | -7.60034 | -46.76102 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fd7cd62-736d-3d61-ab22-5b8a5bc56607 | -3.18977 | -50.57188 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b30e91cd-57f9-3adc-8533-0ec48a2b3a7a | -5.72972 | -41.7653 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b99f81a4-fe58-31af-b792-c8aea15e4710 | -6.89 | -43.68887 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4d21eb1-d19f-3c57-b18b-6f38aa8c0b67 | -8.21902 | -46.34687 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bb3484b-ce1a-3eda-9d79-266161c38f8d | -7.30273 | -43.98709 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d0033c-a0da-3c25-be3a-1311421c9bcc | -7.20877 | -36.62007 | 2026-10-08 04:02:00 | NOAA-20 | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7ba2459-1e5c-3dd8-903f-94345b1c0cd9 | -6.8801 | -43.69824 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f6bccedc-8637-39ad-9c97-ec2f6eda7132 | -8.20918 | -46.37521 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f61db24-feaf-380b-9b92-922fae8fd9af | -6.14332 | -47.93588 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 12add748-98a5-38b6-91a9-ecba8f00adef | -7.22411 | -44.27259 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91d5d303-e370-39ea-8a85-e09620626405 | -7.46911 | -42.84018 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29bc2fd4-dd35-3756-be8f-62da9e85c521 | -5.04832 | -49.76761 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac7ef95-8973-3848-9615-ac79eb5c3034 | -10.15881 | -44.67683 | 2026-10-08 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47e8a9d3-07ac-317d-b937-8dc20e0b2579 | -9.91158 | -46.79635 | 2026-10-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3faae46-ede6-3225-aaa3-a8a3518a45f7 | -8.99759 | -46.76007 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08f9b14d-4aa9-3566-b0e1-19d8f14cd2b3 | -3.32279 | -50.18034 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f11489a0-c4ba-39ed-b4fb-346e2338cd9c | -6.16034 | -39.43946 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9df2b6b8-a5fa-3ba8-9374-17ef8de83cac | -3.80665 | -45.41294 | 2026-10-08 04:02:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 681389c4-1fa7-39bd-8fbd-3edb91502368 | -5.71164 | -41.67051 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d08e7c93-e83c-30d4-a08e-1af9973be2e3 | -5.72537 | -41.76897 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0bb8a8ad-ed80-38ae-9c5f-8ef4020d27ed | -11.22702 | -44.87689 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a79b19de-ed6a-3255-838c-f579fae907e5 | -6.82596 | -39.54959 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc7d088c-2d11-3739-b336-83af5e508759 | -4.59127 | -43.82872 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d35a579a-275e-3166-a804-f8a9e910ca1b | -6.14393 | -47.9323 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7ad9c385-6eee-328c-983a-4ecc166538ec | -5.72677 | -41.76044 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8c399ee-243a-3827-a89d-00ec12b17add | -11.63343 | -43.70175 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aceb6827-2100-394b-a838-8fe0666c8103 | -3.25047 | -50.40075 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8599a441-330b-3c81-a99d-74373f22a80d | -6.62724 | -43.73566 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62624b21-54cb-375f-b0ef-b448414c6193 | -8.71894 | -45.19204 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 806fa8af-a5c9-3270-948e-5cd8445a7ed8 | -4.45238 | -47.91918 | 2026-10-08 04:02:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e6f4cf03-e7a9-3163-bdb6-bc996c368724 | -8.74269 | -45.15777 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d0b12a2d-c86b-3399-a0f0-7efea536a5ee | -7.70739 | -45.44556 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22bf7bbf-6caa-39a3-be9e-8a3ca7333363 | -5.97054 | -41.35295 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 30dda4b7-5425-342c-8012-26537f542c2c | -5.4925 | -42.86642 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8ab7d962-5d45-36c0-8129-69f4c7906438 | -7.46847 | -42.82097 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 89782d7f-5648-3723-b99b-9f0a86f0b0e8 | -11.2679 | -45.19556 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8924b345-6861-3e0e-adc4-e483c6dfa898 | -6.88537 | -43.69172 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69435079-7476-33ed-a080-fed2e5248ed0 | -4.2913 | -49.09276 | 2026-10-08 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75750019-65c4-3043-a459-0165b895c2b1 | -9.8298 | -44.78345 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76a1b60c-977d-37bb-8cd1-1caf344b1a26 | -6.1411 | -47.92426 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e87aba2b-ce75-3cc8-9c1a-5ad8830ce1df | -9.81157 | -44.7765 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deea83ca-3d24-3dff-a8a2-c9a9abb7330f | -10.76907 | -46.58187 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fedd013-c279-3978-810c-f77fb75596d8 | -9.56112 | -40.33691 | 2026-10-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 361d8324-5024-3368-a2e7-b04dcfd3bdad | -8.98119 | -45.94769 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0b1b8ab-c21f-36fd-9b5c-bd4d7b61b9fa | -6.81702 | -38.53947 | 2026-10-08 04:02:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 007518d4-39cc-3e2f-9dd1-cc43396803e4 | -6.3573 | -42.57397 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e0e74c73-9abb-35c5-9903-ab64727e3a21 | -9.12243 | -48.51592 | 2026-10-08 04:02:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0f40ebf-2217-369f-ad13-98b7c6ab6dc7 | -6.63593 | -43.73351 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 634e9592-5eb7-3523-88bf-ddf1a0389d7f | -7.46594 | -42.8589 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cbb0cbef-fe1d-3243-8624-82ceca35a153 | -3.85957 | -50.42352 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cee9717-a6ab-3113-85bc-1f15f25a022c | -9.02612 | -46.90664 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ec989c-b9c2-39d1-8568-cf91f61fdd55 | -5.49026 | -42.85473 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a3778681-9324-37af-a29d-7f2ec06919aa | -6.13244 | -47.9341 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f39321ff-0eec-3e90-8d78-24dd233729c5 | -4.6827 | -40.8308 | 2026-10-08 04:02:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6641c4be-5624-3c39-956e-2cc0082133d9 | -8.21399 | -46.32031 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 505172e6-df53-3186-90cd-f1a18b1c6541 | -6.16311 | -39.44352 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16a6b29d-a10d-346c-a780-1c9a94cfff63 | -2.784 | -51.67715 | 2026-10-08 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d174662-0b2a-3c5c-bba6-5e262c714076 | -8.72973 | -45.18119 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e19e4b05-7b90-31b3-8958-462ddc7dec32 | -9.91639 | -44.799 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c292be-8c4f-37b7-9493-3286fa724afd | -11.22369 | -44.873 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd7b747d-89e6-3cca-9d61-0baff674b160 | -5.1131 | -47.12396 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 99b2dcdb-b4f1-3cc2-b492-83c1f993b64d | -11.45814 | -43.38491 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5c4aed5-cb86-33fe-bbc3-3066f346ea94 | -8.38984 | -46.30527 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| deb6647d-834e-39c8-b9bf-6a14859e712b | -3.2006 | -50.56691 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9d74951-6307-3465-a5ee-df2c0ef10dd9 | -8.72114 | -45.17947 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6871424-e2f9-3159-b5e3-adf2767e5262 | -9.82743 | -44.7832 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 267ce146-ff72-3981-989b-922abdd51901 | -3.18614 | -50.5527 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 756985cc-3390-3a7e-8523-95679c75138e | -3.16455 | -50.59805 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b738760-b105-35d1-b57f-609ab5e26adc | -6.95156 | -45.26982 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3cc05500-e80f-3977-a55f-b71d1b1a1614 | -11.62675 | -43.69555 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ad1a630-4dba-3b52-81f7-9c2e358e251e | -6.82484 | -39.55659 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df45f6ea-b983-3dd0-8c4b-da38800b5836 | -5.72638 | -45.15785 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README69.md)
