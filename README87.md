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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd802db9-6aa3-3442-94dc-d3f45bfc2986 | -3.31281 | -54.13931 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2827bbc3-9e99-39af-8b59-943fc9d29d39 | -3.3089 | -54.13344 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e358760f-44f2-39e7-ada1-a6139b25be55 | -3.30813 | -54.13846 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3398eab-c69b-3a62-b418-a20177dadb82 | -3.30499 | -54.12751 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c677532-adc1-3f32-856e-c25754a99964 | -3.30422 | -54.13258 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb35356d-4f02-3236-831e-ab155b084662 | -3.30244 | -54.11255 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5dde59-7737-30a2-a179-18220f8912d6 | -3.29036 | -54.16075 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d20de7bd-030f-3321-805e-c4c0729c0978 | -3.28964 | -54.16552 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85067c51-6981-3220-b850-6e52190945ff | -3.26942 | -54.17254 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45ce300d-7ae0-3d08-ada3-bb800dc6f5ab | -3.26867 | -54.17751 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9275954e-8fcc-3bef-9cce-f0ce0b437576 | -3.2499 | -54.17496 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 506e1cec-e158-3989-a077-4bc5bc3bee9e | -3.20455 | -53.85371 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2491f505-25d3-3f06-9a69-78c06183bb5b | -3.18545 | -53.85056 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da02bf56-7b1a-3815-b738-32f28a1b435f | -3.09862 | -53.71516 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c452ca44-2b2a-3970-905a-2e30512fa544 | -3.09486 | -53.7132 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24739a5-68f3-3b70-af6b-0e7ee2c6c77b | -3.09405 | -53.71842 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c358a76-ad50-385a-8255-fa24d33ac652 | -3.0938 | -53.71442 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8892e3b-c6d0-3c3f-8155-f80f825d8e6c | -3.07036 | -54.16496 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 60e58f5e-abbd-3783-9baf-9f1d58a69ba6 | -3.06568 | -54.16431 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f2c16c0f-5ef5-3a89-9895-2663024fca86 | -3.061 | -54.16366 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0795fa3f-bc53-36ad-b914-004c4edd1a81 | -3.05093 | -54.16706 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d242a05c-077f-3691-abd4-81819d80d948 | -3.04555 | -54.17116 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d0a3d69-d440-39f8-8775-bba88bc002ca | -3.03347 | -53.79272 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a8ee1fa-3087-31d9-8373-c284dd61a062 | -3.0327 | -53.79782 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6e9372a-2ff0-31f2-910c-d4789f4f4f65 | -3.01607 | -53.87525 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76abf434-96a8-3f51-89b8-a001886fe35a | -2.97604 | -53.91508 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e8280e-e778-352e-8cc4-24db177f801d | -2.97205 | -53.90925 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bc75616-31bc-3961-86da-cf5a368a4c8f | -2.96731 | -53.9085 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fb224a2-b44d-3a16-9725-830db3a73415 | -2.95535 | -54.08593 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d8779d8-37f0-3d42-bb3f-0593d362cc79 | -2.94953 | -54.12488 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0b47f9-b5d8-3387-8417-89c8d5d606de | -2.74048 | -54.11851 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39d2c958-809b-337b-9e2e-cc61ff905cca | -2.55763 | -54.00264 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea59d00-5049-3e9a-9876-ef3750da3ffe | -2.55294 | -54.00192 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f671709-0523-3bf5-8747-59854cae7835 | -2.47294 | -53.98213 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b82be050-3e2f-3bd3-82f8-95e1592258d1 | -2.36923 | -53.70195 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd83b471-ea94-321b-988d-f2fb7dcd9a8c | -2.36846 | -53.70704 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa5f6704-f269-389b-9803-e1ec15b01b9d | -2.36369 | -53.70629 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 468db718-599a-3545-85e5-e4f29c934472 | -2.36059 | -53.7269 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 142b588d-d100-3333-bd81-06825fc8345c | -2.35659 | -53.7211 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d235877-bd0a-3456-b32e-9b35def57cb8 | -2.33914 | -53.93323 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c778176-6a56-3435-b371-4ac5db0774bc | -2.31639 | -53.9248 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5956d084-b127-3730-b31f-c0e61a620000 | -2.2739 | -53.75402 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 296de2bf-45c8-30a0-9f02-0307c713a2fa | -2.27146 | -53.73812 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7b454feb-0c55-3adb-9f27-3667acb5f3b9 | -2.26992 | -53.74825 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5ccd334e-403c-3cdd-b03e-eea3ac0b494f | -2.26915 | -53.75331 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ccea84a4-5650-362a-b7c3-f837e678efa3 | -2.26801 | -53.66429 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 95ff3836-698d-3b30-8886-c6cadc801673 | -2.2667 | -53.73741 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9246323d-668e-3530-8806-a8c31e8a735d | -2.26593 | -53.74247 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d5a22861-939d-3e8d-b55d-951a051ec652 | -2.26321 | -53.66374 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 152e000e-11bf-3d35-9b7d-d4e0ac5879c7 | -3.51916 | -54.68626 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36148832-8b68-3eb4-bb8f-8494e58a1957 | -3.12586 | -54.25409 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5e718a98-a928-3156-b480-aa3cb73592e6 | -3.12514 | -54.25897 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 075a018b-f628-31f5-935f-a94a259e59ca | -3.12369 | -54.26878 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62e7f07a-5ada-3e3d-aeef-227e78afc14e | -3.12048 | -54.25838 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 32b62a23-e347-362c-b27d-09b6b328259e | -3.11976 | -54.26326 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91e37e13-1b05-3b56-b06b-3ec9f6b1494d | -3.11942 | -54.29764 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eebb0b03-6ce4-308b-b749-f66773c38c59 | -3.11872 | -54.30239 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7aca4717-5533-3bd1-9492-6da85252f4fd | -3.11833 | -54.27297 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc7067b-7381-356a-a748-cf82b315b702 | -3.11759 | -54.26119 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 90a9798e-a882-3b2e-bed3-248d6b7a5248 | -3.11683 | -54.26605 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2778688-6477-3b55-b90b-e92430b8d118 | -3.11583 | -54.25769 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d0035b34-669b-3216-8d63-cc05ad95f3e7 | -3.1144 | -54.26744 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ef56dcf-04e3-3236-a99c-6b2a71e4f15d | -3.11298 | -54.27707 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0955ef12-cbbd-3bae-a546-b7cb239e1bc2 | -3.11294 | -54.26051 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 192a8467-2abf-3cad-897b-67670c6d5e4c | -3.11069 | -54.27499 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb4d4dd6-79bd-342d-a632-0c01c40f206c | -3.11016 | -54.29623 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 19f49910-670d-3661-b75a-5cd77acfc8e1 | -3.10847 | -54.28931 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 743aed59-4e46-3a4b-adb2-66277a089010 | -3.10773 | -54.2941 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 35d8ed08-94f4-347a-bbe4-2c6dc7b4586c | -3.10763 | -54.28115 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3cfe947-9c73-3648-88a9-3bb2ec613d7b | -3.10693 | -54.28593 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ea7f26d-edc9-3f14-9357-e60d4073d597 | -3.10623 | -54.29073 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 367072cd-aecb-36f4-96c0-f4cd03a10488 | -3.10606 | -54.27429 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57059e06-3059-3884-ad52-31d55a5e5e5d | -3.10552 | -54.29552 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53faa50b-48d8-3c9f-a6d3-540df29559c0 | -3.10532 | -54.27906 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2228b1b6-6000-3f3d-b24f-0123dd16c5e8 | -3.10384 | -54.28861 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 386f9f70-19b5-3cd2-9934-c4c334573fb6 | -3.1023 | -54.28522 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27a69354-a3ed-3db7-adc2-5575b5804c37 | -3.10068 | -54.27834 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5785fb89-ff93-35e7-859d-64329b69bb97 | -3.09921 | -54.28791 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5eb95557-c9fe-3cc3-98d0-25a72f99245f | -3.09836 | -54.27971 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e269551e-289e-39ff-97a9-b0ca0f905d90 | -3.09605 | -54.2776 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f786b2c-f61e-3898-86b3-6922bb55b0da | -2.98415 | -54.55108 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d00958cd-ea5b-3ff1-85fa-d036110f5307 | -2.63919 | -54.26775 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43e3e795-9486-3bc8-b5d1-7f85c21a2b12 | -2.6353 | -54.26231 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 769c3796-7e48-39a5-913a-91ce05e5af5b | -2.63458 | -54.26704 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca6c3cbf-8954-35ce-990c-dadde7978b19 | -2.58112 | -54.79495 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bb185ae-058b-3ef0-8704-b1383a00681a | -2.57807 | -54.78533 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96a09f86-218d-312a-bbe5-5eb8cc58d7da | -2.5767 | -54.79419 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 077bb00e-c2b9-3d2c-93fd-877acc38c37e | -2.20543 | -54.75484 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c2794a-253f-3bb6-9da5-621b827bf6d4 | -2.201 | -54.75415 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21c3c48-6dd6-3da8-8aa1-90ef7058a105 | -3.12981 | -54.25955 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56f20246-3dbd-33e6-bdba-850127bdcd20 | -3.12442 | -54.26387 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e22d7a7-bd09-31a8-a887-1efb46eb0bc7 | -3.12335 | -54.3031 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fb8a469-1bf9-37f2-b517-359d9f60e6da | -3.1212 | -54.25348 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5eb0cd5c-012e-3ee2-b2eb-8334dc5514c7 | -3.1191 | -54.25145 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83c7aa25-0dd0-3b62-8c1d-0e6d67274046 | -3.11904 | -54.26813 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63887893-7749-35bb-91c7-7e345b8df4c9 | -3.11834 | -54.25632 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8b509dbc-4e3b-3a36-917b-7b0ea9c1ebc5 | -3.11762 | -54.27777 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 283cc37d-8e77-3ae7-afec-ee57fb6f1c1d | -3.11655 | -54.25281 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b0af770f-a988-3408-9c6a-1cc480d72690 | -3.11608 | -54.27089 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c312369-253e-3d3c-881b-b48b71f3fc4f | -3.11511 | -54.26258 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README88.md)
