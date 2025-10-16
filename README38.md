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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2034453-706b-3ff2-8a79-4ff74d39b4bb | -7.66188 | -42.59224 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e94a07df-f69c-3803-b0ce-feb911e722b7 | -8.8305 | -44.41065 | 2025-10-16 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de6e22c-393e-3780-968d-ad9b471eec87 | -7.20278 | -45.48655 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e968158-c347-335e-9ff4-c5e8dffa8be2 | -7.17683 | -42.19904 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1fcc4b70-98b8-30ec-baf5-151f988b5470 | -6.33084 | -46.33231 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2c8f4c0-c452-3db6-bbad-01440407516b | -7.96523 | -44.12943 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d7716d5-889c-3f92-9a5a-93dd2138b4df | -8.40126 | -46.24128 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 146f8c66-1a3b-3207-b59e-1f0c3e62e8c3 | -7.95116 | -44.13985 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7ef30a1-35b8-3185-8f67-20965d97a0a5 | -8.29273 | -44.97472 | 2025-10-16 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23ad152d-f526-3c93-9817-3200b3ad8421 | -14.0556 | -43.54549 | 2025-10-16 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c99ec8a6-00d8-31bc-b88e-1e6b45f071d1 | -13.9024 | -45.5729 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ac1e1dc-93af-392a-be0f-b574f60f04cd | -8.46105 | -46.23394 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f311fc3-54a9-38e2-b2b6-4ea632f0f1c1 | -7.96609 | -44.12457 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d46783a1-ca6c-33ee-a518-a6eb48e665ec | -8.21294 | -43.31621 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c166c58b-d799-3359-a171-1f5011c990ed | -6.80465 | -44.53836 | 2025-10-16 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0d619bb-b77e-3190-8a9e-bc48856c448b | -7.39417 | -39.70673 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b9441b56-74d0-3be6-8a77-3ea7dc38eb7d | -14.07817 | -44.28186 | 2025-10-16 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 910bb783-ced0-3ef1-a36f-64e281140580 | -7.40213 | -44.74521 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6d90d7e-9ca9-3d23-ac18-b5e1b16dccc5 | -7.3903 | -44.75474 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fcabd7c5-30e0-3ce8-b1bf-81c3d8111921 | -13.90147 | -45.5778 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fc3bed8-1dd6-3bb0-a4b1-398ea29d1ebe | -6.7123 | -44.40115 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b8a95e1-dc8e-3e2d-a461-e53ad75221e8 | -8.28878 | -43.40119 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f494d2e1-e905-398b-87ac-7e1842c024bf | -8.28586 | -43.39165 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 846c8769-efb2-3510-82db-d6e65e726d7b | -7.18932 | -42.36108 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d77fea83-6f66-3e73-858b-6948da7f4488 | -6.53527 | -44.6935 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebbba190-70e9-367b-9d6e-0705a630acc5 | -7.9374 | -44.1241 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bebdeb88-a42d-3072-91f9-956b7136c55c | -19.55515 | -45.93646 | 2025-10-16 03:49:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70183638-8d28-3ce5-b28c-9b42e9397398 | -17.6509 | -48.33949 | 2025-10-16 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ef16fa9-5e39-3f6b-8df9-a68b48688067 | -6.59822 | -43.922 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7978c4ce-616e-3e2f-9df0-5b0f446fb1b2 | -7.55536 | -43.92206 | 2025-10-16 03:49:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9fdeda8-8f6f-3286-a180-0b06e22dd855 | -8.40063 | -46.24475 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b3fe852-d59e-3db5-95d6-11225b2ee707 | -7.09547 | -45.27485 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7eea661-fe4d-3854-8b68-4d61fa8e4f6a | -8.23521 | -43.42221 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5412d6e4-be7e-3ff7-a4c8-3430dab9840e | -7.93275 | -44.12328 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99794d9d-3f62-3f4d-b60a-60bab8357209 | -8.20854 | -43.31552 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 75fb3045-81c6-32c1-a7ee-6959bbb858f9 | -8.06862 | -45.42178 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a81d29b9-6402-34d8-a79c-b39f679cdbbb | -8.38655 | -46.26185 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fabd765-733b-359c-8423-9576594a6be8 | -7.54155 | -42.7094 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dc4ab98f-b1a1-335d-8f3a-b64fd92452f3 | -6.77284 | -42.81173 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ba8c2088-8dc8-3b41-82f4-fefcfa246597 | -8.18944 | -43.32132 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| c2eb37a0-30f0-3e7c-ab06-840569c5d1be | -8.23746 | -43.40925 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ffc805cb-6480-34c8-8608-eb4a668ce35c | -13.90527 | -43.61163 | 2025-10-16 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4b75b82-36d2-3785-9639-d8b6db10da3f | -6.45672 | -44.58482 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edef6925-ba99-398d-8393-f90f36f6bb94 | -19.07573 | -46.82469 | 2025-10-16 03:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28dd4ad9-4a10-336d-82dd-329fa0398693 | -7.12791 | -42.49204 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ffe3e05-f2f9-373d-a63a-04532231eb90 | -13.69537 | -43.70728 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cad9d47-5aa5-376f-a8f1-0f6316c7e948 | -7.94949 | -44.14965 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6fbdac6a-d43d-3a37-9450-254191fb8d8a | -8.3468 | -38.95726 | 2025-10-16 03:49:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20d7ac5a-b060-3bc0-8067-6197110df1a4 | -7.16519 | -42.50132 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a47744d-7fdc-3fb2-9c06-4a3e4532bfc2 | -7.68019 | -42.56276 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5a6369e-1fd8-36f2-8cab-fbf92ec8dfd4 | -8.46431 | -46.2162 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbd1331d-cfca-3dda-9243-1c6595566b91 | -7.95423 | -44.13729 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51677b11-94db-3f01-898b-4d55d678218a | -7.68222 | -42.55112 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0eac16ba-7877-3860-9aab-c9608ee97769 | -7.47931 | -42.13385 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e50d289c-a651-312f-9f6e-f15ab90f00ca | -7.92959 | -44.12582 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 30f0522b-1f87-364a-a3c7-87e13fedd17d | -7.23021 | -41.22215 | 2025-10-16 03:49:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7bda438-216f-329b-bd01-a0b6275d9d6e | -6.71139 | -44.39792 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb3b9a77-ef3a-396d-9601-3679ef3ceb0c | -7.53895 | -44.28173 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469d7aec-b49b-3fc1-8614-255bab8f4b45 | -16.66437 | -42.11283 | 2025-10-16 03:49:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac0dcde1-23f4-3a79-b5ba-968e04eee3eb | -7.22798 | -41.21148 | 2025-10-16 03:49:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7a9a454b-549e-38d2-ac28-e357cc85c6b7 | -7.08302 | -44.94365 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38198571-a590-3424-95b8-4a24e4418dbe | -7.46645 | -42.66853 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bed685f7-adc4-3f0e-aad8-5ba8501fb2a7 | -8.24654 | -44.03338 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0586ee6f-2c3f-3352-aaa9-9c55de76d360 | -14.7496 | -42.3767 | 2025-10-16 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d59756d8-b789-36c3-8a27-f995df2f4141 | -7.53611 | -42.06829 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2390ae7-a579-3de1-beeb-ace658dcb10a | -8.18238 | -43.96784 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb0b93c9-dfa5-3ff6-ba48-467330c61437 | -7.20738 | -45.49067 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0576f349-44ba-3580-9577-b6ba16c154d5 | -7.08159 | -41.94271 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a81492d0-a64f-3df5-97da-704852ec56f5 | -13.65398 | -43.93453 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 55bb1371-31b6-375c-86f8-0c5422b23001 | -8.21484 | -43.99809 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0445da67-bb44-3575-9ca0-0e0f4b17ae1a | -8.41825 | -44.73758 | 2025-10-16 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de8e2c04-4377-3591-8446-dbedd34d6f05 | -14.88529 | -42.13243 | 2025-10-16 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a6119a5-d4d4-39ba-bcf5-a1349c8dd531 | -7.95163 | -44.15191 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 91c35485-2f2e-3702-b7a9-318ce02e694e | -7.66296 | -42.38132 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 612077ec-1875-307a-bb36-8c2a34c34bdc | -18.73199 | -45.02802 | 2025-10-16 03:49:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a29a7f68-2f16-3f6e-a4f6-683982ed3305 | -8.24487 | -44.04292 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfaf7527-a4ff-3950-9cc6-f06cca7af77e | -7.07594 | -44.95455 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8454a625-b986-3645-99a5-888defc624e1 | -7.9334 | -44.13155 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d17a3414-dd9f-3b37-b7f7-cfc212b4ba83 | -7.62846 | -40.68916 | 2025-10-16 03:49:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6b93ad2-b8e2-3138-a08a-e9335845ee5c | -7.47208 | -42.1516 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c553f9e2-f6e9-3027-85e0-0c6aee8a1af6 | -7.95033 | -44.14473 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e5a5f8be-c67b-3969-8b22-071db650557c | -17.9385 | -46.72708 | 2025-10-16 03:49:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35336092-68b6-38fb-bb3f-c1466c052e25 | -8.39325 | -46.25518 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 711987f0-93ad-38d7-8039-6cb79f7d8b29 | -7.07162 | -41.95212 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aed415e8-cf09-3427-b475-1c5aa564ef6a | -7.0085 | -41.95741 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41792eea-ed96-39b7-94ac-5fcbd1773332 | -7.48216 | -42.14194 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4833e7b2-8919-3a6e-aa6f-94a981396a4e | -8.36438 | -37.59875 | 2025-10-16 03:49:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e90372d-1484-32ff-b110-20ed459b3c9a | -7.41092 | -44.75255 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50df33de-3229-3e6e-9f44-8f089bdb8048 | -7.67132 | -42.56171 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34214edc-7d7d-3854-8535-80b246ea8388 | -7.16316 | -42.51313 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 186b9935-7232-3e72-9ca3-98daf54b9ecf | -8.18771 | -43.96674 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3270c276-d01e-33c0-8962-b86a258ece05 | -6.98631 | -42.79612 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed8a7c7b-7ecc-3a06-9213-bf81fd358363 | -8.46043 | -44.18601 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| df249a61-d302-3dd4-87f9-de14326b1525 | -7.95716 | -44.14783 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52938bba-2919-39e1-a8fb-02f63a4362e3 | -13.63852 | -44.41806 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76425177-81f4-3d59-a750-80fb7e92e3cd | -7.21818 | -45.16579 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f994cfd-fb24-3175-9230-21fe3ff40077 | -7.54554 | -42.06237 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6239f1c3-dbeb-34e4-a380-a6d4ad9be828 | -7.0591 | -41.57657 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 626b95d1-a36b-3c02-8ceb-9255c7b15e7d | -9.15049 | -41.06168 | 2025-10-16 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58c343fa-72ea-3a4d-a7b8-efb787c3207f | -7.93187 | -44.12816 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README39.md)
