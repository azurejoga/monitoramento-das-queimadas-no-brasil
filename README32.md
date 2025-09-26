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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ff8c240-0e2e-3ea4-b20e-c732c5188c3a | -9.67601 | -46.03101 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f15f31f1-e24c-3e1b-98c5-4b5c41ab6f18 | -6.42472 | -43.07632 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b77bccd9-cd60-36c8-afdc-5ec9c315e344 | -7.3091 | -45.75539 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d887b71a-6ce9-3264-ae18-c017fda4a5d8 | -5.64632 | -43.93215 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aad6251b-176c-3af8-b8ea-322a8c8d198e | -5.74373 | -44.97212 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| cd64af1a-9d9a-3021-9935-1ab35e57f7ca | -6.98587 | -42.59303 | 2025-09-26 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eff32347-4c8f-38ff-9a1e-9fcbcf90d071 | -8.71146 | -50.05442 | 2025-09-26 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aea9868b-2ea7-3eec-9ccb-7547c49bb179 | -8.93364 | -48.66262 | 2025-09-26 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e47500e3-496e-37cf-bbf0-7768ef0dbe23 | -6.42029 | -43.0756 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b03a6bcf-902e-3c6e-ad78-bbf7ae2e1892 | -7.31219 | -45.76054 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e67a9614-5e36-35ca-b524-ccbcda4f299c | -6.25486 | -42.49154 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4a3a84b9-423f-310d-a5a5-e96e21386c2f | -5.64831 | -43.9317 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 410215aa-7d6e-3f71-bad9-0b90b5cf42bf | -9.87069 | -48.87703 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d355ce5-2f80-3a9e-b056-c6d6f7c5d0a4 | -6.26145 | -42.47865 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e73343d7-86a8-35b6-8ec3-42cdb73df596 | -5.97121 | -44.12998 | 2025-09-26 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f49ff5ff-3f32-358f-b509-2d81cacc48af | -7.52895 | -47.28635 | 2025-09-26 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94f1e8dc-11fb-3084-9822-409053508cdb | -4.28062 | -48.18227 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21bdfef6-f298-3509-bee7-1cfd009b81b8 | -6.33606 | -44.01651 | 2025-09-26 04:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9837e108-567f-3b8f-8b0d-a33282add0d4 | -4.56823 | -49.40803 | 2025-09-26 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bc15730-f1c0-3f91-a13a-83d60a20879a | -8.71418 | -50.05157 | 2025-09-26 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39a1c180-71ef-3627-baa2-3f1b42893899 | -6.68001 | -43.5958 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7408b34-d2a0-31cb-bb38-a15ba636596b | -3.82236 | -50.9758 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06c78862-2f71-367b-a7da-692238f9eff6 | -5.78396 | -43.32614 | 2025-09-26 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3313681f-c75b-346b-94a3-47b9beaa4f0f | -10.39487 | -46.14186 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baddfe4f-f34d-3405-bc6c-15c89eb9e76b | -10.40438 | -46.15786 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 542c1d0d-0033-3715-8322-083ccb5d9564 | -4.48472 | -47.68021 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80afebc5-c420-3c71-a6c3-8b44118f2b4b | -7.0909 | -49.17597 | 2025-09-26 04:42:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08259c70-17ed-3d24-9277-0344e77eae69 | -5.75166 | -42.55473 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 530e0d63-b9b8-371f-a259-ec106de07ee6 | -6.55156 | -44.32577 | 2025-09-26 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 358a3d23-0a5d-317a-8be0-513dc4f9b31d | -5.74761 | -44.97271 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 0e775989-acc2-3434-9ea9-7519e0f8d8d2 | -4.48246 | -47.67249 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0613f334-b6ea-33d3-9423-2f2ba14e633b | -5.3698 | -42.29053 | 2025-09-26 04:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a89c37d6-b16c-36d8-ad95-5e5121bbc353 | -6.8767 | -44.502 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e100efe9-bfea-3846-be43-08d1f56b8c2c | -4.26649 | -48.55495 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69281dac-2ebe-35f1-aef6-294657ceb445 | -7.10303 | -44.48225 | 2025-09-26 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c32ad870-0279-382a-bed1-1433b125d344 | -5.79251 | -43.82272 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec4cc6dc-e4d1-3a1c-8325-60d6bf930f46 | -10.3007 | -47.95673 | 2025-09-26 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6379c5c-3855-3de4-a310-2f252bcbae40 | -9.05167 | -50.11497 | 2025-09-26 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bd8f59b-3758-36ed-a506-b3d1a6f37331 | -5.37442 | -42.29127 | 2025-09-26 04:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b72da985-d06d-3f6d-bcd5-e2df1cae7fd0 | -4.26316 | -48.55444 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d6b7b36-5c8e-363f-8fb2-94dba8ed577b | -6.82385 | -44.09153 | 2025-09-26 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3365484a-ffaf-3188-ab2b-e2ea6d8cb9a7 | -7.2704 | -42.97742 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c64c2f6-8681-397b-8fec-732bd337353f | -4.99911 | -44.87871 | 2025-09-26 04:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e56083e2-bca7-3c63-b0a0-896824509b7c | -5.63497 | -43.92311 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99f6d744-d3d3-3eed-a0d7-1dbd18b954f1 | -7.44146 | -41.91027 | 2025-09-26 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48e287a6-de56-3808-a9de-6df0909af572 | -6.63506 | -43.82668 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42bb317a-f988-3f8b-b6b2-4dbb493e76ba | -4.79494 | -47.27995 | 2025-09-26 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94fb00c0-2f5c-3497-a7ca-4f288b0f0b0f | -6.99746 | -46.99415 | 2025-09-26 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8007942e-2b8c-3137-a8a3-bd900ede9d38 | -8.19154 | -46.39064 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9247a5d-50f6-3823-8138-e34fd35fa7e9 | -8.14023 | -42.37706 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fb0044e-2f0f-3958-ac9d-a0439a003485 | -7.27946 | -42.9788 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 837e51c0-a84e-3111-aa5d-d0a67fc63c87 | -10.00866 | -44.17125 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5879088-9c56-3083-854d-95f7b4e71cae | -6.53231 | -43.87977 | 2025-09-26 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25037377-7c23-33b3-84c2-f73b898bfa84 | -7.13063 | -42.19128 | 2025-09-26 04:42:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9db6db96-5420-3710-a8fc-bf4568f002d0 | -10.40549 | -46.1776 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 62b02939-3359-38f4-b7d3-68f399d5e43e | -4.79955 | -48.71664 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00b77ed3-d4d5-307a-bb70-c2137a9adfa2 | -6.82544 | -44.16901 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406c94ec-cb73-326d-bcaf-487f0bd7394e | -8.08156 | -55.21883 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 635bf206-806e-3633-8fee-5ee9b063df47 | -9.69399 | -48.93507 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ab9c63e-6676-3683-90f4-3a16fd3537ec | -8.6136 | -54.99495 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c74a11-a3dd-3136-81e3-9fc0280af445 | -9.10875 | -48.89997 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d7e867-e897-3075-9cf0-ae91948c3003 | -4.4819 | -47.67609 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c58e4a2-8161-3503-8935-61ff72a5215b | -5.79697 | -42.81317 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10f07dec-e5f5-3307-8544-fd3e4c727f81 | -9.69288 | -48.94227 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea655cc5-6b8c-325e-8f74-0d49ec707b8a | -8.32345 | -49.53132 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dcef2e7-685d-3c47-ba3f-38ff29a09863 | -7.66905 | -45.9999 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad8fec9c-1843-3094-aef3-0697753cb290 | -5.46293 | -43.07153 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8b01eccf-13eb-31ca-b944-9aab49cdabbf | -10.19629 | -44.84698 | 2025-09-26 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be47808c-0a83-372c-8a21-f537984d3911 | -5.46731 | -43.07219 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f23bca63-6b8d-370f-9ba6-e43b1370398c | -5.5803 | -48.95293 | 2025-09-26 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1efbcaea-9809-3f26-afc4-61fdd380cb9b | -5.73913 | -44.97636 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f571a601-56f4-3f59-9793-16edf4d33579 | -5.7469 | -44.97747 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 43e523a1-8375-37e6-847c-8cec95d7dae9 | -5.45857 | -43.07078 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b691dc4f-1087-35ce-8beb-18a2c589b831 | -3.81405 | -50.79476 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 473d698f-2d9f-3039-a87c-c420dde5d0fb | -5.45998 | -43.06325 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2a2f3621-2208-3ef2-b1c6-f65ae7ec0e14 | -8.60718 | -48.96891 | 2025-09-26 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db78fde-de09-371d-8976-176ec10cde4d | -5.8015 | -42.8135 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6e8db60-a1bc-36eb-b0cf-465e72f579a6 | -5.83085 | -43.9099 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1f7f8ec-4f4f-3ec8-8687-4fdc7a088c45 | -8.79371 | -46.59009 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20cd10e7-84d0-3238-a2bc-42818f1c00fd | -12.8752 | -44.69873 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 818951a5-e848-3c7f-8056-bc9016cfbbcf | -11.61331 | -44.42602 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34d00777-59e2-36da-b900-e5940755f5dc | -12.87408 | -44.70721 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7fb7cdc-1bc5-36a5-b711-8cd1b9e69957 | -11.96469 | -47.88073 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a0d3f389-5a5f-3d7e-9931-0d3e24ed9c53 | -10.54132 | -47.51972 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5de2caf-5b8b-3427-a22c-db257bf4487e | -12.7718 | -47.51099 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06f258c9-9f7a-393e-bb26-6a7855d9bbdd | -11.66552 | -44.46804 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30c15c1f-09e7-32f3-aebf-0f919685100b | -15.03225 | -46.94055 | 2025-09-26 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9adcd2d6-2ffa-374f-a508-da92e52478e4 | -13.88895 | -43.91543 | 2025-09-26 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b8cccde-6f8c-3d28-ac11-40a67ec7b347 | -15.90611 | -57.48854 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6e699aa-d5f2-32c6-851b-2a0f0e1404b2 | -15.37477 | -48.59963 | 2025-09-26 04:44:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 690b3aa6-2ddd-3feb-a05e-79a4252fe6b7 | -11.62034 | -44.44003 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef629538-bc72-3467-8f30-72d6ab663aa0 | -11.65322 | -45.35502 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2de88530-1a6a-3f25-867c-3d2b5f006c47 | -13.8553 | -45.60936 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc381666-2d17-3c09-af85-c54ca0d149e7 | -13.85112 | -45.60876 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61420c93-86a1-3dfa-aac1-accde4d1ee49 | -10.18354 | -49.51035 | 2025-09-26 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26acc14f-8c81-3091-8fa6-814820479f0b | -10.92969 | -44.29962 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38b1a256-e71f-39c5-ba83-e7d9b337b3b6 | -13.84538 | -45.61983 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f186b6e-6ef7-3c7e-8da8-df143a3813c8 | -15.72425 | -59.4914 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa1c75bf-7d5c-38ce-bf51-2f59f526c68f | -10.45055 | -48.08244 | 2025-09-26 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51f52d5a-9605-3d76-8e49-f1cb43962215 | -13.24295 | -50.6955 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README33.md)
