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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e997d8c-0a8a-336f-924a-dc1d939a378c | -6.18735 | -42.64117 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4d8384d5-bbbb-372d-9e04-efb398baa243 | -7.84694 | -44.93095 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ddd0c46-5a2a-3830-98a6-ab00552771cb | -6.18333 | -45.43409 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| b5dd0fa9-be2c-3377-bd7c-4231f0918586 | -6.20066 | -43.58082 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb7ec609-c179-3a75-a357-82f659dabd81 | -6.87453 | -45.54687 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b06ffaa7-c2a0-3006-9df3-bcfdb43c1ba3 | -7.32305 | -43.94147 | 2025-09-07 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cb9c20a-5324-3291-9cb8-fc42fb6c1bd9 | -7.01608 | -44.97091 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 526b7fca-69f3-352c-aec9-9779be329882 | -6.1993 | -43.59265 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c802ec92-67d1-386c-aff1-47199d1013ef | -7.28609 | -39.21536 | 2025-09-07 03:30:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2b7ee684-b3f9-3fa9-a745-a0a38aebcd58 | -8.02156 | -45.44999 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c6188453-4b60-331d-90c0-2266fcea8aa0 | -7.61344 | -44.6772 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28236d69-7788-37cc-9ac6-5b2b5f452990 | -8.43124 | -45.03297 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c461f555-c761-3cad-baa4-9335b4bebe1d | -4.17266 | -42.0251 | 2025-09-07 03:30:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fef9279e-4ba2-3a60-8c1f-df0992d14789 | -7.23235 | -43.85519 | 2025-09-07 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1a477b3-5032-3be7-8c28-a3e8442de94d | -8.15525 | -44.86101 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 825b892f-5458-3cfa-9d40-513d7ffe80ae | -6.54088 | -44.81776 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b2d10cce-e34b-3d0a-8b91-6c052725da05 | -8.11606 | -45.31662 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 281308cb-7748-35ba-9772-c866afd9424c | -7.02013 | -44.97353 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d98b8b7-dbbb-3354-b8bb-b6f5275b0dbd | -6.22597 | -43.30057 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0b33887-45aa-344c-bbff-33877649acfc | -6.22679 | -43.29602 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d27d08a-ddee-3524-be08-ca790605dbc7 | -6.20201 | -42.62621 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dddcd2b7-4f2d-321d-9928-843466e77fa8 | -6.31961 | -42.19533 | 2025-09-07 03:30:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b99506b8-d390-3569-ae30-564426c06b04 | -7.6127 | -44.67581 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49718527-7ab6-3d57-88f3-3f8d44e80667 | -7.97758 | -44.94942 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3374ca1a-02ad-39db-a5ea-663bed3a6941 | -7.97101 | -44.94854 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89ad42a6-8b4f-390c-adaa-5d0b686f3915 | -6.1347 | -44.25996 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d35aca44-bb85-335f-9cc7-347ff69010c8 | -6.8848 | -45.6072 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11e3da09-c1cd-394f-a6a8-77da74c906b6 | -6.88609 | -45.60049 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8708c65a-6c09-3e24-b1c1-4c1fcfb50739 | -7.80669 | -45.43779 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 377e9e4d-2bbd-3a9b-b3fc-3d620959b67c | -6.21895 | -42.46524 | 2025-09-07 03:30:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 699f6571-2f60-3fe1-9852-9e61c0666a8a | -6.89422 | -45.59521 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d84d131-2419-3337-b36b-488c6d1f9298 | -7.60892 | -44.66601 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df647ab3-c5aa-3d25-8b5b-b2d40e60c65f | -9.39509 | -40.30783 | 2025-09-07 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a07c2bcb-2816-3a8d-a20e-0a85fa2e81cb | -5.52067 | -37.62088 | 2025-09-07 03:30:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 711c34da-dba0-3b59-ad83-54187f23c41b | -6.8941 | -45.59409 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54f772d1-3af9-3052-b293-58a43dd80461 | -6.88219 | -45.54377 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e39759f7-26f9-38a3-b5a6-181ddb50b7bf | -8.0843 | -44.81041 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37f39c92-c2ee-30e0-b95f-ddc29acffdfe | -5.54944 | -43.05923 | 2025-09-07 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4460169-e12b-3cef-af01-f0f1ba568eee | -8.48401 | -45.17499 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7bcaade-752d-3875-84c9-68cf1198ec17 | -4.67931 | -41.01436 | 2025-09-07 03:30:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 679fabdc-cccc-3b64-b111-f41826648515 | -6.14758 | -43.18347 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8dac2eae-8498-3e99-99ca-c3327c1a16ad | -7.19432 | -44.72851 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c95e135a-9d95-3a49-a078-7fe4ce31d100 | -8.43882 | -45.02851 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6abadf8e-386d-34e7-8aaf-1cebe097a327 | -4.67871 | -41.01789 | 2025-09-07 03:30:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 155858f9-0bc0-3cbc-be63-802e9c0bddec | -7.81836 | -45.4281 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27d34929-f891-3e61-b15c-a89cd438427d | -6.22918 | -43.28259 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7f0ddfb8-3eb2-3ee9-9a08-ca8eb29392bb | -6.2454 | -43.50975 | 2025-09-07 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 959f40fd-6f90-3caa-9dde-40fac86fb7be | -6.88478 | -45.60606 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00dbe02c-6594-3c04-bf85-8ae83bcb59dd | -6.23792 | -43.27673 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d5f9678c-486a-3d19-bd2a-24a63d86cf78 | -7.61365 | -44.67066 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61e3f786-ec76-3ab1-abd0-d9810fcce2c4 | -6.19474 | -42.63337 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fb4459f5-fac2-3c26-9382-f34bd742271d | -6.15159 | -43.18367 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 587d8b9b-51a8-303d-abd1-4a1c9633cbef | -8.01707 | -45.49466 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bc297134-98b1-31ef-818f-0793ddd03a77 | -8.03846 | -44.04095 | 2025-09-07 03:30:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 936b9c23-520f-3856-ad12-ab2b3bb7c014 | -6.21966 | -42.46132 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fa502d2b-6a57-33eb-968a-0016e42088e7 | -7.74702 | -44.01329 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9d3df67-622e-3f52-b86d-852c16bd7c4e | -7.71224 | -44.71849 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8de3ec8-1020-30e1-ae63-2dabe15f8014 | -6.55647 | -42.94901 | 2025-09-07 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e76c432b-7c76-39cc-9f4e-bfc7911fd7ab | -7.33099 | -43.93871 | 2025-09-07 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cc857bc-7f38-3e4b-8656-2ced080fb013 | -8.01839 | -45.45048 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43d55b54-3898-3e98-a731-39e0c831e50d | -8.4468 | -40.60345 | 2025-09-07 03:30:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d6569f0-7b93-31a4-8c08-bf98cccb9ed7 | -6.23281 | -43.29725 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53cf8b58-5b8d-3054-a24e-d75f9bf918b2 | -8.03936 | -44.03622 | 2025-09-07 03:30:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9203e40-5c38-39ce-b001-300bd6062023 | -6.15056 | -44.24563 | 2025-09-07 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c75f61d0-98ff-3799-9f28-d46587786335 | -6.24401 | -43.2775 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| af1eea8e-75d3-37c1-b6d1-9bd1ad1bb6eb | -7.71899 | -44.72136 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0c8c267-f30c-3737-a378-35b3eb01dc26 | -7.20079 | -44.72984 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1bfd1b3a-a414-32f9-9027-c91640e863b8 | -6.16428 | -44.24306 | 2025-09-07 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1964376f-0fa7-33e3-8119-7a68c28b5af5 | -6.21219 | -42.63627 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82fd36e5-4329-3a0b-9114-ee4daeeffc16 | -5.5536 | -43.05988 | 2025-09-07 03:30:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41caa4ee-6293-3330-afc8-608178aa4f7a | -6.19843 | -43.59757 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d18afb-85d4-35e7-861e-8e5391164e4e | -6.19552 | -42.62906 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5152f668-ccd5-304c-b754-a66eccbc02b9 | -6.22786 | -43.57114 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe9bd4b2-942d-3024-812f-33eb5c0d267b | -7.34748 | -44.3116 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6525454-6d96-34b7-8fc0-cf1db1630ae3 | -8.12024 | -45.31794 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e985778-116f-35b5-8470-ac11688750df | -7.01471 | -44.96612 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19c2fc98-3d92-33c3-b2de-9c2cc556e50b | -7.71784 | -44.72734 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7466ac15-6305-35b9-8d0e-19d0a20ff4ac | -8.12279 | -45.31732 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da458677-2a2d-3c9e-a01d-c343ca98acc7 | -6.19717 | -43.59974 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2297bc2e-0103-321a-aaf1-8fa3d8c7de3d | -8.15347 | -44.87033 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 541208ef-c4f7-3b5a-b43a-7a57d3fa97a1 | -6.19898 | -43.58993 | 2025-09-07 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34b273b2-d3a0-37d9-a41f-8db28a3f64ef | -8.68866 | -45.30492 | 2025-09-07 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72ee3be6-7bb8-3914-8dbf-52a00050bf5a | -5.75739 | -43.13299 | 2025-09-07 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c290415b-211f-3bf1-97ac-07f46f03f3f5 | -7.60799 | -44.67088 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23168c25-ac6f-3c10-b097-74aa85c3a1a2 | -8.02672 | -44.13544 | 2025-09-07 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cce0af8-06a2-30d1-8bff-f01f6ae0194a | -7.81158 | -45.42727 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b6750a8-b6c9-3835-bb3f-ee4e2e4efc4f | -9.39597 | -40.30276 | 2025-09-07 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c15b6b1-0eb3-304d-a7d9-1ed0d2872d6d | -7.24919 | -41.88876 | 2025-09-07 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dab2c65d-481c-374e-be77-8461b028c75b | -6.23695 | -43.27394 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 321163ae-8180-3abb-9b1a-5cad9f4f1a44 | -6.20278 | -42.62191 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b18e0e05-1d31-3232-9d90-6693ea33b5ea | -6.31895 | -42.19907 | 2025-09-07 03:30:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db4a26ab-a95f-36e3-a526-1ebf959e27b8 | -13.82752 | -46.28189 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f1478268-32a5-3633-af0f-5c8672f07648 | -13.84287 | -46.24923 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfd14d60-e020-3ba6-86de-c3a9592ff9f5 | -13.91288 | -48.02067 | 2025-09-07 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1067704-b4e3-3c5d-8f38-1bdfe2af77ae | -13.72402 | -46.90266 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7470dd28-607b-39db-b301-f2f9e62597dd | -11.58706 | -47.17611 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| cd6176b3-0685-34c1-9526-a40d5bb3de12 | -14.56599 | -43.7287 | 2025-09-07 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c82609a-b755-3bcf-b284-eea918d292b0 | -11.60236 | -47.17228 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 041b0b65-260e-3b65-ad35-f0c9cf8be56b | -16.28174 | -45.68003 | 2025-09-07 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d71f144-63fb-3cee-a718-f41028899e9d | -15.7354 | -47.02806 | 2025-09-07 03:32:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README19.md)
