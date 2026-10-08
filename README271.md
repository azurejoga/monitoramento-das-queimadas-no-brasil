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

## Dados Diários - Página 271

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385a0d92-b371-332d-aad0-6b4126f446c5 | -11.86033 | -47.40087 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6ea0a4f-1bcf-3f37-8dcd-78f96a204014 | -10.64668 | -41.20588 | 2026-10-08 16:18:00 | NPP-375 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b05dee1d-bf4a-3b75-836a-e3698b24cbfb | -11.32569 | -39.4854 | 2026-10-08 16:18:00 | NPP-375 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 184cb631-e8d9-37f6-98a2-c682b287e417 | -13.37164 | -43.88354 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 72211995-932b-3fb0-ae5d-0ed6a498d4a9 | -8.87818 | -48.10104 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 5ea17988-5b08-351d-abdd-2b52577e5e13 | -8.77779 | -47.26583 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cf31d4d-6ac4-3da8-b8d2-811cac25d60d | -10.3342 | -43.6115 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67f6bf0c-6c30-32b7-9f29-7312eb342763 | -8.73928 | -37.33786 | 2026-10-08 16:18:00 | NPP-375 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| baf76b1e-5db0-37c9-979f-de6467e1355a | -11.08532 | -44.01255 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8f2c47c3-6bac-31e0-87af-cb8541a8b6d9 | -9.43449 | -41.7428 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| a08b0016-846d-3dc8-8306-9d5e7f522469 | -12.24159 | -44.7326 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b2d4239f-61b8-35f7-b838-d0f82fbf9ede | -10.44876 | -47.2934 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a96687b6-6317-32a7-b21d-1cde7d878c69 | -11.4477 | -43.39282 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| bd5b91e5-52f5-3b0f-b57c-430a58aab1d7 | -11.51947 | -48.22531 | 2026-10-08 16:18:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a235c6d-44d9-37ee-8faa-952f2beb80c0 | -10.4374 | -47.28795 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9995b392-dbfd-3fc6-9c1a-c23f37ec7dd8 | -11.85377 | -43.53239 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a19aaeb1-d9e8-3a53-9d85-5647af8c636b | -9.89996 | -44.79789 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7cadc4e6-daca-3bf2-8f8d-ae8b34db9103 | -13.14031 | -46.35918 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a93939e5-da93-3c98-addf-a3aa44c19e8e | -11.38626 | -47.72823 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2400017f-9c5c-358b-8894-808d5042ab14 | -8.59937 | -47.1517 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fd74f88-20f2-3ad8-ab62-7cb5bc4a171c | -11.73085 | -43.64708 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f9963798-4f24-3640-b6a3-2d4576297158 | -7.82178 | -38.85909 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 5437c0e7-ddb2-3f09-abd6-696bad945108 | -11.08426 | -44.0046 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bea9c405-71a5-32ae-8c7b-d1308531faae | -9.87718 | -44.86247 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 358.3 |
| 2aa3ad24-41ef-3a78-8316-0d1f9751eb13 | -12.19894 | -38.19584 | 2026-10-08 16:18:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed60e9da-c233-3d72-9f5e-1a8ba849f063 | -10.03579 | -45.60574 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8fe724ce-7285-30e3-8db7-891c60fe26b8 | -9.52465 | -45.60569 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e346f20-a38a-3940-a99a-1c4178c8b49e | -10.77543 | -46.55188 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8ab995bf-f6ea-3f34-b06e-bbcac028a7e8 | -9.234 | -46.46656 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4b394e79-ce5f-3795-8a7b-3c3cbb3a4232 | -10.76837 | -46.53648 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 62f29a4b-fa69-3bf4-9481-b9f5021eeef4 | -11.85241 | -47.38097 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b91fe3be-cdde-3cd0-9242-f3f631f3c493 | -12.03629 | -43.38562 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cf9c8978-bfe6-3040-a795-c1c65b038630 | -10.84407 | -48.13275 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c13b60f8-32f2-3274-b61a-9f55e2279424 | -11.33679 | -46.69575 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 799b1241-173b-3ce5-84b8-97f95ee81a5c | -10.87407 | -45.54808 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 63e60333-6282-3d82-8d47-61f6184a997d | -11.22234 | -45.26593 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3c37e54a-1d45-30da-b0f5-74d6127e95a0 | -13.12623 | -46.32935 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da27c0a7-3572-384f-8485-5a09526bb8c0 | -8.96061 | -45.14802 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3502981a-4696-3cc8-8835-bc268a042783 | -12.64191 | -45.86274 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 080bddc4-bd0a-3ada-982f-8e99e07390d9 | -8.87864 | -48.10449 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| dbf20f68-8fdb-3f17-98c7-c975054ff7ac | -11.59367 | -47.17981 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7c92fd0e-0ad5-3ee2-be85-0a260eddfe37 | -8.36677 | -36.35056 | 2026-10-08 16:18:00 | NPP-375 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| adf44cf7-6d12-3b35-b4f9-c0002df06dec | -9.76475 | -44.78584 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 529c3ce2-8803-31c1-8a9a-5be8b153cc50 | -8.94796 | -45.18007 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 92d46dd2-de7f-35d0-9111-171b12111cf7 | -9.84332 | -47.85396 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e14ebbdc-4c0e-3c00-a46c-4277d96a03f1 | -11.87199 | -47.4065 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3327ea0e-6815-3aa7-af0e-89336b65ebfb | -9.91255 | -44.79177 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 226324d9-f172-3784-af1a-899781d2172a | -6.92287 | -34.96978 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 950cb0c8-808d-3423-adf2-67d2d0895c59 | -14.05067 | -43.82104 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 86ff5295-f001-323a-bebf-1eb9591ea035 | -11.11445 | -44.00454 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4661c39-c29e-3afb-bda8-a2bd1678ab9e | -8.59547 | -44.86786 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c7ef48ef-6e24-3a57-9a32-61cacf8dddd9 | -9.89558 | -44.79863 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3c7f0b5f-1b35-3c7d-a0f8-9f307f8f62e5 | -8.53198 | -46.91377 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 102ef16f-559b-33f2-b636-3218d5a9770b | -11.24214 | -44.85063 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 061e530f-ee2e-3897-88c2-2a0c0dfe28cc | -9.89422 | -44.85556 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 7581d47f-5f2b-3751-bd22-8ff1b0f31fa2 | -10.51516 | -47.31072 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e6f571f1-bafd-3b4a-af09-14efcef12f96 | -8.24556 | -35.93718 | 2026-10-08 16:18:00 | NPP-375 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 093cab9d-dbf2-31b8-9ff8-b8d58381075a | -10.85033 | -42.80955 | 2026-10-08 16:18:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 31f3e712-032c-36b2-8095-2e52e8f98490 | -11.40983 | -46.69805 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba0aad66-b29d-3e92-bae6-aada0d4fb009 | -11.27609 | -45.20976 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 56345698-f548-3dda-a801-35aa39e8ff86 | -11.07843 | -44.0256 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7044d66c-60c3-34a4-a087-a7bd30abcac3 | -11.27944 | -45.1996 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b26c859a-3c98-38f3-bc8b-d0f4c6faf500 | -9.73275 | -46.95561 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| aeec0a6d-32ee-3be8-a1c7-989c33d72361 | -10.58319 | -47.30052 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5345dc77-32b9-3a6a-90ca-2e57f1c41fa3 | -12.18184 | -44.80965 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e77b0e20-0fad-32d0-abb1-f7558901c142 | -12.71264 | -45.81253 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0ec43cfa-e50a-3871-af12-e472f79a8ec3 | -11.87696 | -47.40235 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e4758e64-3120-3196-b903-8998000ba93b | -8.95501 | -45.13997 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 522c9a35-f198-33ff-afb8-b096489b3dd6 | -13.64305 | -47.67075 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a61d29b-ec3b-3dbb-af94-1ce4e5c33c53 | -12.2155 | -44.81943 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| e5cf812e-a7df-395c-9363-48fc99fd5f9d | -9.1096 | -45.12538 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 03c4d7ed-e223-3737-aea5-09211c023e6a | -11.78297 | -45.59068 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57bd4334-c054-30e9-a1ea-09a15702cf19 | -9.08623 | -45.11974 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2d8a1824-f7d8-3bb0-8071-77511fc50d05 | -11.20863 | -44.87403 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ae52e815-586b-305b-a6f8-8051184f67c1 | -11.6231 | -43.70415 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5d886064-9d91-3ff1-b9bb-0f79a44f2175 | -13.70949 | -49.1211 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9947892f-b2b5-3deb-a4a8-d08dc96f859a | -13.69857 | -42.69184 | 2026-10-08 16:18:00 | NPP-375 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1d316087-a58b-35a8-aafc-c31f20e063d5 | -10.83841 | -48.13288 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 639ef7be-f05e-359e-82d8-0294e58e6045 | -11.34613 | -46.72863 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e51aebf0-a4dd-3605-9a0e-ef1da69667cd | -13.14314 | -46.34009 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ff2744f-4787-3a98-bc3c-4a4f28c4f71e | -12.28694 | -45.31621 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2b4a1705-4bba-3c9b-994f-0bb594bf30eb | -11.25773 | -48.45113 | 2026-10-08 16:18:00 | NPP-375 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4100b938-5d78-37d9-98d0-4fc3dd5749de | -11.92217 | -46.7888 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86d04388-3b64-33df-82ef-a42c1072c7fa | -13.3722 | -43.88778 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2341a0c1-ce4b-3364-8e39-9196c8b5a031 | -11.76658 | -37.6042 | 2026-10-08 16:18:00 | NPP-375 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad8cc0c2-6cb4-3e17-bd63-4d17055d6d6a | -11.3269 | -46.65828 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23e8b447-4d75-3c30-9eb5-c7446146c717 | -9.81901 | -45.6907 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 36ddec43-fadc-310b-989d-299c7fb8b081 | -11.34418 | -46.7131 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a6b1270-8867-3438-984d-58546e84cbb4 | -11.33081 | -46.68944 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8d7e10fd-6c21-337d-a4d4-2cf79651ce18 | -11.78696 | -45.58773 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 48e75295-b439-301a-9bb1-ca308ad928a1 | -14.37335 | -47.0771 | 2026-10-08 16:18:00 | NPP-375 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92f1300c-ee08-3e88-998e-81f0192fbdb7 | -12.83184 | -44.62569 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| aec71a4b-6e94-3616-8021-e3cf69e1f6a6 | -10.16067 | -44.67888 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| bedeb624-7f66-367e-b382-db7d1937041b | -12.28757 | -45.32135 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb99d58f-75f9-3590-8463-b4ad2408a4e2 | -11.3938 | -47.56796 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 707e6855-c881-388f-a568-4816ca9dfc2d | -11.34456 | -46.71619 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2ba9f562-d081-3504-a86c-6704573921b5 | -8.95944 | -45.13936 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c70c10a3-3c13-3dd7-a50b-8f5195fd445b | -11.24246 | -47.73563 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb7b111a-3491-3a83-a5b4-a25c15e707bc | -11.8547 | -43.53943 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 63f11655-dc74-3f9b-b3a0-94b585343384 | -8.95799 | -47.57377 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README272.md)
