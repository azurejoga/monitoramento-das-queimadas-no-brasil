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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b4f2430-dc90-3de3-b197-cf6585ca50a8 | -2.18911 | -46.1585 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e5570be-8c81-34d0-819e-f5f25f6724ae | -3.31499 | -52.85809 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adb3ec16-11cf-30ba-ac1c-2137cee6a341 | -2.64811 | -46.18378 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3223019f-7223-3513-8cea-5c58043633ad | -3.58037 | -53.71929 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f200d0e-77ba-39dc-ae9a-930905ffbace | -1.97105 | -46.52928 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63d6b5f1-4f2f-3af8-94e0-9517edf7b13c | -1.70753 | -52.67255 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33ef985d-beed-3ed3-a366-77b9bdfface4 | -3.18881 | -53.99292 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 432cc134-8ed1-3880-af3b-941a028f69af | -2.65636 | -46.18039 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3dc831f-1109-371c-8596-581db7520847 | -1.68521 | -52.69793 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2de333bd-a109-3fd7-996c-7b78cf91b330 | -1.38618 | -52.07898 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 064d28fa-89e7-3a7c-804b-11cd175fca22 | -3.23266 | -54.15348 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34ca070e-b749-3562-92ed-8971207b4620 | -2.3137 | -45.06157 | 2024-11-15 04:44:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b08bd2-6d8a-37ee-a658-ff9d2e6a039a | -2.85781 | -45.40518 | 2024-11-15 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9dd700f-1b3a-3f58-b785-e79b6ca8af53 | -2.99002 | -52.36796 | 2024-11-15 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d0e750b-8ea4-3bf3-ae6a-7f5bc61dcd7d | -2.71799 | -44.77784 | 2024-11-15 04:44:00 | NPP-375D | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd9258a7-ee40-3965-934e-e7bac8773c75 | -2.64434 | -46.18322 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d59d06f4-4788-3981-93f1-6a72f32ff6ba | -3.25232 | -53.67191 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e652e93b-3e10-3bd3-a494-b1d95c46aa73 | -3.54123 | -54.32436 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f72c8a-ab20-32be-a625-53a803e36736 | -3.79041 | -43.90933 | 2024-11-15 04:44:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 662302e1-6915-3b56-9774-60d04e86a6bf | -2.66176 | -46.1951 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f6d615b-fd3b-314b-ba72-55dbea4dfb42 | -2.58547 | -47.47984 | 2024-11-15 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7de15d6d-6d09-35fa-9d4b-dc51e4d91b95 | -2.66084 | -46.17641 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7eeff18-986e-376b-894c-b5c3f3a33741 | -1.55771 | -51.84852 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852be012-fd19-3e25-9171-5fe82dbf517b | -3.24541 | -45.92661 | 2024-11-15 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc8f0ac0-0828-32b0-b0c6-aadfd0391ae9 | -3.42111 | -53.96598 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032bc437-28f5-3378-b15e-00114902b983 | -2.99194 | -52.36828 | 2024-11-15 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b49707-daaf-37f2-9df0-80141a778a96 | -3.88737 | -43.15407 | 2024-11-15 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38862c7f-9810-3a63-9513-185303062d42 | -3.55019 | -54.57571 | 2024-11-15 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603b005e-8f48-3c34-ab06-539a81cdb96a | -2.09778 | -46.33055 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 729f18ab-3b60-3a5e-80aa-f23d7e92662a | -3.45308 | -53.46757 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e0746d7-6b6c-39f0-b54f-6524f90af5f8 | -2.66383 | -46.18382 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bacd6c34-4804-36aa-ab84-22d6255b2138 | -2.44009 | -46.28661 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e76495f0-038c-37b9-b4c7-5dd36308056c | -2.63538 | -46.19116 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3a7a02-3f0e-3d43-ae93-61ec671f9d28 | -1.63924 | -53.27071 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50656397-2fcf-3158-8e68-f9e82da3c4b0 | -2.09682 | -46.32731 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4f7e6f6-a302-3107-85ae-ec88cc66557c | -2.81569 | -52.95477 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb08cf7-69ca-33b2-b721-2a5a3b384c4a | -3.42485 | -53.96655 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8493a53a-ecc7-3b5b-8729-7e7c91dbf8ef | -2.1898 | -46.15403 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ed7b66-7d69-3ed6-a491-1f8d1b69f0cb | -3.71908 | -41.69321 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d2c53c9-679f-3ed9-9ec5-600d84f0fdb9 | -3.23354 | -53.62479 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6db62fde-6527-3338-b8f3-04515e472cdf | -2.64412 | -46.15992 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dd61e9c-c4ba-3ed7-9468-3ec93f9b18ae | -3.22987 | -53.62418 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a37ff1a-9782-399b-bb21-573732623368 | -2.6587 | -46.19003 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11f88478-45d6-3680-858b-731204d16984 | -2.09247 | -46.36553 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e3b9009-b5ce-3b06-8e73-9c3ef535a3d8 | -3.27603 | -53.0113 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d92bbb4-bb73-3760-8b9e-a9eff15519a4 | -4.09879 | -38.74048 | 2024-11-15 04:44:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80b522d5-3955-3059-a92f-7500984d4a00 | -2.63232 | -46.18607 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2f9d92b-c86d-356a-972b-1f39f9c5d7e5 | -1.61258 | -52.49512 | 2024-11-15 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce52e83-8a4a-36d7-ac6c-073cd8b00dbf | -2.03404 | -46.43794 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b47bc85-bcba-3612-b95a-c3de43bea0d9 | -2.65799 | -46.19455 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f59583-3cab-3329-8fbc-405f1385922b | -2.388 | -53.66606 | 2024-11-15 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccd20f30-f690-3fcf-89aa-f75b2d18c785 | -2.65085 | -57.10342 | 2024-11-15 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b47b429a-3901-33f3-b182-615f112d807d | -4.02225 | -53.77998 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04ea917c-4cb3-3e11-9be0-2edcf93c31bf | -3.50265 | -53.43932 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f884bf2-aa63-363e-af0b-2fecebdc94ff | -2.68094 | -46.83144 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4a6a343-0e18-3717-a9b2-0592198556f9 | -1.35609 | -53.07732 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d968a707-03a0-354a-a143-28f18125a2b3 | -3.60157 | -44.48854 | 2024-11-15 04:44:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8eac2f4c-8265-306d-b31d-cc890fbf61c7 | -3.71344 | -41.69553 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e1f9186-0e8c-3a7c-b226-e65fd1486d80 | -1.85576 | -47.82996 | 2024-11-15 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7839ff25-b33e-340e-9504-6050b6900993 | -3.78976 | -43.91373 | 2024-11-15 04:44:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38f966fa-05ee-3641-af4a-308a65b108e1 | -3.6486 | -52.27614 | 2024-11-15 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 174e1721-3f59-3b5f-81e8-764a49179053 | -2.65116 | -46.1889 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a3b151c-1658-3821-ab2e-eb5628bebc6f | -1.38302 | -51.5643 | 2024-11-15 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 800051e4-8dc9-3728-80cb-03f52a2ca2c6 | -2.67731 | -46.83082 | 2024-11-15 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b97bc1b-f8b1-38b5-8e7f-dd51deca58f6 | -1.98431 | -46.36812 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa6f3abb-d508-38dc-a889-2b053e20d8ef | -2.3869 | -54.64335 | 2024-11-15 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da5fe956-eb1c-3685-959b-8260718d73d9 | -2.64718 | -46.16505 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ee46915-c4c2-3f4a-923f-2dbae9a250fc | -2.82637 | -52.14952 | 2024-11-15 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0ab1a05e-e586-3c45-867b-dbe785bb9314 | -3.70828 | -41.69468 | 2024-11-15 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cfb9238a-0117-3fa4-9c43-2ff5d49f5a7a | -1.26577 | -52.13161 | 2024-11-15 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22532687-dbde-3085-bf4f-ce7f8139eae7 | -2.7205 | -53.19739 | 2024-11-15 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16048df-4415-33ba-a19f-1a6cbf0d6c1d | -1.98621 | -46.36591 | 2024-11-15 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16eda606-0241-3642-8f75-ea66a5f04a03 | -6.04505 | -44.0346 | 2024-11-15 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 427364da-505c-3e98-aaa3-2a6ca27c71f0 | -2.66006 | -46.18325 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b5a9329-8cb3-388d-9f22-1087e6b6bee7 | -3.23194 | -54.15799 | 2024-11-15 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d133d73a-a4b8-3325-a7ef-956dedd72510 | -13.48574 | -60.66239 | 2024-11-15 04:46:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea67c6a0-be07-387b-95ff-49415136a7c9 | -8.83383 | -63.03011 | 2024-11-15 04:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13c2eddc-de04-3634-8336-1a5a22d31773 | -12.329 | -57.75028 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ed41345-6251-3c4d-9410-920c5c077caf | -15.31256 | -56.52782 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15eff9b2-6e16-34d2-88ce-0903552363b1 | -15.31335 | -56.52337 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07e91340-735a-39aa-85e4-a8691c75f8c2 | -15.29601 | -56.52161 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 608557b0-b933-3767-a42f-cfa2ebe44f62 | -15.29157 | -56.52538 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 402abf63-b461-3b12-9ac9-dc1d1b62d763 | -15.62745 | -57.51374 | 2024-11-15 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75e30d75-2660-3291-8986-303df0c3060f | -14.28261 | -57.64015 | 2024-11-15 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f82ddf3-bba9-3ed0-aeeb-32fbfdca4124 | -15.29706 | -56.5296 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48862131-5468-3488-bcc2-868217406de4 | -15.3178 | -56.51962 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| def2b682-24e8-311a-a75d-98ba0e6ee570 | -15.16005 | -59.72111 | 2024-11-15 04:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa7b6723-da22-3903-8a66-cf57090e55af | -15.15859 | -59.71758 | 2024-11-15 04:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc0c457-9337-3dfe-87de-aacbc683f435 | -12.57774 | -57.81743 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9740fdba-3fa7-332c-8283-cd37f60a5c9c | -12.57844 | -57.8136 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47e9bd5a-acc0-396b-92be-9905865310f4 | -12.79476 | -62.01175 | 2024-11-15 04:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06028202-f4d8-3325-a27a-d1b16ef16cd9 | -12.57287 | -57.81343 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d07c0f7f-3c25-3b47-9ac5-02ec0ba22df1 | -15.42395 | -59.04166 | 2024-11-15 04:46:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7df7e93-4fff-350d-803c-4e66eafb219f | -14.28354 | -57.63493 | 2024-11-15 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bd71209-3d2a-3203-abde-46c12e877860 | -15.31702 | -56.52406 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0771740-d652-3be7-aa9c-59bc2b706eaa | -15.31045 | -56.51829 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f4ce0586-f25e-392f-b4f0-8362a28d2583 | -12.57699 | -57.81425 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc863009-a40e-3f39-b4b6-8505ee367fce | -8.83473 | -63.02522 | 2024-11-15 04:46:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3ac1a5c-3cb7-3c71-937a-ac8f832701b7 | -15.30781 | -56.51912 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76f13a18-f792-3ce9-ac05-daa1f2d2def7 | -15.29785 | -56.52518 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README22.md)
