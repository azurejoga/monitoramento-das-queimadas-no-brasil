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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90144d39-a1d6-369f-a5b1-5013592fbb74 | -9.61201 | -37.04556 | 2025-05-10 04:19:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5e1da90-2170-3f45-890f-e06564d702e8 | -7.07313 | -44.3879 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfbbef75-8583-355f-af14-5c13b41312ac | -7.07644 | -44.38841 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1a05308-8b6c-391c-a452-dd05b98b41a4 | -6.51016 | -44.72379 | 2025-05-10 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2f6780b-2e0a-35a0-9a35-019557aae107 | -10.97525 | -44.43544 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d5fc8f7-0497-398a-90e8-324509628c3d | -10.61534 | -40.48051 | 2025-05-10 04:19:00 | NOAA-21 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9607d5a0-b413-3e39-8169-a26e705f812b | -7.08797 | -44.37954 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67f82660-7ca1-3fbb-95dd-5102cb21d893 | -7.22279 | -44.25544 | 2025-05-10 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a40fdf92-443c-30d3-b51f-176d79cb56e8 | -8.31331 | -48.04942 | 2025-05-10 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a42f14f-61f0-385d-a9fd-733916c6fd9e | -10.99426 | -44.44575 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99f07217-5dde-3d78-98f6-83a1fa50fbaa | -7.07367 | -44.38443 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1eeae3fd-fe75-377a-b08e-14bc018e8d42 | -10.99091 | -44.44524 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e055fb15-f577-3572-90da-8f668b76533b | -10.64232 | -44.47972 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68ea7b45-206f-3478-8c58-46c046a8f25a | -7.0852 | -44.37556 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a94eedc-dd63-33d5-a40e-83bcf4543607 | -9.29996 | -40.63182 | 2025-05-10 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4545a27-f12c-376c-a496-4bbca5e11a5a | -10.64178 | -44.48331 | 2025-05-10 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40739d73-b0df-37bd-a87e-a5b7103b04d8 | -9.67049 | -49.71236 | 2025-05-10 04:19:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b622f870-baaa-34e8-9ba4-a2969f662ef8 | -11.15508 | -48.67559 | 2025-05-10 04:19:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67e33231-2233-3a89-9d46-1fe8a94c5836 | -6.5107 | -44.72034 | 2025-05-10 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02536884-073b-364b-ba1a-854262a15386 | -9.84621 | -44.68539 | 2025-05-10 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c15f7b9a-6994-3bf1-9f44-6bb58d87a0e5 | -10.73532 | -44.85033 | 2025-05-10 04:19:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34d289e-a7e5-3cca-82ee-5c59b0f90a7a | -6.31828 | -43.37729 | 2025-05-10 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f58bf5bd-a8e1-3563-b40a-6496843c21e5 | -10.4932 | -42.4059 | 2025-05-10 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e8648bc6-eb51-34d0-a3fb-fbf7d167120d | -6.31883 | -43.37374 | 2025-05-10 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9da2bf25-0893-347e-82ff-e161d9cb17bf | -10.98476 | -44.4406 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eeb65e2d-306f-32b5-9e74-a7480d59859a | -10.64457 | -44.48742 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd59fd23-fce2-3267-a36c-9d53108809ca | -10.98195 | -44.43648 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3438ea84-077b-36c8-892a-b43c7892b7a8 | -10.4938 | -42.4017 | 2025-05-10 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 733d9377-7ce4-333d-9096-42110198b382 | -8.89587 | -44.78273 | 2025-05-10 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 220f31e1-8c6f-3328-9e66-2e8eeb848da8 | -11.14796 | -48.67442 | 2025-05-10 04:19:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58163c82-199e-362a-aac2-f94d3e56bae0 | -5.7945 | -43.61796 | 2025-05-10 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd595881-4560-32ec-b0b0-d97e92e1c506 | -10.99201 | -44.43803 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68162c01-4907-352e-bbcc-fd8f77ba68eb | -10.9719 | -44.43492 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9df0bd7b-b925-314a-a825-9e52e82a77cc | -9.61241 | -37.04262 | 2025-05-10 04:19:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30acaf60-b04b-33eb-a587-f92654039fff | -5.10306 | -44.80057 | 2025-05-10 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c5df1f-083e-3e18-9d8f-3924ed58363c | -10.4974 | -42.40225 | 2025-05-10 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3227d438-ac4b-3ee0-bbdb-649ae70b9991 | -9.92159 | -37.17627 | 2025-05-10 04:19:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4be8f65-1675-3551-bb64-56c9c097d1e0 | -8.47283 | -49.61511 | 2025-05-10 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ef82e98-5ea5-38f2-b741-1a098332cfb8 | -5.1036 | -44.79712 | 2025-05-10 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbbfef7f-d51e-37ac-8df0-d9164b5b4c9c | -10.65234 | -44.48131 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2bb91c21-53b9-307a-9ecc-18fb325110cd | -10.67151 | -44.37776 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be72230e-fa73-3304-ad44-b7b16e263b31 | -9.9166 | -37.17539 | 2025-05-10 04:19:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b409a04e-dad4-38d8-9b4f-acf07dfc9a9d | -11.15083 | -48.67912 | 2025-05-10 04:19:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a1a5922-532c-356a-94db-a15a3ea632b6 | -10.97471 | -44.43904 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64805565-47ef-3ebb-8123-c5067e8655f8 | -5.09922 | -44.80351 | 2025-05-10 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f43d09b-9ad5-32ca-8a34-b7654a2123e7 | -9.91663 | -37.17503 | 2025-05-10 04:19:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e7d0e1c8-9fba-36ee-8721-1588ad57e2a1 | -10.97136 | -44.43851 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99926cda-e2e9-3296-818f-f14644b64588 | -10.98585 | -44.43339 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d107361-6cc8-3664-a8ab-778e616616f8 | -7.0819 | -44.37505 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bf0ca2e-e3c7-3af7-a439-2e2028f93907 | -7.62145 | -46.47644 | 2025-05-10 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f99e47-1014-3f4b-9bae-d3fe071177be | -7.05814 | -44.35363 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40174b06-ec69-342c-adce-98a4fb58be89 | -10.4926 | -42.4101 | 2025-05-10 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 686b04b1-a20f-3a83-98cd-bb4adf44dff6 | -7.07421 | -44.38096 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4aa34596-1b20-3072-a28b-37dc759f02af | -9.84289 | -44.68486 | 2025-05-10 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47a61401-efeb-379f-ab7c-3ca7b10a3a3d | -11.14727 | -48.67853 | 2025-05-10 04:19:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72775768-b5cf-3474-b9e8-bdf9571371bc | -9.85007 | -44.6824 | 2025-05-10 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d3f762-62d6-394f-8cff-9cce84600ade | -8.47125 | -49.6175 | 2025-05-10 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 60298cc9-45ee-3f92-98e9-87ac5bd7a25e | -9.17175 | -40.93381 | 2025-05-10 04:19:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 819cc115-6f08-3cea-aba3-7342a3b468ac | -10.98866 | -44.43751 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a98e28c-1744-3b3c-8370-5a63a453de95 | -7.08851 | -44.37606 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0deff1fc-1a25-315b-92f5-a025acd5e8bc | -8.89534 | -44.78621 | 2025-05-10 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceba1779-41d2-3a60-91c8-e6121207a80b | -10.98811 | -44.44111 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5279e7da-3bc7-3a03-ac08-2a15ec064248 | -9.61181 | -37.04533 | 2025-05-10 04:19:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad5206c4-4277-3bd6-8884-b96f3dc0eaa1 | -10.9853 | -44.437 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac84895c-a2e4-3c24-b1e8-8fc06aaf29c4 | -9.64115 | -43.11628 | 2025-05-10 04:19:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d0e36b20-3fc3-3610-8f42-449db894e9c8 | -10.99146 | -44.44164 | 2025-05-10 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b17ddc1e-1427-344d-b8b5-43dab33bc7b1 | -8.31619 | -48.05409 | 2025-05-10 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1da404e8-efee-3e7d-a05f-a6a9d4903867 | -7.08466 | -44.37902 | 2025-05-10 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0038e88e-5198-351d-9c6b-79420d54cb64 | -7.62424 | -46.48061 | 2025-05-10 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41c89183-cc4d-3655-a3a3-57bcc680f786 | -9.92162 | -37.1759 | 2025-05-10 04:19:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c62663c1-e580-3e89-87a7-99110a244cd5 | -11.15152 | -48.67501 | 2025-05-10 04:19:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ad55af1-df67-366f-84d0-ca4ddc97425d | -10.4968 | -42.40645 | 2025-05-10 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 219a3b3e-f707-3892-b4bf-7b345ceaebe0 | -8.07337 | -43.12418 | 2025-05-10 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2691333e-5ed9-3848-a697-73fe6a8baf04 | -13.05356 | -53.72253 | 2025-05-10 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b92bedee-e729-31bf-bee8-627313b6db3a | -11.61367 | -48.12236 | 2025-05-10 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e0ca68-3c0d-3a4c-81ab-50380b897323 | -17.74836 | -42.89573 | 2025-05-10 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49224b27-c575-378f-8dcd-ca8bef8abdd7 | -13.04326 | -53.72564 | 2025-05-10 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 21cfa3dc-9138-3af4-812b-dbe06140c629 | -14.64645 | -45.12102 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e4f99b-6f21-3e1e-8855-413458048394 | -17.53272 | -52.12049 | 2025-05-10 04:21:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c66852cf-7a8f-3daf-843d-07ddb99536e1 | -13.40426 | -46.79636 | 2025-05-10 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3981d51d-9020-3a87-abde-de80a5eb4232 | -16.60746 | -53.40044 | 2025-05-10 04:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5efd3a2b-bd93-306f-b984-3416c02f3d2f | -11.77653 | -48.6968 | 2025-05-10 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc083e73-9f3e-3165-b0fa-72e6b792aad7 | -15.07843 | -48.94292 | 2025-05-10 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9143394-800f-3a18-a07d-33d2743f9df5 | -15.56998 | -47.85574 | 2025-05-10 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 241a8e1e-9e8b-3061-8ed3-c4dff3502586 | -12.11165 | -47.97987 | 2025-05-10 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dca9d34f-ba4c-3b13-bde6-70bd616577a7 | -13.9741 | -56.80903 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00200fbc-1b76-330e-bb64-930d490221d0 | -17.77953 | -42.80981 | 2025-05-10 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ba44102-4120-3297-b7a0-b7bc39bc318c | -11.14494 | -54.22842 | 2025-05-10 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82c85d33-4f82-3f71-bcfb-a94bbfb7ffb7 | -15.608 | -42.65196 | 2025-05-10 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d524e750-d26a-320d-a32f-afbc73c897a8 | -11.773 | -48.69621 | 2025-05-10 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 368c2c0e-bb05-307f-aefe-d1d1a5742435 | -14.64664 | -45.13248 | 2025-05-10 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0057e456-988e-3163-b7e6-f3281fcb7aee | -13.98609 | -56.80772 | 2025-05-10 04:21:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5ae4af1c-e618-3981-b778-dd97d0c65cad | -16.60394 | -53.39537 | 2025-05-10 04:21:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 9b55a314-3d1b-3de8-aa62-386eacfd572d | -16.04447 | -43.8108 | 2025-05-10 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c013e562-f3db-3962-88a0-3c17d76134cb | -12.68965 | -58.15123 | 2025-05-10 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca6283c-0204-36b1-b8cc-3b93d53f8263 | -11.37512 | -55.12421 | 2025-05-10 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b8617a1-db05-38f9-94b4-8bd565fd5a3c | -11.14366 | -54.23112 | 2025-05-10 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3dd9e32-4cfa-332e-b6e9-5b9fe11907ac | -16.11252 | -47.551 | 2025-05-10 04:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e0a5a3-cde9-3277-82fc-13bb53aa17e0 | -12.11446 | -47.98418 | 2025-05-10 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 768f7f3a-fbf0-3698-bdfa-66be10aa3222 | -13.09186 | -52.29345 | 2025-05-10 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README4.md)
