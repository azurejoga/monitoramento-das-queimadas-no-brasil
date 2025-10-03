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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 333b97aa-7b10-3255-bc27-6670bfa892a8 | -10.59093 | -48.70982 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a431eb71-a66e-3858-8fe5-a94d3a45361e | -11.61584 | -47.99231 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8fb3a7d-bdcf-36bc-a9f7-f46c6fdf8be2 | -11.45513 | -44.96032 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f4f2707-1eeb-3669-936e-506b7967eba9 | -10.00237 | -50.2415 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 56c91849-9ad9-3676-91dc-74709efcd4f3 | -11.79456 | -41.19673 | 2025-10-03 04:32:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7b40398-100d-3152-b1b7-a682aaafa93c | -7.75744 | -46.27399 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1e45d42f-05e8-3516-a579-c2ad10aa60a6 | -8.17328 | -44.15454 | 2025-10-03 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47f9016a-78a6-3af0-b09d-831d370c51d1 | -7.50381 | -48.85434 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a574544c-e006-3829-9330-a07398b94c5d | -11.88172 | -45.02779 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a9f4489-f45a-3061-b071-8f39c648aaaa | -6.56091 | -44.13297 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21973b1f-9daf-3a26-8929-869b72635db2 | -10.10293 | -50.35695 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb403664-f0a8-3105-b9ab-b19d3ec871a6 | -11.66548 | -45.31528 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23f7579a-e6ea-3cd8-8212-3b17fe2d2527 | -10.89489 | -46.72427 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 57069b80-9d56-393e-915b-251bb396e0d7 | -6.27118 | -44.05045 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1eb82693-7fc4-3474-9605-cf2e98365b18 | -4.65979 | -45.80159 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff062aaf-84c4-3e74-8278-5ef637e1f948 | -5.89044 | -43.72584 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38acacb0-7be6-3224-8507-3a26ba2bfdeb | -6.04324 | -44.62569 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6689869c-90a5-3cf1-86e9-cccb09a6a8e3 | -10.56133 | -56.55803 | 2025-10-03 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd1b611-2436-34f6-8c69-7a5c931a6107 | -11.49471 | -45.00459 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 277cbbdc-a4ac-34d7-b672-ca453d31c416 | -7.51774 | -50.50005 | 2025-10-03 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d0eb0f-a41c-3c27-ae16-e078dc216376 | -12.22513 | -43.76692 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccfc1bb2-5acf-3bae-a1f0-1404c3917adc | -10.30415 | -48.2869 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af23e418-10be-3001-ab74-5e3176496a37 | -11.90623 | -46.73967 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a44cff-60f8-31e2-afd2-3ac41f32f3a8 | -9.76858 | -47.73852 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef36dfa1-7383-35af-a26e-79fe0730e8c7 | -11.09855 | -47.87112 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd799ff8-c30a-334f-b148-68be3014a5c5 | -11.13521 | -43.4065 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 176a1d40-857c-30d9-8a01-15d839711cdc | -6.72419 | -44.1462 | 2025-10-03 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 757c7752-e864-3258-a323-c482354dbb5c | -11.90344 | -46.31439 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31da1f3f-abfd-3f2f-af18-5afdccf968b0 | -6.55722 | -44.13235 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1079b3a-4ee4-3950-bac0-6b0fa03b05b4 | -10.79797 | -44.23977 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ecf3664-202b-3ca3-b667-ea4988290704 | -9.39874 | -47.53902 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e43d7891-f874-3780-ac7a-9dc5a4c18e53 | -5.18857 | -45.42241 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6d6e0a1-4936-3131-9b64-6375d215a698 | -9.95555 | -48.77547 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 924ddacd-6a22-328d-8678-d2f4a236326a | -7.21361 | -46.87659 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98ac3492-3ff9-36b4-83ec-cc74ab85636c | -7.80371 | -49.86903 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb51e1e-097a-3d88-a299-3b6c5f7c7a25 | -6.09223 | -43.12356 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 381fc10f-e723-3514-9c9b-bd2fa0669bf5 | -7.75373 | -42.5536 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 88504dbd-403e-3b00-8a4d-ffde50ace7fe | -6.94633 | -45.44328 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 450c9f60-1c6e-34b2-af41-fbdd9ce29e6d | -7.79908 | -42.5332 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa35621f-ed18-3f4f-8af1-7ed0ff6e746f | -12.39748 | -45.01151 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68931c2a-95bc-3ade-8e7f-edd74977b589 | -9.33728 | -45.7433 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a69cbab1-c200-3314-9eeb-3ac6bd4b6da4 | -11.24233 | -47.90825 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7818ff01-9d93-3455-8e4b-4e178df8d477 | -7.73665 | -46.22551 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 475c3901-db04-3b06-b469-78e8db260287 | -10.76661 | -45.33455 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42e3a965-ce40-37c0-9c70-a11b2ae8453e | -7.30336 | -45.2584 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be1de6d3-7aad-3662-a23f-29236c63f145 | -10.16139 | -45.49313 | 2025-10-03 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1cbc877-5a21-34f6-b76e-761aaaec8dc0 | -10.89032 | -46.70804 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bff0461-5bfd-3557-8012-68d34a0dee5d | -11.08799 | -47.87315 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1f0ff5a2-fac5-3e3d-8a8d-1dfcb72a41e3 | -10.88052 | -47.05084 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da7fa254-c1d5-372c-9a95-6db98b41f643 | -9.57286 | -48.44592 | 2025-10-03 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72c20b4c-356a-3e61-9bf3-db8ac0778fb2 | -4.55595 | -50.46876 | 2025-10-03 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbf458f8-8092-3d71-a7d3-39278faef946 | -10.88746 | -46.70372 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9d7f501-357f-30e9-98ea-fca2933fe982 | -5.99619 | -44.56079 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b50785-736a-30af-b538-1b5ecb506c7a | -7.92818 | -50.01036 | 2025-10-03 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 064f44fc-8cda-3126-b487-31e6687316ff | -4.42655 | -47.75811 | 2025-10-03 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23043db1-7468-3934-b194-0c04ed5aa9f9 | -12.22063 | -43.76937 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd190976-a299-3044-b734-c89d5d212874 | -9.44394 | -47.37898 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f28785e6-a78e-3677-9701-59c38c33b826 | -9.95833 | -48.77946 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 004b61f6-7543-3ee8-bd90-a5cc354210c4 | -11.77578 | -46.82376 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bcaec85-b9ae-38e8-896d-af1077aa06b7 | -10.90063 | -46.70965 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 422a1f83-f16c-3294-8c44-0fb8d8aeb076 | -10.92929 | -46.72514 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0cf1247-6562-39ff-8346-b6cdb0863568 | -9.87594 | -47.81285 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eea148d5-e258-303a-9ed2-50b6893f2c17 | -11.19015 | -47.74318 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c56e02d-6473-3969-bbce-0432d0d35bb8 | -8.75815 | -49.93129 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea273a6-bbff-366e-8abc-24e2c5cfdaa2 | -11.34936 | -44.97124 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f24b11a6-a388-3076-8499-5d5b80c6e013 | -5.78365 | -45.76543 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab7cf2e-2789-39a8-89d2-02a19dd088b5 | -11.29734 | -47.8402 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8f4c542-e769-3e69-9035-6f5b3cc982a8 | -6.28538 | -44.0569 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e76e718e-8a3a-3a32-be8a-405c680c4260 | -11.1202 | -47.8637 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 27f557bc-0fd3-3e63-b100-73a2f7a7f434 | -11.07321 | -48.36346 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caf9f3c5-2984-34c8-ae15-56198aed5315 | -9.65372 | -48.21238 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67536995-08d5-34ee-9a90-fe223ebcea27 | -10.16499 | -45.49368 | 2025-10-03 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ae624a7-bb8e-323c-8eb3-e9f5cd04065e | -6.51547 | -43.94167 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93b285b2-bf0e-3bbb-94b1-a2e4f59b739a | -7.7738 | -47.38166 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ffe9d45-5a74-3c87-958e-51ce4d97a228 | -7.28513 | -45.25964 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f732dab7-c618-3d65-9cc2-a37a877df5a4 | -9.95225 | -43.71303 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d1739c3-b2ed-3dd6-9b2a-cde3f9505b94 | -8.55875 | -48.65065 | 2025-10-03 04:32:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee96b978-f86e-352c-8def-2c5e5fb1b483 | -11.83614 | -44.94171 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1035d3-8eb6-36fa-9757-6460ef3a6745 | -7.74605 | -46.25716 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc3cc914-c107-3cdb-81d7-07b3d48cd322 | -6.37529 | -43.87211 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e67b870-f81c-3f44-a823-f1a62fdb8942 | -10.10656 | -50.27015 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eedc6a45-3829-3ed1-a3af-8eba9129b87a | -11.2912 | -47.8356 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9fe9b47-8ed8-33f0-b750-4117fbf9fee4 | -5.48512 | -52.13634 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c051048-7846-3bf6-8ea9-09375d9df819 | -11.64373 | -46.8623 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e561434d-5924-39e2-8164-1db2ba10307e | -10.2702 | -50.36525 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60c3fd85-271b-3860-8a14-62733ebe5ec2 | -11.18188 | -47.77459 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8390d013-5ed1-301f-bbba-95548fe80eb0 | -6.67311 | -42.82307 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74eebb16-8845-36fd-a6aa-7cfc23dce602 | -7.31629 | -47.28858 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153706a8-5365-3826-a4e7-2da62142507d | -5.23727 | -45.17416 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f36f025-8576-38c9-8995-500180a014fc | -8.83812 | -48.86037 | 2025-10-03 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 775597cb-5d6d-3574-ad48-ef46501df72d | -8.79148 | -46.67793 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c9ff766-41b1-37d5-89e6-5c1b5ff328e5 | -6.7397 | -44.58748 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbc6ccb5-4b99-3f0c-899e-1bfc0b387bc5 | -9.16473 | -50.84159 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1822839-d319-37fb-8a8e-82414a253d1b | -11.16861 | -47.17783 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b05d22-521e-3c0d-99ba-a090b3107093 | -6.40857 | -43.93166 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0184c8bd-bff2-3757-b624-6dfe3f3b518b | -4.65923 | -45.80519 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f0ac78-9cea-35ad-876c-2644df39597a | -10.88518 | -44.27351 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ce62b10-0dbb-3f80-8d8e-2d18014dca9f | -7.76392 | -42.6013 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 6e6ce063-08fb-3a4e-a29a-32067f107073 | -7.75871 | -42.53517 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb73ef11-a9e6-36b8-aaa9-a66d57bcd0b6 | -7.71506 | -46.20705 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README106.md)
