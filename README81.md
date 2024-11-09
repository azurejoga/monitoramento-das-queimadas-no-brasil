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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e2d4f7f-94db-3dc8-9adb-6ef8904eeb90 | -3.66384 | -50.25374 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8b87481-0a2e-314c-883a-844e5df0e2aa | -1.1286 | -51.94572 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e6a7bbb-645f-3849-a2cc-2c625a1c9ed3 | -2.83867 | -52.90594 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685a37b3-2ad8-307b-9a76-3860cc5a54f2 | -3.02919 | -50.35522 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9286e21d-d7a9-3d91-b8cc-9abd0425362d | -2.19845 | -49.12643 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea8e6e9c-30f4-3394-afc8-1b0241b51e9f | -1.52394 | -52.16456 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d844c129-40a5-378f-b0ab-e902ca71ffdb | -1.70944 | -52.49218 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0db6f447-4404-3dd2-b82c-7286233d657c | -3.3818 | -52.35824 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e0d90eb-a051-3d80-89f4-e3595f45e07d | -4.56372 | -50.26562 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e61325-309e-3a34-9f3b-9493ba4577f8 | -1.97638 | -53.13823 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5bc6dda-fc85-3946-9649-0833a5bea754 | 0.01608 | -49.44723 | 2024-11-09 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0502a99e-7ae4-3b37-89c9-1dcca4208e60 | -3.31163 | -49.63517 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6f35482-397b-3adc-a11c-236b4e672bb8 | -4.264 | -46.91393 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 437eb19b-74aa-3367-94f2-233121d1a5d1 | -2.23872 | -53.77036 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4903d34-8180-3d80-9c52-18bd059c2dcc | -4.23518 | -47.55556 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d38835a-7638-3131-b908-4468c17481e2 | -3.04228 | -50.36556 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e924258b-9e60-383b-8c76-a3398e364b6e | -3.73141 | -54.22147 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2b453ed3-81d4-3f0c-a121-d6756d5828a8 | -2.20307 | -48.36428 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3296823-7f45-338d-923f-a5f69b146c3e | -3.552 | -49.92062 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f1b459c-7d8c-3b96-beab-97fcc2d750eb | -3.80533 | -52.02164 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ddf4957-7cb9-3dc3-89ea-083ced5090fd | -3.06456 | -54.77665 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 967249ab-b80c-3c21-8bbf-5eb8d17a73b9 | -3.32839 | -50.08615 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3cb804cb-c8e7-310d-8386-0885ea88113e | -3.96328 | -48.17957 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 542a4d88-fd4d-32d8-99bc-971e283bd327 | -2.91664 | -51.05153 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af5630ef-4f72-31d5-a795-723e0b8d2949 | -3.97506 | -46.16415 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 45bab3e5-86ef-3e95-b4eb-429ea942e797 | -2.46371 | -50.39851 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 670cdd38-d370-32ec-ac9d-ee973080bedf | -1.52006 | -52.16754 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8341bda6-f126-31c9-a69f-daf857fa2187 | -4.20196 | -48.55114 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7bfef312-f3d5-3873-b362-ec4522e57bbd | -3.79689 | -49.94395 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9496942-df02-36f2-a75f-190806e9ae22 | -2.37351 | -48.58111 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e84a5b7e-7ccc-3818-addf-e0d66b981e76 | -3.09613 | -50.21709 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03456a73-c153-3caa-bdb1-179e5e214c7d | -5.17756 | -43.99963 | 2024-11-09 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b5d50a5-a533-3097-8e50-0db1af3db844 | -3.25003 | -53.36616 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67e9190-1e15-36e8-bb8f-929cff99baca | -3.26454 | -46.32035 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a4f03ef-627a-3d52-9cdd-7df676a82c11 | -3.08691 | -53.88537 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8b98840-04f4-3388-88de-c48aee8ef318 | -3.38236 | -52.35471 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1fcab7c7-b2ab-3077-b408-a88905af46e8 | -2.05222 | -50.72457 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75fdb871-00e4-3753-9253-dd12725496b6 | -2.6805 | -51.75827 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fedd78bc-f280-31fe-9dfb-e60859dcc837 | -2.89117 | -49.40913 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 080de80d-d73b-3fa7-acce-b14e603a0c38 | -4.62714 | -46.53538 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3397d7d-a459-3e92-8779-2b1ce2ff91a2 | -1.5615 | -51.66087 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f49098c-3d1f-3f30-8466-a9f4abb2521b | -3.34955 | -50.35875 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ce8cb223-46dd-35b2-8f42-e1cac35bf5b5 | -3.53964 | -43.56325 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e81291f2-e280-3e49-8d1a-95b35094454e | -3.67201 | -50.22489 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc22a60e-313a-3b97-946b-f6cbafe9c512 | -2.85794 | -48.44578 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaaab8ee-81b0-3673-b7f9-f71680c42968 | -2.56452 | -54.16797 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38c2dce0-bf77-3014-b9ee-ebc69e920bcf | -7.01374 | -45.61974 | 2024-11-09 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea1c816-24e3-3eea-803d-ff180b688577 | -6.27152 | -44.53696 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2f95e26-ab99-3ce8-84eb-3ec551e8f60c | -2.24951 | -48.22201 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c84b8a-a888-39d8-b925-43fa33193b87 | -3.83394 | -50.04719 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f467a37-c254-35cc-b9cc-d27ddd4ee837 | -4.36784 | -48.15396 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b09fef-196c-36e9-b316-8e1d8675385c | -3.97101 | -48.18453 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a851e699-335a-320e-b8e3-d3ecf62c5684 | -1.58862 | -50.43808 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82049ea6-e2be-3373-b8d2-426882cc8174 | -3.25018 | -51.13217 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a15bb033-7929-350b-ae54-2d8d97b98e24 | -2.41665 | -50.41998 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61475e24-8eae-32d2-bcb6-1b4a423c5511 | -1.87784 | -50.97062 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd7bcc60-5b86-3152-9ec7-c5deefb3d0d4 | -3.96173 | -48.13328 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2460ed95-7b6e-384b-b9cd-5be2aba575e9 | -1.63213 | -55.11306 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eafa5ba-c56e-352e-afb8-054e61575589 | -2.21425 | -53.73101 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114929bc-710b-3334-a396-096badadb02f | -4.01674 | -49.91902 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c42aecc7-1506-3c2a-be73-0280fb86e371 | -1.51852 | -52.22088 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f6ebda2-d4ae-3647-a352-293c79a4e197 | -2.67656 | -51.82767 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ed7ba1c-289a-3f9a-ab86-0131a6df1e83 | -2.05443 | -50.75642 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f88066-aeae-3260-84ed-e657d3655607 | -2.84875 | -48.45232 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca811b5d-7f96-326d-9e74-4475cfbf4098 | -3.30141 | -50.13988 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0dcd8c54-e056-36cb-9208-8cf9c2a0ab97 | -2.58329 | -48.18304 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f004cd-8387-3a26-b1cb-74b6cb8a6a17 | -3.26059 | -46.3149 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10dd70cd-556d-3112-884b-35c2d72d7ac9 | -3.38677 | -54.68386 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d225a512-a8a5-3845-b224-47719cbe2af0 | -1.14985 | -53.6568 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b4d5b8f-1475-3d69-9102-3f3016f42244 | -2.30974 | -48.31985 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4adad6d-10b4-3e83-b9e4-bfcbbb9c8122 | -2.21304 | -53.67402 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c46665b-6ccd-3741-98f6-178c78951cab | -3.89051 | -52.19285 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ac9dcc2-dc51-3962-ba06-80d02d23d647 | -1.5229 | -52.193 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 498ca25c-5f8a-333f-b2fe-5e4a69185c25 | -3.97326 | -48.16958 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f037fc29-8804-373b-b5f3-67c768fe9cf3 | -2.6952 | -51.68651 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7dcd04-81fa-35b4-aefc-6188b7e3b0a2 | -3.63773 | -50.18066 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d694065-0dae-3a2c-a0f2-44d5d7c9b179 | -4.06813 | -50.01535 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8a10b09b-d22e-31c0-8cf7-3c43f318484c | -2.1933 | -53.632 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39000f4c-605c-31b8-a44e-d86c429f089d | -3.32577 | -53.18718 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede720fc-e02a-3d47-a7c8-f956c7663c82 | -1.5005 | -52.55206 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f4ad1d-4deb-30e9-9a94-15b7c1a2f723 | -2.14647 | -49.13974 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90021b08-4ed6-309a-b13c-98a700d7c080 | -3.63345 | -50.18431 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aeda84a5-90ab-306e-8997-fcf885d06c74 | -1.42041 | -52.95269 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ee2c966-04e0-36e6-b80c-a2fca3244fee | -3.55982 | -50.51436 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1183f34-fc87-3f33-bbbe-36ad0509b545 | -4.73086 | -43.2514 | 2024-11-09 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cbcaa15-bfb1-3641-a7b4-797e2118ec14 | -1.95704 | -53.06819 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f838161-12d2-33fb-b6d1-898812b009a0 | -2.82227 | -52.96703 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c11b51ce-4f4a-3213-a9b2-e3cea1da2c82 | -3.70534 | -51.3847 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d6d5af-8257-30a2-90e1-02cb02dfc6b0 | -1.15487 | -51.99646 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3f3de2c-966d-3792-8b47-f755a57d7fca | -3.09929 | -53.97972 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7096cfb0-6b6b-312e-b9b2-0f7dc3a56910 | -3.04268 | -50.26893 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43aa505e-1d0c-32ae-b60e-d92df3bcb7f5 | -2.92598 | -49.35846 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81755a05-6c0c-32f0-bb9a-da6d80b181ec | -1.4548 | -51.46812 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc844930-3dab-3377-90ed-4ef75848aa8c | -3.53683 | -50.33009 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed65fc5e-145f-3933-bdf7-711d02628020 | -2.3299 | -53.62135 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46715897-b5fb-36ac-aaf3-a596da019550 | -1.49417 | -54.06595 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b5bbb8-d754-3edc-ace6-c15823c405ab | -3.82513 | -49.85838 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 86d1c4cc-3550-385d-80b6-090c6bfb7b1e | -4.22872 | -50.43369 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd11d6c7-467a-3079-8138-0f085b54e242 | -2.42486 | -50.4376 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cf0c990-deda-3add-97b6-a5f2d2c87beb | -2.40175 | -50.31194 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README82.md)
