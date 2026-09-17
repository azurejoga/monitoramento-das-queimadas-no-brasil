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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a72717-9553-34a1-9b7c-29dca537fc06 | -5.98128 | -53.58475 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02e52b8e-1634-3323-a6a3-bc7fcddad69d | -6.21211 | -55.27995 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59a1a7c0-c33a-3507-b34c-ca714819431e | -9.71847 | -47.09176 | 2026-09-17 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98a71cdd-8ac2-3493-b275-61a4b24c6856 | -3.37432 | -52.7977 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 670426e5-3e8d-3bf1-8a08-b5e4a4d630f6 | -4.54577 | -54.92865 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e81c0e3e-0709-3a6b-8246-9998d7d09ac2 | -2.7991 | -52.07663 | 2026-09-17 05:16:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51a40ec4-1732-3b6d-9cca-aa5e8fc20876 | -3.24786 | -54.27921 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d29c970-b522-3eb8-9a91-102f974959c3 | -8.69437 | -44.87014 | 2026-09-17 05:16:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b641c6c-d350-3a82-ac6a-77df15f2ab4d | -9.47714 | -47.22923 | 2026-09-17 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 732b1f94-5101-3389-b37f-3abdcb671779 | -4.56854 | -54.90714 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da418286-baa2-3842-ae93-ed4fd770da33 | -3.26225 | -54.26759 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f823cc-b082-3142-b56f-16f76180921d | -7.97261 | -44.83073 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6fd2598-ec26-3e2c-9556-a7550a41729a | -2.96249 | -50.32915 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e04c8f14-fd77-3a4c-81eb-311f5600aed7 | -5.2928 | -43.63431 | 2026-09-17 05:16:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5c219b8-6136-3238-a3c5-b5a8c1abe8ad | -2.96171 | -50.33421 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b8ed59f-a126-39dc-935b-aa8482b07184 | -8.22234 | -55.46288 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f242269f-947a-3fb1-9ad0-31aa90f4fb48 | -4.37416 | -55.02609 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b221e3-4c7f-3319-ac49-89f622956c33 | -8.11532 | -54.80695 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af97d28b-a82d-3b5b-bae2-9851683038cc | -7.71512 | -55.60943 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31ce2a7c-43bd-3914-beb2-314dd2d19cc8 | -3.13263 | -59.01994 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e84529d-3e89-354b-81b2-be58629073f8 | -7.64687 | -44.33396 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eee7cc93-a0e3-3213-bf52-4f4dc771af60 | -5.31832 | -55.85648 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7927c43d-d17a-3d89-a777-a29a5e1779c1 | -5.48105 | -45.12619 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a73f9fa6-8ca0-35f6-86a5-28bc0539fac3 | -3.73218 | -55.94061 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b86e50ab-c58b-315d-ab6b-81f70afaf2b2 | -2.95456 | -50.3279 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06629dba-8964-36d3-a360-7d78315234ca | -4.39649 | -55.44072 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4357d2-1f51-39a8-af68-b66008cdb4ea | -8.4876 | -57.63458 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5643cd76-d122-3c76-ad06-44ba82a4d3e4 | -10.39373 | -46.63372 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffa68091-8072-30ae-a51d-4d286d7e5e45 | -9.953 | -45.28622 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50b35330-afaa-3fe0-ae3e-ac275cf5c552 | -3.14684 | -58.64547 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a61edbd-bba0-326e-bd19-70248edc2907 | -9.77436 | -46.54672 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a70723ba-a5fb-3d78-a644-44e67d3ec523 | -6.99665 | -43.3327 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 40a5a27f-bd65-3d56-b9ab-8d192ae0419f | -6.10234 | -57.6262 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976c1f06-c649-330a-b9aa-7a38c590bc1b | -5.98533 | -53.58142 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7517eb9d-14a1-3eb8-ae97-7b4ad3fcf234 | -4.5269 | -54.91856 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930b5d63-d4a2-3274-89d5-a0307e936f13 | -4.51033 | -54.95864 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5af1251-d59c-3d31-b733-1f81c4f2d278 | -7.02604 | -42.06439 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 616aa29c-9b08-381f-b833-57af66d62b13 | -6.37623 | -58.29045 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cec20a5-4909-35f7-9588-fc3b263c8ab6 | -9.16161 | -49.98799 | 2026-09-17 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1960896-9a02-3dce-80e0-b39d92249841 | -4.55366 | -42.95014 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 433bb946-79dd-32e8-8957-5925d9d2ca8f | -7.30304 | -64.6788 | 2026-09-17 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc966cba-29d3-30c3-a0f3-1842bf981351 | -9.60509 | -45.33889 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3cd25ec-d07c-389e-9c0c-fbdaee1143e6 | -8.48024 | -57.63713 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9c8aa515-30b5-3dea-9480-5499c97f309d | -8.94319 | -44.39541 | 2026-09-17 05:16:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56700157-e3ac-30a2-b5a5-134007d48902 | -8.26705 | -42.17327 | 2026-09-17 05:16:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 550983f1-8dda-3d2a-939a-cbe8d2cafe2d | -6.76259 | -55.84047 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed9d2366-e24e-3936-a556-56bccaf036ff | -6.44331 | -58.14508 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5532d027-2ade-36d4-b238-fcebbee82750 | -9.60306 | -46.65124 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fa40daf-8de7-3a7c-a5a6-adacb31f2347 | -6.4342 | -55.60378 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c4f5e17-ca10-3100-a92d-49d89729e17a | -2.77443 | -51.36969 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db7dc10-c5eb-3ac7-bd96-10b34208d80f | -6.90432 | -59.03468 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ffc047-6907-377c-b17a-d543d9624f91 | -3.21161 | -57.78123 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79acef1d-c79f-3ca5-946e-5783533ec98a | -6.79366 | -59.18545 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52d2faf5-18fe-3d76-aacb-b2c147567a31 | -5.77389 | -45.10746 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| e4914bdc-a27f-3c89-b3bf-87e6ae76c69b | -5.48052 | -45.13007 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e897912b-67f0-345d-ad98-74ed5282d896 | -4.89147 | -55.88127 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94681f5c-d6e6-30e9-9e66-945054e87c32 | -5.64335 | -44.80032 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ef9101a2-c4f2-30b6-89c4-476e81fa2602 | -4.87985 | -56.06132 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f2eb1c-010a-36ce-a0a2-7de4b5cd9979 | -7.94577 | -54.89116 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 581528b7-ae8b-3148-acef-b165881ec264 | -5.14759 | -55.93276 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85b830b3-0ef9-34f3-9003-e1d507155450 | -8.5627 | -44.47731 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01e16d29-dc27-303d-8f08-d7d8de8e0ad2 | -4.54189 | -54.93159 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db212861-5f61-3e12-a693-a80e857224e6 | -5.98186 | -53.58095 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e43556-fc02-3e30-97bf-0fe20dcd78c9 | -8.60764 | -44.49773 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 65ff8064-b5e1-3d92-81ca-cf6cebc1c6e0 | -9.03985 | -47.75974 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36159e35-bfd5-3d7a-8b19-ed41c3986231 | -7.07346 | -47.48887 | 2026-09-17 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d84dde77-07bc-369d-8c83-445e79015e76 | -5.77275 | -45.11555 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 76d5e186-705d-3248-acd9-a757e40b6690 | -4.53524 | -54.93053 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d009366d-1745-3f78-93b5-81ea5f09a6b8 | -4.57132 | -54.91116 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91866195-eed9-3f1e-99be-5f5fb9d45493 | -8.37359 | -54.73833 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37825e45-33b9-3bd5-b976-65b8927028e4 | -3.32292 | -57.85158 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7d8a1ca-1f9b-3f87-8829-54ffb1a7453a | -4.5545 | -42.94442 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c6c3d49d-f466-3ab6-b95a-060751bfd0c8 | -8.46799 | -44.55915 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d63044b-9c6e-3a82-8de5-f1013bd60d1c | -9.8311 | -48.35498 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8942187a-a69a-34ca-92b6-f11ba3f70729 | -5.63676 | -44.80377 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d80f541-97f0-365e-8aa8-02e7193218b3 | -6.3533 | -51.77838 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30c0e9af-529e-33d9-bb9f-685ef5f58941 | -3.44836 | -58.42111 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a30bf784-f3f8-3dde-8a8e-bb095cf54c50 | -8.60619 | -44.50895 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 71e17a79-1bdc-390c-a8c7-228fc138cc9d | -9.10649 | -45.7252 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 7d4ae54c-16d2-3eb8-b857-cd9ac4b0a03a | -6.81899 | -59.16708 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8316fdc2-3191-3678-9f10-31f358cd6d81 | -3.48214 | -54.72257 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b0bd5bf-984c-3f50-9697-e0d4c7b38b96 | -6.50178 | -58.38228 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e99341-9ff3-33dc-b28d-124344e538f7 | -7.04029 | -42.06762 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64b6f513-d8eb-337f-ad37-0eb97d505f97 | -9.6211 | -45.35583 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de7aed79-eaea-31cb-ab13-e3a485b2cf5c | -7.13798 | -42.17225 | 2026-09-17 05:16:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 13155fa4-7aee-33ee-aefa-13c4f21d3f78 | -6.36856 | -58.29322 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 823f0da8-760a-3da8-b785-2b513d1b474f | -3.54286 | -53.98956 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56dd7f9-e800-335e-bb4d-9251f8145e41 | -6.36569 | -58.28872 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 869887c1-7cff-3281-b10a-e17115e2f978 | -3.94703 | -52.2188 | 2026-09-17 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51773542-58f1-3ebb-90c4-3bb7b9465485 | -5.89074 | -52.09142 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56515cc2-b0ac-3087-806d-ba8cf2616647 | -4.36572 | -47.78068 | 2026-09-17 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b031fa8-0f5d-369d-b77f-88c8ba4c4201 | -3.08228 | -50.56474 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3baf7ca5-6645-35b0-93ad-3c821ed16a13 | -10.61006 | -46.09306 | 2026-09-17 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8f7a361-5b01-354e-a808-b85947fe174c | -7.09143 | -41.84872 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| afe05753-f77e-315d-95c4-7c46a8fc4033 | -6.4312 | -60.00846 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10ca3588-c1fb-3da4-a0f8-9903c27bbae0 | -7.0932 | -41.83471 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 89a710c0-d3c9-3426-a103-fd4ba5a245dc | -4.5741 | -54.91513 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae7c0d3-bf00-35da-816b-0b13dceb7766 | -4.18526 | -49.4057 | 2026-09-17 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac85680d-250b-3617-99f6-a6077b026309 | -5.91176 | -59.9367 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bf6744b-e3aa-3edd-9230-830008e63a32 | -8.78639 | -46.9035 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README60.md)
