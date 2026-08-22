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
| 2dfe3954-29ed-3496-8483-264becec09b9 | -6.879 | -59.43055 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f7e0b7e-606c-357e-9a40-9f1b49dbce2a | -10.53095 | -50.80074 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 491958b6-8861-31df-bfaa-0a481bcc9eca | -6.69569 | -58.93601 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e2f9545-bd96-3997-a9ad-76c583b4bcbe | -6.25707 | -55.41477 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4e3839b-7583-330e-9335-0dd44e768f0a | -11.38336 | -47.20407 | 2026-08-22 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c6df4f0-bd14-3e1d-a6d7-8ba6121d564e | -8.62827 | -54.68516 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d962760-456f-3d42-b9e8-067377956f87 | -6.09164 | -59.95874 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34e87afe-5226-3873-8219-bc51da40ec09 | -14.14241 | -48.06585 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d545413b-d3cc-3cc8-bf42-c9d13263b955 | -7.48605 | -46.09715 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 805458c6-309e-37f7-b840-c9c0b3c70892 | -9.33454 | -42.44891 | 2026-08-22 04:27:00 | NOAA-21 | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c12898e4-8a72-3076-bc64-4bf948f82a96 | -7.69862 | -46.15144 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9150b8cd-32da-36ce-8695-687cb3e9f5bb | -6.78697 | -59.43915 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 411528f2-686c-3114-9006-a8ded4ac3311 | -6.81224 | -59.40153 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e69b49d8-dd9b-3e94-9a5a-e737e40959ff | -6.25471 | -55.39749 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbf90355-0fc1-3f2d-93cc-17d3a47dd4f1 | -9.16485 | -59.45849 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cf73e26a-d3b6-3000-85da-a09748b66888 | -6.75406 | -58.6563 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b0ae6d24-6c23-39c2-8363-727108e2fcca | -10.53098 | -50.7784 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c9cca19-6fc0-39e3-8f25-9f95719ef379 | -6.81296 | -59.41234 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1282069a-8252-3c9b-ab4e-4eca4ca5c8b8 | -9.43883 | -51.62109 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bc886f2-fcb8-3e40-b214-9fafa15007df | -6.80783 | -59.42553 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fbd9b57f-8d35-380f-853d-7aa6b209411a | -10.80923 | -50.98052 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| eefccb19-188e-3377-92c2-a8dc63d370e8 | -6.96877 | -59.05669 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 132c835f-bc5e-31b3-8cfc-0a14f460af86 | -6.65999 | -56.33869 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12098a91-e4b2-3577-8846-a6230b84d532 | -8.52264 | -54.82837 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 68cf831f-20a6-3214-bbeb-0eb4ce594c9f | -6.78019 | -58.66309 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2e96ada-736b-3529-b570-dffdadabe88d | -6.79764 | -59.59555 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eb06e0dc-40cf-3935-95d4-b63275497545 | -8.15395 | -46.72166 | 2026-08-22 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc090fe6-4d03-30ee-845d-d3ba2a86be90 | -6.96839 | -59.05218 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eec29088-a94f-3e2c-9c45-9b029f015199 | -6.10914 | -53.07542 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0d5022d-2b5c-3ef4-bdf0-6771ba97b7e3 | -8.80811 | -48.54914 | 2026-08-22 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d47d0fc9-5629-3b26-a4e0-48d8a3833eac | -8.54022 | -54.81466 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7dae6806-d2a8-3e49-be58-4d12a2020ad5 | -6.15285 | -57.74503 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a41bfbec-6a09-3214-b83c-f9dbb0dad7c4 | -9.04866 | -57.07363 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8238753d-5100-3d63-a1d8-1ff51bd93e05 | -7.36596 | -55.68434 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 364890ca-f777-3ce3-8672-0b3aeac22755 | -9.16268 | -59.46944 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a920c538-c712-34fe-bd33-de2ebe195207 | -6.25729 | -55.4188 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf4943a2-0bfd-3917-a334-33518442ae55 | -6.79908 | -58.63274 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c02526be-78ee-3fec-9e2c-9add3c3a027b | -6.38144 | -54.95117 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4addf961-15fc-3f7a-a1b5-413274fd933f | -6.3784 | -56.10276 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 804f2d8e-332e-3016-a945-d9b7e317951b | -6.43119 | -54.95463 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 196279f2-d111-3c9a-bd7c-29a211897fb6 | -7.81506 | -46.84538 | 2026-08-22 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797080a5-c94e-3c21-969d-d56bf992c430 | -12.27183 | -43.17653 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3ca3683d-d961-368f-a89c-6b76b8bc90f8 | -9.05157 | -50.87342 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 534ccf9f-242c-3acc-8a4b-f61e3e76bc49 | -6.75923 | -58.70158 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a3a9a7-e6dc-3ace-a674-d09912ecf1d0 | -6.90394 | -59.00449 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2ebddfce-1b5c-3419-96f2-5a436cd72aad | -12.26404 | -43.17543 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a82f331d-a2e7-3086-aa1f-5884cbd07006 | -12.75912 | -47.11929 | 2026-08-22 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd8b4fa-153c-3c3f-9fbe-45f09afca2ed | -7.513 | -47.64152 | 2026-08-22 04:27:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21ee1504-9a52-3dc5-b3a3-432dbf3e2b8f | -6.78765 | -59.42188 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6395291f-a116-3b9e-8833-0d28e7f8a209 | -14.1369 | -48.05769 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19bc9343-87ff-3d62-b3ae-754e27300e74 | -6.86607 | -59.03349 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| feded8b4-9600-3b98-a658-22e7c894cd8a | -7.47678 | -45.14312 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b771edec-baee-3176-8e93-ccd43cffda5c | -10.51573 | -50.82644 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04e8d4bc-a8c3-32fa-8394-289f44ee4d52 | -6.08458 | -59.95773 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34f38bba-a802-3c61-867a-3554941f9181 | -12.83903 | -48.46149 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c66f04a4-9842-3fb5-8389-3e97a35a01d7 | -6.77535 | -59.45078 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e77cedad-9871-374a-9273-323978289b4c | -6.25838 | -55.41243 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1c9d746-abf2-34a8-8735-d41782398300 | -10.27785 | -50.38559 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e98753ed-f761-3cab-b656-ef10113ee01a | -7.34727 | -55.66696 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6389b3db-865d-3a4d-b6b3-7254a62a15f5 | -6.77753 | -59.439 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5cc30689-6b08-379e-a1f3-ae377068743c | -6.91502 | -60.07283 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8b673f6-ed88-3f48-9c44-b53427486abc | -12.25489 | -43.18422 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3360a46b-3d85-3958-8e8d-d28b41622f94 | -6.22657 | -55.61693 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3f999e23-993c-354d-87df-8574811718b5 | -6.8033 | -59.41235 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 913dc408-7cd8-31ce-9a4d-309cb2424ea2 | -8.5802 | -54.78781 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ab1208e-f238-3a1f-aead-6b8e25be7ec2 | -12.77225 | -48.3889 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 13ecd944-fb6c-3137-acb5-8baaf132a150 | -9.45092 | -51.59706 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64cab744-8ab5-3305-9446-4325f83812d2 | -13.40025 | -54.36309 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41c59135-7f47-32d3-9085-91eab9ef3f36 | -6.80582 | -59.67186 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf83247c-99dc-3f1f-af69-c93ede682e35 | -9.00124 | -50.75165 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| defdbcef-1cf1-32cc-88cf-c944ae2ff08c | -6.22595 | -55.62041 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 17f4dcc2-8b30-35e4-9b7b-aa71496a433f | -7.33192 | -46.23637 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc2bf17d-0cf7-35a0-a0d9-e7cc4350093c | -6.25143 | -55.42128 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61431f0e-206d-3564-9ed4-52cbffe3d63d | -5.9975 | -57.80322 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c75e0e9a-a65f-3f78-8630-d1fd9321f4e6 | -8.19061 | -54.97905 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 397648ad-5219-3af0-b940-59c2dd4670a5 | -6.43251 | -54.95999 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e5dbb8e-da5d-3811-a519-81b7d5e26824 | -6.01259 | -57.82592 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d8f1b5a-3743-31da-bf52-bbfeadd5d5cd | -10.52078 | -50.77209 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74796c7e-6c7c-3c98-99ce-62b3f327fd46 | -8.53125 | -54.82233 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d5fc10f4-0323-3d5c-b29f-4ed678a294b7 | -12.74292 | -45.89552 | 2026-08-22 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457c1ef1-40f4-3281-a99f-9c26b2ea9fb6 | -6.93246 | -59.31193 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cfb5f40-66ea-3cb2-9a67-1d4ec5e95a4a | -6.41893 | -52.73245 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea2cc59-06bc-361b-834f-622a9bda1ec5 | -7.69101 | -48.423 | 2026-08-22 04:27:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23d5ec6c-ea90-356e-9c95-aa9caa140001 | -9.39462 | -55.98242 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| affd201b-fda8-34dc-815c-c894878bcaa6 | -9.79461 | -46.62129 | 2026-08-22 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 384fa856-a04f-3b57-b33d-f8b91f702637 | -6.38197 | -54.94812 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32917bec-d857-37e0-b795-6ce0a17bb049 | -14.15161 | -48.3544 | 2026-08-22 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8f045d-8542-3b12-ae5d-5b62ab8d6415 | -12.23677 | -43.17158 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c0df9e57-63ed-3634-a9d7-c80f3b304ffc | -8.03042 | -54.02359 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4e5a324-9d69-3afb-8365-a2b4d4b14b8a | -12.06351 | -56.2944 | 2026-08-22 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c7d84c-b602-39cd-a281-b031bdcda933 | -12.7521 | -48.47291 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 054ad554-b54c-3512-b8aa-d2d5d97d733f | -8.5207 | -55.32694 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5421133b-2b9c-32b5-9443-aab41d4e32c5 | -6.7916 | -59.41501 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| feb74034-d87e-3b1c-8c32-27b424edd1fc | -10.39413 | -50.42967 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a26c7c64-6d82-3983-a0ff-58778657477e | -9.04934 | -57.06993 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a241f3e-346a-3931-bf9e-f677ebe023f9 | -8.54401 | -55.31279 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8479cfe3-56a5-3c5e-8654-12d9a74a1d38 | -12.78552 | -48.39108 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb93db00-9cd4-3e33-a9ef-fe8900002264 | -6.80893 | -59.41955 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8373f0bb-c25f-305c-9d16-0e7286858118 | -9.17043 | -59.46606 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 63728b24-0ccd-3d63-a299-a7ef08412bda | -12.82516 | -48.46311 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
