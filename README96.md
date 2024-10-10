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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0981ff00-caa5-37d9-a723-e7f4e582a2da | -7.67208 | -42.49716 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2d454b31-6cad-3c19-9c05-32562f1b6121 | -7.66846 | -42.49087 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e7423dec-d97a-3ac2-b202-51df14d037ce | -7.66819 | -42.48713 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3f8527a-fa18-3e99-9341-4f19b213ff5d | -7.66775 | -42.49025 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 75667907-03fc-3933-b9fa-a8ea8d3f3c4f | -7.66763 | -42.49714 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7059e35c-ffdc-35fc-a09b-5d3152a54d01 | -7.66366 | -42.48705 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a90a8255-68c0-3021-a312-c4fdf102b625 | -7.66239 | -42.41449 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8d1cc7dd-a398-3e5c-87b7-c2ab3985a228 | -7.66102 | -42.54685 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37166e3a-b017-3e53-939c-bd303db7fcbe | -7.65947 | -42.54917 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d117c43-61cf-3123-a2cc-01075fc1e85d | -7.65583 | -42.54613 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e577c8ed-c623-3596-97d1-7a519b97bdf4 | -7.65471 | -42.54541 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15582014-e295-3507-9159-20455627aefd | -7.65281 | -42.40665 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d22f4329-a06a-3104-a15b-6bdc7bc2d763 | -7.64803 | -42.4026 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 24ede84e-7bd3-39bb-ab64-a617b3ed77d0 | -7.64759 | -42.40582 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cbc0084d-9fa6-3698-84dc-d6193986b213 | -7.64237 | -42.40499 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2731042-6e58-33ef-8fa5-3606a4348ed1 | -7.64191 | -42.40829 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 591a7bf2-b8cf-32a0-9d77-d5f67ace051f | -7.63668 | -42.40752 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c7a1864b-69b5-3a5e-9a49-79a6030138f8 | -7.63146 | -42.40672 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8cb09628-1c52-34db-b788-8bb986549101 | -7.62625 | -42.40585 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6df711ef-e7bc-348d-9f28-9912091e7855 | -7.62579 | -42.40917 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f69ca313-5092-313a-83d8-adb351401d64 | -7.62014 | -42.41152 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c76450e5-3f78-34c1-8b97-f7f96d50600a | -7.22814 | -42.30351 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a21c99ff-b5e0-33d2-86b5-83058e06d3b5 | -7.22771 | -42.30661 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a81fece-8ac1-3fae-ac6d-839697fd6078 | -7.22377 | -42.29655 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 09d46fe0-2006-3928-bf61-d85c04e0a308 | -7.22334 | -42.29965 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3348a68d-8571-31fb-9c17-54f13cc435f2 | -7.22291 | -42.30274 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a445d836-9c26-34b1-99e1-b3a7cbb09661 | -7.22248 | -42.30584 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71f2aef1-35b2-34a4-82ed-2bfbf27501f0 | -7.11766 | -42.60927 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecd0e6b0-2a41-3f32-8c58-5e48a2c45868 | -7.11464 | -42.61046 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 618c2757-97e3-388e-a300-1902f67f7aad | -7.11256 | -42.60843 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2da3906c-edee-34c0-91cb-64c2889d6444 | -7.11214 | -42.61153 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32769500-3041-3b95-bd76-049bf6b9274b | -7.09197 | -42.62304 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e065a11-cdb2-3efb-b738-f1a3d4650a47 | -7.09154 | -42.62611 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7269f783-5998-3b0c-adb9-9ab16c97f713 | -9.30348 | -43.34934 | 2024-10-10 04:44:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fa068c7b-b1f0-3ca8-9194-5cf0749addd7 | -8.1509 | -42.96644 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d3e49ac9-f309-3bec-aaf9-a44963333774 | -8.14799 | -42.95961 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 60651923-3307-36ff-8619-84bc64bf8a70 | -8.14756 | -42.96261 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 8c94cafe-7c92-371c-bf9f-d1b409b3d446 | -8.14714 | -42.96563 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 670ee7b1-df65-3181-850a-cf570f17f6b2 | -8.14671 | -42.96865 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| bb9b87ef-9752-39bc-a3b1-cff92ffca6ed | -8.14664 | -42.95966 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| eab4cba5-a475-3cbb-8f7b-5d932b2293d6 | -8.14624 | -42.96267 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 6a4ae147-4c30-3bd0-abbc-05b79dc94eb8 | -8.14584 | -42.96569 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b6481d04-a6fd-3033-91d7-c74810940283 | -8.14543 | -42.96872 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 01143323-2cc8-3762-9756-382c69cda34d | -8.06223 | -43.84286 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e583ad54-15fc-3276-96da-adb08cb689e0 | -9.94324 | -44.07142 | 2024-10-10 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f04b8d29-5fc3-3520-90d2-34796615d3f8 | -9.9391 | -44.06556 | 2024-10-10 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cd2129d-60ef-320f-9de7-db3b2cc8bdd5 | -9.93462 | -44.06807 | 2024-10-10 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b90e4bf-bcfc-375f-b66f-ed8388e2c793 | -9.93426 | -44.06491 | 2024-10-10 04:44:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a30501ff-91e8-3ae4-8bcd-f7a03e0eeebb | -10.82518 | -43.79497 | 2024-10-10 04:44:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ef0ad51-4f13-3746-991b-a0b07f4cf05a | -12.29056 | -43.73434 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a4155775-ae32-39bd-b3cb-f3615038b5f4 | -11.52868 | -44.03056 | 2024-10-10 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9872afa-f69d-3926-854f-a3759954b60e | -11.52448 | -44.02424 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d622455e-eb75-35e4-8118-951e7bb2d844 | -11.52327 | -43.99516 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ba3ac210-b3d1-3d6e-b62d-f523460c2ea5 | -12.2843 | -43.7428 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4456ec3-a8fd-388d-8c9c-238d9d2507a6 | -12.2839 | -43.74594 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0438bf91-b6a1-3c37-a29e-f8378d4e16a4 | -12.27923 | -43.74186 | 2024-10-10 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73b79b3c-13b3-3cc0-aaf8-e41ab8634736 | -12.22998 | -44.00913 | 2024-10-10 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71e811ca-4c35-3c8a-b823-6afce194a287 | -12.22498 | -44.00839 | 2024-10-10 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e455f09-2191-3bbd-9f58-982bbb8ded1f | -11.52396 | -43.9963 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 456d3945-4b4d-3631-bbbb-ac35b9f3b510 | -12.29017 | -43.73743 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ead17162-ca01-357d-9a80-377ee7881aa7 | -12.28979 | -43.74038 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6a22c313-eb99-3803-aacc-691d2bc06a8d | -12.2851 | -43.7365 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 02e5e9c8-3e38-3b65-ba42-6070c4798dd9 | -12.28469 | -43.73969 | 2024-10-10 04:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 49fc09cb-7379-316b-9d8d-c20ec71f30c6 | -11.88889 | -43.88737 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 542e7b97-e37d-30f6-82b0-70e1c8792f06 | -11.83974 | -43.83409 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb6acc50-23cc-310b-9f92-ea247757948c | -11.52943 | -44.02491 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ca4b8c-1f78-31ea-9a3f-024a6f3b393b | -11.52252 | -44.00085 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 604faf8c-019e-385a-959b-4f8e4ee6dbca | -12.27879 | -43.7453 | 2024-10-10 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 245b3d07-98c9-3ec9-9908-16aeaec0ea9d | -11.89392 | -43.88804 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1d3224f-e37f-3ce0-ae01-58c4c5821b0f | -11.52538 | -44.02545 | 2024-10-10 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d73ef80-8115-3f83-b837-b4cb9be80447 | -11.52373 | -44.02991 | 2024-10-10 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9da4ba5-752e-3576-a42f-8af6c0154514 | -6.42927 | -43.7866 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43d3edfe-3cf0-3569-b3c9-b5cd6746fd4d | -6.35089 | -43.81705 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2554529c-49b9-3783-a6ff-6d32c2b0e4aa | -6.34625 | -43.81626 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 715052a4-676c-391b-9bf1-603ff0207bc4 | -6.34553 | -43.82137 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16b51596-5006-32e7-9ef0-b7e2dc4d65b7 | -6.32974 | -43.76466 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63df295a-4eb1-3a0d-a082-80a0ae957f15 | -6.32506 | -43.7641 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34a50863-3146-383a-ac79-8abeb1996f98 | -6.32199 | -43.76595 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f32c2520-dc86-3434-bad1-c07ea4620022 | -6.17073 | -43.70584 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e5f7050-7e1c-3f37-9c45-41ad092c2dc6 | -6.17001 | -43.71082 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e87e3616-cece-3f59-bc9b-03922362bf48 | -6.16534 | -43.71008 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 712474aa-66ea-35e7-8d29-e1e940d7c5fb | -6.14384 | -43.82637 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f6b84a-0d55-3d67-b281-b5f7eebbfe0b | -5.98794 | -43.48166 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ebf1f83-39a0-382d-aebc-13a89f020df4 | -5.98722 | -43.48664 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 777067d8-784f-3053-a95b-035510966e11 | -5.85263 | -43.73754 | 2024-10-10 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4faf7632-48fc-308f-bfde-d24a7018462c | -5.85191 | -43.74245 | 2024-10-10 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4a75c07-d75c-3b89-9882-ec13948aa0dc | -5.8512 | -43.74735 | 2024-10-10 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 176326fa-6d31-34b0-b7a0-f038edb4b797 | -5.84656 | -43.74664 | 2024-10-10 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 100563fd-6575-3783-9eb5-0371532d59a1 | -5.68818 | -43.63742 | 2024-10-10 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5af3ada8-96b8-3300-bfed-cf06a5639a67 | -5.56382 | -43.69895 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db074f4d-d3f5-3ad8-8e74-c7b551cd66be | -6.50512 | -44.3404 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8dd96fe-515e-3ed4-bdc0-60ec77144e01 | -6.44807 | -44.14956 | 2024-10-10 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41a395d1-f351-3802-b50e-7fe310d936d4 | -6.44099 | -44.26141 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce9d7a4f-ff99-38ef-94b1-c271d1a716cd | -6.44035 | -44.26579 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ced0faa-bef9-30d1-b7eb-93f2441af29f | -6.43972 | -44.27008 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89f276fb-0117-3712-aa74-42bdea4051a1 | -6.43647 | -44.26075 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0ab7374-8aa4-34ea-a65b-cde9a82e14a2 | -6.43583 | -44.26514 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4dc9d68-8969-3ad0-9296-c7ebd562852b | -6.43519 | -44.26951 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26d6d862-a133-3931-9bc0-c8c6bed68339 | -6.42432 | -44.43707 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8def0d9-3351-375e-9616-1c1509a34898 | -6.42309 | -44.43449 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README97.md)
