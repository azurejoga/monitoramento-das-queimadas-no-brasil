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
| 02f5e4a6-41fd-382b-960c-e56c4019ad61 | -12.2729 | -43.51032 | 2026-05-06 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8601180c-2cbe-3623-a0b3-8dc287534dd6 | -11.12261 | -45.11377 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a1f7843-1c03-32fa-afca-4e315e26895f | -11.61541 | -48.05534 | 2026-05-06 04:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 74c78224-44eb-377f-ace5-b1de08084f0a | -10.48425 | -49.36136 | 2026-05-06 04:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20db52d-4a99-3be2-833d-f5a1d504f2b5 | -9.59026 | -40.42475 | 2026-05-06 04:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15700f54-3718-3fdd-bcd7-bdd1c9bd4321 | -12.51037 | -46.67307 | 2026-05-06 04:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12efe174-03c2-3124-b60d-8bf1cfb90edb | -12.39229 | -46.3258 | 2026-05-06 04:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfb2ccc3-d405-3277-85aa-1b1a69fe53f2 | -11.79749 | -43.61361 | 2026-05-06 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59760222-9c24-3aa9-bf71-60c8e05a3094 | -13.22706 | -40.13263 | 2026-05-06 04:04:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5496b5a3-54ef-3f64-83f8-c4b70ce31c66 | -9.68017 | -47.02602 | 2026-05-06 04:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 870ced82-c49a-32d7-b844-793685e9ac17 | -11.1256 | -45.11909 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8a60e5b-a336-311d-8bc5-539f8faed8c0 | -11.99652 | -45.3415 | 2026-05-06 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 771e1871-1223-302e-98bc-b9b3121c5d32 | -12.39292 | -46.3222 | 2026-05-06 04:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d350a4d5-6f89-33eb-8918-74fa038333a8 | -9.46772 | -47.79937 | 2026-05-06 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 982f4719-b097-3c4e-a7be-84b870afe423 | -10.93554 | -49.43299 | 2026-05-06 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbe1a424-be3f-3f5b-be26-3a3acd2d635c | -11.41615 | -47.07839 | 2026-05-06 04:04:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f2bd313-41ca-3aa6-b5ce-19293c1febac | -12.26944 | -43.50972 | 2026-05-06 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f499b04e-f584-37fe-b9a1-d2af1f23de8e | -12.33206 | -44.59255 | 2026-05-06 04:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a38c7aae-4ea1-32cf-97e1-7f03efecd228 | -5.78604 | -45.12909 | 2026-05-06 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a983600e-cc24-37cc-9752-ff435f2d1a9e | -9.68093 | -47.02169 | 2026-05-06 04:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7191c154-e763-339a-945e-929790c35173 | -5.78665 | -45.12533 | 2026-05-06 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af1b0297-89d3-3fc1-8310-48ad98f064f0 | -11.12605 | -45.12133 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3991271d-348d-3aa4-8973-e800872fd339 | -8.61958 | -49.52368 | 2026-05-06 04:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 539c60fb-dc7e-3687-936f-0019af97a468 | -11.84461 | -43.96404 | 2026-05-06 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 813505f3-1ec9-3503-8c21-8eae51f67de1 | -9.25166 | -40.2456 | 2026-05-06 04:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 526bb23a-a646-3935-b3ac-89b965a0148a | -13.22425 | -40.12848 | 2026-05-06 04:04:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1ad8fe88-e8e9-3f3e-88e6-6cd1d469a8cb | -8.15699 | -46.66332 | 2026-05-06 04:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ab8af9a-1ef9-3306-ba91-3eaa9bfd5c09 | -12.27009 | -43.50584 | 2026-05-06 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec32c7ef-9349-3281-8104-b18eb15728a6 | -11.42112 | -40.63637 | 2026-05-06 04:04:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a6168ab6-d86f-3f92-ac5b-3a236c4cca4e | -12.27356 | -43.50644 | 2026-05-06 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94deff63-b416-3efc-82ab-7761a3855bcd | -12.82898 | -43.77961 | 2026-05-06 04:04:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8ff18b1-2923-35fd-af98-498f9f7d9220 | -11.12382 | -45.11133 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d467510e-828a-3f12-8813-d4e5dc399749 | -12.15218 | -46.66162 | 2026-05-06 04:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0a63f4f-1f0e-3f12-ad35-ce58b322f8df | -9.59081 | -40.42126 | 2026-05-06 04:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0045ed1d-75fc-3210-9288-3c9e0778e527 | -8.22594 | -43.87786 | 2026-05-06 04:04:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8fce4603-799c-3f5c-a453-f5d07ecd0912 | -10.93107 | -49.42892 | 2026-05-06 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61a5ae26-af8a-312c-95f7-8e32d5b4d071 | -8.15336 | -46.65823 | 2026-05-06 04:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffe0b270-85db-3de3-9338-b7d2e2278738 | -10.9361 | -49.42997 | 2026-05-06 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac6ab009-2538-311f-b535-7f1efcfb52c5 | -9.46446 | -47.802 | 2026-05-06 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72a0b14a-a1e2-3af8-93b3-adc6e2ff27fa | -11.68103 | -44.8708 | 2026-05-06 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 139f8aab-9af3-37db-ba38-ef6cc4da4327 | -9.46217 | -47.80346 | 2026-05-06 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57686fe0-f213-3bcc-9663-841810fb97f5 | -9.46683 | -47.80422 | 2026-05-06 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2d13603-b24a-3485-acfc-c78e5a67bb41 | -12.19466 | -38.14117 | 2026-05-06 04:04:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0dd724df-4e16-3487-b1fe-86dffe6e2be4 | -11.99757 | -47.77443 | 2026-05-06 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 679c5e1a-6036-38f0-893c-d6a5335206e8 | -9.36691 | -47.67902 | 2026-05-06 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31a3c855-8b0c-3c80-b571-054c6555ef66 | -12.1375 | -40.8961 | 2026-05-06 04:04:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1036a8d-ac7d-3f04-a3ff-a9f7254ce4ea | -11.80034 | -43.61815 | 2026-05-06 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b19cd724-29f8-31ff-af12-b0745a0922e0 | -11.13374 | -45.13982 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7e54d3dc-143c-3582-a857-7d1b4ac93136 | -11.12993 | -45.13917 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a60500ae-79c6-3a9a-831e-b8f4f6aeed11 | -11.99676 | -47.77887 | 2026-05-06 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e334fb18-ae41-31d8-976f-e0ff102fc1f5 | -11.61454 | -48.06005 | 2026-05-06 04:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9203328-ef4a-30bc-b485-e3da4401ca53 | -10.58708 | -44.33204 | 2026-05-06 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e76d291c-0ac1-34f6-93e0-23eb7f6aee96 | -16.76751 | -45.81686 | 2026-05-06 04:06:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17661fe1-a065-35b7-9ae6-fe98d9010c77 | -11.2955 | -54.02957 | 2026-05-06 04:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5852e869-c680-3ae7-8675-ccf43877ae30 | -16.41834 | -54.91381 | 2026-05-06 04:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 951524ac-c673-3421-8388-f96c051fe848 | -14.07111 | -47.75613 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01b712e2-66c1-388f-9508-cd59ad5cc03b | -18.0766 | -46.36561 | 2026-05-06 04:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22c7a5f0-27ad-39b9-997e-b04f21309bb8 | -12.45778 | -54.45185 | 2026-05-06 04:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f454eb1c-0227-3ae7-8610-a71b9c1f767d | -13.64959 | -45.55624 | 2026-05-06 04:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ef4988-83f3-37e3-aa9a-acb02102e0ff | -14.14758 | -45.35819 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0af2df84-1099-3c37-a7e3-a3aeb40ab911 | -16.4247 | -54.91545 | 2026-05-06 04:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e8394fb-5cce-3b6a-8735-02b6021a2671 | -14.07872 | -47.61949 | 2026-05-06 04:06:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05a7e83-d9df-3116-9da3-6febabe83553 | -14.08217 | -47.62455 | 2026-05-06 04:06:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fd0eb23-2d3f-308c-87f1-26f30c0e3d37 | -14.13651 | -45.35619 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 858cb042-7317-3adb-a44f-6aff283b3a74 | -14.06883 | -47.79258 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81331d2f-2863-3724-aa3b-f08534a60524 | -13.31818 | -43.66885 | 2026-05-06 04:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f52d62c8-4a92-38e0-ac05-f813a079cebc | -13.79599 | -43.34534 | 2026-05-06 04:06:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 037654ce-a1a9-31f7-b930-b15368fe694c | -16.42334 | -54.92158 | 2026-05-06 04:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 980260aa-2e58-3cb8-ba48-2c49e4be4159 | -13.65323 | -45.55971 | 2026-05-06 04:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68e0ced7-c73f-3644-924c-17e0d703a8f8 | -13.69587 | -55.68359 | 2026-05-06 04:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 433f0967-6f7a-3be2-bc90-de82c29bf008 | -18.2371 | -45.66747 | 2026-05-06 04:06:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9076dad-8ddf-3d7b-a091-3f02c8d4bd6b | -13.6503 | -45.55438 | 2026-05-06 04:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac75ce72-75f5-30bb-b4fb-28d21fe11ead | -15.98443 | -56.22197 | 2026-05-06 04:06:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 344b63f8-4a5f-347e-91f8-e5010178d221 | -14.0005 | -47.59655 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4910bbbf-4877-3e7a-b4cf-a218e2b565c9 | -18.0758 | -46.3702 | 2026-05-06 04:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 237df752-d232-381a-9b4e-5db57806d7e1 | -11.43913 | -55.1014 | 2026-05-06 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03af0092-5a1c-39bd-9b06-fcfb5d8c77b5 | -14.07462 | -47.76109 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebc2710c-3559-3fe1-8771-15c486b54278 | -17.2864 | -47.78666 | 2026-05-06 04:06:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a6c4134-b817-3f1f-a888-27f0a59219b0 | -13.43874 | -43.84486 | 2026-05-06 04:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3e795d84-c4ac-3f2f-86b5-ea219b1b0df7 | -16.10622 | -49.23413 | 2026-05-06 04:06:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32823bb1-27b2-3b4d-bab6-d6ec3607ab30 | -13.99631 | -47.59553 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1d3df51-626e-3ed8-a8d7-3c642c085c1f | -12.45903 | -54.44602 | 2026-05-06 04:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2af151bc-6ea8-3f44-9caf-9ba48153c311 | -11.43058 | -55.10699 | 2026-05-06 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9350d26-858e-3c87-bc4c-053f87d457ea | -14.85387 | -48.53928 | 2026-05-06 04:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f364d200-94f7-3de3-9d3b-5d3401e5c5ef | -12.34649 | -50.02031 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f635b958-3566-38aa-b5ed-d27c3a216334 | -13.65255 | -45.5616 | 2026-05-06 04:06:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42f609ed-13dc-37a1-8e4c-15dcc5eba93a | -13.69433 | -55.69066 | 2026-05-06 04:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25cc9a7d-da92-305b-b1cf-98e52aa88184 | -15.97906 | -56.2136 | 2026-05-06 04:06:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5002d199-9d47-3944-926c-5984d7f574c1 | -12.34317 | -50.00995 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3abdcd2c-f87a-364c-a297-eb7b0722d4a3 | -12.34981 | -50.03068 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75639abe-46de-343f-b705-de68a8f92f25 | -11.63415 | -54.16685 | 2026-05-06 04:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0362cd8-52ca-34f5-a351-083bc5094ddc | -14.14468 | -45.35302 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b8a65cf-a95c-3239-90db-8bfdb4335911 | -17.53399 | -47.02212 | 2026-05-06 04:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53e8c55a-1b50-35e1-ab10-3262aa5bd5eb | -14.13281 | -45.35552 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f1c9973-4726-3983-9337-43dd0cef0def | -14.85499 | -48.54118 | 2026-05-06 04:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1f80ef6-b8fe-3bc6-8769-a4fe6e039c7a | -13.29013 | -44.2093 | 2026-05-06 04:06:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 811f111b-a00c-3bb0-b460-20fcf0fd0622 | -14.1402 | -45.35685 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 380fd32e-86a4-3e3c-85ab-50d1de5ad80f | -16.41693 | -54.92013 | 2026-05-06 04:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47e2b218-1906-3af1-8f6f-5269c3043f5f | -14.45821 | -46.98907 | 2026-05-06 04:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3be4bc2-41ce-3b12-bcfc-485d3e3d53b5 | -17.53231 | -47.02441 | 2026-05-06 04:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
