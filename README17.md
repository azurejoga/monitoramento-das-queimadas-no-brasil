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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea9701ff-537d-3112-9317-fa659fb5f1d1 | -6.93689 | -41.70871 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a060f0a9-e6c1-384a-9797-076bbde2805a | -9.30888 | -40.24563 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f943ef78-0ba3-3370-9c57-45e256e5f2a3 | -6.31954 | -40.1502 | 2026-09-17 03:36:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91d5a29f-5cde-3eb4-8288-fbcde65676cd | -7.3777 | -38.98081 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7198a62c-7180-38a7-86b4-b4cf466f55a0 | -11.35642 | -44.0309 | 2026-09-17 03:36:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ba0b5a6-6f2a-3d2e-99f0-86940048d495 | -11.35107 | -44.02398 | 2026-09-17 03:36:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d17dcf-4e5a-3ed4-ab77-9994129a08c2 | -7.03554 | -42.03101 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45cb2f41-98c4-3164-9a2d-04f15a54a63e | -7.08574 | -42.09403 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b66d247d-9f10-3547-b146-674174398450 | -7.02775 | -42.07364 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3f132ddb-f494-3716-ade0-8506788707c5 | -8.48633 | -44.70229 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bcf69ce8-6b34-3b74-ac35-8e09c21e4696 | -9.61821 | -45.35606 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a8189c48-d664-3a00-8d2c-11fe68134e26 | -8.907 | -43.88486 | 2026-09-17 03:36:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08b93447-b870-3783-b9d1-97029b53eb29 | -7.10219 | -43.10873 | 2026-09-17 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 72b59c82-f8d4-3922-8990-284ac8cb3c89 | -7.3637 | -44.484 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35631df0-983a-3ac4-8558-58800fed7f8b | -5.28927 | -43.63868 | 2026-09-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f493037-86ba-3087-8dc0-569cf3950bd9 | -7.04383 | -42.05564 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0a932cf1-e3d9-32e4-9f76-fea95f1ba84a | -7.14316 | -42.09525 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 72b47114-b791-3ba5-b506-261361eb98ce | -7.13602 | -42.16965 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 502f2f5f-db5a-32d5-ba0d-a611c08b3bc0 | -7.46019 | -42.10611 | 2026-09-17 03:36:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c3f4022-fffa-3667-85e9-ce23d4d6c447 | -7.08932 | -41.83986 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ba6953c-2225-3d15-862f-e558ea996a04 | -7.07864 | -42.09771 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| acbed57d-a361-3168-8552-df77043d4690 | -7.13693 | -42.16467 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 87ce86af-9196-32c9-a140-3ef32d34c7b8 | -7.04467 | -42.05098 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 93d3272b-99d9-3d98-b688-5989630e8643 | -8.46381 | -44.55536 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2e274e4-162b-3490-8c07-2c9fcd911c83 | -7.09384 | -41.84661 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0e004e3f-0ce0-3c20-bd1f-532759c74d09 | -8.61429 | -44.50471 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 530911d3-640c-31a6-8a8a-66444c2ac1d3 | -7.10492 | -41.82324 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21771545-5690-3965-91e5-da6598b8a0bc | -7.12452 | -42.16223 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 59bfbe4e-41b8-3699-bfd7-a2e57d11ab00 | -11.26968 | -43.46001 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1b2bd1e-b6b9-3c02-b413-2f599e91f912 | -7.72573 | -42.50006 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0b341b6f-879e-3422-8091-f7de83956e68 | -7.64917 | -44.33387 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 834a1a77-4574-383c-8f81-2affdbfbb054 | -11.21075 | -42.83054 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| cc0ddb94-dd3a-349f-9c7e-167e571a430c | -8.46697 | -44.56158 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3fba023-0dbd-3ad8-816f-c1d0772bbcb1 | -7.46115 | -42.11042 | 2026-09-17 03:36:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 657dcccd-a3f6-34db-8c91-c269400c19ad | -7.18974 | -41.80708 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9527b44-95f8-3e5c-9167-e4ec18054f4e | -6.31399 | -40.1492 | 2026-09-17 03:36:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b04dad7-d769-30cf-b46d-92960d554219 | -11.20565 | -42.82462 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bfa04168-0a2d-37c3-9520-d887b99d0084 | -7.75455 | -35.25698 | 2026-09-17 03:36:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 59520515-5eca-33d9-a45c-340f065564ca | -11.43748 | -41.43272 | 2026-09-17 03:36:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3bddc86d-91d3-316d-abf2-acd828ab5c02 | -9.30828 | -40.24896 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b1850be5-b133-34b7-8564-9f48067c16c2 | -9.61643 | -45.3713 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a0a4e076-2bde-313e-9755-328b1fa68515 | -8.57606 | -44.58658 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9de0f423-a337-362e-a6c6-1b939d8767bd | -11.21169 | -42.82582 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a841bf8b-9cbd-3941-91a8-41c71069c98c | -9.61085 | -45.36208 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8afe9e54-7414-3567-aedd-158d9c69afc4 | -8.48503 | -44.70902 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36da0f4c-1a4b-3dfd-9fb6-d9d6be3f8dc0 | -7.81507 | -44.85102 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45193541-5217-36c4-85ee-66eb80505e6f | -7.14933 | -42.09649 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 581b8d5e-c38c-3000-9f05-a4e1e7a40cca | -11.26661 | -43.45506 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86a190fe-0749-3ae5-a6e7-1ee4e1fe11ea | -7.37263 | -38.9801 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0e58f902-c12a-3149-bd99-c0563f1ff4b1 | -7.45927 | -42.11096 | 2026-09-17 03:36:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df363c94-c08f-3072-9902-a5a0e2475fc9 | -8.39244 | -42.2086 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 41673c33-d147-3752-b0cb-b9c084d09e48 | -7.18852 | -41.81134 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8715924f-5e0f-3688-aed4-8d4b19b85156 | -9.96727 | -45.32854 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0a3d38aa-5098-3764-891c-82791c69a760 | -7.64783 | -44.34083 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7c9a400-8367-354e-94b8-03a35c76f8a4 | -6.67342 | -43.65031 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3177033-0ce1-3aa5-8eac-7398349cddef | -10.54056 | -44.85464 | 2026-09-17 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31d4f648-28ce-3487-aa2d-666319c83f02 | -9.46927 | -45.45558 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e4887364-8243-37b2-817d-60be3af44448 | -11.2708 | -43.46646 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7f6bf32-38e8-32c0-8ff5-dd68b1c99d23 | -7.08253 | -41.8396 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28a3e6d8-4fa9-33df-b4ba-5870031af132 | -11.21266 | -42.82099 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0713d00-60df-3d42-bb3b-079b1e81b3fe | -7.12776 | -42.16758 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ffa1cbb-be1a-38c4-afba-5fb2d5bba71c | -8.38545 | -42.21214 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ecf25fcf-660f-3ecb-8197-63b2c1e3a2b9 | -7.03256 | -42.07011 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a653dfe-6dc2-38e6-9be2-b35d218dc05e | -7.81369 | -44.858 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8df9370d-59c2-3aa1-bf16-a8e2b5dd6343 | -9.30948 | -40.24232 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c79f1b6b-c69e-3bc8-927b-704545452a38 | -8.61066 | -44.49493 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a337b049-71d6-3706-aa18-331b9d44c02c | -9.61978 | -45.35509 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7e0ba77f-6dfb-3ab1-bc2b-e3089dbd66f1 | -9.95753 | -45.3265 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 04bcdf85-11b7-3c18-b409-3b6396242dde | -7.13397 | -42.1688 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 295db284-6b6f-380b-be60-c436fc699d80 | -8.39188 | -42.21083 | 2026-09-17 03:36:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fa006030-1756-3f0c-ae2e-e15f5de0ff08 | -9.94887 | -45.3098 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2ad9e4f-d90c-3ad9-9cf5-773561c2c08a | -7.37211 | -38.98307 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7644e55a-e523-33e4-be74-c1e1ed429336 | -6.94536 | -41.6968 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 42dca125-004f-3d82-8ea2-74396cc3318e | -7.12683 | -42.17249 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c2f4af7-da39-3623-8502-c0f5dac91c80 | -7.09545 | -41.84084 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8759bec0-b6a4-35f7-bffd-3e9215e1f95a | -7.969 | -44.83741 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c0aa8b1a-9fd6-3d8b-9da7-8af29e4847e2 | -8.2593 | -42.18072 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c00e427-9337-36d4-b4d6-e9984e690e44 | -7.02478 | -44.62502 | 2026-09-17 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c054a80-c814-314c-94fe-9b61867fe8bb | -9.49666 | -45.43756 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee4a8a32-2128-3db3-8ed6-b0d43fffc714 | -11.28231 | -43.47409 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a34bbec4-e233-347b-ba60-a2b2dcf31d8c | -10.54135 | -44.85624 | 2026-09-17 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29c0510a-c0db-387c-8653-6bdff294f24a | -9.6237 | -45.37236 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9cf8e2d0-185b-3736-aa6b-b6a520bf2354 | -9.46192 | -45.45469 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9f7f40a5-7ff9-3290-8c64-080cc62e61a7 | -6.76475 | -42.77816 | 2026-09-17 03:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 36e0a5cb-6003-31a4-8b96-a40f43039b7d | -11.19961 | -42.82339 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d35eff65-7ad4-39b0-a323-09753c217c81 | -6.31809 | -40.14879 | 2026-09-17 03:36:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d755275a-0c24-3811-82e5-23e425569321 | -6.13076 | -43.74531 | 2026-09-17 03:36:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc437b43-8e22-3a48-8bb5-8ece8917cbec | -6.93088 | -41.70733 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ceed169c-da3e-3d75-a182-05b6e263a26a | -8.60947 | -44.50106 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 61899da5-33be-31fa-9784-fce36a055968 | -8.57893 | -44.58348 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e7f081cb-595f-3426-8096-f793c6636434 | -7.12871 | -42.16258 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bbe0ce98-63df-39f5-81f4-116e50cc7789 | -7.13512 | -42.17463 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cedcb4a3-6367-352f-9e66-b8c8b9d9d7d0 | -7.09458 | -41.84562 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a67dbc94-eec8-3f8e-af4a-4280c1b80662 | -8.26812 | -42.16751 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 08e0f5aa-a12e-3350-87fe-dbd767a7220c | -8.26631 | -42.17709 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86e8f0bb-d0ac-32d6-a1f0-76de224eec74 | -8.58163 | -44.56966 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 48d0d396-79a0-386c-aa09-25c247ef4229 | -10.11504 | -45.57146 | 2026-09-17 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42d559fd-be6a-3e0f-b51a-c97456571aed | -9.31267 | -40.24243 | 2026-09-17 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bdd41ffb-c38f-3bcc-9531-c9567bdf73fb | -9.61415 | -45.34614 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e25d70c-3983-3204-b62f-1423b1905b63 | -9.61256 | -45.34695 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README18.md)
