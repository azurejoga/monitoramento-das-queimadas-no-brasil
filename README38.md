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
| f506ec75-4caa-3d9e-8c67-fbe3d7f62cf7 | -8.70008 | -45.20464 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7ac2d9d4-c4c7-39b9-ad61-dc2c55a1d38c | -11.11374 | -45.73882 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da0b19cd-ef7b-300e-84ad-68757ba74844 | -11.72791 | -43.65211 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7a6a914-8577-3252-a654-61304e1b5fbc | -7.87319 | -44.20704 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ba98b059-4041-3def-b833-070338ed01cc | -12.16906 | -44.70485 | 2026-10-07 04:02:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8680103-f16f-3f00-a74a-53bf4b6f24a2 | -11.10703 | -45.72054 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 338793d5-2fc7-3aa9-8e22-0a201478053f | -8.71091 | -45.20097 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e803ea1d-0ca1-3667-ac86-0862b09d756e | -8.58309 | -45.67161 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ee693a6-92d3-3f62-bccb-5e8350cb5e01 | -11.79528 | -46.70556 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53da66bc-ec2f-332d-abb6-9f1591601c04 | -11.00703 | -45.43808 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 128ad12b-47dd-3d4e-b91c-ce66008db64f | -7.97374 | -44.50337 | 2026-10-07 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23321734-098c-3a78-b13d-515e15d740e7 | -10.49161 | -50.43397 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cdb04c65-b0c7-357d-927b-3f464c1add4e | -11.32668 | -46.6759 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cf8d779-8c22-3c39-9b96-ae67fb2c8df9 | -13.75272 | -43.62177 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a6e7e16-5300-3aad-a402-fc969433dd70 | -9.25604 | -45.65012 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60c425b5-12c8-3c3f-a221-0a706e366cf8 | -9.87661 | -44.805 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be092509-90f0-30f8-a2e8-8da4a2baf54d | -7.87697 | -44.21304 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2d3c0dc0-8b74-3f6b-b03e-106c7c022047 | -8.38771 | -46.28709 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 911445e5-b2b2-34b8-b8da-551fa00fa17b | -10.48158 | -50.43135 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb473bb3-ec06-37cb-81a7-29872ee055dd | -11.38017 | -46.67701 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 539d835a-bc7e-312e-be7c-d123f72218f7 | -12.16091 | -44.69874 | 2026-10-07 04:02:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bc2c0bd-c9c8-3189-9180-c9d8a345f1ec | -13.75206 | -43.62543 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6eaa7a39-3b8d-3442-80b0-5ccbed9b62f3 | -13.63193 | -44.42661 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a348c354-aac4-3a58-a3da-3d72f6cc5f7d | -7.74864 | -49.20665 | 2026-10-07 04:02:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99ce0a32-8c3a-3182-b4fb-5d4c18300e6d | -13.66648 | -44.30978 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2906736-0e1f-3115-a035-e09f32309b71 | -12.46273 | -38.35181 | 2026-10-07 04:02:00 | NPP-375D | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0dca3750-fece-3ea6-aa87-d0e2a6f40075 | -11.1091 | -45.70941 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a54964b-1e51-3046-813c-f8240ac44d83 | -12.19141 | -44.70929 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bfd68bc-f686-389d-b936-3ea801c932f8 | -10.9736 | -45.40932 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d7ff122-df48-3ed5-b7e9-00994b62ba56 | -11.11478 | -45.73323 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33f8d7ea-77ab-320a-959e-82989a4e270d | -9.7921 | -37.32528 | 2026-10-07 04:02:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7cadd95-20e9-3cd6-98d3-5b96520dd34b | -11.37182 | -46.69283 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 177ca301-f83b-32fa-ba74-227d20427c95 | -9.164 | -45.10953 | 2026-10-07 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc458053-fe1e-393c-806f-70c257579875 | -11.64234 | -43.67299 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aebf18fa-067c-3577-b4c7-678f33705834 | -13.50676 | -44.37252 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 497eee75-9181-33f5-bb08-5ee1c4c194c4 | -11.66768 | -43.62432 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51dd2d7b-d940-30d9-b5ee-a78771b30c15 | -10.46831 | -46.82353 | 2026-10-07 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abd24c01-d377-39ff-a1ef-b1f6237f318b | -8.38237 | -46.28619 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f12246b2-3d32-3e65-b59f-b413060f7cf1 | -11.07346 | -45.6466 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1314d557-b615-3ff1-a559-e0b21feb2bf1 | -9.92355 | -46.80013 | 2026-10-07 04:02:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97bc096e-9110-3b67-bb4d-09b9d29b3c47 | -10.84579 | -50.656 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53dad579-cafe-3ee9-b37c-89f2f212be33 | -7.6074 | -42.37481 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6aa0239-41a1-339c-8134-5470a2a83bb4 | -11.07532 | -45.64758 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7da108a-a36f-3bcb-b5fc-ce81aec4db7a | -13.67931 | -44.2875 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9827fb3-1c83-3dcb-8bc6-7676ee046417 | -7.99017 | -45.49475 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7793f96b-2910-31c0-ae93-9109fb469bc6 | -7.97283 | -44.50845 | 2026-10-07 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec57782f-28a7-31e6-8f74-4d96e9a81c23 | -12.17386 | -44.72931 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa26d226-0e53-39fd-ba6e-e7c4593cbdd2 | -14.01227 | -41.84654 | 2026-10-07 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e6e9578e-79ce-32b8-8b75-bd0fcec8ea1d | -8.70989 | -45.20659 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8d0306e3-8ff3-3484-a313-7c3252854166 | -11.0784 | -45.64711 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f8aabdb-f99c-308c-8d43-1e241d6fc428 | -6.7299 | -45.80411 | 2026-10-07 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64eee18b-efc3-3420-9b2e-6f7515380562 | -11.23209 | -44.86408 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff2b34df-3188-3a7b-b41c-1067c858a9c3 | -10.06609 | -36.43401 | 2026-10-07 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1983c545-a740-3ec4-a0ea-5cefe0358005 | -12.04326 | -43.4412 | 2026-10-07 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11bbf22c-6fbc-33c5-be94-e384d5f4471c | -8.7447 | -47.8808 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18eb7ac2-9aa3-3af1-bc86-9406bbcd488b | -11.00972 | -45.45019 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccb43c37-863c-3a71-ba14-aab342330379 | -11.80043 | -46.70654 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a009dfad-fdb6-38a6-a95c-488954d3130b | -11.23951 | -44.87544 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e295aba7-109f-326b-86e5-c20971ca7484 | -13.38986 | -43.87582 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7720f5ba-d77a-3aea-b32f-357a2c6bec9c | -8.2823 | -50.2672 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3b0f351f-b3f8-3d6c-b6ab-01e91d2b2039 | -10.49043 | -50.43975 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7420a67c-3d03-3f2b-ba62-218fad74eaf6 | -14.78385 | -42.26907 | 2026-10-07 04:02:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86862221-31ee-3a03-8203-0d5b6aaf20ce | -9.87191 | -44.80417 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 586ef0bb-a0b3-3977-9d29-83d195ca08d6 | -11.01012 | -45.45429 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ed3749-5701-3393-b6cf-31b25b55114b | -11.71303 | -43.42186 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bca49ae-00de-33e6-a0c5-706807f9c41a | -9.80992 | -44.7903 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c0e088e-2bb1-3d60-abcb-feeadc83cbb1 | -8.07458 | -36.09493 | 2026-10-07 04:02:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b280580f-4774-3c5d-9f69-cc9ff7385cb6 | -13.02679 | -42.67486 | 2026-10-07 04:02:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0cc8d81-957c-3e5c-9f97-0b791a8fb7e5 | -7.81881 | -46.86238 | 2026-10-07 04:02:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08945a38-24d3-3d18-aab2-738e5b587f27 | -11.84572 | -43.551 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9cb1713-20d3-35ea-b336-f1eacd72bc5d | -11.84155 | -43.55021 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca60ce7-091b-3b02-8ab7-72982e29c8c2 | -7.40809 | -44.45549 | 2026-10-07 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d9d9f2a-0fff-35e7-82fb-cec367a0fb8e | -11.37244 | -46.68951 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 014b61ce-ca58-3b8d-b313-76cb09a00de2 | -11.78755 | -46.57919 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89e9e5df-318d-3e83-af1c-8e434bc72e2e | -11.63877 | -43.66853 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e08fcf7-2afa-3a35-8e3c-aafbc6a7864a | -10.47297 | -46.828 | 2026-10-07 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f8d5ca5-46ef-3ea8-941c-c926a23254a7 | -8.19437 | -46.34905 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74cc884c-6321-39fb-869b-7a992305bc6c | -12.21458 | -44.70921 | 2026-10-07 04:02:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7495788-8142-3da5-8c91-cb63a2820495 | -12.66922 | -47.4986 | 2026-10-07 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f33c2710-72bf-3954-9778-07ed842afd11 | -11.69983 | -43.66308 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a044d568-17af-3372-a6bf-455c514e7f4a | -7.87481 | -44.19769 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| de2ec3a3-1b82-3353-9b6f-4fb5f26bdb4e | -11.57933 | -48.44044 | 2026-10-07 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55395666-da6c-3529-b06a-28f51d0f80f8 | -11.79265 | -46.5802 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ea13e5-d50f-3720-b99f-5a7cee1a742d | -13.6327 | -44.42241 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d423653f-6b86-3b06-a082-53e00b161540 | -8.58619 | -45.66786 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b8b9298-4520-3b4a-bb20-397efbd26ce3 | -8.20038 | -46.34649 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831c2469-795f-384b-978d-633151408ae2 | -12.0843 | -48.11921 | 2026-10-07 04:02:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d1685f-1488-3204-be42-7bd65b067e13 | -11.78812 | -46.57621 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 667d1d83-efbb-37a3-ab98-2a70d135e727 | -11.06665 | -45.82771 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10d37301-73a5-3236-814f-a54ac16f6a60 | -8.21116 | -46.34807 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db511415-b940-37ae-a996-a204d0836de9 | -11.37755 | -46.69093 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f33fac04-568b-3d9f-bfcd-b09b7fc35696 | -8.70397 | -45.21117 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61e2466a-2eb7-350c-8923-a24313e982f6 | -10.85788 | -50.66484 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1afd9a4-2c28-332f-be97-2fd9a30d1dce | -7.61221 | -42.37165 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8e43326-e56d-3961-8e92-5f0711238fec | -11.0491 | -49.57492 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dec4d87e-17a0-3c6f-9dd9-4ff3aa531584 | -9.80613 | -44.78434 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5f9960f-f2b3-312f-9e85-0deab86c2f58 | -14.78753 | -42.26984 | 2026-10-07 04:02:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19308d6c-5f41-3d1c-bb72-53a63b042b45 | -11.05534 | -49.57623 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9edd1647-2d72-39ca-9f46-c002b1539374 | -7.27985 | -46.15035 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66192e95-78da-34cc-b757-6ed4ecba792c | -12.43782 | -47.99092 | 2026-10-07 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
