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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d7e865e-3f3c-398d-8654-731fefd9f504 | -11.07212 | -52.02108 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2643c1e-a39a-36c1-97ec-3ac80f5e70b3 | -12.52152 | -53.82225 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 678ecf4a-8be6-39b4-aa7c-263f4536861e | -9.43542 | -60.54 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7864b955-a8e0-3a0e-8aa5-dc6d941b319e | -14.61637 | -48.06623 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60f85d28-3644-3bac-b191-0c6ce14d2d38 | -11.05687 | -52.05289 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c074b0-3e79-3dca-b43d-7457d9a3d3d5 | -12.63338 | -57.00368 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb2ee75-e002-3641-a5ab-b66af8afaf2b | -7.94799 | -46.39141 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 913a5bcd-4926-3e1e-aa92-cfe58dc62aae | -12.43251 | -63.92179 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f35cf5e-99ab-3497-a5df-b4c5b32ca5aa | -13.50013 | -46.97264 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d22a7b3-aa23-3d9f-8253-c9f6ac88d72f | -12.84066 | -48.08271 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7672abe3-2034-3723-a307-4b0489e2afa2 | -7.9511 | -46.41594 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 640dff7b-565f-3971-be09-733a9b7e990d | -11.36284 | -43.54954 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48eae1c2-f903-3dae-b89a-ddcbae397760 | -8.91484 | -62.42145 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2ae2fc5-3a29-31f4-91af-9829cbd261df | -10.1417 | -48.47424 | 2025-08-31 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c72c7af-c64a-3d6c-9c67-fa2e456ff193 | -11.83631 | -46.42491 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f87030e-0dd3-3d65-8c11-78dd9302bfab | -12.3106 | -45.69565 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efaf7ee5-c330-3ed2-a258-8ca0a1149c49 | -14.34434 | -51.88228 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 490f734b-e8ce-3db4-b7dd-5da4485f22ad | -9.68083 | -62.25085 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba90a7b-14ab-3847-a5a2-c7f3fcb51b8d | -9.69229 | -47.04206 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1100bb2e-3798-3c86-94a1-067c58ac7bfe | -11.01895 | -46.86295 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b12c1ca8-6139-3508-b62f-c1c88da7caec | -9.69452 | -48.29448 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50bddf7c-1635-3eb7-8316-4e82d5c39914 | -13.34649 | -46.97979 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f78e9142-49d7-3a18-a41d-27e42e92a1a9 | -10.4844 | -51.62722 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e79fd462-74bd-387f-9083-89d6352761dc | -14.53837 | -51.98751 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aed0347-10d8-3fa4-897e-de23cf8645f0 | -10.04062 | -46.02668 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61aff693-f278-3576-8954-3bd1d4f0d4dd | -11.82215 | -46.53495 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6eaae06-217b-3890-80de-50bbd4038478 | -7.70681 | -50.27256 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0283b9cf-3b9b-37df-a45e-c34176d23a84 | -11.23635 | -55.06326 | 2025-08-31 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de8ce7ef-eee7-3214-8a94-e61df6a783e0 | -11.31966 | -43.68979 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1471da23-8e86-3219-9fe0-39462cef9452 | -11.90133 | -46.69239 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 892b0782-df93-34b7-ad63-318d17b7a5eb | -14.03974 | -44.56253 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d691a6cb-af7c-3ad0-941b-12cbcfcbeba5 | -11.89607 | -46.73092 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cd180e6-2c33-36be-98b1-103a138742e8 | -13.31307 | -46.94481 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3012fc-1017-3b16-98c7-a7cce98412b5 | -8.97037 | -50.03308 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff7cb31c-9553-3cc4-9347-cad6d0f874c1 | -11.90299 | -46.43149 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16385d8a-cec1-35cb-bd3a-1a76dc33fcd9 | -10.60718 | -54.91927 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c35540e-94cf-3c87-b1d3-a32373d10654 | -12.43678 | -63.92889 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 33e1ac76-f904-3fe4-8e79-4556191fdf40 | -11.88268 | -46.72506 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df0ae451-1f05-35b8-a887-bb690ebc2576 | -10.03896 | -48.08958 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50deef14-aa92-3e9d-a833-f4d60c8564ef | -8.88717 | -45.0955 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 438ec82b-8073-3950-b169-ce4547615121 | -11.82532 | -46.42551 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a4727633-f6fe-3dfd-b3a9-d4cbdc279d6b | -9.25479 | -47.05697 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dd27790-499e-3289-8f91-7821c8fe5bc2 | -8.8833 | -62.38449 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2574a8c-e639-3334-99b3-c79a6b4c78a9 | -11.77701 | -47.39909 | 2025-08-31 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fa2ccd8-afa9-378e-b8fe-0db5d8d8119c | -13.6743 | -46.93282 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6bbc5d8-cb4a-3524-9ea5-fa1ecc28ef16 | -8.35047 | -52.53209 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92cded0c-938d-32f6-acff-8ef63886a8d1 | -8.65314 | -62.82834 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94a5b0d9-3eec-3913-87d3-6a8108f09aaa | -10.04185 | -46.02362 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4cd74a5-28b8-3f9a-bc8a-5144d47a4aa0 | -13.32076 | -46.88511 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95075d2-d357-3dc8-8a67-e72d4f9362fd | -9.43482 | -60.57005 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2b41c8a-8683-32d8-8e08-cf1f632d5425 | -15.07392 | -48.62238 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2c5be0-06f9-3b2a-86dc-2b360700fe13 | -13.49607 | -46.96714 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b393fd80-2666-3c2c-be67-9fb77356bdd6 | -11.89537 | -46.37953 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 149d2ae0-81c6-3a26-93ce-fd0c036991ed | -11.05856 | -52.04171 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c17e3453-31ea-3b8f-a37f-ecf2c72cb162 | -11.20934 | -45.036 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 090c9790-c67c-3f88-9352-27c26b598462 | -9.00457 | -63.62946 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 366e9094-a33b-3e1b-9033-afeac5e68f9f | -11.8975 | -46.4727 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba849b10-5dcd-3d2b-a8c2-7fec992aea5f | -9.81913 | -63.85236 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf0d0400-b376-3bcd-b6ac-6ce782dcb8af | -13.53901 | -46.96618 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b256465-5d18-3c6b-9724-7557754c357f | -8.64703 | -62.83092 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7632d59-dc6f-3dd9-9c05-b0b91f1bc07c | -7.95309 | -46.38754 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 381f94c5-10f7-317e-8b3a-a4fd2494eb78 | -9.43397 | -62.3583 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ad00946-8e22-3e61-9d92-50191626cf02 | -11.36088 | -43.56561 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00b2eb51-9a08-37d7-9505-f83bcc64f47d | -14.54714 | -51.97657 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b53dd80-8afe-3b42-a07a-f0ddfa6c8b05 | -11.36115 | -43.61084 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb721335-8abb-3a0c-95c1-140cac4abb42 | -11.30255 | -43.66626 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4b7c74e-889d-3c67-9111-d7cd16d2b2c8 | -14.48936 | -53.00206 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29c82899-0286-37ae-81cc-fafe0541b6a6 | -13.98532 | -46.31529 | 2025-08-31 04:51:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 566644dd-b2ba-3f36-b57d-d84c32d4f860 | -10.03029 | -48.09139 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0147c132-d60b-301e-a742-14e909fd7f91 | -9.46363 | -62.34396 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d7664c3-50ab-33f1-b1a9-4b46873df572 | -12.49226 | -53.83557 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d04fc0e-c6ec-3abe-8a70-3cb53bd261c5 | -11.08063 | -52.05666 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9bbdeb6-4528-342b-b4b3-b570387e34b9 | -9.58776 | -54.47694 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93cbca3e-5e86-306a-8316-27717bcb4872 | -11.00798 | -46.94622 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 861adbe2-2cde-3ea1-b516-8bf205d6c336 | -13.68495 | -46.88784 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c9e977e-5975-3115-8318-48515cfa83d0 | -9.43173 | -62.34119 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b814985d-a5b2-38a9-8754-52d0fd0729fe | -12.61415 | -57.01466 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de96055d-1de5-3e4f-bcce-6e0a4dadd34c | -11.38491 | -63.2788 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a1b71e-ba3f-37b2-b3fb-d0bdab17a6bc | -8.67649 | -62.4236 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f040f16-89d7-36da-8e9d-a581d9cb3d2a | -8.49686 | -44.74583 | 2025-08-31 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3f40031-a950-3e68-a223-860c346e030b | -8.90207 | -62.10239 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e1ca2f-533a-3bd1-9935-e3893fcdf9f6 | -12.31022 | -45.69856 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05702b8b-a69a-3ef4-beba-003fd1d8fbcc | -12.56719 | -44.79817 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 936f1640-aaba-3d94-a2a8-c2d277b08297 | -11.90354 | -46.39095 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4979f5d6-a914-3c25-895c-a5869567c9a0 | -13.48313 | -46.95663 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4894da57-8e98-3c76-bcb9-8fae6b7d67f4 | -12.63268 | -57.00779 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7f5f745-1f95-3c21-a95d-37e0a2b4d3d1 | -8.66994 | -62.42931 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8d82b8-fcb5-3028-b1ee-be87771ee3bb | -14.48992 | -52.99837 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31c4c2b6-7237-3a7a-b810-172d3462135e | -14.3379 | -51.87718 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2baf513f-c0e0-3319-8d58-5c28a772e444 | -12.40534 | -46.46614 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 606297c2-0345-36df-8986-5c0c259102e8 | -12.82779 | -48.08086 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38cc4699-f0f4-3eae-87fc-149076c15867 | -11.35211 | -43.63752 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b2992d55-1471-356f-8ffd-12977a3b5f12 | -7.97187 | -46.41713 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa267ea5-3ff1-39a0-a7b0-174679391dce | -14.35405 | -53.27132 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57e391b8-0c2b-3cfd-9fb6-a8cdcc5fea5d | -10.13204 | -58.01826 | 2025-08-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7caaf37e-25f9-398d-ab9f-107c14920512 | -9.45394 | -60.54334 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 224b2dc5-b450-3374-bf7d-a9b1c210e717 | -14.26803 | -51.90816 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7ece92b-e06b-3b53-9340-86b1074d9736 | -10.13873 | -48.47261 | 2025-08-31 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 089ce2cb-82a7-31f1-8680-2e3d704add65 | -11.06649 | -52.05825 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1d784fd-e0a5-32a9-856c-7acef881a4fb | -8.68056 | -62.43141 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
