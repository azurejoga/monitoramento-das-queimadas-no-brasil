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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bad8c864-2b1c-3a78-b7df-b87d9f1b744d | -6.19654 | -44.24233 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 134125f1-5f66-3ab8-bf35-06715f7b95c1 | -5.48163 | -43.08186 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2136b472-0ad5-3117-969a-7e1d60d6a5ac | -7.12176 | -42.17986 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3b001e65-5036-3bf4-83f9-ce7cbbf4162a | -4.44354 | -40.96868 | 2025-09-27 04:21:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fcf5477e-3b88-3398-961f-b4e04d4fd443 | -5.67068 | -44.85296 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 452d437b-8687-357f-b4f2-a00c5240b10b | -3.58656 | -43.09696 | 2025-09-27 04:21:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e83b1734-31be-38fa-8b99-2c35f366f259 | -6.70004 | -42.75189 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c4894b0c-289b-31a8-ac11-ad4d75e50878 | -3.31209 | -44.1894 | 2025-09-27 04:21:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0c95efb-ba41-375e-a9b4-22413eb0526b | -6.27317 | -44.07184 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aa87cd2-c071-311c-8bec-072140f6c0cd | -5.78817 | -45.36864 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d893913b-9f3b-33e3-b52e-5c1de8283a9a | -6.23141 | -44.19428 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 03dd96dc-575b-3987-a016-ae197df6b041 | -4.57609 | -44.07303 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 218e27f8-f1a3-3748-9fd1-429795ba983e | -5.83225 | -45.8772 | 2025-09-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a383221-ce87-33ba-9aba-71c4472b0754 | -5.23944 | -43.07046 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ea04213-8ed4-3d67-afe9-8929e7550b06 | -5.08495 | -44.85308 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b66af15-60c2-3a2c-ab95-39d37729a7b3 | -7.63305 | -43.80505 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c70972e9-bfce-370a-a4d8-1ed4606a30e0 | -6.06218 | -44.08138 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5ad83d8-d057-326a-b7f8-29b392bf6557 | -3.82637 | -40.33729 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fe9b246-aea1-3a88-9ddf-85cdea712b83 | -4.00588 | -46.9666 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b7bae616-b8ea-38f5-b0bc-e0771675a8a3 | -5.54738 | -45.0546 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5f4551f-db36-3fdd-b29e-0fc7da7483af | -3.82495 | -40.98931 | 2025-09-27 04:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 962a23e9-be75-373a-972e-b2ab5b7db00a | -3.82434 | -40.35076 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0588a4cb-d762-3286-9ddb-8d2e23a3eccf | -6.24776 | -42.48037 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0b243152-0399-34e4-87e3-ec12d7b80474 | -5.76204 | -42.55146 | 2025-09-27 04:21:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 430198be-6d0d-3c96-a409-61a60f920d2f | -5.94577 | -42.71693 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb480312-060e-3374-9982-06ab2941528f | -4.1707 | -44.26839 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea2ab95b-ce2c-3843-b65d-32f88df54622 | -3.70076 | -49.01789 | 2025-09-27 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d11d44-01fc-3a4f-84f9-0ebd20126910 | -5.40089 | -42.27372 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74447ca1-8277-30d5-8559-c20328a13a3b | -5.47936 | -43.0741 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2353c2e0-3a5e-3b8c-a350-a4e7423ca0c7 | -4.53651 | -48.64631 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a3cd684-ad74-372f-a2ce-4f9e91575551 | -5.49461 | -43.06535 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 950d06d8-fdf8-3ed0-be82-e1ace7d3c826 | -5.47824 | -43.08133 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc0c3c98-c288-3501-8c70-037876a2f78e | -5.86071 | -47.26854 | 2025-09-27 04:21:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60f6c241-eae3-3cef-9ae0-dc3727d45290 | -6.9452 | -43.24796 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cab4de37-c179-3103-8407-7f9e54d780e5 | -5.80078 | -42.82409 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ac19547-7411-368b-a972-15ef00de0c42 | -4.16405 | -44.26735 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 846d0090-faa8-37c5-afa3-5d379ecb9a52 | -6.25586 | -42.47395 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f160e0b-bd01-3e4e-8ab9-d10670fce8c8 | -5.07663 | -44.86245 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4eeb98d7-ffd0-36a7-820f-f0d2f1a58d96 | -3.9981 | -46.9695 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90344d77-5965-327d-8143-73368a2b9496 | -5.46888 | -41.07196 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3695e112-f67b-3ce6-bf72-95101deae817 | -6.99673 | -46.9904 | 2025-09-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6860d57a-b659-324a-8b18-80e5909e42a3 | -3.82432 | -40.99346 | 2025-09-27 04:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8246431-86c5-3661-b22e-5fa8cd22e23d | -1.78004 | -48.77317 | 2025-09-27 04:21:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 872048a6-46b5-32c3-890f-c171c3850e0f | -6.21861 | -47.33191 | 2025-09-27 04:21:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4449bc3-8319-38aa-9bf4-fb07f16cfb47 | -6.07382 | -44.07253 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0d99d59-ac19-3047-b446-96b9965ab03c | -3.23983 | -46.7983 | 2025-09-27 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6da1d43-fed3-3cf5-aae2-d24c007c0198 | -4.7737 | -41.04813 | 2025-09-27 04:21:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e2c5dc3-531f-38c2-9b04-13842d958b15 | -7.38111 | -44.0355 | 2025-09-27 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d111a04c-146b-3f04-bc54-8a70375ba7b9 | -4.1904 | -44.28968 | 2025-09-27 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e6a3bb9-fe76-3d73-990d-a14db19a88b7 | -7.34713 | -42.09225 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc9754c1-262d-3e76-aeed-5bd7b59fe82a | -6.53333 | -43.83485 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3091811c-cbe8-3273-9313-243a6ba536f5 | -7.14491 | -45.5125 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 034ce173-9e00-3289-9f39-e4274deab8bf | -5.97644 | -43.24179 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc614fe1-35c4-39eb-849d-9d3552510153 | -5.42314 | -41.32463 | 2025-09-27 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fab11ecf-0da8-37c0-8833-66f5e7185366 | -4.79824 | -45.12212 | 2025-09-27 04:21:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78f0bc39-ff7e-316d-b13e-e2ad5b7d0fc1 | -5.67345 | -44.85696 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b00283c-70c0-3678-8ceb-e0e34e3fd6fe | -7.56858 | -42.41462 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a48de769-3898-365d-9bb0-ba6f3edd5459 | -5.82256 | -41.2949 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1c43e88-5848-3e8e-9a00-f3de110ac15a | -5.5353 | -42.82558 | 2025-09-27 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc8177cc-9e97-39d5-b8c2-a13d79e81ab4 | -2.49267 | -49.26869 | 2025-09-27 04:21:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b57afc6-1b7b-39a4-98c6-b22cdb2486b7 | -5.90566 | -43.67615 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d05da16-956c-328f-901c-bd8e35dcbaee | -7.00715 | -44.70103 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19b05bb8-7022-33fe-85a8-25956b65f17a | -6.27597 | -44.07584 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0880ad7d-62c9-356d-83fa-e091e5719e85 | -5.90231 | -43.67563 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb3e13d7-fe93-3c47-91f8-4b77be50a08c | -3.5993 | -49.4598 | 2025-09-27 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92f70bd9-4988-3fff-a54e-59b92f847a8c | -5.71122 | -42.61348 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0b12583-30ec-3f1b-87f2-eef861e45d90 | -5.80863 | -42.81394 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6991fea-287c-3bb6-b21d-a10ca727768b | -6.32016 | -43.4531 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ade7fe1-6eb7-3c4f-8bec-f1830a95e709 | -6.07491 | -44.06558 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f25d63ff-e921-3271-8e2b-d36527e2da6a | -3.99959 | -43.23417 | 2025-09-27 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6af0f48b-fe22-3e0a-8f72-ceb82431efe1 | -6.42891 | -46.16405 | 2025-09-27 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94f7f224-01f9-3ae0-ad30-55092a6fbcb1 | -7.07047 | -43.86 | 2025-09-27 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d684edb-2c76-3821-86d9-86fea01b2eef | -6.79532 | -41.74939 | 2025-09-27 04:21:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3d1dde3-4be3-3be7-af2e-7af54feaf997 | -4.57276 | -44.07251 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0465aab8-b6b3-398f-bf11-856687383ef6 | -6.49276 | -43.28747 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acf5b711-1620-379b-81cf-56a407f1b96d | -7.56798 | -42.41854 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6b701a5e-eed7-3a53-be55-8f4fe3d1ca5e | -4.57832 | -44.08048 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c5a721e-8b13-3b37-aba9-05d47cceb93a | -2.85083 | -40.19042 | 2025-09-27 04:21:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fb40d339-7cd4-31df-b9bc-553cefc2a4e0 | -5.19322 | -43.72029 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a427c78e-53bb-33ed-931a-d28be336431f | -6.99235 | -42.39148 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c53d54bc-eadf-353b-be5b-6ae0b6bd5a15 | -7.61795 | -43.83582 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b947c99c-b7a6-38c7-b818-ef5136767642 | -6.54954 | -43.84101 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ab14607-d5a8-3f46-bc3f-2eb87d2a4164 | -3.80567 | -41.56662 | 2025-09-27 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ae303bd-e4ef-3d3b-9d73-b05a06a97d31 | -6.53723 | -43.8319 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33f451c-2985-3967-8985-38b3588cda4b | -3.70132 | -49.01444 | 2025-09-27 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14312220-39fd-3a61-b202-c08f7056bb7f | -6.69999 | -44.58859 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70e1981c-3e3b-3e74-bc89-4846fc68951f | -7.62469 | -43.83685 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b658172-63a7-3015-a1ab-3e89e612d129 | -5.14549 | -37.73817 | 2025-09-27 04:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d3ae07a4-0ac7-3343-b7ff-613a9430c763 | -5.49066 | -43.06844 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 640b5752-13a0-396c-bb18-34c033361ce8 | -5.78449 | -43.82693 | 2025-09-27 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9544209c-a6a0-33f8-b031-83cd410ca871 | -6.13316 | -43.46447 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e1f419e-b196-38d6-a00d-fe9dc4cb9db5 | -5.4743 | -43.0844 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 181c2d9b-7238-34e2-ac2f-d62d74e7e834 | -5.47541 | -43.0772 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e88b4b15-4708-3390-b2c7-24100dcb6aeb | -4.62302 | -47.41463 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e1673a-171e-3c1d-b53b-5458891f4ec7 | -4.80684 | -43.02689 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb0c4b4e-28e1-31bd-b6d1-d06265d4f0c5 | -6.53388 | -43.83135 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0286ba9-d725-3717-8ebe-305299331c35 | -6.82478 | -44.09303 | 2025-09-27 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b672500d-2cf6-3381-bac6-3441c6e38ccb | -7.12236 | -42.17585 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9a8d2691-fbe1-30ea-9aec-6dfb6884cbb2 | -5.73333 | -42.64695 | 2025-09-27 04:21:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 607717fc-d51e-3b81-98d3-8dae34b6113d | -4.57996 | -44.07009 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
