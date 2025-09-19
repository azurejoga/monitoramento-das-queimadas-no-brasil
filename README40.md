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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c00161b-9332-3bba-9759-4473b2b4b775 | -9.1933 | -45.3114 | 2025-09-19 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8a226a0c-93b2-393b-b4e5-a04257041e08 | -6.1229 | -43.9578 | 2025-09-19 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 984169a1-1964-3de5-b947-9784810f6c6e | -8.9344 | -46.3119 | 2025-09-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d938d2f4-e3be-3494-8ef5-d051ee07391c | -7.6951 | -44.463 | 2025-09-19 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ce0e13df-a042-3e83-bc06-91b856638941 | -9.7334 | -45.9302 | 2025-09-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 618b52fe-d38e-3867-ae46-9d13a08d8226 | -7.6949 | -44.486 | 2025-09-19 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0b40a90e-9c30-3f5f-a750-22f0d226d2d0 | -6.1881 | -41.1855 | 2025-09-19 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 9148fa6b-49ea-3336-b6f8-3a982a6ebf52 | -9.1937 | -45.2886 | 2025-09-19 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 6723d399-ee88-3c54-83b1-8391e103a4e8 | -8.9344 | -46.3119 | 2025-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8d85a915-3e6a-3435-98be-6e7b3e9d3c8b | -9.1933 | -45.3114 | 2025-09-19 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| fe05a556-104e-3e43-9fdc-0c16cc349e57 | -8.9892 | -45.0376 | 2025-09-19 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a1f329c0-ea0a-365f-bf6a-2f212709ea06 | -8.9895 | -45.0147 | 2025-09-19 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9b07d470-dcaf-3a3e-8bd9-64e920016b8e | -6.1878 | -41.2097 | 2025-09-19 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| f182467d-953c-388e-aa94-af466226d0e8 | -7.6949 | -44.486 | 2025-09-19 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| caba21e8-94e7-3ab1-99fd-6ed9b37b2625 | -8.9908 | -46.3284 | 2025-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 99c36236-f894-3a9b-882c-963b62435cf3 | -8.9911 | -46.3059 | 2025-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c0822d97-8485-3cfb-92b4-3459e693efd8 | -8.0193 | -45.6846 | 2025-09-19 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e6cb226e-1170-3561-8673-af0dc35f58ca | -7.7148 | -44.392 | 2025-09-19 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 83006807-7fe6-3b57-bd49-71bdd9f6b79a | -9.01 | -46.3039 | 2025-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 0e502dfc-ba25-3a63-8b18-c2df3bf8c756 | -8.9908 | -46.3284 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 94cd6a6c-097c-33df-bf8e-75d87d434287 | -9.1933 | -45.3114 | 2025-09-19 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 97e9ca54-ee14-3067-a943-9fbc44ea95a4 | -8.8801 | -46.138 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 13d0ca05-123e-37d0-8ebb-2d680395d7d2 | -9.1937 | -45.2886 | 2025-09-19 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 1b7e40a8-65f0-3b20-9859-58927fb85fa7 | -7.6949 | -44.486 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 4b57bfe9-a6e0-3faa-a6dc-84fd7f008489 | -9.01 | -46.3039 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 4064dbe7-09d9-3171-b26d-ed84171b30ed | -8.6876 | -46.4495 | 2025-09-19 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 55bc40df-7e52-3378-8daf-217386831c59 | -8.9796 | -45.7439 | 2025-09-19 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 39fc951b-c5d7-3d8a-896d-bffd758764c6 | -7.6951 | -44.463 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7cbb3e3d-0190-3251-8928-b91a58f83b6d | -6.9212 | -44.764 | 2025-09-19 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1da265a9-fed4-37c5-9c37-1aa5760a4abd | -9.0097 | -46.3264 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 2db793fe-a029-33fb-a67d-28b2d435b301 | -7.1878 | -44.4193 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| dcd37458-9ac4-395c-b001-37d077f8e748 | -8.899 | -46.136 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 37f1e376-8559-3320-b99f-a1f596de4f9a | -7.6386 | -44.4686 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 248f6978-f630-31fb-8f44-a6f14a2f0b94 | -8.9911 | -46.3059 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 9fc41808-802c-3edf-89e4-a1b4200e3fe1 | -8.9344 | -46.3119 | 2025-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e4056248-562d-33e8-a387-70b69591ef21 | -7.7148 | -44.392 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 6a5ab624-79bc-3c8d-b526-6e6257d25194 | -7.6389 | -44.4455 | 2025-09-19 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 926aaf4d-79cd-370a-8b95-5f1f83d199e9 | -6.5942 | -45.5856 | 2025-09-19 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2a35fc6c-ecae-3070-badf-f24318ef7a71 | -9.1937 | -45.2886 | 2025-09-19 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 9a5c61eb-fc67-344c-8c41-44232f808bff | -7.6389 | -44.4455 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 371e3a4a-7344-3221-98e3-858a40ce7558 | -9.01 | -46.3039 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 5ba5a190-8a5f-3cdf-8f53-2f592b7a869a | -8.9911 | -46.3059 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f992bc16-bf23-324f-9392-c0d67531f197 | -7.6949 | -44.486 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 80899fa9-fe2a-38a2-b3cc-f84ff2feffef | -7.7148 | -44.392 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d28780eb-5c52-33ca-bf8b-ffa979d488db | -6.1881 | -41.1855 | 2025-09-19 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 183.9 |
| 98c9220a-ea4d-3a66-84d5-4f256a455aa9 | -8.0281 | -44.957 | 2025-09-19 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 3922fd82-4de8-38bc-8801-3ea9fade9ff5 | -6.9212 | -44.764 | 2025-09-19 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9f55e06f-059a-3a9f-b4ff-590416fe0cb0 | -7.6951 | -44.463 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b74d1426-7c83-3f2d-86ad-8b3213cf0f3a | -7.3366 | -44.5663 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9c9f7f29-36b6-3520-8a2e-8e3a36bcd4ba | -9.1933 | -45.3114 | 2025-09-19 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 238d3a87-8274-3ade-8d83-55e53c1da34c | -8.9179 | -46.134 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5dc0d481-1a73-38fd-bcf5-ddc1a22226f9 | -8.899 | -46.136 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 66347132-f156-39db-a7d6-c2f8775e6771 | -7.1878 | -44.4193 | 2025-09-19 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b88fd438-e3a8-3481-9e6c-9277f55729ac | -8.9908 | -46.3284 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 9987acf6-c664-3c36-a65b-727778d70920 | -6.1878 | -41.2097 | 2025-09-19 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 229.8 |
| d8bad18d-31b1-3625-8675-a22deb441304 | -8.9344 | -46.3119 | 2025-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 3364e5f2-67d5-3092-88b1-8ece8cb7a095 | -8.9344 | -46.3119 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 426.1 |
| b739cf86-d0bc-347c-80d6-6262a6d48d4f | -8.9536 | -46.2874 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| b06865ee-25eb-3a05-b7ac-5f76db1b7f35 | -8.0281 | -44.957 | 2025-09-19 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 48c21904-88d2-33b3-8329-6a0df5ff164f | -8.3709 | -44.6697 | 2025-09-19 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| af8c7483-5c69-3fd3-b2cd-bc5c7e5f687c | -7.6389 | -44.4455 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 5685e0e7-4a00-34e6-9892-306d7e704a09 | -8.6027 | -45.7162 | 2025-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d0d7514d-31a9-37af-8373-1ce3f1f6c143 | -8.9533 | -46.3099 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| dcbda227-8328-3099-9e7f-4af2239e7c7a | -7.5818 | -44.4971 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 667d9f2b-11e5-3308-b749-93f3016de907 | -9.1744 | -45.3135 | 2025-09-19 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5cc72353-d909-3fda-9520-d4fc20fd969c | -7.6949 | -44.486 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 530178f8-f449-3ddc-b79d-95bcc0ef8c81 | -9.1933 | -45.3114 | 2025-09-19 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 0db790f9-4e31-359b-a50c-f8a84a3c89be | -9.01 | -46.3039 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| c7700993-e06f-3308-a8ea-b542dd187b38 | -7.3111 | -45.1622 | 2025-09-19 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7ac2fdc8-ce2b-373d-9cad-024ab6717fcf | -9.7334 | -45.9302 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 0fef9969-a654-32dc-84e7-ee3294ff1ea2 | -8.9908 | -46.3284 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| c23e0058-3b01-346a-9b93-bd374a11d1f4 | -8.9796 | -45.7439 | 2025-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 377.9 |
| 5ef72b67-21ff-3032-87d8-55ce9b856497 | -9.0671 | -44.8685 | 2025-09-19 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| f945577b-8c4e-3d41-a058-8a4956e4e29b | -8.0193 | -45.6846 | 2025-09-19 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3c3abb94-cb26-3ac9-98b3-70426f20df3f | -7.6951 | -44.463 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 98f3358f-ac79-313f-9a1f-93ae7e18064b | -8.9179 | -46.134 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.6 |
| f86c5648-083f-30b1-91bc-3d0b1428feed | -6.9212 | -44.764 | 2025-09-19 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9183b762-7cd6-3944-bc23-c7b3051b0a57 | -6.169 | -41.2114 | 2025-09-19 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 4da5b588-7e6f-3d01-847e-ea756cdf078c | -8.9911 | -46.3059 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 9a5d9873-b430-3647-beeb-9af75970d78a | -8.9607 | -45.7459 | 2025-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d8c3f9eb-5968-3378-9647-c41d6a147669 | -8.899 | -46.136 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| d660e3ce-8916-32b8-904b-86cff35c2194 | -9.1747 | -45.2907 | 2025-09-19 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| ee0d7e11-f5d9-396b-bc39-ff66358a5e67 | -6.1881 | -41.1855 | 2025-09-19 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 0ffafc00-1436-314a-bbf9-18d47448f9cb | -6.1878 | -41.2097 | 2025-09-19 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 306.8 |
| 01b42b78-736d-34c4-b930-02042528de31 | -6.5754 | -45.5871 | 2025-09-19 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f63cb0ef-05f0-3ab2-8839-3e5fc2144528 | -8.6216 | -45.7142 | 2025-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 58be38d1-ac2a-39c4-be0f-5353eeb4da97 | -8.4834 | -44.7266 | 2025-09-19 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 71c9e9b4-6752-3f8c-8fdf-2a4aff766c7b | -7.5598 | -44.7743 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1256a978-2b9b-3d39-bb6e-45ea2f21df9a | -9.1937 | -45.2886 | 2025-09-19 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 294.1 |
| b19bc358-af71-308d-a5b3-77342ce465a3 | -7.5595 | -44.7972 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f50856e1-cf50-3024-9bbc-1aee9d233403 | -8.9182 | -46.1115 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| ffaf318d-6f1a-3186-87ec-5981e8cb3946 | -8.9347 | -46.2894 | 2025-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 037f9441-420c-3baa-a22e-e4b05bd36dab | -7.3366 | -44.5663 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b579252f-bba6-3132-835a-d6ed09a343be | -7.7148 | -44.392 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4617b4fd-e337-3cf7-9d0e-a0f55ac9752f | -8.9793 | -45.7665 | 2025-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 97f38e27-18f8-3696-8784-ec2ad4a7ee84 | -5.8073 | -43.6352 | 2025-09-19 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| af4dd124-331b-34d1-96b9-0f5656b77e3d | -7.6386 | -44.4686 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d8f3d396-ddad-3469-8a62-6a2e65f9ec4a | -7.1878 | -44.4193 | 2025-09-19 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 44a4d5ef-9664-3233-9e8f-bbeda07ecd62 | -7.6949 | -44.486 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 895333d5-ce52-338a-b1a9-33214b7cbe64 | -8.0281 | -44.957 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |


[Clique aqui para ver as próximas entradas](README41.md)
