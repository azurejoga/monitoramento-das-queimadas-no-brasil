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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa13bdc-8b48-3e26-9937-a950f51cdb3d | -5.59078 | -45.83798 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a054f1c-3f56-3e5d-892a-925f04d10f1f | -4.68305 | -49.49825 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd81e3a5-43ad-3c98-9a33-bd2b842d4d8f | -11.7414 | -50.93452 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 7765a15b-b984-386d-a83e-a19179526b8d | -3.89147 | -44.58218 | 2025-10-08 04:17:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c789c7a-a4fb-3372-accb-6506e52c9861 | -12.21877 | -44.2618 | 2025-10-08 04:17:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be5eb24-6070-3fad-9514-25bca74996ef | -13.06712 | -47.83291 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c53de00c-318a-394b-84e6-16a79e2539c3 | -6.72642 | -43.72565 | 2025-10-08 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20815293-fe3f-308d-bb94-7c96cc2088fb | -12.24705 | -47.86723 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41966370-9209-3fb4-b4be-8d754be8ffc4 | -11.79281 | -45.13665 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 066e0d3a-6339-30d3-9bb6-e12585e394bd | -3.11281 | -47.7951 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb91c239-3148-35e1-80d4-200074c959eb | -12.15725 | -51.43856 | 2025-10-08 04:17:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da6db3b7-39a0-3313-aeb9-4960ca2ec395 | -7.02616 | -42.87458 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fb22fbe5-7873-36ad-87f4-a44064556914 | -8.59943 | -44.90377 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f8fa01-712f-3837-873e-0480fd0ef17c | -7.80162 | -44.21734 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09e4584c-70ae-3110-b224-25178dead4ee | -13.29383 | -48.03517 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34edccda-6e6e-3c53-828c-c657a057989a | -14.28773 | -44.75802 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eda30dba-d3e2-36d9-8744-2d85309d3c4c | -19.8309 | -46.16776 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b156712-bb67-379d-80b9-6ac935e9c0b2 | -9.02288 | -45.80024 | 2025-10-08 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 972c1847-638d-31e6-a59a-255845d66a7f | -8.58873 | -44.90568 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc675a6-e9c5-3fa0-a0ed-76f10b9c7d44 | -16.12965 | -47.90549 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeea8b8e-68bf-331f-9621-fda1277d5d98 | -9.16952 | -46.17894 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4493a01-1866-34ba-8353-55b4c700b3d8 | -15.30939 | -46.16199 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 927b3f16-5326-316c-a0c2-06b1c9137a5b | -8.56136 | -44.62577 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 231e301c-e864-345a-b6e2-370db566b1e6 | -16.11147 | -43.87127 | 2025-10-08 04:19:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb9e721b-479e-3125-bb0e-67d9ce6ea5e7 | -13.33394 | -48.01986 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2173ed7c-9289-38bf-9015-05162ae25dd1 | -16.59187 | -46.54995 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea8c2cdb-d5be-3169-a317-5855f9074653 | -14.87823 | -48.25704 | 2025-10-08 04:19:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2902bc7a-1294-36f6-8fc0-4bd0992c7bac | -20.28848 | -48.51433 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6b6e20-e579-3d0e-bd0d-ee67f18c4baf | -9.2907 | -46.00831 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02e62521-0847-33f1-bd9b-7f4c26158c4f | -8.52035 | -46.28201 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 222b1827-678e-3c7e-a1af-0b1da071e593 | -9.39626 | -45.95802 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed37d35b-a82c-386a-ba80-acb1fe17f817 | -8.19697 | -44.19754 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8d19100-6948-3cf8-8579-de5b10f0ecaa | -17.86378 | -57.64605 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c453adf6-8cc2-306e-962d-b343a11efd2a | -15.0676 | -49.49184 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c0e6e3c-5581-3d12-863f-a4e0240a3984 | -16.29311 | -47.08826 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e0bf474-16a2-3d09-b84a-0025350cb5ee | -18.04541 | -43.15117 | 2025-10-08 04:19:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0be50fd0-c6d2-3d43-be9e-5758c37a5897 | -19.39854 | -44.38774 | 2025-10-08 04:19:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2aca7bcc-ab3f-3ce8-8df0-051c17ac8e5a | -16.11384 | -48.05954 | 2025-10-08 04:19:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be2846a-a351-3061-9d9f-345e6b9d7765 | -17.9387 | -57.53708 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d1054f97-a8fd-3533-92bd-f0d927067d4f | -14.91197 | -46.81812 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc92e285-19c7-3cb6-bbd4-433b8b26975d | -17.27704 | -42.6538 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c99239f4-61a3-3900-b3fc-d8ded5acda47 | -20.20331 | -43.95563 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 34c917ce-1893-3786-ba9e-30ef11230d9c | -13.70035 | -55.0159 | 2025-10-08 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4be15aa-5d8d-36f3-8009-d2617ef4d3fd | -7.24477 | -48.47808 | 2025-10-08 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1910ee6a-226d-3ffc-a00f-263530731713 | -14.25044 | -45.86417 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5866b512-6c7d-3835-9d5c-2eb238b6c15a | -15.38727 | -46.284 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37b7669-b017-3e83-84e4-ec68eb27346f | -14.71577 | -46.00589 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa59f4f9-3b16-3da4-9ef0-d05880035fb5 | -18.06597 | -44.47085 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a53ca587-509f-3a0a-a346-e8eb20e545b7 | -18.5107 | -42.09464 | 2025-10-08 04:19:00 | NPP-375D | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6a92c469-a14e-354f-8458-95161d7a862f | -13.20542 | -51.69739 | 2025-10-08 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ed5620-40b7-39c5-a7f4-d6785662c0d1 | -21.12068 | -47.03392 | 2025-10-08 04:19:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7547f88b-fdba-31f7-a2a4-edb6677a8a6e | -18.45806 | -42.52627 | 2025-10-08 04:19:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5b0c58bd-26b5-342a-bdaf-f280d1dd5313 | -16.78049 | -42.72865 | 2025-10-08 04:19:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfe99ed6-d199-3f7d-b992-770cfd49ab43 | -15.99597 | -50.96413 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f6b9033-9fa2-3c26-8a08-a6098005258c | -17.38329 | -45.06568 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6027ff7f-98ca-3f6e-8d8f-6069088e3db3 | -15.24188 | -46.36457 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e0f7ce1-29e5-3c33-be00-ad9686cc8d82 | -17.98039 | -57.49305 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 197580ab-7e13-3582-9e52-1c711166481a | -7.78713 | -44.22224 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5125e2db-3259-3076-8142-1a1f98d251a2 | -13.79217 | -45.8061 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 423faf39-9440-3fd8-bc6a-da8c6d47f530 | -8.56424 | -46.23608 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef3a1284-5b58-3670-83f4-5bbd930419cd | -19.42718 | -49.58718 | 2025-10-08 04:19:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e1aff6f-f7ff-3009-bd38-f9734457ad98 | -14.9171 | -46.80676 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f62bea8-a43c-3b7b-861b-f81384f6077b | -14.77137 | -46.01118 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536e0b1b-221f-3fcf-9d19-0351addc6000 | -8.23998 | -47.8657 | 2025-10-08 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea4b5944-6eac-3510-9011-0e7ee42a2dc4 | -16.02515 | -43.70349 | 2025-10-08 04:19:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b641a917-314f-3557-9b3a-18cf27a72d12 | -15.35868 | -47.33067 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a7c6f9a-6999-352b-a005-a7bafcb9ff2d | -15.65131 | -44.48895 | 2025-10-08 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66252111-9061-3222-9e3c-d901632bf69f | -15.98952 | -50.83673 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90b35c27-766c-30cf-a918-56cce3cb638a | -17.45754 | -43.38858 | 2025-10-08 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d14fd9c-1208-364b-85d5-d03b7767a392 | -14.7068 | -46.08291 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8487231f-e3ff-3401-97a5-e05edd321320 | -14.39418 | -46.03708 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44fdb167-3d75-37b4-8e42-e42010e13664 | -17.97141 | -44.97802 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d7afb8b-a7e4-338a-9c4d-328a52f74e25 | -17.26613 | -58.11855 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c900a9d4-7587-3aa2-a5a7-d38c2797f027 | -15.25713 | -46.35596 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fccd9306-58c1-3bc2-9724-1a2a15f4bd62 | -15.31274 | -46.16257 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fac4191e-9e64-37d6-9986-feabbb1865b5 | -17.51145 | -45.00079 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d6d099-b23b-3c2e-b9c9-e5ff9a27af31 | -14.71102 | -46.06443 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c4934b4-046e-333e-af3e-b4c60d1864f5 | -8.2003 | -44.19807 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c552197f-90d6-3711-b0db-021740de29ac | -15.79935 | -43.72247 | 2025-10-08 04:19:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b1759c3-ccfa-3be7-8867-e66734f51e5e | -15.79992 | -43.7187 | 2025-10-08 04:19:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc5b438-cfdb-3649-9f6a-4f7d55e96166 | -8.22088 | -44.19778 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e3a0abc-df1f-37cd-adf4-ce09492178f9 | -8.85978 | -46.77735 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa29eeb5-97b6-36aa-9958-9743702102e7 | -8.23314 | -44.18535 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 255d93f3-20b0-3744-a802-b4dbeb9d1c87 | -17.94047 | -57.52991 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c61fd076-b796-310f-bd5f-88225fffdf9e | -15.24645 | -46.35779 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5356f931-8a59-3a9d-891f-f7e9008caa27 | -7.69476 | -49.55064 | 2025-10-08 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ada85f4-da67-31fd-806a-dafb772afb07 | -7.82388 | -46.71746 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d747e90-c0d7-39ad-9463-9c08e12d6d79 | -8.99246 | -40.42004 | 2025-10-08 04:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 660f39f1-3fc2-3d81-8aea-368f84f20404 | -8.4617 | -47.20744 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9d88f0-bb70-3338-918a-612daf8a58fa | -8.15753 | -50.16739 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ea6b1b1-9454-3575-ba46-a881b65c1300 | -13.31338 | -48.03044 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d107091-84d2-3e39-bf6c-e52c05b2bca6 | -15.35524 | -47.32999 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697c4844-3a4c-3f55-92a7-a6b75f5cadac | -20.50107 | -46.99638 | 2025-10-08 04:19:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ec1ec14-62cd-3c5b-bfba-4369b55d604c | -18.05179 | -57.54539 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e9eeb10-d8f4-3c04-bef8-5bcdcdd86415 | -14.94419 | -46.79152 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54e956fd-7920-37a3-bd15-15c31a091974 | -8.47597 | -46.31257 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc9313a-262a-33f3-9ba2-e6fe674400e2 | -19.85203 | -46.16393 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13127f5f-9a8f-3190-bc77-f6c49924f6d2 | -8.4042 | -49.74367 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f33bdae7-e121-3c46-8c45-2bb7f6627f1a | -8.22927 | -44.16671 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 248d605f-1ec4-3ffe-b208-b64d19ae2fa3 | -8.18805 | -43.34019 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |


[Clique aqui para ver as próximas entradas](README47.md)
