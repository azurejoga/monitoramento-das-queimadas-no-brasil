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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b476e717-4388-3869-a7e9-3fd6455332ac | -8.73328 | -45.16095 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76d79e1f-4609-3ecb-be3b-7e0331e262e0 | -3.51033 | -59.3317 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43360ba0-219e-3118-ae1d-34959dc21b67 | -3.54035 | -59.49641 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a85c4f5-c728-3dee-bb6b-a4786fd508ee | -3.25845 | -54.26198 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa01a867-a138-3c7c-b1d8-c550ae6bc8c0 | -1.37917 | -56.895 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1601b287-d8a2-3b8a-89ce-257fee5d5eca | -3.02864 | -53.93439 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df19fd72-7654-3b2f-b3df-d6a6014efa29 | -4.8526 | -42.83329 | 2026-10-08 05:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a8af9d0-c55d-31e4-9eb6-bba43fc587c7 | -3.29379 | -54.03759 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7101e906-7938-3a4a-8521-38e6b0e2d68d | -2.93452 | -53.9361 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172b252d-2d73-3882-9f72-78444dfb1854 | -6.11739 | -51.95576 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37c405cc-4e94-362b-89b5-ce811b845e49 | -11.35831 | -51.87774 | 2026-10-08 05:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12fe1f16-5a4d-3ce8-9b37-5ed4a3c8a29e | -2.86617 | -54.16474 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c0859846-d250-3c07-bf79-fa7749813bba | -4.66393 | -56.21883 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 535c6dd2-e8f8-306c-87d4-7f08d3e95d64 | -3.39778 | -60.84081 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af344ebc-e3d3-38e6-9e70-396e0ef9fa12 | -8.61787 | -67.0266 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b4c29901-5268-37a9-b567-bf90cf0c1c32 | -2.7882 | -51.67702 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf8e312-900c-35ee-9e30-d836705075de | -3.08433 | -54.29449 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fbb83fd-37b7-33e1-b0d7-b7d07bfd99d0 | -10.62664 | -53.83934 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d05714ab-ff3c-373b-b1fb-31710ae82d85 | -9.20443 | -66.09528 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 729523e0-948d-3e99-b0f3-fb228cfdc337 | -3.16391 | -50.44247 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db138b29-b930-37fe-8a7f-e44ff00f0c81 | -2.99115 | -54.06057 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74ac364d-636c-3c39-bd12-9fa62d27e392 | -4.5803 | -54.93082 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 637e1498-9699-3f66-90cd-ca6bd9a01f2e | -4.92665 | -55.85961 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f383bb5-c475-30b6-a83f-5ed17a04533e | -6.95495 | -51.92304 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dda6a4bf-e29e-350d-8cd2-c3365c64d3ef | -2.89887 | -54.02658 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 499d6144-7a26-3e40-b5b2-1713230ff177 | -2.50027 | -56.16701 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f51c2296-02a7-395e-8019-803db6a50ba7 | -2.84957 | -59.10987 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e92a7b9-1e45-3315-a2a5-744505b88a07 | -3.06446 | -54.37662 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c31965-17be-3e92-86a6-a7543d7afbab | -5.30062 | -60.09647 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b276bd17-88d5-3075-9bfb-e6351cd92666 | -3.92561 | -55.85575 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b978a1e-c4c2-3f15-bbb8-c0c28b617d57 | -7.25463 | -48.06549 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98d0355a-f809-3be5-9a15-0a635c1482c3 | -2.98742 | -54.13128 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117dc930-818f-3c5a-a0b0-185d560e1b91 | -3.53651 | -59.47509 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be21a7d-5b3c-3ca2-a461-1c4c576455c7 | -3.56087 | -59.48314 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3da50583-5bf2-32dd-8761-6aa7ebb5cbb7 | -2.47964 | -56.10356 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69f2ea76-fbf5-3c0c-858b-2803529586b5 | -3.58983 | -54.56723 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23cd4112-05ed-379e-9c8c-9aa29b611043 | -3.05934 | -53.92308 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d77e44d3-6cfe-3d1d-b1b6-0d2c810f2850 | -3.59133 | -54.67111 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fce41a7a-9f5f-3f51-9f6f-a6f2cbf83bdb | -4.36536 | -54.74155 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba03beb0-21a7-36b2-8912-92491c62f68c | -3.56696 | -54.22461 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a9148a-f51c-36b4-8ba0-d37fa81b6ff5 | -3.10351 | -54.28577 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c94de8e-fdec-3662-911a-8a74e7a37805 | -3.84599 | -55.97986 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4319ac24-59a6-390a-a056-d560309fe642 | -3.59558 | -54.57586 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b335ddfa-24b9-3727-8237-f5781381ea82 | -3.14087 | -54.36547 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1016749e-36af-318f-af7c-55e8806719b2 | -3.41141 | -58.91296 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cdce2b4-74b1-3617-807f-5d19cab56611 | -3.26254 | -54.67469 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f40c093f-00fa-3c11-b8f6-ce760e4fb611 | -3.72336 | -54.21649 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41e7e76e-a456-3852-80b5-3dd1264d708e | -3.65208 | -55.50948 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2cd22a3-571c-3d22-9635-b2382eff2a01 | -3.00681 | -54.09871 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b21c14a4-f340-39cd-95d5-c652a81ce310 | -9.13995 | -65.29943 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 530a88ac-bd28-32e8-a348-4d1c49f64b64 | -3.55014 | -59.48141 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed2a5a70-a892-3faf-8fba-b45e07aa0767 | -2.99825 | -54.0378 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb168801-0968-32fd-be52-beee37624ffa | -3.95994 | -56.11543 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c83dd196-5b35-37cc-b9e0-1ab1ab9ea96e | -1.77064 | -55.06569 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fba29084-006d-33be-993b-c89492cdb016 | -3.08683 | -53.95545 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 1200d849-279c-3543-b128-47df62f3941e | -3.0792 | -54.25852 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4731041d-9fdc-304f-bdd9-5d796058043c | -3.50792 | -54.62429 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2152dd6-a4cb-3a8b-afad-b940813c50bc | -10.6663 | -58.92846 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea9a38f0-485b-3227-9789-5de1eed6ae9e | -4.65725 | -56.21778 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4984999-1b45-3637-897d-9f4c7e7c05a3 | -13.17466 | -54.3233 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 098187b7-e2f7-3684-8c6a-4bd4a5eeabb9 | -8.59759 | -67.04709 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3c0778-4577-3b6b-9f3b-59dfcb9d025c | -3.04509 | -54.26575 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 04cf34bc-cabf-38ad-b1ec-34e862661f42 | -3.65259 | -55.46216 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40b6b0c7-6b9f-3509-a147-9db9fba1397d | -3.84695 | -55.8653 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 053c5ae4-5d6c-3581-9286-1b6a3c57e4b9 | -3.04229 | -53.91636 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e35a19cc-a77a-3c37-b46a-79abee078278 | -3.52272 | -54.6649 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e78ef79-221c-370e-b534-ce65da527376 | -3.2441 | -56.80848 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d220f2d-3310-3ec3-aae6-6607c7db156b | -3.01743 | -54.07658 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ae70fd0-f87f-3360-a48b-8fe9fa121ab0 | -2.56963 | -56.15292 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1149bcfb-9cb1-3ee1-9cef-f9c06b552e04 | -3.00621 | -54.10256 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0dbc04b5-4527-330a-9170-65b667e41676 | -2.9998 | -54.09761 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b5789734-315f-3593-9396-653913be7bf4 | -3.08291 | -54.39507 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 487b1ac0-1db0-37d5-b106-1fd8add226f3 | -2.97989 | -54.11036 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 21dc7146-8f2c-3c30-9006-a58b60035602 | -3.32871 | -50.18296 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50ce309a-74ba-3ec7-a0aa-6b4dadde42e0 | -7.18673 | -52.61702 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efc204c3-566c-366a-b223-e01d655e5f16 | -7.22254 | -55.09262 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 10355806-221e-33d3-98a8-bd7755229bd3 | -3.8466 | -58.89769 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bebe63d6-f19b-31c5-9459-791bcff0001b | -8.61705 | -67.0164 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 077a3811-4259-3c1d-af1c-2a77a42caa8f | -7.22075 | -55.10419 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e715c2ad-7e92-3906-87d4-dac67c400610 | -3.09619 | -53.73344 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3269650-b227-3837-866f-f957f4814077 | -3.06851 | -54.37341 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43d79ad-093e-30ec-afac-2cd7715ef082 | -3.17937 | -58.63115 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cdae03-b9d4-35b3-9a3b-1fa9c821bb82 | -3.70904 | -58.54876 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77e75145-2c0d-3529-bbf7-70167586e019 | -3.59499 | -54.57962 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5108f8c-fd1e-3019-b400-9fa6bf1cbabe | -3.98733 | -59.21478 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ce5f41a-3ef1-37c7-bf09-30c0ca1fea50 | -6.63389 | -43.73119 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 36fffe74-3cbf-3f8b-a79c-81bc408eef28 | -12.17066 | -53.2328 | 2026-10-08 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa24e94-0c56-3444-97b9-4fa5fd01b888 | -2.9574 | -54.13462 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 275da9ab-6822-3fb1-876a-027f00649965 | -2.98539 | -57.20194 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f4e901-64b5-3a32-be8c-1acfbe6c6cec | -2.77033 | -54.09091 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6d666cb-05d1-39da-a040-8503a72d90e1 | -2.50633 | -56.15025 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb824706-4d26-352f-9f02-62c269f8f297 | -6.72456 | -55.12539 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26a28051-257f-31d3-8151-27a5a2e98b66 | -2.46465 | -56.09058 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff2862f5-7e0b-3a57-a249-fde3cc2d6e2c | -1.46067 | -54.76972 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 057419b9-bbdc-3fdb-9b78-419ed323a7ae | -3.53532 | -54.6745 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c1ff36c-92d9-3245-8743-348374818ad6 | -1.11437 | -54.09319 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3251e162-a104-35d3-9d14-319836c6ed4d | -2.77621 | -54.07604 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40dd77fc-6d27-371b-8b00-7a0df2dd4c5f | -1.77512 | -55.05912 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d796b2f-305f-34d8-be7e-7b1f68a39e99 | -7.22366 | -55.10861 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3062aa60-f197-32b2-a9d1-3156eb9ce9f9 | -8.60069 | -67.04459 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README139.md)
