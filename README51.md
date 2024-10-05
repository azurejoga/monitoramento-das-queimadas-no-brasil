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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9cbd189-48ce-3eea-bb1f-4a3ab50c3eb5 | -18.08834 | -42.59346 | 2024-10-05 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ae2cf9e1-f251-3b1f-aba2-3ee2353f9586 | -18.08762 | -42.59765 | 2024-10-05 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4077ab99-4222-3327-85fe-1842df381cd9 | -18.25308 | -42.94366 | 2024-10-05 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b2ddcd85-ec2d-3ab3-80bb-0e581f2d7e60 | -19.31065 | -42.40454 | 2024-10-05 03:51:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 62c5d880-6d30-3352-9a50-8701dc633d60 | -19.26825 | -42.86103 | 2024-10-05 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 122fb48d-e03c-3146-a314-dbf804bb20c1 | -19.26747 | -42.86552 | 2024-10-05 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 09f82b54-cb31-3fbb-92dd-1f8f2b35141a | -19.26392 | -42.8648 | 2024-10-05 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e66abd66-e81e-30c5-9717-6f05ff422654 | -19.26037 | -42.86406 | 2024-10-05 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0f96dedf-c474-3af6-8548-1438f0f1ced2 | -19.13159 | -42.7451 | 2024-10-05 03:51:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1e219cf8-d67e-3573-8e27-5fa095860cd3 | -19.13085 | -42.74928 | 2024-10-05 03:51:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a2aad347-96de-3cf5-a024-003ccedf73ff | -19.01868 | -43.16984 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f722dbec-6632-3426-871b-20c1cc7ca39c | -19.0179 | -43.17432 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0cc58fc-9420-3644-9cd6-57cb01f9420d | -19.0158 | -43.16486 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 61f11377-bac1-3cfd-8d02-1a815237b420 | -19.01505 | -43.16923 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2eba6f34-aeef-3ba3-b84e-b41ae1f71751 | -19.01428 | -43.17363 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8cec763-9534-3e4e-b025-1b4ad5165976 | -19.01351 | -43.17804 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e8dbcbe3-ec03-3385-a6ee-9208ac2c7514 | -19.01216 | -43.16431 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f614a260-d80e-3faf-83ee-3a5a3b3517f0 | -19.0114 | -43.16866 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab90914c-a9ec-3d02-8d55-bb45d213d268 | -19.01065 | -43.17302 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d003a38f-a4a9-3041-a32a-5610c534d46c | -19.00989 | -43.17739 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59873e3c-71ad-3018-839c-ca284509b270 | -19.00776 | -43.16812 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a62fec17-c53c-3403-a15e-939203554043 | -19.007 | -43.17248 | 2024-10-05 03:51:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eca59669-9d59-3d31-bb68-f67a0371f54e | -18.88482 | -41.97447 | 2024-10-05 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6afe313-e78f-3dfe-a26c-ce813dc34f92 | -18.85639 | -42.90042 | 2024-10-05 03:51:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fada480b-c742-3ca5-a899-f0f5460b697d | -18.84918 | -42.8993 | 2024-10-05 03:51:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7c0008ca-e4eb-3b14-b9e1-c96e451fb328 | -18.84698 | -42.90069 | 2024-10-05 03:51:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 448f3e44-4d47-3bc8-809b-4a36e6df5b01 | -19.50127 | -42.90315 | 2024-10-05 03:51:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db96a352-cc81-35f9-8ad4-8097276bb127 | -19.49699 | -42.90665 | 2024-10-05 03:51:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0cd42750-d063-3903-aa04-4f85f130cbd2 | -19.49416 | -42.90176 | 2024-10-05 03:51:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d7cab9d-45c6-3c74-90be-a577ef3f2b65 | -14.3235 | -42.34729 | 2024-10-05 03:51:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b261dfee-ccf7-3ddd-bd3e-512fc4a4cbc3 | -15.09013 | -43.13595 | 2024-10-05 03:51:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c611bae-75ce-3c3f-8951-e94437653c90 | -16.47771 | -43.81308 | 2024-10-05 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8689fce1-7eae-326c-9404-366dd12d87c6 | -16.47688 | -43.81771 | 2024-10-05 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8655d3e6-d8c0-33bd-8dd7-24e189e29f32 | -16.34919 | -43.6978 | 2024-10-05 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2b6765-5130-339e-a612-85b4013abafa | -16.17965 | -43.64948 | 2024-10-05 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6518025-d0cf-378b-86d0-b0dd31fb8415 | -16.05516 | -43.80389 | 2024-10-05 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e526e5c-93cb-38e5-81c3-740b2d13ca8b | -15.95725 | -43.36143 | 2024-10-05 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39f13418-0875-397e-9868-963a85548aae | -15.95637 | -43.36634 | 2024-10-05 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4addc755-eae3-314b-aebd-11f12f8a76f1 | -15.93125 | -43.93397 | 2024-10-05 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7bb542bd-73b2-39a8-9f69-adad4cd4e51e | -15.9296 | -43.93576 | 2024-10-05 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff29a335-ef0a-3006-8634-079818fbca27 | -15.75268 | -43.84326 | 2024-10-05 03:51:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4adf8da0-042d-3d5e-bd5e-99fd82dfdadc | -17.74177 | -43.82515 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b866087a-4cfb-3c45-a599-11cd7eb43aa1 | -17.74085 | -43.8302 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e61e1ea-d1b1-369e-84ee-537a09a7268d | -17.7034 | -43.80469 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 716b867b-326b-3ab0-b28b-8dee0b7735ab | -17.70263 | -43.80175 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d6175eb5-8eb3-303c-8c5e-dccb7b9b1549 | -17.70171 | -43.80674 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09bb4796-ce1f-3d01-9460-446e0f164f5c | -17.70049 | -43.79884 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a7bb0928-4212-38fe-a4f4-80fed04c6505 | -17.69961 | -43.80381 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 357d255b-5d42-3c61-814b-7e3527010b71 | -17.69289 | -43.79726 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b94674c-e1f8-30ac-892c-04f591373ddd | -17.68997 | -43.79153 | 2024-10-05 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f7c5d65-2f80-3112-849c-c521eb4da449 | -17.63883 | -44.32211 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95b00051-f406-3b3c-8447-41d3d083fbfd | -17.63591 | -44.31591 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a7ab336-140b-33a4-9e6b-5cccc4beea2c | -17.63491 | -44.32129 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37a80679-8c1f-33f5-bcc1-663ec0e8280d | -17.63099 | -44.32047 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c31963-39ee-352e-b04c-528c0f5bfdaa | -17.62031 | -44.31666 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e85ca80-6da3-3c0d-bee6-fdc32922a5e4 | -17.6203 | -43.26397 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 123c5d2c-12ba-37ff-89fd-49ae9295fba0 | -17.61913 | -44.31847 | 2024-10-05 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a829b0bc-589b-3c96-8b28-5f6e5ef96ce8 | -17.6175 | -43.25827 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8cdd1f24-20d3-31ce-befa-39c72d09bd21 | -17.61662 | -43.26315 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d3de75f1-8c88-3409-a7b9-c4b17b852d9b | -16.68322 | -43.8843 | 2024-10-05 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c739dc7-cbf5-3be8-a2b3-91bac35e666b | -19.45476 | -44.12487 | 2024-10-05 03:51:00 | NOAA-21 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5257b8dc-41d9-3661-b492-6ef03a23db7e | -18.5964 | -43.95231 | 2024-10-05 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb2e967f-375a-3fbd-ad6e-cadd4c6318c2 | -18.57869 | -43.83511 | 2024-10-05 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea72c1c-903c-33aa-ab07-ae12fef9a87d | -18.57803 | -43.83834 | 2024-10-05 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64c8d26f-8335-3041-9691-0912b9ddf8fe | -18.57712 | -43.8433 | 2024-10-05 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0f1f1fc-1081-35fc-aceb-688d72bad3d9 | -18.57694 | -43.845 | 2024-10-05 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 499b1ece-2858-3639-a289-a1679b88a8b4 | -18.34351 | -44.01112 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 89c96e22-f545-3b48-9808-3e74438ea0b1 | -18.34254 | -44.01643 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c7c769f1-c9bc-3462-8430-2795eb0add34 | -18.34167 | -43.99966 | 2024-10-05 03:51:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20965d4f-de5f-3ce4-8594-11f752209162 | -18.34072 | -44.00483 | 2024-10-05 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a5cf09b-9f5b-3f78-9c90-606587a0a558 | -18.32538 | -44.02359 | 2024-10-05 03:51:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fc54cd1-520e-32a7-9e73-764dbdf78768 | -18.32378 | -44.04241 | 2024-10-05 03:51:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2c870cf-7d75-31b6-8c60-4558910376c8 | -18.12607 | -43.94049 | 2024-10-05 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b2ee7e-df6f-3941-8085-97089e960e29 | -18.0968 | -43.95799 | 2024-10-05 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6339a59f-9c82-3962-8bd4-4587e9b8dd68 | -19.2412 | -43.36178 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85209edf-a739-3f32-bc33-949b02097b77 | -19.24042 | -43.36617 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e5b650e-3a45-3d8f-8d94-8936d84b13e4 | -19.23752 | -43.36123 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c48516e6-0563-3ccb-9250-b70a4c5fe096 | -19.23674 | -43.36562 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30d155f8-5c0f-309c-ba3c-398a05411a05 | -19.23596 | -43.37003 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| caad098f-975b-3ff8-a018-43e82b370052 | -19.23068 | -43.37842 | 2024-10-05 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91fbb612-04fc-3776-a288-e89f18011c30 | -18.95681 | -44.22041 | 2024-10-05 03:51:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0626223-37f6-3895-bc92-98da4e5bdeaf | -18.95298 | -44.21964 | 2024-10-05 03:51:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dffc08f-5264-3651-b146-b859132062dc | -18.8795 | -43.59403 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| e23b3abc-4877-3f11-a034-cfe71f5b5da8 | -18.87866 | -43.59872 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| a9674fb7-4904-33e3-83a8-4149342207dc | -18.87781 | -43.60344 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 26755d09-794a-3f8e-842d-b15f9bd72675 | -18.8767 | -43.5883 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 379eafe0-cf25-3b9c-a814-837e9816b7fd | -18.87586 | -43.59299 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 7ba145ba-100d-39b8-b9d4-69d72ed3253f | -18.87501 | -43.5977 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| b573b436-8212-38f1-8295-8d09db2e8b1f | -18.87415 | -43.6025 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 72d85baa-dcf6-3760-ac0b-8ed46b12b055 | -18.87307 | -43.5872 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1af6f9de-ee71-34b8-8ec5-53b722142a14 | -18.87222 | -43.59192 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c0139c83-b580-3180-bb8a-1440afe3f2fe | -18.86963 | -43.60629 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| d718734f-3a1a-319f-9d73-25fc05e6f07c | -18.86943 | -43.58611 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cdbcba9e-ae43-3b34-909f-be095e502eec | -18.86877 | -43.61108 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| af2568c3-0007-3193-9568-445d1391f57d | -18.86859 | -43.5908 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ae41bb14-dea4-33e2-913d-343adbbec9b8 | -18.86791 | -43.61582 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5f47bcc3-4b21-3c76-ad49-e95ed184aa50 | -18.86602 | -43.60506 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 9e61e5b9-622b-38bc-9d12-3644d11844be | -18.86579 | -43.58509 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 51f1f898-1370-3cf5-925c-cc73ad37120e | -18.86513 | -43.60999 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 8f72502b-8667-30c5-8454-d7da596fadb2 | -18.86425 | -43.61488 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README52.md)
