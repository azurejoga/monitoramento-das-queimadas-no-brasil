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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 430a9121-c569-3b35-8840-2b4adb192151 | -11.38471 | -50.12886 | 2026-07-30 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ef1cda-063d-33a9-b205-de03e0f48111 | -18.22263 | -42.20786 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b91a0be0-9847-32a5-83f6-da5c26ab0ee3 | -18.5216 | -46.17508 | 2026-07-30 03:55:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aed16e64-8482-3501-951d-5439dd2de193 | -18.22558 | -42.21316 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| c90d503a-5d59-3615-8f63-33dc35266530 | -18.21911 | -42.20473 | 2026-07-30 03:55:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| feddfb11-239c-3975-b2fb-7343ba71bce3 | -18.58386 | -39.83531 | 2026-07-30 03:55:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cdd4487-0415-3a86-ae33-f8e07a19078f | -13.06922 | -42.03719 | 2026-07-30 03:55:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c819066c-e0d4-358b-98b0-2e7a842bc2e2 | -18.35326 | -47.19722 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d76ddd43-9868-3e46-b5b8-92034120b061 | -14.1917 | -43.99001 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f196cdf1-d544-3f26-82a6-c39b0a3362a2 | -18.59447 | -48.20591 | 2026-07-30 03:55:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fd6baa9-4729-3330-a4c6-c2b5b04531f7 | -11.39082 | -50.12582 | 2026-07-30 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88aadfed-340b-36b1-a446-12c48db15f61 | -12.15158 | -48.95352 | 2026-07-30 03:55:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a62893c-0bfe-353a-829d-678479ee4508 | -13.44079 | -43.67679 | 2026-07-30 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 983cf0eb-1cb1-3a6a-b11a-c19723b212ca | -11.39295 | -50.12383 | 2026-07-30 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70e28d53-c93f-30b4-9d81-1572e09fe4e7 | -18.36474 | -47.19351 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98482154-4cb1-3e86-8b92-f7609d4630e7 | -14.39212 | -48.03849 | 2026-07-30 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 116f071f-e847-3536-96e4-28c2a9c39df1 | -18.35389 | -47.19426 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b69d4b2b-6432-398c-9d0f-d21d29aa1042 | -14.19897 | -44.00103 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 001b3dee-1d41-3652-afc0-8f50fff881d8 | -14.18914 | -44.00385 | 2026-07-30 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7c2b171-2ca8-3bab-a38c-dc599a9514db | -15.71037 | -42.25955 | 2026-07-30 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d6ba81-63b1-3910-b3e1-0ba1ad526edb | -14.38663 | -48.03566 | 2026-07-30 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a4afe5c-c485-34e5-b323-6b2a0901feda | -18.35963 | -47.19239 | 2026-07-30 03:55:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f002cf09-843f-36a5-bf55-c1ebd27dbbc4 | -11.41838 | -50.09761 | 2026-07-30 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad62eae2-b7b8-3a03-907e-bdbfd1ce569e | -21.48166 | -41.1999 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e9225e1e-f10b-3a90-8ce2-9a5e79a2c703 | -19.17842 | -47.3543 | 2026-07-30 03:57:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6f277e3-3212-3c65-937c-cef4bfe80a6e | -21.43916 | -41.10527 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c34db016-fc56-3604-9f15-c14da9847078 | -21.43571 | -41.10459 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 08eb1545-88bc-3a2f-b1cd-83d16fb4abdd | -19.17906 | -47.35128 | 2026-07-30 03:57:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4182321b-fa6f-3705-8c22-771a9e16dcc0 | -22.71654 | -42.85801 | 2026-07-30 03:57:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e3e5049-0c9f-35d5-a94f-3b846e783867 | -18.47564 | -51.72559 | 2026-07-30 03:57:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c18f62c-7fa8-3701-b1ce-07922f3d814c | -22.05067 | -45.08659 | 2026-07-30 03:57:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c234f99-3554-3045-8a51-bf1dd276d1b0 | -21.35768 | -44.82192 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4a572ecf-bb15-36fa-a982-2fc61a949308 | -21.45579 | -43.76883 | 2026-07-30 03:57:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 141d6a2b-bb35-3018-b301-f136e38cc289 | -22.76324 | -43.73958 | 2026-07-30 03:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 2d903022-4a8d-3279-b70d-7569572a27d5 | -21.48858 | -41.20126 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d59d83b8-360f-3d26-8195-e9ff52c96520 | -22.28069 | -45.37967 | 2026-07-30 03:57:00 | NPP-375D | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 527626da-074a-3f1e-a010-41de26806d94 | -21.48512 | -41.20058 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b0ef4164-8513-3e63-ab90-e67e5d9f6089 | -20.72999 | -42.04363 | 2026-07-30 03:57:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ebeee2d6-3e45-308b-b12e-76a5bb5110ae | -21.35097 | -44.81195 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7128396d-6f80-37aa-951b-c9420a7bd8d9 | -22.7623 | -43.74459 | 2026-07-30 03:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d5af9f89-7003-3229-8061-80cd7176c9c3 | -21.35922 | -44.81404 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e60d8baa-a265-39d8-b305-4150495338e0 | -20.34949 | -40.9426 | 2026-07-30 03:57:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6e508054-e016-3049-babc-5308d781b195 | -21.43159 | -46.66287 | 2026-07-30 03:57:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fedec018-15cf-3516-9e4a-c633a8deaca9 | -21.64188 | -49.75657 | 2026-07-30 03:57:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87e8a3ca-7aac-392c-b0ff-2507cca185b4 | -21.49204 | -41.20195 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0b38ec41-7114-3ae6-9edf-5edb8e4ece44 | -21.59346 | -41.30468 | 2026-07-30 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2fc27c34-9a12-39b8-b842-21e226272681 | -21.35522 | -44.83446 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fb226181-ed11-3b07-a93c-3882c2b890d9 | -22.41387 | -42.2472 | 2026-07-30 03:57:00 | NPP-375D | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43d005bd-38db-3836-9c56-6eae9ba60e6a | -22.94952 | -42.96085 | 2026-07-30 03:57:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| abb40c6e-819c-3b7a-90c2-31fcdc9790bb | -21.43985 | -41.10125 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c5b953cf-7656-3313-b1b6-806bcc9c56b1 | -19.82735 | -48.2061 | 2026-07-30 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b14a4bd6-8cd5-3ab7-afb5-2da661918628 | -19.83265 | -48.20727 | 2026-07-30 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56034fca-37a2-3cfc-ac98-2248eec6c46d | -21.35512 | -44.81285 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d25eac76-43e9-330f-ade2-b89c2aee5cec | -21.48928 | -41.19721 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d7c60ca7-72dd-3b30-ac57-6326b35a0e89 | -21.35435 | -44.8168 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 43101440-4687-3a6f-84a1-f8ce2bf26b55 | -20.34325 | -40.93732 | 2026-07-30 03:57:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 423bd7fd-8559-3ca2-9d12-5455c0f4775d | -20.3467 | -40.93801 | 2026-07-30 03:57:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d1e5b4b-8bc5-372c-892c-b5ee54f8edba | -20.77596 | -42.97897 | 2026-07-30 03:57:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca68c944-4da3-3068-a113-dd22c7748856 | -22.28416 | -45.38449 | 2026-07-30 03:57:00 | NPP-375D | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a8978f7-5ec3-3c19-a664-128796993bb2 | -18.47421 | -51.73165 | 2026-07-30 03:57:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60c61bcc-81bf-3a36-974e-7ba356dcaeed | -20.42798 | -40.35728 | 2026-07-30 03:57:00 | NPP-375D | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae14384f-7034-3091-8e20-244730e9c095 | -21.46064 | -43.78608 | 2026-07-30 03:57:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 856abd57-289d-3477-b3f2-28871a634220 | -21.46164 | -43.7808 | 2026-07-30 03:57:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8f092d8f-cf3e-314e-96d0-06782f5d8d76 | -21.45773 | -43.78002 | 2026-07-30 03:57:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 192b87a8-74b1-3cc7-bd07-b15fe2be884d | -21.65913 | -41.51237 | 2026-07-30 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3b7cc54-4830-393c-87bc-93d3ea67f7fd | -21.75362 | -41.27695 | 2026-07-30 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0948d25-22fe-3499-bb30-119d70b30563 | -21.34772 | -44.8285 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26d7fa02-3652-3f8a-bb29-ee8bf9ece116 | -21.56233 | -41.27744 | 2026-07-30 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90c3ff80-1151-3efa-a6ea-445113107c90 | -22.68298 | -43.79835 | 2026-07-30 03:57:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f33af6a5-079d-35c3-b0e2-f0b0d75de6f6 | -21.35356 | -44.82079 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0d386a9a-69d9-3a1f-8ab1-d5328c0353f3 | -19.17633 | -47.35287 | 2026-07-30 03:57:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 188d6fb2-0b25-3df9-b908-6a9d55ba83f9 | -21.35602 | -44.83039 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1ae0cc39-33d5-3108-8285-3bda1af03835 | -21.35846 | -44.81791 | 2026-07-30 03:57:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 367fdcbf-ea3b-39f8-b2f7-6f05725e26a0 | -21.519 | -41.2115 | 2026-07-30 03:57:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55a9336d-d43e-3a51-ab20-c7eaf0e729f4 | -19.82659 | -48.20967 | 2026-07-30 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3f05d37-5511-35ea-800e-d3055029ff60 | -22.04986 | -45.0907 | 2026-07-30 03:57:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0fe858ce-d647-3aac-8129-2244361c0bc7 | -10.9397 | -43.0593 | 2026-07-30 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3087c733-8fe1-3120-9247-a88c7c0ab9ec | -10.9397 | -43.0593 | 2026-07-30 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| eb94013f-4712-35ce-9e37-0a344b2fe0b2 | -2.90726 | -40.3975 | 2026-07-30 04:12:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc803970-7a39-360e-a17a-8ecdbf67a317 | -7.13828 | -38.28221 | 2026-07-30 04:12:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d21ed868-8470-3ccc-a328-6d7fe01addc0 | -3.18403 | -48.01875 | 2026-07-30 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df72ec6a-6e57-31cb-8746-a4e937f43f01 | -3.67428 | -49.48403 | 2026-07-30 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e167198-1d3a-3978-9771-a105915b6e0b | -6.83925 | -42.8971 | 2026-07-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b253471d-eff5-3e0b-b443-00e8145c322e | -6.87288 | -46.00698 | 2026-07-30 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e81d7d8-e819-367d-a109-902f5fec76f0 | -7.54275 | -46.90375 | 2026-07-30 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 259f2e1f-fd26-349a-b080-27adb95705de | -3.68818 | -47.64741 | 2026-07-30 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55375988-5b0f-307f-9954-3bd6087c87ff | -7.19849 | -45.50037 | 2026-07-30 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d52e55a-268a-33f7-b253-627cdea5d3c8 | -4.36765 | -47.77093 | 2026-07-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e102be14-b231-3866-b943-9ecc46ce024c | -6.83983 | -42.89355 | 2026-07-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08b282b9-2ee9-328f-b43e-89482779d9b7 | -5.82248 | -44.75174 | 2026-07-30 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87f6ab1c-524f-36ef-a820-1a3b91b9c339 | -5.90657 | -35.7255 | 2026-07-30 04:12:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| bd6999b2-dc2f-3208-8705-4326b56a5b15 | -5.90174 | -35.72882 | 2026-07-30 04:12:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6b032ef9-e0d1-3fbd-8b64-af8e3794ac01 | -7.33354 | -42.99806 | 2026-07-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a07d625-1910-378a-a2fe-2dda5cb8edd3 | -7.24365 | -40.86209 | 2026-07-30 04:12:00 | NOAA-20 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 22dce688-3c5f-3bb1-8f85-28523aacc44c | -4.9033 | -43.47506 | 2026-07-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12970bcd-33f4-3fcc-9954-dcc6e245dcdf | -4.44876 | -37.92761 | 2026-07-30 04:12:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2926abf-da0a-3117-abea-dc8b8cdbb46d | -5.74826 | -51.71228 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95eb93bd-0e25-3a42-9fcd-0ff5f0fe1720 | -3.67795 | -49.48239 | 2026-07-30 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6b0224b-c172-354d-84f2-89e0b80d54ab | -3.1693 | -49.51845 | 2026-07-30 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01467a89-6a29-32f0-a615-09c5718cd87c | -7.20112 | -44.87392 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
