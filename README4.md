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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 868dca71-053c-3759-872f-f87f0f76707f | -13.038 | -43.9771 | 2024-10-28 00:46:30 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05a438d6-4dbc-3b4a-9f18-cb071e84f560 | -13.04 | -43.985298 | 2024-10-28 00:46:30 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c3c1b24-2879-3af8-8764-d2045a426e76 | -12.9051 | -44.5942 | 2024-10-28 00:46:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b8c6e07f-ca28-35a2-bfc2-2d859a8de09f | -12.907 | -44.602001 | 2024-10-28 00:46:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dd71847-7696-35ae-87ea-66396eb2f330 | -12.8954 | -44.5966 | 2024-10-28 00:46:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12a18319-07ce-34e7-b51d-0d8167386740 | -12.8973 | -44.604401 | 2024-10-28 00:46:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09e1f49f-7888-3b33-b2bc-521e2bb14654 | -12.8991 | -44.612202 | 2024-10-28 00:46:35 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 682ca385-2510-3ad7-bb22-542a6a765000 | -13.2618 | -48.236698 | 2024-10-28 00:46:42 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d125f508-a132-333d-8148-90971576c9e2 | -12.6718 | -46.571201 | 2024-10-28 00:46:46 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb6c5278-ae21-35c2-bcb9-d655fae3f11a | -12.6734 | -46.5783 | 2024-10-28 00:46:46 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdd76f4e-8607-30c0-b030-3feabc58deb6 | -11.9327 | -43.937901 | 2024-10-28 00:46:48 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52be798d-3efe-3959-ae6e-ea36edade72e | -11.5724 | -42.915298 | 2024-10-28 00:46:50 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42252039-90a9-3b24-95c9-16bae452b1c0 | -10.6442 | -44.9972 | 2024-10-28 00:47:13 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae7f887d-c57c-3e9b-b8ae-66b7b694f5d8 | -10.646 | -45.005001 | 2024-10-28 00:47:13 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b14f0f31-fca7-34ca-94ff-fa3c5116594b | -11.6272 | -44.9594 | 2024-10-28 00:47:23 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d20a0ac5-1592-3862-88cf-e70e92eeca18 | -11.6291 | -44.967098 | 2024-10-28 00:47:23 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0f6f406-300b-3721-a547-c735dbe2bd2a | -10.0904 | -45.365601 | 2024-10-28 00:47:23 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5a5c1bd-0e5a-32ff-a628-ce46f80c09fc | -9.4539 | -44.464699 | 2024-10-28 00:47:30 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea2ee907-ff4d-35cb-93a5-c9ec14cfc649 | -9.4421 | -44.4585 | 2024-10-28 00:47:30 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 020c1e7d-f1b3-33d6-823f-53fc59217075 | -9.4441 | -44.466999 | 2024-10-28 00:47:30 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5686eacf-ac4f-3230-a0d2-5bb859cfa05a | -9.4461 | -44.475498 | 2024-10-28 00:47:30 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a407f38-5a88-3e77-a673-0b47067d9fbb | -10.8764 | -44.536598 | 2024-10-28 00:47:33 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3ab3ab1-cf15-3e83-bafe-2683cf35e57f | -8.8316 | -42.7798 | 2024-10-28 00:47:33 | METOP-C | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f64680f2-2abc-3780-a457-9e177d3aecb9 | -9.6763 | -46.245701 | 2024-10-28 00:47:33 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f65aabb9-5381-31d2-a0e8-bfa1ae534130 | -9.678 | -46.252899 | 2024-10-28 00:47:33 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 979a8f9b-af82-3b40-bc0b-3d4c2ca6cf41 | -10.0605 | -48.0569 | 2024-10-28 00:47:34 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39d4cd84-7293-34cd-b751-5572c895809b | -10.0621 | -48.063801 | 2024-10-28 00:47:34 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fba4c1d3-1a9a-36ee-8b71-178a4d0fcd04 | -10.5962 | -44.271 | 2024-10-28 00:47:37 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5177fa-efdf-3361-9000-09f69a0f9a17 | -10.5982 | -44.279499 | 2024-10-28 00:47:37 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e3e61f29-7454-3dc2-b4d7-c7f7053f2723 | -10.6541 | -44.994801 | 2024-10-28 00:47:39 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a2b8b0b2-4144-3f03-b1f2-d8cde76de67c | -10.6559 | -45.002701 | 2024-10-28 00:47:39 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11ab9b14-745e-35e3-a66b-18f9775bc6fa | -10.6578 | -45.010502 | 2024-10-28 00:47:39 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7227802-be47-34ca-a76a-f10d8a3465f4 | -9.2728 | -47.901402 | 2024-10-28 00:47:46 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 615e34f7-bbdc-389f-925f-a5cac8f7f193 | -9.2744 | -47.908298 | 2024-10-28 00:47:46 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9080d67-890f-33d0-b126-6d380c1289f8 | -14.13457 | -42.92769 | 2024-10-28 00:48:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ae78bfe0-40a2-3bf4-a50a-e7bf0d201588 | -16.53619 | -41.79331 | 2024-10-28 00:48:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f42f81ef-8226-31d4-bc43-e8e321b3f73a | -15.64149 | -41.70735 | 2024-10-28 00:48:00 | TERRA_M-M | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 09e08250-d499-3725-8fa4-51dced52e9df | -15.63993 | -41.70141 | 2024-10-28 00:48:00 | TERRA_M-M | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5cd7b8c7-a5ad-3c78-bb3d-40c7dc71805a | -15.513 | -42.27902 | 2024-10-28 00:48:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e1cde363-6b2a-374c-a815-37bfea70a3bc | -15.51134 | -42.26809 | 2024-10-28 00:48:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0449feb5-a9da-3b99-9cf3-a1c94e12718c | -15.43027 | -41.14244 | 2024-10-28 00:48:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4cd0bd0c-44fd-3fd5-8909-04d85ca6b628 | -15.37011 | -40.18214 | 2024-10-28 00:48:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 8036cd47-a669-3000-bf3c-d6b1d28051b1 | -15.35905 | -40.18427 | 2024-10-28 00:48:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 43.8 |
| d7044118-e86e-3c99-8b2f-e9b8a71ec8e5 | -15.3566 | -40.16919 | 2024-10-28 00:48:00 | TERRA_M-M | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| ddf0a727-9035-3720-971e-5c53f6fec806 | -15.31982 | -41.75077 | 2024-10-28 00:48:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ff2c994b-db6e-3dee-9fc8-ee04a67a532c | -14.96269 | -41.89413 | 2024-10-28 00:48:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0be3497d-3fa8-32d5-8326-19ccac7bb33f | -14.55673 | -42.98811 | 2024-10-28 00:48:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46a86a75-4c18-3300-b9ad-ecaac9c4b101 | -14.55517 | -42.97779 | 2024-10-28 00:48:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 843fcc3d-3554-30bf-95b2-ecf3ebbceb7a | -14.32769 | -42.30468 | 2024-10-28 00:48:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5b35a40d-c6cb-3ce8-a79b-33431d94bafb | -14.19611 | -43.72556 | 2024-10-28 00:48:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fd0dafd-23d2-303b-87ba-1534248359ce | -14.0693 | -43.99216 | 2024-10-28 00:48:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a2f3705-e10b-3d2a-8285-d3bee368f52e | -13.89756 | -43.45155 | 2024-10-28 00:48:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2b30ef1b-080a-3f91-b5ed-77491ad86559 | -13.7008 | -42.88364 | 2024-10-28 00:48:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e8ee4baf-3033-30fe-9995-5bf5d5f21f33 | -13.68869 | -44.03783 | 2024-10-28 00:48:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a69d943b-7aeb-3ce8-9d4f-b0758c15ec16 | -13.57281 | -43.06538 | 2024-10-28 00:48:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a18610d5-eff4-3695-807f-686c4f59fd20 | -13.54828 | -44.34008 | 2024-10-28 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| afab69c4-a48b-3408-aead-67ea86201bbe | -13.54692 | -44.33075 | 2024-10-28 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 9205a928-0bd0-36ab-bb73-579d418d8e84 | -13.45707 | -44.28411 | 2024-10-28 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a22cd2f0-f3ac-30eb-9145-e6235090ecd9 | -13.33004 | -44.61908 | 2024-10-28 00:48:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1e947145-965c-3319-8c15-53ecafba11ee | -13.17025 | -42.97194 | 2024-10-28 00:48:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5af1e4f1-cbf4-3158-8cfe-f26693abe881 | -13.16866 | -42.96144 | 2024-10-28 00:48:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| be08d42a-ce0e-39e8-bedd-696c480893c2 | -13.0369 | -43.99648 | 2024-10-28 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a964733b-f2cd-3f48-a4ba-4ecf8f0e11bc | -13.03549 | -43.9869 | 2024-10-28 00:48:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e6c327ae-7907-399c-b484-c52818834865 | -12.97691 | -43.46402 | 2024-10-28 00:48:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b13dc6e-8b9f-3044-aa0f-9be0fdb2cdeb | -8.2929 | -40.882599 | 2024-10-28 00:48:01 | METOP-C | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6565780a-88e2-348e-88f4-c296a3601955 | -10.3068 | -51.882099 | 2024-10-28 00:48:09 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8920d135-5f16-367f-af8a-8497fb4513ec | -8.9983 | -46.749401 | 2024-10-28 00:48:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0322a1bb-8ce7-3b7f-ad3a-5b31046fa2df | -9.0 | -46.7565 | 2024-10-28 00:48:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac5d6193-7596-3edd-b5d0-54e2b4a9cbf7 | -9.2631 | -47.903599 | 2024-10-28 00:48:12 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9a1c1a9-322f-3b05-a594-cb36d7da605d | -9.2647 | -47.9105 | 2024-10-28 00:48:12 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 961f710d-0612-309c-99ce-43b1ebbfd428 | -7.01 | -41.321899 | 2024-10-28 00:48:23 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72a98c8d-16c5-3d34-94bb-4460b58021c1 | -7.0135 | -41.336201 | 2024-10-28 00:48:23 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db5a918e-0a0e-3dc9-9c56-cf82b0c02bfd | -7.8821 | -45.416302 | 2024-10-28 00:48:25 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03f4b74a-0950-36a7-a50f-bfbfaa35cfaa | -6.2306 | -39.505299 | 2024-10-28 00:48:29 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e421a6eb-680b-36f1-a212-bbd915817578 | -6.2354 | -39.524799 | 2024-10-28 00:48:29 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 508ad35a-133c-30c1-a7cd-9dc14947617c | -7.4347 | -44.790199 | 2024-10-28 00:48:30 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 31b8437c-f140-39bf-8451-c1a5f67ac420 | -7.5605 | -45.893799 | 2024-10-28 00:48:32 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed4d864f-1dd4-3c9d-831f-1b6f5386d817 | -7.5623 | -45.901402 | 2024-10-28 00:48:32 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96b3eab6-5918-39c8-b27b-d2a1ff2d8f24 | -6.6241 | -42.783501 | 2024-10-28 00:48:35 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ec985a8b-48d2-3357-9b7e-47b334d86412 | -6.6269 | -42.795101 | 2024-10-28 00:48:35 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 04e04853-0e1e-35d5-9342-ab6bfa9893c4 | -7.6379 | -47.069698 | 2024-10-28 00:48:35 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6fc0a4-5595-30cc-adb1-0d303afe393c | -8.1447 | -49.473801 | 2024-10-28 00:48:36 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0844e584-d9ea-3787-8cdf-c2268c2c9727 | -8.1463 | -49.480999 | 2024-10-28 00:48:36 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea81fbc-3694-3316-9d99-50c40d360e53 | -6.2975 | -41.9044 | 2024-10-28 00:48:37 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb4ad2d9-30f2-34c6-a299-64e3ef271880 | -6.3007 | -41.917702 | 2024-10-28 00:48:37 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 45497fef-2d76-3778-af80-9cb9b1f66740 | -7.4721 | -46.710201 | 2024-10-28 00:48:37 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 145da787-3f04-3f60-a678-aef1cad52bdf | -7.4842 | -46.896 | 2024-10-28 00:48:37 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd747ad0-7976-3199-9a83-595246c23c2a | -7.9562 | -49.049198 | 2024-10-28 00:48:37 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2234c0e0-06a6-3f78-a846-43d611648874 | -6.1611 | -41.851898 | 2024-10-28 00:48:39 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc755b37-a0e8-3024-b6dc-d118ad5eab4a | -6.1027 | -41.866001 | 2024-10-28 00:48:40 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6030abef-db42-3f77-b989-24a15a58c969 | -6.106 | -41.879501 | 2024-10-28 00:48:40 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ee0237e-6691-3030-8b9b-d17868e8609d | -6.0896 | -41.854801 | 2024-10-28 00:48:40 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 15569b19-3d71-3f29-b694-06f630248d48 | -6.0929 | -41.868301 | 2024-10-28 00:48:40 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79c99e67-ce12-3251-8500-119fcb098357 | -6.0962 | -41.881802 | 2024-10-28 00:48:40 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 243e2e96-9c77-3f14-a406-0759eb6a54b4 | -6.7274 | -44.680302 | 2024-10-28 00:48:41 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e27eef91-a86b-3ec1-8d26-ee515b283b15 | -6.1836 | -45.437302 | 2024-10-28 00:48:53 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 536e802a-0912-33ab-a29e-594bafb2c600 | -5.8198 | -44.117699 | 2024-10-28 00:48:53 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e99a224-b78a-3348-92d9-5e4b797a0dc0 | -5.8221 | -44.127499 | 2024-10-28 00:48:53 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5afd1a8d-421f-3bc8-9329-b26a13760e9d | -5.8124 | -44.129799 | 2024-10-28 00:48:54 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22c76f60-8d35-3bd4-8c27-2f77290f32ee | -5.8471 | -44.754501 | 2024-10-28 00:48:55 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
