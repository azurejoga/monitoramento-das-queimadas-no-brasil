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

## Dados Diários - Página 270

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2961f578-5a85-3ba2-b5dd-3a619caa7b49 | -9.98753 | -45.98409 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c980fad-0066-325f-a960-03089f8807a6 | -8.90159 | -45.41072 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5016908-afff-3119-b83d-79e68a7cc4ea | -7.39308 | -44.74697 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0fc1aed-20ce-3894-9f83-06fa1803ae66 | -11.21625 | -44.84726 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba90ec7c-ef10-30ab-ad26-cb3de0c74c43 | -9.75202 | -45.68345 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 7f931208-ca8e-3756-ab91-62b6e17d2863 | -8.66242 | -44.88394 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ab974f41-d837-3773-a99f-22a5fdb4bf26 | -11.2381 | -44.87337 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2d76f487-abb4-3c5a-b1fc-487c48a4a1a9 | -7.0284 | -44.7966 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| afa0e476-bb86-39d7-b83c-52ff0667da4b | -10.96198 | -45.38558 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee95b92e-40f4-38c8-8a3c-efc01a53eb8e | -5.12499 | -42.97191 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 17630c34-8836-317d-a053-0cb637164a0c | -10.47914 | -47.50094 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 976139f2-6597-3ec5-8517-57474ff936ac | -4.58037 | -40.66946 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 3ef33193-edee-358b-894e-549338328211 | -10.82748 | -47.3387 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| daca99f0-e36a-3a34-b0a6-80c683cb4156 | -5.84284 | -42.68607 | 2026-10-09 16:01:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 201c5420-3f64-306a-91dc-1c85b2cc7ec2 | -5.76132 | -42.09297 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 53f0c6de-b206-3634-bce0-7b97494c529a | -10.91632 | -45.39441 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 57139799-aa1c-3761-b57a-337c0f15c78e | -6.97099 | -45.25185 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41e3087d-a105-36d2-983b-85867bc3744b | -5.15167 | -39.50774 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2067cf23-658f-30e2-9d53-65796c710cae | -7.01439 | -47.67684 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 943e620c-0070-3805-863c-0b041099ced1 | -6.49665 | -41.82098 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3a6df09d-a707-3d4c-a8bc-ab7880ce205c | -5.99825 | -40.97783 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c33d13a2-8b89-32ca-98bd-d862cfdc4fc2 | -5.49232 | -40.54922 | 2026-10-09 16:01:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d8b15565-7291-35ab-a6a5-bcca9967bdd8 | -11.06938 | -44.08973 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 77794944-d076-3970-8a8f-1442938d07a4 | -10.82114 | -47.34655 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed8b4caf-3cf1-3fb0-bbb9-ad75b19a7b99 | -5.69813 | -41.74292 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3cc0ea68-6480-3a43-a351-8af2cb580f0c | -9.0151 | -45.94119 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3c728744-b62a-356d-8890-9d84f5f35bb0 | -6.88345 | -43.68933 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6f0dabb6-8bac-3404-a5a4-2f0e411cfc8e | -9.42779 | -45.81666 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0203e1a2-38b4-37f8-be59-a66e0b9550c2 | -9.91379 | -44.86059 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f03f40e0-60a5-3817-b74b-86dc33910dc8 | -5.76608 | -42.09233 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 935fccb1-9e09-3669-b77b-4b1808518ba1 | -11.04132 | -44.05465 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| a70f8334-ee1d-3830-b5fd-df9aa2a37174 | -7.40756 | -44.7658 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d2cbbe2e-50ca-308a-a3aa-5aef7f7235ea | -7.00747 | -47.67806 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f13a18fe-0ded-3334-ae8c-d8cb3f7a632d | -9.10138 | -45.12303 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c05b21a6-b3e8-3d0d-9eab-44ce0b126a00 | -9.76561 | -45.67841 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c52945bf-6516-3f33-89ef-dff7f7845896 | -6.9479 | -43.66615 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5346da0-5583-34cf-b72a-38c18cef9ca6 | -9.59734 | -41.6357 | 2026-10-09 16:01:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c09f603c-5f91-3a1e-ab4d-d2b35c5e7c60 | -6.57729 | -43.05552 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4929c0a2-7497-3cfb-92f9-963a6d225429 | -7.16042 | -44.50325 | 2026-10-09 16:01:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0d0a855f-afaa-3d33-932f-11a07afab948 | -11.20349 | -45.31955 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83fa4b7b-acb1-3388-83d1-033ff1895f9f | -10.3229 | -46.25765 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 27012bc6-f4d8-38ac-be7a-175dccf31e96 | -6.88887 | -44.90508 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e94a1117-67df-35d1-9626-7e5c3d1bcbd0 | -11.06299 | -44.0862 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| be649ed6-e916-3fca-a835-9ce904b6523e | -5.10846 | -42.85342 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fbfc99e-a348-3964-9afa-8999739c8ac8 | -11.22885 | -45.3159 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 112d95ed-48e8-3f9b-ba90-5ebc11795ace | -9.73929 | -45.68531 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67f9aa9a-603f-3cf6-969a-a6654753f547 | -7.47485 | -42.79056 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2d550a81-9d0f-3e24-8c78-b40cf5bab590 | -7.2978 | -44.01548 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0dee1f57-9ffc-3b21-9d67-d64f8742b62b | -9.86524 | -44.86732 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| daad8c26-e52e-37e8-8bf2-70a8d4f1d201 | -5.38999 | -42.97249 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2b7fe63d-2106-3cbe-a46e-6da1d8f06690 | -7.39327 | -44.75138 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 577bef3a-0dc2-30ad-abc7-778c70da2abe | -10.45491 | -47.19423 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c28caa5d-a81d-3365-a2ed-f872853d6405 | -5.76752 | -42.10259 | 2026-10-09 16:01:00 | NPP-375 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 807f2fad-15ce-3165-9b71-cd1c9fb71b00 | -10.4806 | -47.23137 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bde25365-239a-36a8-adbf-1ea9c0805bf6 | -6.19678 | -40.80473 | 2026-10-09 16:01:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0db8d2c2-4e16-3a1b-ab71-cafe22dee5f6 | -10.85715 | -45.56684 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fdf0ba87-0b32-37db-b8fb-568fd71add73 | -5.5196 | -43.05707 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 683344e1-6487-329e-8935-3f94106482cc | -11.07195 | -44.11091 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 428.6 |
| 71ed237e-5af5-3207-b438-f757c4452bfa | -10.84415 | -47.35794 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bf519c02-9b68-350c-8cbe-6f45435b97fa | -4.56884 | -40.73121 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4f308e36-5e4c-3e41-a40a-d8418f606f20 | -10.94652 | -45.37721 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 23be225b-5ebc-3067-9196-96f6caac8504 | -5.71829 | -41.61827 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e2ac438c-e4c8-3261-aefd-df1f87f1877c | -6.81936 | -39.54976 | 2026-10-09 16:01:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 56c9dd89-6cae-311f-8684-1de8d8470f6d | -5.07752 | -43.06384 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1b70141-32cb-3f7f-afec-31b62b843158 | -11.42853 | -46.67483 | 2026-10-09 16:01:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1cf7ab76-21e7-3717-8028-048b8427b3e4 | -9.87301 | -44.88039 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c9261038-d539-3d20-85e9-3f00f2dcdf26 | -5.87552 | -43.53695 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87814135-c628-3f1d-9d0d-faf7397b7be4 | -11.09858 | -43.99328 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40188aaa-2d73-3404-b8cc-bebebd08e8d1 | -10.40351 | -46.24905 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c670e26c-155e-3935-9c8f-8155f71a3e95 | -10.42471 | -47.30828 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3f72a1e-bf42-3179-8026-a1f1bef28e12 | -8.97609 | -45.16098 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4a7f2b82-80f8-3e3d-9363-42d388c2b8e5 | -6.48865 | -41.83262 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 896e33ca-f2ea-3d0b-aac8-25687c9dd9da | -9.75269 | -45.68866 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c30a1408-a161-30d8-8b0e-5524cbaeaba2 | -10.39328 | -46.24654 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d3e8cf49-d28d-339d-b08f-490a6d647267 | -11.04414 | -44.02871 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 53f64475-10f3-329d-8a3e-0f581ce4cfe0 | -9.55003 | -46.85155 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 563b6566-9b8f-3deb-bf48-d55b01176bd7 | -5.07016 | -42.69733 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f9c9cde4-a018-31c0-9345-7501731fc373 | -7.48013 | -42.8298 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9e54329e-4540-37bf-90bd-aa75fa308033 | -7.02372 | -45.30975 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95f4eb27-9dd3-3eac-8259-55031c73faaa | -11.01829 | -45.42495 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 73b867ca-b12d-3968-bd5d-91099a7473ac | -6.93708 | -43.66742 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 52dd73d8-1f79-3c15-b0a1-9216528b8a2e | -7.08232 | -44.04123 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 766ad648-a3e5-37d6-9fdc-7fed550d1d53 | -6.00266 | -40.94642 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| cd2b4e6c-c810-3707-9baa-63a74d3a8b38 | -7.45943 | -42.84364 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3fbcd12d-8f99-39db-818e-06eeb6c71ca8 | -7.48258 | -42.84798 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 712f3659-f55f-362f-8c23-f4493838ad14 | -9.72486 | -45.55459 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6e277cf-b1c8-3bb0-b2e6-802d58190298 | -10.42671 | -47.30132 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 2b9dba56-40a5-3a60-892b-6edc764bf01a | -11.11868 | -44.00723 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 17af692f-1a04-32b5-b00f-3c985aa06700 | -10.85879 | -45.56924 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 534553a6-cef5-3dbb-b72e-6b885bf98cd3 | -11.06812 | -44.1286 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0dff86c8-49b1-382f-b27d-9eae6734366d | -9.35522 | -46.57356 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a35beb3c-8b20-3950-a12d-3d775cc6b8be | -11.28212 | -45.1976 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 693f4f69-4c95-3af3-86e8-509d2f3d865a | -10.83379 | -47.33065 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c7f6bcfe-3e16-3d8e-9d12-4be17717f0c3 | -8.97307 | -45.13706 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 99ead853-1b31-311f-ac69-06f336bd33f2 | -10.40193 | -42.57121 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 71ccdd58-ef8d-3981-857f-4bf3d5f0a74f | -5.45501 | -42.89095 | 2026-10-09 16:01:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f655fe86-f54c-3b1f-b306-361ff7238289 | -11.12445 | -44.01143 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1688c582-aca6-3a83-a861-a13780a74f76 | -6.21211 | -37.87141 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 11.6 |
| dfd99d89-12c1-37d6-bd46-aed1284f5297 | -6.9463 | -43.94349 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29c77787-d34b-3567-a6df-1c3bbfdfe0ec | -10.70224 | -44.2056 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README271.md)
