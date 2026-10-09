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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc9c03a-ab4a-33a5-a4a0-b191699ac598 | -11.58932 | -43.64937 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b0cc21d-0e27-358d-9e19-d7245dc0df65 | -11.65163 | -43.68294 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e4acc5b-d24b-323d-825e-ce7d421c80c0 | -11.76893 | -44.95481 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83ab38f0-2437-3de6-8689-846030fba17a | -10.9937 | -45.40567 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2ddd6c7e-03eb-39e6-b0b6-b4f7802f109d | -12.02641 | -43.47209 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95e40c3c-57f6-355a-9379-88f1a263de70 | -11.17928 | -45.31689 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70678cb-fb82-32a1-b73b-712383e5eaa5 | -13.62869 | -44.42778 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 59d700a8-c565-33e4-8830-e2cc85901de7 | -11.57677 | -43.68711 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b8b4992-e929-3471-b1a7-22c3aff53353 | -11.75948 | -45.47651 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da6df7e-e548-381a-abdf-2b8e48347dc9 | -9.01837 | -44.38096 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1464120-2d6b-342a-9a2b-90d5c2a71fe8 | -11.64986 | -43.69239 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99ab2b07-5232-3c0f-bdb5-ba8ca3597819 | -9.30325 | -47.42582 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 212ba03a-8e7a-3b17-9c2a-7a9ca4656c80 | -13.75451 | -43.62796 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 313449ed-48a5-3906-b320-f6a0cebab14e | -11.77816 | -45.56742 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a4a685-c57c-3ef3-9330-3f2ccb2ff03b | -6.87434 | -45.9094 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eef266e2-bc6f-334b-b976-61baea2c2e8a | -11.26142 | -46.27658 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abb657bf-4f06-3ec0-a682-329c4284fc91 | -14.39554 | -43.81459 | 2026-10-09 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54035650-ab3a-3331-a230-ad86e8e104f7 | -8.3253 | -45.44999 | 2026-10-09 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa6473a6-6669-3538-b3f1-ec34cfac7ac4 | -11.09399 | -43.99884 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb5f3538-22a7-36d4-9337-3a42c340ce6c | -11.65493 | -43.69357 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ba5dc64-7906-3b07-b12a-8e2c1860830e | -11.86722 | -43.60479 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39cbf8a6-640b-3245-831b-4f82aba902a2 | -8.98999 | -45.91333 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 784453be-e73d-32bf-a9b8-25eb6f7a663c | -8.90911 | -45.22701 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9ef5e6a8-ff5d-3953-9c31-5dfae2b31a93 | -12.01836 | -43.45981 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b20a700-959b-30f1-ad49-ed9a690c025e | -9.89325 | -44.80005 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10a4c41e-8c70-379d-992d-f195b8b9d2ff | -11.99955 | -43.47726 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e39c981b-0666-3732-9c41-df6316203ebe | -11.61951 | -43.60181 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2adf22af-6279-3ac0-94a5-b17918c5892e | -10.28787 | -46.61772 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8da5778-59d8-36c9-84ce-3dc184b33e48 | -11.66936 | -46.77417 | 2026-10-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 844957b8-f723-3525-a2e7-fa28135a97c6 | -11.63914 | -43.69313 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dc4b937-92c7-30bd-94eb-809cba2ac0c2 | -12.01888 | -43.45703 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 735d5fb3-21ca-332d-b3ed-acda7f7e14a9 | -9.91815 | -44.79237 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8113b62a-6048-3eaa-a423-63b291a75753 | -10.99285 | -45.41005 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51192ac5-4583-3474-94d8-cd35d681124b | -13.36705 | -43.89211 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0031ebae-9ed5-3f72-99e0-5bcd1185c09c | -13.25272 | -42.25539 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| bbdea81d-df29-3417-beae-10cda25ee88a | -7.41077 | -44.75643 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b925893c-73e9-3f5e-a9f5-ed8308cd12fa | -13.25645 | -42.25376 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 7c8e1cfb-2d4a-3a32-8c45-a22c2588672a | -7.18776 | -44.27888 | 2026-10-09 03:45:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0245f2c-53e5-3c09-afcf-275eabbd73a9 | -7.50214 | -45.76572 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db60fe41-4f6c-3c7a-a31c-fe7e6b0a1e51 | -11.85374 | -43.59301 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9477acdc-b15e-32d3-82d0-d2591cb23f70 | -11.46346 | -43.39154 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35928257-7664-398d-87df-7686a692d38c | -11.22012 | -45.32037 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a63bc43-9ba9-34a3-8bbc-e94079b286dd | -11.6064 | -43.6983 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb68ef95-38ad-3b22-a1ff-b6ed4bad313b | -7.39309 | -44.75331 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 16ce0386-8e97-35fa-a7d8-7ca5dbfade76 | -6.87713 | -45.89451 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2d8652bb-7be9-3376-b70a-d831608e07f2 | -9.29542 | -47.43027 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97d4c64e-c5b6-32ee-9ab1-70e93cbaca20 | -14.43915 | -43.93702 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c607322-369c-369c-9f6a-dc15a1d1eddb | -10.86035 | -45.53808 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b72eeb85-f993-3087-b977-fb263b7239a7 | -11.21702 | -45.24496 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 948ace93-87b8-3c44-8ac7-a334bf31f42d | -9.29766 | -47.46777 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fbdbd2e-f87e-3e17-bd51-62860cea477c | -13.34728 | -43.96882 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82d223f2-3af9-3a81-9410-1a52310dd0cd | -11.05487 | -44.05978 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07d72eb9-f067-3ee4-a10a-30fdcd6f8ff7 | -7.28803 | -45.41685 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bd5693b-e787-3ae7-bfa1-cb078a86c76a | -11.74141 | -43.6409 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99996aa3-1934-3d16-a675-6cf99dd78f04 | -10.59233 | -46.42028 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d34cf7f9-65b1-3db1-85e9-c01c1d84d5f6 | -12.81352 | -44.6554 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b72518f-db9b-399e-be49-25227d533d5c | -13.16022 | -43.27953 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 9932bdd0-87b9-310e-a872-e4bc7a2c6b05 | -13.25377 | -42.24981 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| a8d0e876-09dd-3271-bbad-0d2967102e9d | -13.50333 | -44.37063 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ceded2fd-736a-38f8-a991-044b39f90dcb | -11.25055 | -45.25458 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6804dc02-2e62-36bb-9bed-27a40bb96033 | -13.4999 | -44.36686 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a82464f8-b96c-3d93-93a0-673ead130387 | -11.83976 | -43.58391 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3ecafa3-a861-3355-91dc-5bb2b0591949 | -6.96015 | -45.27896 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 33e55af6-df41-38cc-ae9c-4ab293d7d1bf | -7.48559 | -42.83875 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48c69791-fb95-33cf-9779-7e5fd5652d1b | -9.34781 | -46.5799 | 2026-10-09 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25360f8d-db3f-398e-b414-f426362305d1 | -10.8595 | -45.54249 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7b403856-d310-37d3-a2ff-3d67b1b614ce | -8.72702 | -45.13581 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e93d1d5-32c5-32e2-b9c1-d0a7013ca39a | -9.02047 | -44.36971 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2cceb6e-fddb-399d-b7f4-3c0abdc8acc5 | -8.72204 | -45.16198 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18d130c7-824d-3ef9-a961-201f811187bc | -8.7262 | -45.14014 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bebcd063-fc50-33a9-a942-383db8eb1df1 | -6.95903 | -45.25013 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42629016-3254-31b2-9f20-24ca8e45dd3c | -10.59473 | -46.41479 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f41116a-ec78-3574-903b-732c91e73a2a | -11.78071 | -45.58465 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56be8df7-9d5a-32b1-b991-e40a5a1c1c27 | -11.58189 | -43.66051 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8f04212-08b8-345d-b010-23b3aac2775e | -9.11911 | -45.83223 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 840c8390-377b-3087-ac89-f1edfa672009 | -10.93211 | -45.38327 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba0f572b-d24f-3aeb-b43a-8b30132f9694 | -11.60909 | -43.71198 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 662c5282-d906-3e8e-91c3-f46d955f4057 | -11.58248 | -43.65746 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 679cba70-a258-3332-b0eb-da0c731b19ba | -13.49693 | -44.37611 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc7b823c-1434-3382-8af1-cc0a498b1556 | -11.19069 | -45.3192 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f82a6559-2a52-319a-8b9c-3ce5a5d3f3a0 | -11.0073 | -45.42949 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7737ee1-ab44-3949-83d2-c3ac80c02439 | -12.58194 | -42.22576 | 2026-10-09 03:45:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 37db8145-a439-34d5-8b8e-5c7206e3d259 | -8.90992 | -45.22264 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85510373-831c-3c10-bd94-f785b449b617 | -12.00301 | -43.48639 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c60a8ca6-a4d5-3af1-8ccf-2cb5d8f07890 | -13.11233 | -46.33482 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3da4331-df47-3298-a377-d90147969e77 | -13.80998 | -44.19124 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a64b613-f02e-3ea6-a12e-5bc1e761780a | -11.06802 | -44.08383 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96dbf4ba-eb95-3090-8f79-0bf4e307a440 | -11.61328 | -43.60689 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2339944-bbd4-3f89-a589-d69fcb6a7caf | -12.0356 | -43.4505 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a05b85d5-36bb-3efe-80f8-d022cf202930 | -12.02719 | -43.4402 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ffa85a3-8013-3684-ac95-7c5fa3eb4628 | -11.99699 | -43.49078 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7523162b-a7b8-38ff-ab3f-9b2c4878fb8a | -11.64301 | -43.70068 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b251316b-b7fe-337c-92a3-866436484b63 | -8.7363 | -45.15127 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9db9054-e641-3a7b-a0be-cd0135c4a423 | -8.97009 | -45.91272 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41830dde-371a-3d2d-8e43-0f17bf43b883 | -13.36607 | -43.89272 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a85d0e2-3215-382b-9c1b-0db15417698e | -7.28714 | -45.42163 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a72f2f05-c174-34e4-98ea-4fdc8f01cbeb | -12.02607 | -43.44623 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34363205-1a58-36a4-8454-93150a0e4c92 | -8.91745 | -45.21499 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d653f71-9987-3d36-ac20-2d54cb60e7a5 | -13.78979 | -41.02539 | 2026-10-09 03:45:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe0e54cf-e4c3-3b3f-8e7f-fea666b7d626 | -9.91324 | -44.78735 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README68.md)
