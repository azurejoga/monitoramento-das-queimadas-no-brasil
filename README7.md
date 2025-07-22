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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e335499-d411-3e94-aea7-b359fac26b5f | -11.73272 | -48.18947 | 2025-07-22 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1793dc17-89d7-398d-b391-856d6c69decd | -13.69499 | -45.70513 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05ca231-500d-38e9-87e9-5c7ff4c4b20c | -12.71188 | -47.80139 | 2025-07-22 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8346c865-6d91-34b7-8b5c-2774e232c4ce | -14.76264 | -47.11642 | 2025-07-22 03:40:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32055944-c71b-3521-b9f5-d0bc19345b23 | -13.65365 | -45.7271 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16f84f6f-8be7-32d5-b02f-afef63bb5830 | -12.65829 | -45.0498 | 2025-07-22 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61b774c5-eb8c-341d-9852-6a17860c0cbb | -14.37731 | -47.76203 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2786daa4-140e-310f-aa7d-a85e93937a48 | -14.38402 | -47.76177 | 2025-07-22 03:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f0d1f7a-f6ca-3e80-8066-2ecd1333c2dc | -13.65282 | -45.73119 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| da96d2d9-8f58-3d39-8913-895be161758d | -11.18505 | -48.62355 | 2025-07-22 03:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11ab3fa1-0ca9-3909-b356-1ab0861d7a56 | -13.66883 | -46.52855 | 2025-07-22 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a580475-a1de-3f18-9a3f-3e712b98c397 | -13.69101 | -45.68866 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7344415f-3a16-3af2-aef8-89455135012e | -15.53898 | -47.98924 | 2025-07-22 03:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 438b404c-3bb8-3519-8da1-1e951a44ec6a | -15.61515 | -41.33309 | 2025-07-22 03:40:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b171fbca-72a0-3546-a438-c27eec730f74 | -13.65937 | -45.7282 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43b86e5f-896b-3729-8e19-8027ce2d4675 | -18.20075 | -45.04271 | 2025-07-22 03:40:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae0bbd16-b78f-3300-93bc-7e577e412c6b | -13.70149 | -45.70235 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6dfd962-06c5-3793-b2f0-b96757c66343 | -13.68613 | -45.68344 | 2025-07-22 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e68935c-7835-34bf-b8d8-ab5eeeb2ba13 | -22.17117 | -52.69358 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7b900fe6-1074-3e9d-8802-b64657552312 | -21.66085 | -46.93854 | 2025-07-22 03:42:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f99b5117-3e6a-3993-a711-90aaf63506e3 | -21.65895 | -46.93834 | 2025-07-22 03:42:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96a0fcfe-6f9d-3981-b220-4a47b89dca3d | -20.30675 | -46.67976 | 2025-07-22 03:42:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0868e88b-02b7-3f66-8156-98421e699684 | -19.82975 | -41.95181 | 2025-07-22 03:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0eb3314b-74e8-32fd-8f55-b26cd41e9b5d | -22.8296 | -46.14788 | 2025-07-22 03:42:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7dd97591-9825-3e46-aeb4-6a873425021b | -18.99123 | -45.78014 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 673f9150-ba30-3469-86ec-187d7c8ed385 | -18.9905 | -45.78358 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99bec859-fd00-3b4f-882c-293cbc1cb1e7 | -18.99639 | -45.78139 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a37a573-dfd8-3adc-9132-e69e9820c52a | -22.16265 | -52.69446 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c0522375-7d26-3564-ab78-c59b0d5bb59c | -19.41146 | -44.9626 | 2025-07-22 03:42:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b23e2b18-a31a-3e5e-a146-f22b208773b7 | -23.30033 | -46.95348 | 2025-07-22 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6aeb9ed-c8c9-3fe1-9100-a94341cfbdc6 | -18.99064 | -45.78367 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62062e89-5e85-35ca-aecc-3dbe8f4e7e57 | -22.82973 | -46.14864 | 2025-07-22 03:42:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aadbe330-abd3-3bf1-afbf-14c87ee97ab5 | -20.06465 | -41.39853 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 028222fb-ec55-325a-adc7-ee96a092ed9a | -19.76321 | -43.64781 | 2025-07-22 03:42:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 288d7a9c-2cfa-3be9-8e6a-324095dfb586 | -20.16543 | -41.39963 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0648082d-39c5-384d-9e64-5de0d773f674 | -22.82478 | -46.14766 | 2025-07-22 03:42:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4e728ef2-4156-3cec-bfdc-627bdf950cee | -23.30153 | -46.95331 | 2025-07-22 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6e0d5093-55c1-3f92-b60c-f911483301e0 | -22.17158 | -52.68948 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c1ed682a-61ef-301d-872a-25756521598d | -18.99135 | -45.78024 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7ad8d5f-5aac-32fe-9ae7-834c91301cc6 | -20.0641 | -41.40091 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 54257bc4-8350-3861-8841-a7a0744051c8 | -22.69613 | -43.34947 | 2025-07-22 03:42:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa5116b4-32e2-3f84-b3e7-4fe723da19ea | -22.11997 | -43.15431 | 2025-07-22 03:42:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bd98583a-f7da-3630-a0a6-cea48d4b6d4f | -20.35375 | -41.48832 | 2025-07-22 03:42:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0b8e93a9-2521-3cd8-92af-7843875fecee | -20.05939 | -41.40475 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 97d3ec4b-7960-3f81-b2ba-1883e6d43a44 | -23.29967 | -46.95653 | 2025-07-22 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9e2e66f-74e9-344d-b609-e1b563037f39 | -18.98993 | -45.7871 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 282d836f-cd91-349c-94b2-af3da0fb48a9 | -21.66421 | -46.93966 | 2025-07-22 03:42:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f4ed1ae-a95b-37a9-9690-2db1482be719 | -20.16509 | -41.39739 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b67a87c6-00fd-368d-92cb-ad27c94ca812 | -21.05771 | -42.95634 | 2025-07-22 03:42:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 705d23be-91ff-3af7-97ea-1462917ba8f8 | -18.99495 | -45.78815 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f12633f3-106c-3928-8434-10073a377741 | -20.06381 | -41.40304 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 72e93437-572f-3cb7-abee-368dba3e58d2 | -22.16923 | -52.70099 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ab2c751f-23c2-3882-93ee-12a0f84f9e4f | -20.06326 | -41.40549 | 2025-07-22 03:42:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 5ab8d982-c856-39ec-b972-ea9c1ee07ab1 | -19.41635 | -44.96363 | 2025-07-22 03:42:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cca48a88-3c21-3977-9fbe-bf3430e83565 | -18.99567 | -45.78477 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 989aec28-26ad-3d2a-b678-bb9e74f08acd | -20.3058 | -46.68405 | 2025-07-22 03:42:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b82cf1e1-9ee1-317a-9cc9-f14e241f5cee | -19.16532 | -46.56411 | 2025-07-22 03:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b48fd992-4cdf-3555-a67e-62ba376e494f | -22.1697 | -52.69686 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1ffaf94b-c026-3bb2-850b-71bde954a54f | -22.16413 | -52.69116 | 2025-07-22 03:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ce71e020-8c7c-3eea-ae17-5c26e91b379b | -23.30085 | -46.95635 | 2025-07-22 03:42:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1f036c7-d76a-3b8d-8e95-742b46c7e200 | -20.3113 | -46.67588 | 2025-07-22 03:42:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aa72c54-b2d0-326e-b417-0536acbfd7a5 | -22.82466 | -46.14688 | 2025-07-22 03:42:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c73b24a5-9532-3533-aa2c-6709791a7bd4 | -19.15993 | -46.56276 | 2025-07-22 03:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c6e1d94-46ab-310e-b9aa-24e5a1e998e8 | -22.11582 | -43.15348 | 2025-07-22 03:42:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cf65cb2b-281f-3173-9cf6-59341e093173 | -18.98977 | -45.78699 | 2025-07-22 03:42:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 643b9727-ca06-3140-aaeb-81e3107db7ac | -23.54198 | -51.62272 | 2025-07-22 03:45:00 | NPP-375D | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ebc21ef8-af34-3778-a3ec-cbbe6cd19cdb | -23.54371 | -51.61596 | 2025-07-22 03:45:00 | NPP-375D | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8da1bc18-f2ba-3fea-a874-4587d09559c3 | -11.7317 | -48.1849 | 2025-07-22 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9bf33ac1-3539-3725-8300-048bdbbe0628 | -4.388 | -43.2896 | 2025-07-22 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ff9d5022-0c71-3fae-b4ac-a652e7c56f17 | -8.5211 | -43.3063 | 2025-07-22 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 81dcbab4-c211-3bfb-a4f7-f03642c4d972 | -8.5022 | -43.3085 | 2025-07-22 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 890d08d5-32bf-3d16-90d6-e3242bcf145f | -8.5211 | -43.3063 | 2025-07-22 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| b0972123-56d6-3f54-ad51-457590b9ac06 | -11.7317 | -48.1849 | 2025-07-22 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 232c2afa-2dcc-3e15-a0e3-9e237c7a347b | -7.20957 | -45.33139 | 2025-07-22 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf82eca5-ec56-31a3-9a42-2e47465673c0 | -5.91849 | -43.46756 | 2025-07-22 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8487fd25-f4d2-3bcb-b736-89e704176f0b | -6.2071 | -44.29473 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a92779-ac02-35c4-8e05-5fb267e666a9 | -5.88631 | -45.20562 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cd92624-e531-3387-848f-2613c70ff3e5 | -5.27812 | -44.9491 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6400f564-7261-3bdf-8e53-2849cd1c29cc | -3.5044 | -43.24311 | 2025-07-22 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82089f93-493f-3260-be5a-44433652d423 | -3.35884 | -42.87067 | 2025-07-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 181bcfaa-7baf-3e88-b578-6fce04c8cfb1 | -4.38532 | -43.28728 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0e593dfb-d822-3ab5-a4f8-e30933d30c29 | -4.3809 | -43.29107 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d80597fa-23a3-381c-861e-d1b4df7e27ea | -6.7754 | -39.1869 | 2025-07-22 04:00:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e1eeedcc-2011-3190-8220-e53747a707e5 | -7.17753 | -44.14858 | 2025-07-22 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90587e5d-d8e7-3ed7-a8b1-0c5aa1bba83c | -6.62305 | -42.33233 | 2025-07-22 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28983fa4-0962-3908-98cd-e3b2e8203766 | -3.97309 | -47.88192 | 2025-07-22 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afb3a362-a82d-316c-9323-a2a69d8d6e5f | -4.38162 | -43.28665 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 85991adb-7bd6-38d1-9d4f-fc8a46c3405c | -4.38902 | -43.2879 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d07673f-3c10-3d41-b978-2109de2f773f | -7.29031 | -44.3591 | 2025-07-22 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd90d14-d1d5-383c-b1c0-19674c4d490e | -6.5642 | -41.47269 | 2025-07-22 04:00:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ade25b6-86ea-3c64-995a-20b2fa8c135a | -6.19606 | -44.38654 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b5a1cc0-c0c0-3e37-ae05-aba809a7e6db | -3.28871 | -42.5391 | 2025-07-22 04:00:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7fe3e49-1df2-345e-ac44-171c989334b2 | -9.09969 | -37.3121 | 2025-07-22 04:00:00 | NOAA-20 | OURO BRANCO | ALAGOAS | Brasil | 2706109 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b40f1947-f70a-3042-97a0-f1b1c0fb8a37 | -4.64624 | -37.79857 | 2025-07-22 04:00:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8065b54e-f2fa-396f-a3ee-da55898615cb | -6.97741 | -42.80826 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2fe5ea81-97a2-350b-a335-abdcb185f3cd | -5.2315 | -40.87865 | 2025-07-22 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4725f948-51b1-3c73-a938-4652495b6580 | -6.97454 | -42.80375 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 01a3d7ee-1e08-3bd2-bbc5-cdb954f8ffa0 | -7.08593 | -49.17312 | 2025-07-22 04:00:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac189b09-d06b-32ae-98e5-c0d295497de9 | -6.96295 | -43.07699 | 2025-07-22 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 425172d0-9f7c-31f8-a964-5a394f3252ff | -6.50277 | -43.51386 | 2025-07-22 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README8.md)
