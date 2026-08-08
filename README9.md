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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abdd36e4-d813-3a24-9a70-128c674c3ad2 | -4.52747 | -38.54613 | 2026-08-08 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3851b9e9-2f05-3975-97f5-13fbe3ee03d2 | -2.48897 | -47.08477 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c948384-b56d-3fb8-924d-18becf7d4316 | -4.52862 | -38.54839 | 2026-08-08 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c57f546b-4bd4-3a92-a9e2-6b334ab36e07 | -2.76619 | -49.46557 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23dead34-192e-32b6-915b-7a8d22eb4e74 | -3.19834 | -49.05954 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75404c71-47c2-31fb-b1fb-e78c9cac5585 | -2.75151 | -49.46804 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c4636d2-3e96-3bb0-98b5-c7572f12fa5d | -5.42895 | -43.42693 | 2026-08-08 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d42719a-452b-3eb4-9504-3db6933027ef | -2.69829 | -47.36291 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a991d34e-cbd5-30aa-a4a7-2a6254dd2f45 | -2.82793 | -46.72206 | 2026-08-08 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5725b18e-2d9f-3ba2-8b46-ef286a6be534 | -3.95401 | -48.12234 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3bc09cd-ac7b-305d-b9d9-5b5b501016e1 | -4.52672 | -38.55091 | 2026-08-08 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2f798f6-f67f-3b8a-8243-9d97178e2849 | -2.69427 | -47.36225 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdd7cf88-2034-3def-bead-0f9023cecd9e | -3.05217 | -39.9279 | 2026-08-08 04:23:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8b99e189-2c70-341e-a84e-114406585cb2 | -2.419 | -48.63723 | 2026-08-08 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc77ffdc-271b-3bf0-bc6d-df8ea0cc7ff0 | -4.36906 | -47.76876 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bd074be-fd80-32bd-ac05-3ecce8c3cd26 | -4.27424 | -48.19611 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59ac863e-1ef5-3bed-996c-efb68b5df493 | -2.8293 | -52.30499 | 2026-08-08 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a513ae3a-77f7-3d41-8832-b19db6e36833 | -5.52568 | -45.78511 | 2026-08-08 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3e94b87-615e-3b4b-8fef-9f3c90a8e706 | -4.4603 | -47.91768 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 178a1ed2-de7f-3ed1-86e3-63caa87a265a | -4.46435 | -47.91835 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 384d821e-2fb3-337a-a782-5b75271524ae | -4.36846 | -47.77229 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 612fef62-c515-33a8-943a-35c369f004bf | -4.60079 | -45.58516 | 2026-08-08 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae78dbc1-a278-36f1-8128-a0b6e562c406 | -2.41971 | -48.63293 | 2026-08-08 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a338e63-0eb0-368b-b5b1-4f8a930f3ebf | -2.83178 | -46.7227 | 2026-08-08 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf307c17-0137-383c-8ebf-d1082775f66b | -4.64436 | -43.12497 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b21032b-6f61-3779-ad19-77dc5026aa9e | -4.64713 | -43.12895 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c729d89e-1e80-3df1-a0b6-eea2dd7f2b37 | -4.52476 | -38.54781 | 2026-08-08 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ec4ebc75-2398-3d54-a9c0-a9527424fa79 | -4.26344 | -38.03519 | 2026-08-08 04:23:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1849e0b4-3355-31e7-8d0d-b18e09a4da80 | -4.89039 | -37.50269 | 2026-08-08 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d3a3259f-67ae-3dee-a416-f7f046b02fdc | -2.72435 | -49.78907 | 2026-08-08 04:23:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187787cf-e1fa-3475-82b4-44924e6f2272 | -2.48977 | -47.07978 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a417d546-ca6e-34ca-8911-77417c7e0b8b | -4.38243 | -43.3671 | 2026-08-08 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0336bc11-5068-32cc-bda8-44a754704708 | -3.95817 | -48.12293 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc9eb3f-481e-305c-8224-5e2026380fc3 | -4.26716 | -48.18725 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ad43b8d6-225d-34bc-a3e4-881c43b2b237 | -4.27131 | -48.18795 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4e60b6e0-3486-3dec-ae6a-dd29d22c5857 | -5.2719 | -45.16812 | 2026-08-08 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8629022-7fdc-3fca-9f4f-c129a04b25c3 | -2.48501 | -47.08411 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36c686af-7d83-3cf2-bebe-a1ace37efb66 | -3.42427 | -41.72323 | 2026-08-08 04:23:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9536f2df-275a-34a3-8a4a-072739d9edfc | -4.90474 | -43.4683 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e38d390-6b9a-3b05-8526-83fadc4cbf39 | -4.69941 | -50.44185 | 2026-08-08 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda5f02c-9e61-3b01-8562-1730314a8563 | -2.76 | -49.47442 | 2026-08-08 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f75cb6-652a-337d-b3bb-759d89843cea | -2.77082 | -49.46634 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f130cb67-d730-38ff-8b3a-29ba800ca7d4 | -2.79257 | -49.52636 | 2026-08-08 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45bd61b7-58f0-32a4-9be8-69cb29e3e3da | -4.69463 | -50.44091 | 2026-08-08 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b41b9209-aedd-3e64-bb2b-318003d19c79 | -6.91224 | -41.96825 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e42f90bc-c3e7-3304-8dd0-805bf1905eb4 | -12.5574 | -46.93111 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88aa9e38-ed1f-307a-a549-3b59ce2dbaed | -11.8809 | -40.96392 | 2026-08-08 04:25:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5af1f283-cbde-3624-bc97-e59b5a0700d0 | -9.383 | -47.09084 | 2026-08-08 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd0742d6-3a99-3fcb-be91-e9be8b43d714 | -11.24005 | -54.02229 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33aba927-fd3a-358d-b18c-46463b3ec28b | -6.92421 | -41.9623 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6b0a7cc-d0cc-31db-a2bf-a2c8e17b0479 | -6.92426 | -42.42624 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9eef8dad-9971-3b04-9b80-bd30132971d8 | -7.18378 | -42.33979 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 06ee1793-33a5-3b58-a5b6-be4519371c44 | -6.98353 | -42.9062 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1641cb69-2393-3362-a25c-b956a7281e9c | -6.90549 | -41.96715 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae77096d-db3a-3480-97f4-1b080f88c7b9 | -11.24564 | -54.01974 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa590958-bba1-3075-8e37-77e5c13bcf18 | -8.35453 | -37.28506 | 2026-08-08 04:25:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4b00737-7336-322a-9b2c-c72d588b1e53 | -8.16072 | -55.41538 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf7184a1-006b-3f70-bfa0-df90511d55f5 | -13.95271 | -41.87259 | 2026-08-08 04:25:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee66c6ec-9f10-3816-be1e-b991eea009f7 | -8.16225 | -55.42403 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4dc8d1f5-afe1-346c-a024-9b9d2dcdec89 | -12.54093 | -46.94422 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2c3bcd97-4c14-3d0a-b810-e32276917b6b | -11.19181 | -54.8426 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3177b89d-6f9a-3285-aa2d-e04aaf26f155 | -6.91393 | -41.95748 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75cfee60-7ee0-31b5-a483-6a6285560b16 | -7.08332 | -42.26599 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46139cb2-a499-3f07-abc5-f0e84b83a53f | -11.01841 | -50.53757 | 2026-08-08 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 339d9c01-969e-38f3-9af8-5f62404532c4 | -6.30561 | -52.81578 | 2026-08-08 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769c10f2-bd08-3ebb-a4c7-ded224cfd657 | -12.54179 | -46.96037 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 159bd42c-b82c-3a32-bd7f-df9685b6f9fb | -10.50877 | -46.6258 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca831be4-ae06-3706-85db-503651a98558 | -11.78016 | -46.38906 | 2026-08-08 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd40a4ca-ada4-3aa6-ba7c-8b73a085b749 | -6.89317 | -43.71365 | 2026-08-08 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35779497-6a90-3079-b7aa-014a22909cfa | -11.03892 | -44.2731 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1eb43b38-f608-32a6-8721-e4ae6a6e5f24 | -8.62107 | -50.02792 | 2026-08-08 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bf10e75b-8963-3cfb-9b46-f608344aeb6b | -7.18366 | -39.29211 | 2026-08-08 04:25:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4cd9e85b-7370-368a-b575-669999054f09 | -11.1168 | -50.76876 | 2026-08-08 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6e31e33-c489-3249-8921-148581e75f3a | -7.15864 | -44.06705 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff58e229-de7d-3d69-acb3-3f1160dc0dd0 | -11.72627 | -50.12817 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e98591e7-0806-3b41-99b3-3c0fc2a36af7 | -10.26042 | -45.8062 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e75714b-27d4-30b8-a6c3-1944e89413a8 | -12.33558 | -53.15608 | 2026-08-08 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18279923-0123-3429-9b40-43af38d9dcdc | -6.91202 | -42.43875 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9364d14-690c-3775-965f-27ea56671005 | -8.33017 | -46.38799 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ceb8d10-36e6-3fba-9abc-2f6dbc37407f | -12.56151 | -46.92784 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b76f1f5a-1370-3aa9-99e8-45904264f0d0 | -12.32996 | -53.15807 | 2026-08-08 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84339b68-03fa-30c5-a54a-4e45f0753b22 | -9.3823 | -47.09504 | 2026-08-08 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 944e265d-ffee-34aa-bfc6-3c07403106e2 | -6.9512 | -41.92213 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b9574db8-af13-350e-a3d5-8125cb69bad8 | -11.03449 | -44.27958 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4d3ceb0-8d7f-3982-b178-74a6ee205d21 | -7.18295 | -39.29683 | 2026-08-08 04:25:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20cbb270-36bc-360a-be51-5aa842b4c976 | -6.91981 | -42.43277 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04bcbec6-5f3b-3fdc-a48a-ab74015c8d4d | -8.16167 | -55.41047 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7136965-4912-307c-bff0-56d142a10dca | -11.03504 | -44.27607 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2e52c622-461c-3b06-acc5-51dc37875fa4 | -6.92036 | -42.42925 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2888aef0-3597-362f-bccf-c3cc270a8afb | -9.63382 | -45.51218 | 2026-08-08 04:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb5ae858-0495-32b9-9d53-f89e71c8a6e7 | -12.5509 | -46.96999 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 857157d6-14b2-3688-900e-7ee2a57d50c7 | -6.97639 | -41.49142 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fde68b53-1b12-372c-9048-5dfc9c530da2 | -13.37115 | -41.35239 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2e6f7cfb-d1a0-300d-93f2-66ab44c1ee38 | -6.94785 | -41.94379 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c785506b-bb01-35ac-9901-1748dfa08e44 | -13.38949 | -41.34863 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6dfddac2-7f2b-3863-9933-876811fb31cc | -12.53136 | -46.95862 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb528cbc-4a72-38e0-a4eb-cfbe1ec45037 | -12.54286 | -46.93266 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af78f4ee-51e4-3b6d-8249-beb539ca0ab4 | -12.8508 | -44.38951 | 2026-08-08 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ea8d92-bb0c-3aa7-9cae-5475a1e1227b | -12.53853 | -46.91597 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1ef6858-74db-3676-a9be-799f8da87b52 | -7.77462 | -49.48569 | 2026-08-08 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
