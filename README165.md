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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0db7b8f0-29d2-38c3-9b70-182f24b18169 | -9.94555 | -64.91293 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c5b6f3b-aa1f-34df-8d2d-8c77d5a2ed74 | -9.94499 | -64.91644 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2dd347d3-687c-3380-b8a0-deb76e4434eb | -9.94444 | -64.91994 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| efe21a9d-0a35-376e-8d0a-1a44a9052ef4 | -9.9439 | -64.90189 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb010eac-923b-3d67-be88-5b86568a3fe2 | -9.94335 | -64.90539 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 72d23c03-4068-3e1d-b0de-8f6c99f231fe | -9.94279 | -64.90888 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b43f2498-d146-3fc0-8d9b-45d2d3dc306e | -9.94224 | -64.91239 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6b6ef309-9898-3b00-99a9-8f39115850f7 | -9.94168 | -64.91589 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3781e5f5-90d8-3edc-861f-74f5ce2b644f | -9.94112 | -64.9194 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 08b4fbe9-1110-352d-ae30-d15432eba528 | -9.94059 | -64.90136 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bcac3c26-f41a-3a31-b861-22858f893c7a | -9.94003 | -64.90485 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 85f15e18-33df-3407-9635-d7fa627153ee | -9.93948 | -64.90836 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 04d4ba30-e571-37d2-94bf-2001986c95f9 | -9.93892 | -64.91186 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 28c7e680-60d6-3779-8980-4a3a7637de6e | -9.93836 | -64.91536 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d594630-6b6b-3a41-854d-0222727d2ec4 | -9.93781 | -64.91886 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f8df52f5-75e9-3c73-8245-8f139ed97c7b | -9.93725 | -64.92237 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0fcf05f-7a00-3534-9b65-36896800ba18 | -9.93672 | -64.90432 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0d4552e-b49d-309d-9e46-7e1e667d7ab1 | -9.93616 | -64.90783 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d965095-5313-396f-8998-d0dc93c126c2 | -9.80683 | -64.95137 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b37372c-2279-342f-ba3e-a7dbc43624b1 | -9.7696 | -65.65476 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 596878b7-ef31-3758-b175-281d54de69a0 | -9.75828 | -65.79007 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5598be2f-1ed6-35cd-9293-b297fdb65ba7 | -9.75491 | -65.78951 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a420d851-c042-3cd2-ab8b-60143b78782f | -9.58563 | -65.67293 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300b945d-ce73-36be-8de9-f90ade6bfbde | -9.38245 | -65.46347 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e40978ad-f613-3cde-b178-06e270464abb | -9.38188 | -65.46706 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fe2e796-7a2a-3285-9736-956498c8f62c | -9.3791 | -65.46292 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 147259cf-62ba-36d1-997e-5cb7c6b1d274 | -9.37853 | -65.46651 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cdb797f-2275-3349-a8dd-453913b33f8f | -9.37274 | -65.52438 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d60736f3-f8eb-3cb5-9e4a-28e80e18c65a | -9.36996 | -65.52023 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d91b427-13ac-3d0a-984d-06b68185190c | -7.29475 | -64.66002 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0feb3b56-cba5-3147-b0c6-9c1566c6dfa7 | -7.29419 | -64.66353 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f41e791-8389-34f4-b080-398df2970e7e | -7.29198 | -64.65598 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5b86587-9e29-32d9-acec-ac1ddff022c5 | -7.29142 | -64.65948 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6c3afdc-acef-3659-995e-722cc67c409f | -7.29086 | -64.663 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf05553-f665-31c6-820e-5c13528885d0 | -7.28865 | -64.65545 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b148bb87-29d1-38e2-8235-be250dfaa707 | -8.80617 | -64.25451 | 2024-10-02 05:33:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2451ea-12aa-3f78-acc9-0f70c9f7fbc5 | -2.64049 | -65.90001 | 2024-10-02 05:33:00 | NOAA-20 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7c798ae-2d55-314b-89e4-5ef78df2c565 | -2.63983 | -65.90415 | 2024-10-02 05:33:00 | NOAA-20 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae357a8-aefb-30ff-9bca-d4a65e81b419 | -9.31711 | -66.54878 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f2af528-3d3d-36b1-b582-e1042701abfe | -9.31302 | -66.55206 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 270d4e43-1fed-3fa6-81e0-f1e266104bd5 | -9.3124 | -66.55592 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f2eccdc-fa2e-3b74-82a1-c38ca1c9c9fb | -9.31115 | -66.56363 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1adb3395-c499-3af6-b432-56800593c8c2 | -9.30894 | -66.55535 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 865d7301-4bad-373c-b0f3-e1d4e8440ffc | -9.30831 | -66.55921 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3bcbe0f-4f53-327e-b481-1f1b8c514ed4 | -9.20439 | -67.17617 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45bbfccc-7a40-34b2-be8f-597407abfe68 | -9.42741 | -66.10467 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c53852fd-e276-36f1-92bf-e3be188b83d4 | -8.92765 | -67.04807 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8242df6e-acda-3e93-9a5a-8ade2069689c | -8.88798 | -66.71844 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5be021c3-f7a6-35bf-86af-cb5a761e851b | -8.88733 | -66.72237 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0e5c07c-6021-3526-8c50-88b68e392e9d | -8.77043 | -66.62 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e85197b-5fb9-34a1-aad3-9e6db3a14433 | -8.76969 | -66.6164 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191eeef4-b01b-3f70-9646-21cce5776224 | -8.76906 | -66.62031 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d152fc-9cdb-347b-a458-26cd782f150b | -8.7662 | -66.61581 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03986959-cdbc-3655-bc59-409b1922579f | -8.76557 | -66.61971 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c112513f-7437-3bcb-ba32-3051982799ed | -8.76494 | -66.62362 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 878cc745-871c-3840-87ae-31e1da277b9d | -8.76208 | -66.61912 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc5d9a4-cb9b-3f9c-bc39-ae5549d270d4 | -8.76145 | -66.62303 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce42f19b-52a2-3aaf-90b1-b2b345c8ba73 | -8.75796 | -66.62245 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cff5b754-62c8-3b89-aa3e-0aaee9242254 | -8.75447 | -66.62186 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd55344-2671-35d7-9039-f676467bcb87 | -8.75162 | -66.61738 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f2d469-7b0b-36d3-acf6-8c2b0fb9e339 | -8.75098 | -66.62128 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a02798c-f140-30dd-be6d-223b946d86d7 | -8.69441 | -66.6601 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 545380ce-810c-33c1-b280-0417eb403e56 | -8.69091 | -66.65953 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 948d77c6-9b48-37f5-a543-1aeb4b463c06 | -8.64977 | -67.13104 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4580df61-12e0-397e-a8a5-cee68145fb6d | -9.67228 | -66.3903 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54721444-7c6f-35a9-b54e-f47ba2119280 | -9.67167 | -66.39407 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec71d24e-d0d7-31a7-8ac6-86ce10ec3e68 | -9.66338 | -66.83028 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abee094c-a752-3be5-b62b-0af6b358baa5 | -9.66274 | -66.83419 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2db2bb56-feb4-3f95-96b2-2dacdadac332 | -9.61264 | -67.1607 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 457fa45d-645e-3746-8f6c-3f2a001517b9 | -9.6091 | -67.1601 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9ac271f-4349-3543-9e66-ba7365b72744 | -9.59413 | -66.50179 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c6bc62-7054-3fe8-922d-23bcb0069875 | -9.5935 | -66.50562 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec889e1b-5706-3dbf-b47c-5df7504f993e | -9.59006 | -66.50504 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 493bd8cc-1dc0-3f47-aa0c-1b3cbd25467f | -9.58943 | -66.50887 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30c2ab79-169e-387a-be62-fbb537f0cb1d | -9.58661 | -66.50446 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efe82c87-79a0-3501-837e-851799bce50e | -9.58598 | -66.50829 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ed2f407-3ff0-3af2-8f45-6844941ee800 | -9.54696 | -66.61591 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 215fe8d1-c3b5-3351-930c-9d4a0babec24 | -9.54633 | -66.61975 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e4b034-013d-3ce8-adf0-80c8b94cfbad | -9.54569 | -66.6236 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e20c1db-851b-32b3-b3aa-76306db6df66 | -9.5435 | -66.61533 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9bfb435-ab2e-3846-a203-abfc00b433ee | -9.54287 | -66.61916 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68013e2b-3155-3066-9b12-b007c95c60b8 | -9.54223 | -66.62301 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46e8c689-f056-3935-8d64-33e68c69d5ec | -9.49778 | -67.10899 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26f4e9c1-dffc-3d9b-865d-51e3d34d2dbd | -9.49712 | -67.11301 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4fa7dc66-4d0e-3140-b6fb-41080aad0ee8 | -9.44702 | -67.15572 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce921bbf-9c7a-343f-8cd4-b4bd62f8f006 | -9.44636 | -67.15979 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01fc7a79-0ac9-3113-bfad-5d72d6ff3384 | -9.44584 | -67.15846 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3d7daad-8331-3a67-82db-ac278e789e77 | -9.44347 | -67.15512 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c59db2d-3416-317c-8d16-88eea03ea568 | -9.44281 | -67.15919 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abfc0490-748f-303e-be96-9f62a1996feb | -9.4423 | -67.15788 | 2024-10-02 05:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8248b1bc-506f-36c1-8aab-8db41d43ae3f | -7.64552 | -67.1991 | 2024-10-02 05:33:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3fa4b3d-d1aa-3f2c-8951-986b61569bbd | -7.64189 | -67.19849 | 2024-10-02 05:33:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 650a8d7e-7080-3689-8386-43f1d9591aea | -7.64119 | -67.20273 | 2024-10-02 05:33:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae662f42-661e-3ed2-a334-baa4a83f7560 | -7.63826 | -67.19788 | 2024-10-02 05:33:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1fac55d8-39c2-392b-af4e-d80feccf537b | -7.63756 | -67.20213 | 2024-10-02 05:33:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1b02ef9-f955-3c54-8612-c25f5d0ba5b8 | -9.32571 | -67.67086 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 283d37ee-e1bb-3e75-b3f4-4763e8970f59 | -9.32207 | -67.67024 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e9e8cf6-9036-3d3d-bedf-6431fa4823ef | -9.32018 | -68.19579 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43e05269-389b-3e3d-9ae3-f10d06f3b301 | -9.31256 | -67.65981 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a573f921-a844-3312-bc80-f59c7ce2d46f | -9.31184 | -67.6641 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README166.md)
