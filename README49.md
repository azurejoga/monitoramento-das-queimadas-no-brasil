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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 993b661a-eaec-376d-b064-4147833f8d3d | -7.21818 | -43.86098 | 2024-10-15 04:25:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ca2b82f-5acb-37a0-b348-1c24a6840a7c | -7.13018 | -43.91965 | 2024-10-15 04:25:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a378b9be-092d-3d64-bddc-46408af1f4c7 | -7.12668 | -43.91911 | 2024-10-15 04:25:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10096a1f-e217-3aa6-8729-335ff2a0fad4 | -7.12018 | -43.96185 | 2024-10-15 04:25:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95656f92-57d9-3243-93d9-5976a80b9546 | -7.39857 | -45.19166 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86dc3747-ab7c-33ce-9118-a2921269c78b | -7.39802 | -45.19523 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8ff2125-a96f-302c-a48b-a267838ecfd6 | -7.39521 | -45.19113 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 858f99e3-526e-343d-998a-b1d108055047 | -7.39465 | -45.1947 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f93bffb-8f35-3d79-b1cb-c2adaa1476ef | -7.28555 | -44.97611 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af766747-3aae-3b12-b4fe-e5eaa9dc8b26 | -7.28217 | -44.97557 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eea7f3e3-7a43-3473-846b-a91e2b8050bc | -7.01141 | -44.87506 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba2777e8-894c-34ae-9a4b-2244b40c4ec7 | -7.00353 | -44.88121 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c7dd78a-90a3-3405-917c-51185b948172 | -7.00229 | -45.18578 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8c611c3-4d85-3611-9e00-589eb0b3ed91 | -7.00175 | -45.18934 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a78b0286-975f-3e52-ac4a-55fef67001ca | -6.94899 | -45.21024 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a09c8935-7523-3b86-b45b-3c5f762630fc | -6.94563 | -45.20976 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee4327e2-359c-3bf5-bc30-d23f1018c2cf | -6.93978 | -44.59277 | 2024-10-15 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a81b77a3-ba3d-342c-9ae4-0d461ea1fcfd | -6.93921 | -44.59642 | 2024-10-15 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2e7d41d-0b58-3565-9866-b83b79a3124e | -6.92871 | -45.1415 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f6ce6e-c5f3-350c-9a28-e097e05683a9 | -6.92816 | -45.14502 | 2024-10-15 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceebd77d-91da-3058-bcaa-b0d2ba4a9f43 | -6.81593 | -44.46902 | 2024-10-15 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3863004-d5ee-3ad2-97b3-e0c2817278a4 | -6.81251 | -44.4685 | 2024-10-15 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb667078-9c55-3986-a107-550b852f5bfa | -6.68739 | -44.03554 | 2024-10-15 04:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d56c4ada-265c-3213-92ba-cb0304b08089 | -6.68099 | -44.07734 | 2024-10-15 04:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0624d8bf-1f35-3f07-9f80-5b087379b0a3 | -6.58527 | -44.1795 | 2024-10-15 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9fb6f13a-4eac-3656-a7af-6f4f549b45b5 | -6.5824 | -44.17528 | 2024-10-15 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1102978-c3cd-3277-acb3-3c2355323cf7 | -6.58117 | -44.22875 | 2024-10-15 04:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1096e1fa-2c6d-39c5-b478-dbc89abb28c7 | -9.13483 | -44.78737 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210ff727-9885-3457-8f49-e5b909007ffa | -8.94717 | -45.03709 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c04f63a2-5758-3320-a796-d8741708d6a4 | -8.91593 | -45.0587 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5b31427-c34c-3802-8295-cbc86d89d434 | -8.91537 | -45.06236 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 206c4e0e-71e6-3848-a40c-a59b7a301118 | -8.91196 | -45.06185 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d244b0f-a335-3f72-b35a-c69eb582884b | -8.85497 | -44.84116 | 2024-10-15 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57ce7bee-e31f-34b3-8e01-6f0f31a294ee | -8.28516 | -44.85098 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad049c9e-e3ff-3585-a6b6-66a20460d74d | -8.24648 | -44.85257 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 528df19d-7b92-3e08-bdca-c1769b7b5bee | -8.24592 | -44.85629 | 2024-10-15 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0cbf48-caab-309a-8c8f-6edc69e23a31 | -8.15231 | -43.94709 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ae0edcb-3bbe-35a0-8d77-ef7c0ee700a2 | -8.1517 | -43.95106 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c26c61f-037a-36a3-b9e9-0e2adb6567d6 | -8.15169 | -43.9507 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f98da50-bddc-3de7-9b44-16f9d7c93950 | -8.14819 | -43.95043 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 866c56ee-91b0-31b8-a478-c86eda41865f | -8.14817 | -43.95007 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b776d5a-4c7d-3c7a-ae1f-2a75f19a5515 | -8.13231 | -43.95988 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a18b2fe0-c565-391a-9e82-8ff3bbc4ab6b | -8.1288 | -43.95929 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69ad5864-f5be-3b5b-af56-839c2e00ce40 | -8.12819 | -43.96323 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea4e80c5-93fd-3223-8f86-7dbef2e47956 | -8.06307 | -45.3889 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e82f22e-f784-3d23-aac0-08d7c613b063 | -8.06026 | -45.38483 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 943fc65f-47db-342d-9a2a-84bd734293c9 | -8.0316 | -44.82089 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a4d8377-5987-3aea-8af0-89ee00a9f1de | -8.03104 | -44.8246 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6050401f-fa0f-3665-8f02-bdb0c31498e7 | -8.03048 | -44.8283 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88717abe-8553-3f60-bf38-37b50dbe40ad | -8.01402 | -44.79884 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95653877-8c42-3c4a-b947-21d1ba7724c6 | -8.00946 | -44.80573 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 827b0b92-5f75-3276-bd2f-266b63bb86eb | -8.00888 | -44.80944 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 40e9f8d4-be48-3ecc-b825-57b7da1bdacd | -8.00662 | -44.80149 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaf3b35a-e6e9-38ed-952f-2103c9ea7653 | -8.0049 | -44.81261 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 603658cd-1bab-3652-a8d4-f535cefb843e | -8.00432 | -44.81635 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70d963fb-546a-3358-8e1d-9db744b314c8 | -8.00206 | -44.80836 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51b152fe-deaa-37c0-80bc-b81484a673f4 | -8.00149 | -44.81206 | 2024-10-15 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 954b6b11-03c7-3277-a5fa-dfe7616ec240 | -9.45422 | -45.5069 | 2024-10-15 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9225450-fe07-364b-96d3-ebf17e89503c | -10.13864 | -44.83409 | 2024-10-15 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee4685a4-425f-316e-bc1d-b4603eb472dc | -10.06855 | -45.04103 | 2024-10-15 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c7aa2a2-375e-3c2e-9aec-229adc8ce557 | -10.91668 | -44.71326 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 817b2ef5-475c-308a-a92c-25ead64e20ae | -10.82022 | -44.95319 | 2024-10-15 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 514e5edd-effd-3553-ab83-662523deb2bf | -10.75828 | -44.83371 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12059c9a-a02e-3ca4-8930-1678463d7f19 | -10.75219 | -44.61005 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d572a87f-96cd-3bbe-a1fb-f79c3cf0ff7b | -10.75163 | -44.61277 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760c8877-3386-33b2-b2b4-0fda4a8f9336 | -10.74181 | -44.704 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3655ed9a-4df9-330e-a097-fb15c3bc9550 | -10.73946 | -44.6956 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d455690f-d2b8-3a13-907f-bd06db8bc6e9 | -10.73904 | -44.69672 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5551f59c-f489-33bb-88c3-b9f046cdf019 | -10.73596 | -44.69506 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9ca53f0-ef27-3ef5-a120-4a2b1b144db3 | -10.73554 | -44.69618 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc474ab5-aff0-3105-b3d2-3dfe98fd9c3d | -10.72504 | -44.69455 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 644ff96d-6ed1-36b7-9d15-566b87dccdd1 | -10.60445 | -44.77631 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2a79efd-a3d6-3cf1-b610-bf8b5aa29bc7 | -10.53424 | -44.86425 | 2024-10-15 04:25:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f28d9535-2e7e-3b03-9df5-1a69cc5a9532 | -10.51536 | -45.15389 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a9cbd60-c1a7-3a06-9614-3c97c408f047 | -10.51193 | -45.15336 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7ac4dfa-d210-308d-85b7-02a252ccf620 | -10.49207 | -44.90903 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f49f8e-284f-35fb-904f-ac8f60c983ef | -10.49058 | -44.90976 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdb5b6f8-d395-3202-8bf8-02967c446308 | -10.39241 | -44.82005 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a3f8d65-6cc1-32cf-980c-88eea3942eec | -10.39182 | -44.82391 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cb5d9be-0cd3-3d57-9a0a-50cddb522fda | -10.38893 | -44.81955 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 460e80c2-3ed2-3898-8b02-6019b0b89f4d | -10.38834 | -44.82341 | 2024-10-15 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca4211d1-c77b-3a8a-bd64-19946701a85c | -11.94158 | -45.60939 | 2024-10-15 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1667205a-2ce4-37c4-9def-022a7157716e | -11.93816 | -45.60886 | 2024-10-15 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08fb5d37-0ade-3984-9d1c-2d4f5f20543e | -11.92135 | -45.76661 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79057914-1bb9-3ed0-afd3-5b84d9f19a04 | -11.91738 | -45.76978 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8be6b21-a730-3f8a-b56f-547165784e00 | -11.91682 | -45.77349 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9703984-9bed-335a-86d5-4b1927fd10cf | -11.91342 | -45.77296 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53ce62a5-ac2a-3096-a1f4-458fe3c41605 | -11.91286 | -45.77667 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d6f3c52-1365-302b-b425-7c06f4d72d9e | -11.90945 | -45.77614 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab867ed6-02e9-3d74-ad40-52f2dfec55ae | -11.90889 | -45.77985 | 2024-10-15 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 029b9862-8615-3cda-b6b1-7470f2c05b44 | -11.43895 | -45.2917 | 2024-10-15 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 329525c2-6cb4-30a8-98f3-116eedd140c4 | -11.05589 | -45.36171 | 2024-10-15 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e348e6a3-ba12-3fdb-8044-24acfd1330d9 | -5.45184 | -46.30091 | 2024-10-15 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d5ce885-7703-398d-9fde-270811b51dcc | -5.28692 | -46.39894 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd9c6129-da26-33df-b5d1-f9ec2b083494 | -5.28637 | -46.40241 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a01055fd-f6b3-371b-b758-ace5a4bb37c3 | -5.28582 | -46.40589 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e66eb510-2e0d-368d-a8e7-9f47ba958118 | -5.28304 | -46.40189 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af3f581b-e4c0-3071-9701-ea211694576d | -6.47464 | -46.05701 | 2024-10-15 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7ab5586-d584-3a67-ba6c-90035dcb00d5 | -5.48093 | -45.5134 | 2024-10-15 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 168eb1d1-4745-347b-a4c5-3624488e4b14 | -5.48038 | -45.51686 | 2024-10-15 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README50.md)
