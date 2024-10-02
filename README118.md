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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e96d18b-30d0-318b-98f2-6c83e245aa2f | -20.6973 | -41.98255 | 2024-10-02 04:51:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9bf8af1e-91c0-3008-b24f-cf4d7818f294 | -20.69441 | -41.9794 | 2024-10-02 04:51:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1ad3c3b8-0f17-35e0-9bd0-68d219e3eb39 | -20.69408 | -41.98311 | 2024-10-02 04:51:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 86b8f333-7530-3cdf-a169-87e86f298f94 | -19.73871 | -41.6418 | 2024-10-02 04:51:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 80af4c9d-5f9f-31fa-a758-bcfd84b12a9b | -19.7382 | -41.64758 | 2024-10-02 04:51:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c5d4518a-268f-3573-aa67-19adbf61ccfc | -21.52242 | -42.06091 | 2024-10-02 04:51:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6cb94ed7-2e9e-33bb-9652-ecca6dcb3e6f | -21.51895 | -42.05969 | 2024-10-02 04:51:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 909a4d8b-96a0-3772-9c28-b31a6c97895c | -19.50357 | -42.33235 | 2024-10-02 04:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 883f580b-662b-39e5-8136-45b5954e9b7b | -19.50326 | -42.33213 | 2024-10-02 04:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e1f61974-f04d-35d5-a27c-533936dc08e4 | -19.50215 | -42.34384 | 2024-10-02 04:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c42c8200-916f-33cd-90c4-99aada90c5f8 | -19.5017 | -42.34855 | 2024-10-02 04:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b3342fb3-c040-3668-807f-fe055d44ca57 | -20.8146 | -42.29354 | 2024-10-02 04:51:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| af8ac736-12fd-3a70-a9ad-7f4bae18acb7 | -20.8142 | -42.29829 | 2024-10-02 04:51:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 98ee3a5f-b13d-3c68-bd08-d6defe26d9a9 | -20.80797 | -42.29775 | 2024-10-02 04:51:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 78737b2c-8630-3315-9782-acce74c66765 | -20.40862 | -42.91043 | 2024-10-02 04:51:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bef76d83-8c68-3202-9639-9c107d86bbdc | -20.35268 | -42.75804 | 2024-10-02 04:51:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1ac31d5c-0ae5-388c-be07-0d641b362a10 | -20.35227 | -42.76259 | 2024-10-02 04:51:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b6724231-e14c-3acc-8043-85b3f8243df5 | -20.33848 | -42.14926 | 2024-10-02 04:51:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4bf44827-0140-3d35-b2c3-65a3cc9880af | -19.89516 | -42.32245 | 2024-10-02 04:51:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1b451b09-daa2-3562-86db-9713f30cb4fc | -19.87397 | -42.35121 | 2024-10-02 04:51:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d18c3679-63cf-3bb7-9c41-d5649ec91c5c | -19.78664 | -43.17168 | 2024-10-02 04:51:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ace42119-f2ea-32cf-b413-4bcb0df919bf | -19.78624 | -43.17595 | 2024-10-02 04:51:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| decbff8f-d0cc-3131-a28c-ca7b0fb1dd70 | -19.50874 | -42.87825 | 2024-10-02 04:51:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6d1f8879-eed9-3ad1-ab89-db1b123c8fdf | -19.44446 | -43.05799 | 2024-10-02 04:51:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d344714-5188-3d15-acff-3958be0b268d | -22.34715 | -43.36021 | 2024-10-02 04:51:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5f809380-5d74-3156-8891-d331535c9ab9 | -21.62024 | -42.80371 | 2024-10-02 04:51:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6454427a-258a-3300-a12f-1cc14e6ade22 | -21.61992 | -42.80742 | 2024-10-02 04:51:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| bbe8ac62-bb4f-3ac4-8c71-dd42d09785bc | -21.61431 | -42.80115 | 2024-10-02 04:51:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 7711b72d-2006-36b1-977a-5d127a790e64 | -21.61394 | -42.80553 | 2024-10-02 04:51:00 | NOAA-21 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 1d7e0e8c-5dc5-3c41-9d2d-0f70662cd178 | -22.66877 | -43.70527 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a04fba29-c0bd-38cf-b908-ee52fc2ec8c8 | -22.66853 | -43.70863 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a3757d37-27d4-32c7-9fe2-7f4a3dbe0c19 | -22.66847 | -43.70879 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 766aed29-bf48-356b-9ba0-e8c3937954fc | -22.61646 | -43.96267 | 2024-10-02 04:51:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aa50da5c-59a7-324b-b3c9-6ec6d4306da3 | -22.61606 | -43.96711 | 2024-10-02 04:51:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 44ec9b3e-4d0b-32d3-8e74-53d88b03fd4d | -22.61071 | -43.96231 | 2024-10-02 04:51:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2a740569-ceda-370a-8981-3a93812ff8e8 | -22.61031 | -43.9667 | 2024-10-02 04:51:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a094992a-c3af-3d8e-8f54-68bbda1287db | -22.51634 | -43.83691 | 2024-10-02 04:51:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b3734f5a-c5cc-393c-bd12-7d4bd01c6dec | -22.38515 | -43.52145 | 2024-10-02 04:51:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5d87287a-770f-336a-b212-54f0996301e9 | -22.38481 | -43.52541 | 2024-10-02 04:51:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 66d44cbf-1fb9-3b62-b1e1-cdf1f97b71fb | -19.29683 | -44.42397 | 2024-10-02 04:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 894332bb-25eb-3c39-ab18-648eadc3a61d | -19.26166 | -43.76431 | 2024-10-02 04:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 303d09c2-120f-35b4-8c92-bf3abfe67331 | -19.25061 | -43.36209 | 2024-10-02 04:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d68ba385-b861-30d5-9cce-68b71c6730fe | -19.25017 | -43.3667 | 2024-10-02 04:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c3880c1-fe2c-35fc-95da-e18009383366 | -20.2121 | -44.74352 | 2024-10-02 04:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 298e2ea8-e0ef-374f-869b-e8dd04992c9a | -20.21175 | -44.74691 | 2024-10-02 04:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e3652171-bda0-3266-967c-b21abe5ccdd6 | -19.79569 | -43.64817 | 2024-10-02 04:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5f73d70-3bda-3797-a2d3-4660b12decfb | -19.61796 | -44.10582 | 2024-10-02 04:51:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7cfdceb-4edc-3232-88d4-28d50ba021ab | -19.61247 | -44.10525 | 2024-10-02 04:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc0af24c-37e4-319e-a29d-87bc788e087a | -20.30074 | -44.04068 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a0bb7974-5ba6-3b50-bd88-8113d14ffbb1 | -20.29588 | -44.0332 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c5121b2-db05-3e31-81d5-930678d83c21 | -20.29564 | -44.03067 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac613af2-7d2b-3da6-834d-7303d4146913 | -20.29553 | -44.03666 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d98650d6-346c-34af-810a-ce8bb61f1583 | -20.29531 | -44.03419 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89262fbb-600c-3a69-a707-8200820b0da8 | -20.29498 | -44.03767 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7871886f-881b-327f-b706-56c1320492ef | -20.23094 | -44.23652 | 2024-10-02 04:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a1be972-cfb0-35ca-ac90-6ec81e51f71d | -20.02171 | -44.52852 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4517c501-5c47-37a7-9846-972f590e6a6c | -20.01714 | -44.52024 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1b48eafe-b8d6-3a5f-826d-f2005fa170f5 | -20.01597 | -44.5316 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a955321f-75cd-355e-bb7c-f32442bb18ca | -20.0121 | -44.51645 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6f464e0b-fd3e-34a1-af5c-c7ab4102b4ec | -20.01171 | -44.52027 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 04a9ddc2-c96f-3f09-842b-186a6a0a3a7d | -20.01133 | -44.52394 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e694dfd8-dfec-3cf8-9540-7dd623d7a61e | -20.0095 | -44.54169 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| da44db71-b668-3b43-94ff-bb72ecb8ace1 | -20.0063 | -44.52005 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1748b073-9c01-343f-aef9-7848c06ea8b7 | -20.00059 | -44.52283 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e08f77b-78dc-3bfd-acb6-8a52cbe24b5f | -20.00024 | -44.52629 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e8511420-989a-399b-a363-527f4f9247d7 | -19.99988 | -44.52978 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4c6c2b16-e32f-345f-ba49-0b408017212b | -19.99952 | -44.53331 | 2024-10-02 04:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 339c48bd-e675-3a75-bfa8-0df41b2adb1c | -22.35797 | -44.22589 | 2024-10-02 04:51:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ae1b73bf-243f-3358-98d9-ffe5db7ba079 | -22.3576 | -44.22989 | 2024-10-02 04:51:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 826339d7-a038-3814-b303-c1a3cfd3dad7 | -22.35235 | -44.2253 | 2024-10-02 04:51:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 722f5736-6071-371d-af7c-a531d02a4e48 | -22.35199 | -44.22929 | 2024-10-02 04:51:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b5c4b913-8aa5-35d1-9b96-ab9e287d8149 | -21.88556 | -45.34441 | 2024-10-02 04:51:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0de46814-7ccb-378f-b101-1f5ca5a74edf | -21.67614 | -43.95598 | 2024-10-02 04:51:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0f21250c-f591-3775-ab85-ca6724925330 | -21.67372 | -43.94905 | 2024-10-02 04:51:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2c6a57ff-3bb3-370a-8488-7ef5cbb5620f | -21.67336 | -43.95316 | 2024-10-02 04:51:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 34bcd968-ea39-3a62-9a51-f8fac66fc0e1 | -21.67082 | -43.95168 | 2024-10-02 04:51:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fbe03911-f9c8-39b6-b038-8c00971845cb | -21.48171 | -44.58425 | 2024-10-02 04:51:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14161aed-291d-3e31-a7ef-2ba4d950958b | -21.47624 | -44.58392 | 2024-10-02 04:51:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 394fe293-2c02-3370-8865-00b94990dfab | -21.46563 | -44.58001 | 2024-10-02 04:51:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ede65621-fb2e-364f-a713-0b981afa8f73 | -21.46528 | -44.58363 | 2024-10-02 04:51:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1aec0055-ed04-3b7e-af33-30a8e669d555 | -21.1969 | -44.93723 | 2024-10-02 04:51:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b1aab353-814d-3fb7-87b5-c564000430b8 | -22.49376 | -44.1496 | 2024-10-02 04:51:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee999b25-2ce0-35ed-97be-e13a0d3e7673 | -22.4881 | -44.14911 | 2024-10-02 04:51:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5ffb9e8e-1b77-3de9-8422-e8d6c97c639c | -23.29231 | -45.29509 | 2024-10-02 04:51:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d2f6b8a-5b34-343d-95a4-5320aed2e037 | -23.28708 | -45.29358 | 2024-10-02 04:51:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| befcfb7e-6920-3d5a-87b0-c9a1bd618926 | -23.20772 | -45.57147 | 2024-10-02 04:51:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99f1386b-898c-3b29-b748-bc764c4638ae | -22.90794 | -45.09534 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| dafd9d59-781c-3ac0-b663-4436242df558 | -22.90762 | -45.09879 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 89e7be5d-e701-30f5-b3c4-4d4b3cac07ca | -22.90732 | -45.10199 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 196d840a-7ddc-3470-8b93-13d0374e0fea | -22.90258 | -45.09481 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2831edbc-065a-3910-85d4-6986e911c19c | -22.90227 | -45.09814 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 40e19087-dd0d-3f77-9d42-75937129541d | -22.90199 | -45.10116 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9128b4b3-0b86-382a-a779-e5fdde8b8fa0 | -22.9017 | -45.10416 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 524f727a-4c3b-3a5c-8af5-f9eceed1e669 | -22.90052 | -45.1166 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| db867d85-ab77-35a8-8167-3edbce441d09 | -22.89726 | -45.09388 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 84e4d73e-b541-3d34-bcdc-689941de0ffc | -22.89695 | -45.09719 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| c494ad68-05f3-30d1-9acd-22e39ec29d3b | -22.89668 | -45.10007 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3b86623f-48fd-3c87-9931-098d1c5500d6 | -22.8964 | -45.10296 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 32f69459-2416-397a-ad70-5c6c7365c3a3 | -22.89612 | -45.10594 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| b41d9606-7018-3a75-a0e6-3f1399041926 | -22.89524 | -45.11531 | 2024-10-02 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README119.md)
