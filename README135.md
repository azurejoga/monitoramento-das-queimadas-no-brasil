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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b9d5561-45b8-3101-99c0-912669a4eab3 | -21.797 | -48.45019 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8530736-a527-36b6-a009-10f7dd5a467a | -21.79344 | -48.44963 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95f4b184-4294-3b89-bfb1-d87aa9642090 | -21.76008 | -48.50554 | 2024-10-04 04:36:00 | NPP-375D | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a1f582d-da48-3199-9067-b34cfb3148c6 | -22.39395 | -47.89377 | 2024-10-04 04:36:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9cdb165-03c3-39f4-959e-8203aa6bd0c8 | -22.39027 | -47.89315 | 2024-10-04 04:36:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8980f779-c5f5-3ad5-96ab-47a3489598b0 | -22.38964 | -47.89782 | 2024-10-04 04:36:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37d0f5c7-d9d9-3ef3-8882-680fe8cb777f | -19.20502 | -48.38697 | 2024-10-04 04:36:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fa21f26-1339-3a69-951c-403d74be270c | -19.9204 | -48.33693 | 2024-10-04 04:36:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6146b207-dbf6-3f5f-aad0-bc1e567c5f3e | -19.53861 | -48.64471 | 2024-10-04 04:36:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8180062a-66d0-368a-9d25-18382c4a583d | -19.53804 | -48.64869 | 2024-10-04 04:36:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 475fe0da-eb15-331d-adec-22c54ffac80d | -19.53515 | -48.64415 | 2024-10-04 04:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c0ba16d-4199-3b93-8e63-80fd00025150 | -20.6644 | -49.54144 | 2024-10-04 04:36:00 | NPP-375D | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f431658-6217-3cc1-bad9-aa1e4ee27216 | -20.5726 | -49.62075 | 2024-10-04 04:36:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f353e68-f5cb-35ef-b205-c7949cb6ab4c | -22.3775 | -49.0422 | 2024-10-04 04:36:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c1388c2-95ef-38bd-a63a-c7bdbc6b0bae | -22.374 | -49.04161 | 2024-10-04 04:36:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d5272fb3-a5c5-37df-9833-21f5cfbf2177 | -22.37342 | -49.04575 | 2024-10-04 04:36:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f65a31c-3db7-33f6-8106-12692ca0ed4a | -22.36992 | -49.04516 | 2024-10-04 04:36:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dbe07cd8-e618-30a6-a5a6-71fc835fc426 | -22.34737 | -49.23103 | 2024-10-04 04:36:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a79df1-9394-3a15-9ceb-7faac70bb49a | -22.38674 | -49.25427 | 2024-10-04 04:36:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fad929f-dca7-33b6-aaf5-a2ab3336a9e1 | -22.28741 | -49.79572 | 2024-10-04 04:36:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b078ec4b-4917-38bb-83f6-7c9c17cd7e22 | -22.28478 | -50.0034 | 2024-10-04 04:36:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d4cae3b7-c93f-3139-973b-e2593fdd2a57 | -22.23776 | -49.70741 | 2024-10-04 04:36:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b16c4dbe-6085-3238-8549-f54cff4325be | -22.23433 | -49.70689 | 2024-10-04 04:36:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 450915aa-acb6-392a-a53a-bb0531213a04 | -21.40587 | -48.87612 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9981328-2744-389f-8e5f-5afdc877552c | -21.40238 | -48.87553 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c096fb3-eeb4-3259-adf5-72e4aa7a7691 | -21.40178 | -48.87964 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58e838bf-56bd-3da2-95b1-05144aa31761 | -21.3971 | -48.88734 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a85dafbf-c996-35c9-9362-e33228be2253 | -21.39361 | -48.88676 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8425440f-0a54-3e57-aabd-50f47d541021 | -21.35695 | -48.89342 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12656944-76c1-3f35-9124-a792a3883b38 | -21.35637 | -48.8975 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7223da30-4b80-30f9-a85e-e57e8db33325 | -21.35288 | -48.89695 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06b0c503-4a6a-398d-9090-5d38d46dba47 | -21.3523 | -48.90101 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6cfec308-2d2b-3802-bef1-d70bce4edf4d | -21.34881 | -48.90046 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfa06e60-1818-3dc4-a23c-67c4ce566466 | -21.34822 | -48.87955 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d01681ab-2c62-39a3-a267-e5230bd09f43 | -21.34764 | -48.88363 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8f142359-042a-3843-b51b-5d837838ff5a | -21.34591 | -48.89582 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd41a701-c5d2-3d02-b384-d5d05cf1ec69 | -21.34532 | -48.89991 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5d3c339b-ca92-3d80-8740-9a92868daf34 | -21.34415 | -48.88308 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 99059db4-0625-3201-bb64-01b9c577b221 | -21.34357 | -48.88714 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 06e29edb-53db-30b9-a992-593a4b8703ef | -21.34241 | -48.89528 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fa1183f4-2290-39ea-8971-2ca981febabd | -21.34183 | -48.89937 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 88973251-62c1-38bd-8318-38e0043b491b | -21.34125 | -48.90347 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3eaedc97-61d2-3ebe-8e8d-051a2a32f3be | -21.34066 | -48.88252 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f54b9727-3b98-3bce-b7b2-9cdda308eeee | -21.34008 | -48.88659 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af2428ea-52da-3dcb-91a4-cbf7de172c39 | -21.33834 | -48.89883 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e19cf80-f0d9-31fd-b250-9dc61acf8ebd | -21.33776 | -48.90292 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92096fd5-b224-32b4-8787-a0f894675b51 | -21.33195 | -48.89359 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61b7bdba-a7f3-3469-90d5-37187728857e | -21.33022 | -48.90582 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0db58c2-919c-38ae-b81f-c9bc601ce390 | -21.32964 | -48.90987 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7d3612b-6425-3367-b908-5f0cb2ee1698 | -21.32846 | -48.89301 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdb8ae9d-85be-3181-8c05-4708b1c156d1 | -21.32731 | -48.90117 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb8549ba-63e4-39a6-8d4f-31a2161ca003 | -21.32728 | -48.87617 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09ea6bc6-9259-3c90-aad1-3204a3a32d26 | -21.32673 | -48.90524 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bc7c6c8-bd84-3f29-a213-86fb2ec1b2bb | -21.3267 | -48.88028 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2937ae63-d1c4-3b32-9bba-f20235058647 | -21.32382 | -48.90059 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67fb8416-c6a0-325c-a63b-0bdd736e27d0 | -21.32263 | -48.88379 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c5e47ca-57d2-3771-941f-c6fd0f1355ea | -21.32034 | -48.90001 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc47a75d-736b-3aea-8e52-0de1c754d901 | -21.31977 | -48.90406 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a219951-a440-3ee2-b818-c8156bca2e91 | -21.57679 | -48.48344 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f625bed7-cdc7-372b-917b-4c7173494719 | -21.57618 | -48.48771 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76236a65-9521-302a-a9f6-0a3cc514bc7a | -21.57557 | -48.49198 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8017533-277e-3df4-aedc-de5c5f03b300 | -21.57324 | -48.48285 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fa13a0e-80e5-33ae-9408-fbd48000de74 | -21.57264 | -48.4871 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b5ee67-9295-3280-b2a3-341660b79413 | -21.57203 | -48.49138 | 2024-10-04 04:36:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4e7de04-afa3-3b54-893c-61c2ab3ee4ca | -21.55983 | -48.67754 | 2024-10-04 04:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 605ccc4b-5e63-389f-8103-0677af093de1 | -21.34941 | -48.84599 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d10cb05f-6a11-3364-9c6f-ec828876dd34 | -21.34706 | -48.86255 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7259222a-a505-34a7-b366-3a7d05b821e5 | -21.34357 | -48.86197 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72ac272a-0f1b-346a-9e86-86e6556b12c6 | -21.33252 | -48.86435 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d803cf6-efe5-35f9-919c-2710f2f8f065 | -21.33194 | -48.86848 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b396078-f1a3-3ed8-ac30-c1e821a6f9fa | -21.33135 | -48.87261 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa26f7bb-c80c-31df-be9f-1d85a2139b2d | -21.32786 | -48.87204 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1a54bc1-c407-37cc-8c3d-7ca7eb98b0cd | -21.32612 | -48.85907 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 875d56c0-fe03-3271-8a51-4b3d76829cb0 | -21.32554 | -48.86318 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 670e3382-2923-3d7f-812a-fad488c9c1bf | -21.32205 | -48.86261 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a2e6ac9-b4ae-33a7-a86f-fb01b76885db | -21.31856 | -48.86205 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80f94d58-894c-3c1e-afca-c98ab162c288 | -21.31391 | -48.86971 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dfd841c-f09b-320e-9e52-d8c6b3996cb5 | -21.31343 | -48.86689 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e1021e6-32dd-331b-ba02-d556af77c0d8 | -21.31284 | -48.87099 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7cb6ec2-4a85-30e6-b908-0f2367fae033 | -21.31042 | -48.86915 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c49f2fbe-5a2f-3a31-861f-c1c6ee7fe3d6 | -21.34299 | -48.81553 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 987c2183-66c1-32f3-9142-2877c2487de1 | -21.33716 | -48.80613 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 326f9e74-fe30-39b7-b26e-19658db2a0e9 | -21.33366 | -48.80558 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ad2cd1f5-a76f-3eef-900e-9e2f5137b525 | -21.33308 | -48.80971 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| adcdbd3d-de77-3e9e-9ed9-fb8608ebed15 | -21.33016 | -48.80503 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1dd7e077-0686-35dd-8338-52efbdb21c99 | -21.32958 | -48.80915 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cf37863b-3b7d-3161-b175-440e24e74a92 | -21.82303 | -48.77301 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f29f7e33-ddc4-304d-bc9a-3c8e7fd54240 | -21.81952 | -48.7724 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 027306d0-f259-3065-8223-9428a80e5a61 | -21.816 | -48.77183 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496e9d60-0300-377f-b152-bea9ea5765dc | -21.81189 | -48.77544 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19fcbd65-4ca1-3bfa-bce8-36db9d981905 | -21.81074 | -48.75809 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2c85cc4-3452-3992-a28f-b5b985901f32 | -21.80955 | -48.76652 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 136b13de-c5d8-3be5-be7d-215e08b3252f | -21.80836 | -48.77493 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f06c78fd-1594-343b-832c-4ca3d6bb2e1b | -21.80721 | -48.75755 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 242ab913-086e-3934-8b90-5a1f8977a909 | -21.80662 | -48.76175 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc81e574-6108-38d9-a726-1d1868b8ff02 | -21.80366 | -48.78277 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f049476-a7d7-3ca9-a6fc-6c0de4737d7e | -21.80014 | -48.7822 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 711085ba-fc6f-35b1-b75e-b24e01c10152 | -21.79897 | -48.76494 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5e525b9-b6cb-3b2d-8719-a6a3efb487ea | -21.79662 | -48.78164 | 2024-10-04 04:36:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 054f0e0e-c27b-3b48-a6ff-035c6bd4066c | -21.31628 | -48.90351 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README136.md)
