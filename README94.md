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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2544905-d810-3b64-9854-f048d618be1f | -3.4233 | -52.80947 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 769bbf29-3728-3bff-979c-77e1f385def6 | -3.29882 | -53.35571 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac175767-7992-3e70-814f-21754f9a88dd | -3.29488 | -53.35511 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0911fe6d-4a19-3a35-b984-6852cdd34646 | -3.25254 | -53.34581 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c484915-366a-39d4-9a9f-b5b8e21b9045 | -3.24598 | -52.63449 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d510a516-f51a-32b5-8088-ecae1a53c483 | -3.12804 | -52.92762 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0f25902-2108-37a5-b79b-bf03c1fc6722 | -3.12725 | -52.9324 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a76d64b-e800-3658-8c5a-2af436f20ea8 | -3.12572 | -52.92947 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4489c75-3212-3d96-bfbe-919cf8f7cac9 | -2.9543 | -52.78258 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e52bd9e-6872-3042-981c-fa1ff3c6453e | -2.95355 | -52.7872 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b17ff35d-852c-30c7-b63c-45a5b590e2d7 | -2.95048 | -52.78195 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f03ef17e-26f5-30b4-a5a5-575c6910f908 | -2.94973 | -52.78657 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c305300-6934-3b74-9bfa-15fa38c8805e | -2.94591 | -52.78593 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6aa18bf4-ea5f-3339-a4c9-fb89f07ca2f6 | -2.94419 | -52.91737 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19b92065-25ae-38ea-b3a1-d48321811132 | -2.94033 | -52.91673 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 586fb0d5-33ea-3b47-bc8a-541013a7471d | -2.93724 | -52.91144 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6f4ac5b-9895-30a9-add0-992074b649ec | -2.93648 | -52.91611 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdd5cd74-b332-382a-b314-9394793515ac | -2.93457 | -52.79106 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14805b21-c6cf-3e5d-88c4-2c903c271465 | -2.93366 | -52.78881 | 2024-10-05 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd39a70-ce4c-335e-9c82-c962266e9531 | -2.85473 | -53.31774 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a170247-e4b8-3cad-a229-3c03ac84098e | -3.8442 | -52.35855 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48ada487-e242-3efc-a2bd-d0450f692dd4 | -3.84051 | -52.35795 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 46d9c142-bfc6-3f3f-911c-4ee8d50b7a94 | -3.82351 | -52.3461 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6172fc35-5a00-358b-ad01-ec1fe6eff457 | -3.81962 | -52.32332 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96b302fa-24ce-3a17-b0e3-ec1178a0ee42 | -3.81275 | -52.3894 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b71dd5dc-18ac-392a-90cb-30bce07d016d | -3.79227 | -52.30578 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a6d8eb9-75bb-321b-8af5-a505044ee86d | -3.77492 | -52.27814 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d11e062e-26bb-329c-94a3-c08e0caf9cd6 | -3.77446 | -52.27631 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be2d1717-8bea-3b0b-b027-c99db61cadb6 | -3.77124 | -52.27757 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d468510-bbd2-399b-b2c6-808b0abb8562 | -3.75862 | -52.26214 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f311b19-8450-3fcf-9608-cd94e5d23a4b | -3.72412 | -52.43125 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8032bb6d-338c-34dc-9686-88901ab748c0 | -2.14484 | -53.65141 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57baeab-2e4d-3233-ade7-94f7902b854e | -1.21162 | -54.52525 | 2024-10-05 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2313f5d-8c47-3b44-aa55-6a56a8284f31 | -1.20789 | -54.52025 | 2024-10-05 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31d8033e-da59-31f4-871c-c49b808b3a01 | -1.20722 | -54.52454 | 2024-10-05 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 881fad75-45dc-3ee4-bb17-9cf779c817af | -1.18671 | -54.20792 | 2024-10-05 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7a1056e-19f5-3259-8ffd-d03a4ea692ea | -1.1646 | -53.78401 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7f505db-b40f-3471-9f6c-60abcdf40f51 | -1.164 | -53.78776 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a80db1-dd16-3888-82af-13824faabe6c | -1.16044 | -53.7832 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 242c0cae-dba2-3b0b-8a53-d4faabd4abc4 | -1.15985 | -53.78685 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a37c07ed-2171-3dce-8ae8-a11a4d210ca8 | -1.13076 | -53.63947 | 2024-10-05 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 397786ab-b744-31cb-9358-eb13d59943ca | -1.12723 | -53.63488 | 2024-10-05 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26091822-7b7c-3962-af27-7fb243916bbb | -1.12314 | -53.63384 | 2024-10-05 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e00ae400-fb99-390d-b586-7a0f2a85f4d4 | -1.12255 | -53.63755 | 2024-10-05 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cfdcc1b-35b7-3d62-b565-3b6e329c489e | -1.03778 | -53.54193 | 2024-10-05 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e95ec9d9-35fd-392a-b3be-aeb0c0108474 | -1.02463 | -53.73393 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b759369-d321-3380-a6da-294bac05c9ef | -3.06487 | -54.77659 | 2024-10-05 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a1a0568-0e6e-3fb1-abfc-8949ea649b53 | -2.97487 | -53.72713 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b484902-524e-32f5-83bc-aac7082ec32c | -2.97081 | -53.72646 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4e658e4-7835-39ee-82a9-4688788f1a93 | -2.96618 | -53.7294 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08f09d6-b938-3632-bcde-549e4aab8bff | -2.94878 | -53.70821 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5993d43e-0aca-397c-8815-a46df419ec7c | -2.9482 | -53.71178 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b615bad8-b86f-3f6d-9496-a610b2362304 | -2.93778 | -53.69912 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c4a1b04-9266-34e0-9f74-1156d6f421d2 | -2.93372 | -53.69846 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 961fe5f8-188a-32c5-bb3d-e68daa142d98 | -2.89836 | -53.86407 | 2024-10-05 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3f66f1c-463f-3aa3-8da4-8a233cc7f947 | -2.81698 | -54.71504 | 2024-10-05 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b5f984d-76cf-33d2-bf16-4bb593503b41 | -2.72263 | -53.97682 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d443acb-8eec-3aca-9406-839debbb0ece | -2.60326 | -54.21098 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fd27fda6-25fd-3dfc-8e2b-537de76902d9 | -2.60299 | -54.21198 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0773b443-b199-3452-ad83-475dfc159000 | -2.3166 | -53.85944 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c88dad-7222-3e52-9842-77e001875f8a | -2.31601 | -53.86316 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b062e1f3-f206-3bf7-a514-ef31e15d0a0d | -2.31247 | -53.85876 | 2024-10-05 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65781453-7e46-34d8-a23d-4d07a6264dde | -3.87398 | -54.22809 | 2024-10-05 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17695002-3a3f-3ae2-a3a7-01831d72fee9 | -3.86925 | -54.23114 | 2024-10-05 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd0f6490-a76d-31ae-9556-7eee86463d9c | -3.86864 | -54.23491 | 2024-10-05 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e675214-bdc5-345f-9ffb-d2020d4433bd | -2.18674 | -55.13189 | 2024-10-05 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03318a49-ab41-3c2f-a1d6-f60ba921fcfa | -1.82531 | -55.18823 | 2024-10-05 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88ea0a14-dab4-383a-8188-1b4d3d58c152 | -3.10012 | -59.3723 | 2024-10-05 04:36:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eebcd90-5a2f-344b-be4b-722f107fb9c4 | -3.09495 | -59.36679 | 2024-10-05 04:36:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff3e3967-2f56-3974-bba1-1c8c9008a2fa | -3.09421 | -59.37117 | 2024-10-05 04:36:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 941cc591-ebd0-3dec-98b6-1514dfd09913 | -3.87001 | -59.74241 | 2024-10-05 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b88f0e89-ef46-33a9-866d-7ae8dcbc4336 | -3.86402 | -59.74134 | 2024-10-05 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d2d6ff-81b2-334b-9113-3f4c3d3dc5c7 | -3.86325 | -59.74579 | 2024-10-05 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 238a735f-1526-36b6-ae2e-5b53a080a7cc | -9.8802 | -59.5008 | 2024-10-05 04:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8b999c12-1bb9-34d5-8b61-910f5e89d626 | -10.3131 | -50.5128 | 2024-10-05 04:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 2046ddbd-84ac-388b-85fa-749e0b1129d8 | -11.2754 | -60.5814 | 2024-10-05 04:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 33ed2d07-e3e6-3765-b4af-edd4b9e78084 | -11.2566 | -60.5825 | 2024-10-05 04:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7aaf41f6-8304-3388-b637-fe4678150c34 | -11.896 | -56.9354 | 2024-10-05 04:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d2f819e5-d168-39c8-a68f-5d4fcab647ab | -11.8957 | -56.9554 | 2024-10-05 04:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 4eba8fc0-1820-38e1-8b77-5b1763341b33 | -11.877 | -56.937 | 2024-10-05 04:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 17fc6c89-9a2d-3ccb-bd35-b59c34edc856 | -11.8768 | -56.957 | 2024-10-05 04:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 9313c0df-8fc1-3910-95be-17c41c3eb6b1 | -12.763 | -50.5352 | 2024-10-05 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 554119a1-807f-33e7-b532-11d8bcf15651 | -12.7819 | -50.5543 | 2024-10-05 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 365.3 |
| f944de46-ef31-3980-91e5-9663498233f1 | -12.7627 | -50.5567 | 2024-10-05 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 048b2c84-d987-3829-89b9-05522b4c2601 | -12.7822 | -50.5328 | 2024-10-05 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 224.0 |
| c5ab52aa-e87b-3d7c-a571-acb78b1e5466 | -12.801 | -50.5519 | 2024-10-05 04:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b9020574-040f-3b46-8ed0-d45b848ed5f3 | -16.554 | -57.2237 | 2024-10-05 04:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 7672fb76-a8c7-3f60-a403-c08cd56d45d4 | -16.7647 | -57.4856 | 2024-10-05 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| cf0814d7-c977-3ebf-8826-2492baeab8d7 | -16.6871 | -57.4536 | 2024-10-05 04:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 1352cc60-13e2-3133-b17b-24a4d6d49156 | -16.7843 | -57.4834 | 2024-10-05 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| dc842f40-0938-3c0a-8ac4-285b409b63ca | -17.1235 | -51.7238 | 2024-10-05 04:36:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 122.3 |
| e137d2fa-8460-3c61-ae4b-b16f2da39dee | -17.1085 | -56.7892 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| c768b157-b1b3-3f6d-ac24-beddca04cec0 | -17.1182 | -57.4039 | 2024-10-05 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.4 |
| 21ca7e24-3a9e-3ec7-9bb7-6409f7c62c40 | -17.0512 | -56.6932 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| bd935f62-11f0-3f37-afb5-64956821a9bf | -17.1178 | -57.4244 | 2024-10-05 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| 5c21af23-1dbb-3567-ac7c-1c8e2ed70a01 | -17.012 | -56.698 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| c56cc5a7-39ff-3429-91f9-6a6dd794a36d | -17.0123 | -56.6773 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| e46d4327-b06f-3315-b0f1-63bbc54acf93 | -17.1378 | -57.4016 | 2024-10-05 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| a5de6845-fb0f-3060-abec-fa4291b610d3 | -17.0316 | -56.6956 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.6 |
| c5efccdb-8057-3b58-98cd-1b04cb5c38d0 | -17.1375 | -57.4221 | 2024-10-05 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.1 |


[Clique aqui para ver as próximas entradas](README95.md)
