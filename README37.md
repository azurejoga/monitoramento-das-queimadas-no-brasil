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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63165048-eb57-38fa-b161-41618b472f6d | -6.68291 | -40.89108 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 959880a9-9ec9-3d84-ab99-2975b388dfb0 | -6.67851 | -40.89755 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39e442ec-6189-3c55-a5e4-1f6064b9bd78 | -6.6752 | -40.89703 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e36b1e3-1bb1-3361-aa8b-5054d8f4d9f3 | -6.67188 | -40.89652 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5567bb21-a723-3c76-b36e-a8c8c03ab401 | -6.67134 | -40.90001 | 2024-10-28 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a53193a7-e0fc-3259-9c47-26d3ea7a110f | -6.48676 | -42.01192 | 2024-10-28 04:06:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9bf68567-87a3-3471-b7de-0e27676d0984 | -8.8713 | -41.27546 | 2024-10-28 04:06:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c87a1ec6-ab16-3933-a2cd-7d3d21200b84 | -8.32056 | -41.23618 | 2024-10-28 04:06:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 714b53ef-96f4-3516-9cc2-3cdd589a0099 | -9.02572 | -41.89777 | 2024-10-28 04:06:00 | NOAA-20 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c182815f-a6e9-3f68-9847-bbce65c33b71 | -8.62735 | -41.42426 | 2024-10-28 04:06:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a4e9ea1-4f21-3357-a35b-2cca7c3e8881 | -8.28576 | -40.88824 | 2024-10-28 04:06:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1648854-c6fe-3a01-ad0b-cb3055a95ab3 | -8.87185 | -41.27194 | 2024-10-28 04:06:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5cc48d56-b60a-3529-b90d-5f9aa1cfc683 | -8.68548 | -41.2249 | 2024-10-28 04:06:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dece80d9-ba78-3d58-b0d7-b3bd88296c9f | -8.68494 | -41.22841 | 2024-10-28 04:06:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a674ba79-2f79-3b8e-9193-654fa169c2da | -9.77642 | -42.04864 | 2024-10-28 04:06:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4384d0b7-9c99-302c-b813-e22f3104b737 | -9.77311 | -42.04811 | 2024-10-28 04:06:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2912577c-f849-397c-8fd7-ec4180c91120 | -10.75811 | -41.41021 | 2024-10-28 04:06:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb9c34f4-5225-3484-b239-a0a2d2c310c0 | -4.95613 | -43.20012 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c312cc19-d73f-320f-82a1-abfd4c7ac44b | -4.95554 | -43.20386 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ae48bf9-7554-31f4-9329-e26626ff41aa | -4.9533 | -43.19585 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb63028-ab00-3ea9-b997-1e486f318f88 | -4.9527 | -43.19958 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7894d1e-bf92-37a4-b0c4-56a46adb8903 | -4.94928 | -43.19904 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7350c27-0241-3473-99be-95cdb141a76d | -4.94704 | -43.19103 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a27c8eec-fd9b-36af-add2-9716dacd98eb | -4.74555 | -43.09103 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1d4a184-cf15-3c30-ad15-96c3ee0cf401 | -4.62951 | -43.11443 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37abb36d-ba16-3c28-bc23-3c8a65ea4199 | -4.62668 | -43.11016 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56a59887-80cb-3f73-8294-225004c151c2 | -4.62326 | -43.10961 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78d976c4-ccef-3d85-99e7-eb74880a7648 | -4.73506 | -42.82951 | 2024-10-28 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 690ec649-5a29-319e-9613-699d3b942e03 | -4.73167 | -42.82898 | 2024-10-28 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acc9c577-46c5-3981-8e4d-6ac1ec661228 | -4.72828 | -42.82845 | 2024-10-28 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f17f7a1-b48a-32ac-b550-a8f21e82a3d4 | -4.69641 | -42.91331 | 2024-10-28 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 183eb205-d57a-3854-b690-32a20cc3233b | -4.54226 | -42.98016 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5f60e9e5-ceed-3973-8eba-4e06be67b543 | -4.54167 | -42.98385 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 202c0980-7541-3ba7-af65-fe2db8770bce | -6.5852 | -42.24855 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 079cf07a-24a7-3be8-9c05-7fe704e1fa3b | -6.52768 | -42.18204 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd33982d-66e9-32df-9474-ef286d966429 | -6.515 | -42.1978 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63b19663-2722-3961-934b-e99b17dfd6b1 | -6.51338 | -42.35855 | 2024-10-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 977c7032-fcdb-3649-8a79-4e3c3e76386f | -6.51282 | -42.36206 | 2024-10-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d19a993-e332-3a71-b57a-e649f78a29e9 | -6.51005 | -42.35802 | 2024-10-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2d1bb282-afd6-3524-8bf2-f382ce817516 | -6.5095 | -42.36154 | 2024-10-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20b94712-77c3-340d-9737-d3636632d74d | -6.50618 | -42.33947 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89c45ad4-099a-35fd-8d49-fab0b879e798 | -6.50563 | -42.34296 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac47c0b6-bccf-3367-be48-c76ec7abd255 | -6.50286 | -42.33894 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5390f3a-181f-3962-8a7d-70f9d2af7d25 | -6.48903 | -42.19015 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a35c2c7-00a1-3563-a5e9-4865d597e112 | -6.48848 | -42.19365 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dad15b3d-58a2-37ea-901d-3611d1422a92 | -6.48793 | -42.19715 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37baef48-32ed-3666-859c-07eaad73004e | -6.40625 | -42.21993 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e43e7d55-a58b-315a-94c8-989981814f8e | -6.40348 | -42.21593 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eafbe3f6-5d49-3029-b05f-99de24fdaadd | -6.40293 | -42.21941 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d33eb53a-e778-3a8f-bbc4-54e268cbd95e | -6.36976 | -42.21418 | 2024-10-28 04:06:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6288208b-691d-361a-868f-80a12020bdef | -6.31701 | -42.01026 | 2024-10-28 04:06:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0847d997-81ef-3ae6-8af1-bbdc7dce900d | -6.05903 | -42.58949 | 2024-10-28 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15595285-b12f-3de6-b6dc-ab57d48f8155 | -6.05171 | -42.84424 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b88a3159-63df-3d23-9f5f-5703752ebb89 | -6.0443 | -42.74025 | 2024-10-28 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9998af82-5833-3328-934c-9deefbb1f648 | -6.35839 | -42.96597 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d2e2d78-cc0a-376f-8f08-dd07fedfa5dc | -6.3432 | -42.97454 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d35de7-f667-39cf-af29-2115c2778112 | -6.34262 | -42.97813 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e84d0d48-fc99-3bb6-aaef-2f36f29f9667 | -6.21245 | -42.92872 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 435d0ca4-ba1e-381d-a729-6a9064a20571 | -5.68115 | -43.20623 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b780e01c-60c7-3c94-9953-4566e5510ada | -5.67834 | -43.20197 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcb709d3-ea18-3abd-b313-76bf2270ecd8 | -5.67213 | -43.19717 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0aa91aeb-5d06-3a9c-a016-3198796a9c29 | -6.19671 | -43.46933 | 2024-10-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d45c900-a71d-3470-bb78-a921a37a2eb6 | -6.0871 | -43.4523 | 2024-10-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2da489dc-42ba-3b88-a99c-73dacc8da880 | -5.78773 | -43.24204 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4dc5a5e-2489-3f5a-a0da-0d4a8e170ced | -5.68397 | -43.21049 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d79d8e5-0692-35be-9fd7-16e043c83bae | -5.62834 | -43.27332 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed0de0e4-a706-3a6c-8931-23437410e527 | -5.55611 | -43.22112 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53ef9aac-858f-3973-991c-f9b589557080 | -5.55551 | -43.22482 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36cdd9d6-346a-3db8-8e60-e29a5f3f003e | -5.5521 | -43.22428 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6df0ad73-1c1b-39cd-a6c3-623c048e9db6 | -5.43181 | -43.33878 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d19a1d1-fcdb-3072-885a-9544b61e1c92 | -5.43076 | -43.25824 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff3f98e8-2067-35ef-88de-b89625d54106 | -5.42838 | -43.33824 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 105ba583-fe22-306c-8fb1-030d98853b6c | -5.29339 | -43.21791 | 2024-10-28 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4486a2d3-c52a-30eb-b97d-4cd498559ea6 | -5.96865 | -42.12931 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6dca319b-4a58-3bbf-99a6-ad1b8f25ebce | -5.9681 | -42.13279 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd98c90d-4d2e-375b-ad99-644b16116e14 | -5.96478 | -42.13225 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6a07ffd-9f10-3f41-9965-e7d2671f01df | -5.91851 | -42.86695 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd5aca61-ca9f-3cf4-a91d-e144374c26d6 | -5.91573 | -42.86277 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02892e80-74bc-3223-9996-ede7c22e9346 | -5.91515 | -42.86639 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d03d797-621c-350b-97ac-3db1b07c4a4c | -5.89555 | -42.87083 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d3d994d8-ba3a-3c43-962f-6900dc88a1ad | -5.87554 | -42.58586 | 2024-10-28 04:06:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 205e71c9-cf35-3e7f-aa7a-2ba3a883565b | -5.872 | -42.28903 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8eee415-d623-3f98-8a07-3b936a5d4ea7 | -5.83695 | -42.78401 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 395b2845-612d-3ff4-a093-bdd1317e0adc | -5.83417 | -42.77988 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77d2168c-f624-312d-b58f-b903580ce1fa | -5.83339 | -42.82774 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b6e4cfd-6cf5-3139-83c5-3398f3df1d8c | -5.83281 | -42.8313 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46381b87-77af-3ca2-b737-c4dd03246b35 | -5.83081 | -42.77934 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0d92460e-d8cf-350a-8047-17b8cdc90307 | -5.83002 | -42.82722 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84d17b0d-7a17-32be-9ae3-3c12b38623e7 | -5.82945 | -42.8308 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf22119a-6a0b-3c7f-975c-5b8a51ecca8e | -5.75983 | -42.62887 | 2024-10-28 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9818084-b8fd-3d93-a7f3-26e35d75ca1e | -5.75541 | -42.78576 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3173e99a-6f9a-33b4-be93-3ddd36ba25a0 | -5.75484 | -42.78932 | 2024-10-28 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0554ff87-1d73-3cb3-892e-66940e756e09 | -5.69265 | -42.69221 | 2024-10-28 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c487c5bb-0c5f-3e48-a4ef-b1bc598466d8 | -5.62634 | -42.76239 | 2024-10-28 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e9fd25a-6541-39c5-a09c-bc1af376e4c2 | -5.62577 | -42.76597 | 2024-10-28 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c9d01ec-b2ea-3f42-bf61-e6236bc9e031 | -5.60348 | -42.96976 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a35758c-a677-3e66-a55f-dbcac8ade63a | -5.60289 | -42.9734 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3d8c4bd-75c4-3360-9244-09a0c17ae3af | -5.59671 | -42.96869 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 903df294-2eb1-317b-afdf-43b532d9d868 | -5.59612 | -42.97234 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d247913-c803-3f5a-8eb7-29f2448f063e | -5.59274 | -42.9718 | 2024-10-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
