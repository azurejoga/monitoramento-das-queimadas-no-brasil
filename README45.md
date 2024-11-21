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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1d9be4-1222-34f6-9ced-2de5153bc270 | -3.71054 | -51.1852 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 861fdf92-6c9a-3d3b-bbaa-b58f3962aa4d | -11.46035 | -48.00925 | 2024-11-21 04:31:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f103ff72-4761-3aa6-a53e-c91e7fc6ddcc | -3.70746 | -53.75097 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7d84aaa-1119-3f00-9cd2-42bb2a8c5a53 | -3.80115 | -52.22481 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b0f33ea-ba7e-32b3-9938-76571f7a5c6c | -4.8514 | -50.85997 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dce05f72-6e1f-367b-bc30-6fa046eece1a | -3.83036 | -50.29183 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 028da987-d0f0-3cce-a7c9-247130ded971 | -9.19574 | -43.03244 | 2024-11-21 04:31:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65aead80-67f7-3513-86f8-ab0caacafc3f | -6.06949 | -44.15062 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bccc8fa4-3548-33b6-9e9c-4460d94ebc7f | -4.53446 | -48.46114 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a378e4a0-f322-3d80-a8b3-b91c7fa460a5 | -4.38836 | -47.75853 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 883e5076-c473-334f-ab86-fe3ed59b0b9e | -3.64719 | -51.45777 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45fa35ea-2fb3-3b07-8700-80a2f544b336 | -3.29704 | -53.85284 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 820ee758-5503-38eb-86ec-af7db945d24b | -3.53797 | -51.61123 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6d8fce-51f6-3189-b905-f4869cb5e73b | -5.19376 | -47.74024 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79f6989e-8962-38c0-aed3-51d025bbeeb5 | -4.55351 | -50.22918 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85855650-5f5a-379f-9626-04b83f3c9738 | -3.28375 | -53.85389 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eacd4f6f-2980-3986-a251-981b391ef5af | -6.29681 | -45.33541 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0115035-479d-362b-9bf4-50ada6f8fd21 | -3.24378 | -52.82931 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b749a8-ae7f-33a5-8d15-dc20d5bfd59a | -3.80523 | -52.2254 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52b6f3ee-ad51-3f36-ad49-b23cbb00a5bd | -4.57713 | -48.0205 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 10f23665-4a74-3e46-a981-f85e2e6a28dd | -3.86325 | -52.3271 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40fde3df-07f3-39b3-8ec2-91cb5059f0af | -3.9109 | -53.82516 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ae775a0-d611-3313-97c8-a75be9b9d7ca | -3.51599 | -53.80457 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 731ce729-ffc3-34ab-bb2c-91e12fd923a3 | -3.75312 | -52.67221 | 2024-11-21 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d5a6f4-ce9f-3ab1-a855-ed2f45c4902f | -3.75721 | -55.57346 | 2024-11-21 04:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d924d778-1ca1-3816-bc00-f2dfbc8af476 | -7.38762 | -42.7783 | 2024-11-21 04:31:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0b111884-c9d4-38a7-b317-610c6b4e136d | -3.28722 | -53.8274 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3168cfb4-c1dc-3a87-ac15-9f54d70b7210 | -5.59883 | -46.53923 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2392f2a-9bf4-3c41-aeeb-edccc6a64a97 | -5.31967 | -47.30639 | 2024-11-21 04:31:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7207b631-1786-3c95-8f92-a179286da5a1 | -6.61203 | -42.38287 | 2024-11-21 04:31:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0695003a-e45c-3a64-bc60-4720aa3df38c | -6.57345 | -46.75507 | 2024-11-21 04:31:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e880e07c-90f9-3eae-8f2f-eac411bedb66 | -4.95958 | -49.84301 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bee088f7-aacd-3eeb-8ef0-12c2be2551e6 | -3.99 | -49.92203 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10b29ab5-be36-3a2e-a2fb-05fce2440d6f | -3.8823 | -52.23803 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 719c3589-2b15-3c62-96be-910b8e9fee34 | -6.87287 | -48.67524 | 2024-11-21 04:31:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55389923-973e-35c0-aa34-55a9d9442a2e | -4.56975 | -49.61693 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17fd4029-9929-390f-9847-012e5ad27362 | -4.60134 | -47.03387 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f18327-adfb-36f8-ad54-9b8648d2e636 | -3.37766 | -52.46119 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0c8a1c3-7bc5-323a-9321-e64820fdb9aa | -4.63959 | -49.54487 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abe9f650-9eac-3472-aefd-e9d318b8c190 | -5.95036 | -44.24797 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2fd3f65-b9d5-3726-8cff-4de3951a4912 | -3.91452 | -50.11721 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ee1a52b-6a1b-3392-8db4-4c65cff4607e | -4.5512 | -48.01638 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ed1cfe-fc62-3b97-8c68-a8f5748bf744 | -4.76851 | -44.49519 | 2024-11-21 04:31:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d513cd5-6ee6-3420-9451-65deccda1b35 | -4.05335 | -50.34158 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d5ff39-7255-3604-8a0c-cc2cace0abc4 | -10.23472 | -49.30485 | 2024-11-21 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7022865d-b20e-3870-b2cd-a0f2fc096a05 | -3.04331 | -54.40605 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478881e9-5c9f-3f97-8da2-c3fe86476d9c | -3.79718 | -52.4026 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14bb82ac-17e9-3c52-839a-a5bbac2f60f9 | -3.53498 | -51.60877 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d17f9a8-7b79-3ef7-8059-481288a7de31 | -4.7236 | -44.43053 | 2024-11-21 04:31:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 191ac905-b51d-320a-9e7a-0bd88a0f542f | -9.40731 | -43.31425 | 2024-11-21 04:31:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44aa5348-b6fb-3608-a74a-aa06745b8803 | -3.80544 | -51.26477 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13cf1245-b9c6-3842-b386-c746f92f1574 | -3.62111 | -51.09232 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cdd3aef-fcb9-38e5-ad8f-a004b6dc9171 | -6.82327 | -46.77171 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 553abdd3-6ad5-3d4c-b91f-e85d98bccb46 | -5.18316 | -45.43464 | 2024-11-21 04:31:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e8c30a5-611e-33e5-a199-8cb7a5e236a8 | -3.61525 | -52.11763 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d86ca269-5cf8-3a2f-bc47-8f90edb127c9 | -4.58047 | -48.02103 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 111087ce-f170-3cc1-a991-101200eaa8a1 | -5.25139 | -43.5402 | 2024-11-21 04:31:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6ab432d-678f-3d3f-b2cf-c5c2a159a939 | -3.61218 | -54.74623 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d92df2c-8bc4-3f63-8906-86bf9889d2c9 | -3.28675 | -53.83521 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfa5c478-c5ae-3056-b443-af45142f2fa2 | -6.66664 | -47.10787 | 2024-11-21 04:31:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df307bb7-91e2-3953-b5e0-8705daad11c1 | -3.61244 | -50.62146 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42c85391-4fb7-33df-b1b3-665dfcbe1d2a | -6.21007 | -46.22092 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 748ce2e5-3de2-315f-b86d-8e1ec8e66784 | -3.87885 | -52.38514 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 119f8868-50a1-3f0d-8792-c4abf7ec2b21 | -3.85092 | -49.44054 | 2024-11-21 04:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bdd19b5-d023-37cd-9271-31757175df8f | -6.20951 | -46.22453 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a92cc73f-cb85-365b-93f2-b7946af21e6b | -5.54361 | -43.90516 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f8b929-127b-3e00-ba1d-9f01411c953b | -4.898 | -48.06715 | 2024-11-21 04:31:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e71b4bac-3677-35f0-8d4a-c2884ec3e98c | -3.1851 | -54.3164 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ae72403-4dbd-3d73-853f-9084d588bac7 | -3.68918 | -50.21946 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b06bc8c7-788d-3270-8692-d202a0bab78f | -3.05372 | -54.40242 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b6c49fd-ce23-34d4-a925-596047307c44 | -3.54683 | -51.43438 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 450b6f17-af2d-3ff6-a1da-3c056a95ee8c | -7.0255 | -47.62466 | 2024-11-21 04:31:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ed5ba1-80b1-3175-b509-aabe2805c2d3 | -4.18026 | -53.58135 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa2a072d-9fd5-3fa0-b0ce-cbc53f4ee8cb | -6.98166 | -39.65623 | 2024-11-21 04:31:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2711f858-79cc-3dec-9d6d-c912097f4418 | -3.77638 | -54.22092 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 270f4a17-7da7-3af9-9129-541101138cb0 | -3.53822 | -54.4874 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42f0d912-fdbe-385d-8f40-ff5272225630 | -3.10374 | -53.75068 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bbb3258-28c1-311a-9dc3-62e3595b7aa3 | -4.12998 | -49.4353 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b25149c-62af-31f3-9bf7-5706c0b3d97d | -4.5738 | -48.01998 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bc94ad30-408e-3844-8855-d0ee2ad9e381 | -4.22522 | -47.18778 | 2024-11-21 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e73bbc7-ea54-3a88-b554-bb1015af5318 | -3.89464 | -50.07383 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f6b487c-093e-344b-b126-287164daf42c | -4.12224 | -53.82398 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23fc1212-56f8-364b-9d1a-2b3d4d0d86f4 | -4.13059 | -49.43153 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b564fa9-2e23-395b-ba3c-fa929c6688ba | -3.36598 | -53.06416 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f59d6c1a-0028-38a6-97b3-de11ff5a421a | -6.20895 | -46.22814 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ae57ced-17dc-3c32-a2f1-9c00b20c0b8d | -4.43147 | -48.29618 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e24d0d8e-26ee-3499-bafd-2e6aba72ff92 | -5.43084 | -45.34466 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa941c3e-c0d8-3098-9128-8aa23e0e14b1 | -3.42799 | -53.28596 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df712fe6-543f-363e-b364-f7f41699f11d | -3.74945 | -50.05196 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c3bc930-7fc2-3643-a326-1ca4281a9753 | -3.46095 | -52.72145 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e954deea-c01e-3cf3-8c17-f0092a42cd75 | -3.29057 | -53.84061 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1092899b-77a6-3dff-a1fa-363a0f418d1b | -6.57444 | -47.86969 | 2024-11-21 04:31:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5d70fc-32d3-3346-a964-46c650f1ebd1 | -3.76237 | -55.57405 | 2024-11-21 04:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1881a535-f08e-3935-b313-c18f5baac53c | -3.80672 | -52.36996 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b438067-9e67-342c-afdc-a20b40b5ae56 | -3.28908 | -53.84996 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d7c7a2b-59e4-3862-8932-6bc542067dfa | -3.28185 | -53.83141 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e4b072e-9a21-3fe6-9481-e297cc2b85ed | -3.6643 | -51.57601 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e76ed532-951a-3f4f-9929-2e762605a353 | -3.28833 | -53.85463 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ce97ed9-48bb-326f-89eb-7e8cf384284e | -5.35869 | -46.86471 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6f2e9d2-62a3-375e-a597-520e654e65dc | -3.38547 | -53.27033 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README46.md)
